# Plan: Lean Change Layer for Scoped Product Evolution

## Approval Status

```text
Status: approved and minimally implemented
Implementation authorized: yes, by user request on 2026-08-17
Required next action: exercise the router on a supervised scoped change
```

This document defines the full scope for adding features, pages, backend revisions, repairs, and post-launch improvements without restarting or bypassing the Genesis eight-stage workflow. The initial implementation intentionally covers deterministic routing, compact records, ID locks, schema validation, and completion auditing; deferred enhancements remain governed by the non-goals below.

---

## Objective

Add a lightweight change-control capability that:

- distinguishes active-stage refinement from changes to approved scope
- routes an intentional change to the earliest materially affected stage
- runs only the stages and validations required by the change
- preserves all unaffected canonical content and stable traceability IDs
- isolates provisional work from approved work with Git branches or worktrees
- prevents local changes from silently expanding into cross-cutting work
- preserves the existing decision, readiness, evidence, risk, and handoff contracts
- avoids custom baseline storage, semantic merge engines, and unnecessary artifact duplication

The layer must make the least expensive safe path the default while failing closed when impact, ownership, approval, or validation evidence is uncertain.

---

## Proposed Name and Position

Use a pre-stage orchestration capability named `lean-change-layer`, with a router skill named `change-intake-router`.

The layer is not Stage 9. It sits above the existing workflow and selectively invokes existing stages.

```text
User request or Stage 8 feedback
  -> change intake and preflight
    -> refinement or change-cycle decision
      -> classification and scoped routing
        -> affected stages in normal ownership order
          -> targeted validation and readiness
            -> Git review and merge
```

The existing Stage 1 through Stage 8 cognitive boundaries remain authoritative.

---

## Core Design Decisions

1. Use the current canonical stage outputs as the single current-product view.
1. Use Git commits for historical baselines, branches or worktrees for isolation, diffs for review, and Git reversion for recovery.
1. Create one authoritative compact change record per intentional change cycle; keep the shared change ledger as an index and affected-ID lock table only.
1. Do not create per-stage delta files; the Git diff is the implementation delta.
1. Do not regenerate unrelated stage outputs.
1. Use scoped Stage 5 ticket generation and an embedded change execution packet instead of a full Stage 5 finalization for trivial and bounded changes.
1. Validate in proportion to risk and blast radius.
1. Permit only one active writer for a stable traceability ID.
1. Keep revision loops for discovered defects, contradictions, readiness failures, and routed rework. Do not use revision loops as the primary representation of intentional scope additions.
1. Require explicit reasons for every skipped or conditionally deferred stage, stored in the single change record.
1. Keep change-cycle stage state separate from the baseline `Global-workflow-state.json` stage statuses and `current_stage`.
1. Treat files modified in a change worktree as candidate outputs until the change is merged and post-merge verification succeeds.

---

## Initiation Rules

### Natural-Language Entry

The layer may initiate from ordinary requests such as:

```text
Add threaded comments to project records.
Redesign the project list page without changing its behavior.
Change the existing export API to support date ranges.
Emergency change: disable the endpoint exposing private records.
```

Explicit forms may also be supported:

```text
Start a change: <request>
Start a trivial change: <request>
Start a bounded change: <request>
Start a feature change: <request>
Start an emergency change: <request>
```

### Refinement Versus Change Cycle

Before creating a `CHANGE-` record, determine whether the owning output is already approved.

```text
Owning stage still active and unapproved
  -> treat request as an ordinary current-stage revision

Owning output already approved or downstream work has started
  -> initiate a controlled change cycle
```

This prevents change-management overhead during normal initial product planning.

### Stage 8 Entry

Stage 8 feedback with `creates_new_stage_cycle = true` may seed a transient change proposal. Keep it as a Stage 8 feedback-route candidate until the user grants proportional approval. Stage 8 evidence does not automatically authorize product modification or create a durable `CHANGE-` record.

---

## Preflight

The router must perform a read-only, fail-fast preflight before it creates or modifies change artifacts. After the user approves the route, rerun the preflight immediately before recording the base commit or creating an isolated workspace.

Check:

- global workflow state and current stage statuses
- applicable decision-brief approval status
- relevant canonical stage outputs
- active revision loops and blockers
- current Git commit and target branch
- working-tree cleanliness and unrelated modifications
- existing active change records
- affected-ID ownership conflicts
- availability of required upstream artifacts

Do not create a branch or worktree when unrelated uncommitted changes make the base ambiguous. Report the conflict and request direction without modifying or discarding the existing work.

Approved initiation sequence:

