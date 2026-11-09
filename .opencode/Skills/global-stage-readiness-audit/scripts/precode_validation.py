"""Readiness gates for the early waitlist and deployment decisions."""

from __future__ import annotations

import re
from collections.abc import Mapping
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from workflow_validation import load_json, validate_schema
from decision_bindings import binding_errors

WAITLIST_PATH = "Build-Plans/Stage-4/10-waitlist-validation.json"
DEPLOYMENT_PATH = "Build-Plans/Stage-3/09-deployment-strategy.json"
WAITLIST_CHECKS = (
    "public_url", "signup_persistence", "success_error_states", "duplicate_handling",
    "spam_protection", "mobile_layout", "accessibility", "measurement",
)


def _public_url(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    try:
        parsed = urlparse(value)
        host = parsed.hostname or ""
    except ValueError:
        return False
    return parsed.scheme in {"http", "https"} and bool(host) and host not in {
        "localhost", "127.0.0.1", "::1",
    } and not host.endswith(".localhost")


def _artifact(root: Path, path: str, schema: str) -> tuple[Mapping[str, Any], list[str]]:
    try:
        document = load_json(root / path)
        errors = validate_schema(document, root / "System-References/Schemas" / schema, root)
    except ValueError as exc:
        return {}, [str(exc)]
    if not isinstance(document, Mapping):
        return {}, [f"{path}: expected an object"]
    return document, [f"{path}: {error}" for error in errors]


def validate_waitlist(root: Path, canonical: Mapping[str, Any]) -> list[str]:
    """Require launch evidence, without imposing a demand threshold."""
    document, errors = _artifact(root, WAITLIST_PATH, "waitlist-validation.schema.json")
    if errors:
        return errors
    expected_ref = WAITLIST_PATH + "#"
    handoff = canonical.get("stage_5_handoff", {})
    if canonical.get("waitlist_validation_ref") != expected_ref or not isinstance(handoff, Mapping) or handoff.get("waitlist_validation_ref") != expected_ref:
        errors.append("Waitlist: UX state and Stage 5 handoff must reference the canonical waitlist artifact")
    deployment_ref = DEPLOYMENT_PATH + "#"
    features_ref = "Build-Plans/Stage-1/05-feature-structure.json#"
    if document["core_features_ref"] != features_ref or not (root / features_ref[:-1]).is_file():
        errors.append("Waitlist: reference the approved Stage 1 core features")
    if document["deployment_strategy_ref"] != deployment_ref or canonical.get("deployment_strategy_ref") != deployment_ref or not isinstance(handoff, Mapping) or handoff.get("deployment_strategy_ref") != deployment_ref:
        errors.append("Waitlist: artifact, UX state, and handoff must reference the approved deployment strategy")
    try:
        planning = load_json(root / "Build-Plans/Build-status/Planning-state.json")
        if not isinstance(planning, Mapping) or planning.get("stage_decision_brief", {}).get("approval_status") != "approved":
            errors.append("Waitlist: core features require Stage 1 approval before page creation")
        architecture = load_json(root / "Build-Plans/Build-status/Architecture-state.json")
        if not isinstance(architecture, Mapping):
            errors.append("Waitlist: approved architecture state is missing")
        else:
            errors.extend(validate_deployment(root, architecture))
        strategy = load_json(root / DEPLOYMENT_PATH)
        errors.extend(binding_errors(root, architecture, strategy, document))
        published_at = datetime.fromisoformat(document["publication"]["published_at"].replace("Z", "+00:00"))
        approved_at = datetime.fromisoformat(strategy["approval"]["approved_at"].replace("Z", "+00:00"))
        if published_at.tzinfo is None or approved_at.tzinfo is None or published_at < approved_at:
            errors.append("Waitlist: publication must follow stack/deployment approval with timezone-aware timestamps")
    except (ValueError, KeyError, TypeError, AttributeError) as exc:
        errors.append(f"Waitlist: approved scope/deployment prerequisites are invalid: {exc}")
    publication = document["publication"]
    if publication["status"] != "published" or not _public_url(publication["url"]) or not publication["published_at"].strip():
        errors.append("Waitlist: a published public URL and publication timestamp are required")
    try:
        registry = load_json(root / "Build-Plans/Build-status/Artifact-evidence-registry.json")
        entries = registry.get("artifacts", []) if isinstance(registry, Mapping) else []
        artifacts = {entry.get("artifact_id"): entry for entry in entries if isinstance(entry, Mapping)}
    except ValueError:
        artifacts = {}
    for name in WAITLIST_CHECKS:
        check = document["verification"][name]
        if check["status"] != "passed" or not check["checked_at"].strip():
            errors.append(f"Waitlist: {name} verification must pass with a timestamp")
        for reference in check["evidence_refs"]:
            entry = artifacts.get(reference, {})
            location = entry.get("path_or_url", "")
            if not isinstance(location, str):
                location = ""
            local = root / location
            # lazy: inspect stored evidence, not the network; the owning skill performs live checks.
            exists = _public_url(location) or (bool(location) and local.is_file())
            if not re.fullmatch(r"ARTIFACT-[A-Za-z0-9._-]+", reference) or entry.get("status") != "verified" or not exists:
                errors.append(f"Waitlist: {name} evidence {reference} is missing, unverified, or has no artifact")
    metrics = document["metrics"]
    if metrics["status"] == "observed":
        visits, signups = metrics["visits"], metrics["completed_signups"]
        expected_rate = signups / visits if visits else 0
        if signups > visits or abs(metrics["conversion_rate"] - expected_rate) > 0.001:
            errors.append("Waitlist: observed conversion metrics are inconsistent")
    elif any(key in metrics for key in ("visits", "completed_signups", "conversion_rate")):
        errors.append("Waitlist: omit unobserved numeric metrics while awaiting evidence")
    return errors


def _unresolved(value: str) -> bool:
    return not value.strip() or bool(re.search(r"\b(tbd|to decide later|depends|optional|or)\b", value, re.IGNORECASE))


def validate_deployment(root: Path, canonical: Mapping[str, Any]) -> list[str]:
    """Require approved selections matching all stack deployment targets."""
    document, errors = _artifact(root, DEPLOYMENT_PATH, "deployment-strategy.schema.json")
    if errors:
        return errors
    expected_ref = DEPLOYMENT_PATH + "#"
    handoff = canonical.get("stage_4_handoff", {})
    stack = canonical.get("selected_stack", {})
    hosting = stack.get("hosting_and_deployment", {}) if isinstance(stack, Mapping) else {}
    if not isinstance(hosting, Mapping):
        hosting = {}
    if canonical.get("deployment_strategy_ref") != expected_ref or hosting.get("deployment_strategy_ref") != expected_ref or not isinstance(handoff, Mapping) or handoff.get("deployment_strategy_ref") != expected_ref:
        errors.append("Deployment: state, stack, and Stage 4 handoff must reference the canonical strategy")
    required = document["required_targets"]
    targets = document["targets"]
    platforms = [target["platform"] for target in targets]
    if len(set(required)) != len(required) or len(set(platforms)) != len(platforms) or set(platforms) != set(required) or canonical.get("deployment_targets") != required:
        errors.append("Deployment: required target coverage must match architecture deployment_targets exactly")
    selected_methods = {}
    for target in targets:
        method = target["method"]
        selected_methods[target["platform"]] = method
        chosen = [item for item in target["alternatives"] if item["disposition"] == "selected"]
        if _unresolved(method) or len(chosen) != 1 or chosen[0]["method"] != method:
            errors.append(f"Deployment: {target['platform']} needs one concrete selected alternative matching its method")
    if hosting.get("target_methods") != selected_methods:
        errors.append("Deployment: selected methods disagree with selected_stack hosting target_methods")
    compatibility = document["stack_compatibility"]
    if compatibility["status"] != "compatible" or compatibility["unresolved_blockers"]:
        errors.append("Deployment: unresolved stack compatibility blockers")
    approval = document["approval"]
    brief = canonical.get("stage_decision_brief", {})
    brief_path = "Build-Plans/Stage-3/00-stage-decision-brief.md"
    if approval["approval_status"] != "approved" or not approval["approved_by"].strip() or not approval["approved_at"].strip() or approval["brief_ref"] != brief_path or not (root / brief_path).is_file() or not isinstance(brief, Mapping) or brief.get("approval_status") != "approved":
        errors.append("Deployment: user approval and the approved Stage 3 decision brief are required")
    errors.extend(binding_errors(root, canonical, document))
    for source in document["sources"]:
        if not _public_url(source["url"]):
            errors.append("Deployment: official research sources require HTTP(S) URLs")
    return errors
