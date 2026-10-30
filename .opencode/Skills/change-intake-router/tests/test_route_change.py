from __future__ import annotations

import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
REPOSITORY_ROOT = SKILL_DIR.parents[2]
sys.path.insert(0, str(SKILL_DIR / "scripts"))

from route_change import audit_record, classify  # noqa: E402


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


class ChangeRouterTests(unittest.TestCase):
    def test_routes_to_earliest_affected_stage(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.assertEqual(classify("Add a new user workflow", root)["entry_stage"], "stage_1")
            self.assertEqual(classify("Change the public API response", root)["entry_stage"], "stage_3")
            self.assertEqual(classify("Redesign the settings page", root)["entry_stage"], "stage_4")
            self.assertEqual(classify("Repair the existing serializer", root)["entry_stage"], "stage_6")

    def test_active_unapproved_stage_remains_refinement(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            write_json(root / "Build-Plans/Build-status/Global-workflow-state.json", {"current_stage": "stage_3", "stages": {"stage_3": {"status": "in_progress"}}})
            route = classify("Change the API", root)
            self.assertEqual(route["mode"], "active_stage_refinement")
            self.assertEqual(route["change_class"], "none")

    def test_completion_audit_passes_compact_record(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "System-References/Schemas").mkdir(parents=True)
            shutil.copy2(REPOSITORY_ROOT / "System-References/Schemas/change-record.schema.json", root / "System-References/Schemas/change-record.schema.json")
            record = self._record()
            record_path = root / "Build-Plans/Changes/CHANGE-001/change-record.json"
            write_json(record_path, record)
            write_json(root / "Build-Plans/Build-status/Change-ledger.json", {"ledger_version": "1.0.0", "changes": [{"change_id": "CHANGE-001", "record_path": "Build-Plans/Changes/CHANGE-001/change-record.json", "status": "active", "base_commit": "abc", "affected_id_locks": ["FEATURE-1"]}]})
            audit = audit_record(root, record_path, False)
            self.assertEqual(audit["audit_status"], "passed")

    def test_completion_audit_blocks_unowned_deferred_work(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "System-References/Schemas").mkdir(parents=True)
            shutil.copy2(REPOSITORY_ROOT / "System-References/Schemas/change-record.schema.json", root / "System-References/Schemas/change-record.schema.json")
            record = self._record()
            record["deferred_items"] = [{"reason": "later"}]
            record_path = root / "Build-Plans/Changes/CHANGE-001/change-record.json"
            write_json(record_path, record)
            write_json(root / "Build-Plans/Build-status/Change-ledger.json", {"ledger_version": "1.0.0", "changes": [{"change_id": "CHANGE-001", "affected_id_locks": ["FEATURE-1"]}]})
            audit = audit_record(root, record_path, False)
            self.assertEqual(audit["audit_status"], "failed")

    def _record(self) -> dict[str, object]:
        return {
            "$schema": "System-References/Schemas/change-record.schema.json",
            "change_id": "CHANGE-001",
            "title": "Update feature",
            "requested_outcome": "Update the approved feature",
            "change_class": "bounded",
            "base_commit": "abc",
            "owner": "user",
            "affected_ids": ["FEATURE-1"],
            "preserved_behavior": [],
            "risk_level": "medium",
            "risk_refs": [],
            "evidence_refs": [],
            "validation_level": "workflow",
            "impact_confidence": "high",
            "unresolved_impacts": [],
            "entry_stage": "stage_4",
            "required_stages": ["stage_4", "stage_5", "stage_6"],
            "stage_dispositions": {},
            "approval": {"required_types": ["product"], "status": "approved", "evidence_refs": [], "approved_by": "user", "approved_at": "2026-08-17T00:00:00Z"},
            "deferred_items": [],
            "completion_disposition": "",
            "status": "active",
        }


if __name__ == "__main__":
    unittest.main()
