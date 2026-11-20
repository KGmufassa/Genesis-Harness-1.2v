# AGENTS.md — Genesis App Building Harness

This file guides agentic coding tools operating in this repository. It
documents the project structure, workflow contracts, build/test commands,
and code style conventions.

---

## Quick Reference

Use these section links to load the relevant guidance.

| Section | Purpose |
|---------|---------|
| [Repository Overview](#repository-overview) | What this repo is |
| [Directory Structure](#directory-structure) | Where things live |
| [Stage Workflow Model](#stage-workflow-model) | Pipeline ownership and approvals |
| [Stage 4 Page Standards and Revisions](#stage-4-page-standards-and-revisions) | Page outputs, editing, and review gates |
| [Build / Lint / Test Commands](#build--lint--test-commands) | Tests and validation |
| [Health Reporting](#health-reporting) | Reporting-only diagnostics |
| [Code Style Guidelines](#code-style-guidelines) | Python/JSON/Markdown conventions |
| [Global ID Standards](#global-id-standards) | Stable traceability IDs |
| [Skill Architecture](#skill-architecture) | Skill package format |
| [Traceability Chain](#traceability-chain) | Upstream/downstream references |
| [Visual & Design Continuity](#visual--design-continuity) | Frontend continuity rules |

---

## Repository Overview

This is a **meta-framework / orchestration harness**. It defines an 8-stage
AI‑powered pipeline (Product Initialization → Post‑Launch Evolution) for
building applications. No application source code lives here yet — the repo
contains skill definitions, workflow contracts, JSON state files, and
schemas that drive the harness.

---

## Directory Structure

```text
.opencode/
  Skills/                   Skill packages (skill.md, references, scripts, tests)
Build-Plans/
  Build-status/             Canonical state, approvals, registries, and audits
  Changes/                  Approved scoped-change records
  Stage-1/ … Stage-4/        Existing application-output placeholders
  Stage-5/ … Stage-8/        Created during application workflow runs
System-References/
  Docs/                     Workflow contracts, stage drafts, health reports
  Schemas/                  Draft 2020-12 JSON schemas
  plans/                    Implementation and improvement plans
  skill-regisry/            Skill registry JSON for agent-task-builder
```

---

## Stage Workflow Model

```text
Stage 1 → Stage 2 → Stage 3 → Stage 4 → Stage 5 → Stage 6 → Stage 7 → Stage 8
```

Each stage produces structured outputs, a completion status, a handoff
object for the next stage, assumptions, risks, and traceability IDs.
Stages 1‑4 require a user‑reviewable decision brief (`Build-Plans/Stage-N/00-stage-decision-brief.md`) with explicit approval before readiness. Stages 1–7 use `ready_for_stage_N` for the next stage; Stage 8 uses `evolution_plan_ready` and `prior_stage_feedback`, with no Stage 9. The readiness audit records `ready_for_next_stage` as a boolean.

- Stage 3 selects and approves the concrete stack and deployment strategy.
- Stage 4 opens with waitlist validation after approved Stage 3 preflight; verified publication and signup/measurement checks are required, but demand targets and elapsed measurement windows do not block completion.
- Full application implementation remains Stage 6, apart from the focused Stage 4 waitlist exception.
- Run the global readiness audit before finalization; do not treat passing tests or stored hashes as evidence of actual user approval or live application success.

| Status | Meaning |
|--------|---------|
| `ready_for_stage_N` / `evolution_plan_ready` | Stage-specific ready status; audit must permit progression |
| `needs_current_stage_revision` | Current stage needs more work |
| `needs_prior_stage_revision` | Route back to an earlier stage |
| `blocked` | Missing input, approval, or system capability |

| Issue → Stage | Issue → Stage |
| Product / workflow / MVP → 1 | Invalidated assumptions → 2 |
| Service / data / API / security → 3 | Screen / behaviour / a11y / UI → 4 |
| Sequencing / ticket / testing → 5 | Implementation / validation / regression → 6 |
| Deployment / monitoring / launch → 7 | Telemetry / optimisation / scale → 8 |

---

## Stage 4 Page Standards and Revisions

Follow the [page standards and revision contract](.opencode/Skills/stage-4-ux-interaction-architecture/references/page-standards-and-revisions.md), the [page specification template](.opencode/Skills/stage-4-ux-interaction-architecture/references/page-spec-template.md), and the Stage 4 command skill.

- After design-system foundation and template selection, generate `PAGE-STANDARDS.md`, `Pages/README.md`, and `Pages/<screen_id>/page-spec.md` under `Build-Plans/Stage-4/` for every in-scope screen, including supporting screens. Human review reconciles inventory coverage against approved workflows.
- Derive shared standards from canonical design-system, accessibility, and interaction decisions; canonical JSON remains authoritative. Cover typography, colors, spacing/layout, responsive behavior, assets/icons, components, navigation/controls, accessibility, and UI states.
- Each page specifies assets, precise font styles or resolvable typography tokens, components, individual controls, routes/actions/outcomes, permissions, data/validation, states, responsive/accessibility behavior, and approved deviations from the shared standard. Preserve page → section → component → interactive element → route/action/`no_navigation` ownership.
- Generate `Page-Revisions/README.md`, `Page-Revisions/<change_id>.md`, and retained content snapshots. Record attribution (or explicitly unknown), reason, timestamp, affected IDs, before/after hashes, exact diffs, reviewed standard hashes, approvals, validation evidence, and downstream impacts. Reuse authoritative `CHANGE-` IDs when applicable.
- Preserve direct user edits and stable page paths. Follow edit → record → reconcile → validate → reapprove → propagate. Never overwrite user edits from stale state, fabricate prior history, or infer approval from hash updates.
- Keep `page_standards`, `page_specifications`, `page_baselines`, `page_revisions`, and `page_set_approval` in `Build-Plans/Build-status/UX-state.json`. Reset affected page approvals after edits and complete-set approval when screens are added/removed; review affected pages after shared-standard changes.
- Require approval of all written specifications and the complete page set before any Stitch generation/update or accepted fallback. Prototype approval remains a separate review. Run the read-only draft gate immediately before each prototype mutation; final readiness additionally checks completed blueprints and resolved or owned/routed downstream impacts.
- Link standards, page specifications, and the revision index from `09-complete-app-blueprint.md` for Stage 5/6 consumption. Preserve the existing Stage 5 handoff interface and keep Stitch metadata Stage-4-local.
- Create application-specific outputs during an application run; do not populate this unused harness with fictional pages or approvals.

---

## Build / Lint / Test Commands

No TypeScript/JavaScript build systems. Python utility scripts use **unittest**:

```sh
python3 -m unittest discover .opencode/Skills/stage-summary/tests
python3 -m unittest .opencode/Skills/stage-summary/tests/test_generate_stage_summaries.py
python3 -m unittest .opencode/Skills/stage-summary/tests/test_generate_stage_summaries.StageSummaryScriptTests.test_generates_summary_for_populated_stage_recursively
python3 -m unittest discover .opencode/Skills/global-stage-readiness-audit/tests
python3 -m unittest discover -s .opencode/Skills/global-stage-readiness-audit/tests -p test_page_specifications.py
python3 -m unittest discover .opencode/Skills/stage-4-ux-interaction-architecture/tests
python3 -m unittest discover .opencode/Skills/stage-5-development-orchestration/tests
python3 -m unittest discover .opencode/Skills/stage-health-report-check/tests
python3 -m unittest discover .opencode/Skills/change-intake-router/tests
python3 -m unittest discover .opencode/Skills/skill-registry-builder/tests
```

JSON validation:
```sh
check-jsonschema --schemafile System-References/Schemas/stage-1-output.schema.json Build-Plans/Build-status/Planning-state.json
```

Read-only Stage 4 gates (require populated application outputs):

```sh
python3 .opencode/Skills/global-stage-readiness-audit/scripts/page_specifications.py --workspace-root /path/to/application --phase draft
python3 .opencode/Skills/global-stage-readiness-audit/scripts/page_specifications.py --workspace-root /path/to/application --phase final
```

Dependency-free readiness finalization **writes audit/global state**. Run it in the intended application workspace, not as a read-only health probe of this unused harness:

```sh
python3 .opencode/Skills/global-stage-readiness-audit/scripts/run_readiness_audit.py --workspace-root /path/to/application --stage 1 --proposed-status ready_for_stage_2
```

---

## Health Reporting

- Use [stage-health-report-check](.opencode/Skills/stage-health-report-check/skill.md) for all-stage diagnostics; consult the current health report rather than hardcoding test counts, grades, or finding status here.
- Collect evidence in an absolute temporary path. Reproduce findings in isolated fixtures with passing controls; do not advance actual stage state or change approvals during diagnostics.
- Reporting-only updates are limited to the health report (`Stage-1-8 Health Report.mdx`) and Markdown/HTML improvement-plan editions in `System-References/Docs/`. Fixes require a separate implementation task.
- Review the health report and Markdown plan together before regenerating HTML. Preserve finding IDs, patch numbers, historical closures, and pending real-app work; disclose failed/skipped checks and unavailable visual previews.

```sh
python3 .opencode/Skills/stage-health-report-check/scripts/collect_health_evidence.py --workspace-root . --output /absolute/temporary/path/stage-health-evidence.json
python3 .opencode/Skills/stage-health-report-check/scripts/render_patch_plan.py --workspace-root .
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

```text
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

```text
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

```text
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

```text
Stage 4 shared standards + reviewed page specifications + revision history
  → UI blueprint → visual spec → design system foundation
  → Stage 5 frontend ticket → agent handoff
    → Stage 6 implementation → visual QA result
      → Stage 7 visual launch readiness
```

Stage 6 cannot complete visual-QA tickets without recording preview
evidence, responsive validation, and design system compliance. Stage 7
cannot mark launch readiness complete with unresolved visual QA failures
unless explicitly accepted as a launch risk.