```text
read-only intake and preflight
  -> transient route and approval preview
    -> user approval
      -> second preflight against the current target commit
        -> record the product base commit
          -> commit the initial change record, ledger index entry, and ID locks as coordination metadata
            -> create the branch or worktree from that coordination commit
              -> begin scoped execution
```

The coordination commit is the only approved change-cycle metadata written to the target before implementation. It must not modify product, architecture, UX, execution, implementation, or launch artifacts. This makes active locks visible to other routers while keeping candidate product changes isolated.

---

## Change Classes

### Class A — Trivial

Examples:

- copy correction
- spacing, color, or token-aligned styling correction
- documentation correction
- internal refactor with no behavior or contract change
- implementation repair that restores approved behavior

Default route:

```text
change record
  -> scoped Stage 5 ticket generation when implementation work is required
  -> Stage 6 implementation
    -> local validation
      -> completion review
```

Invoke Stage 4 only when approved design intent changes. Use the user request as approval when the active guidance policy permits low-risk inference.

### Class B — Bounded

Examples:

- new page using existing workflows, permissions, and APIs
- page redesign with unchanged product behavior
- new API endpoint within an existing service boundary
- modification to an existing feature
- component addition using the approved design system

Default route:

```text
owning planning stage
  -> scoped Stage 5 ticket generation
    -> Stage 6 implementation and workflow validation
      -> conditional Stage 7 release work
```

### Class C — Cross-Cutting or New Feature

Examples:

- feature absent from the approved product scope
- new user outcome, role, workflow, or permission model
- new external integration
- material data-model or shared-contract change
- feature requiring both backend and page additions

Default route:

```text
Stage 1 scoped amendment
  -> conditional Stage 2 assumption validation
    -> conditional Stage 3 architecture amendment
      -> conditional Stage 4 UX/UI amendment
        -> scoped or full Stage 5 execution planning, based on orchestration complexity
          -> Stage 6 implementation and validation
            -> conditional Stage 7 release work
```

### Class D — Emergency

Examples:

- production outage
- active security vulnerability
- data-loss risk
- broken launch-critical workflow

Default route:

```text
Stage 6 containment and repair
  -> Stage 7 operational validation and release
    -> mandatory retrospective routing to affected earlier stages
```

Emergency status must not become a permanent way to bypass planning or traceability.

---

## Deterministic Entry-Stage Router

Evaluate these questions in order and select the earliest `yes` result:

1. Does the request introduce or change a user outcome, product feature, role, workflow, or product boundary? Route to Stage 1.
1. Does it change a demand, market, business, or behavioral assumption without changing product scope? Route to Stage 2.
1. Does it change services, data, APIs, integrations, security, infrastructure, or scalability? Route to Stage 3.
1. Does it change pages, navigation, behavior, visual design, responsive behavior, state, or accessibility? Route to Stage 4.
1. Does it change tickets, sequencing, agent assignment, testing strategy, or release planning? Route to Stage 5.
1. Otherwise, route implementation or repair to Stage 6.

Stage 7 owns deployment and operational changes. Stage 8 owns evidence-driven evolution findings and routes resulting changes through this layer.

---

## Escalation Triggers

A fast-path change must be widened or reclassified when it introduces any of the following:

- new user role or permission
- new database entity or destructive migration
- breaking API or event-contract change
- shared component or shared service modification
- new external integration
- new launch-critical workflow
- authentication, payment, privacy, or security impact
- navigation architecture change
- analytics contract change
- more than one existing workflow materially affected
- unresolved upstream traceability

Escalation rules:

```text
Class A -> Class B
Class B -> Class C
local validation -> workflow or system validation
```

Material escalation after initial approval must be shown to the user before the layer expands product behavior, architecture, UX direction, release risk, or implementation scope.

---

## Minimal Change Record

Use one durable change object as the authoritative source for the cycle. The final schema may allow additional properties, but the initial required contract should remain compact enough for targeted processing while carrying the references required by approval and completion audits.

```json
{
  "change_id": "CHANGE-014",
  "title": "Add threaded project comments",
  "change_class": "cross_cutting",
  "change_type": "feature_addition",
  "requested_outcome": "Users can discuss individual project records",
  "base_commit": "",
  "target_branch": "",
  "owner": "",
  "affected_ids": [],
  "created_ids": [],
  "modified_ids": [],
  "removed_ids": [],
  "revalidated_ids": [],
  "preserved_behavior": [],
  "risk_level": "medium",
  "risk_refs": [],
  "accepted_risk_refs": [],
  "evidence_refs": [],
  "validation_level": "system",
  "impact_confidence": "high",
  "confidence_reason": "",
  "unresolved_impacts": [],
  "entry_stage": "stage_1",
  "required_stages": [],
  "next_required_stage": "stage_1",
  "stage_dispositions": {},
  "active_stage": "stage_1",
  "stage_attempts": [],
  "stage_results": [],
  "escalations": [],
  "impact_results": [],
  "change_budget": {},
  "compatibility": {},
  "release_control": {},
  "approval": {
    "required_types": ["product"],
    "status": "approved",
    "evidence_refs": [],
    "approved_by": "",
    "approved_at": null
  },
  "execution_packet": {},
  "deferred_items": [],
  "completion_disposition": "",
  "status": "active"
}
```

