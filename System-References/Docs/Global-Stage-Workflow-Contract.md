# Global Stage Workflow Contract

## Stage 5 Normalized v2 Handoff

Stage 5 format `2.0` consists of a shared context file `00`, eight normalized
numbered artifact envelopes, and manifest file `09`. The manifest locates every
artifact and is the sole owner of completion status and the Stage 6 handoff.
Stage 6 must reject partial v2 handoffs and use the read-only compatibility
resolver for archived self-contained outputs.

Future v2 ticket evidence records use:

```json
{
  "related_stage_output": "Build-Plans/Stage-5/05-build-tickets.json",
  "related_stage_data_path": "/data/tickets"
}
```

# Purpose

This document defines the shared operating contract for all eight harness stages.

It exists to keep the stage system coherent across:

```text
Stage 1 -> Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6 -> Stage 7 -> Stage 8
```

The individual stage review docs define each stage's cognitive domain. This document defines the cross-stage rules that make those stages work as one workflow.

---

# Core Rule

Each stage must produce:

* structured outputs
* a completion status
* a handoff object for the next stage
* assumptions made
* unresolved risks
* traceability IDs
* enough evidence or rationale for downstream use

No stage should require the next stage to reinterpret vague planning notes.

---

# Global ID Standard

Use stable IDs across all stage outputs.

Recommended prefixes:

```text
USER-
WORKFLOW-
CAP-
FEATURE-
BOUNDARY-
DEP-
RISK-
ASSUMPTION-
SERVICE-
ENTITY-
API-
INTEGRATION-
INFRA-
SECURITY-
SCALE-
JOURNEY-
SCREEN-
BEHAVIOR-
STATE-
A11Y-
UI-BLUEPRINT-
VISUAL-SPEC-
DESIGN-SYSTEM-
SLICE-
TICKET-
AGENT-
BATCH-
VALIDATION-
VISUAL-QA-
ARTIFACT-
LAUNCH-GATE-
TELEMETRY-
EXPERIMENT-
CHANGE-
```

IDs should be stable once created. If a concept changes materially, update the object and preserve references rather than silently replacing the ID.

---

# Traceability Chain

The harness should preserve this end-to-end chain:

```text
Stage 1 feature/workflow
-> Stage 2 assumption
-> Stage 3 architecture decision
-> Stage 4 screen/behavior/state/UI architecture template/page archetype/layout pattern/component family/UI blueprint/visual spec/design system
-> Stage 5 slice/ticket/agent
-> Stage 6 implementation/validation/visual QA result
-> Stage 7 launch gate/operational signal
-> Stage 8 telemetry/evolution finding
```

Every downstream object should reference the upstream IDs that justify it.

Example:

```json
{
  "ticket_id": "TICKET-012",
  "feature_ids": ["FEATURE-004"],
  "workflow_ids": ["WORKFLOW-002"],
  "assumption_ids": ["ASSUMPTION-009"],
  "service_ids": ["SERVICE-003"],
  "screen_ids": ["SCREEN-005"],
  "ui_architecture_refs": ["saas-dashboard"],
  "page_archetype_refs": ["collection"],
  "layout_pattern_refs": ["data-table"],
  "ui_blueprint_ids": ["UI-BLUEPRINT-002"],
  "visual_spec_ids": ["VISUAL-SPEC-002"],
  "design_system_ids": ["DESIGN-SYSTEM-001"],
  "validation_ids": ["VALIDATION-018"]
}
```

---

# Global Visual And Design Continuity Rules

Frontend-facing work must preserve this continuity chain:

```text
Stage 4 UI blueprint
-> Stage 4 UI architecture template/page archetype/layout pattern/component family decisions
-> Stage 4 visual spec
-> Stage 4 design system foundation
-> Stage 5 frontend ticket
-> Stage 5 agent handoff
-> Stage 6 implementation result
-> Stage 6 visual QA result
-> Stage 7 visual launch readiness
```

# Workflow Outcome Evidence

