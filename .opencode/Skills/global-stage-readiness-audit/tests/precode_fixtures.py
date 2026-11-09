"""Complete pre-code artifacts for isolated readiness tests."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Sequence


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value), encoding="utf-8")


def seed_precode(root: Path, platforms: Sequence[str] = ("web",)) -> None:
    wait_ref = "Build-Plans/Stage-4/10-waitlist-validation.json#"
    deployment_ref = "Build-Plans/Stage-3/09-deployment-strategy.json#"
    stage1 = root / "Build-Plans/Stage-1/01-product-foundation.json"
    origin = json.loads(stage1.read_text())
    origin["assumption_id"] = "ASSUMPTION-DEMAND"
    write_json(stage1, origin)
    scope_path = root / "Build-Plans/Stage-1/05-feature-structure.json"
    scope = json.loads(scope_path.read_text())
    scope.update(target_platforms=list(platforms), features=[{"feature_id": "FEATURE-CORE", "name": "Coordinate events"}])
    write_json(scope_path, scope)
    evidence = root / "evidence/waitlist.txt"
    evidence.parent.mkdir(parents=True, exist_ok=True)
    evidence.write_text("Verified public signup persistence and page checks", encoding="utf-8")
    write_json(root / "Build-Plans/Build-status/Artifact-evidence-registry.json", {
        "registry_version": "1.0.0", "artifacts": [{"artifact_id": "ARTIFACT-WAITLIST", "type": "validation_report", "related_stage": "Stage 4", "status": "verified", "path_or_url": "evidence/waitlist.txt"}],
    })
    check = {"status": "passed", "checked_at": "2026-11-08T12:00:00Z", "evidence_refs": ["ARTIFACT-WAITLIST"]}
    waitlist = {
        "$schema": "System-References/Schemas/waitlist-validation.schema.json", "stage": "Stage 4",
        "deployment_strategy_ref": deployment_ref,
        "core_features_ref": "Build-Plans/Stage-1/05-feature-structure.json#",
        "experiment_id": "EXPERIMENT-WAITLIST", "source_refs": ["ASSUMPTION-DEMAND"],
        "audience": "Event planners", "value_proposition": "Plan events together", "signup_offer": "Early access",
        "desired_metrics": ["Signup conversion"], "measurement_window": "Two weeks", "owner": "user",
        "hosting": {"method": "Static hosting", "collection_method": "Hosted signup endpoint", "rationale": "Minimal experiment", "cost_assumptions": "Low volume"},
        "publication": {"status": "published", "url": "https://example.com/waitlist", "published_at": "2026-11-08T12:00:00Z"},
        "verification": {name: dict(check) for name in ("public_url", "signup_persistence", "success_error_states", "duplicate_handling", "spam_protection", "mobile_layout", "accessibility", "measurement")},
        "metrics": {"status": "awaiting_evidence"}, "limitations": ["No traffic yet"], "follow_up_actions": ["Measure demand"],
    }
    envelope = json.loads((root / "Build-Plans/Stage-4/01-user-journeys.json").read_text())
    envelope.pop("artifact_id", None)
    write_json(root / wait_ref[:-1], envelope | waitlist)
    methods = {platform: f"Concrete {platform} deployment" for platform in platforms}
    targets = []
    for platform in platforms:
        target = {"platform": platform, "method": methods[platform], "rationale": "App fit", "runtime_fit": "Supported APIs", "cost_assumptions": "Low usage", "operational_burden": "Managed", "alternatives": [{"method": methods[platform], "disposition": "selected", "rationale": "App fit"}, {"method": "Alternative deployment", "disposition": "rejected", "rationale": "Higher burden"}]}
        if platform != "web":
            target.update({name: "Concrete mobile requirement" for name in ("build_toolchain", "signing", "test_distribution", "distribution_channel", "developer_accounts", "release_process", "update_process")})
        targets.append(target)
    deployment = {
        "$schema": "System-References/Schemas/deployment-strategy.schema.json", "stage": "Stage 3", "strategy_id": "INFRA-DEPLOYMENT",
        "source_refs": ["ASSUMPTION-DEMAND"], "required_targets": list(platforms), "backend_hosting": "Managed API runtime", "targets": targets,
        "sources": [{"url": "https://developers.cloudflare.com/", "accessed_at": "2026-11-08", "finding": "Runtime suitability checked"}], "prerequisites": [], "risks": [],
        "stack_compatibility": {"status": "compatible", "findings": ["Build and runtime compatible"], "unresolved_blockers": []},
        "approval": {"approval_status": "approved", "approved_by": "user", "approved_at": "2026-11-08T12:00:00Z", "brief_ref": "Build-Plans/Stage-3/00-stage-decision-brief.md"},
    }
    envelope = json.loads((root / "Build-Plans/Stage-3/01-system-topology.json").read_text())
    envelope.pop("artifact_id", None)
    write_json(root / deployment_ref[:-1], envelope | deployment)
    for stage, filename in ((4, "UX-state.json"), (3, "Architecture-state.json")):
        path = root / "Build-Plans/Build-status" / filename
        state = json.loads(path.read_text())
        if stage == 4:
            state["waitlist_validation_ref"] = wait_ref
            state["deployment_strategy_ref"] = deployment_ref
            state["stage_5_handoff"].update({"waitlist_validation_ref": wait_ref, "deployment_strategy_ref": deployment_ref})
        if stage == 3:
            state["deployment_strategy_ref"] = deployment_ref
            state["deployment_targets"] = list(platforms)
            state["stage_4_handoff"]["deployment_strategy_ref"] = deployment_ref
            state["selected_stack"] = {"hosting_and_deployment": {"deployment_strategy_ref": deployment_ref, "target_methods": methods}}
        write_json(path, state)

    from decision_bindings import decision_hashes
    architecture_path = root / "Build-Plans/Build-status/Architecture-state.json"
    architecture = json.loads(architecture_path.read_text())
    deployment = json.loads((root / deployment_ref[:-1]).read_text())
    hashes = decision_hashes(root, architecture, deployment)
    deployment["approval"].update(hashes)
    write_json(root / deployment_ref[:-1], deployment)
    planning_path = root / "Build-Plans/Build-status/Planning-state.json"
    planning = json.loads(planning_path.read_text())
    planning["stage_decision_brief"]["core_features_hash"] = hashes["core_features_hash"]
    write_json(planning_path, planning)
    waitlist = json.loads((root / wait_ref[:-1]).read_text())
    waitlist["approved_decisions"] = hashes
    write_json(root / wait_ref[:-1], waitlist)
