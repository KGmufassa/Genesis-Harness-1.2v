---
name: stage-6-implementation-validation
description: Execute and validate Stage 5 handoffs through normalized v2 or legacy-compatible reads.
compatibility: opencode
---

# Command — stage-6-implementation-validation

# Purpose

The `stage-6-implementation-validation` command orchestrates Stage 6.

It transforms:

* Stage 5 implementation sequence
* engineering dependencies
* testing strategy
* build tickets with ticket-required skills
* agent assignment plan
* generated agents
* parallel execution plan
* release plan
* prior stage architecture and UX outputs

into:

* implementation status
* validation results
* regression analysis
* system health assessment
* repair log

This is the Stage 6 command skill. It is not a single implementation subskill.

---

# Scoped Change Input

When `scoped_change` is present, load the approved `CHANGE-` record and its embedded execution packet instead of claiming a normal Stage 5 finalization. Require a valid change schema, matching affected-ID locks, one ticket with normal skill/acceptance/validation fields, preserved-behavior checks, and the routed validation level. Write scoped audits under the change directory and do not overwrite baseline stage audits or `Global-workflow-state.json.current_stage`.

The scoped path does not relax workflow evidence, security, accessibility, visual QA, artifact evidence, regression, or risk-acceptance rules.

---

# Cognitive Boundary

Stage 6 asks:

```text
Can the planned system be built, validated, repaired, and verified?
```

Stage 6 must not:

* redefine product strategy
* redesign architecture
* redesign UX flows
* change release strategy unless execution exposes a blocker
* perform post-launch optimization

Stage 6 may recommend earlier-stage revision only when implementation or validation exposes a blocking flaw in the plan.

---

# Output Directory

All final Stage 6 outputs must be recorded in:

```text
Build-Plans/Stage-6/
```

The command must create this folder if it does not exist.

---

# Shared Implementation State

The shared Stage 6 state must be written to:

```text
Build-Plans/Build-status/Implementation-state.json
```

The command must load this file at the beginning of Stage 6, update it after each implementation/validation skill runs, and preserve it as durable execution state.

```json
{
  "stage": "Stage 6",
  "command": "stage-6-implementation-validation",
  "status": "not_started",
  "scoped_change": {},
  "stage_5_inputs": {},
  "build_tickets": {},
  "agent_assignment_plan": {},
  "parallel_execution_plan": {},
  "active_agents": [],
  "parallel_batches": [
    {
      "batch_id": "",
      "ticket_ids": [],
      "agent_ids": [],
      "status": "pending",
      "completed_at": "",
      "recorded_at": "",
      "file_locks": [],
      "conflicts_detected": [],
      "validation_results": [],
      "blocking_failures": [],
      "downstream_batches_blocked": [],
      "batch_completion_recorded": false
    }
  ],
  "preflight": {},
  "implementation_status": {},
  "validation_results": {},
  "regression_analysis": {},
  "system_health": {},
  "repair_log": [],
  "workflow_evidence": [],
  "dead_control_validation": {},
  "runtime_data_source_validation": {},
  "execution_blockers": [],
  "test_failures": [],
  "open_questions": [],
  "interactive_guidance": {
    "open_questions": [],
    "answered_questions": [],
    "assumptions_made": [],
    "blocked_decisions": [],
    "user_confirmations": [],
    "implementation_confidence_gaps": []
  },
  "stage_7_handoff": {},
  "completion_status": {
    "status": "",
    "reason": "",
    "completed_at": "",
    "recorded_at": "",
    "blocking_items": [],
    "next_actions": [],
    "ready_for": ""
  }
}
```

After each subskill completes, persist the updated state to:

```text
Build-Plans/Build-status/Implementation-state.json
```

---

# Interactive Guidance Rules

The Stage 6 command should behave like a guided implementation and validation controller.

Use this decision rule:

```text
Ask only for execution decisions that materially affect implementation, validation, repair, or system verification.
Infer standard engineering defaults when risk is low and Stage 5 planning supports the inference.
Record assumptions when proceeding without user confirmation.
Block only when a missing decision prevents implementation or trustworthy validation.
```

Pause for user input when:

