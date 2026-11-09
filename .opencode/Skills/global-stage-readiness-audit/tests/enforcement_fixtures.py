"""Real normalized package and domain evidence for integration tests."""
from __future__ import annotations

import json
from pathlib import Path

from precode_fixtures import write_json
from readiness_controls import PROOF_FIELDS, stage5_module


def seed_enforcement(root: Path) -> None:
    status = root / "Build-Plans/Build-status"
    state_path = status / "Validation-state.json"
    state = json.loads(state_path.read_text())
    state.update(
        confidence_scores={"market": .8, "technical": .8, "business": .8, "operational": .8, "architecture_readiness": .8},
        assumption_registry=[{"id": "ASSUMPTION-VALIDATED", "assumption": "Teams need shared event planning", "source_refs": ["ASSUMPTION-DEMAND"], "architecture_critical": True, "status": "validated", "confidence": .8, "evidence_quality": "high", "evidence": [{"source_type": "user_provided", "evidence_quality": "high", "summary": "Interview fixture", "source_date": "2026-11-08", "freshness": "current", "is_inference": False, "source_url": "https://example.com/interview-fixture"}]}],
        critical_unknowns=[], contradictions=[],
    )
    write_json(state_path, state)
    workflow_source = root / "Build-Plans/Stage-1/03-workflow-architecture.json"
    workflow_doc = json.loads(workflow_source.read_text())
    workflow_doc["workflow_id"] = "WORKFLOW-CRITICAL"
    workflow_doc["launch_critical_workflow_ids"] = ["WORKFLOW-CRITICAL"]
    write_json(workflow_source, workflow_doc)
    module = stage5_module()
    refs = {"waitlist_validation_ref": "Build-Plans/Stage-4/10-waitlist-validation.json#", "deployment_strategy_ref": "Build-Plans/Stage-3/09-deployment-strategy.json#"}
    architecture = json.loads((status / "Architecture-state.json").read_text())
    context = module.build_context(status="complete", selected_stack=architecture["selected_stack"], stage_contract_profile={"profile_id": "standard"}, guidance_policy=state["guidance_policy"], source_inputs={f"stage_{n}": [] for n in range(1,5)}, **refs)
    context.update(assumptions_not_applicable=True, risks_not_applicable=True)
    values = {"development_roadmap": [], "implementation_sequence": [], "engineering_dependencies": [], "testing_strategy": {"test_levels": []}, "build_tickets": [], "agent_assignment_plan": [], "parallel_execution_plan": [], "release_plan": {"release_phases": []}}
    artifacts = [module.build_artifact(kind, status="complete", traceability_refs=[], canonical_data=value) for kind, value in values.items()]
    manifest = module.build_manifest(artifacts, completion_status={"status": "ready_for_stage_6"}, stage_6_handoff={"source_stage": "Stage 5", "target_stage": "Stage 6", "readiness": "ready", **refs}, schema_validation={"validation_executed": True, "schemas_valid": True})
    write_json(root / module.CONTEXT_PATH, context)
    for artifact in artifacts:
        write_json(root / "Build-Plans/Stage-5" / module.ARTIFACTS[artifact["artifact_type"]]["filename"], artifact)
    write_json(root / module.MANIFEST_PATH, manifest)
    evidence_path = root / "evidence/runtime-and-release.txt"
    evidence_path.write_text("Synthetic successful runtime and launch checks; not real-app evidence.")
    registry_path = status / "Artifact-evidence-registry.json"
    registry = json.loads(registry_path.read_text())
    registry["artifacts"].append({"artifact_id": "ARTIFACT-RELEASE", "type": "validation_report", "related_stage": "Stage 7", "status": "verified", "path_or_url": "evidence/runtime-and-release.txt"})
    write_json(registry_path, registry)
    for stage, name in ((6,"04-system-health.json"),(7,"01-launch-readiness.json")):
        path = root / f"Build-Plans/Stage-{stage}" / name
        doc = json.loads(path.read_text())
        doc.update(refs)
        doc[f"stage_{stage+1}_handoff"].update(refs)
        doc.update(launch_critical_workflow_ids=["WORKFLOW-CRITICAL"], workflow_evidence=[{"workflow_id": "WORKFLOW-CRITICAL", "status": "staging_e2e_passed", "verified_user_outcome": "User completes event planning workflow", "evidence_refs": ["ARTIFACT-RELEASE"]}], dead_control_validation={"checked": True, "dead_controls_detected": []}, runtime_data_source_validation={"checked": True, "fixture_runtime_dependencies": []})
        if stage == 7:
            doc["deployment_proof"] = {field: {"status": "passed", "evidence_refs": ["ARTIFACT-RELEASE"]} for field in PROOF_FIELDS}
            doc["deployment_proof"]["release_blockers"] = []
        write_json(path, doc)
