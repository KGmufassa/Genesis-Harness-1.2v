# AGENTS.md — Genesis App Building Harness

This file guides agentic coding tools operating in this repository. It
documents the project structure, workflow contracts, build/test commands,
and code style conventions.

---

## Quick Reference

Read the table below first. It maps section headings to line numbers so
you can load only the sections you need.

| Section | Lines | Purpose |
|---------|-------|---------|
| Repository Overview | 28-34 | What this repo is |
| Directory Structure | 38-51 | Where things live |
| Stage Workflow Model | 55-77 | 8-stage pipeline rules |
| Build / Lint / Test Commands | 80-93 | How to run tests |
| Code Style Guidelines | 97-104 | Python/JSON/Markdown conventions |
| Global ID Standards | 106-117 | ID prefixes for traceability |
| Skill Architecture | 121-145 | Skill package format |
| Traceability Chain | 148-161 | ID reference chain |
| Visual & Design Continuity | 165-179 | Frontend continuity rules |

---

## Repository Overview

This is a **meta-framework / orchestration harness**. It defines an 8-stage
AI‑powered pipeline (Product Initialization → Post‑Launch Evolution) for
building applications. No application source code lives here yet — the repo
contains skill definitions, workflow contracts, JSON state files, and
schemas that drive the harness.

---

## Directory Structure

```
.opencode/                  OpenCode agent configuration and skills
   Skills/                   87 skill packages (skill.md + refs + scripts)
  package.json              Only dependency: @opencode-ai/plugin
Build-Plans/                Stage output and build-status tracking
  Build-status/             JSON state files (architecture, UX, planning, etc.)
  Stage-1/ … Stage-4/      Stage output directories (empty placeholders)
System-References/
  Docs/                     Workflow contracts, stage drafts, health reports
  Schemas/                  JSON Schema (draft-2020-12) for stage outputs
  skill-regisry/            Skill registry JSON for agent-task-builder
```

---

## Stage Workflow Model

```
Stage 1 → Stage 2 → Stage 3 → Stage 4 → Stage 5 → Stage 6 → Stage 7 → Stage 8
```

Each stage produces structured outputs, a completion status, a handoff
object for the next stage, assumptions, risks, and traceability IDs.
Stages 1‑4 require a user‑reviewable decision brief (`Build-Plans/Stage-N/00-stage-decision-brief.md`). They may not use `ready_for_next_stage` unless `approval_status = "approved"`.

| Status | Meaning |
|--------|---------|
| `ready_for_next_stage` | Outputs/handoff complete enough to proceed |
| `needs_current_stage_revision` | Current stage needs more work |
| `needs_prior_stage_revision` | Route back to an earlier stage |
| `blocked` | Missing input, approval, or system capability |

| Issue → Stage | Issue → Stage |
| Product / workflow / MVP → 1 | Invalidated assumptions → 2 |
| Service / data / API / security → 3 | Screen / behaviour / a11y / UI → 4 |
| Sequencing / ticket / testing → 5 | Implementation / validation / regression → 6 |
| Deployment / monitoring / launch → 7 | Telemetry / optimisation / scale → 8 |

---

## Build / Lint / Test Commands

No TypeScript/JavaScript build systems. Python utility scripts use **unittest**:

```sh
python -m unittest discover .opencode/Skills/stage-summary/tests
python -m unittest .opencode/Skills/stage-summary/tests/test_generate_stage_summaries.py
python -m unittest .opencode/Skills/stage-summary/tests/test_generate_stage_summaries.StageSummaryScriptTests.test_generates_summary_for_populated_stage_recursively
python -m unittest discover .opencode/Skills/global-stage-readiness-audit/tests
python -m unittest discover .opencode/Skills/change-intake-router/tests
python -m unittest discover .opencode/Skills/skill-registry-builder/tests
```

JSON validation:
```sh
check-jsonschema --schemafile System-References/Schemas/stage-1-output.schema.json Build-Plans/Build-status/Planning-state.json
```

