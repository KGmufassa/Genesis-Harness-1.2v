from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any

SKILL_DIR = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = SKILL_DIR / "scripts"
REPOSITORY_ROOT = SKILL_DIR.parents[2]
sys.path.insert(0, str(SCRIPTS_DIR))

from resolve_stage5 import resolve_artifact  # noqa: E402
from stage5_contract import (  # noqa: E402
    ARTIFACTS,
    ContractError,
    build_artifact,
    build_context,
    build_manifest,
    validate_agent_scopes,
    validate_execution_waves,
    validate_file_pointer_ref,
    validate_risk_refs,
    validate_ticket_references,
    validate_workflow_completion_definitions,
    validate_workflow_evidence,
)


class Stage5ContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.context = build_context(
            status="in_progress",
            selected_stack={"runtime": "python"},
            stage_contract_profile={"profile": "standard"},
            guidance_policy={"mode": "guided"},
            source_inputs={
                "stage_1": ["stage-1.json"],
                "stage_2": ["stage-2.json"],
                "stage_3": ["stage-3.json"],
                "stage_4": ["stage-4.json"],
            },
            risks=[{"risk_id": "RISK-1"}],
        )
        values: dict[str, Any] = {
            "development_roadmap": [],
            "implementation_sequence": [],
            "engineering_dependencies": [],
            "testing_strategy": {"test_levels": []},
            "build_tickets": [],
            "agent_assignment_plan": [],
            "parallel_execution_plan": [],
            "release_plan": {"release_phases": []},
        }
        self.artifacts = [
            build_artifact(
                artifact_type,
                status="complete",
                traceability_refs=[],
                canonical_data=values[artifact_type],
            )
            for artifact_type in ARTIFACTS
        ]
        self.manifest = build_manifest(
            self.artifacts,
            completion_status={"status": "ready_for_stage_6"},
            stage_6_handoff={"ticket_refs": []},
            schema_validation={
                "validation_executed": True,
                "schemas_valid": True,
                "results": [],
            },
        )

    def _write_v2(self, directory: Path) -> None:
        (directory / "00-stage-context.json").write_text(
            json.dumps(self.context), encoding="utf-8"
        )
        for artifact in self.artifacts:
            filename = ARTIFACTS[artifact["artifact_type"]]["filename"]
            (directory / filename).write_text(json.dumps(artifact), encoding="utf-8")
        (directory / "09-stage-manifest.json").write_text(
            json.dumps(self.manifest), encoding="utf-8"
        )

    def test_v2_context_structure_and_no_common_envelope_duplication(self) -> None:
        self.assertEqual(self.context["format_version"], "2.0")
        self.assertEqual(self.context["artifact_type"], "stage_context")
        for artifact in self.artifacts:
            self.assertNotIn("selected_stack", artifact["data"])
            self.assertNotIn("risks", artifact["data"])
            self.assertNotIn("completion_status", artifact)
            self.assertNotIn("stage_6_handoff", artifact)

    def test_v2_envelopes_have_unique_ids_and_canonical_keys(self) -> None:
        ids = {artifact["artifact_id"] for artifact in self.artifacts}
        self.assertEqual(len(ids), 8)
        for artifact in self.artifacts:
            definition = ARTIFACTS[artifact["artifact_type"]]
            self.assertIn(definition["data_key"], artifact["data"])

    def test_tickets_agents_and_batches_are_stored_once(self) -> None:
        serialized = json.dumps(self.artifacts)
        self.assertEqual(serialized.count('"tickets"'), 1)
        self.assertEqual(serialized.count('"agents"'), 1)
        self.assertEqual(serialized.count('"batches"'), 1)

    def test_manifest_indexes_every_artifact_consistently(self) -> None:
        self.assertEqual(len(self.manifest["artifacts"]), 8)
        by_type = {item["artifact_type"]: item for item in self.manifest["artifacts"]}
        for artifact in self.artifacts:
            entry = by_type[artifact["artifact_type"]]
            self.assertEqual(entry["artifact_id"], artifact["artifact_id"])
            self.assertEqual(
                entry["data_path"],
                f"/data/{ARTIFACTS[artifact['artifact_type']]['data_key']}",
            )

    def test_schemas_valid_requires_executed_validation(self) -> None:
        with self.assertRaises(ContractError):
            build_manifest(
                self.artifacts,
                completion_status={},
                stage_6_handoff={},
                schema_validation={
                    "validation_executed": False,
                    "schemas_valid": True,
                },
            )

    def test_v2_resolver_returns_data_and_context(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            self._write_v2(directory)
            result = resolve_artifact(directory, "build_tickets", with_context=True)
        self.assertEqual(result["data"], {"tickets": []})
        self.assertEqual(result["context"]["artifact_type"], "stage_context")

    def test_legacy_resolver_supports_self_contained_file(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            path = directory / ARTIFACTS["build_tickets"]["filename"]
            path.write_text(
                json.dumps({"build_tickets": [{"ticket_id": "TICKET-1"}]}),
                encoding="utf-8",
            )
            result = resolve_artifact(directory, "build_tickets", with_context=True)
        self.assertTrue(result["legacy"])
        self.assertEqual(result["data"]["tickets"][0]["ticket_id"], "TICKET-1")

    def test_partial_v2_handoff_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            artifact = next(
                item for item in self.artifacts if item["artifact_type"] == "build_tickets"
            )
            (directory / ARTIFACTS["build_tickets"]["filename"]).write_text(
                json.dumps(artifact), encoding="utf-8"
            )
            with self.assertRaises(ContractError):
                resolve_artifact(directory, "build_tickets")

    def test_manifest_artifact_mismatch_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            self.manifest["artifacts"][4]["artifact_id"] = "ARTIFACT-S5-WRONG"
            self._write_v2(directory)
            with self.assertRaises(ContractError):
                resolve_artifact(directory, "build_tickets")

    def test_risk_refs_resolve_and_copied_risks_are_rejected(self) -> None:
        validate_risk_refs([{"risk_refs": ["RISK-1"]}], ["RISK-1"])
        with self.assertRaises(ContractError):
            validate_risk_refs([{"risk_refs": ["RISK-MISSING"]}], ["RISK-1"])
        with self.assertRaises(ContractError):
            validate_risk_refs([{"risk_refs": [], "risks": []}], ["RISK-1"])

    def test_upstream_ids_and_file_pointer_references_are_validated(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source_path = root / "stage-4.json"
            document = {"screens": [{"id": "SCREEN-1", "criteria": ["visible"]}]}
            source_path.write_text(json.dumps(document), encoding="utf-8")
            sources = {"stage-4.json": document}
            validate_ticket_references(
                [
                    {
                        "ticket_id": "TICKET-1",
                        "screen_refs": ["SCREEN-1"],
                        "visual_acceptance_criteria_refs": [
                            "stage-4.json#/screens/0/criteria/0"
                        ],
                    }
                ],
                repository_root=root,
                source_documents=sources,
            )
            validate_file_pointer_ref(
                "stage-4.json#/screens/0", repository_root=root
            )
            with self.assertRaises(ContractError):
                validate_ticket_references(
                    [{"ticket_id": "TICKET-2", "screen_refs": ["SCREEN-FAKE"]}],
                    repository_root=root,
                    source_documents=sources,
                )
            with self.assertRaises(ContractError):
                validate_file_pointer_ref(
                    "stage-4.json#/screens/9", repository_root=root
                )

    def test_agent_scope_validation(self) -> None:
        tickets = [{"ticket_id": "TICKET-1", "file_scopes": ["src/app.py"]}]
        validate_agent_scopes(
            [
                {
                    "agent_id": "AGENT-1",
                    "assigned_tickets": ["TICKET-1"],
                    "allowed_file_scopes": ["src"],
                }
            ],
            tickets,
        )
        with self.assertRaises(ContractError):
            validate_agent_scopes(
                [
                    {
                        "agent_id": "AGENT-1",
                        "assigned_tickets": ["TICKET-1"],
                        "allowed_file_scopes": ["tests"],
                    }
                ],
                tickets,
            )

    def test_execution_wave_validation(self) -> None:
        tickets = [
            {"ticket_id": "TICKET-1", "depends_on": []},
            {"ticket_id": "TICKET-2", "depends_on": ["TICKET-1"]},
        ]
        validate_execution_waves(
            [
                {
                    "batch_id": "BATCH-1",
                    "tickets": ["TICKET-1", "TICKET-2"],
                    "execution_waves": [
                        {"wave": 1, "ticket_ids": ["TICKET-1"]},
                        {"wave": 2, "ticket_ids": ["TICKET-2"]},
                    ],
                }
            ],
            tickets,
        )
        with self.assertRaises(ContractError):
            validate_execution_waves(
                [
                    {
                        "batch_id": "BATCH-1",
                        "tickets": ["TICKET-1", "TICKET-2"],
                        "execution_waves": [
                            {"wave": 1, "ticket_ids": ["TICKET-1", "TICKET-2"]}
                        ],
                    }
                ],
                tickets,
            )

    def test_launch_critical_tickets_require_workflow_completion_definition(self) -> None:
        validate_workflow_completion_definitions(
            [
                {
                    "ticket_id": "TICKET-1",
                    "priority": "critical",
                    "ticket_type": "frontend",
                    "ui_blueprint_refs": ["UI-BLUEPRINT-1"],
                    "completion_definition": {
                        "contract_only_allowed": False,
                        "requires_ui_wiring": True,
                        "requires_runtime_persistence": True,
                        "requires_end_to_end_smoke": True,
                        "done_means_user_can_complete_workflow": True,
                    },
                    "workflow_smoke_tests": [
                        {
                            "workflow_id": "WORKFLOW-1",
                            "expected_user_outcome": "User can save the setting.",
                        }
                    ],
                }
            ]
        )
        with self.assertRaises(ContractError):
            validate_workflow_completion_definitions(
                [
                    {
                        "ticket_id": "TICKET-2",
                        "priority": "critical",
                        "ticket_type": "frontend",
                        "ui_blueprint_refs": ["UI-BLUEPRINT-1"],
                    }
                ]
            )

    def test_workflow_evidence_requires_passed_launch_critical_e2e(self) -> None:
        validate_workflow_evidence(
            [
                {
                    "workflow_id": "WORKFLOW-1",
                    "status": "local_e2e_passed",
                    "evidence_refs": ["ARTIFACT-1"],
                    "verified_user_outcome": "User completed the workflow.",
                }
            ],
            launch_critical_workflow_ids=["WORKFLOW-1"],
        )
        with self.assertRaises(ContractError):
            validate_workflow_evidence(
                [
                    {
                        "workflow_id": "WORKFLOW-1",
                        "status": "api_exists_not_wired",
                    }
                ],
                launch_critical_workflow_ids=["WORKFLOW-1"],
            )
        with self.assertRaises(ContractError):
            validate_workflow_evidence(
                [
                    {
                        "workflow_id": "WORKFLOW-1",
                        "status": "local_e2e_passed",
                        "verified_user_outcome": "User completed the workflow.",
                    }
                ],
                launch_critical_workflow_ids=["WORKFLOW-1"],
            )

    def test_schema_and_repository_json_parse(self) -> None:
        schema_dir = REPOSITORY_ROOT / "System-References" / "Schemas"
        for path in schema_dir.glob("*.json"):
            with self.subTest(path=path.name):
                self.assertIsInstance(
                    json.loads(path.read_text(encoding="utf-8")), dict
                )

    def test_stage_5_artifact_schema_contains_workflow_completion_contract(self) -> None:
        schema_path = REPOSITORY_ROOT / "System-References" / "Schemas" / "stage-5-artifact.schema.json"
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        serialized = json.dumps(schema)

        self.assertIn("completion_definition", serialized)
        self.assertIn("workflow_smoke_tests", serialized)
        self.assertIn("done_means_user_can_complete_workflow", serialized)

    def test_scripts_compile_as_modules(self) -> None:
        for path in SCRIPTS_DIR.glob("*.py"):
            with self.subTest(path=path.name):
                spec = importlib.util.spec_from_file_location(path.stem, path)
                self.assertIsNotNone(spec)


if __name__ == "__main__":
    unittest.main()
