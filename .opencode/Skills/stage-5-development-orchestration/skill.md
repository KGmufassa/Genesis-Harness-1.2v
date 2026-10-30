---
name: stage-5-development-orchestration
description: Orchestrate a normalized, dependency-safe Stage 5 planning package for future Stage 6 execution.
compatibility: opencode
---

# Command — stage-5-development-orchestration

# Purpose

The `stage-5-development-orchestration` command orchestrates Stage 5.

It transforms:

* Stage 1 product model
* Stage 2 validation outputs
* Stage 3 system architecture
* Stage 4 UX and interaction architecture
* known risks, dependencies, and constraints

into:

* development roadmap
* implementation sequence
* engineering dependency map
* testing strategy
* build tickets
* agent assignment plan
* parallel execution plan
* release plan

This is the Stage 5 command skill. It is not a single planning subskill.

---

# Cognitive Boundary

Stage 5 asks:

```text
How should engineering execution be sequenced, coordinated, tested, and released?
```

Stage 5 must not:

* redefine product strategy
* perform validation research
* redesign system architecture
* redesign UX flows
* write production code
* perform QA execution

Stage 5 may recommend earlier-stage revision only when execution planning exposes a blocking dependency, missing specification, or unresolved contradiction.

---

# Output Directory

All final Stage 5 outputs must be recorded in:

```text
Build-Plans/Stage-5/
```

The command must create this folder if it does not exist.

---

# Shared Development Orchestration State

The command maintains a shared Stage 5 development orchestration state object.

The shared orchestration state is transient working memory. Do not copy it into
the numbered outputs. Durable shared Stage 5 information is written once to:

```text
Build-Plans/Stage-5/00-stage-context.json
```

The command may update workflow state only through the normal, intentionally
invoked stage workflow. The output contract itself does not require a duplicate
`Development-state.json`.

```json
{
  "stage": "Stage 5",
  "command": "stage-5-development-orchestration",
  "status": "not_started",
  "stage_1_inputs": {},
  "stage_2_inputs": {},
  "stage_3_inputs": {},
  "stage_4_inputs": {},
  "preflight": {},
  "ui_blueprint_inputs": {},
  "visual_spec_inputs": {},
  "design_system_inputs": {},
  "visual_reference_inputs": {},
  "frontend_build_package": {},
  "development_roadmap": {},
  "implementation_sequence": {},
  "engineering_dependencies": {},
  "testing_strategy": {},
  "build_tickets": {},
  "agent_assignment_plan": {},
  "parallel_execution_plan": {},
  "release_plan": {},
  "milestones": [],
  "workstreams": [],
  "execution_risks": [],
  "coordination_notes": [],
  "open_questions": [],
  "interactive_guidance": {
    "open_questions": [],
    "answered_questions": [],
    "assumptions_made": [],
    "blocked_decisions": [],
    "user_confirmations": [],
    "execution_confidence_gaps": []
  },
  "schema_validation": {
    "validation_executed": false,
    "schemas_valid": false,
    "results": []
  }
}
```

Each subskill reads and updates this transient object before final normalized
serialization. Completion status and the Stage 6 handoff are held separately
until they are written only to `09-stage-manifest.json`.

---

# Interactive Guidance Rules

The Stage 5 command should behave like a guided engineering execution planning interview.

Use this decision rule:

```text
Ask only for execution decisions that materially affect implementation order, dependency sequencing, testing scope, release readiness, or Stage 6 execution.
Infer standard engineering defaults when risk is low and earlier-stage outputs support the inference.
Record assumptions when proceeding without user confirmation.
Block only when a missing decision prevents coherent engineering orchestration.
```

When asking the user questions:

* ask 1-3 questions at a time
* prioritize implementation-blocking dependencies first
* avoid asking questions already answered by Stages 1-4
* explain what roadmap, sequence, dependency, test, or release decision each question affects
* prefer concrete options over open-ended questions when the tradeoff is known
* update `interactive_guidance.open_questions`
* move answered questions into `interactive_guidance.answered_questions`
* record inferred defaults in `interactive_guidance.assumptions_made`
* record unresolved blockers in `interactive_guidance.blocked_decisions`

The command should continue automatically when an engineering planning decision has a low-risk default.

The command should pause for user input when:

* MVP launch scope is still ambiguous
* implementation order depends on an unresolved product or architecture decision
* dependency sequencing changes engineering feasibility
* testing scope materially changes release confidence
* release strategy affects what must be built first
* manual workaround tolerance is unknown
* Stage 6 cannot begin without a missing execution decision

The command should not ask the user to choose low-level implementation details that belong to Stage 6 unless the choice changes Stage 5 sequencing, testing, or release planning.

---

# Stage 5 Input Contract

Load Stage 1 outputs from:

```text
Build-Plans/Stage-1/
```

Load Stage 2 outputs from:

```text
Build-Plans/Stage-2/
```

Load Stage 3 outputs from:

```text
Build-Plans/Stage-3/
```

Load Stage 4 outputs from:

```text
Build-Plans/Stage-4/
```

Minimum viable input set:

```text
Stage 1:
05-feature-structure.json
08-mvp-operational-model.json
09-risk-and-constraints.json

Stage 3:
02-service-architecture.json
03-data-architecture.json
04-api-architecture.json
07-infrastructure-model.json

Stage 4:
03-screen-system.json
04-feature-behaviors.json
05-state-transition-map.json
07-ui-blueprint-specification.json
08-design-system-foundation.json
09-complete-app-blueprint.md
```

If the minimum viable input set is missing, stop and set:

```text
completion_status.status = "blocked"
completion_status.reason = "missing_development_orchestration_inputs"
```

Stage 5 must also consume the approved Stage 3 `selected_stack` from the Stage 3 architecture state, decision brief, or Stage 3 handoff.

Stage 5 must not invent, change, or defer the implementation stack. If `selected_stack` is missing, incomplete, or contains unresolved alternatives, stop and set:

```text
completion_status.status = "blocked"
completion_status.reason = "missing_or_unresolved_selected_stack"
```

If Stage 4 completion status is not `ready_for_stage_5`, continue only if unresolved issues are not execution-blocking. Record all carry-forward risks in `execution_risks`.

---

# Preflight Validation

Before development orchestration, validate:

* Stage 1 MVP scope exists
* Stage 3 architecture outputs exist and are readable
* Stage 3 `selected_stack` exists
* Stage 3 `selected_stack` has concrete choices for frontend, backend, database, auth, deployment, testing, and package manager
* Stage 3 `selected_stack` contains no unresolved alternatives such as `or`, `TBD`, `to decide later`, `optional`, or `depends`
* Stage 4 UX outputs exist and are readable
* Stage 4 UI blueprint output exists and is readable
* Stage 4 design system foundation exists and is readable
* Stage 4 selected visual style references exist when referenced by the design system foundation
* Stage 4 complete app blueprint markdown exists and is readable
* Stage 4 UI architecture template selection exists or records why no template applies
* launch-critical features are known
* service, data, API, and infrastructure dependencies are available
* feature behaviors and state transitions are clear enough to sequence implementation
* UI blueprints define launch-critical pages, components, routes, actions, states, interactive elements (buttons, links, menu items, etc.) with route_targets, visual specs, visual acceptance criteria, and frontend build package hints
* launch-critical UI blueprints define structural UI architecture context, including page archetype, layout pattern decision, component-family decisions, selected template/extensions, and template deviations when applicable
* every Stage 4 created page has a reconciled interaction contract and stable `UI-ELEMENT-`, `ROUTE-`, and `ACTION-` references
* Stage 4 interaction contracts have no required `needs_user_review` or `blocked` status
* required Stage 4 Mermaid maps reconcile with the structured page, element, route, action, and navigation inventories
* complete app blueprint markdown maps launch-critical pages to UI blueprint IDs and summarizes page sections, components, actions, routes, states, and data requirements
* complete app blueprint markdown summarizes UI architecture template selection, page archetypes, layout pattern decisions, component families, and template deviations when available
* `UI-COMPONENTS.md`, when generated by Stage 4, is readable and treated as a companion artifact rather than a canonical source of truth
* Stage 5 does not require or consume Stitch project IDs, screen IDs, prompts, approval ledgers, divergence logs, or MCP availability metadata
* design system foundation defines shared visual tokens, component rules, responsive rules, selected visual style references, and design approval status
* accessibility and security requirements are available for test planning
* earlier-stage risks do not block engineering planning

