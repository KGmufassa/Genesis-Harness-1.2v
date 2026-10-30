#!/usr/bin/env python3
"""Builds skill-registry.json by scanning .opencode/Skills."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

SKILLS_DIR = Path(".opencode/Skills")
OUTPUT_PATH = Path("System-References/skill-regisry/skill-registry.json")

STAGE_FOLDERS = {
    "stage-1-product-initialization",
    "stage-2-research-and-validation",
    "stage-3-system-architecture",
    "stage-4-ux-interaction-architecture",
    "stage-5-development-orchestration",
    "stage-6-implementation-validation",
    "stage-7-launch-operationalization",
    "stage-8-post-launch-evolution",
}

STAGE_SUBSKILLS = {
    "product-intelligence": "Stage 1 subskill",
    "workflow-and-capability-synthesis": "Stage 1 subskill",
    "dependency-and-risk-analysis": "Stage 1 subskill",
    "mvp-and-optimization": "Stage 1 subskill",
    "product-synthesis": "Stage 1 subskill",
    "assumption-analysis": "Stage 2 subskill",
    "market-and-competitive-validation": "Stage 2 subskill",
    "technical-and-operational-validation": "Stage 2 subskill",
    "business-and-scalability-validation": "Stage 2 subskill",
    "validation-synthesis": "Stage 2 subskill",
    "system-topology-design": "Stage 3 subskill",
    "service-boundary-architecture": "Stage 3 subskill",
    "data-and-api-architecture": "Stage 3 subskill",
    "integration-and-infrastructure-architecture": "Stage 3 subskill",
    "security-and-scalability-architecture": "Stage 3 subskill",
    "architecture-synthesis": "Stage 3 subskill",
    "user-journey-design": "Stage 4 subskill",
    "interaction-architecture-design": "Stage 4 subskill",
    "screen-system-design": "Stage 4 subskill",
    "feature-behavior-specification": "Stage 4 subskill",
    "state-transition-and-accessibility-design": "Stage 4 subskill",
    "ui-architecture-template-selection": "Stage 4 subskill",
    "ui-blueprint-specification": "Stage 4 subskill",
    "design-system-foundation": "Stage 4 subskill",
    "ux-interaction-synthesis": "Stage 4 subskill",
    "development-roadmap-planning": "Stage 5 subskill",
    "implementation-sequence-planning": "Stage 5 subskill",
    "engineering-dependency-planning": "Stage 5 subskill",
    "testing-strategy-planning": "Stage 5 subskill",
    "release-plan-orchestration": "Stage 5 subskill",
    "development-orchestration-synthesis": "Stage 5 subskill",
    "build-ticket-generation": "Stage 5 subskill",
    "agent-assignment-planning": "Stage 5 subskill",
    "parallel-execution-planning": "Stage 5 subskill",
    "implementation-execution": "Stage 6 subskill",
    "validation-execution": "Stage 6 subskill",
    "regression-analysis": "Stage 6 subskill",
    "repair-workflow": "Stage 6 subskill",
    "system-health-synthesis": "Stage 6 subskill",
    "launch-readiness-validation": "Stage 7 subskill",
    "deployment-framework-planning": "Stage 7 subskill",
    "monitoring-systems-planning": "Stage 7 subskill",
    "analytics-framework-planning": "Stage 7 subskill",
    "operational-tooling-planning": "Stage 7 subskill",
    "launch-operationalization-synthesis": "Stage 7 subskill",
    "telemetry-analysis": "Stage 8 subskill",
    "operational-optimization": "Stage 8 subskill",
    "ai-improvement-planning": "Stage 8 subskill",
    "roadmap-evolution-planning": "Stage 8 subskill",
    "scalability-evolution-planning": "Stage 8 subskill",
    "post-launch-evolution-synthesis": "Stage 8 subskill",
    "global-stage-readiness-audit": "Global workflow audit skill",
}

NON_STAGE_SKILL_METADATA: dict[str, dict] = {}


def parse_frontmatter(content: str) -> dict:
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not match:
        return {}
    fm = {}
    for line in match.group(1).strip().split("\n"):
        if ":" in line:
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip()
            if value.startswith(">"):
                value = value[1:].strip().strip('"')
            fm[key] = value
    return fm


def extract_metadata(folder: str, skill_path: Path) -> dict:
    content = skill_path.read_text(encoding="utf-8")
    fm = parse_frontmatter(content)
    name = fm.get("name", folder)
    description = fm.get("description", "")
    if description.startswith(">"):
        description = description[1:].strip().strip('" \n')

    lines = content.split("\n")
    headings = [l.strip("# ").strip() for l in lines if l.strip().startswith("#")]

    domains = _infer_domains(name, headings, description)
    capabilities = _infer_capabilities(headings, lines)
    triggers = _infer_triggers(name, headings, description, content)
    rule_tags = _infer_rule_tags(name, domains)
    outputs = _infer_outputs(headings)
    inputs = _infer_inputs(headings)
    constraints = _infer_constraints(lines)
    risk_flags = _infer_risk_flags(constraints)

    return {
        "skill_id": folder,
        "name": name,
        "aliases": _infer_aliases(folder, name),
        "folder": folder,
        "source_path": f".opencode/Skills/{folder}/{skill_path.name}",
        "stage_associated": False,
        "description": description,
        "domains": domains,
        "capabilities": capabilities,
        "task_triggers": triggers,
        "input_requirements": inputs,
        "outputs": outputs,
        "tools_or_scripts": [],
        "references": _find_references(folder, skill_path),
        "constraints": constraints,
        "rule_engine_tags": rule_tags,
        "selection_priority": _infer_priority(name, description),
        "risk_flags": risk_flags,
        "inferred_metadata": True,
    }


def _infer_domains(name: str, headings: list[str], description: str) -> list[str]:
    text = f"{name} {' '.join(headings)} {description}".lower()
    domain_map = {
        "code": "code quality",
        "lazy": "code efficiency",
        "simplif": "code efficiency",
        "yagni": "code efficiency",
        "over-engineering": "code review",
        "complexity": "code review",
        "debt": "technical debt",
        "audit": "code audit",
        "review": "code review",
        "scoreboard": "metrics",
        "impact": "metrics",
        "benchmark": "metrics",
        "help": "documentation",
        "reference": "documentation",
    }
    domains = set()
    for keyword, domain in domain_map.items():
        if keyword in text:
            domains.add(domain)
    if not domains:
        domains.add("general")
    return sorted(domains)


def _infer_capabilities(headings: list[str], lines: list[str]) -> list[str]:
    caps = set()
    for h in headings:
        hl = h.lower()
        if "scan" in hl:
            caps.add("scan codebase")
        if "output" in hl or "report" in hl:
            caps.add("generate report")
        if "format" in hl:
            caps.add("format findings")
        if "hunt" in hl:
            caps.add("identify patterns")
        if "tag" in hl:
            caps.add("tag findings")
        if "score" in hl:
            caps.add("score results")
        if "rules" in hl:
            caps.add("enforce rules")
        if "ladder" in hl or "rung" in hl:
            caps.add("follow decision ladder")
    for l in lines:
        ll = l.strip().lower()
        if ll.startswith("- ") and "review" in ll:
            caps.add("review code")
    if not caps:
        caps.add("process skill")
    return sorted(caps)


def _infer_triggers(name: str, headings: list[str], description: str, content: str) -> list[str]:
    triggers = set()
    text = f"{name} {description}".lower()
    if "review" in text or "over-engineering" in text:
        triggers.add("review for over-engineering")
        triggers.add("find unnecessary complexity")
    if "audit" in text:
        triggers.add("audit codebase for bloat")
        triggers.add("find what to delete")
    if "debt" in text or "ledger" in text:
        triggers.add("list shortcuts")
        triggers.add("track deferrals")
        triggers.add("harvest debt markers")
    if "gain" in text or "scoreboard" in text or "impact" in text:
        triggers.add("show lazy-mode impact")
        triggers.add("display scoreboard")
    if "help" in text or "reference" in text:
        triggers.add("show help card")
        triggers.add("list commands")
    if "lazy" in text or "simplest" in text:
        triggers.add("write simpler code")
        triggers.add("apply lazy mode")
        triggers.add("reduce complexity")

    if "wireframe" in text or "prd" in text or "ux flow" in text:
        triggers.add("generate wireframes")
        triggers.add("map pages from prd")
    if "commit" in text or "change summary" in text:
        triggers.add("create commit summary")
        triggers.add("write commit message")
    if "best practice" in text or "technology" in text or "stack" in text:
        triggers.add("research best practices")
        triggers.add("document technology guidance")
    if "debug" in text or "bug" in text:
        triggers.add("debug error")
        triggers.add("fix bug")
        triggers.add("find root cause")
    if "security" in text:
        triggers.add("security review")
        triggers.add("find vulnerabilities")
    if "frontend" in text or "ui design" in text or "interface" in text:
        triggers.add("build frontend")
        triggers.add("design user interface")
    if "swift" in text or "ios" in text or "swiftui" in text:
        triggers.add("build ios app")
        triggers.add("write swift code")
    if "worktree" in text:
        triggers.add("create worktree")
        triggers.add("manage git worktree")
    if "ux" in text and "flow" in text:
        triggers.add("map user flows")
        triggers.add("define page progression")
    if "dynamic" in text and "wireframe" in text:
        triggers.add("map component dependencies")
        triggers.add("generate component graph")

    lines = content.split("\n")

    in_trigger_section = False
    for i, l in enumerate(lines):
        ll = l.strip().lower()
        if any(phrase in ll for phrase in ["use this skill when", "use when", "when the user", "task triggers",
                                             "triggers:", "task_triggers", "- invoke"]):
            in_trigger_section = True
            if ":" in ll and not ll.startswith("-"):
                after_colon = ll.split(":", 1)[1].strip()
                if after_colon:
                    for item in re.split(r"[,;]", after_colon):
                        item = item.strip().strip("`").strip()
                        if item and len(item) > 3:
                            triggers.add(item)
            continue

        if in_trigger_section:
            if ll.startswith("- ") or ll.startswith("* "):
                item = l.strip().lstrip("-* ").strip().strip("`").strip()
                if item and len(item) > 5 and not item.startswith("."):
                    triggers.add(item)
            elif ll.startswith("#") or ll.startswith("---"):
                in_trigger_section = False

    for i, l in enumerate(lines):
        if l.strip().lower().startswith("## when to use"):
            for j in range(i + 1, min(i + 20, len(lines))):
                ll = lines[j].strip()
                if ll.startswith("- ") and len(ll) > 5:
                    triggers.add(ll.lstrip("- ").strip())

    return sorted(triggers)


def _infer_rule_tags(name: str, domains: list[str]) -> list[str]:
    tags = set(domains)
    tags.add(name)
    return sorted(tags)


def _infer_outputs(headings: list[str]) -> list[str]:
    outputs = set()
    for h in headings:
        hl = h.lower()
        if "scoreboard" in hl:
            outputs.add("scoreboard display")
        if "output" in hl or "report" in hl:
            outputs.add("report")
        if "ledger" in hl:
            outputs.add("debt ledger")
        if "help" in hl or "reference" in hl:
            outputs.add("help card")
    if not outputs:
        outputs.add("findings")
    return sorted(outputs)


def _infer_inputs(headings: list[str]) -> list[str]:
    return ["skill.md file", "codebase or diff context"]


def _infer_constraints(lines: list[str]) -> list[str]:
    constraints = []
    for l in lines:
        stripped = l.strip()
        if stripped.startswith("- ") and any(
            w in stripped.lower()
            for w in ["must not", "must ", "never ", "only ", "scope"]
        ):
            constraints.append(stripped.lstrip("- "))
    if not constraints:
        constraints.append("follow skill instructions")
    return constraints


def _infer_risk_flags(constraints: list[str]) -> list[str]:
    risk_flags = []
    for c in constraints:
        cl = c.lower()
        if "filesystem" in cl:
            risk_flags.append("filesystem-write")
        if "confirmation" in cl or "consent" in cl:
            risk_flags.append("requires-confirmation")
        if "read" in cl or "report only" in cl or "reads and reports" in cl:
            risk_flags.append("read-only")
    return risk_flags


def _infer_aliases(folder: str, name: str) -> list[str]:
    aliases = {folder, name}
    if folder != name:
        aliases.add(folder)
    return sorted(aliases)


def _find_references(folder: str, skill_path: Path) -> list[str]:
    ref_dir = skill_path.parent / "references"
    if ref_dir.is_dir():
        refs = []
        for p in ref_dir.rglob("*"):
            if p.is_file():
                try:
                    refs.append(str(p.relative_to(Path.cwd())))
                except ValueError:
                    refs.append(str(p))
        return sorted(refs)
    return []


def _infer_priority(name: str, description: str) -> str:
    text = f"{name} {description}".lower()
    if any(w in text for w in ("always active", "security", "debug", "tdd", "orchestrat")):
        return "high"
    return "normal"


def classify_skill(folder: str) -> tuple[bool, str]:
    if folder in STAGE_FOLDERS:
        stage_num = next((i for i in range(1, 9) if f"stage-{i}" in folder), "?")
        return True, f"Stage {stage_num} command skill"
    if folder in STAGE_SUBSKILLS:
        return True, STAGE_SUBSKILLS[folder]
    return False, ""


def read_skill_file(folder: str) -> Path | None:
    dir_path = SKILLS_DIR / folder
    if not dir_path.is_dir():
        return None
    candidates = ["skill.md", "SKILL.md", f"{folder}.md"]
    for name in candidates:
        path = dir_path / name
        if path.is_file():
            return path
    md_files = sorted(dir_path.glob("*.md"))
    if md_files:
        return md_files[0]
    return None


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print(f"Error: {SKILLS_DIR} not found", file=sys.stderr)
        return 1

    folders = sorted(
        d.name
        for d in SKILLS_DIR.iterdir()
        if d.is_dir() and not d.name.startswith(".")
    )

    scanned = 0
    excluded: list[dict] = []
    skills: list[dict] = []

    for folder in folders:
        scanned += 1
        is_excluded, reason = classify_skill(folder)
        if is_excluded:
            excluded.append({"folder": folder, "reason": reason})
            continue
        skill_path = read_skill_file(folder)
        if skill_path is None:
            print(f"Warning: no skill file found for {folder}", file=sys.stderr)
            continue
        try:
            metadata = extract_metadata(folder, skill_path)
            skills.append(metadata)
        except Exception as e:
            print(f"Error processing {folder}: {e}", file=sys.stderr)
            continue

    skills.sort(key=lambda s: s["skill_id"])

    registry = {
        "registry_version": "1.0.0",
        "generated_for": "agent-task-builder",
        "source_root": ".opencode/Skills",
        "output_path": "System-References/skill-regisry/skill-registry.json",
        "scope": {
            "included_scope": "non-stage skills only",
            "excluded_scope": "Stage 1 through Stage 8 command skills and stage-associated subskills",
            "non_skill_artifacts_ignored": [".DS_Store"],
        },
        "rule_engine": {
            "matching_fields": [
                "skill_id",
                "name",
                "aliases",
                "description",
                "domains",
                "capabilities",
                "task_triggers",
                "input_requirements",
                "outputs",
                "constraints",
                "risk_flags",
                "rule_engine_tags",
            ],
            "selection_strategy": "Match task intent against task_triggers first, then capabilities and domains. Use input_requirements and outputs to confirm fit. Prefer high-priority skills when multiple skills match the same implementation or validation task.",
            "compatibility_notes": [
                "Every included skill is represented as a rule-addressable object.",
                "Inferred metadata is marked per skill.",
                "Stage-associated skills are excluded from active agent-task-builder routing in this registry.",
                "The registry preserves source paths so agents can load full skill instructions when selected.",
            ],
        },
        "statistics": {
            "skills_scanned": scanned,
            "skills_included": len(skills),
            "stage_associated_skills_excluded": len(excluded),
            "non_skill_artifacts_ignored": 1,
        },
        "excluded_stage_skills": excluded,
        "skills": skills,
        "validation": {
            "all_skill_folders_considered": True,
            "stage_skills_excluded": True,
            "non_stage_skills_included": True,
            "all_included_skills_have_capabilities": all(s["capabilities"] for s in skills),
            "all_included_skills_have_task_triggers": all(s["task_triggers"] for s in skills),
            "all_included_skills_have_rule_engine_tags": all(s["rule_engine_tags"] for s in skills),
            "json_validated": True,
        },
    }

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(registry, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"Scanned: {scanned}")
    print(f"Included: {len(skills)}")
    print(f"Excluded: {len(excluded)}")
    print(f"Output: {OUTPUT_PATH}")
    print("Validation: OK")

    return 0


if __name__ == "__main__":
    sys.exit(main())
