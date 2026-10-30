---
name: stage-3-system-architecture
description: The stage-3-system-architecture command orchestrates Stage 3.
compatibility: opencode
---

# Command — stage-3-system-architecture

# Purpose

The `stage-3-system-architecture` command orchestrates Stage 3.

It transforms:

* Stage 1 product structures
* Stage 2 validation intelligence
* architecture readiness findings
* validated assumptions
* known risks and constraints

into:

* technical system topology
* service architecture
* data architecture
* API architecture
* integration model
* security foundations
* infrastructure model
* scalability framework

This is the Stage 3 command skill. It is not a single architecture subskill.

---

# Cognitive Boundary

Stage 3 asks:

```text
How should the validated product be technically structured?
```

Stage 3 must not:

* redefine the product concept
* perform market validation
* design detailed user interfaces
* write implementation tickets
* produce production deployment scripts

Stage 3 may recommend product or validation revisions only when architecture analysis exposes a blocking contradiction.

---

# Output Directory

All final Stage 3 outputs must be recorded in:

```text
Build-Plans/Stage-3/
```

The command must create this folder if it does not exist.

---

# Shared Architecture State

The command maintains a shared Stage 3 architecture state object.

The shared architecture state must be written to:

```text
Build-Plans/Build-status/Architecture-state.json
```

The command must load this file at the beginning of Stage 3, update it after each architecture skill runs, and preserve it as the durable architecture state for the build.

```json
{
  "stage": "Stage 3",
  "command": "stage-3-system-architecture",
  "status": "not_started",
  "stage_1_inputs": {},
  "stage_2_inputs": {},
  "preflight": {},
  "architecture_drivers": [],
  "architecture_decisions": [],
  "selected_stack": {
    "frontend": {},
    "backend": {},
    "database": {},
    "storage": {},
    "authentication": {},
    "hosting_and_deployment": {},
    "testing_stack": {},
    "package_manager": "",
    "ai_and_external_services": [],
    "rationale": "",
    "stack_evaluation": {
      "overall_grade": "",
      "overall_score": 0,
      "strength_grade": "",
      "strength_score": 0,
      "compatibility_grade": "",
      "compatibility_score": 0,
      "evaluated_against": [],
      "strengths": [],
      "weaknesses": [],
      "decision": ""
    },
    "component_rationales": [],
    "rejected_alternatives": [],
    "risks": []
  },
  "stack_decision_status": {},
  "rejected_stack_alternatives": [],
  "system_topology": {},
  "service_architecture": {},
  "data_architecture": {},
  "api_architecture": {},
  "integration_architecture": {},
  "security_foundations": {},
  "infrastructure_model": {},
  "scalability_framework": {},
  "architecture_risks": [],
  "tradeoffs": [],
  "open_questions": [],
  "interactive_guidance": {
    "open_questions": [],
    "answered_questions": [],
    "assumptions_made": [],
    "blocked_decisions": [],
    "user_confirmations": [],
    "architecture_confidence_gaps": []
  },
  "stage_4_handoff": {},
  "stage_5_handoff": {},
  "completion_status": {}
}
```

Each subskill reads the current architecture state and writes its updates back into the shared state before the next skill runs.

After each subskill completes, the command must persist the updated shared state to:

```text
Build-Plans/Build-status/Architecture-state.json
```

---

# Interactive Guidance Rules

The Stage 3 command should behave like a guided architecture decision interview.

Use this decision rule:

```text
Ask only for architecture decisions that materially affect system design.
Infer standard technical defaults when risk is low and the product model supports the inference.
Record assumptions when proceeding without user confirmation.
Block only when a missing decision prevents coherent architecture.
```

When asking the user questions:

* ask 1-3 questions at a time
* prioritize architecture-blocking decisions first
* avoid asking questions already answered by Stage 1 or Stage 2 outputs
* explain the architectural consequence of each question
* prefer concrete options over open-ended questions when the tradeoff is known
* update `interactive_guidance.open_questions`
* move answered questions into `interactive_guidance.answered_questions`
* record inferred defaults in `interactive_guidance.assumptions_made`
* record unresolved blockers in `interactive_guidance.blocked_decisions`