* implementation cannot proceed because a requirement is ambiguous
* a generated agent is missing, malformed, or lacks required permissions
* a ticket lacks required skills, skill instructions, acceptance criteria, or validation steps
* a parallel batch has unresolved dependency, file ownership, API, schema, architecture, or UX conflicts
* a validation failure has multiple valid repair paths
* a regression affects product behavior or architecture assumptions
* test scope must change to verify correctness
* repair would alter Stage 5 sequencing or Stage 7 readiness

---

# Stage 6 Input Contract

Load Stage 5 outputs from:

```text
Build-Plans/Stage-5/
```

Required Stage 5 files:

```text
00-stage-context.json
01-development-roadmap.json
02-implementation-sequence.json
03-engineering-dependencies.json
04-testing-strategy.json
05-build-tickets.json
06-agent-assignment-plan.json
07-parallel-execution-plan.json
08-release-plan.json
09-stage-manifest.json
```

For normalized format `2.0`, read:

```text
shared context       -> 00-stage-context.json
completion/handoff   -> 09-stage-manifest.json
tickets              -> 05-build-tickets.json#/data/tickets
agents               -> 06-agent-assignment-plan.json#/data/agents
batches               -> 07-parallel-execution-plan.json#/data/batches
other payloads        -> each numbered artifact's /data property
```

Use the manifest index to locate artifacts. If any numbered artifact declares
`format_version = "2.0"`, both context and manifest are mandatory and the
handoff is blocked if either is absent or inconsistent.

For archived self-contained Stage 5 files, use the read-only compatibility
resolver:

```sh
python3 .opencode/Skills/stage-5-development-orchestration/scripts/resolve_stage5.py \
  --artifact build_tickets \
  --with-context
```

The resolver reads normalized and legacy formats but never writes or migrates
files. Future Stage 6 consumers and generated-agent prompts must use it when
format detection is needed.

Minimum viable input set:

```text
02-implementation-sequence.json
03-engineering-dependencies.json
04-testing-strategy.json
05-build-tickets.json
06-agent-assignment-plan.json
07-parallel-execution-plan.json
```

For v2, the minimum viable set additionally requires
`00-stage-context.json` and `09-stage-manifest.json`.

If the minimum viable input set is missing, stop and set:

```text
completion_status.status = "blocked"
completion_status.reason = "missing_implementation_inputs"
```

---

# Stage 5 Handoff Requirements

Stage 6 must consume Stage 5 as an execution handoff, not as general planning notes.

Each build ticket must include:

```text
primary_skill
recommended_skills
agent_required_skills
agent_skill_instructions
acceptance_criteria
validation_steps
completion_definition
workflow_smoke_tests
risk_level
completion_status
ui_blueprint_refs
ui_architecture_refs
page_archetype
layout_pattern_refs
component_family_refs
template_deviation_refs
ui_components_markdown_refs
interaction_contract_refs
visual_spec_refs
visual_reference_refs
design_system_refs
page_refs
component_refs
route_refs
state_refs
action_refs
interactive_element_refs
complete_app_blueprint_refs
interaction_requirements
frontend_task_hint
visual_requirements
responsive_requirements
layout_requirements
component_family_requirements
visual_acceptance_criteria_refs
preview_required
visual_qa_required
design_system_compliance_required
expected_artifacts
```

For launch-critical workflow tickets, Stage 6 must treat `completion_definition`
and `workflow_smoke_tests` as execution requirements. Contract files, API routes,
static UI, fixture data, or a successful build do not satisfy workflow
completion unless the declared user outcome is exercised end to end.

Use explicit workflow evidence statuses. Do not use vague labels such as
`runtime_enabled`, `implemented`, `mostly_done`, or `ready` unless the record
also states the exact evidence level (`contract_only`, `api_exists_not_wired`,
`ui_wired_not_validated`, `runtime_persistence_verified`, `local_e2e_passed`, or
`staging_e2e_passed`).

Frontend tickets that include `ui_blueprint_refs` must preserve the referenced UI blueprint requirements from:

```text
Build-Plans/Stage-4/07-ui-blueprint-specification.json
```

Stage 6 must validate referenced UI blueprint requirements for page structure, layout type, UI architecture template context, page archetype, layout pattern decision, component-family decisions, template deviations, sections, components, shared components, routes, actions, states, data requirements, validation requirements, accessibility requirements, responsive requirements, visual requirements, visual reference requirements, visual acceptance criteria, and design system compliance.