Dependency-free readiness validation:
```sh
python3 .opencode/Skills/global-stage-readiness-audit/scripts/run_readiness_audit.py --stage 1 --proposed-status ready_for_stage_2
```

---

## Code Style Guidelines

- **Python 3.10+** with `from __future__ import annotations`. Type annotations on all function signatures. Use `pathlib.Path` (never `os.path`). `argparse` for CLI, return `int` from `main()`. `subprocess.run(capture_output=True, text=True)` in tests. `snake_case` for functions/variables, `PascalCase` for classes. `json.loads(path.read_text(encoding="utf-8"))`. `unittest.TestCase` with `tempfile.TemporaryDirectory`. Favour `Sequence`/`Iterable` over `list`/`dict` in parameters.
- **JSON**: `snake_case` property names. Draft 2020-12 schema. `"additionalProperties": true` on stage schemas. Defaults: `[]` for arrays, `{}` for objects, `""` for strings, `false` for bools. `null` only for optional date/timestamp fields.
- **Markdown**: ATX headings. `---` section separators. Language-tagged code blocks. Backtick-wrapped IDs/filenames. GFM pipe tables. `-` for unordered, `1.` for ordered lists (never mixed).
- **Commits**: Short imperative mood, no period. E.g. `Add stage summary generation skill`.
- **lazy-mode**: Always active when creating or updating code. Climb the Ladder (YAGNI → stdlib → native → one line → minimum). Mark deliberate simplifications with `lazy:` comments naming the ceiling and upgrade path; `ponytail:` is also recognized. On-demand siblings: `lazy-mode-review`, `lazy-mode-audit`, `lazy-mode-debt`, `lazy-mode-gain`, `lazy-mode-help`.

---

## Global ID Standards

```
USER-  WORKFLOW-  CAP-  FEATURE-  BOUNDARY-  DEP-  RISK-  ASSUMPTION-
SERVICE-  ENTITY-  API-  INTEGRATION-  INFRA-  SECURITY-  SCALE-
JOURNEY-  SCREEN-  BEHAVIOR-  STATE-  A11Y-  UI-BLUEPRINT-  VISUAL-SPEC-
UI-ELEMENT-  ROUTE-  ACTION-  DESIGN-SYSTEM-  SLICE-  TICKET-  AGENT-
BATCH-  VALIDATION-  VISUAL-QA-
ARTIFACT-  LAUNCH-GATE-  TELEMETRY-  EXPERIMENT-  CHANGE-
```

IDs are stable once created. If a concept changes materially, update the
object and preserve references — never silently replace the ID.

---

## Skill Architecture

Each skill lives in `.opencode/Skills/<skill-name>/` and follows:

```
skill.md          # YAML frontmatter + instructions (required)
references/       # Supporting markdown docs (optional)
scripts/          # Python utility scripts (optional)
tests/            # unittest test files (optional)
```

### skill.md Format

```yaml
---
name: <kebab-case-name>
description: One‑sentence summary of when to invoke this skill.
compatibility: opencode
---
```

The body uses category‑based headings (no numbered steps). Rules are
presented as bullet lists, never as paragraphs. Every skill updates its
skill.md file in place when the team learns something new.

---

## Traceability Chain

Every downstream object references the upstream IDs that justify it:

```
Stage 1 feature/workflow
  → Stage 2 assumption
    → Stage 3 architecture decision
      → Stage 4 screen/behaviour/state/UI blueprint
        → Stage 5 slice/ticket/agent
          → Stage 6 implementation/validation/visual QA
            → Stage 7 launch gate/operational signal
              → Stage 8 telemetry/evolution finding
```

---

## Visual & Design Continuity

Frontend‑facing work must preserve:

```
Stage 4 UI blueprint → visual spec → design system foundation
  → Stage 5 frontend ticket → agent handoff
    → Stage 6 implementation → visual QA result
      → Stage 7 visual launch readiness
```

Stage 6 cannot complete visual-QA tickets without recording preview
evidence, responsive validation, and design system compliance. Stage 7
cannot mark launch readiness complete with unresolved visual QA failures
unless explicitly accepted as a launch risk.
