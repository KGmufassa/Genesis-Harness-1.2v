from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from precode_validation import DEPLOYMENT_PATH, WAITLIST_PATH
from run_readiness_audit import READY_STATUSES, build_audit
from precode_fixtures import seed_precode, write_json
import test_readiness_runner


class PrecodeReadinessTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        test_readiness_runner.ReadinessRunnerTests()._workspace(self.root)

    def change(self, relative: str, key: str, value: Any) -> None:
        path = self.root / relative
        document = json.loads(path.read_text())
        parts = key.split("/")
        parent = document
        for part in parts[:-1]:
            parent = parent[int(part)] if isinstance(parent, list) else parent[part]
        parent[parts[-1]] = value
        write_json(path, document)

    def audit(self, stage: int) -> dict[str, Any]:
        return build_audit(self.root, stage, READY_STATUSES[stage])

    def test_launch_passes_without_demand_or_elapsed_window(self) -> None:
        self.assertTrue(self.audit(4)["ready_for_next_stage"])
        self.change(WAITLIST_PATH, "metrics", {"status": "observed", "visits": 10, "completed_signups": 0, "conversion_rate": 0, "traffic_sources": [], "observation_start": "2026-11-08", "observation_end": "2026-11-08"})
        self.assertTrue(self.audit(4)["ready_for_next_stage"])

    def test_missing_launch_or_signup_evidence_blocks(self) -> None:
        for field, value in (("publication/status", "pending"), ("publication/url", "http://localhost:3000"), ("verification/signup_persistence/status", "failed"), ("verification/measurement/evidence_refs", [])):
            with self.subTest(field=field):
                seed_precode(self.root)
                self.change(WAITLIST_PATH, field, value)
                self.assertFalse(self.audit(4)["ready_for_next_stage"])

    def test_missing_or_unverified_artifacts_block(self) -> None:
        (self.root / "evidence/waitlist.txt").unlink()
        self.assertFalse(self.audit(4)["ready_for_next_stage"])
        seed_precode(self.root)
        self.change("Build-Plans/Build-status/Artifact-evidence-registry.json", "artifacts/0/status", "pending")
        self.assertFalse(self.audit(4)["ready_for_next_stage"])

    def test_pending_metrics_cannot_claim_counts(self) -> None:
        self.change(WAITLIST_PATH, "metrics/visits", 0)
        self.assertFalse(self.audit(4)["ready_for_next_stage"])

    def test_web_mobile_and_combined_strategies_pass(self) -> None:
        for platforms in (("web",), ("ios",), ("android",), ("web", "ios", "android")):
            with self.subTest(platforms=platforms):
                seed_precode(self.root, platforms)
                audit = self.audit(3)
                self.assertTrue(audit["ready_for_next_stage"], audit["blocking_gaps"])

    def test_unresolved_incompatible_or_unapproved_deployment_blocks(self) -> None:
        for field, value in (("targets/0/method", "Cloudflare or another host"), ("stack_compatibility/status", "incompatible"), ("stack_compatibility/unresolved_blockers", ["Runtime unsupported"]), ("approval/approval_status", "pending"), ("approval/approved_by", ""), ("targets/0/alternatives", [])):
            with self.subTest(field=field):
                seed_precode(self.root)
                self.change(DEPLOYMENT_PATH, field, value)
                self.assertFalse(self.audit(3)["ready_for_next_stage"])

    def test_missing_mobile_requirements_block(self) -> None:
        seed_precode(self.root, ("ios",))
        document = json.loads((self.root / DEPLOYMENT_PATH).read_text())
        del document["targets"][0]["signing"]
        write_json(self.root / DEPLOYMENT_PATH, document)
        self.assertFalse(self.audit(3)["ready_for_next_stage"])

    def test_target_coverage_and_stack_drift_block(self) -> None:
        seed_precode(self.root, ("web", "ios"))
        self.change(DEPLOYMENT_PATH, "targets", json.loads((self.root / DEPLOYMENT_PATH).read_text())["targets"][:1])
        self.assertFalse(self.audit(3)["ready_for_next_stage"])
        seed_precode(self.root)
        self.change("Build-Plans/Build-status/Architecture-state.json", "selected_stack/hosting_and_deployment/target_methods", {"web": "Different host"})
        self.assertFalse(self.audit(3)["ready_for_next_stage"])

    def test_state_and_handoff_references_are_required(self) -> None:
        self.change("Build-Plans/Build-status/UX-state.json", "stage_5_handoff/waitlist_validation_ref", "")
        self.assertFalse(self.audit(4)["ready_for_next_stage"])
        self.change("Build-Plans/Build-status/Architecture-state.json", "stage_4_handoff/deployment_strategy_ref", "")
        self.assertFalse(self.audit(3)["ready_for_next_stage"])

    def test_legacy_outputs_require_new_artifacts_without_backfill(self) -> None:
        for stage, path in ((4, WAITLIST_PATH), (3, DEPLOYMENT_PATH)):
            (self.root / path).unlink()
            audit = self.audit(stage)
            self.assertFalse(audit["ready_for_next_stage"])
            self.assertTrue(audit["revision_loops"])
            self.assertFalse((self.root / path).exists())

    def test_malformed_new_artifacts_report_blockers(self) -> None:
        for stage, path in ((4, WAITLIST_PATH), (3, DEPLOYMENT_PATH)):
            write_json(self.root / path, {"targets": "invalid"})
            self.assertFalse(self.audit(stage)["ready_for_next_stage"])

    def test_stages_2_and_3_do_not_require_waitlist_launch(self) -> None:
        (self.root / WAITLIST_PATH).unlink()
        for stage in (2, 3):
            audit = self.audit(stage)
            self.assertTrue(audit["ready_for_next_stage"], audit["blocking_gaps"])
        self.assertFalse(self.audit(4)["ready_for_next_stage"])

    def test_stage4_requires_scope_and_deployment_approval(self) -> None:
        self.change("Build-Plans/Build-status/Planning-state.json", "stage_decision_brief/approval_status", "pending")
        self.assertFalse(self.audit(4)["ready_for_next_stage"])
        self.change("Build-Plans/Build-status/Planning-state.json", "stage_decision_brief/approval_status", "approved")
        self.change(DEPLOYMENT_PATH, "approval/approval_status", "pending")
        self.assertFalse(self.audit(4)["ready_for_next_stage"])

    def test_publication_cannot_precede_deployment_approval(self) -> None:
        self.change(WAITLIST_PATH, "publication/published_at", "2026-11-07T12:00:00Z")
        self.assertFalse(self.audit(4)["ready_for_next_stage"])

    def test_legacy_stage2_artifact_is_history_not_a_launch_gate(self) -> None:
        legacy = self.root / "Build-Plans/Stage-2/07-waitlist-validation.json"
        legacy.write_text((self.root / WAITLIST_PATH).read_text(), encoding="utf-8")
        for stage in (2, 3, 4):
            audit = self.audit(stage)
            self.assertTrue(audit["ready_for_next_stage"], audit["blocking_gaps"])
        (self.root / WAITLIST_PATH).unlink()
        self.assertFalse(self.audit(4)["ready_for_next_stage"])
        self.assertTrue(legacy.is_file())
