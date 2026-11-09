from __future__ import annotations

from html.parser import HTMLParser
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

SKILL = Path(__file__).resolve().parents[1]
ROOT = SKILL.parents[2]
sys.path.insert(0, str(SKILL / "scripts"))
from collect_health_evidence import collect, run_suite, snapshot, STATE_SCHEMAS
from render_patch_plan import render_html, split_blocks

REPORT = """Diagnostic date: **2030-01-02**.
Overall harness health: **81 / 100 — B**.
| All repository Python suites | **7 passed; 0 failed** |
## Open Findings
### RISK-HEALTH-500 — Example
"""
PLAN = """# Stage 1-8 A-Grade Improvement Patch Plan
# Purpose
A source document, never an automatic grade.
# Current Health Baseline
| Item | Status |
| --- | --- |
| Example | **Open** |
# Patch 2 — Old design
# Objective
Historical example.
# Patch 37 — New work
## Implementation Status
- Planned; not implemented.
## Changes
- Escape `<script>alert('x')</script>`.
```json
{"literal": "<tag>", "value": "A | B"}
```
# Implementation Strategy
Review the open work.
"""


class DocumentParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(); self.ids = []; self.anchors = []; self.patches = []
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if "id" in values: self.ids.append(values["id"])
        if tag == "a" and values.get("href", "").startswith("#"): self.anchors.append(values["href"][1:])
        if tag == "details" and "data-patch" in values: self.patches.append(values["data-patch"])


class HealthSkillTests(unittest.TestCase):
    def test_new_patch_numbers_metrics_and_source_content(self) -> None:
        page = render_html(PLAN, REPORT)
        self.assertIn("81 / 100", page)
        self.assertIn("7 passed; 0 failed", page)
        self.assertIn("2030-01-02", page)
        self.assertIn("Showing all 2 patches", page)
        self.assertIn('id="patch-37" data-patch="37" open', page)
        self.assertIn("&lt;script&gt;", page)
        self.assertIn('&quot;value&quot;: &quot;A | B&quot;', page)
        parser = DocumentParser(); parser.feed(page)
        self.assertEqual(parser.patches, ["37", "2"])
        self.assertEqual(len(parser.ids), len(set(parser.ids)))
        self.assertTrue(set(parser.anchors) <= set(parser.ids))

    def test_missing_metrics_are_not_invented(self) -> None:
        page = render_html(PLAN, "No completed assessment")
        self.assertIn("Not assessed", page)
        self.assertIn("Not recorded", page)
        self.assertNotIn("88 / 100", page)

    def test_duplicate_patches_and_unclosed_fences_are_rejected(self) -> None:
        for content in (PLAN + "\n# Patch 37 — Duplicate\n", PLAN + "\n```json\n{}"):
            with self.assertRaises(ValueError): split_blocks(content)

    def test_current_plan_content_is_preserved(self) -> None:
        docs = ROOT / "System-References/Docs"
        source = (docs / "Stage-1-8-A-Grade-Improvement-Patch-Plan.md").read_text()
        blocks = split_blocks(source)
        page = render_html(source, (docs / "Stage-1-8 Health Report.mdx").read_text())
        for block in blocks:
            self.assertIn(block["body"], page)
        parser = DocumentParser(); parser.feed(page)
        self.assertEqual(len(parser.patches), sum(bool(b["number"]) for b in blocks))
        self.assertTrue(set(parser.anchors) <= set(parser.ids))

    def workspace(self, root: Path) -> Path:
        shutil.copytree(ROOT / "System-References/Schemas", root / "System-References/Schemas")
        status = root / "Build-Plans/Build-status"; status.mkdir(parents=True)
        for filename in STATE_SCHEMAS:
            shutil.copyfile(ROOT / "Build-Plans/Build-status" / filename, status / filename)
        (status / "Global-workflow-state.json").write_text('{"stages": {}}')
        skill = root / ".opencode/Skills/example"; skill.mkdir(parents=True)
        (skill / "skill.md").write_text('---\nname: example\ndescription: A test fixture skill.\ncompatibility: opencode\n---\n')
        return skill

    def test_collection_preserves_baseline_and_reports_skips_and_bad_json(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary); self.workspace(root)
            (root / "bad.json").write_text("{")
            before = snapshot(root)
            data = collect(root, run_tests=False)
            self.assertEqual(data["test_summary"]["status"], "not_run")
            self.assertEqual(data["json"]["errors"][0]["path"], "bad.json")
            self.assertEqual(data["skill_metadata"]["packages_checked"], 1)
            self.assertEqual(len(data["stages"]), 8)
            self.assertTrue(data["build_plans_unchanged"])
            self.assertEqual(before, snapshot(root))
            self.assertTrue(all(check["status"] == "passed" for check in data["seed_registry_schemas"]))

    def test_failing_suite_is_recorded_without_being_claimed_passed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary); skill = self.workspace(root)
            tests = skill / "tests"; tests.mkdir()
            (tests / "test_bad.py").write_text('import unittest\nclass Example(unittest.TestCase):\n def test_bad(self): self.fail("deliberate fixture failure")\n')
            data = collect(root)
            self.assertEqual(data["test_summary"]["status"], "failed")
            self.assertEqual(data["test_summary"]["tests_run"], 1)
            self.assertIn("deliberate fixture failure", data["test_suites"][0]["output"])

    def test_suite_timeout_is_not_a_pass(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary); tests = root / "tests"; tests.mkdir()
            (tests / "test_slow.py").write_text('import time\ntime.sleep(10)\n')
            result = run_suite(root, tests, .05)
            self.assertEqual(result["status"], "timeout")
            self.assertIsNone(result["exit_code"])


if __name__ == "__main__":
    unittest.main()
