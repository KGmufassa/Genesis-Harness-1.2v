from __future__ import annotations

import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any


SKILL_DIR = Path(__file__).resolve().parents[1]
REPOSITORY_ROOT = SKILL_DIR.parents[2]
sys.path.insert(0, str(SKILL_DIR / "scripts"))

from run_readiness_audit import (  # noqa: E402
    HANDOFF_KEYS,
    READY_STATUSES,
    STAGE_FILES,
    STATE_FILES,
    build_audit,
    write_results,
)
from workflow_validation import validate_schema  # noqa: E402


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


class ReadinessRunnerTests(unittest.TestCase):
    def _workspace(self, root: Path) -> None:
        shutil.copytree(REPOSITORY_ROOT / "System-References/Schemas", root / "System-References/Schemas")
        status = root / "Build-Plans/Build-status"
        write_json(status / "Global-workflow-state.json", {"stages": {}})
        write_json(status / "Artifact-evidence-registry.json", {"registry_version": "1.0.0", "artifacts": []})
        write_json(status / "Risk-acceptance-ledger.json", {"ledger_version": "1.0.0", "accepted_risks": []})
        for stage in range(1, 9):
            stage_dir = root / "Build-Plans" / f"Stage-{stage}"
            stage_dir.mkdir(parents=True)
            for index, filename in enumerate(STAGE_FILES[stage]):
                path = stage_dir / filename
                if path.suffix == ".md":
                    path.write_text(f"# Stage {stage} Review\n", encoding="utf-8")
                    continue
                payload = self._payload(stage, index)
                if filename == ("09-stage-manifest.json" if stage == 5 else "04-system-health.json" if stage == 6 else "01-launch-readiness.json" if stage == 7 else "01-telemetry-analysis.json" if stage == 8 else ""):
                    payload[HANDOFF_KEYS[stage]] = self._handoff(stage)
                write_json(path, payload)
            if stage in STATE_FILES:
                payload = self._payload(stage, 99)
                payload[HANDOFF_KEYS[stage]] = self._handoff(stage)
                payload["stage_decision_brief"] = {"approval_status": "approved"}
                write_json(status / STATE_FILES[stage], payload)

    def _payload(self, stage: int, index: int) -> dict[str, Any]:
        return {
            "stage": f"Stage {stage}",
            "status": "complete",
            "artifact_id": f"ARTIFACT-S{stage}-{index}",
            "completion_status": {"status": READY_STATUSES[stage]},
            "stage_contract_profile": {"profile_id": "standard", "requirements_checked": True},
            "guidance_policy": {"complexity_level": "medium", "guidance_depth": "standard", "ask_threshold": "material_decisions", "default_inference_allowed": True, "approval_required_for": [], "max_questions_per_turn": 3},
            "schema_validation": {"validation_executed": True, "schemas_valid": True},
            "reference_integrity": {"integrity_status": "passed"},
            "risk_acceptance_ledger": {"accepted_risk_refs": []},
            "revision_loops": [],
            "assumptions_not_applicable": True,
            "risks_not_applicable": True,
        }

    def _handoff(self, stage: int) -> Any:
        if stage == 8:
            return [{"feedback_route_id": "TELEMETRY-ROUTE-1", "owner": "user", "recommended_action": "Review"}]
        return {"source_stage": f"Stage {stage}", "target_stage": f"Stage {stage + 1}", "readiness": "ready"}

    def test_minimal_stage_1_through_8_fixture_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._workspace(root)
            for stage in range(1, 9):
                audit = build_audit(root, stage, READY_STATUSES[stage])
                self.assertTrue(audit["ready_for_next_stage"], audit["blocking_gaps"])
                self.assertEqual(audit["audit_status"], "passed")
                self.assertEqual(
                    validate_schema(audit, root / "System-References/Schemas/global-readiness-audit.schema.json", root),
                    [],
                )
                write_results(root, stage, audit)
            state = json.loads((root / "Build-Plans/Build-status/Global-workflow-state.json").read_text(encoding="utf-8"))
            self.assertEqual(state["stages"]["stage_8"]["audit_status"], "passed")

    def test_missing_output_creates_blocking_revision_loop(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._workspace(root)
            (root / "Build-Plans/Stage-6/02-validation-results.json").unlink()
            audit = build_audit(root, 6, READY_STATUSES[6])
            self.assertFalse(audit["ready_for_next_stage"])
            self.assertTrue(audit["revision_loops"])
            self.assertIn("02-validation-results.json", " ".join(audit["blocking_gaps"]))

    def test_missing_stable_reference_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._workspace(root)
            path = root / "Build-Plans/Stage-4/07-ui-blueprint-specification.json"
            payload = json.loads(path.read_text(encoding="utf-8"))
            payload["feature_refs"] = ["FEATURE-MISSING"]
            write_json(path, payload)
            audit = build_audit(root, 4, READY_STATUSES[4])
            self.assertFalse(audit["ready_for_next_stage"])
            self.assertIn("FEATURE-MISSING", " ".join(audit["blocking_gaps"]))

    def test_high_risk_requires_explicit_authority(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._workspace(root)
            write_json(
                root / "Build-Plans/Build-status/Risk-acceptance-ledger.json",
                {"ledger_version": "1.0.0", "accepted_risks": [{"risk_id": "RISK-1", "severity": "critical", "accepted_by": "agent"}]},
            )
            audit = build_audit(root, 7, READY_STATUSES[7])
            self.assertFalse(audit["ready_for_next_stage"])
            self.assertIn("acceptance authority", " ".join(audit["blocking_gaps"]))

    def test_repository_seed_states_match_common_schema(self) -> None:
        schema_path = REPOSITORY_ROOT / "System-References/Schemas/stage-output-common.schema.json"
        for filename in ("Planning-state.json", "Validation-state.json", "Architecture-state.json", "UX-state.json"):
            path = REPOSITORY_ROOT / "Build-Plans/Build-status" / filename
            payload = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(validate_schema(payload, schema_path, REPOSITORY_ROOT), [], filename)

    def test_schema_validator_enforces_high_risk_authority_condition(self) -> None:
        schema_path = REPOSITORY_ROOT / "System-References/Schemas/risk-acceptance-ledger.schema.json"
        payload = {
            "ledger_version": "1.0.0",
            "accepted_risks": [{"risk_id": "RISK-1", "source_stage": "Stage 7", "risk": "Known issue", "severity": "critical", "status": "active"}],
        }
        errors = validate_schema(payload, schema_path, REPOSITORY_ROOT)
        self.assertIn("accepted_by", " ".join(errors))
        self.assertIn("acceptance_authority", " ".join(errors))


if __name__ == "__main__":
    unittest.main()