Allowed initial lifecycle statuses:

```text
active
validating
ready_to_merge
completed
blocked
rejected
cancelled
```

Approval state is separate from operational lifecycle state. `completed` means the candidate changes have been merged into the target branch and post-merge verification confirms that the target contains the approved change and valid canonical outputs. Do not introduce a larger state machine until real usage demonstrates the need.

Allowed initial change types:

```text
feature_addition
bounded_revision
removal
repair
migration
emergency
```

Minimum stage disposition:

```json
{
  "stage": "stage_2",
  "status": "not_required",
  "reason": "No new demand, market, business, or behavioral assumption",
  "evaluated_refs": [],
  "evidence_refs": [],
  "approval_refs": []
}
```

Allowed disposition statuses are `required`, `executed`, `not_required`, `deferred`, and `blocked`.

Minimum durable impact entry:

```json
{
  "object_id": "API-042",
  "disposition": "modify",
  "owner_stage": "stage_3",
  "direct_dependency_refs": [],
  "reason": ""
}
```

---

## Change Budget

Every change receives a class-appropriate expected scope ceiling. A budget measures unexpected expansion beyond the approved route; it must not reject a valid Class C change merely because its expected route spans several stages.

```json
{
  "change_budget": {
    "approved_stage_route": ["stage_1", "stage_3", "stage_4", "stage_5", "stage_6"],
    "maximum_unplanned_stages": 1,
    "maximum_primary_ids": 10,
    "maximum_tickets": 5,
    "expected_risk": "medium"
  }
}
```

Budget defaults:

- Class A: one implementation domain and local validation
- Class B: no more than two planning domains and five tickets unless explicitly approved
- Class C: no total stage-count ceiling; budget affected workflows, primary IDs, tickets, risk, and unplanned stage expansion
- Class D: budget immediate containment separately from mandatory retrospective scope

Exceeding the budget does not automatically block the change. It requires route recalculation, class escalation when available, and user review when the expansion is material.

---

## Preserved Behavior

Every change must record the important behavior that is expected to remain unchanged.

Examples:

```text
Existing project access permissions remain unchanged.
Existing API consumers remain compatible.
Project-list loading and error behavior remain unchanged.
Existing keyboard navigation remains valid.
```

Preserved behavior becomes the minimum targeted regression boundary. This provides explicit regression protection without running every project test for every change.

---

## Impact Analysis

Use a bounded traceability walk rather than constructing a full dependency graph for every request.

Default traversal:

```text
explicitly affected IDs
  -> direct upstream sources
    -> direct downstream consumers
      -> launch-critical workflow containing those IDs
```

Expand beyond direct consumers only when an escalation trigger, unresolved reference, or medium-to-high compatibility risk is detected.

Each affected object should receive one disposition:

```text
create
modify
remove
revalidate
no_change
defer
```

Store durable impact results in the authoritative change record as compact entries containing object ID, disposition, owner stage, direct dependency refs, and reason. Generate exploratory traversal details transiently. Do not create a separate canonical impact database.

---

## Impact Confidence

Record one confidence level:

```text
high
medium
low
```

Rules:

- `high`: affected IDs, upstream sources, direct consumers, and applicable workflow resolve; proceed within approved scope
- `medium`: one or more indirect impacts remain uncertain; widen targeted validation
- `low`: material references or ownership are unresolved; request review or run broader analysis before implementation

Confidence must be justified by traceability coverage and resolved references, not agent intuition alone.

---

## Scoped Stage Execution

Affected stage commands should accept a shared scoped-change context:

```json
{
  "execution_mode": "scoped_change",
  "change_id": "CHANGE-014",
  "requested_outcome": "",
  "affected_ids": [],
  "preserved_behavior": [],
  "allowed_outputs": [],
  "validation_level": "workflow",
  "preserve_unaffected_content": true
}
```

Scoped execution rules:

- load the existing canonical output before modification
- treat the worktree version as a candidate output until merge and post-merge verification
- create new stable IDs only for new concepts
- preserve stable IDs for modifications to the same concept
- preserve all unrelated valid content
- stop when the stage discovers work owned by an earlier stage
- return created, updated, removed, revalidated, and newly affected IDs
- append the current stage and attempt to the change record without changing the baseline global `current_stage`
- run a change-profile readiness audit only for a stage being finalized in scoped mode
- do not mark skipped stages as finalized

### Change-Cycle State Isolation

During scoped execution:

- preserve baseline stage statuses and `Global-workflow-state.json.current_stage`
- store `active_stage`, `stage_attempts`, `stage_results`, blockers, and next actions in the authoritative change record
- permit `Global-workflow-state.json` to expose only compact `active_change_refs` when needed
- write scoped readiness audits under `Build-Plans/Changes/CHANGE-NNN/audits/`
- never overwrite the baseline stage readiness audit with a scoped change attempt

### Scoped Change Handoff

Use a change-specific handoff when the next required stage is not the normal adjacent stage:

```json
{
  "handoff_mode": "scoped_change",
  "change_id": "CHANGE-014",
  "source_stage": "stage_1",
  "next_required_stage": "stage_3",
  "changed_refs": [],
  "preserved_refs": [],
  "evidence_refs": [],
  "blocking_items": []
}
```

The change handoff supplements rather than rewrites the baseline stage handoff. It allows a justified Stage 2 disposition or another conditional stage decision without pretending that a normal full-pipeline handoff occurred.

### Scoped Readiness Profile

The change-profile audit must preserve schema validation, changed-reference integrity, risk acceptance, required artifact evidence, approval, visual continuity, workflow outcome evidence, and revision-loop behavior. It replaces only full-stage file and adjacent-handoff requirements that are not applicable to a scoped amendment.

The audit must use `handoff_mode = "scoped_change"`. The global readiness-audit schema and contract must add that enum value and define `ready_for_next_stage` in this mode as readiness for the change record's `next_required_stage`, not readiness for the baseline pipeline's normal adjacent stage.

Use existing audit status values:

```text
pending
passed
passed_with_warnings
failed
blocked
```

When the audit returns `failed`, record `needs_revision` as the change or scoped-stage completion disposition rather than as `audit_status`.

---

## Stage Stop Conditions

Each affected stage must fail closed when scoped execution discovers an earlier-stage concern.

Examples:

- Stage 4 discovers a new product outcome or workflow: route to Stage 1
- Stage 4 discovers an undefined backend action, data requirement, or permission: route to Stage 3
- Stage 5 discovers a missing product, architecture, or UX specification: route to the owning earlier stage
- Stage 6 discovers that approved behavior is internally contradictory: route to the owning planning stage
- Stage 7 discovers missing launch-critical workflow evidence: route to Stage 6

The layer updates the required-stage route and requests approval only when the expansion is material.

---

## Conditional Stage Rules

### Stage 1

Add an explicit amendment mode without weakening normal initialization:

```text
normal mode
  -> run all Stage 1 subskills in their required sequence

scoped_change mode
  -> run only affected Stage 1 producer subskills
    -> run product-synthesis reconciliation
      -> verify all ten existing Stage 1 outputs remain present and coherent
        -> produce a scoped change handoff
```

Scoped amendment mode must not claim that a new normal Stage 1-to-Stage 2 cycle completed. It updates candidate product artifacts, preserves unrelated content, and records its readiness under the change cycle.

### Stage 2

Run scoped validation when the change introduces a new demand, market, business, or behavioral assumption. Otherwise record a concise `not_required` disposition with the evaluated assumption references and reason.

### Stage 3

Run when service, entity, API, integration, security, infrastructure, storage, authentication, or scalability contracts change.

### Stage 4

Run when journeys, screens, routes, actions, states, accessibility, responsive behavior, UI blueprints, visual specs, or design-system intent change.

### Stage 5

For Class A and bounded Class B changes, invoke `build-ticket-generation` in `scoped_change` mode without finalizing the full Stage 5 command. Store the resulting micro-ticket and its minimum execution context in the change record's `execution_packet`. Do not mark Stage 5 globally complete or create a normal Stage 5 manifest for this path.

Run the full Stage 5 orchestration only when the change requires multiple dependent tickets, parallel execution, release resequencing, a revised testing strategy, or material agent coordination.

### Stage 7

Run only when the change is prepared for deployment or changes migration, monitoring, analytics, support, rollout, rollback, or operational readiness.

### Stage 8

Stage 8 may seed a transient change proposal from live evidence but is not part of every change execution route. Its feedback route remains authoritative until approval creates a durable active change record.

---

## Micro-Ticket Contract

The scoped Stage 5 ticket generator must preserve the applicable canonical ticket fields. The minimum embedded execution packet is:

```json
{
  "change_id": "CHANGE-014",
  "implementation_sequence": [],
  "engineering_dependencies": [],
  "testing_strategy": {},
  "agent_assignment": {},
  "ticket": {
    "ticket_id": "TICKET-CHANGE-014",
    "slice_id": "SLICE-CHANGE-014",
    "title": "",
    "description": "",
    "ticket_type": "",
    "priority": "",
    "stage_1_feature_refs": [],
    "stage_3_architecture_refs": [],
    "stage_4_ux_refs": [],
    "ui_blueprint_refs": [],
    "route_refs": [],
    "action_refs": [],
    "interactive_element_refs": [],
    "completion_definition": {},
    "workflow_smoke_tests": [],
    "prerequisites": [],
    "depends_on_tickets": [],
    "primary_skill": "",
    "recommended_skills": [],
    "agent_required_skills": [],
    "agent_skill_instructions": {
      "must_use": [],
      "use_if_needed": [],
      "skill_usage_order": [],
      "usage_notes": ""
    },
    "expected_artifacts": [],
    "acceptance_criteria": [],
    "preserved_behavior": [],
    "validation_requirements": [],
    "rollback_or_disable_path": ""
  }
}
```

Include visual, responsive, accessibility, interaction, architecture, data, security, artifact, and other ticket fields whenever the affected work requires them. Do not generate the normal eight-artifact Stage 5 package for a one-ticket scoped change.

Stage 6 must gain an explicit `scoped_change` input path that consumes this embedded execution packet. The normal Stage 6 path must continue to require the complete Stage 5 v2 or legacy-compatible package. Supporting a micro-ticket must not relax normal Stage 6 requirements or allow incomplete frontend, workflow, artifact, skill, or validation instructions.

---

## Transient Context Bundle

Before each affected stage runs, assemble a non-canonical context bundle containing only:

- change record
- affected objects
- direct upstream sources
- direct downstream consumers
- relevant risks and assumptions
- preserved behavior
- applicable stage contract
- required validation criteria

Generate this bundle on demand. Do not preserve it as another source of truth. Its purpose is to reduce agent context size and prevent accidental modification of unrelated artifacts.

---

## Affected-ID Lock

Use a simple single-writer rule:

```text
Only one active change may modify a stable traceability ID.
```

Read-only dependencies do not require locks. When a second change needs the same ID, it must wait, declare a dependency, or be intentionally combined with the active change.

Lock lifecycle:

1. Acquire locks after approval, the second preflight, and initial impact analysis.
1. Reserve new stable IDs when they are allocated.
1. Acquire locks for newly discovered existing IDs through a serialized target-ledger coordination update before modifying those objects.
1. Retain locks while a change is `active`, `validating`, `ready_to_merge`, or `blocked` unless an authorized recovery explicitly releases them.
1. Release locks after successful merge and post-merge verification, rejection, or explicit cancellation.
1. Permit stale-lock recovery only when the owning change is terminal or an authorized recovery records the reason and evidence.

Do not implement automatic semantic rebasing or field-level merge resolution in the initial version.

---

## Compatibility Declaration

Require backend, data, event, and integration changes to declare:

```json
{
  "compatibility": {
    "api_breaking_change": false,
    "event_contract_breaking_change": false,
    "data_migration_required": false,
    "backward_compatible": true,
    "existing_consumers_checked": true,
    "rollback_safe": true
  }
}
```

An unknown or unsafe answer escalates validation and prevents the change from remaining on the bounded fast path.

---

## Validation Levels

### Local

Use for trivial, isolated changes:

- changed unit or component checks
- schema validation for changed structured artifacts
- one relevant smoke check

### Workflow

Use for bounded feature, page, API, or interaction changes:

- local checks
- affected end-to-end workflow
- direct API/UI integration where applicable
- immediate consumer regression tests
- accessibility, responsive, and visual checks when applicable

### System

Use for cross-cutting changes:

- affected workflow suite
- contract compatibility
- migration validation
- security validation
- broader regression boundary
- deployment and rollback validation when applicable

### Critical

Use for authentication, authorization, payments, destructive migrations, privacy, security, or critical operational work:

- all applicable system validation
- explicit human approval
- staging or equivalent runtime evidence
- monitoring and rollback proof

Do not run the full validation suite solely because a `CHANGE-` record exists. Validation scope must follow risk, shared dependencies, and preserved behavior.

---

## Feature Flags

Feature flags are optional and should be required only for:

- medium- or high-risk user-facing features
- gradual rollout
- features requiring live observation
- separately deployed frontend and backend work
- changes requiring immediate disablement