For launch-critical user workflows, stage readiness is based on user outcomes,
not implementation artifacts. A workflow is not complete merely because a
contract, schema, API route, generated file, static UI, fixture-backed page, or
production build exists.

The required evidence chain is:

```text
UI action -> route/API/action -> database/queue/storage -> worker/service -> result visible in UI -> test or preview evidence
```

Stage 5 must declare the workflow proof obligations in build tickets. Stage 6
must execute and record workflow evidence. Stage 7 must reject Stage 6 handoffs
that lack launch-critical workflow evidence unless the gap is explicitly
deferred or accepted as a launch risk.

Allowed workflow evidence statuses:

```text
contract_only
api_exists_not_wired
ui_wired_not_validated
runtime_persistence_failed
runtime_persistence_verified
local_e2e_passed
staging_e2e_passed
deferred_with_approval
blocked
```

Rules:

* Stage 4 cannot complete launch-critical frontend planning without approved or explicitly assumed visual specs and a design system foundation.
* Stage 5 cannot create frontend build tickets without carrying UI blueprint refs, applicable UI architecture/page archetype/layout pattern/component family/template deviation refs, visual spec refs, design system refs, visual requirements, responsive requirements, and visual acceptance criteria.
* Stage 6 cannot complete frontend tickets requiring visual QA without recording preview evidence, responsive validation, layout pattern compliance when applicable, design system compliance, and visual drift status.
* Stage 7 cannot mark launch readiness as complete when launch-critical frontend work has unresolved visual QA failures, unresolved UI architecture/layout pattern/component-family/template-deviation compliance failures, unresolved design system compliance failures, missing required preview evidence, or `major_visual_drift`, unless explicitly accepted as a launch risk.

---

# Shared Completion Status Model

Each stage may keep stage-specific statuses, but every stage should also map to one global status.

Global statuses:

```text
ready_for_next_stage
needs_current_stage_revision
needs_prior_stage_revision
blocked
```

Status meaning:

| Status                         | Meaning                                                         |
| ------------------------------ | --------------------------------------------------------------- |
| `ready_for_next_stage`         | Required outputs and handoff are complete enough to proceed     |
| `needs_current_stage_revision` | The current stage needs more work before handoff                |
| `needs_prior_stage_revision`   | A problem must be sent back to an earlier stage                 |
| `blocked`                      | Work cannot continue without missing input, approval, or system capability |

Each `completion_status` should include:

```json
{
  "stage_specific_status": "",
  "global_status": "",
  "reason": "",
  "blocking_items": [],
  "next_actions": [],
  "ready_for": ""
}
```

---

# Stage Handoff Index

Each stage must produce the handoff expected by the next stage.

| Source Stage | Target Stage | Required Handoff |
| ------------ | ------------ | ---------------- |
| Stage 1 | Stage 2 | `stage_2_handoff` |
| Stage 2 | Stage 3 | `stage_3_handoff` |
| Stage 3 | Stage 4 | `stage_4_handoff` |
| Stage 3 | Stage 5 | `stage_5_handoff` |
| Stage 4 | Stage 5 | `stage_5_handoff` |
| Stage 5 | Stage 6 | `stage_6_handoff` |
| Stage 6 | Stage 7 | `stage_7_handoff` |
| Stage 7 | Stage 8 | `stage_8_handoff` |
| Stage 8 | Earlier stages | `prior_stage_feedback` |

Every handoff must include:

```json
{
  "source_stage": "",
  "target_stage": "",
  "source_output_directory": "",
  "required_files": [],
  "ready": false,
  "blocking_items": [],
  "accepted_risks": [],
  "traceability_refs": [],
  "completion_status": {}
}
```

---

# Stage Decision Brief Rules

Stages 1-4 must use a proposal-first planning workflow before final readiness.

Stages 1-4 decide the product, validation, architecture, and UX/UI direction. These stages must present a user-reviewable decision brief before they lock outputs and hand off to the next stage.

Stages 5-8 consume approved direction and do not require a stage decision brief by default.

Required brief output path:

```text
Build-Plans/Stage-N/00-stage-decision-brief.md
```