Record preflight results in:

```text
preflight
execution_risks
open_questions
interactive_guidance
completion_status
```

---

# Orchestrated Skills

Run Stage 5 skills in this order:

```text
1. development-roadmap-planning
2. implementation-sequence-planning
3. engineering-dependency-planning
4. testing-strategy-planning
5. build-ticket-generation
6. agent-assignment-planning
7. parallel-execution-planning
8. release-plan-orchestration
9. development-orchestration-synthesis
```

---

# Execution Sequence

## 1. Load Stage 1, Stage 2, Stage 3, And Stage 4 Outputs

Load and normalize earlier-stage outputs into:

```text
stage_1_inputs
stage_2_inputs
stage_3_inputs
stage_4_inputs
ui_blueprint_inputs
visual_spec_inputs
design_system_inputs
visual_reference_inputs
frontend_build_package
```

Do not modify earlier-stage outputs during Stage 5.

## 2. Initialize Shared Development State

Initialize the transient shared development state in memory. A normally invoked
workflow may update its general stage progress record, but must not persist
shared output context, `completion_status`, or `stage_6_handoff` there. Shared
output context belongs only in file `00`; completion and handoff belong only in
file `09`.

## 3. Run `development-roadmap-planning`

Required shared state updates:

```text
development_roadmap
workstreams
milestones
execution_risks
open_questions
interactive_guidance
```

## 4. Run `implementation-sequence-planning`

Required shared state updates:

```text
implementation_sequence
engineering_dependencies
execution_risks
coordination_notes
interactive_guidance
```

## 5. Run `engineering-dependency-planning`

Required shared state updates:

```text
engineering_dependencies
coordination_notes
execution_risks
open_questions
interactive_guidance
```

## 6. Run `testing-strategy-planning`

Required shared state updates:

```text
testing_strategy
execution_risks
coordination_notes
interactive_guidance
```

## 7. Run `build-ticket-generation`

Required shared state updates:

```text
build_tickets
engineering_dependencies
execution_risks
coordination_notes
stage_6_handoff
interactive_guidance
```

## 8. Run `agent-assignment-planning`

Required shared state updates:

```text
agent_assignment_plan
build_tickets
engineering_dependencies
execution_risks
coordination_notes
stage_6_handoff
interactive_guidance
```

## 9. Run `parallel-execution-planning`

Required shared state updates:

```text
parallel_execution_plan
agent_assignment_plan
engineering_dependencies
execution_risks
coordination_notes
stage_6_handoff
interactive_guidance
```

## 10. Run `release-plan-orchestration`

Required shared state updates:

```text
release_plan
execution_risks
coordination_notes
stage_6_handoff
interactive_guidance
```

## 11. Run `development-orchestration-synthesis`

Required shared state updates:

```text
development_roadmap
implementation_sequence
engineering_dependencies
testing_strategy
build_tickets
agent_assignment_plan
parallel_execution_plan
release_plan
execution_risks
coordination_notes
stage_6_handoff
completion_status
interactive_guidance
```

---

# Final Stage 5 Outputs

Generate format version `2.0`:

```text
Build-Plans/Stage-5/00-stage-context.json
Build-Plans/Stage-5/01-development-roadmap.json
Build-Plans/Stage-5/02-implementation-sequence.json
Build-Plans/Stage-5/03-engineering-dependencies.json
Build-Plans/Stage-5/04-testing-strategy.json
Build-Plans/Stage-5/05-build-tickets.json
Build-Plans/Stage-5/06-agent-assignment-plan.json
Build-Plans/Stage-5/07-parallel-execution-plan.json
Build-Plans/Stage-5/08-release-plan.json
Build-Plans/Stage-5/09-stage-manifest.json
Build-Plans/Stage-5/10-stage-5-summary.md
```

`10-stage-5-summary.md` is a local human-readable review artifact for every Stage 5 finalization attempt, including ready, revision, and blocked outcomes. It must summarize the actions taken, roadmap, implementation sequence, ticket plan, agent assignments, parallel execution plan, release plan, validation and reference-integrity evidence, blockers, major risks, next actions, Stage 6 handoff readiness, and a clear user assessment. It must not contain canonical data that is absent from the JSON outputs.

Do not add `10-stage-5-summary.md` to `stage_6_handoff`, required Stage 6 inputs, artifact indexes, or downstream readiness requirements. Stage 6 must continue to consume the normalized v2 JSON package and `09-stage-manifest.json`.

`00-stage-context.json` stores shared information exactly once: selected stack,
stage contract profile, guidance policy, Stage 1-4 source inputs, execution
decision references, assumptions, risks, unresolved questions,
reference-integrity results, risk acceptance, and revision loops.

Files `01` through `08` use this envelope:

```json
{
  "$schema": "System-References/Schemas/stage-5-artifact.schema.json",
  "format_version": "2.0",
  "artifact_id": "ARTIFACT-S5-*",
  "artifact_type": "",
  "stage": "Stage 5",
  "status": "",
  "context_ref": "Build-Plans/Stage-5/00-stage-context.json",
  "traceability_refs": [],
  "data": {}
}
```

Canonical data paths are:

| Artifact type | Data path |
|---|---|
| `development_roadmap` | `/data/roadmap` |
| `implementation_sequence` | `/data/slices` |
| `engineering_dependencies` | `/data/dependencies` |
| `testing_strategy` | `/data/testing_strategy` |
| `build_tickets` | `/data/tickets` |
| `agent_assignment_plan` | `/data/agents` |
| `parallel_execution_plan` | `/data/batches` |
| `release_plan` | `/data/release_plan` |

Testing collections remain inside `data.testing_strategy`; release collections
remain inside `data.release_plan`. Secondary views use stable IDs or compact
indexes. Records use `risk_refs` into the shared context. Never copy complete
ticket, risk, slice, agent, batch, completion, or handoff objects into another
field.

`09-stage-manifest.json` indexes all eight numbered artifacts with artifact ID,
type, path, schema reference, and JSON data path. It is the only file containing
`completion_status` and `stage_6_handoff`. It also records schema-validation
results. Set `schema_validation.schemas_valid` to `true` only after validation
has executed successfully.

Use the reusable construction and validation helpers in:

```text
.opencode/Skills/stage-5-development-orchestration/scripts/stage5_contract.py
```

The build ticket output must include:

* ticket IDs
* slice IDs
* ticket dependencies
* UI blueprint references for frontend tickets
* visual spec references and visual requirements for frontend tickets
* design system references for frontend tickets
* `visual_reference_refs` for frontend tickets
* page, component, shared component, route, state, and action references when applicable
* UI architecture template, extension, page archetype, layout pattern, component family, and template deviation references for frontend tickets when applicable
* `UI-COMPONENTS.md` references for frontend tickets when structural UI architecture context matters and the artifact exists
* frontend task hints from the Stage 4 frontend build package
* primary skill from the skill registry
* recommended skill chain from the skill registry
* required skills the assigned agent must use
* skill usage instructions for the assigned agent
* skill suitability score and selection rationale
* skill coverage gaps when no suitable skill exists
* acceptance criteria
* validation steps
* completion definition for launch-critical workflow tickets
* workflow smoke-test obligations for launch-critical user paths
* risk level
* Stage 6 execution queue position

