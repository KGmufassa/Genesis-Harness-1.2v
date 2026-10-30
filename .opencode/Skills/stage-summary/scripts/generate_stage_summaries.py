#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Mapping, Sequence


STAGE_NUMBERS: Sequence[int] = (5, 6, 7, 8)
SUMMARY_FILENAMES: Mapping[int, str] = {
    5: "10-stage-5-summary.md",
    6: "06-stage-6-summary.md",
    7: "06-stage-7-summary.md",
    8: "06-stage-8-summary.md",
}
STAGE_TITLES: Mapping[int, str] = {
    5: "Development Orchestration",
    6: "Implementation And Validation",
    7: "Launch Operationalization",
    8: "Post-Launch Evolution",
}
REQUIRED_STAGE_FILES: Mapping[int, Sequence[str]] = {
    5: (
        "00-stage-context.json",
        "01-development-roadmap.json",
        "02-implementation-sequence.json",
        "03-engineering-dependencies.json",
        "04-testing-strategy.json",
        "05-build-tickets.json",
        "06-agent-assignment-plan.json",
        "07-parallel-execution-plan.json",
        "08-release-plan.json",
        "09-stage-manifest.json",
    ),
    6: (
        "01-implementation-status.json",
        "02-validation-results.json",
        "03-regression-analysis.json",
        "04-system-health.json",
        "05-repair-log.json",
    ),
    7: (
        "01-launch-readiness.json",
        "02-deployment-framework.json",
        "03-monitoring-systems.json",
        "04-analytics-framework.json",
        "05-operational-tooling.json",
    ),
    8: (
        "01-telemetry-analysis.json",
        "02-operational-optimization.json",
        "03-ai-improvement-plan.json",
        "04-roadmap-evolution.json",
        "05-scalability-evolution.json",
    ),
}
READY_STATUSES: Mapping[int, str] = {
    5: "ready_for_stage_6",
    6: "ready_for_stage_7",
    7: "ready_for_stage_8",
    8: "evolution_plan_ready",
}
STAGE_FOCUS: Mapping[int, Sequence[str]] = {
    5: (
        "roadmap",
        "implementation sequence",
        "dependencies",
        "testing",
        "tickets",
        "agents",
        "parallel batches",
        "release",
    ),
    6: (
        "implementation",
        "validation",
        "live linked routed pages",
        "regression",
        "repair",
        "system health",
    ),
    7: (
        "launch readiness",
        "deployment",
        "monitoring",
        "analytics",
        "operational tooling",
    ),
    8: (
        "telemetry",
        "operational optimization",
        "AI improvement",
        "roadmap evolution",
        "scalability evolution",
        "feedback routes",
    ),
}
ASSESSMENT_FIELDS: Sequence[str] = (
    "completion_status",
    "status",
    "schema_validation",
    "reference_integrity",
    "risk_acceptance_ledger",
    "stage_6_handoff",
    "stage_7_handoff",
    "stage_8_handoff",
    "prior_stage_feedback",
)
ISSUE_FIELDS: Sequence[str] = (
    "blocking_items",
    "blocking_gaps",
    "blockers",
    "execution_blockers",
    "test_failures",
    "open_questions",
    "unresolved_questions",
    "risks",
    "execution_risks",
    "known_risks",
    "accepted_risks",
    "revision_loops",
    "next_actions",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate assessment markdown summaries for populated Stage 5-8 folders."
    )
    parser.add_argument(
        "--workspace-root",
        default=".",
        help="Repository root containing Build-Plans/.",
    )
    parser.add_argument(
        "--stages",
        default="5,6,7,8",
        help="Comma-separated stage numbers to summarize. Defaults to 5,6,7,8.",
    )
    return parser.parse_args()


def parse_stage_numbers(raw_stages: str) -> Sequence[int]:
    stage_numbers = []
    for raw_stage in raw_stages.split(","):
        stripped = raw_stage.strip()
        if not stripped:
            continue
        stage_number = int(stripped)
        if stage_number not in STAGE_NUMBERS:
            raise ValueError("Only Stage 5 through Stage 8 summaries are supported.")
        stage_numbers.append(stage_number)
    if not stage_numbers:
        raise ValueError("At least one stage number is required.")
    return tuple(stage_numbers)


def stage_folder_name(stage_number: int) -> str:
    return f"Stage-{stage_number}"


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {path}: {exc.msg} at line {exc.lineno} column {exc.colno}") from exc


def load_stage_documents(stage_dir: Path) -> dict[str, Any]:
    documents: dict[str, Any] = {}
    for path in sorted(stage_dir.glob("*.json")):
        if path.name.startswith("."):
            continue
        documents[path.name] = load_json(path)
    return documents


