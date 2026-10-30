#!/usr/bin/env python3
"""Convert a markdown document and mapping file into a skill package."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


HEADING_RE = re.compile(r"^# (.+)$", re.MULTILINE)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert a structured markdown document into a skill package."
    )
    parser.add_argument("--source-doc", required=True, help="Path to the source markdown file.")
    parser.add_argument("--mapping-file", required=True, help="Path to the mapping markdown file.")
    parser.add_argument(
        "--target-root",
        default=".opencode/skills",
        help="Root directory where the skill package will be created.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite an existing target skill package.",
    )
    return parser.parse_args()


def parse_mapping(mapping_text: str) -> tuple[str, list[str]]:
    package_name: str | None = None
    refs: list[str] = []

    for raw_line in mapping_text.splitlines():
        line = raw_line.rstrip()
        if not line:
            continue

        match_root = re.search(r"([A-Za-z0-9._-]+)/\s*$", line)
        if package_name is None and match_root:
            candidate = match_root.group(1)
            if candidate != "references":
                package_name = candidate
                continue

        match_ref = re.search(r"(references/[A-Za-z0-9._/-]+\.md)\s*$", line)
        if match_ref:
            refs.append(match_ref.group(1))
            continue

        match_ref_leaf = re.search(r"([A-Za-z0-9._-]+\.md)\s*$", line)
        if "references" in line and match_ref_leaf:
            refs.append(f"references/{match_ref_leaf.group(1)}")

    if not package_name:
        raise ValueError("Could not determine skill package name from mapping file.")
    if not refs:
        raise ValueError("Could not determine mapped reference files from mapping file.")
    return package_name, refs


def split_top_level_sections(source_text: str) -> list[str]:
    matches = list(HEADING_RE.finditer(source_text))
    if not matches:
        raise ValueError("Source document does not contain top-level headings.")

    sections: list[str] = []
    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(source_text)
        section = source_text[start:end].strip()
        if section:
            sections.append(section + "\n")
    return sections


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> int:
    args = parse_args()

    source_doc = Path(args.source_doc)
    mapping_file = Path(args.mapping_file)
    target_root = Path(args.target_root)

    if not source_doc.is_file():
        print(f"Source document not found: {source_doc}", file=sys.stderr)
        return 1
    if not mapping_file.is_file():
        print(f"Mapping file not found: {mapping_file}", file=sys.stderr)
        return 1

    try:
        package_name, ref_paths = parse_mapping(mapping_file.read_text(encoding="utf-8"))
        sections = split_top_level_sections(source_doc.read_text(encoding="utf-8"))
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    if len(sections) < 2:
        print("Source document must contain at least two top-level sections.", file=sys.stderr)
        return 1

    if len(ref_paths) != len(sections) - 1:
        print(
            "Mapped reference count does not match source top-level sections after the first.",
            file=sys.stderr,
        )
        print(
            f"Expected {len(sections) - 1} references, found {len(ref_paths)} in mapping.",
            file=sys.stderr,
        )
        return 1

    package_dir = target_root / package_name
    if package_dir.exists() and not args.force:
        print(
            f"Target skill package already exists: {package_dir}. Use --force to overwrite.",
            file=sys.stderr,
        )
        return 1

    if args.force and package_dir.exists():
        for child in sorted(package_dir.rglob("*"), reverse=True):
            if child.is_file():
                child.unlink()
            elif child.is_dir():
                child.rmdir()

    write_file(package_dir / "SKILL.md", sections[0])
    for section, ref_path in zip(sections[1:], ref_paths):
        write_file(package_dir / ref_path, section)

    print(f"Created skill package: {package_dir}")
    print(f"Wrote SKILL.md and {len(ref_paths)} reference files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
