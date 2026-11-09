"""Stage-specific readiness controls shared by the global audit.

lazy: use existing contracts and stdlib helpers; add a policy engine only if
projects require policy expressions beyond explicit outputs/layers/approvals.
"""
from __future__ import annotations

import importlib.util
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence
from urllib.parse import urlparse

from workflow_validation import load_json, resolve_json_pointer, validate_schema

WAITLIST_REF = "Build-Plans/Stage-4/10-waitlist-validation.json#"
DEPLOYMENT_REF = "Build-Plans/Stage-3/09-deployment-strategy.json#"
PROOF_FIELDS = (
    "production_build_artifact", "deployment_dry_run_result", "smoke_test_results",
    "rollback_test_result", "environment_verification", "monitoring_alert_test",
)
CONFIDENCE_MINIMUMS = {"market": .70, "technical": .75, "business": .65, "operational": .70, "architecture_readiness": .75}


def object_file(root: Path, relative: str) -> Mapping[str, Any]:
    value = load_json(root / relative)
    if not isinstance(value, Mapping):
        raise ValueError(f"{relative}: expected an object")
    return value


def walk_values(value: Any, key: str) -> list[Any]:
    if isinstance(value, Mapping):
        return ([value[key]] if key in value else []) + [v for child in value.values() for v in walk_values(child, key)]
    if isinstance(value, list):
        return [v for child in value for v in walk_values(child, key)]
    return []


def references_exist(root: Path, refs: Any) -> bool:
    if not isinstance(refs, list) or not refs or any(not isinstance(ref, str) or not ref.strip() for ref in refs):
        return False
    for ref in refs:
        path, separator, pointer = ref.partition("#")
        if separator:
            try:
                resolve_json_pointer(load_json(root / path), pointer)
            except ValueError:
                return False
        elif not (root / path).is_file():
            return False
    return True


def risk_exception(root: Path, reference: Any, stage: int) -> bool:
    if not isinstance(reference, str) or not reference:
        return False
    ledger = object_file(root, "Build-Plans/Build-status/Risk-acceptance-ledger.json")
    for entry in ledger.get("accepted_risks", []):
        if not isinstance(entry, Mapping) or entry.get("risk_id") != reference:
            continue
        authority = entry.get("acceptance_authority")
        if entry.get("status") not in {"active", "accepted"} or entry.get("source_stage") != f"Stage {stage}":
            return False
        if authority not in {"user", "delegated_policy"} or not all(entry.get(k) for k in ("accepted_by", "acceptance_reason", "mitigation")):
            return False
        if not references_exist(root, [entry.get("approval_ref")]):
            return False
        if authority == "delegated_policy" and not references_exist(root, [entry.get("delegated_policy_ref")]):
            return False
        expiration = entry.get("expires_or_recheck_at")
        if expiration:
            try:
                expiry = datetime.fromisoformat(expiration.replace("Z", "+00:00"))
                if expiry.tzinfo is None or expiry <= datetime.now(timezone.utc):
                    return False
            except (ValueError, TypeError, AttributeError):
                return False
        return True
    return False


def evidence_errors(root: Path, refs: Any, label: str) -> list[str]:
    if not isinstance(refs, list) or not refs:
        return [f"{label}: verified artifact evidence_refs are required"]
    registry = object_file(root, "Build-Plans/Build-status/Artifact-evidence-registry.json")
    entries = registry.get("artifacts", [])
    if not isinstance(entries, list) or any(not isinstance(entry, Mapping) for entry in entries):
        return [f"{label}: malformed artifact registry"]
    by_id = {entry.get("artifact_id"): entry for entry in entries}
    errors = []
    for reference in refs:
        entry = by_id.get(reference, {}) if isinstance(reference, str) else {}
        location = entry.get("path_or_url", "")
        valid_location = False
        if isinstance(location, str) and location.strip():
            parsed = urlparse(location)
            if parsed.scheme in {"http", "https"} and parsed.hostname:
                valid_location = True
            elif (root / location).is_file():
                try:
                    valid_location = bool((root / location).read_bytes())
                except OSError:
                    pass
        if not isinstance(reference, str) or not re.fullmatch(r"ARTIFACT-[A-Za-z0-9._-]+", reference) or entry.get("status") != "verified" or not valid_location:
            errors.append(f"{label}: evidence {reference!r} is missing, unverified, or unreadable")
    return errors