def load_readiness_audit(workspace_root: Path, stage_number: int) -> Any:
    audit_path = workspace_root / "Build-Plans" / "Build-status" / f"Stage-{stage_number}-readiness-audit.json"
    if not audit_path.exists():
        return {}
    return load_json(audit_path)


def get_path(payload: Any, pointer: str) -> Any:
    current = payload
    for raw_part in pointer.strip("/").split("/"):
        if raw_part == "":
            continue
        part = raw_part.replace("~1", "/").replace("~0", "~")
        if isinstance(current, dict):
            current = current.get(part)
        elif isinstance(current, list) and part.isdigit():
            index = int(part)
            current = current[index] if index < len(current) else None
        else:
            return None
    return current


def coerce_items(value: Any) -> list[Any]:
    if value in (None, "", {}, []):
        return []
    if isinstance(value, list):
        return value
    return [value]


def summarize_value(value: Any) -> str:
    if isinstance(value, dict):
        for key in ("status", "summary", "reason", "title", "name", "id"):
            nested = value.get(key)
            if isinstance(nested, str) and nested:
                return nested
        return f"{len(value)} fields"
    if isinstance(value, list):
        if value and isinstance(value[0], dict):
            first_summary = summarize_value(value[0])
            if first_summary and not first_summary.endswith(" fields"):
                return f"{len(value)} items; first: {first_summary}"
        return f"{len(value)} items"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    return str(value)


def summarize_collection(value: Any, noun: str) -> str:
    if isinstance(value, list):
        return f"{len(value)} {noun}"
    if isinstance(value, dict):
        return f"{len(value)} {noun}"
    if value in (None, "", [], {}):
        return f"0 {noun}"
    return f"1 {noun}"


def first_non_empty_mapping_value(payload: Mapping[str, Any], keys: Sequence[str]) -> Any:
    for key in keys:
        value = payload.get(key)
        if value not in (None, "", [], {}):
            return value
    return None


def payload_status(payload: Any) -> str:
    if not isinstance(payload, dict):
        return ""
    completion_status = payload.get("completion_status")
    if isinstance(completion_status, dict):
        status = completion_status.get("status")
        if isinstance(status, str):
            return status
    status = payload.get("status")
    return status if isinstance(status, str) else ""


def readiness_label(stage_number: int, status: str, missing_files: Sequence[str], audit: Any) -> str:
    audit_ready = isinstance(audit, dict) and audit.get("ready_for_next_stage") is True
    audit_failed = isinstance(audit, dict) and audit.get("audit_status") in ("failed", "blocked")
    if missing_files:
        return "Blocked"
    if status == READY_STATUSES[stage_number] and (not audit or audit_ready):
        return "Ready"
    if audit_failed:
        return "Blocked"
    if status and status != READY_STATUSES[stage_number]:
        return "Needs Revision"
    return "Needs Assessment"


def stage_status(stage_number: int, documents: Mapping[str, Any]) -> str:
    if stage_number == 5:
        manifest = documents.get("09-stage-manifest.json")
        if isinstance(manifest, dict):
            return payload_status(manifest)
    for name in REQUIRED_STAGE_FILES[stage_number]:
        status = payload_status(documents.get(name))
        if status == READY_STATUSES[stage_number]:
            return status
    for name in REQUIRED_STAGE_FILES[stage_number]:
        status = payload_status(documents.get(name))
        if status:
            return status
    for payload in documents.values():
        status = payload_status(payload)
        if status:
            return status
    return ""


def stage5_metric_lines(documents: Mapping[str, Any]) -> list[str]:
    manifest = documents.get("09-stage-manifest.json", {})
    context = documents.get("00-stage-context.json", {})
    tickets = get_path(documents.get("05-build-tickets.json", {}), "/data/tickets")
    agents = get_path(documents.get("06-agent-assignment-plan.json", {}), "/data/agents")
    batches = get_path(documents.get("07-parallel-execution-plan.json", {}), "/data/batches")
    artifacts = []
    if isinstance(manifest, dict):
        artifacts = coerce_items(first_non_empty_mapping_value(manifest, ("artifacts", "artifact_index", "numbered_artifacts")))
    return [
        f"- Manifest indexed artifacts: {len(artifacts)}",
        f"- Build tickets: {summarize_collection(tickets, 'tickets')}",
        f"- Assigned agents: {summarize_collection(agents, 'agents')}",
        f"- Parallel batches: {summarize_collection(batches, 'batches')}",
        f"- Shared context risks: {summarize_collection(context.get('risks') if isinstance(context, dict) else None, 'risks')}",
    ]