Every flag must include an owner and removal condition. Do not require flags for copy changes, internal refactors, or low-risk repairs.

---

## Approval Policy

Use proportional approval:

| Change | Approval expectation |
| --- | --- |
| Repair matching an existing approved requirement | No new product approval |
| Cosmetic correction within approved design direction | Request itself or low-risk inferred approval |
| Page layout or interaction change | Stage 4 change approval |
| Backend contract, migration, or security change | Technical approval |
| New feature, role, workflow, or product boundary | Consolidated product-change approval |
| High-risk deployment or migration | Explicit technical and release approval |
| Emergency | Incident authorization followed by retrospective review |

For a new feature affecting multiple planning stages, present one consolidated user-facing change brief. Affected Stage 1–4 outputs may reference that approval rather than presenting repetitive independent briefs, provided the global approval contract is explicitly updated to permit this scoped-change mode.

Normalize approval state separately from approval type:

```json
{
  "approval": {
    "required_types": ["product", "technical", "release", "incident"],
    "status": "pending",
    "evidence_refs": [],
    "approved_by": "",
    "approved_at": null
  }
}
```

Allowed approval states:

```text
pending
approved
revision_requested
blocked
rejected
```

Before implementation, normalize the existing stage decision-brief documentation and schema to use the same approval vocabulary where their meanings overlap. The change layer must not infer approval for a material product, architecture, UX, security, migration, or release decision.

---

## Git Isolation and Completion

After approval:

1. Rerun the read-only preflight.
1. Record the verified current target commit as the product `base_commit`.
1. Allocate the change ID and initial affected IDs.
1. Write the initial authoritative change record, compact ledger index entry, and affected-ID locks to the target as one coordination-only commit.
1. Create a branch or worktree named from the change ID and title, based on that coordination commit.
1. Update only affected candidate stage objects inside that isolated workspace.
1. Implement and validate according to the routed scope.
1. Review the Git diff for unrelated modifications.
1. Run the lightweight change completion audit.
1. Merge through the repository's approved publishing workflow.
1. Verify the target branch contains the approved change and valid canonical outputs.
1. Finalize the authoritative record as `completed` and release its affected-ID locks in a post-merge coordination update.

Git is the baseline, delta, conflict, and rollback mechanism. The change layer must not implement a competing storage or promotion system.

Terminology:

```text
target canonical outputs
  = approved files on the target branch

candidate outputs
  = provisional modified files in the change worktree

canonical outputs after merge
  = approved candidate files after post-merge verification
```

---

## Lightweight Completion Audit

The change completion audit should verify:

- change record exists and is valid
- required approvals resolve
- base commit and target are known
- changed schemas pass
- created and modified traceability IDs resolve
- direct upstream and downstream references resolve
- no affected-ID lock conflict remains
- preserved behavior received the required regression coverage
- escalation triggers were handled
- required workflow evidence exists
- high and critical risks resolve or link to accepted-risk records
- compatibility and migration declarations are complete when applicable
- Git diff contains no unexplained unrelated changes
- affected scoped stages passed the change-profile readiness requirements while preserving all applicable normal safety obligations

The audit returns:

```text
pending
passed
passed_with_warnings
failed
blocked
```

Only `passed` or `passed_with_warnings` may move the change to `ready_to_merge`. A `failed` audit records a `needs_revision` completion disposition in the change record. The change becomes `completed` only after merge and post-merge verification.

### Deferred-Item Gate

Every deferred item must record its owner, reason, next action, target stage or future change reference, approval evidence when required, and risk disposition. A deferred item may pass only when it is explicitly non-blocking, accepted as risk, converted into a proposed future change, or confirmed out of scope. A launch-critical requirement or required acceptance criterion cannot be deferred solely to obtain a passing audit.

---

## Completion Summary

Generate a concise human-readable summary from the change record, affected IDs, validation evidence, and Git diff. It should report:

- requested outcome
- created, modified, removed, and revalidated IDs
- stages executed and skipped
- implementation results
- validation performed
- preserved behavior confirmed
- deferred work
- risks and accepted risks
- release or feature-flag controls

The summary is a review artifact and must not become a competing canonical product definition.

---

## Anticipated Repository Changes After Approval

Exact names may be refined during implementation, but the expected minimal surface is:

### New Skill

```text
.opencode/Skills/change-intake-router/skill.md
```

Responsibilities:

- preflight
- refinement-versus-change decision
- classification
- entry-stage routing
- escalation handling
- change-budget enforcement
- affected-ID lock checks
- transient context assembly
- completion routing

### New Schema

```text
System-References/Schemas/change-record.schema.json
```

Do not create separate schemas for baselines, deltas, promotions, or dependency graphs in the initial implementation.

