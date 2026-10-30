# Genesis App Building Harness

Genesis is an orchestration harness for taking an application from an early
idea through implementation, launch, and post-launch evolution. It is a
meta-framework rather than an application codebase: the repository contains
OpenCode skills, workflow contracts, schemas, stage outputs, and durable state
used to coordinate the work.

The harness divides application development into eight stages. Each stage owns
a specific kind of decision, produces structured artifacts, and hands those
artifacts to the next stage only after its readiness requirements are met.

## Workflow at a Glance

```text
Stage 1              Stage 2              Stage 3              Stage 4
Product          ->  Research &       ->  System           ->  UX & Interaction
Initialization       Validation           Architecture         Architecture
                                                                  |
                                                                  v
Stage 8              Stage 7              Stage 6              Stage 5
Post-Launch      <-  Launch &         <-  Implementation   <-  Development
Evolution            Operationalization   & Validation         Orchestration
```

| Stage | Purpose | Primary result | Orchestrating skill |
| --- | --- | --- | --- |
| 1 — Product Initialization | Turn an idea into a structured product, workflow, capability, and MVP model | Validation-ready product definition | `stage-1-product-initialization` |
| 2 — Research & Validation | Test product assumptions against evidence and feasibility constraints | Validated assumptions and architecture-readiness guidance | `stage-2-research-and-validation` |
| 3 — System Architecture | Define topology, services, data, APIs, integrations, infrastructure, security, and scale | Implementation-ready technical architecture | `stage-3-system-architecture` |
| 4 — UX & Interaction Architecture | Define journeys, screens, behaviors, states, accessibility, UI blueprints, and design foundations | Frontend build package | `stage-4-ux-interaction-architecture` |
| 5 — Development Orchestration | Convert approved product, architecture, and UX direction into executable engineering work | Sequenced tickets, assignments, test strategy, and release plan | `stage-5-development-orchestration` |
| 6 — Implementation & Validation | Build the planned system, validate behavior, repair failures, and detect regressions | Verified implementation and system-health evidence | `stage-6-implementation-validation` |
| 7 — Launch & Operationalization | Prepare deployment, monitoring, analytics, support, and operational controls | Launch decision and operational framework | `stage-7-launch-operationalization` |
| 8 — Post-Launch Evolution | Use live telemetry and operational learning to improve the product | Optimization, roadmap, AI, and scalability plans | `stage-8-post-launch-evolution` |

## How a Stage Runs

Every stage follows the same operating cycle:

1. Load approved upstream outputs and the stage's durable state.
1. Run the stage orchestrator and its ordered subskills.
1. Record structured outputs, assumptions, risks, evidence, and stable IDs.
1. Produce the handoff required by the next stage.
1. Run the global readiness audit.
1. Advance, revise the current stage, route a problem to an earlier stage, or
   stop as blocked.

The shared completion statuses are:

| Status | Meaning |
| --- | --- |
| `ready_for_next_stage` | Required outputs and the next-stage handoff are complete. |
| `needs_current_stage_revision` | The active stage must correct or complete its own work. |
| `needs_prior_stage_revision` | An earlier stage owns a blocking issue and must be revisited. |
| `blocked` | Progress requires missing input, approval, evidence, or system capability. |

### Approval gates

Stages 1–4 define product, validation, architecture, and UX direction. Each must
write a user-reviewable decision brief to
`Build-Plans/Stage-N/00-stage-decision-brief.md`. These stages cannot report
ready status until the brief is approved, unless the active contract profile
explicitly allows inferred approval.

Stages 5–8 consume approved direction and do not require a decision brief by
default.

### Handoffs and traceability

Each downstream artifact references the upstream IDs that justify it. The
expected traceability chain is:

```text
feature/workflow -> assumption -> architecture decision
-> journey/screen/behavior/UI blueprint -> slice/ticket/agent
-> implementation/validation -> launch gate -> telemetry/evolution finding
```

IDs remain stable after creation. A material change updates the existing
concept and preserves its references rather than silently replacing its ID.
The full prefix list and handoff shapes are defined in the
[global workflow contract](System-References/Docs/Global-Stage-Workflow-Contract.md).

For launch-critical workflows, the harness requires outcome evidence rather
than the mere presence of code or a contract:

```text
UI action -> route/API/action -> durable system effect
-> worker/service result -> result visible in UI -> test or preview evidence
```

### Audits, risks, and revision loops

