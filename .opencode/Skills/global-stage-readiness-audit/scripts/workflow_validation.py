#!/usr/bin/env python3
"""Small, dependency-free validators for Genesis workflow artifacts."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


ID_PREFIXES: Sequence[str] = (
    "USER", "WORKFLOW", "CAP", "FEATURE", "BOUNDARY", "DEP", "RISK",
    "ASSUMPTION", "SERVICE", "ENTITY", "API", "INTEGRATION", "INFRA",
    "SECURITY", "SCALE", "JOURNEY", "SCREEN", "BEHAVIOR", "STATE", "A11Y",
    "UI-BLUEPRINT", "VISUAL-SPEC", "UI-ELEMENT", "ROUTE", "ACTION",
    "DESIGN-SYSTEM", "SLICE", "TICKET", "AGENT", "BATCH", "VALIDATION",
    "VISUAL-QA", "ARTIFACT", "LAUNCH-GATE", "TELEMETRY", "EXPERIMENT", "CHANGE",
)
ID_PATTERN = re.compile(
    rf"^(?:{'|'.join(re.escape(prefix) for prefix in ID_PREFIXES)})-[A-Za-z0-9._-]+$"
)


class ValidationError(ValueError):
    """Raised when a workflow artifact cannot be validated."""


def load_json(path: Path) -> Any:
    """Load one UTF-8 JSON document with a useful path-aware error."""
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValidationError(f"Invalid JSON in {path}: {exc}") from exc


def resolve_json_pointer(document: Any, pointer: str) -> Any:
    """Resolve an RFC 6901 JSON Pointer."""
    if pointer in ("", "#"):
        return document
    pointer = pointer.removeprefix("#")
    if not pointer.startswith("/"):
        raise ValidationError(f"Invalid JSON Pointer: {pointer}")
    current = document
    for raw_token in pointer[1:].split("/"):
        token = raw_token.replace("~1", "/").replace("~0", "~")
        try:
            current = current[int(token)] if isinstance(current, list) else current[token]
        except (KeyError, IndexError, TypeError, ValueError) as exc:
            raise ValidationError(f"JSON Pointer target does not exist: {pointer}") from exc
    return current


def _schema_target(ref: str, schema_path: Path, repository_root: Path) -> tuple[Any, Path]:
    file_part, _, fragment = ref.partition("#")
    target_path = schema_path if not file_part else (
        repository_root / file_part
        if file_part.startswith("System-References/")
        else schema_path.parent / file_part
    )
    document = load_json(target_path)
    return resolve_json_pointer(document, f"#{fragment}" if fragment else ""), target_path


def _matches_type(value: Any, expected: str) -> bool:
    if expected == "object":
        return isinstance(value, Mapping)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "boolean":
        return isinstance(value, bool)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if expected == "null":
        return value is None
    return True


def _validate(
    value: Any,
    schema: Mapping[str, Any],
    *,
    schema_path: Path,
    repository_root: Path,
    location: str,
) -> list[str]:
    errors: list[str] = []
    if "$ref" in schema:
        target, target_path = _schema_target(str(schema["$ref"]), schema_path, repository_root)
        return _validate(
            value,
            target,
            schema_path=target_path,
            repository_root=repository_root,
            location=location,
        )
    for branch in schema.get("allOf", []):
        errors.extend(
            _validate(
                value,
                branch,
                schema_path=schema_path,
                repository_root=repository_root,
                location=location,
            )
        )
    if "anyOf" in schema:
        branch_errors = [
            _validate(
                value,
                branch,
                schema_path=schema_path,
                repository_root=repository_root,
                location=location,
            )
            for branch in schema["anyOf"]
        ]
        if all(branch_errors):
            errors.append(f"{location}: expected at least one matching schema")
    if "if" in schema:
        condition_errors = _validate(
            value,
            schema["if"],
            schema_path=schema_path,
            repository_root=repository_root,
            location=location,
        )
        selected = schema.get("then") if not condition_errors else schema.get("else")
        if isinstance(selected, Mapping):
            errors.extend(
                _validate(
                    value,
                    selected,
                    schema_path=schema_path,
                    repository_root=repository_root,
                    location=location,
                )
            )
    if "oneOf" in schema:
        branch_errors = [
            _validate(
                value,
                branch,
                schema_path=schema_path,
                repository_root=repository_root,
                location=location,
            )
            for branch in schema["oneOf"]
        ]
        if sum(not item for item in branch_errors) != 1:
            errors.append(f"{location}: expected exactly one matching schema")
        return errors
    expected_type = schema.get("type")
    if expected_type:
        expected_types = [expected_type] if isinstance(expected_type, str) else expected_type
        if not any(_matches_type(value, item) for item in expected_types):
            return [f"{location}: expected type {' | '.join(expected_types)}"]
    if "const" in schema and value != schema["const"]:
        errors.append(f"{location}: expected constant {schema['const']!r}")
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{location}: value is not in the allowed enum")
    if isinstance(value, Mapping):
        required = schema.get("required", [])
        errors.extend(f"{location}: missing required property {key}" for key in required if key not in value)
        properties = schema.get("properties", {})
        for key, child in value.items():
            if key in properties:
                errors.extend(
                    _validate(
                        child,
                        properties[key],
                        schema_path=schema_path,
                        repository_root=repository_root,
                        location=f"{location}/{key}",
                    )
                )
            elif schema.get("additionalProperties") is False:
                errors.append(f"{location}: unexpected property {key}")
    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0):
            errors.append(f"{location}: too few items")
        if "maxItems" in schema and len(value) > schema["maxItems"]:
            errors.append(f"{location}: too many items")
        item_schema = schema.get("items")
        if isinstance(item_schema, Mapping):
            for index, item in enumerate(value):
                errors.extend(
                    _validate(
                        item,
                        item_schema,
                        schema_path=schema_path,
                        repository_root=repository_root,
                        location=f"{location}/{index}",
                    )
                )
    if isinstance(value, str):
        if len(value) < schema.get("minLength", 0):
            errors.append(f"{location}: string is too short")
        if "pattern" in schema and not re.search(str(schema["pattern"]), value):
            errors.append(f"{location}: string does not match required pattern")
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if "minimum" in schema and value < schema["minimum"]:
            errors.append(f"{location}: value is below minimum")
        if "maximum" in schema and value > schema["maximum"]:
            errors.append(f"{location}: value is above maximum")
    return errors


def validate_schema(instance: Any, schema_path: Path, repository_root: Path) -> list[str]:
    """Validate the JSON Schema subset used by this repository."""
    # lazy: keep this to the repository's used keywords; adopt a standards library if schemas outgrow it.
    schema = load_json(schema_path)
    return _validate(
        instance,
        schema,
        schema_path=schema_path,
        repository_root=repository_root,
        location="$",
    )


def _walk(value: Any, path: str = "$") -> Iterable[tuple[str, str, Any]]:
    if isinstance(value, Mapping):
        for key, child in value.items():
            child_path = f"{path}/{key}"
            yield child_path, str(key), child
            yield from _walk(child, child_path)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from _walk(child, f"{path}/{index}")


def validate_reference_integrity(
    documents: Mapping[str, Any], repository_root: Path
) -> dict[str, list[str] | str]:
    """Resolve stable-ID and file-plus-pointer references across loaded documents."""
    definitions: dict[str, list[str]] = {}
    references: list[tuple[str, str]] = []
    for document_path, document in documents.items():
        for location, key, value in _walk(document, document_path):
            manifest_index_ref = key == "artifact_id" and "stage-manifest.json/artifacts/" in location
            if not manifest_index_ref and (key == "id" or key.endswith("_id")) and isinstance(value, str) and ID_PATTERN.fullmatch(value):
                definitions.setdefault(value, []).append(location)
            if key.endswith("_ref") and isinstance(value, str):
                references.append((location, value))
            elif key.endswith("_refs") and isinstance(value, list):
                references.extend((f"{location}/{index}", item) for index, item in enumerate(value) if isinstance(item, str))
    missing: list[str] = []
    checked: list[str] = []
    for location, reference in references:
        if "#" in reference and reference.split("#", 1)[0].endswith(".json"):
            file_part, pointer = reference.split("#", 1)
            try:
                resolve_json_pointer(load_json(repository_root / file_part), f"#{pointer}")
                checked.append(reference)
            except ValidationError:
                missing.append(f"{location}: {reference}")
        elif ID_PATTERN.fullmatch(reference):
            checked.append(reference)
            if reference not in definitions:
                missing.append(f"{location}: {reference}")
    duplicates = [identifier for identifier, locations in definitions.items() if len(locations) > 1]
    status = "failed" if missing or duplicates else "passed"
    return {
        "checked_refs": sorted(set(checked)),
        "missing_refs": sorted(missing),
        "duplicate_ids": sorted(duplicates),
        "integrity_status": status,
        "blocking_ref_errors": sorted(missing + duplicates),
    }