Before serialization, validate every ticket reference against the actual loaded
Stage 1-4 documents. Stable ID references must exist in those documents.
File-plus-JSON-Pointer references must name an existing file and resolve to an
existing target. When visual acceptance criteria have no stable IDs, use a real
file-plus-JSON-Pointer reference rather than fabricating an ID.

Validate `risk_refs`, agent scopes, and execution waves with
`stage5_contract.py` before any output is written; validation failure stops
generation.

Launch-critical workflow tickets must also pass
`validate_workflow_completion_definitions` from `stage5_contract.py`. Do not
allow contract-only completion for user-facing workflows. Define done as a
verified user outcome through the full runtime chain:

```text
UI action -> route/API/action -> database/queue/storage -> worker/service -> result visible in UI -> evidence
```

---

# Completion Gate

Before Stage 5 may use `ready_for_stage_6`, run `global-stage-readiness-audit`.

The audit must write:

```text
Build-Plans/Build-status/Stage-5-readiness-audit.json
```

The audit must pass according to:

```text
System-References/Docs/Global-Stage-Workflow-Contract.md
```

If the audit does not pass, do not use `ready_for_stage_6`.

Stage 5 may complete only when:

* context, all eight numbered artifacts, and the manifest exist
* local human-readable assessment summary exists at `Build-Plans/Stage-5/10-stage-5-summary.md`
* the summary matches canonical Stage 5 JSON outputs and identifies whether the stage is ready, needs revision, or is blocked
* development roadmap is defined
* implementation sequence is dependency-aware
* engineering dependencies are mapped
* testing strategy covers launch-critical workflows
* build tickets cover every MVP implementation slice
* build tickets include a best-suited primary skill or record why no matching skill exists
* build tickets include an ordered recommended skill chain
* build tickets include required skills for the assigned agent
* build tickets include skill usage instructions for the assigned agent
* build tickets include skill suitability scores and selection rationale
* build tickets include acceptance criteria and validation steps
* launch-critical workflow tickets include `completion_definition`
* launch-critical workflow tickets include workflow smoke tests with expected user outcomes
* frontend build tickets reference applicable UI blueprint IDs or explicitly record why no UI blueprint applies
* frontend build tickets reference `09-complete-app-blueprint.md` when page structure, component structure, route structure, or state structure matters
* frontend build tickets preserve Stage 4 UI architecture template context, page archetype, layout pattern decisions, component-family decisions, and template deviations when applicable
* frontend build tickets reference `UI-COMPONENTS.md` when structural UI architecture template, extension, page archetype, layout pattern, component-family, or template-deviation context matters and the artifact exists
* frontend build tickets reference applicable visual spec IDs or explicitly record why no visual spec applies
* frontend build tickets reference applicable design system IDs or explicitly record why no design system applies
* frontend build tickets reference selected visual style references or explicitly record why no visual reference applies
* frontend build tickets preserve page, component, route, action, state, interactive element, validation, accessibility, responsive, visual, visual reference, and design system requirements from Stage 4
* frontend build tickets preserve layout pattern requirements, including selected pattern, rationale, rejected alternatives, source refs, and desktop/tablet/mobile transformations
* frontend build tickets reference applicable interaction contracts and stable `UI-ELEMENT-`, `ROUTE-`, and `ACTION-` IDs
* frontend build tickets preserve route types, action outcomes, confirmation, permission-denied, recovery, design-system component mapping, mobile behavior, and accessibility behavior where applicable
* agent assignment plan scans available agents before assignment
* agent assignment plan assigns every MVP ticket to the most suitable available agent that can use the ticket-required skills, or records why it requires manual ownership
* every assigned agent's allowed scopes cover every file scope required by its assigned tickets
* generated agents are written under `.opencode/agents/`
* generated agents include valid subagent frontmatter and prompt body based on ticket-required skills
* generated agent permissions match the assigned role and risk level
* parallel execution plan separates safe parallel work from serial work
* every batch has dependency-valid `execution_waves`
* release plan exists
* high and critical execution risks have mitigation paths
* critical interactive guidance questions are answered or converted into recorded assumptions
* no execution-blocking Stage 3 or Stage 4 unknowns remain unresolved