def evaluate_profile(root: Path, stage: int, canonical: Mapping[str, Any]) -> tuple[list[str], dict[str, Any]]:
    profile = canonical.get("stage_contract_profile", {})
    errors = []
    if not isinstance(profile, Mapping) or not isinstance(profile.get("profile_id"), str) or not profile["profile_id"].strip():
        profile = {}; errors.append("Profile: active profile_id is missing")
    lists = ("required_outputs", "required_validation_layers", "approval_gates", "optional_outputs", "skip_allowed_outputs")
    for key in lists:
        values = profile.get(key, [])
        if not isinstance(values, list) or any(not isinstance(v, str) or not v.strip() for v in values):
            errors.append(f"Profile: {key} must contain explicit nonempty strings")
    for output in profile.get("required_outputs", []) if isinstance(profile.get("required_outputs", []), list) else []:
        if not isinstance(output, str):
            continue
        path = root / output if output.startswith("Build-Plans/") else root / f"Build-Plans/Stage-{stage}" / output
        if not path.resolve().is_relative_to(root.resolve()) or not path.is_file():
            errors.append(f"Profile: required output missing: {output}")
    layers = {
        "schema_validation": set(range(1, 9)), "reference_integrity": set(range(1, 9)),
        "research_evidence": {2}, "deployment_strategy": {3}, "waitlist_validation": {4},
        "page_specifications": {4}, "normalized_handoff": {5}, "workflow_outcomes": {6, 7},
        "deployment_proof": {7}, "visual_qa": {6, 7}, "feedback_routes": {8},
    }
    for layer in profile.get("required_validation_layers", []) if isinstance(profile.get("required_validation_layers", []), list) else []:
        if not isinstance(layer, str) or stage not in layers.get(layer, set()):
            errors.append(f"Profile: unsupported validation layer for Stage {stage}: {layer}")
    for pointer in profile.get("approval_gates", []) if isinstance(profile.get("approval_gates", []), list) else []:
        try:
            approval = resolve_json_pointer(canonical, pointer)
            if not isinstance(approval, Mapping) or approval.get("approval_status") != "approved":
                raise ValueError("approval required")
        except (ValueError, TypeError):
            errors.append(f"Profile: required approval gate is not approved: {pointer}")
    # Unknown control fields must not silently appear to have been evaluated.
    known = set(lists) | {"profile_id", "profile_name", "app_type", "complexity_level", "guidance_depth", "required_stage_depth", "requirements_checked"}
    for key in profile:
        if key not in known:
            errors.append(f"Profile: unsupported policy field {key}")
    depth = profile.get("required_stage_depth", {})
    if not isinstance(depth, Mapping) or any(key not in {f"stage_{n}" for n in range(1, 9)} or not isinstance(value, str) or value not in {"minimal", "standard", "detailed", "exhaustive"} for key, value in depth.items()):
        errors.append("Profile: unsupported required_stage_depth; use explicit validation layers for executable depth")
    if isinstance(depth, Mapping) and depth.get(f"stage_{stage}") in ("detailed", "exhaustive") and not profile.get("required_validation_layers"):
        errors.append("Profile: detailed/exhaustive depth requires explicit executable validation layers")
    return errors, {"profile_id": profile.get("profile_id", ""), "profile_requirements_checked": True, "missing_profile_requirements": errors}


