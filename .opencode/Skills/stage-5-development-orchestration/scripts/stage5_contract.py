"""Normalized Stage 5 v2 contract construction and validation helpers."""

from __future__ import annotations

import json
from fnmatch import fnmatch
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

FORMAT_VERSION = "2.0"
CONTEXT_PATH = "Build-Plans/Stage-5/00-stage-context.json"
MANIFEST_PATH = "Build-Plans/Stage-5/09-stage-manifest.json"
WORKFLOW_STATUSES = {
    "contract_only",
    "api_exists_not_wired",
    "ui_wired_not_validated",
    "runtime_persistence_failed",
    "runtime_persistence_verified",
    "local_e2e_passed",
    "staging_e2e_passed",
    "deferred_with_approval",
    "blocked",
}

ARTIFACTS: Mapping[str, Mapping[str, str]] = {
    "development_roadmap": {
        "artifact_id": "ARTIFACT-S5-DEVELOPMENT-ROADMAP",
        "filename": "01-development-roadmap.json",
        "schema": "System-References/Schemas/stage-5-artifact.schema.json",
        "data_key": "roadmap",
    },
    "implementation_sequence": {
        "artifact_id": "ARTIFACT-S5-IMPLEMENTATION-SEQUENCE",
        "filename": "02-implementation-sequence.json",
        "schema": "System-References/Schemas/stage-5-artifact.schema.json",
        "data_key": "slices",
    },
    "engineering_dependencies": {
        "artifact_id": "ARTIFACT-S5-ENGINEERING-DEPENDENCIES",
        "filename": "03-engineering-dependencies.json",
        "schema": "System-References/Schemas/stage-5-artifact.schema.json",
        "data_key": "dependencies",
    },
    "testing_strategy": {
        "artifact_id": "ARTIFACT-S5-TESTING-STRATEGY",
        "filename": "04-testing-strategy.json",
        "schema": "System-References/Schemas/stage-5-artifact.schema.json",
        "data_key": "testing_strategy",
    },
    "build_tickets": {
        "artifact_id": "ARTIFACT-S5-BUILD-TICKETS",
        "filename": "05-build-tickets.json",
        "schema": "System-References/Schemas/stage-5-artifact.schema.json",
        "data_key": "tickets",
    },
    "agent_assignment_plan": {
        "artifact_id": "ARTIFACT-S5-AGENT-ASSIGNMENT-PLAN",
        "filename": "06-agent-assignment-plan.json",
        "schema": "System-References/Schemas/stage-5-artifact.schema.json",
        "data_key": "agents",
    },
    "parallel_execution_plan": {
        "artifact_id": "ARTIFACT-S5-PARALLEL-EXECUTION-PLAN",
        "filename": "07-parallel-execution-plan.json",
        "schema": "System-References/Schemas/stage-5-artifact.schema.json",
        "data_key": "batches",
    },
    "release_plan": {
        "artifact_id": "ARTIFACT-S5-RELEASE-PLAN",
        "filename": "08-release-plan.json",
        "schema": "System-References/Schemas/stage-5-artifact.schema.json",
        "data_key": "release_plan",
    },
}


class ContractError(ValueError):
    """Raised when normalized Stage 5 data violates the reusable contract."""