The command should continue automatically when a decision has a low-risk default.

The command should pause for user input when:

* data ownership is unclear
* user roles or permissions materially affect service boundaries
* an external integration is required but unspecified
* AI processing requires a major architecture choice
* synchronous vs asynchronous workflow behavior changes the topology
* sensitive data handling is unclear
* scalability expectations materially affect infrastructure choices
* a Stage 2 risk cannot be mitigated through architecture

The command should not ask the user to choose implementation details that can be deferred to Stage 5 unless the decision changes Stage 3 architecture.

---

# Concrete Stack Decision Rules

Stage 3 must select one concrete implementation stack before completion.

The command may compare alternatives, but it must collapse them into a single selected stack before final synthesis.

The selected stack must include concrete choices for:

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

Selection rules:

* choose the best-fit stack using Stage 2 feasibility, product complexity, known risks, skill availability, implementation speed, scalability, security, cost, and operational burden
* record rejected alternatives with rationale
* use `none_for_mvp` for stack areas intentionally excluded from the MVP
* do not leave unresolved choices such as `or`, `TBD`, `to decide later`, `optional`, or `depends`
* if the user rejects the stack, update `stack_decision_status`, revise `selected_stack`, and regenerate affected architecture outputs before completion

## Stack Evaluation And Rationale

Before generating the Stage 3 decision brief, evaluate the selected stack against the actual app being created. Do not grade the stack in isolation or use popularity as a substitute for fit.

Record `selected_stack.stack_evaluation` with:

* `overall_grade` and `overall_score` on a 0-100 scale
* `strength_grade` and `strength_score`, covering implementation maturity, maintainability, security, delivery speed, operational burden, and scalability
* `compatibility_grade` and `compatibility_score`, covering the Stage 1 workflows/capabilities and Stage 2 feasibility findings, constraints, risks, and expected usage pattern
* `evaluated_against`, naming the concrete product capabilities, workflows, constraints, and evidence used
* `strengths` and `weaknesses`, including material tradeoffs
* `decision`, which must be `proceed`, `revise`, or `blocked`

Use letter grades consistently: `A` = 90-100, `B` = 80-89, `C` = 70-79, `D` = 60-69, and `F` = below 60. A score below 70 in either strength or compatibility requires `decision = revise` or `blocked` and a recorded mitigation or revision path.

Record `selected_stack.component_rationales` as one entry for every selected stack element, including frontend framework/language/styling, backend framework/runtime/API, database/query layer, authentication, storage, hosting/deployment, testing, package manager, and AI/external services. Each entry must include:

* `component`
* `choice`
* `why_chosen`
* `app_fit`
* `tradeoffs`

The explanation must be specific to this app and must cite relevant Stage 1 or Stage 2 IDs/files where available. Do not use generic claims such as “popular” or “industry standard” without connecting them to an app requirement.

Stage 3 must block completion when `selected_stack` is missing, incomplete, or contains unresolved alternatives.

---

# Stage 3 Input Contract

Load Stage 1 outputs from:

```text
Build-Plans/Stage-1/
```

Load Stage 2 outputs from:

```text
Build-Plans/Stage-2/
```

Required Stage 1 files:

```text
01-product-foundation.json
02-user-system-map.json
03-workflow-architecture.json
04-product-capabilities.json
05-feature-structure.json
06-product-boundaries.json
07-dependency-map.json
08-mvp-operational-model.json
09-risk-and-constraints.json
10-success-framework.json
```

Required Stage 2 files:

```text
01-market-analysis.json
02-competitive-landscape.json
03-technical-feasibility.json
04-business-viability.json
05-risk-validation.json
06-strategic-positioning.json
```

Minimum viable input set:

```text
Stage 1:
01-product-foundation.json
03-workflow-architecture.json
04-product-capabilities.json
05-feature-structure.json
07-dependency-map.json
08-mvp-operational-model.json
09-risk-and-constraints.json

Stage 2:
03-technical-feasibility.json
05-risk-validation.json
06-strategic-positioning.json
```

