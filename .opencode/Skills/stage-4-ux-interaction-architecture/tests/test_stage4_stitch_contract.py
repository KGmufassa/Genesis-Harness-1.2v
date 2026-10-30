from __future__ import annotations

import json
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[4]


class Stage4StitchContractTests(unittest.TestCase):
    def _read(self, relative_path: str) -> str:
        return (REPOSITORY_ROOT / relative_path).read_text(encoding="utf-8")

    def test_stage_4_schema_supports_stitch_visual_source_control(self) -> None:
        schema = json.loads(
            self._read("System-References/Schemas/stage-4-output.schema.json")
        )
        stitch_def = schema["$defs"]["stitch_prototyping"]["properties"]
        visual_source = schema["$defs"]["stitch_visual_source_control"]["properties"]

        self.assertIn("stitch_prototyping", schema["properties"])
        self.assertIn("visual_source_control", stitch_def)
        self.assertIn("suggestion_review_ledger", stitch_def)
        self.assertEqual(visual_source["scope"]["const"], "visual_only")
        self.assertIn("excluded_from", visual_source)

    def test_stage_4_command_keeps_stitch_visual_only(self) -> None:
        command = self._read(".opencode/Skills/stage-4-ux-interaction-architecture/skill.md")

        self.assertIn("visual_source_control", command)
        self.assertIn("suggestion_review_ledger", command)
        self.assertIn("visual-only", command)
        self.assertIn("Stage 5 handoff impact is `none`", command)
        self.assertIn("Build-Plans/Stage-4/Screen-shots/", command)
        self.assertIn("read-only capability preflight", command)
        self.assertIn("screen generate/update", command)

    def test_stage_4_consumers_reference_stitch_visual_source_boundary(self) -> None:
        synthesis = self._read(".opencode/Skills/ux-interaction-synthesis/skill.md")
        design_system = self._read(".opencode/Skills/design-system-foundation/skill.md")
        ui_blueprint = self._read(".opencode/Skills/ui-blueprint-specification/skill.md")

        self.assertIn("Stitch-specific metadata remains Stage-4-local", synthesis)
        self.assertIn("locked screenshot evidence", design_system)
        self.assertIn("visual-only guidance", ui_blueprint)
        self.assertIn("not use Stitch to add or change product scope", ui_blueprint)
        self.assertIn("Stage 5 handoff fields", ui_blueprint)


if __name__ == "__main__":
    unittest.main()