### New Durable State

```text
Build-Plans/Build-status/Change-ledger.json
```

The ledger is not a second copy of each change record. It should contain only compact record references, operational status, base commit, and affected-ID locks. It must not copy stage outputs, stage results, risks, approvals, or execution packets.

Illustrative index entry:

```json
{
  "change_id": "CHANGE-014",
  "record_path": "Build-Plans/Changes/CHANGE-014/change-record.json",
  "status": "active",
  "base_commit": "",
  "affected_id_locks": []
}
```

### Change Records

```text
Build-Plans/Changes/CHANGE-NNN/change-record.json
Build-Plans/Changes/CHANGE-NNN/change-summary.md
Build-Plans/Changes/CHANGE-NNN/audits/
```

`change-record.json` is authoritative. The summary is created at completion. Scoped audit attempts are stored under `audits/` so they do not overwrite baseline stage audits. Additional artifacts are added only when an existing stage contract requires them.

### Existing Contracts to Amend

At minimum, implementation will need to assess and selectively update:

- global workflow contract
- global readiness audit contract and skill
- global workflow state contract
- Stage 1, Stage 2, Stage 3, Stage 4, Stage 5, Stage 6, Stage 7, and Stage 8 command skills
- Stage 5 context or micro-ticket compatibility
- Stage 6 scoped input compatibility
- stage summary generation if change summaries are automated
- global ID standards to add `CHANGE-`
- skill registry after the new skill is finalized

Existing stage schemas should be changed only where required properties, fixed artifact counts, enums, handoff modes, or scoped input contracts cannot represent the approved change path. `additionalProperties: true` does not remove existing required-file, required-property, fixed-manifest, or enum constraints.

---

## Implementation Phases

### Phase 1 — Contract and Data Model

1. Add `CHANGE-` to the global ID standard.
1. Define the change classes, routing rules, escalation triggers, lifecycle statuses, and approval rules in the global workflow contract.
1. Add the compact change-record schema.
1. Add the initial empty change ledger.
1. Define affected-ID lock semantics.
1. Define the ledger as an index and lock table, with the per-change record as authoritative.
1. Define change-cycle state isolation from baseline global workflow state.
1. Normalize approval vocabulary used by the change layer and affected stage decision briefs.

Exit criteria:

- schema validates representative Class A through Class D records
- intentional changes are distinct from revision loops
- stage ownership remains unchanged

### Phase 2 — Intake Router

1. Create `change-intake-router`.
1. Implement read-only preflight behavior.
1. Implement post-approval preflight revalidation before recording the base commit.
1. Implement refinement-versus-change detection.
1. Implement deterministic classification and entry-stage routing.
1. Implement change budget, impact confidence, escalation, and stage dispositions.
1. Implement transient context bundle generation instructions.

Exit criteria:

- representative requests route consistently
- ambiguous or dirty-state requests fail closed
- low-risk requests do not trigger unnecessary stages

### Phase 3 — Scoped Stage Support

1. Add the shared `scoped_change` input contract to affected stage commands.
1. Add Stage 1 amendment-mode rules and Stage 2 scoped validation or disposition rules.
1. Add preservation rules for unrelated canonical content.
1. Add created, modified, removed, and revalidated ID reporting.
1. Add stage-specific stop conditions and backward routing.
1. Add conditional Stage 2, Stage 3, Stage 4, and Stage 7 rules.
1. Add scoped change handoffs, change-profile audits, and per-change audit paths.
1. Prevent scoped attempts from overwriting baseline global stage state or readiness audits.

Exit criteria:

- scoped changes update only permitted objects
- stable IDs are preserved
- newly discovered earlier-stage impacts stop or reroute work

### Phase 4 — Micro Stage 5 and Stage 6 Integration

1. Define micro-ticket compatibility with Stage 5 and Stage 6.
1. Invoke scoped `build-ticket-generation` without finalizing the normal Stage 5 package for a micro change.
1. Add the embedded execution packet and explicit Stage 6 `scoped_change` input path.
1. Ensure ticket-required skills and validation criteria remain preserved.
1. Implement validation-level routing.
1. Map preserved behavior to regression obligations.

Exit criteria:

- one-ticket changes do not regenerate the complete Stage 5 package
- Stage 6 can consume micro-tickets without weakening validation

### Phase 5 — Completion Audit and Summary

1. Extend the readiness audit or add a lightweight change profile to it.
1. Validate changed schemas and changed-ID reference integrity.
1. Validate approval, locks, compatibility, preserved behavior, and Git diff scope.
1. Validate deferred-item ownership and risk disposition.
1. Generate the completion summary.
1. Define `ready_to_merge`, post-merge verification, terminal completion, and lock release behavior.