def build_context(
    *,
    status: str,
    selected_stack: Mapping[str, Any],
    stage_contract_profile: Mapping[str, Any],
    guidance_policy: Mapping[str, Any],
    source_inputs: Mapping[str, Any],
    execution_decision_refs: Sequence[str] = (),
    assumptions: Sequence[Mapping[str, Any]] = (),
    risks: Sequence[Mapping[str, Any]] = (),
    unresolved_questions: Sequence[Mapping[str, Any]] = (),
    reference_integrity: Mapping[str, Any] | None = None,
    risk_acceptance: Mapping[str, Any] | None = None,
    revision_loops: Sequence[Mapping[str, Any]] = (),
) -> dict[str, Any]:
    """Build the single shared Stage 5 context document."""
    return {
        "$schema": "System-References/Schemas/stage-5-context.schema.json",
        "format_version": FORMAT_VERSION,
        "artifact_id": "ARTIFACT-S5-STAGE-CONTEXT",
        "artifact_type": "stage_context",
        "stage": "Stage 5",
        "status": status,
        "selected_stack": dict(selected_stack),
        "stage_contract_profile": dict(stage_contract_profile),
        "guidance_policy": dict(guidance_policy),
        "source_inputs": dict(source_inputs),
        "execution_decision_refs": list(execution_decision_refs),
        "assumptions": list(assumptions),
        "risks": list(risks),
        "unresolved_questions": list(unresolved_questions),
        "reference_integrity": dict(reference_integrity or {}),
        "risk_acceptance": dict(risk_acceptance or {}),
        "revision_loops": list(revision_loops),
    }