For referenced layout pattern decisions, Stage 6 must confirm the implemented UI preserves the selected pattern, rationale, rejected plausible alternatives, source refs, and responsive transformation. `data-table` pages must preserve sorting, filtering, loading, empty, no-results, error, mobile transformation, and bulk-selection behavior where applicable. Comparison-heavy pages must not be implemented as `card-grid` or another weaker comparison pattern without an approved deviation.

Stage 6 must also validate each referenced page interaction contract and preserve stable `UI-ELEMENT-`, `ROUTE-`, and `ACTION-` IDs. Confirm element existence, label or accessible name, behavior, route type and target, action outcomes, confirmation, permission-denied behavior, recovery behavior, responsive behavior, accessibility behavior, and design-system component mapping where applicable.

Record intentional differences only as approved deviations with the affected stable IDs, rationale, approval evidence, and replacement behavior. Treat dropped, renamed, rerouted, or behavior-changed interactions without approval as validation failures.

For frontend tickets that require preview or visual QA, Stage 6 must record:

```json
{
  "preview_url": "",
  "visual_qa_results": [],
  "responsive_validation_results": [],
  "visual_reference_compliance": {},
  "design_system_compliance": {},
  "visual_drift_status": "visual_match | minor_visual_drift | major_visual_drift | requires_user_review",
  "visual_drift_source": "ui_blueprint_drift | visual_spec_drift | visual_reference_drift | design_system_drift | implementation_only_drift"
}
```

For any ticket with `expected_artifacts`, Stage 6 must record matching artifact evidence updates or a blocker explaining why the artifact could not be produced.

For visible launch-critical buttons, forms, links, menu items, and primary
actions, Stage 6 must record dead-control validation. Each control must be wired
to a working route, API, client action, or state transition; explicitly disabled
with a visible or accessible reason; deferred with approval; or blocked.

Launch-critical runtime pages may use fixtures for preview only. Before Stage 6
can use `ready_for_stage_7`, runtime pages must fetch from the database, API,
queue, storage, worker, or service layer needed by the workflow, or record an
approved deferral or accepted launch risk.

Each agent assignment must include:

```text
agent_id
assigned_tickets
ticket_required_skills
ticket_skill_instructions
allowed_file_scopes
restricted_file_scopes
validation_requirements
```

Generated agents must exist in:

```text
.opencode/agents/
```

Generated agent files must include:

* valid subagent frontmatter
* no agent-specific `model` override
* safe permission settings for the assigned role
* a prompt body with assigned tickets, required skills, skill usage order, file scopes, handoff inputs, validation requirements, rules, and reporting requirements

The parallel execution plan must include:

```text
parallel_batches
serial_batches
conflict_controls
workspace_plan
merge_plan
batch_validation_gates
execution_waves
```

Execute tickets within a batch by `execution_waves`; never run a dependent
ticket in the same wave as or before its prerequisite.

Stage 6 must not execute a ticket until:

* the ticket has required skill instructions
* the ticket is assigned to an agent or explicitly marked for manual execution
* the agent can use the ticket-required skills
* file scopes are clear
* validation requirements are clear
* parallel execution conflicts are resolved or the ticket is placed in a serial batch

---

# Orchestrated Skills

Run Stage 6 skills in this order:

```text
1. implementation-execution
2. validation-execution
3. regression-analysis
4. repair-workflow
5. system-health-synthesis
```

---

# Execution Sequence

## 1. Load Stage 5 Handoff

Load and normalize:

```text
build_tickets
agent_assignment_plan
parallel_execution_plan
testing_strategy
release_plan
```

Do not modify Stage 5 outputs during Stage 6.

## 2. Initialize Shared Implementation State

Create or load:

```text
Build-Plans/Build-status/Implementation-state.json
```

Initialize missing fields using the shared implementation state schema.

## 3. Run `implementation-execution`

Required shared state updates:

```text
implementation_status
execution_blockers
active_agents
parallel_batches
interactive_guidance
```

## 4. Run `validation-execution`

Required shared state updates:

```text
validation_results
test_failures
system_health
interactive_guidance
```