Exit criteria:

- incomplete changes fail closed
- completed changes have evidence proportional to risk
- the summary matches canonical outputs and implementation evidence

### Phase 6 — Stage 8 and Emergency Integration

1. Convert Stage 8 feedback routes into transient route proposals and create durable active change records only after proportional user approval.
1. Add emergency entry and mandatory retrospective reconciliation.
1. Confirm Stage 7 and Stage 8 readiness behavior remains compatible.

Exit criteria:

- Stage 8 can seed but not silently authorize product changes
- emergency work retains retrospective traceability

---

## Verification Scenarios

Implementation must include tests or deterministic contract checks for at least:

1. Feature added while Stage 1 is still unapproved remains a Stage 1 refinement and creates no change cycle.
1. Feature added after Stage 1 approval creates a Class C change beginning at Stage 1.
1. Scoped Stage 1 runs affected producer work plus product-synthesis reconciliation without overwriting the baseline Stage 1 audit or global stage status.
1. Copy correction uses Class A and local validation.
1. Page redesign with unchanged behavior begins at Stage 4.
1. New page that creates a new workflow escalates from Stage 4 to Stage 1.
1. Backend refactor with unchanged contracts begins at Stage 6.
1. Breaking API change begins at Stage 3 and widens validation.
1. API change affecting UI includes Stage 4.
1. Dirty working tree blocks unsafe branch or worktree creation without altering user changes.
1. Target movement between approval and workspace creation is detected by the second preflight.
1. Second active change attempting to modify a locked ID is blocked or declared dependent.
1. Locks are acquired, retained, recovered, and released according to the defined lifecycle.
1. Change exceeding its budget is reclassified rather than silently expanded.
1. Low impact confidence prevents unsafe fast-path implementation.
1. Preserved behavior becomes explicit validation obligations.
1. Emergency work routes through Stage 6 and Stage 7, then requires retrospective reconciliation.
1. Stage 8 feedback remains a feedback-route candidate until approval creates a durable active change record.
1. Stage 1 may hand scoped work to Stage 3 when Stage 2 has a valid `not_required` disposition and scoped handoff.
1. A micro-ticket reaches Stage 6 through the embedded execution packet without creating or claiming a normal Stage 5 v2 finalization.
1. Scoped stage attempts do not change baseline `Global-workflow-state.json.current_stage` or overwrite baseline readiness audits.
1. Deferred launch-critical or unowned work blocks completion.
1. A passing audit sets `ready_to_merge`; only merge plus post-merge verification sets `completed` and releases locks.
1. Completion audit rejects unresolved references, missing approval, unexplained diff scope, or missing workflow evidence.

---

## Non-Goals

The initial implementation must not include:

- a ninth workflow stage
- custom immutable baseline storage
- duplicated full stage snapshots
- semantic JSON merge engine
- automatic field-level rebasing
- parallel writes to the same stable ID
- duplicated authoritative change records in both the ledger and change directory
- a general dependency-graph database
- custom atomic promotion transactions
- mandatory feature flags for every change
- full Stage 1–8 reruns for bounded changes
- full regression execution for trivial changes without risk justification
- automatic approval of material product, architecture, UX, security, migration, or release changes

---

## Success Criteria

The layer is successful when:

- a new feature absent from the initial PRD enters Stage 1 without restarting unrelated work
- a page-only revision can begin at Stage 4 when product and backend contracts remain unchanged
- an implementation-only backend repair can begin at Stage 6
- escalation automatically routes discovered upstream impacts to the correct owner
- unaffected stage artifacts remain byte-for-byte or semantically unchanged
- bounded changes require substantially less context and planning output than a full pipeline run
- every completed change retains stable-ID traceability, approval, validation evidence, and Git history
- scoped change activity does not regress or overwrite the baseline global stage state and readiness history
- one-ticket changes reach Stage 6 without generating a false full Stage 5 completion
- unresolved reference, compatibility, lock, approval, or validation failures prevent completion
- the current canonical outputs always describe the current approved product without reconstructing a chain of amendments

---

## Deferred Enhancements

Consider only after real usage demonstrates a need:

- richer change dependency relationships
- multiple coordinated changes per release train
- automated change rebasing
- cached reference indexes
- change lead-time and failure-rate metrics
- automatic feature-flag lifecycle cleanup
- advanced conflict visualization
- reusable change templates by application profile

---

## Approval Decision

Approved on **2026-08-17** for the minimal implementation described in the approval block. Any material expansion into baseline services, semantic merging, automatic branch/worktree mutation, parallel change orchestration, or additional workflow stages requires separate approval.
