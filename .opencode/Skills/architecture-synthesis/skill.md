---
name: architecture-synthesis
description: The architecture-synthesis skill combines all Stage 3 architecture intelligence into final architecture outputs.
compatibility: opencode
---

# Skill — architecture-synthesis

# Purpose

The `architecture-synthesis` skill combines all Stage 3 architecture intelligence into final architecture outputs.

It produces:

* coherent system topology
* service architecture
* data architecture
* API architecture
* integration architecture
* selected concrete implementation stack
* security foundations
* infrastructure model
* scalability framework
* handoff guidance for Stage 4 and Stage 5

This skill is the final architecture synthesis and handoff engine for Stage 3.

---

# Inputs

```json
{
  "system_topology": {},
  "service_architecture": {},
  "data_architecture": {},
  "api_architecture": {},
  "integration_architecture": {},
    "selected_stack": {},
    "stack_evaluation": {},
    "component_rationales": [],
  "security_foundations": {},
  "infrastructure_model": {},
  "scalability_framework": {},
  "existing_state": {}
}
```

Read and update shared architecture state from:

```text
Build-Plans/Build-status/Architecture-state.json
```

---

# Core Responsibilities

## Architecture Coherence

Validate:

* service boundaries align with capabilities
* data ownership is clear
* APIs support workflows
* integrations are mapped to dependencies
* infrastructure supports technical feasibility findings
* security controls map to risk validation
* scalability framework supports MVP and future growth

## Tradeoff Documentation

Record:

* major architecture decisions
* selected concrete stack
* alternatives considered
* rejected stack alternatives with rationale
* accepted risks
* deferred architecture concerns
* Stage 4 handoff implications
* Stage 5 execution implications

## Stack Evaluation And Decision Brief Content

Before writing `Build-Plans/Stage-3/00-stage-decision-brief.md`, evaluate the concrete selected stack against the app described by Stage 1 and the evidence and constraints carried from Stage 2.

Persist the result under `selected_stack.stack_evaluation` with:

* `overall_grade` and `overall_score` (0-100)
* `strength_grade` and `strength_score`
* `compatibility_grade` and `compatibility_score`
* `evaluated_against`
* `strengths`
* `weaknesses`
* `decision` (`proceed`, `revise`, or `blocked`)

Use `A` for 90-100, `B` for 80-89, `C` for 70-79, `D` for 60-69, and `F` below 60. Scores below 70 require a revision or blocking decision and a mitigation path.

Persist `selected_stack.component_rationales` with one object per selected stack element. Each object must contain `component`, `choice`, `why_chosen`, `app_fit`, and `tradeoffs`. Rationales must explain the choice in relation to this app’s workflows, capabilities, risks, constraints, and Stage 2 evidence; generic popularity claims are insufficient.

The generated decision brief must render these persisted fields in a `Stack evaluation` section and a per-component rationale table. The brief is incomplete if either section is missing, if a stack element lacks a rationale, or if the scores are unsupported by named app/evidence inputs.

## Completion Determination

Determine whether Stage 3 is:

```text
ready_for_stage_4
needs_architecture_revision
needs_stage_2_revalidation
blocked
```

Also determine whether `Build-Plans/Stage-3/00-stage-decision-brief.md` exists and `stage_decision_brief.approval_status` is `approved`.

Also determine whether `selected_stack` is complete and contains no unresolved alternatives.

---

# Concrete Stack Enforcement

Before finalizing Stage 3, verify that `selected_stack` includes exactly one concrete choice for:

```text
frontend framework
frontend language
styling approach
backend framework
backend runtime
API style
primary database
ORM or query layer
authentication provider or strategy
hosting and deployment model
testing stack
package manager
AI providers or none_for_mvp
storage provider or none_for_mvp
```

Reject stack outputs that leave implementation choices unresolved with terms such as:

```text
or
TBD
to decide later
optional
depends
choose during implementation
```

If multiple options remain viable, choose the best-fit option based on Stage 2 feasibility, product complexity, security, scalability, cost, operational burden, and available skill coverage.

Record non-selected options in `selected_stack.rejected_alternatives` with rationale.

If `selected_stack` is incomplete or unresolved, do not use `ready_for_stage_4`; set `completion_status.status` to `needs_architecture_revision` and return the missing stack decisions.

---

# Interactive Guidance Responsibilities

This skill should not finalize Stage 3 if architecture-blocking questions remain unresolved.

Before writing final outputs, inspect:

```text
interactive_guidance.open_questions
interactive_guidance.blocked_decisions
interactive_guidance.architecture_confidence_gaps
architecture_risks
open_questions
tradeoffs
```

Classify unresolved guidance items as:

```text
safe_to_assume
needs_user_confirmation
blocks_stage_3_completion
```

Ask the minimum number of final questions needed to complete Stage 3.

Do not ask broad technical preference questions at this stage. Only ask questions tied directly to:

* missing final architecture output fields
* unresolved service boundary decisions
* unresolved data ownership decisions
* unresolved security decisions
* unresolved infrastructure or integration decisions
* incomplete or unresolved selected stack decisions
* architecture risks that block Stage 4 or Stage 5 handoff
* unapproved Stage 3 architecture and tech stack decision brief

If proceeding with assumptions, record them in:

```text
interactive_guidance.assumptions_made
```

If Stage 3 cannot complete, set `completion_status` to one of:

```text
needs_architecture_revision
needs_stage_2_revalidation
blocked
```

and return the specific questions or decisions required.

---

# Outputs

```json
{
  "architecture_outputs": {},
  "selected_stack": {},
  "architecture_decisions": [],
  "architecture_risks": [],
  "tradeoffs": [],
  "stage_4_handoff": {},
  "stage_5_handoff": {},
  "completion_status": {}
}
```

---

# Final Stage 3 Outputs

Write or update:

```text
Build-Plans/Stage-3/01-system-topology.json
Build-Plans/Stage-3/02-service-architecture.json
Build-Plans/Stage-3/03-data-architecture.json
Build-Plans/Stage-3/04-api-architecture.json
Build-Plans/Stage-3/05-integration-architecture.json
Build-Plans/Stage-3/06-security-foundations.json
Build-Plans/Stage-3/07-infrastructure-model.json
Build-Plans/Stage-3/08-scalability-framework.json
```

Each output must include:

* related Stage 1 source files
* related Stage 2 assumption IDs where applicable
* architecture decisions
* risks and constraints
* unresolved questions
* Stage 4 or Stage 5 handoff notes when relevant

---

# Shared State Updates

Update:

```text
architecture_decisions
selected_stack
architecture_risks
tradeoffs
stage_4_handoff
stage_5_handoff
completion_status
interactive_guidance
```

Persist updates to:

```text
Build-Plans/Build-status/Architecture-state.json
```

---

# Completion Gate

Stage 3 may complete only when:

* all eight architecture outputs exist
* system topology is defined
* service boundaries are clear enough for implementation planning
* data ownership is defined
* API surfaces are mapped to workflows
* integrations and infrastructure are defined
* selected concrete stack is complete
* selected stack contains no unresolved alternatives
* stack evaluation includes strength and app-compatibility grades with named evidence
* every selected stack element has a rationale, app fit, and tradeoffs
* stack evaluation decision is `proceed`
* security foundations are present
* scalability framework exists
* high and critical architecture risks have mitigation paths
* critical interactive guidance questions are answered or converted into recorded assumptions
* no architecture-blocking Stage 2 unknowns remain unresolved
* Stage 3 decision brief exists and is approved

---

# Validation Checklist

Before completing Stage 3, confirm:

* Stage 3 did not redefine product strategy
* Stage 3 did not perform UX screen design
* Stage 3 did not write implementation tickets
* every major capability maps to a system or service
* every core workflow is supported by the architecture
* every data entity has an owner
* every external dependency has an integration strategy
* selected stack has exactly one concrete choice for frontend, backend, database, auth, deployment, testing, and package manager
* rejected stack alternatives are recorded with rationale
* stack strength and app compatibility are graded with evidence-backed scores
* every selected stack element has an app-specific rationale and tradeoffs
* security and scalability risks are recorded
* critical interactive guidance questions are answered or converted into recorded assumptions
* Stage 4 handoff is usable for UX architecture
* Stage 5 handoff is usable for development orchestration
* Stage 3 decision brief approval is recorded before Stage 4 or Stage 5 handoff is used

Before using `ready_for_stage_4` or sending Stage 5 architecture handoff, this skill must generate or verify:

```text
Build-Plans/Stage-3/00-stage-decision-brief.md
```

If the decision brief is not approved, return the architecture and tech stack proposal for user review instead of locking Stage 3.

If `selected_stack` is not complete or contains unresolved alternatives, return the concrete stack gaps for revision before producing `ready_for_stage_4` or Stage 5 architecture handoff.