def build_artifact(
    artifact_type: str,
    *,
    status: str,
    traceability_refs: Sequence[str],
    canonical_data: Any,
    secondary_data: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Build one numbered artifact containing only its canonical payload."""
    if artifact_type not in ARTIFACTS:
        raise ContractError(f"unknown artifact_type: {artifact_type}")
    definition = ARTIFACTS[artifact_type]
    data = {definition["data_key"]: canonical_data}
    if secondary_data:
        data.update(secondary_data)
    artifact = {
        "$schema": definition["schema"],
        "format_version": FORMAT_VERSION,
        "artifact_id": definition["artifact_id"],
        "artifact_type": artifact_type,
        "stage": "Stage 5",
        "status": status,
        "context_ref": CONTEXT_PATH,
        "traceability_refs": list(traceability_refs),
        "data": data,
    }
    validate_canonical_data(artifact)
    return artifact


def build_manifest(
    artifacts: Sequence[Mapping[str, Any]],
    *,
    completion_status: Mapping[str, Any],
    stage_6_handoff: Mapping[str, Any],
    schema_validation: Mapping[str, Any],
) -> dict[str, Any]:
    """Build the sole Stage 5 completion and Stage 6 handoff document."""
    if schema_validation.get("schemas_valid") is True and not schema_validation.get(
        "validation_executed"
    ):
        raise ContractError("schemas_valid cannot be true before validation executes")
    validate_artifact_set(artifacts)
    index = []
    for artifact in artifacts:
        definition = ARTIFACTS[str(artifact["artifact_type"])]
        index.append(
            {
                "artifact_id": artifact["artifact_id"],
                "artifact_type": artifact["artifact_type"],
                "path": f"Build-Plans/Stage-5/{definition['filename']}",
                "schema_ref": artifact["$schema"],
                "data_path": f"/data/{definition['data_key']}",
            }
        )
    return {
        "$schema": "System-References/Schemas/stage-5-manifest.schema.json",
        "format_version": FORMAT_VERSION,
        "artifact_id": "ARTIFACT-S5-STAGE-MANIFEST",
        "artifact_type": "stage_manifest",
        "stage": "Stage 5",
        "context_ref": CONTEXT_PATH,
        "artifacts": index,
        "completion_status": dict(completion_status),
        "stage_6_handoff": dict(stage_6_handoff),
        "schema_validation": dict(schema_validation),
    }


def validate_canonical_data(artifact: Mapping[str, Any]) -> None:
    """Require the canonical key and reject duplicated canonical collections."""
    artifact_type = str(artifact.get("artifact_type", ""))
    if artifact_type not in ARTIFACTS:
        raise ContractError(f"unknown artifact_type: {artifact_type}")
    data = artifact.get("data")
    if not isinstance(data, Mapping):
        raise ContractError(f"{artifact_type} data must be an object")
    required_key = ARTIFACTS[artifact_type]["data_key"]
    if required_key not in data:
        raise ContractError(f"{artifact_type} requires data.{required_key}")
    exclusive = {"tickets", "agents", "batches"}
    illegal = (exclusive & set(data)) - {required_key}
    if illegal:
        raise ContractError(f"{artifact_type} contains non-canonical collections: {sorted(illegal)}")
    forbidden_envelope = {
        "selected_stack",
        "stage_contract_profile",
        "guidance_policy",
        "source_inputs",
        "assumptions",
        "risks",
        "unresolved_questions",
        "completion_status",
        "stage_6_handoff",
    }
    copied = forbidden_envelope & set(data)
    if copied:
        raise ContractError(f"{artifact_type} duplicates shared or manifest data: {sorted(copied)}")


def validate_artifact_set(artifacts: Sequence[Mapping[str, Any]]) -> None:
    """Validate completeness, identity uniqueness, and canonical payloads."""
    types = [str(item.get("artifact_type", "")) for item in artifacts]
    if set(types) != set(ARTIFACTS) or len(types) != len(ARTIFACTS):
        raise ContractError("manifest requires exactly one of every numbered artifact")
    ids = [str(item.get("artifact_id", "")) for item in artifacts]
    if len(ids) != len(set(ids)):
        raise ContractError("artifact IDs must be unique")
    for artifact in artifacts:
        artifact_type = str(artifact["artifact_type"])
        if artifact.get("format_version") != FORMAT_VERSION:
            raise ContractError(f"{artifact_type} must declare format 2.0")
        if artifact.get("context_ref") != CONTEXT_PATH:
            raise ContractError(f"{artifact_type} has an invalid context_ref")
        if artifact.get("artifact_id") != ARTIFACTS[artifact_type]["artifact_id"]:
            raise ContractError(f"{artifact_type} has an invalid artifact_id")
        validate_canonical_data(artifact)


def resolve_json_pointer(document: Any, pointer: str) -> Any:
    """Resolve an RFC 6901 JSON Pointer."""
    if pointer == "":
        return document
    if not pointer.startswith("/"):
        raise ContractError(f"invalid JSON Pointer: {pointer}")
    current = document
    for raw_token in pointer[1:].split("/"):
        token = raw_token.replace("~1", "/").replace("~0", "~")
        try:
            if isinstance(current, list):
                current = current[int(token)]
            elif isinstance(current, Mapping):
                current = current[token]
            else:
                raise KeyError(token)
        except (KeyError, IndexError, ValueError) as error:
            raise ContractError(f"JSON Pointer target does not exist: {pointer}") from error
    return current


def validate_file_pointer_ref(
    reference: str, *, repository_root: Path, loaded_documents: Mapping[str, Any] | None = None
) -> None:
    """Validate a repository-relative file plus JSON-Pointer reference."""
    if "#" not in reference:
        raise ContractError(f"file reference must include a JSON Pointer: {reference}")
    file_part, pointer = reference.split("#", 1)
    path = repository_root / file_part
    if not path.is_file():
        raise ContractError(f"reference file does not exist: {file_part}")
    if loaded_documents is not None and file_part in loaded_documents:
        document = loaded_documents[file_part]
    else:
        document = json.loads(path.read_text(encoding="utf-8"))
    resolve_json_pointer(document, pointer)


def collect_ids(value: Any) -> set[str]:
    """Collect stable upstream IDs from fixture or source documents."""
    found: set[str] = set()
    if isinstance(value, Mapping):
        for child in value.values():
            found.update(collect_ids(child))
    elif isinstance(value, list):
        for child in value:
            found.update(collect_ids(child))
    elif isinstance(value, str) and "-" in value and value.split("-", 1)[0].isupper():
        found.add(value)
    return found


def validate_ticket_references(
    tickets: Sequence[Mapping[str, Any]],
    *,
    repository_root: Path,
    source_documents: Mapping[str, Any],
) -> None:
    """Resolve ticket refs against the actual Stage 1-4 source documents."""
    upstream_ids = collect_ids(source_documents)
    for ticket in tickets:
        for field, refs in ticket.items():
            if not (field.endswith("_refs") or field == "traceability_refs"):
                continue
            if field == "risk_refs":
                continue
            if not isinstance(refs, list):
                raise ContractError(f"{field} must be an array")
            for reference in refs:
                if not isinstance(reference, str):
                    raise ContractError(f"{field} entries must be strings")
                if "#" in reference:
                    validate_file_pointer_ref(
                        reference,
                        repository_root=repository_root,
                        loaded_documents=source_documents,
                    )
                elif reference not in upstream_ids:
                    raise ContractError(f"unresolved upstream reference: {reference}")


def validate_risk_refs(
    records: Iterable[Mapping[str, Any]], known_risk_ids: Iterable[str]
) -> None:
    """Require compact risk_refs to resolve to shared-context risks."""
    known = set(known_risk_ids)
    for record in records:
        refs = record.get("risk_refs", [])
        if not isinstance(refs, list) or any(ref not in known for ref in refs):
            raise ContractError("risk_refs must resolve to shared context risks")
        if "risks" in record:
            raise ContractError("canonical records must use risk_refs, not copied risk objects")


def _scope_covers(path: str, scope: str) -> bool:
    normalized = scope.rstrip("/")
    return path == normalized or path.startswith(f"{normalized}/") or fnmatch(path, scope)


def validate_agent_scopes(
    agents: Sequence[Mapping[str, Any]], tickets: Sequence[Mapping[str, Any]]
) -> None:
    """Ensure every assigned ticket target is inside its agent's allowed scopes."""
    by_id = {str(ticket["ticket_id"]): ticket for ticket in tickets}
    for agent in agents:
        scopes = [str(scope) for scope in agent.get("allowed_file_scopes", [])]
        for ticket_id in agent.get("assigned_tickets", []):
            if ticket_id not in by_id:
                raise ContractError(f"agent references unknown ticket: {ticket_id}")
            targets = by_id[ticket_id].get(
                "file_scopes", by_id[ticket_id].get("allowed_file_scopes", [])
            )
            for target in targets:
                if not any(_scope_covers(str(target), scope) for scope in scopes):
                    raise ContractError(
                        f"agent {agent.get('agent_id')} scope does not cover "
                        f"{ticket_id}: {target}"
                    )


def validate_execution_waves(
    batches: Sequence[Mapping[str, Any]], tickets: Sequence[Mapping[str, Any]]
) -> None:
    """Require dependencies to be scheduled in earlier execution waves."""
    dependencies = {
        str(ticket["ticket_id"]): set(
            str(item) for item in ticket.get("depends_on", ticket.get("ticket_dependencies", []))
        )
        for ticket in tickets
    }
    for batch in batches:
        batch_tickets = [str(item) for item in batch.get("tickets", [])]
        waves = batch.get("execution_waves")
        if not isinstance(waves, list) or not waves:
            raise ContractError(f"batch {batch.get('batch_id')} requires execution_waves")
        positions: dict[str, int] = {}
        for index, wave in enumerate(waves):
            ticket_ids = wave.get("ticket_ids", [])
            for ticket_id in ticket_ids:
                if ticket_id in positions:
                    raise ContractError(f"ticket appears in multiple waves: {ticket_id}")
                positions[str(ticket_id)] = index
        if set(positions) != set(batch_tickets):
            raise ContractError("execution_waves must contain every batch ticket exactly once")
        for ticket_id in batch_tickets:
            for prerequisite in dependencies.get(ticket_id, set()) & set(batch_tickets):
                if positions[prerequisite] >= positions[ticket_id]:
                    raise ContractError(
                        f"{prerequisite} must precede dependent ticket {ticket_id}"
                    )


def _truthy_field(record: Mapping[str, Any], key: str) -> bool:
    return bool(record.get(key))


def _is_launch_critical_workflow_ticket(ticket: Mapping[str, Any]) -> bool:
    priority = str(ticket.get("priority", "")).lower()
    ticket_type = str(ticket.get("ticket_type", "")).lower()
    if ticket.get("launch_critical") is True or priority == "critical":
        return True
    if ticket_type in {"frontend", "integration"} and (
        ticket.get("ui_blueprint_refs")
        or ticket.get("interactive_element_refs")
        or ticket.get("action_refs")
        or ticket.get("route_refs")
    ):
        return True
    return False


def validate_workflow_completion_definitions(tickets: Sequence[Mapping[str, Any]]) -> None:
    """Require outcome-based completion definitions for launch-critical workflows."""
    for ticket in tickets:
        if not _is_launch_critical_workflow_ticket(ticket):
            continue
        ticket_id = ticket.get("ticket_id", "<unknown>")
        completion_definition = ticket.get("completion_definition")
        if not isinstance(completion_definition, Mapping):
            raise ContractError(f"{ticket_id} requires completion_definition")
        required_true = (
            "requires_ui_wiring",
            "requires_runtime_persistence",
            "requires_end_to_end_smoke",
            "done_means_user_can_complete_workflow",
        )
        missing = [key for key in required_true if completion_definition.get(key) is not True]
        if completion_definition.get("contract_only_allowed") is not False:
            missing.append("contract_only_allowed=false")
        if missing:
            raise ContractError(
                f"{ticket_id} has incomplete workflow completion_definition: {missing}"
            )
        smoke_tests = ticket.get("workflow_smoke_tests", ticket.get("smoke_tests", []))
        if not isinstance(smoke_tests, list) or not smoke_tests:
            raise ContractError(f"{ticket_id} requires workflow smoke tests")
        for smoke_test in smoke_tests:
            if not isinstance(smoke_test, Mapping):
                raise ContractError(f"{ticket_id} workflow smoke tests must be objects")
            if not smoke_test.get("workflow_id") or not smoke_test.get("expected_user_outcome"):
                raise ContractError(
                    f"{ticket_id} workflow smoke tests require workflow_id and expected_user_outcome"
                )


def validate_workflow_evidence(
    workflow_evidence: Sequence[Mapping[str, Any]],
    *,
    launch_critical_workflow_ids: Iterable[str],
) -> None:
    """Validate Stage 6/7 workflow evidence for launch-critical outcomes."""
    required = set(launch_critical_workflow_ids)
    by_workflow: dict[str, Mapping[str, Any]] = {}
    for record in workflow_evidence:
        workflow_id = str(record.get("workflow_id", ""))
        if not workflow_id:
            raise ContractError("workflow evidence requires workflow_id")
        status = str(record.get("status", ""))
        if status not in WORKFLOW_STATUSES:
            raise ContractError(f"unsupported workflow status: {status}")
        by_workflow[workflow_id] = record
        if status in {"local_e2e_passed", "staging_e2e_passed"}:
            if not record.get("evidence_refs"):
                raise ContractError(f"{workflow_id} passed without evidence_refs")
            if not record.get("verified_user_outcome"):
                raise ContractError(f"{workflow_id} passed without verified_user_outcome")
        elif status == "deferred_with_approval":
            if not record.get("approval_ref") and not record.get("accepted_risk_ref"):
                raise ContractError(f"{workflow_id} deferred without approval or accepted risk")
        elif workflow_id in required:
            raise ContractError(f"{workflow_id} is launch-critical but not end-to-end passed")
    missing = required - set(by_workflow)
    if missing:
        raise ContractError(f"missing launch-critical workflow evidence: {sorted(missing)}")


def evidence_registry_link() -> dict[str, str]:
    """Return the canonical v2 Stage 5 ticket evidence locator."""
    return {
        "related_stage_output": "Build-Plans/Stage-5/05-build-tickets.json",
        "related_stage_data_path": "/data/tickets",
    }
