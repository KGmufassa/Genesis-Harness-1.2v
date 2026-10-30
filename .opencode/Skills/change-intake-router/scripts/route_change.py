#!/usr/bin/env python3
"""Preview, record, or audit a minimal Genesis scoped change."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

VALIDATION_DIR = Path(__file__).resolve().parents[2] / "global-stage-readiness-audit/scripts"
sys.path.insert(0, str(VALIDATION_DIR))
from workflow_validation import load_json, validate_schema  # noqa: E402


ACTIVE_STATUSES = {"active", "validating", "ready_to_merge", "blocked"}
ROUTES: Sequence[tuple[int, str, Sequence[str]]] = (
    (1, "cross_cutting", ("feature", "user outcome", "role", "workflow", "product boundary", "permission model")),
    (2, "bounded", ("market", "demand", "business assumption", "behavioral assumption")),
    (3, "bounded", ("api", "database", "data model", "service", "integration", "security", "infrastructure", "scalability", "authentication", "payment", "migration")),
    (4, "bounded", ("page", "screen", "navigation", "layout", "visual", "responsive", "accessibility", "interaction")),
    (5, "bounded", ("ticket", "sequence", "agent assignment", "test strategy", "release plan")),
    (7, "bounded", ("deploy", "monitoring", "alert", "rollback", "launch configuration")),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Route or audit a scoped Genesis change.")
    parser.add_argument("request", nargs="?", default="")
    parser.add_argument("--workspace-root", default=".")
    parser.add_argument("--approval-status", choices=("pending", "approved", "revision_requested", "blocked", "rejected"), default="pending")
    parser.add_argument("--owner", default="")
    parser.add_argument("--affected-id", action="append", default=[])
    parser.add_argument("--record", action="store_true")
    parser.add_argument("--audit-record")
    parser.add_argument("--mark-ready", action="store_true")
    return parser.parse_args()


def _contains(text: str, phrases: Sequence[str]) -> bool:
    return any(re.search(rf"\b{re.escape(phrase)}s?\b", text) for phrase in phrases)


def _active_refinement(root: Path) -> str | None:
    state_path = root / "Build-Plans/Build-status/Global-workflow-state.json"
    if not state_path.is_file():
        return None
    state = load_json(state_path)
    current = state.get("current_stage")
    status = state.get("stages", {}).get(current, {}).get("status") if current else None
    if current and status not in {None, "not_started"} and not str(status).startswith("ready_for_"):
        return str(current)
    return None


def classify(request: str, root: Path) -> dict[str, Any]:
    text = request.lower().strip()
    if not text:
        raise ValueError("A change request is required")
    refinement_stage = _active_refinement(root)
    if refinement_stage:
        return {"mode": "active_stage_refinement", "entry_stage": refinement_stage, "change_class": "none", "required_stages": [refinement_stage], "validation_level": "local", "reason": "The owning workflow is active and not approved; no CHANGE record is required."}
    emergency = _contains(text, ("emergency", "outage", "active vulnerability", "data loss"))
    entry_stage, change_class = 6, "trivial"
    for candidate, candidate_class, phrases in ROUTES:
        if _contains(text, phrases):
            entry_stage, change_class = candidate, candidate_class
            break
    if emergency:
        entry_stage, change_class = (3 if _contains(text, ("security", "vulnerability", "data")) else 6), "emergency"
    critical = emergency or _contains(text, ("authentication", "authorization", "payment", "privacy", "destructive migration", "security"))
    validation_level = "critical" if critical else "system" if change_class == "cross_cutting" else "workflow" if change_class == "bounded" else "local"
    if entry_stage == 1:
        required = [1, 2, 3, 4, 5, 6]
    elif entry_stage in {2, 3, 4}:
        required = list(range(entry_stage, 7))
    elif entry_stage == 5:
        required = [5, 6]
    elif entry_stage == 7:
        required = [7]
    else:
        required = [6]
    return {"mode": "change_cycle", "entry_stage": f"stage_{entry_stage}", "change_class": change_class, "required_stages": [f"stage_{item}" for item in required], "validation_level": validation_level, "reason": f"Earliest affected owner is Stage {entry_stage}."}


def _git(root: Path, *args: str) -> str:
    result = subprocess.run(["git", *args], cwd=root, capture_output=True, text=True)
    if result.returncode:
        raise ValueError(result.stderr.strip() or "Git preflight failed")
    return result.stdout.strip()


def _ledger(root: Path) -> tuple[Path, dict[str, Any]]:
    path = root / "Build-Plans/Build-status/Change-ledger.json"
    return path, load_json(path) if path.is_file() else {"ledger_version": "1.0.0", "changes": []}


def _next_change_id(ledger: Mapping[str, Any]) -> str:
    numbers = [int(match.group(1)) for item in ledger.get("changes", []) if (match := re.fullmatch(r"CHANGE-(\d+)", str(item.get("change_id", ""))))]
    return f"CHANGE-{max(numbers, default=0) + 1:03d}"


def record_change(root: Path, request: str, route: Mapping[str, Any], args: argparse.Namespace) -> dict[str, Any]:
    if route["mode"] != "change_cycle":
        raise ValueError("Active-stage refinements must not create CHANGE records")
    if args.approval_status != "approved" or not args.owner:
        raise ValueError("Recording requires approved status and an owner")
    if _git(root, "status", "--porcelain"):
        raise ValueError("Working tree is not clean; record creation is blocked")
    ledger_path, ledger = _ledger(root)
    conflicts = [item["change_id"] for item in ledger.get("changes", []) if item.get("status") in ACTIVE_STATUSES and set(item.get("affected_id_locks", [])) & set(args.affected_id)]
    if conflicts:
        raise ValueError(f"Affected-ID lock conflict with: {', '.join(conflicts)}")
    change_id = _next_change_id(ledger)
    change_dir = root / "Build-Plans/Changes" / change_id
    change_dir.mkdir(parents=True, exist_ok=False)
    now = datetime.now(timezone.utc).isoformat()
    record = {
        "$schema": "System-References/Schemas/change-record.schema.json",
        "change_id": change_id,
        "title": request[:100],
        "requested_outcome": request,
        "change_class": route["change_class"],
        "base_commit": _git(root, "rev-parse", "HEAD"),
        "owner": args.owner,
        "affected_ids": args.affected_id,
        "preserved_behavior": [],
        "risk_level": "critical" if route["validation_level"] == "critical" else "medium" if route["validation_level"] in {"system", "workflow"} else "low",
        "risk_refs": [],
        "evidence_refs": [],
        "validation_level": route["validation_level"],
        "impact_confidence": "high" if args.affected_id else "medium",
        "unresolved_impacts": [],
        "entry_stage": route["entry_stage"],
        "required_stages": route["required_stages"],
        "stage_dispositions": {},
        "approval": {"required_types": ["product"] if route["entry_stage"] == "stage_1" else ["technical"], "status": "approved", "evidence_refs": [], "approved_by": args.owner, "approved_at": now},
        "deferred_items": [],
        "completion_disposition": "",
        "status": "active",
    }
    record_path = change_dir / "change-record.json"
    record_path.write_text(json.dumps(record, indent=2), encoding="utf-8")
    ledger.setdefault("changes", []).append({"change_id": change_id, "record_path": str(record_path.relative_to(root)), "status": "active", "base_commit": record["base_commit"], "affected_id_locks": args.affected_id})
    ledger_path.parent.mkdir(parents=True, exist_ok=True)
    ledger_path.write_text(json.dumps(ledger, indent=2), encoding="utf-8")
    return record


def audit_record(root: Path, record_path: Path, mark_ready: bool) -> dict[str, Any]:
    record = load_json(record_path)
    schema_errors = validate_schema(record, root / "System-References/Schemas/change-record.schema.json", root)
    blocking = list(schema_errors)
    approval = record.get("approval", {})
    if approval.get("status") != "approved" or not approval.get("approved_by"):
        blocking.append("Required approval is unresolved")
    if record.get("unresolved_impacts"):
        blocking.append("Unresolved impacts remain")
    for item in record.get("deferred_items", []):
        if not all(item.get(key) for key in ("owner", "reason", "next_action", "risk_disposition")):
            blocking.append("Deferred item lacks owner, reason, next action, or risk disposition")
    if record.get("risk_level") in {"high", "critical"} and not approval.get("evidence_refs"):
        blocking.append("High/critical change requires explicit approval evidence")
    ledger_path, ledger = _ledger(root)
    entry = next((item for item in ledger.get("changes", []) if item.get("change_id") == record.get("change_id")), None)
    if entry is None or set(entry.get("affected_id_locks", [])) != set(record.get("affected_ids", [])):
        blocking.append("Change ledger entry or affected-ID locks do not match")
    status = "passed" if not blocking else "failed"
    if mark_ready and status == "passed":
        record["status"] = "ready_to_merge"
        record["completion_disposition"] = "ready_to_merge"
        record_path.write_text(json.dumps(record, indent=2), encoding="utf-8")
        assert ledger_path.is_file()
        for item in ledger["changes"]:
            if item.get("change_id") == record["change_id"]:
                item["status"] = "ready_to_merge"
        ledger_path.write_text(json.dumps(ledger, indent=2), encoding="utf-8")
    return {"change_id": record.get("change_id"), "audit_status": status, "blocking_gaps": blocking, "ready_to_merge": status == "passed"}


def main() -> int:
    args = parse_args()
    root = Path(args.workspace_root).resolve()
    try:
        if args.audit_record:
            result = audit_record(root, root / args.audit_record, args.mark_ready)
        else:
            route = classify(args.request, root)
            result = record_change(root, args.request, route, args) if args.record else route
        print(json.dumps(result, indent=2))
        return 0 if result.get("audit_status") != "failed" else 1
    except (OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