Shared decision brief object:

```json
{
  "stage_decision_brief": {
    "brief_id": "",
    "stage": "",
    "brief_path": "",
    "recommended_direction": "",
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
    "alternatives_considered": [],
    "key_decisions": [],
    "assumptions": [],
    "risks": [],
    "downstream_impact": [],
    "user_decision_required": true,
    "approval_status": "pending | approved | revise | rejected",
    "approved_by": "",
    "approved_at": "",
    "revision_notes": []
  }
}
```

Completion rule:

```text
Stages 1-4 may not use ready completion status unless stage_decision_brief.approval_status = approved.
```

Exception:

```text
Assumed approval is allowed only when the active stage_contract_profile explicitly permits inferred approval for that stage.
```

Traceability:

```text
stage_decision_brief -> stage outputs -> next stage handoff
```

Stage 1 decision brief confirms the app idea, features, MVP direction, and how the app should work.

Stage 2 decision brief confirms whether validated product assumptions are strong enough to continue into architecture.

Stage 3 decision brief confirms architecture and tech stack direction.

Stage 4 decision brief uses the recommended approach to propose UX/UI direction before build tickets are generated.

---

# Revision Loop Rules

When a later stage discovers a blocker, it must route the issue to the correct earlier stage.

| Issue Type | Route Back To |
| ---------- | ------------- |
| Product identity, user, workflow, MVP scope problem | Stage 1 |
| Invalid, contradicted, or unsupported assumption | Stage 2 |
| Service, data, API, security, infrastructure, or scalability flaw | Stage 3 |
| Journey, screen, behavior, state, accessibility, UI architecture template, page archetype, layout pattern, component family, UI blueprint, visual spec, or design system flaw | Stage 4 |
| Sequencing, ticket, agent, testing, or release planning flaw | Stage 5 |
| Implementation, validation, regression, repair, visual QA, responsive validation, UI architecture/layout pattern compliance, or design system compliance flaw | Stage 6 |
| Deployment, monitoring, analytics, support, visual launch readiness, or launch readiness flaw | Stage 7 |
| Live telemetry, optimization, roadmap, AI, or scale evolution need | Stage 8 |

Revision feedback must include:

```json
{
  "feedback_id": "",
  "source_stage": "",
  "target_stage": "",
  "issue": "",
  "severity": "",
  "affected_ids": [],
  "evidence_refs": [],
  "recommended_action": "",
  "blocks_current_stage": false
}
```

Readiness failures must also produce revision-loop records.

```json
{
  "revision_loop": {
    "revision_id": "",
    "triggering_audit": "",
    "owning_stage": "",
    "owning_output": "",
    "owning_skill": "",
    "blocking_issue": "",
    "required_change": "",
    "recommended_action": "",
    "can_continue_with_accepted_risk": false,
    "target_status_after_revision": "",
    "status": "open | in_progress | resolved | accepted_risk"
  }
}
```

Revision-loop records must distinguish:

* current-stage revisions
* prior-stage revisions
* blocked items needing user input
* accepted-risk exceptions

Accepted-risk revision loops must link to `Build-Plans/Build-status/Risk-acceptance-ledger.json`.

---

# Shared Risk Model

All stages should use the same risk shape.

```json
{
  "risk_id": "",
  "risk": "",
  "domain": "",
  "severity": "medium",
  "likelihood": "medium",
  "status": "open",
  "affected_ids": [],
  "mitigation": "",
  "owner_stage": "",
  "evidence_refs": [],
  "next_action": ""
}
```

Allowed severity values:

```text
low
medium
high
critical
```

Allowed likelihood values:

```text
low
medium
high
```

Allowed risk statuses:

```text
open
mitigated
accepted
resolved
```

High and critical risks must include mitigation, owner stage, and next action.

---

# Risk Acceptance Ledger Rules

Accepted risks must be durable and visible downstream.

Canonical risk acceptance ledger path:

```text
Build-Plans/Build-status/Risk-acceptance-ledger.json
```

Risk acceptance ledger structure:

```json
{
  "ledger_version": "1.0.0",
  "accepted_risks": [
    {
      "risk_id": "",
      "source_stage": "",
      "source_output": "",
      "risk": "",
      "severity": "low | medium | high | critical",
      "accepted_by": "",
      "acceptance_authority": "user | delegated_policy",
      "approval_ref": "",
      "delegated_policy_ref": "",
      "accepted_at": "",
      "acceptance_reason": "",
      "mitigation": "",
      "owner_stage": "",
      "downstream_visibility": [],
      "revisit_trigger": "",
      "expires_or_recheck_at": "",
      "status": "active | mitigated | expired | superseded"
    }
  ]
}
```

Rules:

* accepted high and critical risks must include owner stage, mitigation, downstream visibility, and revisit trigger
* accepted high and critical risks require explicit user approval unless a checked project policy delegates that authority
* delegated acceptance must record `acceptance_authority: delegated_policy`, `delegated_policy_ref`, the acting identity in `accepted_by`, and an `approval_ref`
* agents may identify, mitigate, escalate, or propose acceptance of high and critical risks, but may not silently accept them
* accepted high and critical risks must appear in the next stage handoff
* accepted launch risks must be visible to Stage 8
* expired or superseded accepted risks must be revisited before a ready completion status is used

---

# Shared Assumption And Evidence Rules

Every stage may make assumptions. Assumptions must be recorded instead of hidden.

Assumption structure:

```json
{
  "assumption_id": "",
  "assumption": "",
  "source_stage": "",
  "affected_ids": [],
  "confidence": 0.0,
  "risk_if_false": "",
  "evidence_refs": [],
  "status": "active"
}
```

Evidence structure:

```json
{
  "evidence_id": "",
  "type": "",
  "source": "",
  "summary": "",
  "quality": "medium",
  "url_or_path": "",
  "collected_at": "",
  "supports_ids": []
}
```

Evidence quality values:

```text
none
low
medium
high
```

Rules:

* distinguish evidence from inference
* mark unsupported claims as assumptions
* mark low-evidence recommendations as provisional
* preserve source links or local artifact paths when available
* record when external research, telemetry, testing, or validation was unavailable

---

# Artifact Registry Rules

Artifacts are evidence created or collected during stage execution.

Examples:

* research sources
* planning traces
* screenshots
* test logs
* build logs
* deployment logs
* incident reports
* telemetry exports
* support summaries
* user feedback records

Canonical artifact registry path:

```text
Build-Plans/Build-status/Artifact-evidence-registry.json
```

Artifact registry structure:

```json
{
  "registry_version": "1.0.0",
  "artifacts": [
    {
      "artifact_id": "",
      "type": "test_output | screenshot | preview_url | build_log | validation_report | deployment_evidence | launch_check | telemetry_source",
      "related_stage": "",
      "related_stage_output": "",
      "related_ticket_ids": [],
      "related_validation_ids": [],
      "related_agent_ids": [],
      "path_or_url": "",
      "status": "pending | passed | failed | blocked | accepted_risk",
      "confidence": "low | medium | high",
      "created_by": "",
      "created_at": "",
      "notes": ""
    }
  ]
}
```

Large artifacts should be referenced by path instead of embedded in full.

Stages 5-7 must use this registry for expected artifacts, generated validation evidence, deployment proof, preview evidence, launch checks, and accepted-risk evidence.

---

# Stage Contract Profile Rules

Each project should use a stage contract profile to decide required depth, required outputs, optional outputs, and approval gates.

The profile may be selected by the user or inferred during Stage 1.

Supported profile examples:

```text
simple-crud-app
frontend-heavy-app
ai-heavy-app
marketplace-app
internal-tool
enterprise-saas
mobile-first-app
compliance-sensitive-app
integration-heavy-app
data-heavy-app
```

Shared profile object:

```json
{
  "stage_contract_profile": {
    "profile_id": "",
    "profile_name": "",
    "app_type": "",
    "complexity_level": "low | medium | high | critical",
    "guidance_depth": "minimal | standard | detailed | exhaustive",
    "required_stage_depth": {
      "stage_1": "",
      "stage_2": "",
      "stage_3": "",
      "stage_4": "",
      "stage_5": "",
      "stage_6": "",
      "stage_7": "",
      "stage_8": ""
    },
    "required_validation_layers": [],
    "optional_outputs": [],
    "required_outputs": [],
    "skip_allowed_outputs": [],
    "approval_gates": []
  }
}
```

Readiness audits must evaluate the active stage against the selected profile instead of assuming every project requires exhaustive depth.

---

# Schema Validation Rules

Stage outputs should be validated against machine-checkable schema references.

Canonical schema folder:

```text
System-References/Schemas/
```

Each readiness audit should record:

```json
{
  "schema_validation": {
    "schema_refs": [],
    "validated_files": [],
    "schema_errors": [],
    "schemas_valid": false,
    "validated_at": "",
    "validator": "",
    "blocking": true
  }
}
```

Missing or invalid schema validation may block readiness when the affected output is required by the active stage contract profile.

Every stage review doc and stage command must require this object before a ready completion status is used.

---

# Reference Integrity Rules

Every readiness audit should validate cross-stage references.

Reference integrity structure:

```json
{
  "reference_integrity": {
    "checked_refs": [],
    "missing_refs": [],
    "orphaned_refs": [],
    "stale_refs": [],
    "duplicate_ids": [],
    "integrity_status": "passed | passed_with_warnings | failed",
    "blocking_ref_errors": []
  }
}
```

Reference checks should cover:

```text
USER-*
WORKFLOW-*
CAP-*
FEATURE-*
BOUNDARY-*
DEP-*
RISK-*
ASSUMPTION-*
SERVICE-*
ENTITY-*
API-*
SCREEN-*
PAGE-*
COMPONENT-*
TICKET-*
AGENT-*
ARTIFACT-*
```

Readiness must fail when launch-critical downstream outputs reference missing, duplicate, or stale upstream IDs unless the active stage contract profile allows an explicit accepted exception.

---

# Scoped Change Layer

Approved-product changes use `change-intake-router`; they do not create Stage 9.

Canonical files:

```text
System-References/Schemas/change-record.schema.json
Build-Plans/Build-status/Change-ledger.json
Build-Plans/Changes/CHANGE-NNN/change-record.json
```

Rules:

* work in an active, unapproved owning stage remains an ordinary stage refinement and creates no `CHANGE-` record
* approved-scope changes route to the earliest materially affected stage
* one authoritative change record stores approval, route, affected IDs, preserved behavior, validation level, risks, evidence, and completion state
* the ledger is only an index and affected-ID lock table
* only one active change may write a stable ID
* scoped work must not overwrite baseline global stage status or baseline readiness audits
* material escalation requires renewed user review before scope expands
* only a passed scoped audit may set `ready_to_merge`
* `completed` requires merge plus post-merge verification

Use:

```sh
python3 .opencode/Skills/change-intake-router/scripts/route_change.py "<request>"
```

---

# Canonical Artifact Field Names

Use these field names consistently:

```text
expected_artifacts
artifact_evidence_updates
artifact_refs
Artifact-evidence-registry.json
```

Stage 5 build tickets must define `expected_artifacts` when validation, preview, visual QA, deployment proof, launch readiness, or post-launch evidence is required.

Stage 6 must map `expected_artifacts` to `artifact_evidence_updates` and final `artifact_refs`.

Stage 7 must consume `artifact_refs` and `deployment_proof`.

Global readiness audits must validate that required expected artifacts have matching registry entries or accepted blockers.

---

# Shared Interactive Guidance Rules

Every stage should use the same interaction discipline:

```text
Ask only when the answer materially affects the stage output or downstream handoff.
Infer low-risk defaults when supported by prior outputs.
Record assumptions when proceeding without confirmation.
Block only when missing information prevents reliable completion.
```

Each stage state should include:

```json
{
  "interactive_guidance": {
    "open_questions": [],
    "answered_questions": [],
    "assumptions_made": [],
    "blocked_decisions": [],
    "user_confirmations": [],
    "confidence_gaps": []
  }
}
```

