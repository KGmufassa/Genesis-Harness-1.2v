"""Regression coverage for the 2026-11 enforcement findings."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any

import test_readiness_runner
from precode_fixtures import write_json

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from run_readiness_audit import READY_STATUSES, build_audit
from workflow_validation import validate_schema

ROOT = Path(__file__).resolve().parents[4]


class EnforcementPatchTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        test_readiness_runner.ReadinessRunnerTests()._workspace(self.root)

    def change(self, relative: str, key: str, value: Any) -> None:
        path = self.root / relative
        doc = json.loads(path.read_text())
        parent = doc
        parts = key.split("/")
        for part in parts[:-1]:
            parent = parent[int(part)] if isinstance(parent, list) else parent[part]
        parent[parts[-1]] = value
        write_json(path, doc)

    def assertBlocked(self, stage: int, fragment: str) -> None:
        audit = build_audit(self.root, stage, READY_STATUSES[stage])
        self.assertFalse(audit["ready_for_next_stage"], fragment)
        self.assertIn(fragment.lower(), " ".join(audit["blocking_gaps"]).lower())

    def test_stage_specific_seed_schemas(self) -> None:
        for stage, name in enumerate(("Planning", "Validation", "Architecture", "UX"), 1):
            doc = json.loads((ROOT / f"Build-Plans/Build-status/{name}-state.json").read_text())
            self.assertEqual(validate_schema(doc, ROOT / f"System-References/Schemas/stage-{stage}-output.schema.json", ROOT), [])

    def test_unique_items(self) -> None:
        path = self.root / "unique.schema.json"
        write_json(path, {"type": "array", "uniqueItems": True})
        self.assertTrue(validate_schema([{"a": 1}, {"a": 1}], path, self.root))
        self.assertEqual(validate_schema([True, 1], path, self.root), [])

    def test_profile_missing_output(self) -> None:
        self.change("Build-Plans/Build-status/Planning-state.json", "stage_contract_profile", {"profile_id": "custom", "required_outputs": ["missing-required.json"]})
        self.assertBlocked(1, "missing-required.json")

    def test_missing_research_evidence(self) -> None:
        self.change("Build-Plans/Build-status/Validation-state.json", "assumption_registry", [])
        self.assertBlocked(2, "assumption_registry")

    def test_low_confidence(self) -> None:
        self.change("Build-Plans/Build-status/Validation-state.json", "confidence_scores", {"market": .1})
        self.assertBlocked(2, "confidence")

    def test_broken_normalized_manifest(self) -> None:
        self.change("Build-Plans/Stage-5/09-stage-manifest.json", "artifacts/0/path", "Build-Plans/Stage-5/MISSING.json")
        self.assertBlocked(5, "manifest")

    def test_failed_persistence(self) -> None:
        self.change("Build-Plans/Stage-6/04-system-health.json", "workflow_evidence", [{"workflow_id": "WORKFLOW-CRITICAL", "status": "runtime_persistence_failed"}])
        self.assertBlocked(6, "workflow")

    def test_launch_proof_categories(self) -> None:
        for field in ("production_build_artifact", "deployment_dry_run_result", "smoke_test_results", "rollback_test_result", "environment_verification", "monitoring_alert_test"):
            with self.subTest(field=field):
                path = self.root / "Build-Plans/Stage-7/01-launch-readiness.json"
                original = path.read_text()
                self.change(str(path.relative_to(self.root)), f"deployment_proof/{field}", {})
                self.assertBlocked(7, field)
                path.write_text(original)

    def test_invalid_feedback_target(self) -> None:
        self.change("Build-Plans/Stage-8/01-telemetry-analysis.json", "prior_stage_feedback", [{"owner": "user", "recommended_action": "Review", "recommended_target_stage": "Stage 99"}])
        self.assertBlocked(8, "target")

    def test_corrupt_canonical_cli_writes_failed_audit(self) -> None:
        path = self.root / "Build-Plans/Build-status/Planning-state.json"
        path.write_text("{")
        result = subprocess.run([sys.executable, str(ROOT / ".opencode/Skills/global-stage-readiness-audit/scripts/run_readiness_audit.py"), "--stage", "1", "--proposed-status", "ready_for_stage_2", "--workspace-root", str(self.root)], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        audit = json.loads((self.root / "Build-Plans/Build-status/Stage-1-readiness-audit.json").read_text())
        self.assertFalse(audit["ready_for_next_stage"])
        self.assertTrue(audit["revision_loops"])
        self.assertEqual(path.read_text(), "{")

    def test_corrupt_global_state_is_preserved(self) -> None:
        from run_readiness_audit import write_results
        path = self.root / "Build-Plans/Build-status/Global-workflow-state.json"
        path.write_text("{")
        audit = build_audit(self.root, 1, READY_STATUSES[1])
        write_results(self.root, 1, audit)
        saved = json.loads((path.parent / "Stage-1-readiness-audit.json").read_text())
        self.assertFalse(saved["ready_for_next_stage"])
        self.assertIn("global", " ".join(saved["blocking_gaps"]).lower())
        self.assertEqual(path.read_text(), "{")

    def test_scope_change_invalidates_waitlist(self) -> None:
        self.change("Build-Plans/Stage-1/05-feature-structure.json", "features", [{"name": "Different product"}])
        self.assertBlocked(4, "hash")

    def test_platform_omission_cannot_be_mirrored_away(self) -> None:
        self.change("Build-Plans/Stage-1/05-feature-structure.json", "target_platforms", ["web", "ios"])
        self.assertBlocked(3, "platform")

    def test_schema_vocabulary_and_reference_siblings(self) -> None:
        from workflow_validation import SCHEMA_KEYWORDS
        def check(schema: Any) -> None:
            if not isinstance(schema, dict): return
            self.assertFalse(set(schema) - SCHEMA_KEYWORDS)
            for key in ("properties", "$defs"):
                for child in schema.get(key, {}).values(): check(child)
            for key in ("items", "if", "then", "else"):
                check(schema.get(key))
            for key in ("allOf", "anyOf", "oneOf"):
                for child in schema.get(key, []): check(child)
        for path in (ROOT / "System-References/Schemas").glob("*.json"):
            check(json.loads(path.read_text()))
        path = self.root / "siblings.schema.json"
        write_json(path, {"$defs": {"value": {"type": "integer"}}, "$ref": "#/$defs/value", "minimum": 2})
        self.assertTrue(validate_schema(1, path, self.root))
        write_json(path, {"type": "string", "maxLength": 1})
        self.assertIn("unsupported", " ".join(validate_schema("long", path, self.root)))

    def test_research_low_quality_and_critical_unknowns(self) -> None:
        self.change("Build-Plans/Build-status/Validation-state.json", "assumption_registry/0/evidence_quality", "low")
        self.assertBlocked(2, "evidence")
        self.change("Build-Plans/Build-status/Validation-state.json", "critical_unknowns", [{"finding": "Unknown provider"}])
        self.assertBlocked(2, "critical_unknowns")

    def test_profile_unknown_layer_and_approval(self) -> None:
        self.change("Build-Plans/Build-status/Planning-state.json", "stage_contract_profile", {"profile_id": "custom", "required_validation_layers": ["imaginary_check"]})
        self.assertBlocked(1, "unsupported validation layer")
        self.change("Build-Plans/Build-status/Planning-state.json", "stage_contract_profile", {"profile_id": "custom", "approval_gates": ["/additional_approval"]})
        self.assertBlocked(1, "approval gate")
        self.change("Build-Plans/Build-status/Planning-state.json", "additional_approval", {"approval_status": "approved"})
        self.assertTrue(build_audit(self.root, 1, READY_STATUSES[1])["ready_for_next_stage"])

    def test_current_stage_decisions_cannot_use_prior_records(self) -> None:
        path = self.root / "Build-Plans/Stage-6"
        for document in path.glob("*.json"):
            data = json.loads(document.read_text())
            data.pop("assumptions", None); data["assumptions_not_applicable"] = False
            write_json(document, data)
        self.assertBlocked(6, "current-stage assumptions")

    def test_all_launch_proof_and_workflow_successes_pass(self) -> None:
        for stage in (5, 6, 7, 8):
            audit = build_audit(self.root, stage, READY_STATUSES[stage])
            self.assertTrue(audit["ready_for_next_stage"], audit["blocking_gaps"])
        feedback = build_audit(self.root, 8, READY_STATUSES[8])["feedback_route_audit"]
        self.assertEqual(feedback["routes_checked"][0]["recommended_target_stage"], "Stage 1")
        self.assertTrue(feedback["creates_new_stage_cycle"])

    def test_missing_runtime_workflow_and_earlier_success_do_not_pass(self) -> None:
        self.change("Build-Plans/Stage-6/04-system-health.json", "workflow_evidence", [])
        self.assertBlocked(6, "missing launch-critical workflow")

    def test_unverified_evidence_blocks_runtime_and_launch(self) -> None:
        self.change("Build-Plans/Build-status/Artifact-evidence-registry.json", "artifacts/1/status", "pending")
        self.assertBlocked(6, "unverified")
        self.assertBlocked(7, "unverified")

    def test_stage5_context_and_handoff_references_are_required(self) -> None:
        self.change("Build-Plans/Stage-5/00-stage-context.json", "waitlist_validation_ref", "")
        self.assertBlocked(5, "waitlist_validation_ref")
        self.change("Build-Plans/Stage-6/04-system-health.json", "stage_7_handoff/deployment_strategy_ref", "")
        self.assertBlocked(6, "deployment_strategy_ref")

    def test_visual_qa_needs_responsive_and_design_proof(self) -> None:
        path = "Build-Plans/Stage-6/04-system-health.json"
        self.change(path, "visual_qa", {"status": "passed", "evidence_refs": ["ARTIFACT-RELEASE"]})
        self.assertBlocked(6, "visual qa")
        self.change(path, "visual_qa", {"status": "passed", "responsive_validation": "passed", "design_system_compliance": "passed", "evidence_refs": ["ARTIFACT-RELEASE"], "unresolved_failures": []})
        audit = build_audit(self.root, 6, READY_STATUSES[6])
        self.assertTrue(audit["ready_for_next_stage"], audit["blocking_gaps"])

    def test_feedback_high_severity_needs_verified_evidence(self) -> None:
        self.change("Build-Plans/Stage-8/01-telemetry-analysis.json", "prior_stage_feedback/0/severity", "critical")
        self.assertBlocked(8, "evidence")
        self.change("Build-Plans/Stage-8/01-telemetry-analysis.json", "prior_stage_feedback/0/evidence_refs", ["ARTIFACT-RELEASE"])
        self.assertTrue(build_audit(self.root, 8, READY_STATUSES[8])["ready_for_next_stage"])

    def test_malformed_sources_fail_without_exceptions(self) -> None:
        for path, stage in (("Build-Plans/Build-status/Risk-acceptance-ledger.json", 7), ("Build-Plans/Build-status/Artifact-evidence-registry.json", 7), ("Build-Plans/Build-status/Planning-state.json", 1)):
            with self.subTest(path=path):
                target = self.root / path
                original = target.read_text()
                target.write_text("[]")
                self.assertFalse(build_audit(self.root, stage, READY_STATUSES[stage])["ready_for_next_stage"])
                target.write_text(original)

    def test_missing_schema_reference_is_a_durable_blocker(self) -> None:
        self.change("Build-Plans/Stage-1/01-product-foundation.json", "$schema", "System-References/Schemas/MISSING.json")
        self.assertBlocked(1, "schema does not exist")

    def test_unrelated_envelope_edit_does_not_invalidate_scope(self) -> None:
        self.change("Build-Plans/Stage-1/05-feature-structure.json", "schema_validation", {"checked_at": "later"})
        self.assertTrue(build_audit(self.root, 4, READY_STATUSES[4])["ready_for_next_stage"])

    def test_stack_change_invalidates_approval(self) -> None:
        self.change("Build-Plans/Build-status/Architecture-state.json", "selected_stack/frontend", {"framework": "Different framework"})
        self.assertBlocked(3, "stack_hash")
        self.assertBlocked(4, "stack_hash")

    def test_deferral_requires_scoped_risk_authority(self) -> None:
        path = "Build-Plans/Stage-7/01-launch-readiness.json"
        self.change(path, "deployment_proof/monitoring_alert_test", {"status": "deferred_with_approval", "accepted_risk_ref": "RISK-ALERT"})
        self.assertBlocked(7, "monitoring_alert_test")
        self.change(path, "risks", [{"risk_id": "RISK-ALERT", "description": "Alert setup pending"}])
        approval = self.root / "evidence/accepted-risk.md"
        approval.write_text("User-approved test fixture risk decision")
        ledger = {"ledger_version": "1.0.0", "accepted_risks": [{"risk_id": "RISK-ALERT", "source_stage": "Stage 7", "risk": "Alert setup pending", "severity": "high", "status": "active", "acceptance_authority": "user", "accepted_by": "user", "acceptance_reason": "Supervised launch", "mitigation": "Manual monitoring", "owner_stage": "Stage 7", "revisit_trigger": "Before unattended operation", "approval_ref": "evidence/accepted-risk.md"}]}
        write_json(self.root / "Build-Plans/Build-status/Risk-acceptance-ledger.json", ledger)
        audit = build_audit(self.root, 7, READY_STATUSES[7])
        self.assertTrue(audit["ready_for_next_stage"], audit["blocking_gaps"])
        ledger["accepted_risks"][0]["source_stage"] = "Stage 2"
        write_json(self.root / "Build-Plans/Build-status/Risk-acceptance-ledger.json", ledger)
        self.assertBlocked(7, "monitoring_alert_test")

    def test_profile_forces_visual_check_without_blueprint_marker(self) -> None:
        self.change("Build-Plans/Stage-6/04-system-health.json", "stage_contract_profile", {"profile_id": "custom", "required_validation_layers": ["visual_qa"]})
        self.assertBlocked(6, "visual_qa")

    def test_damaged_summary_is_a_blocker(self) -> None:
        path = self.root / "Build-Plans/Stage-7/06-stage-7-summary.md"
        path.write_bytes(b"\xff")
        self.assertBlocked(7, "unreadable")

    def test_malformed_feedback_fields_do_not_crash(self) -> None:
        self.change("Build-Plans/Stage-8/01-telemetry-analysis.json", "prior_stage_feedback/0/severity", {})
        self.assertBlocked(8, "feedback")

    def test_failed_feedback_audit_itself_matches_schema(self) -> None:
        self.change("Build-Plans/Stage-8/01-telemetry-analysis.json", "prior_stage_feedback", [{"recommended_target_stage": "Stage 99", "owner": [], "recommended_action": {}}])
        audit = build_audit(self.root, 8, READY_STATUSES[8])
        self.assertFalse(audit["ready_for_next_stage"])
        self.assertEqual(validate_schema(audit, ROOT / "System-References/Schemas/global-readiness-audit.schema.json", ROOT), [])