def research_errors(root: Path, state: Mapping[str, Any]) -> list[str]:
    errors = []
    assumptions = state.get("assumption_registry")
    scores = state.get("confidence_scores", {})
    exception = risk_exception(root, state.get("research_accepted_risk_ref"), 2)
    if not isinstance(assumptions, list) or not assumptions:
        errors.append("Research: nonempty assumption_registry is required")
        assumptions = []
    for name, minimum in CONFIDENCE_MINIMUMS.items():
        score = scores.get(name) if isinstance(scores, Mapping) else None
        if not isinstance(score, (int, float)) or isinstance(score, bool) or not minimum <= score <= 1:
            if not exception:
                errors.append(f"Research: {name} confidence must be at least {minimum}")
    for assumption in assumptions:
        if not isinstance(assumption, Mapping) or not assumption.get("id") or not assumption.get("assumption"):
            errors.append("Research: malformed assumption_registry entry"); continue
        evidence = assumption.get("evidence", [])
        critical = assumption.get("architecture_critical") is True
        accepted = risk_exception(root, assumption.get("accepted_risk_ref"), 2)
        quality = assumption.get("evidence_quality")
        score = assumption.get("confidence")
        if quality not in {"none", "low", "medium", "high"} or not isinstance(score, (int, float)) or isinstance(score, bool) or not 0 <= score <= 1:
            errors.append(f"Research: invalid confidence or evidence quality for {assumption['id']}")
        elif score > {"none": .35, "low": .55, "medium": .75, "high": 1}[quality] and not accepted:
            errors.append(f"Research: confidence exceeds evidence quality for {assumption['id']}")
        if assumption.get("status") == "validated" and isinstance(score, (int, float)) and score < .75 and not accepted:
            errors.append(f"Research: validated assumption confidence must be at least .75: {assumption['id']}")
        if assumption.get("status") == "validated" or critical:
            valid = isinstance(evidence, list) and bool(evidence) and all(
                isinstance(item, Mapping) and item.get("source_type") in {"primary", "secondary", "user_provided"}
                and item.get("evidence_quality") in {"medium", "high"} and item.get("summary")
                and item.get("source_date") and item.get("freshness") in {"current", "recent"}
                and item.get("is_inference") is False and (
                    (isinstance(item.get("source_url"), str) and urlparse(item["source_url"]).scheme in {"https", "http"} and urlparse(item["source_url"]).hostname)
                    or (item.get("artifact_refs") and not evidence_errors(root, item["artifact_refs"], "Research"))
                )
                for item in evidence
            )
            if (not valid or quality not in {"medium", "high"} or assumption.get("status") != "validated") and not accepted:
                errors.append(f"Research: architecture-critical/validated assumption lacks sufficient evidence: {assumption['id']}")
    for key in ("critical_unknowns", "contradictions"):
        entries = state.get(key, [])
        if not isinstance(entries, list):
            errors.append(f"Research: {key} must be an array"); continue
        for record in entries:
            unresolved = not isinstance(record, Mapping) or record.get("status") not in {"resolved", "mitigated"}
            critical = key == "critical_unknowns" or not isinstance(record, Mapping) or record.get("severity") == "critical"
            if unresolved and critical:
                errors.append(f"Research: unresolved critical {key}")
    return errors