Each stage state should also include:

```json
{
  "guidance_policy": {
    "complexity_level": "low | medium | high | critical",
    "guidance_depth": "minimal | standard | detailed | exhaustive",
    "ask_threshold": "only_blockers | material_decisions | important_tradeoffs | all_uncertainties",
    "default_inference_allowed": true,
    "approval_required_for": [],
    "max_questions_per_turn": 3
  }
}
```

Low-complexity profiles should ask fewer questions and record more safe assumptions. High-risk profiles should ask more confirmation questions and block on more unresolved decisions.

---

# Stage Readiness Audit

Every stage finalization attempt must write a readiness audit before the final completion status is committed to shared state.

This applies when the proposed status is ready, revision-needed, prior-stage-revision, or blocked. The audit records the reason the stage can proceed, cannot proceed, or must route work elsewhere.

Stages 5 through 8 must also write a local markdown assessment summary for every finalization attempt:

```text
Build-Plans/Stage-5/10-stage-5-summary.md
Build-Plans/Stage-6/06-stage-6-summary.md
Build-Plans/Stage-7/06-stage-7-summary.md
Build-Plans/Stage-8/06-stage-8-summary.md
```

The summary must be clear, concise, and detailed enough for a user to assess the stage. It must summarize actions taken, canonical outputs, results, validation and readiness evidence, blockers, risks, accepted risks, next actions, and downstream handoff or feedback-route readiness. It is a local review artifact only; downstream stages must continue to consume canonical JSON outputs and handoff contracts.

Before any stage marks itself ready, verify:

* required output directory exists
* required output files exist
* required local assessment summary exists for Stage 5-8
* output files follow expected schemas
* completion status is present
* handoff object is present
* risks are recorded
* assumptions are recorded
* unresolved blockers are explicit
* traceability IDs connect to upstream objects
* downstream stage has enough structured input to proceed

Stage 7 must write:

```text
Build-Plans/Build-status/Stage-7-readiness-audit.json
```

Stage 8 must write:

```text
Build-Plans/Build-status/Stage-8-readiness-audit.json
```

Stage 8 is terminal and cyclical. Its audit evaluates `prior_stage_feedback` and feedback routes to earlier stages instead of a Stage 9 handoff.

Readiness audit output:

```json
{
  "stage": "",
  "command": "global-stage-readiness-audit",
  "audit_status": "",
  "finalization_attempt": true,
  "proposed_completion_status": "",
  "evaluated_completion_status": "",
  "handoff_mode": "next_stage | feedback_routes | terminal",
  "required_files_present": true,
  "local_assessment_summary": {
    "required": false,
    "path": "",
    "present": false,
    "matches_canonical_outputs": false,
    "assessment": "",
    "blocking_gaps": []
  },
  "workflow_outcome_evidence": {
    "required": false,
    "workflow_evidence_present": false,
    "launch_critical_workflows_checked": [],
    "launch_critical_workflows_passed": false,
    "dead_controls_detected": [],
    "fixture_runtime_dependencies": [],
    "blocking_workflow_gaps": []
  },
  "schemas_valid": true,
  "handoff_present": true,
  "feedback_routes_present": false,
  "traceability_present": true,
  "schema_validation": {},
  "reference_integrity": {},
  "artifact_evidence_registry": {},
  "risk_acceptance_ledger": {},
  "feedback_route_audit": {},
  "revision_loops": [],
  "blocking_gaps": [],
  "warnings": [],
  "ready_for_next_stage": false
}
```

For Stage 8, `ready_for_next_stage` means the current evolution package is ready to close or start a new routed stage cycle. It does not imply a Stage 9 exists.

---

# Global Workflow Completion Principle

The harness is complete only when every stage can answer:

```text
What did this stage decide?
Why was it decided?
What evidence or assumptions support it?
What risks remain?
What exact structured input does the next stage receive?
```

If any stage cannot answer those questions, it is not ready to hand off.