def stage6_metric_lines(documents: Mapping[str, Any]) -> list[str]:
    implementation = documents.get("01-implementation-status.json", {})
    validation = documents.get("02-validation-results.json", {})
    regression = documents.get("03-regression-analysis.json", {})
    repair = documents.get("05-repair-log.json", {})
    live_routes = []
    workflow_evidence = []
    if isinstance(validation, dict):
        live_routes = coerce_items(
            first_non_empty_mapping_value(
                validation,
                ("live_route_validation", "live_page_route_evidence", "route_validation_results", "preview_route_results"),
            )
        )
        workflow_evidence = coerce_items(validation.get("workflow_evidence"))
    return [
        f"- Ticket execution records: {summarize_collection(implementation.get('ticket_statuses') if isinstance(implementation, dict) else None, 'records')}",
        f"- Validation results: {summarize_collection(validation.get('validation_results') if isinstance(validation, dict) else None, 'results')}",
        f"- Live linked/routed page checks: {len(live_routes)}",
        f"- Workflow outcome evidence records: {len(workflow_evidence)}",
        f"- Regression findings: {summarize_collection(regression.get('regressions') if isinstance(regression, dict) else None, 'findings')}",
        f"- Repair records: {summarize_collection(repair.get('repairs') if isinstance(repair, dict) else repair, 'records')}",
    ]


def stage7_metric_lines(documents: Mapping[str, Any]) -> list[str]:
    readiness = documents.get("01-launch-readiness.json", {})
    deployment = documents.get("02-deployment-framework.json", {})
    monitoring = documents.get("03-monitoring-systems.json", {})
    analytics = documents.get("04-analytics-framework.json", {})
    operations = documents.get("05-operational-tooling.json", {})
    return [
        f"- Launch gates: {summarize_collection(readiness.get('launch_gates') if isinstance(readiness, dict) else None, 'gates')}",
        f"- Deployment checks: {summarize_collection(deployment.get('deployment_checks') if isinstance(deployment, dict) else None, 'checks')}",
        f"- Monitoring signals: {summarize_collection(monitoring.get('monitoring_signals') if isinstance(monitoring, dict) else None, 'signals')}",
        f"- Analytics events: {summarize_collection(analytics.get('analytics_events') if isinstance(analytics, dict) else None, 'events')}",
        f"- Operational runbooks/tools: {summarize_collection(operations.get('operational_tools') if isinstance(operations, dict) else None, 'items')}",
    ]


def stage8_metric_lines(documents: Mapping[str, Any]) -> list[str]:
    telemetry = documents.get("01-telemetry-analysis.json", {})
    operations = documents.get("02-operational-optimization.json", {})
    ai_plan = documents.get("03-ai-improvement-plan.json", {})
    roadmap = documents.get("04-roadmap-evolution.json", {})
    scale = documents.get("05-scalability-evolution.json", {})
    return [
        f"- Telemetry findings: {summarize_collection(telemetry.get('findings') if isinstance(telemetry, dict) else None, 'findings')}",
        f"- Operational improvements: {summarize_collection(operations.get('optimization_actions') if isinstance(operations, dict) else None, 'actions')}",
        f"- AI improvement items: {summarize_collection(ai_plan.get('improvement_items') if isinstance(ai_plan, dict) else None, 'items')}",
        f"- Roadmap changes: {summarize_collection(roadmap.get('roadmap_changes') if isinstance(roadmap, dict) else None, 'changes')}",
        f"- Scalability actions: {summarize_collection(scale.get('scalability_actions') if isinstance(scale, dict) else None, 'actions')}",
    ]


def stage_metric_lines(stage_number: int, documents: Mapping[str, Any]) -> list[str]:
    if stage_number == 5:
        return stage5_metric_lines(documents)
    if stage_number == 6:
        return stage6_metric_lines(documents)
    if stage_number == 7:
        return stage7_metric_lines(documents)
    return stage8_metric_lines(documents)


def action_lines(documents: Mapping[str, Any]) -> list[str]:
    lines = []
    for name, payload in documents.items():
        if not isinstance(payload, dict):
            lines.append(f"- `{name}`: recorded root {summarize_value(payload)}.")
            continue
        purpose = payload.get("artifact_type") or payload.get("command") or payload.get("stage") or Path(name).stem
        status = payload_status(payload)
        suffix = f" Status: `{status}`." if status else ""
        lines.append(f"- `{name}`: recorded `{purpose}`.{suffix}")
    return lines or ["- No JSON outputs were available to summarize."]


