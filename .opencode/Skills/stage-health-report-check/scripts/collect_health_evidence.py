"""Collect reproducible harness checks without finalizing application stages."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from typing import Any

SKILLS = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(SKILLS / "global-stage-readiness-audit/scripts"))
sys.path.insert(0, str(SKILLS / "skill-registry-builder/scripts"))
from workflow_validation import validate_schema
from normalize_skill_frontmatter import skill_file, validate

SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__"}
STATE_SCHEMAS = {
    "Planning-state.json": "stage-1-output.schema.json",
    "Validation-state.json": "stage-2-output.schema.json",
    "Architecture-state.json": "stage-3-output.schema.json",
    "UX-state.json": "stage-4-output.schema.json",
    "Artifact-evidence-registry.json": "artifact-evidence-registry.schema.json",
    "Risk-acceptance-ledger.json": "risk-acceptance-ledger.schema.json",
}


def snapshot(root: Path) -> dict[str, str]:
    return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((root / "Build-Plans").rglob("*")) if p.is_file() and p.name != ".DS_Store"}


def run_suite(root: Path, directory: Path, timeout: float) -> dict[str, Any]:
    command = [sys.executable, "-m", "unittest", "discover", str(directory.relative_to(root))]
    try:
        result = subprocess.run(command, cwd=root, capture_output=True, text=True, timeout=timeout)
        output = result.stdout + result.stderr
        count = re.search(r"Ran (\d+) tests?", output)
        tests = int(count.group(1)) if count else 0
        return {"suite": str(directory.relative_to(root)), "command": command, "status": "passed" if result.returncode == 0 and tests else "failed", "tests_run": tests, "exit_code": result.returncode, "output": output}
    except subprocess.TimeoutExpired as exc:
        output = (exc.stdout or b"") + (exc.stderr or b"") if isinstance(exc.stdout or exc.stderr, bytes) else (exc.stdout or "") + (exc.stderr or "")
        return {"suite": str(directory.relative_to(root)), "command": command, "status": "timeout", "tests_run": None, "exit_code": None, "output": output.decode(errors="replace") if isinstance(output, bytes) else output}


def collect(root: Path, *, run_tests: bool = True, timeout: float = 120) -> dict[str, Any]:
    root = root.resolve()
    if not (root / ".opencode/Skills").is_dir() or not (root / "System-References/Schemas").is_dir():
        raise ValueError("Workspace must contain the Genesis skills and schemas")
    before = snapshot(root)
    suites = []
    if run_tests:
        for directory in sorted((root / ".opencode/Skills").glob("*/tests")):
            if list(directory.glob("test_*.py")):
                suites.append(run_suite(root, directory, timeout))
    files = [p for p in sorted(root.rglob("*.json")) if not SKIP_DIRS.intersection(p.relative_to(root).parts)]
    json_errors = []
    for path in files:
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            json_errors.append({"path": str(path.relative_to(root)), "error": str(exc)})
    scripts = list((root / ".opencode/Skills").glob("*/scripts/*.py"))
    syntax_errors = []
    for path in scripts:
        try:
            compile(path.read_text(encoding="utf-8"), str(path), "exec")
        except (OSError, ValueError, SyntaxError) as exc:
            syntax_errors.append({"path": str(path.relative_to(root)), "error": str(exc)})
    schemas = []
    for filename, schema in STATE_SCHEMAS.items():
        try:
            value = json.loads((root / "Build-Plans/Build-status" / filename).read_text(encoding="utf-8"))
            errors = validate_schema(value, root / "System-References/Schemas" / schema, root)
        except (OSError, ValueError, TypeError, KeyError, AttributeError, RecursionError) as exc:
            errors = [str(exc)]
        schemas.append({"file": filename, "schema": schema, "status": "failed" if errors else "passed", "errors": errors})
    metadata_errors = []
    folders = sorted(p for p in (root / ".opencode/Skills").iterdir() if p.is_dir() and not p.name.startswith("."))
    for folder in folders:
        instruction = skill_file(folder)
        metadata_errors.extend(validate(instruction) if instruction else [f"{folder.relative_to(root)}: missing skill.md"])
    stage_inventory = []
    for stage in range(1, 9):
        matches = [p for p in folders if p.name.lower().startswith(f"stage-{stage}-")]
        stage_inventory.append({"stage": stage, "command_skills": [str(p.relative_to(root)) for p in matches], "numbered_json_outputs": len(list((root / f"Build-Plans/Stage-{stage}").glob("*.json")))})
    try:
        state = json.loads((root / "Build-Plans/Build-status/Global-workflow-state.json").read_text(encoding="utf-8"))
        baseline = state.get("stages", {})
    except (OSError, ValueError, AttributeError) as exc:
        baseline = {"read_error": str(exc)}
    diff = subprocess.run(["git", "diff", "--check"], cwd=root, capture_output=True, text=True)
    after = snapshot(root)
    changed = sorted(key for key in before.keys() | after.keys() if before.get(key) != after.get(key))
    return {
        "collected_at": datetime.now(timezone.utc).isoformat(), "workspace_root": str(root),
        "test_suites": suites,
        "test_summary": {"status": "passed" if suites and all(s["status"] == "passed" for s in suites) else "failed" if suites else "not_run", "tests_run": sum(s["tests_run"] or 0 for s in suites), "failed_suites": [s["suite"] for s in suites if s["status"] != "passed"]},
        "json": {"files_checked": len(files), "errors": json_errors},
        "python_syntax": {"scripts_checked": len(scripts), "errors": syntax_errors},
        "seed_registry_schemas": schemas,
        "skill_metadata": {"packages_checked": len(folders), "errors": metadata_errors},
        "stages": stage_inventory, "baseline_stage_state": baseline,
        "whitespace": {"exit_code": diff.returncode, "output": diff.stdout + diff.stderr},
        "build_plans_unchanged": not changed, "changed_build_plan_files": changed,
        "assessment_required": "Review all eight contracts and runtime gates, re-probe open findings, then update the report and Markdown plan before rendering HTML. Counts alone do not determine health or close findings.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace-root", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path, help="Optional evidence JSON; otherwise prints to stdout")
    parser.add_argument("--timeout", type=float, default=120, help="Timeout per suite in seconds")
    parser.add_argument("--skip-tests", action="store_true", help="Partial collection only; report tests as not run")
    args = parser.parse_args()
    try:
        if args.timeout <= 0:
            raise ValueError("timeout must be positive")
        if args.output and args.output.resolve().is_relative_to((args.workspace_root / "Build-Plans").resolve()):
            raise ValueError("Evidence output must not overwrite baseline Build-Plans")
        data = collect(args.workspace_root, run_tests=not args.skip_tests, timeout=args.timeout)
        payload = json.dumps(data, indent=2) + "\n"
        if args.output:
            args.output.write_text(payload, encoding="utf-8")
        else:
            print(payload, end="")
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Health evidence collection failed: {exc}\n")
    failed = data["test_summary"]["status"] != "passed" or data["json"]["errors"] or data["python_syntax"]["errors"] or any(s["status"] != "passed" for s in data["seed_registry_schemas"]) or data["skill_metadata"]["errors"] or data["whitespace"]["exit_code"] != 0 or not data["build_plans_unchanged"]
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
