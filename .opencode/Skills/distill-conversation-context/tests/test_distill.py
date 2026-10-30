from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from typing import Any, Protocol, cast


SCRIPT_PATH = Path(__file__).parents[1] / "scripts" / "distill.py"
SPEC = importlib.util.spec_from_file_location("distill", SCRIPT_PATH)
assert SPEC and SPEC.loader


class DistillModule(Protocol):
    def run(
        self,
        root: Path = Path("."),
        force: bool = False,
        dry_run: bool = False,
        no_synthesize: bool = False,
    ) -> dict[str, Any]: ...


distill_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(distill_module)
distill = cast(DistillModule, distill_module)


class DistillSkillTests(unittest.TestCase):
    def make_workspace(self, content: str = "") -> tuple[tempfile.TemporaryDirectory[str], Path]:
        temporary = tempfile.TemporaryDirectory()
        root = Path(temporary.name)
        source = root / "Memory" / "Context Thread archive"
        source.mkdir(parents=True)
        if content:
            (source / "conversation.md").write_text(content, encoding="utf-8")
        return temporary, root

    def test_processes_report_registry_and_project_state(self) -> None:
        temporary, root = self.make_workspace(
            "# Conversation\n\nThe user decided to use Python.\n\n"
            "An error occurred.\nThe issue was fixed."
        )
        try:
            stats = distill.run(root=root)
            self.assertEqual(stats["processed"], 1)
            report = root / "Memory" / "Distilled Context threads" / "conversation-distilled.md"
            self.assertTrue(report.exists())
            self.assertIn("## Unresolved Problems", report.read_text(encoding="utf-8"))
            registry = json.loads((root / "Memory" / "processed-files.json").read_text(encoding="utf-8"))
            self.assertEqual(len(registry["processed"]), 1)
            self.assertTrue((root / "Memory" / "project-state.md").exists())
            self.assertFalse((root / "Memory" / "synthesis-prompt.md").exists())
        finally:
            temporary.cleanup()

    def test_unchanged_file_is_skipped_without_duplicate_report(self) -> None:
        temporary, root = self.make_workspace("The user approved the plan.")
        try:
            first = distill.run(root=root)
            second = distill.run(root=root)
            self.assertEqual(first["processed"], 1)
            self.assertEqual(second["processed"], 0)
            self.assertEqual(second["skipped"], 1)
            reports = list((root / "Memory" / "Distilled Context threads").glob("*.md"))
            self.assertEqual(len(reports), 1)
        finally:
            temporary.cleanup()

    def test_dry_run_does_not_write_log_or_outputs(self) -> None:
        temporary, root = self.make_workspace("The user approved the plan.")
        try:
            stats = distill.run(root=root, dry_run=True)
            self.assertEqual(stats["processed"], 0)
            self.assertFalse((root / "Memory" / "processed-files.json").exists())
            self.assertFalse((root / "Memory" / "processing-log.md").exists())
            self.assertFalse((root / "Memory" / "project-state.md").exists())
        finally:
            temporary.cleanup()

    def test_malformed_registry_fails_loudly(self) -> None:
        temporary, root = self.make_workspace("The user approved the plan.")
        try:
            registry = root / "Memory" / "processed-files.json"
            registry.write_text("{not json", encoding="utf-8")
            with self.assertRaises(ValueError):
                distill.run(root=root)
        finally:
            temporary.cleanup()


if __name__ == "__main__":
    unittest.main()
