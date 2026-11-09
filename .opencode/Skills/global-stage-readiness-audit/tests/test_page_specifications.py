from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
from page_specifications import validate_page_specifications  # noqa: E402
from workflow_validation import validate_schema  # noqa: E402


class PageSpecificationTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.pages = self.root / "Build-Plans/Stage-4/Pages"
        self.state_path = self.root / "Build-Plans/Build-status/UX-state.json"
        self.state_path.parent.mkdir(parents=True)
        self.approval = {"approval_status": "approved", "approved_by": "user", "approved_at": "2026-10-30T12:00:00Z"}
        self.state: dict[str, Any] = {
            "screen_system": {"screen_inventory": []},
            "page_specifications": [],
            "page_set_approval": {"approved_screen_refs": [], **self.approval},
        }
        for number, name in enumerate(("Dashboard", "Settings"), 1):
            ref = f"SCREEN-{number:03}"
            path = self.pages / ref / "page-spec.md"
            path.parent.mkdir(parents=True)
            path.write_text(f"# {name}\n\nWeb/mobile variants, modal, loading and recovery states.\n", encoding="utf-8")
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            self.state["screen_system"]["screen_inventory"].append({"screen_id": ref})
            self.state["page_specifications"].append({"screen_ref": ref, "document_path": path.relative_to(self.root).as_posix(), "content_hash": digest, "approved_hash": digest, **self.approval})
            self.state["page_set_approval"]["approved_screen_refs"].append(ref)
        (self.pages / "README.md").write_text("[Dashboard](SCREEN-001/page-spec.md)\n[Settings](SCREEN-002/page-spec.md)\n", encoding="utf-8")

    def errors(self) -> str:
        return "\n".join(validate_page_specifications(self.root, self.state))

    def run_gate(self) -> subprocess.CompletedProcess[str]:
        self.state_path.write_text(json.dumps(self.state), encoding="utf-8")
        return subprocess.run([sys.executable, str(SCRIPTS / "page_specifications.py"), "--workspace-root", str(self.root)], capture_output=True, text=True)

    def test_approved_set_passes_without_mutation(self) -> None:
        self.state_path.write_text(json.dumps(self.state), encoding="utf-8")
        before = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        result = self.run_gate()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertTrue(json.loads(result.stdout)["passed"])
        after = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.assertEqual(before, after)

    def test_edit_preserved_and_requires_reapproval_even_after_hash_refresh(self) -> None:
        path = self.pages / "SCREEN-002/page-spec.md"
        content = b"# User changes\n\nDifferent mobile workflow.\n"
        path.write_bytes(content)
        self.state["page_specifications"][1]["content_hash"] = hashlib.sha256(content).hexdigest()
        result = self.run_gate()
        self.assertEqual(result.returncode, 1)
        self.assertIn("matching approved content hash", result.stdout)
        self.assertEqual(path.read_bytes(), content)
        self.state["page_specifications"][1]["approved_hash"] = hashlib.sha256(content).hexdigest()
        self.assertEqual(self.errors(), "")

    def test_one_unapproved_page_blocks_entire_set_despite_prototype_approval(self) -> None:
        self.state["page_specifications"][1]["approval_status"] = "needs_user_review"
        self.state["stitch_prototyping"] = {"approved_page_refs": ["SCREEN-001", "SCREEN-002"]}
        self.assertIn("SCREEN-002: explicit written-specification approval", self.errors())

    def test_approval_requires_attribution_and_complete_set_confirmation(self) -> None:
        for key in ("approved_by", "approved_at"):
            with self.subTest(key=key):
                original = self.state["page_specifications"][0][key]
                self.state["page_specifications"][0][key] = " "
                self.assertIn("explicit written-specification approval", self.errors())
                self.state["page_specifications"][0][key] = original
        self.state["page_set_approval"]["approval_status"] = "needs_user_review"
        self.assertIn("approval of the complete page set is missing", self.errors())

    def test_missing_and_duplicate_records_block(self) -> None:
        self.state["page_specifications"] = [self.state["page_specifications"][0]] * 2
        errors = self.errors()
        self.assertIn("duplicate review records", errors)
        self.assertIn("SCREEN-002: missing", errors)

    def test_missing_document_and_index_link_block(self) -> None:
        (self.pages / "SCREEN-001/page-spec.md").unlink()
        (self.pages / "README.md").write_text("# Pages\n", encoding="utf-8")
        errors = self.errors()
        self.assertIn("specification is missing", errors)
        self.assertIn("lacks a relative specification link", errors)

    def test_added_and_removed_screens_invalidate_page_set(self) -> None:
        self.state["screen_system"]["screen_inventory"].append({"screen_id": "SCREEN-003"})
        self.assertIn("page-set approval does not match", self.errors())
        self.assertIn("SCREEN-003: missing", self.errors())
        self.state["screen_system"]["screen_inventory"] = [{"screen_id": "SCREEN-001"}]
        self.assertIn("page-set approval does not match", self.errors())
        self.assertIn("unexpected screen SCREEN-002", self.errors())

    def test_unlisted_blueprint_and_extra_file_block(self) -> None:
        self.state["ui_blueprints"] = [{"page_ref": "SCREEN-003"}]
        path = self.pages / "duplicate/page-spec.md"
        path.parent.mkdir()
        path.write_text("# Duplicate", encoding="utf-8")
        self.assertIn("outside the screen inventory", self.errors())
        self.assertIn("unindexed specification", self.errors())

    def test_malformed_state_and_wrong_paths_block(self) -> None:
        self.state["page_specifications"][0]["document_path"] = "../elsewhere.md"
        self.assertIn("document_path must be", self.errors())
        self.state["page_set_approval"] = []
        self.assertIn("approval of the complete page set is missing", self.errors())
        self.state["screen_system"] = []
        self.assertIn("must list every in-scope screen", self.errors())

    def test_schema_accepts_review_records_and_rejects_invalid_status(self) -> None:
        repository = SCRIPTS.parents[3]
        schema = repository / "System-References/Schemas/stage-4-output.schema.json"
        # Common stage fields are exercised by the readiness fixture; inspect review errors here.
        errors = validate_schema(self.state, schema, repository)
        self.assertFalse(any("page_specifications" in error or "page_set_approval" in error for error in errors), errors)
        self.state["page_specifications"][0]["approval_status"] = "assumed_low_risk"
        self.assertTrue(any("approval_status" in error for error in validate_schema(self.state, schema, repository)))


if __name__ == "__main__":
    unittest.main()
