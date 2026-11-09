"""Content fingerprints for approved feature, stack, and deployment decisions."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Mapping

from workflow_validation import load_json

CONTROL_FIELDS = frozenset({
    "$schema", "stage", "status", "artifact_id", "completion_status", "stage_contract_profile",
    "guidance_policy", "schema_validation", "reference_integrity", "risk_acceptance_ledger",
    "revision_loops", "stage_decision_brief", "approval", "assumptions_not_applicable", "risks_not_applicable",
})


def content_hash(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")).hexdigest()


def decision_hashes(root: Path, architecture: Mapping[str, Any], strategy: Mapping[str, Any]) -> dict[str, str]:
    scope = load_json(root / "Build-Plans/Stage-1/05-feature-structure.json")
    if not isinstance(scope, Mapping):
        raise ValueError("Stage 1 feature structure must be an object")
    return {
        "core_features_hash": content_hash({k: v for k, v in scope.items() if k not in CONTROL_FIELDS}),
        "stack_hash": content_hash(architecture.get("selected_stack", {})),
        "strategy_hash": content_hash({k: v for k, v in strategy.items() if k not in CONTROL_FIELDS}),
    }


def binding_errors(root: Path, architecture: Mapping[str, Any], strategy: Mapping[str, Any], waitlist: Mapping[str, Any] | None = None) -> list[str]:
    errors = []
    expected = decision_hashes(root, architecture, strategy)
    planning = load_json(root / "Build-Plans/Build-status/Planning-state.json")
    brief = planning.get("stage_decision_brief", {})
    if brief.get("approval_status") != "approved" or brief.get("core_features_hash") != expected["core_features_hash"]:
        errors.append("Decision hash: approved core-feature scope is missing or changed; reconcile Stage 1 approval")
    scope = load_json(root / "Build-Plans/Stage-1/05-feature-structure.json")
    platforms = scope.get("target_platforms")
    if not isinstance(platforms, list) or not platforms or any(p not in {"web", "ios", "android"} for p in platforms) or len(set(platforms)) != len(platforms) or set(platforms) != set(strategy.get("required_targets", [])):
        errors.append("Deployment platform coverage must match approved Stage 1 target_platforms; omissions require approved scope revision")
    approval = strategy.get("approval", {})
    for key, digest in expected.items():
        if approval.get(key) != digest:
            errors.append(f"Decision hash: deployment approval has missing or stale {key}")
        if waitlist is not None and waitlist.get("approved_decisions", {}).get(key) != digest:
            errors.append(f"Decision hash: waitlist requires reconciliation of {key}")
    return errors