If the minimum viable input set is missing, stop and set:

```text
completion_status.status = "blocked"
completion_status.reason = "missing_architecture_inputs"
```

If Stage 2 completion status is not `ready_for_stage_3`, continue only if the unresolved issues are not architecture-blocking. Record all carry-forward risks in `architecture_risks`.

---

# Preflight Validation

Before architecture design, validate:

* Stage 1 outputs exist and are readable
* Stage 2 outputs exist and are readable
* architecture readiness status is acceptable
* critical unknowns from Stage 2 are resolved or mitigated
* validated assumptions are available
* high and critical risks have mitigation paths
* MVP scope is clear enough to architecture

Record preflight results in:

```text
preflight
architecture_risks
open_questions
interactive_guidance
completion_status
```

---

# Orchestrated Skills

Run Stage 3 skills in this order:

```text
1. system-topology-design
2. service-boundary-architecture
3. data-and-api-architecture
4. integration-and-infrastructure-architecture
5. security-and-scalability-architecture
6. architecture-synthesis
```

---

# Execution Sequence

## 1. Load Stage 1 And Stage 2 Outputs

Load Stage 1 outputs from `Build-Plans/Stage-1/`.

Load Stage 2 outputs from `Build-Plans/Stage-2/`.

Normalize them into:

```text
stage_1_inputs
stage_2_inputs
```

Do not modify Stage 1 or Stage 2 outputs during Stage 3.

---

## 2. Initialize Shared Architecture State

Create or load:

```text
Build-Plans/Build-status/Architecture-state.json
```

Initialize missing fields using the shared architecture state schema.

---

## 3. Run `system-topology-design`

Purpose:

* define primary systems and subsystems
* extract architecture drivers
* map system, trust, data flow, ownership, and external dependency boundaries

Required shared state updates:

```text
system_topology
architecture_drivers
architecture_risks
open_questions
interactive_guidance
```

---

## 4. Run `service-boundary-architecture`

Purpose:

* define service responsibilities
* map service ownership domains
* define communication patterns
* validate service boundaries against capabilities and MVP scope

Required shared state updates:

```text
service_architecture
architecture_decisions
architecture_risks
tradeoffs
interactive_guidance
```

---

## 5. Run `data-and-api-architecture`

Purpose:

* define core data entities
* define data ownership
* design API boundaries and operations
* detect data risks and API exposure risks

Required shared state updates:

```text
data_architecture
api_architecture
architecture_decisions
architecture_risks
open_questions
interactive_guidance
```

---

## 6. Run `integration-and-infrastructure-architecture`

Purpose:

* define external integrations
* define hosting and runtime infrastructure
* define queue, worker, storage, and observability foundations
* detect infrastructure and integration risks

Required shared state updates:

```text
integration_architecture
infrastructure_model
architecture_decisions
architecture_risks
tradeoffs
interactive_guidance
```

---

## 7. Run `security-and-scalability-architecture`

Purpose:

* define authentication and authorization foundations
* define sensitive data and trust boundary controls
* define scalability and resilience strategy
* detect security and scalability risks

Required shared state updates:

```text
security_foundations
scalability_framework
architecture_risks
architecture_decisions
tradeoffs
interactive_guidance
```

---

## 8. Run `architecture-synthesis`

Purpose:

* reconcile all Stage 3 architecture outputs
* validate architecture coherence
* document tradeoffs and decisions
* produce Stage 4 and Stage 5 handoffs
* determine completion status

Required shared state updates:

```text
architecture_decisions
architecture_risks
tradeoffs
stage_4_handoff
stage_5_handoff
completion_status
interactive_guidance
```

---

# Final Stage 3 Outputs

Generate:

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

# Stage Decision Brief

Before final synthesis, `ready_for_stage_4`, or Stage 5 architecture handoff, generate:

```text
Build-Plans/Stage-3/00-stage-decision-brief.md
```

