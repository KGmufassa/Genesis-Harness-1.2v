#!/usr/bin/env python3
"""Validate or minimally repair Genesis skill frontmatter."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Sequence


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate Genesis skill package metadata.")
    parser.add_argument("--skills-dir", default=".opencode/Skills")
    parser.add_argument("--fix", action="store_true")
    return parser.parse_args()


def skill_file(folder: Path) -> Path | None:
    for name in ("skill.md", "SKILL.md"):
        path = folder / name
        if path.is_file():
            return path
    return None


def _plain_description(content: str, folder_name: str) -> str:
    lines = content.splitlines()
    start = next((index + 1 for index, line in enumerate(lines) if line.strip().lower() == "# purpose"), 0)
    paragraph: list[str] = []
    for line in lines[start:]:
        stripped = line.strip()
        if paragraph and (stripped.startswith("#") or stripped == "---"):
            break
        if not stripped or stripped.startswith(("```", "* ", "- ")):
            if paragraph:
                break
            continue
        paragraph.append(stripped)
    text = " ".join(paragraph)
    text = re.sub(r"[`*_]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        text = f"Use for {folder_name.replace('-', ' ')} tasks in the Genesis workflow."
    if len(text) > 240:
        text = text[:237].rsplit(" ", 1)[0] + "..."
    return text.replace(":", " -")


def normalize(path: Path) -> bool:
    content = path.read_text(encoding="utf-8")
    if content.startswith("---\n"):
        end = content.find("\n---\n", 4)
        if end == -1:
            raise ValueError(f"Unclosed frontmatter: {path}")
        frontmatter = content[4:end]
        missing = []
        if not re.search(r"(?m)^name:\s*\S", frontmatter):
            missing.append(f"name: {path.parent.name}")
        if not re.search(r"(?m)^description:\s*(?:\S|>)", frontmatter):
            missing.append(f"description: {_plain_description(content[end + 5:], path.parent.name)}")
        if not re.search(r"(?m)^compatibility:\s*opencode\s*$", frontmatter):
            missing.append("compatibility: opencode")
        if not missing:
            return False
        updated = content[:end] + "\n" + "\n".join(missing) + content[end:]
    else:
        description = _plain_description(content, path.parent.name)
        updated = (
            "---\n"
            f"name: {path.parent.name}\n"
            f"description: {description}\n"
            "compatibility: opencode\n"
            "---\n\n"
            + content
        )
    path.write_text(updated, encoding="utf-8")
    return True


def validate(path: Path) -> Sequence[str]:
    content = path.read_text(encoding="utf-8")
    errors: list[str] = []
    if not content.startswith("---\n"):
        return [f"{path}: missing YAML frontmatter"]
    end = content.find("\n---\n", 4)
    if end == -1:
        return [f"{path}: unclosed YAML frontmatter"]
    frontmatter = content[4:end]
    for field in ("name", "description", "compatibility"):
        if not re.search(rf"(?m)^{field}:\s*(?:\S|>)", frontmatter):
            errors.append(f"{path}: missing {field}")
    name_match = re.search(r"(?m)^name:\s*(\S+)\s*$", frontmatter)
    if name_match and not re.fullmatch(r"[a-z0-9-]+", name_match.group(1)):
        errors.append(f"{path}: name must be lowercase kebab-case")
    if not re.search(r"(?m)^compatibility:\s*opencode\s*$", frontmatter):
        errors.append(f"{path}: compatibility must be opencode")
    return errors


def main() -> int:
    args = parse_args()
    skills_dir = Path(args.skills_dir)
    paths = [skill_file(folder) for folder in sorted(skills_dir.iterdir()) if folder.is_dir() and not folder.name.startswith(".")]
    missing_files = [folder for folder in sorted(skills_dir.iterdir()) if folder.is_dir() and not folder.name.startswith(".") and skill_file(folder) is None]
    if missing_files:
        for folder in missing_files:
            print(f"{folder}: missing skill.md", file=sys.stderr)
        return 1
    changed = 0
    if args.fix:
        changed = sum(normalize(path) for path in paths if path is not None)
    errors = [error for path in paths if path is not None for error in validate(path)]
    for error in errors:
        print(error, file=sys.stderr)
    print(f"Skills checked: {len(paths)}; changed: {changed}; errors: {len(errors)}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