def evidence_lines(documents: Mapping[str, Any], audit: Any) -> list[str]:
    lines = []
    for name, payload in documents.items():
        if not isinstance(payload, dict):
            continue
        for field in ASSESSMENT_FIELDS:
            value = payload.get(field)
            if value not in (None, "", [], {}):
                lines.append(f"- `{name}` `{field}`: {summarize_value(value)}")
    if isinstance(audit, dict) and audit:
        audit_status = audit.get("audit_status", "")
        ready = audit.get("ready_for_next_stage", "")
        lines.append(f"- Readiness audit: `{audit_status or 'present'}`; ready_for_next_stage: `{ready}`")
    return lines or ["- No explicit schema, handoff, reference, or readiness evidence was found in the available JSON."]


def issue_lines(documents: Mapping[str, Any], audit: Any) -> list[str]:
    lines = []
    for name, payload in documents.items():
        if not isinstance(payload, dict):
            continue
        for field in ISSUE_FIELDS:
            value = payload.get(field)
            if value not in (None, "", [], {}):
                lines.append(f"- `{name}` `{field}`: {summarize_value(value)}")
    if isinstance(audit, dict):
        for field in ("blocking_gaps", "warnings", "next_actions", "revision_loops"):
            value = audit.get(field)
            if value not in (None, "", [], {}):
                lines.append(f"- readiness audit `{field}`: {summarize_value(value)}")
    return lines or ["- No blockers, unresolved questions, revision loops, or accepted risks were found in the available JSON."]


def missing_required_files(stage_number: int, stage_dir: Path) -> list[str]:
    return [name for name in REQUIRED_STAGE_FILES[stage_number] if not (stage_dir / name).exists()]


def render_stage_summary(stage_number: int, stage_dir: Path, documents: Mapping[str, Any], audit: Any) -> str:
    missing_files = missing_required_files(stage_number, stage_dir)
    status = stage_status(stage_number, documents)
    assessment = readiness_label(stage_number, status, missing_files, audit)
    summary_file = SUMMARY_FILENAMES[stage_number]

    lines = [
        f"# Stage {stage_number} Assessment Summary",
        "",
        f"- Stage: Stage {stage_number} - {STAGE_TITLES[stage_number]}",
        f"- Summary file: `{summary_file}`",
        f"- Final status: `{status or 'unknown'}`",
        f"- User assessment: `{assessment}`",
        f"- Canonical JSON outputs summarized: {len(documents)}",
        f"- Required outputs missing: {', '.join(f'`{name}`' for name in missing_files) if missing_files else 'none'}",
        "",
        "## What This Stage Did",
        "",
        f"- Focus areas: {', '.join(STAGE_FOCUS[stage_number])}",
    ]
    lines.extend(action_lines(documents))
    lines.extend(["", "## Results", ""])
    lines.extend(stage_metric_lines(stage_number, documents))
    lines.extend(["", "## Evidence And Readiness", ""])
    lines.extend(evidence_lines(documents, audit))
    lines.extend(["", "## Blockers, Risks, And Next Actions", ""])
    lines.extend(issue_lines(documents, audit))
    lines.extend(
        [
            "",
            "## Assessment",
            "",
            f"- Result: `{assessment}`",
            f"- Ready status required for this stage: `{READY_STATUSES[stage_number]}`",
            f"- Summary role: local human review artifact only; canonical consumers must use the Stage {stage_number} JSON outputs and handoff contracts.",
            "",
        ]
    )
    return "\n".join(lines)


def generate_stage_summaries(workspace_root: Path, stage_numbers: Sequence[int]) -> tuple[list[str], list[str]]:
    build_plans_dir = workspace_root / "Build-Plans"
    if not build_plans_dir.exists():
        raise FileNotFoundError(f"Build-Plans directory not found at {build_plans_dir}")

    generated: list[str] = []
    skipped: list[str] = []

    for stage_number in stage_numbers:
        stage_dir = build_plans_dir / stage_folder_name(stage_number)
        if not stage_dir.exists():
            skipped.append(stage_dir.name)
            continue

        documents = load_stage_documents(stage_dir)
        if not documents:
            skipped.append(stage_dir.name)
            continue

        audit = load_readiness_audit(workspace_root, stage_number)
        output_path = stage_dir / SUMMARY_FILENAMES[stage_number]
        output_path.write_text(render_stage_summary(stage_number, stage_dir, documents, audit), encoding="utf-8")
        generated.append(output_path.relative_to(workspace_root).as_posix())

    return generated, skipped


def main() -> int:
    args = parse_args()
    workspace_root = Path(args.workspace_root).resolve()

    try:
        stage_numbers = parse_stage_numbers(args.stages)
        generated, skipped = generate_stage_summaries(workspace_root, stage_numbers)
    except (FileNotFoundError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1

    if generated:
        print("Generated stage assessment summaries:")
        for path in generated:
            print(f"- {path}")
    else:
        print("No populated Stage 5-8 folders found.")

    if skipped:
        print("Skipped stages:")
        for stage_name in skipped:
            print(f"- {stage_name}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