Possible completion statuses:

```text
ready_for_stage_6
needs_orchestration_revision
needs_earlier_stage_revision
blocked
```

---

# Validation Checklist

Before completing Stage 5, confirm:

* Stage 5 did not redefine product strategy
* Stage 5 did not redesign architecture or UX
* Stage 5 did not implement code
* every MVP feature appears in the roadmap or deferred work
* every launch-critical workflow has an implementation sequence
* every major engineering dependency is mapped
* testing strategy includes validation checkpoints
* build tickets exist for every MVP implementation slice
* build tickets include primary skill, recommended skill chain, agent-required skills, skill usage instructions, acceptance criteria, and validation steps
* frontend build tickets include UI blueprint references, visual spec references, `visual_reference_refs`, design system references, component references, route references, state references, action references, interactive element references, visual requirements, and frontend task hints
* frontend build tickets include UI architecture refs, page archetype, layout pattern refs, component family refs, and template deviation refs when applicable
* frontend build tickets include interaction contract references and preserve stable Stage 4 interaction IDs without replacement
* tickets covering complex pages reference the applicable Mermaid maps in `09-complete-app-blueprint.md`
* frontend build tickets reference `09-complete-app-blueprint.md` when page structure, component structure, route structure, or state structure matters
* agent assignment plan gives each agent clear ownership and handoff inputs
* generated agents have valid markdown definitions in `.opencode/agents/`, safe permission settings, and complete prompt bodies
* parallel execution plan defines batches, merge strategy, and validation gates
* execution-wave dependency validation passed before serialization
* release plan includes readiness gates
* approved Stage 3 `selected_stack` is present and unchanged
* critical interactive guidance questions are answered or converted into recorded assumptions
* Stage 6 handoff is usable for implementation and validation
* `10-stage-5-summary.md` is readable and matches the canonical Stage 5 JSON outputs without adding downstream requirements

---

# A-Grade Workflow Compliance

Stage 5 must consume `stage_contract_profile` and `guidance_policy`.

Stage 5 must consume the approved Stage 3 `selected_stack`.

If the selected stack is missing or ambiguous, Stage 5 must not create build tickets. It must write a revision loop targeting Stage 3 and stop with:

```text
completion_status.status = blocked
completion_status.reason = "missing_or_unresolved_selected_stack"
```

Stage 5 must reference:

```text
System-References/Schemas/stage-5-output.schema.json
```

Build tickets must define `expected_artifacts` when validation, preview, visual QA, deployment proof, or launch readiness evidence will be required later.

Expected artifacts must be carried into:

```text
Build-Plans/Build-status/Artifact-evidence-registry.json
```

For v2 ticket evidence, registry updates must use
`related_stage_output = "Build-Plans/Stage-5/05-build-tickets.json"` and
`related_stage_data_path = "/data/tickets"`.

Before using `ready_for_stage_6`, Stage 5 must provide `schema_validation`, `reference_integrity`, `risk_acceptance_ledger`, and `revision_loops` in the readiness audit or stage state.

Accepted high and critical execution, sequencing, ticketing, or agent risks must be recorded in:

```text
Build-Plans/Build-status/Risk-acceptance-ledger.json
```

Failed readiness checks must become revision-loop actions with owning output, owning skill, required change, and next action.