The readiness audit checks required files, schemas, handoffs, reference
integrity, approval gates, risks, and evidence before a stage advances. A
failed audit creates an actionable revision record owned by the stage that can
correct the problem.

Examples of revision ownership include:

- Product, workflow, or MVP issues return to Stage 1.
- Unsupported assumptions return to Stage 2.
- Service, data, API, infrastructure, security, or scale issues return to
  Stage 3.
- Journey, screen, behavior, accessibility, or visual-system issues return to
  Stage 4.
- Sequencing, ticket, testing, or release-plan issues return to Stage 5.
- Implementation, regression, validation, or visual-QA issues return to Stage
  6.
- Deployment, monitoring, support, or launch-readiness issues return to Stage
  7.
- Telemetry, optimization, roadmap, AI, or live-scale needs belong to Stage 8.

Accepted risks remain visible in
`Build-Plans/Build-status/Risk-acceptance-ledger.json`. Test results,
screenshots, previews, build logs, deployment proof, and other evidence are
referenced through
`Build-Plans/Build-status/Artifact-evidence-registry.json` rather than copied
into every stage output.

## Repository Map

```text
.opencode/
  Skills/                  Stage orchestrators and reusable skill packages
  package.json             OpenCode plugin dependency
Build-Plans/
  Stage-1/ ... Stage-8/    Generated artifacts for each workflow stage
  Build-status/            Durable workflow, planning, risk, and evidence state
  Changes/                 Scoped post-baseline change records
System-References/
  Docs/                    Workflow contracts and detailed stage specifications
  Schemas/                 Draft 2020-12 JSON Schemas for structured outputs
  skill-regisry/           Registry used by agent-task planning
  plans/ and Misc/         Supporting plans, examples, and design references
Memory/                    Archived and distilled project context
AGENTS.md                   Repository rules for agentic coding tools
```

Stage 1–4 placeholder directories are committed. The Stage 5–8 orchestrators
create their output directories when those stages begin.

Each skill package follows this shape:

```text
.opencode/Skills/<skill-name>/
  skill.md                 Required frontmatter and operating instructions
  references/              Optional supporting guidance
  scripts/                 Optional Python utilities
  tests/                   Optional unittest coverage
```

## Getting Started

1. Review any existing product requirements under `System-References/PRD Docs/`.
1. Inspect
   [`Global-workflow-state.json`](Build-Plans/Build-status/Global-workflow-state.json)
   to identify the active stage and current blockers.
1. Invoke the
   [`stage-1-product-initialization`](.opencode/Skills/stage-1-product-initialization/skill.md)
   skill with the product idea, goals, users, and known constraints.
1. Review and approve the Stage 1 decision brief.
1. Run the Stage 1 readiness audit and address any reported revision loops.
1. Continue with the next stage only when the audit permits the handoff.

When resuming an existing project, begin with the global workflow state and
the active stage's files instead of restarting at Stage 1.

For a narrowly scoped change after a baseline exists, use the change-intake
workflow and keep its audits under `Build-Plans/Changes/`; do not overwrite the
baseline stage audits or current-stage state.

## Validation Commands

Python utilities use the standard library `unittest` framework:

```sh
python -m unittest discover .opencode/Skills/stage-summary/tests
python -m unittest discover .opencode/Skills/global-stage-readiness-audit/tests
python -m unittest discover .opencode/Skills/change-intake-router/tests
python -m unittest discover .opencode/Skills/skill-registry-builder/tests
```

Validate a structured stage output against its schema with
`check-jsonschema`:

```sh
check-jsonschema \
  --schemafile System-References/Schemas/stage-1-output.schema.json \
  Build-Plans/Build-status/Planning-state.json
```

The readiness audit also has a dependency-free entry point:

```sh
python3 \
  .opencode/Skills/global-stage-readiness-audit/scripts/run_readiness_audit.py \
  --stage 1 \
  --proposed-status ready_for_stage_2
```

## Authoritative References

- [Global Stage Workflow Contract](System-References/Docs/Global-Stage-Workflow-Contract.md)
- [Global Stage Readiness Audit](System-References/Docs/Global-Stage-Readiness-Audit.md)
- [Stage output schemas](System-References/Schemas/)
- [Stage orchestration skills](.opencode/Skills/)
- [Agent and contribution conventions](AGENTS.md)

The README is an entry point. If it conflicts with a workflow contract, schema,
or stage skill, use the more specific contract as the source of truth and
update this overview to match.
