from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[4]
SCRIPT_PATH = REPOSITORY_ROOT / ".opencode/Skills/skill-registry-builder/scripts/normalize_skill_frontmatter.py"
SPEC = importlib.util.spec_from_file_location("normalize_skill_frontmatter", SCRIPT_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class SkillPackageTests(unittest.TestCase):
    def test_every_skill_has_required_frontmatter(self) -> None:
        skills_dir = REPOSITORY_ROOT / ".opencode/Skills"
        errors: list[str] = []
        for folder in sorted(path for path in skills_dir.iterdir() if path.is_dir() and not path.name.startswith(".")):
            path = MODULE.skill_file(folder)
            if path is None:
                errors.append(f"{folder}: missing skill.md")
            else:
                errors.extend(MODULE.validate(path))
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