def stage5_module() -> Any:
    # lazy: load the existing sibling contract by path; avoid copying its rules or packaging the harness.
    path = Path(__file__).resolve().parents[2] / "stage-5-development-orchestration/scripts/stage5_contract.py"
    spec = importlib.util.spec_from_file_location("genesis_stage5_contract", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    return module


def stage5_errors(root: Path, documents: Mapping[str, Any]) -> list[str]:
    module = stage5_module()
    folder = "Build-Plans/Stage-5/"
    context = documents.get(folder + "00-stage-context.json", {})
    manifest = documents.get(folder + "09-stage-manifest.json", {})
    normalized = any(isinstance(doc, Mapping) and doc.get("format_version") == "2.0" for name, doc in documents.items() if name.startswith(folder))
    if not normalized:
        return ["Stage 5: active readiness requires a normalized v2 package; archived self-contained input remains read-only via the compatibility resolver"]
    errors = []
    try:
        if context.get("format_version") != "2.0" or manifest.get("format_version") != "2.0" or manifest.get("context_ref") != module.CONTEXT_PATH:
            raise ValueError("manifest/context must be complete normalized v2")
        artifacts = [object_file(root, folder + definition["filename"]) for definition in module.ARTIFACTS.values()]
        module.validate_artifact_set(artifacts)
        for document, schema in [(context, "stage-5-context.schema.json"), (manifest, "stage-5-manifest.schema.json")] + [(item, "stage-5-artifact.schema.json") for item in artifacts]:
            schema_errors = validate_schema(document, root / "System-References/Schemas" / schema, root)
            if schema_errors:
                raise ValueError("manifest/package schema: " + "; ".join(schema_errors))
        index = manifest.get("artifacts", [])
        if len(index) != 8 or len({item.get("artifact_type") for item in index}) != 8:
            raise ValueError("manifest must index exactly eight unique types")
        for item in index:
            definition = module.ARTIFACTS.get(item.get("artifact_type"))
            if not definition or any(item.get(key) != expected for key, expected in {
                "path": folder + definition["filename"], "artifact_id": definition["artifact_id"],
                "schema_ref": definition["schema"], "data_path": "/data/" + definition["data_key"],
            }.items()):
                raise ValueError("manifest index path, ID, schema, or data pointer disagrees with its artifact")
        if manifest.get("schema_validation", {}).get("validation_executed") is not True or manifest.get("schema_validation", {}).get("schemas_valid") is not True:
            raise ValueError("manifest requires executed successful schema validation")
        data = {item["artifact_type"]: item["data"] for item in artifacts}
        tickets = data["build_tickets"]["tickets"]
        agents = data["agent_assignment_plan"]["agents"]
        batches = data["parallel_execution_plan"]["batches"]
        upstream = {name: doc for name, doc in documents.items() if any(name.startswith(f"Build-Plans/Stage-{s}/") for s in range(1, 5))}
        module.validate_ticket_references(tickets, repository_root=root, source_documents=upstream)
        module.validate_risk_refs(tickets + agents + batches, [item["risk_id"] for item in context.get("risks", [])])
        module.validate_agent_scopes(agents, tickets)
        module.validate_execution_waves(batches, tickets)
        module.validate_workflow_completion_definitions(tickets)
        errors.extend(continuity_errors(root, context, manifest.get("stage_6_handoff", {})))
    except (ValueError, KeyError, TypeError, AttributeError) as exc:
        errors.append(f"Stage 5 manifest/package: {exc}")
    return errors


def continuity_errors(root: Path, canonical: Mapping[str, Any], handoff: Any) -> list[str]:
    errors = []
    for key, expected in (("waitlist_validation_ref", WAITLIST_REF), ("deployment_strategy_ref", DEPLOYMENT_REF)):
        if canonical.get(key) != expected or not isinstance(handoff, Mapping) or handoff.get(key) != expected or not references_exist(root, [expected]):
            errors.append(f"Handoff: canonical {key} and outgoing reference must resolve to {expected}")
    return errors


def outcome_errors(root: Path, stage: int, current: Mapping[str, Any], all_documents: Mapping[str, Any]) -> tuple[list[str], list[str]]:
    errors = []
    required = set()
    for values in walk_values(all_documents, "launch_critical_workflow_ids"):
        if not isinstance(values, list) or any(not isinstance(item, str) or not item for item in values):
            errors.append("Workflow: launch_critical_workflow_ids must contain stable IDs")
        else:
            required.update(values)
    records = [record for values in walk_values(current, "workflow_evidence") if isinstance(values, list) for record in values]
    module = stage5_module()
    try:
        module.validate_workflow_evidence(records, launch_critical_workflow_ids=required)
    except (ValueError, KeyError, TypeError, AttributeError) as exc:
        errors.append(f"Workflow: {exc}")
    for record in records:
        if not isinstance(record, Mapping):
            errors.append("Workflow: evidence record must be an object"); continue
        status = record.get("status")
        if status in {"runtime_persistence_failed", "blocked"}:
            errors.append(f"Workflow: failed outcome for {record.get('workflow_id')}")
        elif status == "deferred_with_approval":
            if not risk_exception(root, record.get("accepted_risk_ref"), stage):
                errors.append("Workflow: deferral requires a valid stage-scoped accepted risk")
        elif status in {"local_e2e_passed", "staging_e2e_passed"}:
            errors.extend(evidence_errors(root, record.get("evidence_refs"), "Workflow"))
    ids = [record.get("workflow_id") for record in records if isinstance(record, Mapping)]
    if len(ids) != len(set(ids)):
        errors.append("Workflow: duplicate outcome records")
    if required:
        for key in ("dead_control_validation", "runtime_data_source_validation"):
            checks = walk_values(current, key)
            if not checks or any(not isinstance(check, Mapping) or check.get("checked") is not True for check in checks):
                errors.append(f"Workflow: {key} must be checked")
    return errors, sorted(required)


def launch_errors(root: Path, canonical: Mapping[str, Any]) -> list[str]:
    proof = canonical.get("deployment_proof", {})
    if not isinstance(proof, Mapping):
        return ["Launch: deployment_proof must be an object"]
    errors = []
    for field in PROOF_FIELDS:
        record = proof.get(field, {})
        if isinstance(record, Mapping) and record.get("status") == "deferred_with_approval" and risk_exception(root, record.get("accepted_risk_ref"), 7):
            continue
        if not isinstance(record, Mapping) or record.get("status") != "passed":
            errors.append(f"Launch: {field} requires a passed result"); continue
        errors.extend(evidence_errors(root, record.get("evidence_refs"), f"Launch {field}"))
    if proof.get("release_blockers") or canonical.get("release_blockers"):
        errors.append("Launch: unresolved release_blockers")
    return errors


def visual_errors(root: Path, stage: int, current: Mapping[str, Any], required: bool) -> list[str]:
    records = walk_values(current, "visual_qa")
    if not required and not records:
        return []
    if not records:
        return ["Visual QA: a passed visual_qa result is required"]
    errors = []
    for record in records:
        if isinstance(record, Mapping) and record.get("status") == "deferred_with_approval" and stage == 7 and risk_exception(root, record.get("accepted_risk_ref"), 7):
            continue
        if not isinstance(record, Mapping) or record.get("status") != "passed" or record.get("responsive_validation") != "passed" or record.get("design_system_compliance") != "passed" or record.get("unresolved_failures"):
            errors.append("Visual QA: responsive/design-system checks and all required outcomes must pass")
        else:
            errors.extend(evidence_errors(root, record.get("evidence_refs"), "Visual QA"))
    return errors


def feedback_errors(root: Path, routes: Any) -> tuple[list[str], dict[str, Any]]:
    errors = []
    checked, owners, actions, evidence = [], [], [], []
    creates_cycle = False
    if not isinstance(routes, list) or not routes:
        errors.append("Feedback: prior_stage_feedback requires at least one explicit route")
        routes = []
    for i, route in enumerate(routes):
        if not isinstance(route, Mapping):
            errors.append(f"Feedback: malformed route {i}"); continue
        identifier = route.get("feedback_route_id", f"route-{i}")
        if not isinstance(identifier, str):
            identifier = f"route-{i}"
            errors.append(f"Feedback: invalid route ID at index {i}")
        # Preserve evaluated fields in a schema-valid failed audit even when source data is malformed.
        array_fields = {"source_signal_ids", "ui_element_refs", "route_refs", "action_refs", "stage_5_ticket_refs", "stage_6_validation_refs", "evidence_refs"}
        boolean_fields = {"blocks_current_evolution", "creates_new_stage_cycle"}
        string_fields = {"feedback_route_id", "finding", "recommended_target_stage", "owner", "severity", "recommended_action"}
        checked.append({key: value for key, value in route.items() if (key in array_fields and isinstance(value, list)) or (key in boolean_fields and isinstance(value, bool)) or (key in string_fields and isinstance(value, str))})
        if not isinstance(route.get("owner"), str) or not route["owner"].strip(): owners.append(identifier)
        if not isinstance(route.get("recommended_action"), str) or not route["recommended_action"].strip(): actions.append(identifier)
        if route.get("severity", "low") not in ("low", "medium", "high", "critical"):
            errors.append(f"Feedback: invalid severity for {identifier}")
        target = route.get("recommended_target_stage")
        if not isinstance(target, str) or target not in {f"Stage {n}" for n in range(1, 9)}:
            errors.append(f"Feedback: invalid target stage for {identifier}: {target}")
        if route.get("creates_new_stage_cycle") is True:
            creates_cycle = True
        elif route.get("creates_new_stage_cycle") not in (False, None):
            errors.append(f"Feedback: invalid cycle flag for {identifier}")
        if route.get("severity") in ("high", "critical"):
            missing = evidence_errors(root, route.get("evidence_refs"), f"Feedback {identifier}")
            if missing: evidence.append(identifier); errors.extend(missing)
        domain = route.get("issue_domain")
        routing = {"product": 1, "assumptions": 2, "architecture": 3, "ux": 4, "planning": 5, "implementation": 6, "deployment": 7, "telemetry": 8}
        if domain is not None and (not isinstance(domain, str) or domain not in routing or target != f"Stage {routing[domain]}"):
            errors.append(f"Feedback: issue_domain and target disagree for {identifier}")
    errors.extend(f"Feedback: missing owner for {item}" for item in owners)
    errors.extend(f"Feedback: missing recommended_action for {item}" for item in actions)
    return errors, {"required": True, "routes_checked": checked, "missing_route_owners": owners, "missing_route_actions": actions, "missing_route_evidence": evidence, "critical_routes_blocking": errors, "creates_new_stage_cycle": creates_cycle}
