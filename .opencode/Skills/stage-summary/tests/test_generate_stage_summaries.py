from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "generate_stage_summaries.py"


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


class StageSummaryScriptTests(unittest.TestCase):
    def run_script(self, root: Path, *extra_args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT_PATH), "--workspace-root", str(root), *extra_args],
            capture_output=True,
            text=True,
        )

    def test_generates_stage_5_v2_assessment_summary(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            stage_5 = root / "Build-Plans" / "Stage-5"
            stage_5.mkdir(parents=True)
            write_json(stage_5 / "00-stage-context.json", {"stage": "Stage 5", "risks": [{"risk_id": "RISK-1"}]})
            write_json(
                stage_5 / "01-development-roadmap.json",
                {"artifact_type": "development_roadmap", "status": "complete", "data": {"roadmap": {"milestones": []}}},
            )
            write_json(
                stage_5 / "02-implementation-sequence.json",
                {"artifact_type": "implementation_sequence", "status": "complete", "data": {"slices": []}},
            )
            write_json(
                stage_5 / "03-engineering-dependencies.json",
                {"artifact_type": "engineering_dependencies", "status": "complete", "data": {"dependencies": []}},
            )
            write_json(
                stage_5 / "04-testing-strategy.json",
                {"artifact_type": "testing_strategy", "status": "complete", "data": {"testing_strategy": {}}},
            )
            write_json(
                stage_5 / "05-build-tickets.json",
                {"artifact_type": "build_tickets", "status": "complete", "data": {"tickets": [{"ticket_id": "TICKET-1"}]}},
            )
            write_json(
                stage_5 / "06-agent-assignment-plan.json",
                {"artifact_type": "agent_assignment_plan", "status": "complete", "data": {"agents": [{"agent_id": "AGENT-1"}]}},
            )
            write_json(
                stage_5 / "07-parallel-execution-plan.json",
                {"artifact_type": "parallel_execution_plan", "status": "complete", "data": {"batches": [{"batch_id": "BATCH-1"}]}},
            )
            write_json(
                stage_5 / "08-release-plan.json",
                {"artifact_type": "release_plan", "status": "complete", "data": {"release_plan": {}}},
            )
            write_json(
                stage_5 / "09-stage-manifest.json",
                {
                    "status": "ready_for_stage_6",
                    "completion_status": {"status": "ready_for_stage_6"},
                    "artifacts": [{"artifact_id": f"ARTIFACT-S5-{index}"} for index in range(1, 9)],
                    "stage_6_handoff": {"readiness": "ready"},
                    "schema_validation": {"schemas_valid": True},
                },
            )

            result = self.run_script(root, "--stages", "5")

            self.assertEqual(result.returncode, 0, result.stderr)
            summary_path = stage_5 / "10-stage-5-summary.md"
            self.assertTrue(summary_path.exists())
            summary = summary_path.read_text(encoding="utf-8")
            self.assertIn("# Stage 5 Assessment Summary", summary)
            self.assertIn("User assessment: `Ready`", summary)
            self.assertIn("Manifest indexed artifacts: 8", summary)
            self.assertIn("Build tickets: 1 tickets", summary)
            self.assertIn("Assigned agents: 1 agents", summary)
            self.assertIn("Parallel batches: 1 batches", summary)
            self.assertIn("Stage 5 JSON outputs and handoff contracts", summary)

    def test_stage_6_summary_includes_live_route_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            stage_6 = root / "Build-Plans" / "Stage-6"
            stage_6.mkdir(parents=True)
            write_json(stage_6 / "01-implementation-status.json", {"status": "complete", "ticket_statuses": []})
            write_json(
                stage_6 / "02-validation-results.json",
                {
                    "status": "complete",
                    "validation_results": [{"validation_id": "VALIDATION-1"}],
                    "workflow_evidence": [
                        {
                            "workflow_id": "WORKFLOW-1",
                            "status": "local_e2e_passed",
                            "evidence_refs": ["ARTIFACT-1"],
                        }
                    ],
                    "live_page_route_evidence": [
                        {"route_ref": "ROUTE-dashboard", "incoming_navigation": "primary_nav", "rendered": True}
                    ],
                },
            )
            write_json(stage_6 / "03-regression-analysis.json", {"status": "complete", "regressions": []})
            write_json(stage_6 / "04-system-health.json", {"status": "ready_for_stage_7", "stage_7_handoff": {}})
            write_json(stage_6 / "05-repair-log.json", {"status": "complete", "repairs": []})

            result = self.run_script(root, "--stages", "6")

            self.assertEqual(result.returncode, 0, result.stderr)
            summary = (stage_6 / "06-stage-6-summary.md").read_text(encoding="utf-8")
            self.assertIn("Live linked/routed page checks: 1", summary)
            self.assertIn("Workflow outcome evidence records: 1", summary)
            self.assertIn("User assessment: `Ready`", summary)

    def test_blocked_summary_reports_missing_required_outputs(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            stage_7 = root / "Build-Plans" / "Stage-7"
            stage_7.mkdir(parents=True)
            write_json(
                stage_7 / "01-launch-readiness.json",
                {"status": "blocked", "blocking_items": [{"summary": "deployment proof missing"}]},
            )

            result = self.run_script(root, "--stages", "7")

            self.assertEqual(result.returncode, 0, result.stderr)
            summary = (stage_7 / "06-stage-7-summary.md").read_text(encoding="utf-8")
            self.assertIn("User assessment: `Blocked`", summary)
            self.assertIn("Required outputs missing:", summary)
            self.assertIn("02-deployment-framework.json", summary)
            self.assertIn("deployment proof missing", summary)

    def test_reads_only_explicit_stage_readiness_audit_from_build_status(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            stage_8 = root / "Build-Plans" / "Stage-8"
            build_status = root / "Build-Plans" / "Build-status"
            stage_8.mkdir(parents=True)
            build_status.mkdir(parents=True)
            write_json(stage_8 / "01-telemetry-analysis.json", {"status": "evolution_plan_ready", "findings": []})
            write_json(stage_8 / "02-operational-optimization.json", {"status": "complete", "optimization_actions": []})
            write_json(stage_8 / "03-ai-improvement-plan.json", {"status": "complete", "improvement_items": []})
            write_json(stage_8 / "04-roadmap-evolution.json", {"status": "complete", "roadmap_changes": []})
            write_json(stage_8 / "05-scalability-evolution.json", {"status": "complete", "scalability_actions": []})
            write_json(build_status / "Stage-8-readiness-audit.json", {"audit_status": "passed", "ready_for_next_stage": True})
            write_json(build_status / "Unrelated-state.json", {"blocking_gaps": [{"summary": "should not appear"}]})

            result = self.run_script(root, "--stages", "8")

            self.assertEqual(result.returncode, 0, result.stderr)
            summary = (stage_8 / "06-stage-8-summary.md").read_text(encoding="utf-8")
            self.assertIn("Readiness audit: `passed`; ready_for_next_stage: `True`", summary)
            self.assertNotIn("should not appear", summary)

    def test_fails_on_invalid_stage_json(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            stage_6 = root / "Build-Plans" / "Stage-6"
            stage_6.mkdir(parents=True)
            (stage_6 / "01-implementation-status.json").write_text("{not valid json}", encoding="utf-8")

            result = self.run_script(root, "--stages", "6")

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Invalid JSON", result.stderr)
            self.assertFalse((stage_6 / "06-stage-6-summary.md").exists())

    def test_rejects_unsupported_stage_numbers(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "Build-Plans").mkdir()

            result = self.run_script(root, "--stages", "4")

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Only Stage 5 through Stage 8", result.stderr)


if __name__ == "__main__":
    unittest.main()