## 5. Run `regression-analysis`

Required shared state updates:

```text
regression_analysis
system_health
execution_blockers
interactive_guidance
```

## 6. Run `repair-workflow`

Required shared state updates:

```text
repair_log
validation_results
system_health
interactive_guidance
```

## 7. Run `system-health-synthesis`

Required shared state updates:

```text
implementation_status
validation_results
regression_analysis
system_health
repair_log
stage_7_handoff
completion_status
interactive_guidance
```

---

# Final Stage 6 Outputs

Generate:

```text
Build-Plans/Stage-6/01-implementation-status.json
Build-Plans/Stage-6/02-validation-results.json
Build-Plans/Stage-6/03-regression-analysis.json
Build-Plans/Stage-6/04-system-health.json
Build-Plans/Stage-6/05-repair-log.json
Build-Plans/Stage-6/06-stage-6-summary.md
```

`06-stage-6-summary.md` is a local human-readable review artifact for every Stage 6 finalization attempt, including ready, repair, revalidation, and blocked outcomes. It must summarize actions taken, implementation status, validation results, live linked/routed page evidence, regression findings, repairs, system health, blockers, known risks, next actions, Stage 7 handoff readiness, and a clear user assessment. It must not contain canonical data that is absent from the JSON outputs.

Do not add `06-stage-6-summary.md` to `stage_7_handoff`, required Stage 7 inputs, or downstream readiness requirements. Stage 7 must continue to consume the Stage 6 JSON outputs.

Each output must include references to relevant:

* Stage 5 ticket IDs
* implementation slice IDs
* agent IDs
* parallel batch IDs
* required skills used
* validation gates
* unresolved blockers

---

# Completion Gate

Before Stage 6 may use `ready_for_stage_7`, run `global-stage-readiness-audit`.

The audit must write:

```text
Build-Plans/Build-status/Stage-6-readiness-audit.json
```

The audit must pass according to:

```text
System-References/Docs/Global-Stage-Workflow-Contract.md
```

If the audit does not pass, do not use `ready_for_stage_7`.

Stage 6 may complete only when:

* all assigned Stage 5 build tickets are implemented, blocked with reason, deferred with approval, or explicitly marked not applicable
* every executed ticket followed its `agent_required_skills` and `agent_skill_instructions`
* every executed frontend ticket with UI blueprint references was validated against the referenced UI blueprint requirements
* every executed frontend ticket with UI architecture, layout pattern, component family, or template deviation references was validated against those referenced Stage 4 requirements
* every executed frontend ticket with interaction contract references was validated against each referenced `UI-ELEMENT-`, `ROUTE-`, and `ACTION-` requirement
* every executed frontend ticket with visual spec references was validated against the referenced visual requirements and visual acceptance criteria
* every executed frontend ticket with `visual_reference_refs` was validated against the selected visual style references as converted through the design system
* every executed frontend ticket with design system references was validated against the referenced design system foundation
* every frontend ticket requiring preview recorded a preview URL or a blocker
* every frontend ticket requiring visual QA recorded visual QA results, responsive validation results, and visual drift status
* every launch-critical workflow has workflow evidence tied to Stage 5 smoke tests
* every launch-critical workflow is `local_e2e_passed`, `staging_e2e_passed`, `deferred_with_approval`, or blocked with a reason
* every visible launch-critical control is wired, explicitly disabled with a reason, approved as deferred, or blocked
* every launch-critical runtime page uses live database/API/queue/storage/service data instead of fixtures, unless explicitly deferred or accepted as known risk
* every generated or assigned agent reported execution status
* every parallel batch has validation results
* all required validation gates have pass/fail status
* regressions are analyzed and assigned severity
* high and critical defects have repairs, blockers, or escalation paths
* repair work has been revalidated
* system health is synthesized from implementation, validation, regression, and repair results
* local human-readable assessment summary exists at `Build-Plans/Stage-6/06-stage-6-summary.md`
* the summary matches canonical Stage 6 JSON outputs and identifies whether the stage is ready, needs repair/revalidation, or is blocked
* Stage 7 handoff contains unresolved operational, deployment, monitoring, analytics, and support needs

Stage 6 is `ready_for_stage_7` only when:

* no critical implementation blockers remain
* no unresolved critical validation failures remain
* no unresolved critical regressions remain
* all launch-critical tickets are implemented and validated
* all launch-critical user workflows have end-to-end outcome evidence or explicit approved deferral/risk acceptance
* no launch-critical visible control is inert, misleading, or fixture-only
* all launch-critical frontend tickets preserve referenced UI blueprint page, component, route, action, state, interactive element (element_type, label, route_target, behavior), validation, accessibility, responsive, visual, visual reference, and design system requirements
* all launch-critical frontend tickets preserve referenced page archetype, layout pattern decision, component-family decisions, template deviations, and responsive transformations
* all launch-critical frontend tickets preserve stable interaction IDs, route types, action outcomes, confirmations, permission-denied behavior, recovery behavior, mobile behavior, accessibility behavior, and design-system component mappings
* every dropped, renamed, rerouted, or behavior-changed interaction has an approved deviation record
* all launch-critical frontend tickets requiring preview have a recorded preview URL or accepted blocker
* all launch-critical frontend tickets have no `major_visual_drift` unless explicitly accepted as known release risk
* all high-risk repairs are verified or explicitly accepted as known risk

Possible completion statuses:

```text
ready_for_stage_7
needs_repair
needs_revalidation
blocked
```

## Global Workflow State Update

After the readiness audit passes and before using `ready_for_stage_7`, update:

```text
Build-Plans/Build-status/Global-workflow-state.json
```

Record:

* `stages.stage_6.status` — the Stage 6 completion status
* `stages.stage_6.ready_for_next_stage` — true when audit passed and stage is ready
* `stages.stage_6.audit_file` — path to the written readiness audit
* `current_stage` — set to `stage_7` when ready
* `last_audit` — timestamp of completion
* `blocking_gaps` and `revision_loops` — from the audit result, if any
* `next_recommended_action` — `proceed_to_stage_7` or repair instruction

---

# Validation Checklist

Before completing Stage 6, confirm:

* Stage 6 did not redefine product strategy
* Stage 6 did not redesign architecture or UX
* Stage 6 did not silently change release strategy
* every Stage 5 ticket has execution status
* every assigned agent has execution status
* every parallel batch has validation status
* validation results map to ticket acceptance criteria
* workflow evidence maps to Stage 5 workflow smoke tests and expected user outcomes
* build success is recorded separately from workflow success
* dead-control validation has no unresolved launch-critical failures
* fixture-to-live validation has no unresolved launch-critical runtime fixture dependencies
* frontend validation results map to referenced UI blueprint IDs when present
* frontend validation results map to interaction contract, `UI-ELEMENT-`, `ROUTE-`, and `ACTION-` IDs when present
* frontend validation results map to referenced visual spec IDs when present
* frontend validation results map to referenced visual style references when present
* frontend validation results map to referenced design system IDs when present
* visual QA, responsive validation, visual reference compliance, design system compliance, visual drift status, and visual drift source are recorded for frontend tickets when required
* interaction conformance results and approved deviations are recorded for frontend tickets with interaction references
* regression analysis maps failures back to affected tickets, agents, batches, workflows, and features
* repair log includes verification results
* Stage 7 handoff is usable for launch and operationalization
* `06-stage-6-summary.md` is readable and matches the canonical Stage 6 JSON outputs without adding downstream requirements

---

# A-Grade Workflow Compliance

Stage 6 must consume `stage_contract_profile` and `guidance_policy`.

Stage 6 must reference:

```text
System-References/Schemas/stage-6-output.schema.json
```

Stage 6 must record implementation, validation, repair, regression, workflow outcome, dead-control, runtime data source, preview, visual QA, and build evidence in:

```text
Build-Plans/Build-status/Artifact-evidence-registry.json
```

Before using `ready_for_stage_7`, Stage 6 must provide `schema_validation`, `reference_integrity`, `risk_acceptance_ledger`, and `revision_loops` in the readiness audit or stage state.

Accepted high and critical implementation, validation, regression, repair, or visual QA risks must be recorded in:

```text
Build-Plans/Build-status/Risk-acceptance-ledger.json
```

Failed readiness checks must become revision-loop actions with owning output, owning skill, required change, and next action.
