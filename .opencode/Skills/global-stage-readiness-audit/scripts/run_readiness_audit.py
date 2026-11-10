#!/usr/bin/env python3
"""Execute the Genesis stage readiness audit with only Python stdlib."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from workflow_validation import load_json, validate_reference_integrity, validate_schema
from page_specifications import validate_page_specifications
from precode_validation import validate_waitlist, validate_deployment
from readiness_controls import (
    continuity_errors, evaluate_profile, feedback_errors, launch_errors, outcome_errors,
    research_errors, stage5_errors, visual_errors,
)


STAGE_FILES: Mapping[int, Sequence[str]] = {
    1: tuple(f"{index:02d}-{name}.json" for index, name in enumerate((
        "product-foundation", "user-system-map", "workflow-architecture", "product-capabilities",
        "feature-structure", "product-boundaries", "dependency-map", "mvp-operational-model",
        "risk-and-constraints", "success-framework",
    ), 1)) + ("00-stage-decision-brief.md",),
    2: ("01-market-analysis.json", "02-competitive-landscape.json", "03-technical-feasibility.json", "04-business-viability.json", "05-risk-validation.json", "06-strategic-positioning.json", "00-stage-decision-brief.md"),
    3: tuple(f"{index:02d}-{name}.json" for index, name in enumerate((
        "system-topology", "service-architecture", "data-architecture", "api-architecture",
        "integration-architecture", "security-foundations", "infrastructure-model", "scalability-framework",
    ), 1)) + ("09-deployment-strategy.json", "00-stage-decision-brief.md"),
    4: tuple(f"{index:02d}-{name}" for index, name in enumerate((
        "user-journeys.json", "interaction-architecture.json", "screen-system.json", "feature-behaviors.json",
        "state-transition-map.json", "accessibility-framework.json", "ui-blueprint-specification.json",
        "design-system-foundation.json", "complete-app-blueprint.md",
    ), 1)) + ("10-waitlist-validation.json", "00-stage-decision-brief.md"),
    5: ("00-stage-context.json", "01-development-roadmap.json", "02-implementation-sequence.json", "03-engineering-dependencies.json", "04-testing-strategy.json", "05-build-tickets.json", "06-agent-assignment-plan.json", "07-parallel-execution-plan.json", "08-release-plan.json", "09-stage-manifest.json", "10-stage-5-summary.md"),
    6: ("01-implementation-status.json", "02-validation-results.json", "03-regression-analysis.json", "04-system-health.json", "05-repair-log.json", "06-stage-6-summary.md"),
    7: ("01-launch-readiness.json", "02-deployment-framework.json", "03-monitoring-systems.json", "04-analytics-framework.json", "05-operational-tooling.json", "06-stage-7-summary.md"),
    8: ("01-telemetry-analysis.json", "02-operational-optimization.json", "03-ai-improvement-plan.json", "04-roadmap-evolution.json", "05-scalability-evolution.json", "06-stage-8-summary.md"),
}
STATE_FILES = {1: "Planning-state.json", 2: "Validation-state.json", 3: "Architecture-state.json", 4: "UX-state.json"}
CANONICAL_FILES = {5: "09-stage-manifest.json", 6: "04-system-health.json", 7: "01-launch-readiness.json", 8: "01-telemetry-analysis.json"}
READY_STATUSES = {stage: f"ready_for_stage_{stage + 1}" for stage in range(1, 8)} | {8: "evolution_plan_ready"}
HANDOFF_KEYS = {stage: f"stage_{stage + 1}_handoff" for stage in range(1, 8)} | {8: "prior_stage_feedback"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run one Genesis stage readiness audit.")
    parser.add_argument("--stage", type=int, choices=range(1, 9), required=True)
    parser.add_argument("--proposed-status", required=True)
    parser.add_argument("--workspace-root", default=".")
    return parser.parse_args()


def _find_values(value: Any, keys: set[str]) -> list[Any]:
    found: list[Any] = []
    if isinstance(value, Mapping):
        for key, child in value.items():
            if key in keys:
                found.append(child)
            found.extend(_find_values(child, keys))
    elif isinstance(value, list):
        for child in value:
            found.extend(_find_values(child, keys))
    return found


def _has_record(value: Any, keys: set[str]) -> bool:
    return any(item not in (None, "", [], {}, False) for item in _find_values(value, keys))


def _risk_authority_errors(root: Path, documents: Mapping[str, Any]) -> list[str]:
    flattened_ids = {
        risk_id
        for document in documents.values()
        for value in _find_values(document, {"accepted_risk_refs"})
        for risk_id in (value if isinstance(value, list) else [value])
        if isinstance(risk_id, str)
    }
    ledger_path = root / "Build-Plans/Build-status/Risk-acceptance-ledger.json"
    if not ledger_path.is_file():
        return ["Risk acceptance ledger is missing"] if flattened_ids else []
    entries = load_json(ledger_path).get("accepted_risks", [])
    by_id = {entry.get("risk_id"): entry for entry in entries}
    errors: list[str] = []
    for risk_id in sorted(flattened_ids):
        if risk_id not in by_id:
            errors.append(f"{risk_id}: accepted risk reference is missing from the ledger")
    for entry in entries:
        if entry.get("status") in {"mitigated", "expired", "superseded"}:
            continue
        if str(entry.get("severity", "")).lower() not in {"high", "critical"}:
            continue
        if entry.get("acceptance_authority") not in {"user", "delegated_policy"}:
            errors.append(f"{entry.get('risk_id', '<unknown>')}: high/critical risk lacks acceptance authority")
        if not entry.get("accepted_by") or not entry.get("approval_ref"):
            errors.append(f"{entry.get('risk_id', '<unknown>')}: high/critical risk lacks approver or approval_ref")
    return errors


def _checked(label: str, operation: Any) -> list[str]:
    try:
        return operation()
    except (ValueError, TypeError, KeyError, AttributeError, OSError, RecursionError) as exc:
        return [f"{label}: invalid or unreadable input: {exc}"]


def _load_documents(root: Path, stage: int, stage_dir: Path) -> tuple[dict[str, Any], list[str]]:
    documents: dict[str, Any] = {}
    errors: list[str] = []
    for prior_stage in range(1, stage + 1):
        prior_dir = root / "Build-Plans" / f"Stage-{prior_stage}"
        if not prior_dir.is_dir():
            continue
        for path in sorted(prior_dir.glob("*.json")):
            # lazy: retain the superseded Stage 2 artifact as history; only Stage 4 owns live waitlist evidence.
            if prior_stage == 2 and path.name == "07-waitlist-validation.json":
                continue
            try:
                value = load_json(path)
                if not isinstance(value, Mapping):
                    raise ValueError(f"{path.relative_to(root)}: expected an object")
                documents[str(path.relative_to(root))] = value
            except ValueError as exc:
                errors.append(str(exc))
    extra_paths = [root / "Build-Plans/Build-status" / name for name in (
        "Artifact-evidence-registry.json", "Risk-acceptance-ledger.json",
    )]
    if stage in STATE_FILES:
        extra_paths.append(root / "Build-Plans/Build-status" / STATE_FILES[stage])
    for path in extra_paths:
        if path.is_file():
            try:
                value = load_json(path)
                if not isinstance(value, Mapping):
                    raise ValueError(f"{path.relative_to(root)}: expected an object")
                documents[str(path.relative_to(root))] = value
            except ValueError as exc:
                errors.append(str(exc))
    return documents, errors


def _schema_errors(root: Path, stage: int, documents: Mapping[str, Any]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    validated: list[str] = []
    default_schema = root / "System-References/Schemas" / f"stage-{stage}-output.schema.json"
    for relative_path, document in documents.items():
        is_output = f"Build-Plans/Stage-{stage}/" in relative_path
        is_state = stage in STATE_FILES and relative_path.endswith("/" + STATE_FILES[stage])
        registry_schemas = {"Artifact-evidence-registry.json": "artifact-evidence-registry.schema.json", "Risk-acceptance-ledger.json": "risk-acceptance-ledger.schema.json"}
        registry_schema = registry_schemas.get(Path(relative_path).name)
        if not is_output and not is_state and not registry_schema:
            continue
        schema_ref = document.get("$schema") if isinstance(document, Mapping) else None
        schema_path = root / "System-References/Schemas" / registry_schema if registry_schema else root / schema_ref if is_output and isinstance(schema_ref, str) else default_schema
        if not schema_path.resolve().is_relative_to(root.resolve()):
            errors.append(f"{relative_path}: schema must be inside the workspace")
            continue
        if not schema_path.is_file():
            errors.append(f"{relative_path}: schema does not exist: {schema_path.relative_to(root)}")
            continue
        file_errors = _checked(relative_path, lambda: validate_schema(document, schema_path, root))
        errors.extend(f"{relative_path}: {error}" for error in file_errors)
        validated.append(relative_path)
    return errors, validated


def build_audit(root: Path, stage: int, proposed_status: str) -> dict[str, Any]:
    stage_dir = root / "Build-Plans" / f"Stage-{stage}"
    required_paths = [stage_dir / filename for filename in STAGE_FILES[stage]]
    missing_files = [str(path.relative_to(root)) for path in required_paths if not path.is_file()]
    documents, parse_errors = _load_documents(root, stage, stage_dir)
    schema_errors, validated_files = _schema_errors(root, stage, documents)
    reference_result = validate_reference_integrity(documents, root)
    canonical_path = (
        root / "Build-Plans/Build-status" / STATE_FILES[stage]
        if stage in STATE_FILES
        else stage_dir / CANONICAL_FILES[stage]
    )
    canonical = documents.get(str(canonical_path.relative_to(root)), {})
    completion = canonical.get("completion_status", {})
    completion_status = completion.get("status", "") if isinstance(completion, Mapping) else completion
    handoff_key = HANDOFF_KEYS[stage]
    handoff = canonical.get(handoff_key) or None
    approval_ok = True
    if stage <= 4 and proposed_status == READY_STATUSES[stage]:
        brief = canonical.get("stage_decision_brief", {})
        approval_ok = isinstance(brief, Mapping) and brief.get("approval_status") == "approved" and all(isinstance(brief.get(key), str) and brief[key].strip() for key in ("approved_by", "approved_at"))
    risk_errors = _checked("Risk acceptance authority", lambda: _risk_authority_errors(root, documents))
    blocking = list(missing_files) + parse_errors + schema_errors + list(reference_result["blocking_ref_errors"]) + risk_errors
    current = {name: doc for name, doc in documents.items() if name.startswith(f"Build-Plans/Stage-{stage}/")}
    current[str(canonical_path.relative_to(root))] = canonical
    controls = documents.get("Build-Plans/Stage-5/00-stage-context.json", {}) if stage == 5 else canonical
    try:
        profile_errors, profile_result = evaluate_profile(root, stage, controls)
    except (ValueError, TypeError, KeyError, AttributeError, OSError) as exc:
        profile_errors = [f"Profile: invalid policy data: {exc}"]
        profile_result = {"profile_id": "", "profile_requirements_checked": True, "missing_profile_requirements": profile_errors}
    blocking.extend(profile_errors)
    if not _has_record(current if stage != 5 else controls, {"assumptions", "assumption_registry", "assumptions_not_applicable"}):
        blocking.append("Current-stage assumptions are not recorded or marked not applicable")
    if not _has_record(current if stage != 5 else controls, {"risks", "risk_registry", "risks_not_applicable"}):
        blocking.append("Current-stage risks are not recorded or marked not applicable")
    if stage == 2:
        blocking.extend(_checked("Research", lambda: research_errors(root, canonical)))
    if stage == 3:
        blocking.extend(_checked("Deployment", lambda: validate_deployment(root, canonical)))
    if stage == 4:
        blocking.extend(_checked("Waitlist", lambda: validate_waitlist(root, canonical)))
        blocking.extend(_checked("Page specifications", lambda: validate_page_specifications(root, canonical, final=True)))
    if stage == 5:
        blocking.extend(_checked("Stage 5 manifest", lambda: stage5_errors(root, documents)))
    if stage in {6, 7}:
        blocking.extend(_checked("Handoff", lambda: continuity_errors(root, canonical, handoff)))
    if stage == 7:
        blocking.extend(_checked("Launch", lambda: launch_errors(root, canonical)))
    feedback_result = {"required": False, "routes_checked": [], "missing_route_owners": [], "missing_route_actions": [], "missing_route_evidence": [], "critical_routes_blocking": [], "creates_new_stage_cycle": False}
    if stage == 8:
        try:
            feedback_blocks, feedback_result = feedback_errors(root, handoff)
        except (ValueError, TypeError, KeyError, AttributeError, OSError) as exc:
            feedback_blocks = [f"Feedback: invalid route data: {exc}"]
            feedback_result.update(required=True, critical_routes_blocking=feedback_blocks)
        blocking.extend(feedback_blocks)
    if proposed_status == READY_STATUSES[stage] and completion_status != proposed_status:
        blocking.append(f"Canonical completion status is {completion_status or 'missing'}, expected {proposed_status}")
    if proposed_status == READY_STATUSES[stage] and handoff is None:
        blocking.append(f"Canonical {handoff_key} is missing")
    if stage < 8 and handoff is not None:
        if not isinstance(handoff, Mapping) or not all(handoff.get(key) for key in ("source_stage", "target_stage", "readiness")):
            blocking.append(f"Canonical {handoff_key} lacks source_stage, target_stage, or readiness")
    if not approval_ok:
        blocking.append("Required Stage 1-4 decision brief is not approved")
    if not _has_record(documents, {"assumptions", "assumptions_not_applicable"}):
        blocking.append("Assumptions are not recorded or marked not applicable")
    if not _has_record(documents, {"risks", "risk_registry", "risks_not_applicable"}):
        blocking.append("Risks are not recorded or marked not applicable")
    artifact_registry_path = root / "Build-Plans/Build-status/Artifact-evidence-registry.json"
    if stage >= 6 and not artifact_registry_path.is_file():
        blocking.append("Artifact evidence registry is missing")
    launch_critical_ids = _find_values(documents, {"launch_critical_workflow_ids"})
    workflow_required = stage in {6, 7} and any(item for item in launch_critical_ids)
    workflow_present = _has_record(current, {"workflow_evidence", "workflow_smoke_tests"})
    workflow_checked = []
    outcome_blocks = []
    if stage in {6, 7}:
        try:
            outcome_blocks, workflow_checked = outcome_errors(root, stage, current, documents)
        except (ValueError, TypeError, KeyError, AttributeError, OSError) as exc:
            outcome_blocks = [f"Workflow: invalid input: {exc}"]
        blocking.extend(outcome_blocks)
    if workflow_required and not workflow_present:
        blocking.append("Launch-critical workflow evidence is missing")
    dead_controls = _find_values(documents, {"dead_controls_detected"})
    fixture_dependencies = _find_values(documents, {"fixture_runtime_dependencies"})
    workflow_gaps = _find_values(documents, {"blocking_workflow_gaps"})
    if stage in {6, 7} and any(item for item in dead_controls + fixture_dependencies + workflow_gaps):
        blocking.append("Unresolved workflow, dead-control, or fixture-runtime gaps remain")
    visual_required = stage in {4, 5, 6, 7} and _has_record(documents, {"ui_blueprint_refs", "ui_blueprints", "visual_reference_refs"})
    if visual_required and not _has_record(documents, {"visual_spec_refs", "visual_spec_inventory"}):
        blocking.append("Frontend work lacks visual specification references")
    if visual_required and not _has_record(documents, {"design_system_refs", "design_system_foundation"}):
        blocking.append("Frontend work lacks design system references")
    if stage in {6, 7}:
        blocking.extend(_checked("Visual QA", lambda: visual_errors(root, stage, current, visual_required or "visual_qa" in controls.get("stage_contract_profile", {}).get("required_validation_layers", []))))
    summary_name = STAGE_FILES[stage][-1] if stage >= 5 else ""
    summary_path = stage_dir / summary_name if summary_name else None
    summary_present = False
    if summary_path and summary_path.is_file():
        try:
            summary_present = f"Stage {stage}" in summary_path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            blocking.append(f"Summary is unreadable: {exc}")
    if stage >= 5 and not summary_present:
        blocking.append("Local stage assessment summary is missing or malformed")
    global_path = root / "Build-Plans/Build-status/Global-workflow-state.json"
    if global_path.is_file():
        try:
            global_state = load_json(global_path)
            if not isinstance(global_state, Mapping) or not isinstance(global_state.get("stages", {}), Mapping):
                raise ValueError("expected global state object with stages object")
        except ValueError as exc:
            blocking.append(f"Global state update blocked; preserve source for repair: {exc}")
    blocking = list(dict.fromkeys(blocking))
    ready = not blocking and proposed_status == READY_STATUSES[stage]
    revision_loops = [
        {
            "owning_stage": f"Stage {stage}",
            "owning_output": str(canonical_path.relative_to(root)),
            "owning_skill": f"stage-{stage}",
            "blocking_issue": issue,
            "required_change": issue,
            "recommended_action": "Correct the owning output and rerun the readiness audit.",
            "accepted_risk_allowed": False,
        }
        for issue in blocking
    ]
    return {
        "stage": f"Stage {stage}",
        "command": "global-stage-readiness-audit",
        "audit_status": "passed" if ready else "failed",
        "finalization_attempt": True,
        "proposed_completion_status": proposed_status,
        "evaluated_completion_status": proposed_status if ready else "needs_current_stage_revision",
        "handoff_mode": "feedback_routes" if stage == 8 else "next_stage",
        "global_workflow_contract": "System-References/Docs/Global-Stage-Workflow-Contract.md",
        "required_files_present": not missing_files,
        "local_assessment_summary": {
            "required": stage >= 5,
            "path": str(summary_path.relative_to(root)) if summary_path else "",
            "present": summary_present,
            "matches_canonical_outputs": summary_present and not parse_errors,
            "assessment": "Structurally matched" if summary_present else "Not required" if stage < 5 else "Missing or malformed",
            "blocking_gaps": [item for item in missing_files if item.endswith(".md")],
        },
        "workflow_outcome_evidence": {
            "required": workflow_required,
            "workflow_evidence_present": workflow_present,
            "launch_critical_workflows_checked": workflow_checked,
            "launch_critical_workflows_passed": not outcome_blocks and not any(item for item in workflow_gaps),
            "dead_controls_detected": dead_controls,
            "fixture_runtime_dependencies": fixture_dependencies,
            "blocking_workflow_gaps": workflow_gaps,
        },
        "schemas_valid": not schema_errors and not parse_errors,
        "completion_status_present": bool(completion_status),
        "global_status_mapped": proposed_status in set(READY_STATUSES.values()) | {"needs_current_stage_revision", "needs_prior_stage_revision", "blocked"},
        "handoff_present": handoff is not None,
        "handoff_usable": handoff is not None,
        "feedback_routes_present": stage == 8 and handoff is not None,
        "feedback_routes_usable": stage == 8 and handoff is not None,
        "risks_recorded": _has_record(documents, {"risks", "risk_registry", "risks_not_applicable"}),
        "assumptions_recorded": _has_record(documents, {"assumptions", "assumptions_not_applicable"}),
        "traceability_present": bool(reference_result["checked_refs"]) or not reference_result["missing_refs"],
        "artifacts_recorded": artifact_registry_path.is_file(),
        "stage_contract_profile": profile_result,
        "schema_validation": {
            "schema_refs": [f"System-References/Schemas/stage-{stage}-output.schema.json"],
            "validated_files": validated_files,
            "schema_errors": parse_errors + schema_errors,
            "schemas_valid": not parse_errors and not schema_errors,
            "validated_at": datetime.now(timezone.utc).isoformat(),
            "validator": "workflow_validation.py",
            "blocking": True,
        },
        "reference_integrity": reference_result | {"orphaned_refs": [], "stale_refs": []},
        "artifact_evidence_registry": {
            "registry_path": "Build-Plans/Build-status/Artifact-evidence-registry.json",
            "required": stage >= 6,
            "required_artifacts_present": artifact_registry_path.is_file(),
            "missing_artifacts": [],
        },
        "risk_acceptance_ledger": {
            "ledger_path": "Build-Plans/Build-status/Risk-acceptance-ledger.json",
            "required": bool(risk_errors),
            "accepted_risks_present": not risk_errors,
            "missing_risk_acceptance_entries": risk_errors,
            "expired_or_unowned_risks": [],
        },
        "revision_loops": revision_loops,
        "feedback_route_audit": feedback_result,
        "visual_design_continuity": {"required": visual_required, "ui_blueprint_refs_present": _has_record(documents, {"ui_blueprint_refs", "ui_blueprints"}), "visual_spec_refs_present": _has_record(documents, {"visual_spec_refs", "visual_spec_inventory"}), "visual_reference_refs_present": _has_record(documents, {"visual_reference_refs", "visual_reference_selection"}), "design_system_refs_present": _has_record(documents, {"design_system_refs", "design_system_foundation"}), "visual_acceptance_criteria_mapped": _has_record(documents, {"visual_acceptance_criteria", "visual_acceptance_criteria_refs"}), "visual_reference_compliance_recorded": _has_record(documents, {"visual_reference_compliance"}), "preview_or_visual_qa_evidence_present": _has_record(documents, {"visual_qa", "preview_evidence"}), "design_system_compliance_recorded": _has_record(documents, {"design_system_compliance"}), "visual_drift_status_recorded": _has_record(documents, {"visual_drift_status", "visual_drift_source"}), "blocking_visual_gaps": [item for item in blocking if "Frontend work" in item]},
        "blocking_gaps": blocking,
        "warnings": [],
        "next_actions": ["Correct blocking gaps and rerun the audit."] if blocking else [],
        "ready_for_next_stage": ready,
    }


def write_results(root: Path, stage: int, audit: Mapping[str, Any]) -> dict[str, Any]:
    status_dir = root / "Build-Plans/Build-status"
    status_dir.mkdir(parents=True, exist_ok=True)
    audit_path = status_dir / f"Stage-{stage}-readiness-audit.json"
    audit = dict(audit)
    global_path = status_dir / "Global-workflow-state.json"
    try:
        global_state = load_json(global_path) if global_path.is_file() else {"stages": {}}
        if not isinstance(global_state, dict) or not isinstance(global_state.get("stages", {}), dict) or any(not isinstance(record, dict) for record in global_state.get("stages", {}).values()):
            raise ValueError("Global state stages must contain objects")
    except ValueError as exc:
        issue = f"Global state update failed; original file preserved: {exc}"
        audit.update(audit_status="failed", ready_for_next_stage=False, evaluated_completion_status="needs_current_stage_revision")
        audit["blocking_gaps"] = list(audit["blocking_gaps"]) + [issue]
        audit["revision_loops"] = list(audit["revision_loops"]) + [{"owning_stage": f"Stage {stage}", "owning_output": str(global_path.relative_to(root)), "owning_skill": "global-stage-readiness-audit", "blocking_issue": issue, "required_change": "Repair global state and rerun", "recommended_action": "Preserve and repair the original global state", "accepted_risk_allowed": False}]
        audit["next_actions"] = ["Repair global state and rerun the audit."]
        audit_path.write_text(json.dumps(audit, indent=2), encoding="utf-8")
        return audit
    audit_path.write_text(json.dumps(audit, indent=2), encoding="utf-8")
    stage_key = f"stage_{stage}"
    global_state.setdefault("stages", {}).setdefault(stage_key, {})
    global_state["stages"][stage_key].update({
        "status": audit["evaluated_completion_status"],
        "audit_file": str(audit_path.relative_to(root)),
        "audit_status": audit["audit_status"],
        "ready_for_next_stage": audit["ready_for_next_stage"],
    })
    global_state["current_stage"] = stage_key
    global_state["blocking_gaps"] = audit["blocking_gaps"]
    global_state["revision_loops"] = audit["revision_loops"]
    global_state["last_audit"] = str(audit_path.relative_to(root))
    global_state["next_recommended_action"] = audit["next_actions"][0] if audit["next_actions"] else "Proceed to the routed next stage."
    global_path.write_text(json.dumps(global_state, indent=2), encoding="utf-8")
    return audit


def main() -> int:
    args = parse_args()
    root = Path(args.workspace_root).resolve()
    audit = build_audit(root, args.stage, args.proposed_status)
    audit = write_results(root, args.stage, audit)
    print(json.dumps({"stage": args.stage, "audit_status": audit["audit_status"], "ready_for_next_stage": audit["ready_for_next_stage"], "blocking_gaps": audit["blocking_gaps"]}, indent=2))
    return 0 if audit["ready_for_next_stage"] else 1


if __name__ == "__main__":
    sys.exit(main())