The brief confirms the selected concrete architecture stack before UX/UI planning and build orchestration.

The brief must present one selected concrete stack, not multiple unresolved options.

In addition to the shared decision brief fields, the Stage 3 brief must include:

* a `Stack evaluation` section showing overall, strength, and compatibility grades and scores
* the evidence and app characteristics used for the evaluation
* a `Why each stack element was chosen` table containing every `component_rationales` entry
* material weaknesses, tradeoffs, and mitigations

The Markdown brief must be generated from `selected_stack.stack_evaluation` and `selected_stack.component_rationales`; do not invent a separate explanation that can drift from the shared architecture state.

Use this minimum brief structure:

```markdown
# Stage 3 Decision Brief — System Architecture

## Recommended architecture and stack
<!-- one concrete stack and the app capabilities it supports -->

## Stack evaluation
| Measure | Grade | Score |
| --- | --- | --- |
| Overall | ... | .../100 |
| Strength | ... | .../100 |
| App compatibility | ... | .../100 |

### Evaluation basis
<!-- evaluated_against, strengths, weaknesses, and mitigations -->

## Why each stack element was chosen
| Component | Choice | Why chosen | App fit | Tradeoffs |
| --- | --- | --- | --- | --- |
<!-- one row per component_rationales entry -->

## Alternatives and downstream impact
<!-- rejected alternatives, Stage 4/5 implications, and risks -->

## Decision required
Do you approve this selected concrete stack for the build?
```

Do not mark the brief complete when the evaluation table or any required component row is absent.

Ask:

```text
Do you approve this selected concrete stack for the build?
```

Allowed user decisions:

```text
Approve tech stack
Change frontend stack
Change backend stack
Change database/auth/deployment
Choose simpler architecture
Choose more scalable architecture
```

Record the brief in shared architecture state as `stage_decision_brief`.

Do not use `ready_for_stage_4` or send Stage 5 architecture handoff unless:

```text
selected_stack is complete
selected_stack contains no unresolved alternatives
stage_decision_brief.approval_status = approved
```

---

# Completion Gate

Before Stage 3 may use `ready_for_stage_4`, run `global-stage-readiness-audit`.

The audit must write:

```text
Build-Plans/Build-status/Stage-3-readiness-audit.json
```

The audit must pass according to:

```text
System-References/Docs/Global-Stage-Workflow-Contract.md
```

If the audit does not pass, do not use `ready_for_stage_4`.

Stage 3 may complete only when:

* all eight architecture outputs exist
* system topology is defined
* service boundaries are clear enough for implementation planning
* data ownership is defined
* API surfaces are mapped to workflows
* integrations and infrastructure are defined
* selected concrete stack is complete and approved
* stack evaluation is complete, evidence-backed, and has `decision = proceed`
* security foundations are present
* scalability framework exists
* high and critical architecture risks have mitigation paths
* critical interactive guidance questions are answered or converted into recorded assumptions
* no architecture-blocking Stage 2 unknowns remain unresolved
* Stage 3 decision brief exists and is approved

Possible completion statuses:

```text
ready_for_stage_4
needs_architecture_revision
needs_stage_2_revalidation
blocked
```

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

---

# A-Grade Workflow Compliance

Stage 3 must consume `stage_contract_profile` and `guidance_policy`.

Stage 3 must reference:

```text
System-References/Schemas/stage-3-output.schema.json
```

Architecture decisions should reference Stage 2 evidence quality and create artifacts when architecture proof, diagrams, or decision records are produced.

Those artifacts should be recorded or referenced in:

```text
Build-Plans/Build-status/Artifact-evidence-registry.json
```

Before using `ready_for_stage_4`, Stage 3 must provide `schema_validation`, `reference_integrity`, `risk_acceptance_ledger`, and `revision_loops` in the readiness audit or stage state.

Accepted high and critical architecture risks must be recorded in:

```text
Build-Plans/Build-status/Risk-acceptance-ledger.json
```

Failed readiness checks must become revision-loop actions with owning output, owning skill, required change, and next action.
