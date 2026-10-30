#!/usr/bin/env python3
"""
Distill Conversation Context Skill
Converts archived AI conversations into structured distilled reports with duplicate prevention.
"""

import argparse
import hashlib
import json
import re
import sys
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Any

# ============================================================================
# CONSTANTS & PATHS (set at runtime in run())
# ============================================================================
SOURCE_DIR: Path
DISTILLED_DIR: Path
REGISTRY_PATH: Path
LOG_PATH: Path
REPORT_TEMPLATE_PATH: Path
PROJECT_STATE_TEMPLATE_PATH: Path
SYNTHESIS_PROMPT_TEMPLATE_PATH: Path
PROJECT_STATE_OUTPUT: Path

# ============================================================================
# REGEX PATTERNS FOR HEURISTIC EXTRACTION
# ============================================================================
PATTERNS = {
    "state_changes": re.compile(r"(?i)\b(changed|updated|migrated|switched|replaced)\b"),
    "locked_decisions": re.compile(r"(?i)\b(decided|final|locked|approved)\b"),
    "new_knowledge": re.compile(r"(?i)\b(learned|discovered|found that|realized)\b"),
    "problem_indicators": re.compile(r"(?i)\b(error|failed|issue|bug|broken)\b"),
    "resolution_indicators": re.compile(r"(?i)\b(fixed|resolved|solved|workaround)\b"),
    "user_preferences": re.compile(r"(?i)\b(prefer|always|never|standard|convention)\b"),
    "entities": re.compile(
        r"\b(?:[A-Z][A-Za-z]+(?:Project|Service|Model|Lib|API|SDK)|"
        r"[A-Z][A-Za-z]+\s+(?:Project|Service|Model|Lib|API|SDK))\b"
    ),
    "files": re.compile(r"(?:[\w./-]+)\.(?:md|py|json|yaml|toml|txt)\b"),
}


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================
def sha256_file(path: Path) -> str:
    """Compute SHA256 hash of file content."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_registry() -> dict[str, Any]:
    """Load processed-files.json registry."""
    if REGISTRY_PATH.exists():
        try:
            registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise ValueError(f"Malformed registry JSON: {REGISTRY_PATH}") from exc
        if not isinstance(registry, dict) or not isinstance(registry.get("processed"), list):
            raise ValueError(f"Invalid registry structure: {REGISTRY_PATH}")
        for entry in registry["processed"]:
            if not isinstance(entry, dict) or not isinstance(entry.get("hash"), str):
                raise ValueError(f"Invalid registry entry: {REGISTRY_PATH}")
        return registry
    return {"processed": []}


def save_registry_atomic(registry: dict) -> None:
    """Write registry atomically."""
    REGISTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", dir=REGISTRY_PATH.parent, delete=False, suffix=".tmp"
    ) as f:
        json.dump(registry, f, indent=2)
        f.flush()
        temp_path = Path(f.name)
    temp_path.replace(REGISTRY_PATH)


def append_log(line: str) -> None:
    """Append line to processing log."""
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(line + "\n")


def load_template(path: Path) -> str:
    """Load markdown template file."""
    if not path.exists():
        raise FileNotFoundError(f"Template not found: {path}")
    return path.read_text(encoding="utf-8")


def extract_paragraphs(text: str, max_paras: int = 3) -> str:
    """Extract the first substantive non-empty paragraphs."""
    paras = []
    for paragraph in text.split("\n\n"):
        cleaned = paragraph.strip()
        if not cleaned or cleaned.startswith("#"):
            continue
        if all(line.lstrip().startswith("**") for line in cleaned.splitlines()):
            continue
        paras.append(cleaned)
    return "\n\n".join(paras[:max_paras])


def grep_lines(text: str, pattern: re.Pattern) -> list[str]:
    """Return lines matching pattern."""
    return [line.strip() for line in text.split("\n") if pattern.search(line)]


def unique_preserve_order(items: list[str]) -> list[str]:
    """Deduplicate while preserving first occurrence order."""
    seen = set()
    out = []
    for item in items:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out


# ============================================================================
# STAGE 1: INVENTORY
# ============================================================================
def stage_inventory() -> list[Path]:
    """Find all .md files in source directory."""
    if not SOURCE_DIR.exists():
        raise FileNotFoundError(f"Source directory not found: {SOURCE_DIR}")
    files = sorted(SOURCE_DIR.glob("*.md"))
    return files


# ============================================================================
# STAGE 2: DUPLICATE PREVENTION
# ============================================================================
def stage_duplicate_prevention(
    files: list[Path], registry: dict, force: bool
) -> tuple[list[tuple[Path, str]], list[Path]]:
    """Return (to_process, skipped) where to_process = [(file, hash), ...]."""
    to_process = []
    skipped = []
    processed_hashes = {e["hash"] for e in registry.get("processed", [])}

    for f in files:
        h = sha256_file(f)
        if force or h not in processed_hashes:
            to_process.append((f, h))
        else:
            skipped.append(f)

    return to_process, skipped


# ============================================================================
# STAGE 3: CONVERSATION ANALYSIS
# ============================================================================
def stage_conversation_analysis(content: str, filepath: Path) -> dict[str, Any]:
    """Extract 9 categories via heuristics."""

    # Summary: first 3 non-empty paragraphs
    summary = extract_paragraphs(content, 3)

    # State Changes
    state_changes = grep_lines(content, PATTERNS["state_changes"])

    # Locked Decisions (exclude brainstorming)
    locked = grep_lines(content, PATTERNS["locked_decisions"])
    locked = [
        decision_line
        for decision_line in locked
        if not re.search(r"(?i)maybe|draft|consider", decision_line)
    ]

    # New Knowledge
    new_knowledge = grep_lines(content, PATTERNS["new_knowledge"])

    # Resolved and unresolved problems: pair only nearby, related lines.
    resolved = []
    unresolved = []
    lines = content.split("\n")
    for i, line in enumerate(lines):
        if PATTERNS["problem_indicators"].search(line):
            matched = False
            for j in range(i, min(i + 4, len(lines))):
                if PATTERNS["resolution_indicators"].search(lines[j]):
                    resolved.append(f"{line.strip()} → {lines[j].strip()}")
                    matched = True
                    break
            if not matched:
                unresolved.append(line.strip())

    # Repeated Mistakes: duplicate normalized problem lines.
    error_lines = grep_lines(content, PATTERNS["problem_indicators"])
    seen: dict[str, int] = {}
    for line in error_lines:
        key = re.sub(r"[^a-z0-9 ]", "", line.lower())
        key = re.sub(r"\s+", " ", key).strip()[:100]
        seen[key] = seen.get(key, 0) + 1
    repeated = [f"{k} (x{v})" for k, v in seen.items() if v >= 2]

    # User Preferences
    prefs = grep_lines(content, PATTERNS["user_preferences"])

    # Entities
    entities = unique_preserve_order(PATTERNS["entities"].findall(content))

    # Files
    files = unique_preserve_order(PATTERNS["files"].findall(content))

    return {
        "summary": summary,
        "state_changes": state_changes or [],
        "locked_decisions": locked or [],
        "new_knowledge": new_knowledge or [],
        "resolved_problems": resolved or [],
        "unresolved_problems": unique_preserve_order(unresolved),
        "repeated_mistakes": repeated or [],
        "user_preferences": prefs or [],
        "entities": entities or [],
        "files": files or [],
    }


# ============================================================================
# STAGE 4: REPORT GENERATION
# ============================================================================
def stage_generate_report(source_path: Path, analysis: dict, conversation_date: str) -> Path:
    """Render template and write to distilled dir."""
    DISTILLED_DIR.mkdir(parents=True, exist_ok=True)

    template = load_template(REPORT_TEMPLATE_PATH)

    def fmt_list(items: list[str]) -> str:
        if not items:
            return "None captured"
        return "\n".join(f"- {item}" for item in items)

    rendered = template.format(
        source_filename=source_path.name,
        processed_timestamp=datetime.now().isoformat(timespec="seconds"),
        conversation_date=conversation_date,
        summary=analysis["summary"],
        state_changes=fmt_list(analysis["state_changes"]),
        locked_decisions=fmt_list(analysis["locked_decisions"]),
        new_knowledge=fmt_list(analysis["new_knowledge"]),
        resolved_problems=fmt_list(analysis["resolved_problems"]),
        unresolved_problems=fmt_list(analysis["unresolved_problems"]),
        repeated_mistakes=fmt_list(analysis["repeated_mistakes"]),
        user_preferences=fmt_list(analysis["user_preferences"]),
        entities=fmt_list(analysis["entities"]),
        files=fmt_list(analysis["files"]),
    )

    out_name = f"{source_path.stem}-distilled.md"
    out_path = DISTILLED_DIR / out_name
    out_path.write_text(rendered, encoding="utf-8")
    return out_path


# ============================================================================
# STAGE 5: REGISTRY UPDATE
# ============================================================================
def stage_update_registry(registry: dict, source_path: Path, file_hash: str, distilled_name: str) -> None:
    """Upsert entry to registry atomically (replace if same filename)."""
    mtime = datetime.fromtimestamp(source_path.stat().st_mtime).isoformat(timespec="seconds")
    entry = {
        "filename": source_path.name,
        "hash": file_hash,
        "created": mtime,
        "distilled": distilled_name,
    }
    processed = registry.setdefault("processed", [])
    # Replace existing entry with same filename
    processed[:] = [e for e in processed if e["filename"] != source_path.name]
    processed.append(entry)
    save_registry_atomic(registry)


# ============================================================================
# STAGE 6: LOG APPEND
# ============================================================================
def stage_log(source_path: Path, status: str, detail: str) -> None:
    """Append one line to processing log."""
    ts = datetime.now().isoformat(timespec="seconds")
    append_log(f"{ts} | {source_path.name} | {status} | {detail}")


# ============================================================================
# STAGE 7: PROJECT STATE SYNTHESIS (prompt contract + deterministic renderer)
# ============================================================================
def stage_synthesize_project_state(distilled_dir: Path) -> None:
    """Generate project state using the reusable synthesis prompt contract."""
    reports = sorted(distilled_dir.glob("*-distilled.md"))
    if not reports:
        return

    report_text = "\n\n".join(
        f"### {report.name}\n{report.read_text(encoding='utf-8')}" for report in reports
    )
    synthesis_prompt = load_template(SYNTHESIS_PROMPT_TEMPLATE_PATH).format(
        source_count=len(reports),
        distilled_context=report_text,
    )
    if "## Required Output" not in synthesis_prompt:
        raise ValueError("Synthesis prompt template is missing Required Output instructions")

    all_data = []
    for r in reports:
        text = r.read_text(encoding="utf-8")
        source_match = re.search(r"\*\*Source File\*\*: (.+)", text)
        date_match = re.search(r"\*\*Conversation Date\*\*: (.+)", text)
        source = source_match.group(1) if source_match else r.name
        date = date_match.group(1) if date_match else ""

        sections = {}
        current = None
        for line in text.split("\n"):
            if line.startswith("## "):
                current = line[3:].strip()
                sections[current] = []
            elif current and line.strip() and not line.startswith("#") and line.strip() != "---":
                if line.strip() != "None captured":
                    sections[current].append(line.strip())

        all_data.append({"source": source, "date": date, "sections": sections})

    all_data.sort(key=lambda x: x["date"])

    merged = {
        "current_architecture": "None captured",
        "current_stack": "None captured",
        "active_features": [],
        "deprecated_features": [],
        "current_priorities": [],
        "known_constraints": [],
        "active_risks": [],
        "unresolved_questions": [],
        "next_recommended_steps": [],
    }

    for data in all_data:
        sec = data["sections"]

        def strip_bullet(s: str) -> str:
            return s[2:] if s.startswith("- ") else s

        def evidence(s: str) -> str:
            return f"[medium] {s} (Source: `{data['source']}`)"

        # State Changes -> Architecture/Stack
        for item in sec.get("State Changes", []):
            clean = strip_bullet(item)
            if "architect" in clean.lower():
                merged["current_architecture"] = evidence(clean)
            if any(k in clean.lower() for k in ["stack", "language", "framework", "database", "switched", "go", "python", "rust", "node", "java"]):
                merged["current_stack"] = evidence(clean)

        # Locked Decisions -> Architecture/Stack/Features
        for item in sec.get("Locked Decisions", []):
            clean = strip_bullet(item)
            if "architect" in clean.lower():
                merged["current_architecture"] = evidence(clean)
            if any(k in clean.lower() for k in ["stack", "language", "framework", "database", "switched", "go", "python", "rust", "node", "java"]):
                merged["current_stack"] = evidence(clean)

        # New Knowledge -> Constraints
        merged["known_constraints"].extend(
            evidence(strip_bullet(x)) for x in sec.get("New Knowledge", [])
        )

        # Active/Deprecated Features
        for item in sec.get("State Changes", []):
            clean = strip_bullet(item)
            if "removed" in clean.lower() or "deprecat" in clean.lower() or "dropped" in clean.lower():
                merged["deprecated_features"].append(evidence(clean))
            elif "added" in clean.lower() or "new" in clean.lower() or "implement" in clean.lower():
                merged["active_features"].append(evidence(clean))

        # Priorities are only extracted from explicitly priority-oriented lines.
        priority_lines = [
            evidence(strip_bullet(x))
            for x in sec.get("Locked Decisions", [])
            if re.search(r"(?i)priority|prioritize|focus|next", x)
        ]
        merged["current_priorities"].extend(priority_lines)

        # Unresolved questions and problems remain visible to the next agent.
        merged["unresolved_questions"].extend(
            evidence(strip_bullet(p)) for p in sec.get("Unresolved Problems", [])
        )
        merged["active_risks"].extend(
            evidence(strip_bullet(p)) for p in sec.get("Repeated Mistakes", [])
        )

        # Next steps are inferred only from explicit action language.
        action_lines = [
            evidence(strip_bullet(x))
            for x in sec.get("State Changes", []) + sec.get("Locked Decisions", [])
            if re.search(r"(?i)next|implement|add|build|resolve|investigate|follow up", x)
        ]
        merged["next_recommended_steps"].extend(action_lines)

    # Deduplicate arrays
    for key in [
        "active_features",
        "deprecated_features",
        "known_constraints",
        "active_risks",
        "unresolved_questions",
        "next_recommended_steps",
    ]:
        merged[key] = unique_preserve_order(merged[key])

    # Render template
    template = load_template(PROJECT_STATE_TEMPLATE_PATH)

    def fmt(key: str) -> str:
        val = merged[key]
        if isinstance(val, list):
            return "\n".join(f"- {v}" for v in val) if val else "None captured"
        return val if val else "None captured"

    date_range = "N/A"
    if all_data:
        date_range = f"{all_data[0]['date']} to {all_data[-1]['date']}"

    rendered = template.format(
        timestamp=datetime.now().isoformat(timespec="seconds"),
        source_count=len(reports),
        date_range=date_range,
        current_architecture=fmt("current_architecture"),
        current_stack=fmt("current_stack"),
        active_features=fmt("active_features"),
        deprecated_features=fmt("deprecated_features"),
        current_priorities=fmt("current_priorities"),
        known_constraints=fmt("known_constraints"),
        active_risks=fmt("active_risks"),
        unresolved_questions=fmt("unresolved_questions"),
        next_recommended_steps=fmt("next_recommended_steps"),
    )

    PROJECT_STATE_OUTPUT.write_text(rendered, encoding="utf-8")


# ============================================================================
# MAIN ORCHESTRATOR
# ============================================================================
def run(
    root: Path = Path("."),
    force: bool = False,
    dry_run: bool = False,
    no_synthesize: bool = False,
) -> dict[str, Any]:
    """Main entry point. Returns stats dict."""
    global SOURCE_DIR, DISTILLED_DIR, REGISTRY_PATH, LOG_PATH, PROJECT_STATE_OUTPUT
    global REPORT_TEMPLATE_PATH, PROJECT_STATE_TEMPLATE_PATH, SYNTHESIS_PROMPT_TEMPLATE_PATH

    skill_root = Path(__file__).resolve().parents[1]
    REPORT_TEMPLATE_PATH = skill_root / "references" / "report-template.md"
    PROJECT_STATE_TEMPLATE_PATH = skill_root / "references" / "project-state-template.md"
    SYNTHESIS_PROMPT_TEMPLATE_PATH = skill_root / "references" / "synthesis-prompt.md"

    SOURCE_DIR = root / "Memory/Context Thread archive"
    DISTILLED_DIR = root / "Memory/Distilled Context threads"
    REGISTRY_PATH = root / "Memory/processed-files.json"
    LOG_PATH = root / "Memory/processing-log.md"
    PROJECT_STATE_OUTPUT = root / "Memory/project-state.md"

    stats = {"processed": 0, "skipped": 0, "errors": []}

    # Stage 1
    files = stage_inventory()
    if not files:
        print("No conversation files found.")
        return stats

    # Stage 2
    registry = load_registry()
    to_process, skipped = stage_duplicate_prevention(files, registry, force)
    stats["skipped"] = len(skipped)

    if not dry_run:
        for f in skipped:
            stage_log(f, "SKIPPED", "unchanged (hash match)")

    # Stages 3-6 per file
    for source_path, file_hash in to_process:
        try:
            content = source_path.read_text(encoding="utf-8")
            mtime = datetime.fromtimestamp(source_path.stat().st_mtime).isoformat(timespec="seconds")

            if dry_run:
                print(f"Would process: {source_path.name}")
                continue

            # Stage 3
            analysis = stage_conversation_analysis(content, source_path)

            # Stage 4
            out_path = stage_generate_report(source_path, analysis, mtime)

            # Stage 5
            stage_update_registry(registry, source_path, file_hash, out_path.name)

            # Stage 6
            stage_log(source_path, "PROCESSED", out_path.name)

            stats["processed"] += 1

        except Exception as e:
            stats["errors"].append(f"{source_path.name}: {e}")
            stage_log(source_path, "ERROR", str(e))

    # Stage 7
    if not dry_run and not no_synthesize and (stats["processed"] > 0 or DISTILLED_DIR.exists()):
        try:
            stage_synthesize_project_state(DISTILLED_DIR)
        except Exception as e:
            stats["errors"].append(f"synthesis: {e}")

    return stats


def main() -> int:
    parser = argparse.ArgumentParser(description="Distill conversation context into structured reports.")
    parser.add_argument("--force", action="store_true", help="Reprocess all files (ignore registry)")
    parser.add_argument("--dry-run", action="store_true", help="Show actions without writing")
    parser.add_argument("--no-synthesize", action="store_true", help="Skip Stage 7 project state synthesis")
    args = parser.parse_args()

    try:
        stats = run(force=args.force, dry_run=args.dry_run, no_synthesize=args.no_synthesize)
    except Exception as e:
        print(f"Fatal error: {e}", file=sys.stderr)
        return 1

    print(f"Processed: {stats['processed']}")
    print(f"Skipped: {stats['skipped']}")
    if stats["errors"]:
        print(f"Errors: {len(stats['errors'])}")
        for err in stats["errors"]:
            print(f"  - {err}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
