from __future__ import annotations

import json
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[4]


class Stage7Stage8ReadinessContractTests(unittest.TestCase):
    def _read(self, relative_path: str) -> str:
        return (REPOSITORY_ROOT / relative_path).read_text(encoding="utf-8")

    def test_stage_7_command_requires_audit_for_every_finalization_attempt(self) -> None:
        command = self._read(".opencode/Skills/stage-7-launch-operationalization/skill.md")

        self.assertIn("At the end of every Stage 7 finalization attempt", command)
        self.assertIn("Build-Plans/Build-status/Stage-7-readiness-audit.json", command)
        self.assertIn('"finalization_attempt": true', command)
        self.assertIn('"handoff_mode": "next_stage"', command)
        self.assertIn("needs_launch_readiness_work", command)
        self.assertIn("needs_operational_revision", command)
        self.assertIn("blocked", command)

    def test_stage_8_command_requires_audit_for_every_finalization_attempt(self) -> None:
        command = self._read(".opencode/Skills/stage-8-post-launch-evolution/skill.md")

        self.assertIn("At the end of every Stage 8 finalization attempt", command)
        self.assertIn("Build-Plans/Build-status/Stage-8-readiness-audit.json", command)
        self.assertIn('"finalization_attempt": true', command)
        self.assertIn('"handoff_mode": "feedback_routes"', command)
        self.assertIn("needs_more_telemetry", command)
        self.assertIn("needs_operational_review", command)
        self.assertIn("blocked", command)

    def test_global_audit_schema_supports_stage_8_feedback_routes(self) -> None:
        schema_path = REPOSITORY_ROOT / "System-References/Schemas/global-readiness-audit.schema.json"
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        properties = schema["properties"]

        self.assertEqual(
            properties["handoff_mode"]["enum"],
            ["next_stage", "feedback_routes", "terminal"],
        )
        self.assertIn("feedback_route_audit", properties)
        self.assertIn("local_assessment_summary", properties)
        self.assertIn("matches_canonical_outputs", properties["local_assessment_summary"]["properties"])
        self.assertIn("workflow_outcome_evidence", properties)
        self.assertIn("dead_controls_detected", properties["workflow_outcome_evidence"]["properties"])
        self.assertIn("fixture_runtime_dependencies", properties["workflow_outcome_evidence"]["properties"])
        self.assertIn("feedback_route", schema["$defs"])
        self.assertIn("owner", schema["$defs"]["feedback_route"]["properties"])
        self.assertIn("creates_new_stage_cycle", schema["$defs"]["feedback_route"]["properties"])

    def test_global_contract_documents_unconditional_stage_7_and_stage_8_audits(self) -> None:
        contract = self._read("System-References/Docs/Global-Stage-Workflow-Contract.md")

        self.assertIn("Every stage finalization attempt must write a readiness audit", contract)
        self.assertIn("Build-Plans/Build-status/Stage-7-readiness-audit.json", contract)
        self.assertIn("Build-Plans/Build-status/Stage-8-readiness-audit.json", contract)
        self.assertIn("Stage 8 is terminal and cyclical", contract)

    def test_standalone_audit_doc_matches_new_control_shape(self) -> None:
        audit_doc = self._read("System-References/Docs/Global-Stage-Readiness-Audit.md")
        self.assertIn('"local_assessment_summary": {', audit_doc)
        self.assertIn('"visual_reference_refs_present": false', audit_doc)
        self.assertIn('"visual_reference_compliance_recorded": false', audit_doc)
        self.assertIn("run_readiness_audit.py", audit_doc)

    def test_stage_6_and_stage_7_schemas_include_workflow_outcome_contract(self) -> None:
        stage_6_schema = json.loads(
            (REPOSITORY_ROOT / "System-References/Schemas/stage-6-output.schema.json").read_text(
                encoding="utf-8"
            )
        )
        stage_7_schema = json.loads(
            (REPOSITORY_ROOT / "System-References/Schemas/stage-7-output.schema.json").read_text(
                encoding="utf-8"
            )
        )

        self.assertIn("workflow_evidence", stage_6_schema["properties"])
        self.assertIn("dead_control_validation", stage_6_schema["properties"])
        self.assertIn("runtime_data_source_validation", stage_6_schema["properties"])
        self.assertIn("workflow_evidence_review", stage_7_schema["properties"])


if __name__ == "__main__":
    raise SystemExit(unittest.main())
