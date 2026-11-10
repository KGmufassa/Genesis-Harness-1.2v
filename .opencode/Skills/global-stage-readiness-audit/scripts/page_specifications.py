#!/usr/bin/env python3
"""Read-only Stage 4 written page approval gate, also used by readiness audits."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any, Mapping

from workflow_validation import load_json
from page_documents import validate_documents


PAGES = Path("Build-Plans/Stage-4/Pages")


def _approved(record: Mapping[str, Any]) -> bool:
    return record.get("approval_status") == "approved" and all(
        isinstance(record.get(key), str) and record[key].strip()
        for key in ("approved_by", "approved_at")
    )


def validate_page_specifications(root: Path, state: Mapping[str, Any], *, final: bool = False) -> list[str]:
    errors: list[str] = []
    system = state.get("screen_system", {})
    screens = system.get("screen_inventory", []) if isinstance(system, Mapping) else []
    if not isinstance(screens, list) or not screens:
        return ["Page specifications: screen_system.screen_inventory must list every in-scope screen"]
    screen_ids = [item.get("screen_id", "") if isinstance(item, Mapping) else "" for item in screens]
    if any(not isinstance(ref, str) or not re.fullmatch(r"SCREEN-[A-Za-z0-9._-]+", ref) for ref in screen_ids):
        return ["Page specifications: each screen needs a valid stable SCREEN- ID"]
    expected = set(screen_ids)
    if len(expected) != len(screen_ids):
        errors.append("Page specifications: duplicate screen IDs")
    for key in ("page_inventory", "ui_blueprints"):
        inventory = state.get(key, [])
        # lazy: accept the legacy empty object until the blueprint seed migrates to a list.
        if inventory == {}:
            inventory = []
        if not isinstance(inventory, list):
            errors.append(f"Page specifications: {key} must be a list")
            continue
        for page in inventory:
            if not isinstance(page, Mapping) or page.get("page_ref") not in expected:
                errors.append(f"Page specifications: {key} contains a page outside the screen inventory")
    records = state.get("page_specifications", [])
    if not isinstance(records, list):
        return errors + ["Page specifications: page_specifications must be a list"]
    documents: dict[str, str] = {}
    refs: list[str] = []
    index_path = root / PAGES / "README.md"
    try:
        index = index_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        index = ""
        errors.append("Page specifications: Pages/README.md is missing or unreadable")
    for record in records:
        if not isinstance(record, Mapping) or not isinstance(record.get("screen_ref"), str):
            errors.append("Page specifications: malformed review record")
            continue
        ref = record["screen_ref"]
        refs.append(ref)
        if ref not in expected:
            errors.append(f"Page specifications: unexpected screen {ref}")
            continue
        relative = PAGES / ref / "page-spec.md"
        if record.get("document_path") != relative.as_posix():
            errors.append(f"{ref}: document_path must be {relative}")
        path = root / relative
        if not path.resolve().is_relative_to((root / PAGES).resolve()):
            errors.append(f"{ref}: specification resolves outside Pages")
            continue
        try:
            content = path.read_bytes()
            if not content.decode("utf-8").strip():
                errors.append(f"{ref}: specification is empty")
        except (OSError, UnicodeError):
            errors.append(f"{ref}: specification is missing or unreadable")
            continue
        documents[ref] = content.decode("utf-8")
        digest = hashlib.sha256(content).hexdigest()
        if record.get("content_hash") != digest or record.get("approved_hash") != digest:
            errors.append(f"{ref}: specification changed or lacks matching approved content hash")
        if not _approved(record):
            errors.append(f"{ref}: explicit written-specification approval is missing")
        if not re.search(r"\[[^\]\n]+\]\(" + re.escape(f"{ref}/page-spec.md") + r"\)", index):
            errors.append(f"{ref}: Pages/README.md lacks a relative specification link")
    if len(refs) != len(set(refs)):
        errors.append("Page specifications: duplicate review records")
    for ref in sorted(expected - set(refs)):
        errors.append(f"{ref}: missing page specification review record")
    expected_paths = {f"{ref}/page-spec.md" for ref in expected}
    for path in (root / PAGES).rglob("page-spec.md"):
        if path.relative_to(root / PAGES).as_posix() not in expected_paths:
            errors.append(f"Page specifications: unindexed specification {path.relative_to(root)}")
    approval = state.get("page_set_approval", {})
    if not isinstance(approval, Mapping):
        approval = {}
    approved_refs = approval.get("approved_screen_refs", [])
    if not isinstance(approved_refs, list) or sorted(str(ref) for ref in approved_refs) != sorted(expected):
        errors.append("Page specifications: page-set approval does not match the current screen set")
    if not _approved(approval):
        errors.append("Page specifications: explicit approval of the complete page set is missing")
    errors.extend(validate_documents(root, state, documents, final))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace-root", type=Path, default=Path.cwd())
    parser.add_argument("--phase", choices=("draft", "final"), default="draft")
    args = parser.parse_args()
    try:
        state = load_json(args.workspace_root / "Build-Plans/Build-status/UX-state.json")
        errors = validate_page_specifications(args.workspace_root, state, final=args.phase == "final") if isinstance(state, Mapping) else ["UX state must be an object"]
    except (ValueError, OSError, UnicodeError, TypeError, KeyError, AttributeError) as exc:
        errors = [str(exc)]
    print(json.dumps({"passed": not errors, "blocking_gaps": errors}, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
