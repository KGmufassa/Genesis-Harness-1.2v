"""Read normalized or legacy Stage 5 artifacts without modifying them."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Sequence

from stage5_contract import ARTIFACTS, CONTEXT_PATH, FORMAT_VERSION, ContractError


def _load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def resolve_artifact(
    stage5_dir: Path, artifact_type: str, *, with_context: bool = False
) -> dict[str, Any]:
    """Return canonical artifact data and optional context."""
    if artifact_type not in ARTIFACTS:
        raise ContractError(f"unknown artifact: {artifact_type}")
    definition = ARTIFACTS[artifact_type]
    default_artifact_path = stage5_dir / definition["filename"]
    manifest_path = stage5_dir / "09-stage-manifest.json"
    manifest = _load(manifest_path) if manifest_path.is_file() else None
    if isinstance(manifest, dict) and manifest.get("format_version") == FORMAT_VERSION:
        index = {
            item.get("artifact_type"): item for item in manifest.get("artifacts", [])
        }
        entry = index.get(artifact_type)
        if not entry or not isinstance(entry.get("path"), str):
            raise ContractError(f"manifest does not index artifact: {artifact_type}")
        # lazy: basename suffices while v2 artifacts stay flat; add root-aware
        # path resolution if a future contract permits nested artifact paths.
        artifact_path = stage5_dir / Path(entry["path"]).name
        context_path = stage5_dir / Path(str(manifest.get("context_ref", ""))).name
        if not context_path.is_file() or not artifact_path.is_file():
            raise ContractError("partial Stage 5 v2 handoff: indexed files are missing")
        context = _load(context_path)
        artifact = _load(artifact_path)
        expected_path = f"Build-Plans/Stage-5/{artifact_path.name}"
        if (
            context.get("format_version") != FORMAT_VERSION
            or manifest.get("format_version") != FORMAT_VERSION
            or artifact.get("format_version") != FORMAT_VERSION
            or artifact.get("context_ref") != CONTEXT_PATH
            or entry.get("path") != expected_path
            or entry.get("artifact_id") != artifact.get("artifact_id")
            or entry.get("data_path") != f"/data/{definition['data_key']}"
        ):
            raise ContractError("Stage 5 manifest, context, and artifact are inconsistent")
        result = {"artifact_type": artifact_type, "data": artifact["data"]}
        if with_context:
            result["context"] = context
        return result

    if not default_artifact_path.is_file():
        raise ContractError(f"missing Stage 5 artifact: {default_artifact_path}")
    artifact = _load(default_artifact_path)
    any_v2 = (
        isinstance(artifact, dict) and artifact.get("format_version") == FORMAT_VERSION
    ) or any(
        path.is_file()
        and isinstance(candidate := _load(path), dict)
        and candidate.get("format_version") == FORMAT_VERSION
        for item in ARTIFACTS.values()
        if (path := stage5_dir / item["filename"]) != default_artifact_path
    )
    if any_v2:
        raise ContractError("partial Stage 5 v2 handoff: context and manifest are required")

    data_key = definition["data_key"]
    if isinstance(artifact, dict) and data_key in artifact:
        canonical = {data_key: artifact[data_key]}
    elif isinstance(artifact, dict) and artifact_type in artifact:
        canonical = {data_key: artifact[artifact_type]}
    else:
        canonical = artifact
    result = {"artifact_type": artifact_type, "data": canonical, "legacy": True}
    if with_context:
        result["context"] = artifact
    return result


def build_parser() -> argparse.ArgumentParser:
    """Build the read-only resolver CLI parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--stage5-dir", type=Path, default=Path("Build-Plans/Stage-5")
    )
    parser.add_argument("--artifact", required=True, choices=sorted(ARTIFACTS))
    parser.add_argument("--with-context", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Resolve and print one Stage 5 payload."""
    args = build_parser().parse_args(argv)
    try:
        result = resolve_artifact(
            args.stage5_dir, args.artifact, with_context=args.with_context
        )
    except (ContractError, OSError, json.JSONDecodeError) as error:
        print(f"error: {error}")
        return 1
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
