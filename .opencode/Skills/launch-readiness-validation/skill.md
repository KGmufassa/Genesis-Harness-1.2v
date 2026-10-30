---
name: launch-readiness-validation
description: The launch-readiness-validation skill validates whether the implemented system is ready for launch preparation.
compatibility: opencode
---

# Skill — launch-readiness-validation

# Purpose

The `launch-readiness-validation` skill validates whether the implemented system is ready for launch preparation.

It confirms:

* production readiness
* unresolved launch blockers
* onboarding readiness
* support readiness
* visual QA readiness
* visual reference compliance readiness
* design system compliance readiness
* accepted launch risks
* interaction contract readiness
* workflow outcome evidence readiness

---

# Core Responsibilities

## Readiness Gate Review

Validate:

* implementation status
* validation results
* regression status
* system health
* visual QA results
* responsive validation results
* visual reference compliance
* design system compliance
* visual drift status
* interaction contract validation results
* stable `UI-ELEMENT-`, `ROUTE-`, and `ACTION-` conformance
* destructive, security-sensitive, payment, admin, permission-sensitive, and mutation path results
* launch-critical workflow evidence from Stage 6
* dead-control validation results
* runtime data source validation results
* approved interaction deviations
* unresolved repair items
* launch-critical risks

## Onboarding And Support Readiness

Identify:

* onboarding gaps
* support gaps
* user-facing setup needs
* operational handoff needs

## Blocker Detection

Record launch blockers with owner, severity, affected systems, required action, and launch impact.

---

# Inputs

```json
{
  "implementation_status": {},
  "validation_results": {},
  "regression_analysis": {},
  "system_health": {},
  "repair_log": {},
  "existing_state": {}
}
```

---

# Outputs

Update shared Stage 7 state in:

```text
Build-Plans/Build-status/Operationalization-state.json
```

Return:

```json
{
  "launch_readiness": {},
  "launch_blockers": [],
  "readiness_gates": [],
  "visual_launch_readiness": {},
  "visual_reference_launch_readiness": {},
  "design_system_launch_readiness": {},
  "interaction_launch_readiness": {},
  "workflow_evidence_review": {},
  "critical_interaction_path_results": [],
  "accepted_interaction_deviations": [],
  "deployment_proof_readiness": {},
  "onboarding_gaps": [],
  "support_gaps": []
}
```

Block launch readiness when launch-critical frontend work has:

* missing required preview URL or preview evidence
* unresolved visual QA failures
* unresolved responsive validation failures
* unresolved UI architecture template, page archetype, layout pattern, component-family, or template-deviation compliance failures
* unresolved visual reference compliance failures
* unresolved design system compliance failures
* `major_visual_drift`
* an unresolved interaction contract failure
* a missing or broken critical route or action outcome
* a missing or broken required layout pattern behavior, such as data-table sorting/filtering/mobile transformation/bulk-selection behavior when required
* a missing required confirmation, permission-denied, recovery, mobile, accessibility, or design-system behavior
* a dropped, renamed, rerouted, or behavior-changed interaction without an approved deviation
* missing Stage 6 workflow evidence for a launch-critical workflow
* a launch-critical workflow that is only `contract_only`, `api_exists_not_wired`, `ui_wired_not_validated`, `runtime_persistence_failed`, or `blocked`
* unresolved dead controls on launch-critical visible actions
* unresolved fixture-backed runtime data on launch-critical screens

These may proceed only when explicitly recorded as accepted launch risks.

Tie every interaction blocker or accepted risk to the affected `UI-ELEMENT-`, `ROUTE-`, `ACTION-`, Stage 5 ticket, and Stage 6 validation references.

Tie every workflow blocker or accepted risk to the affected `WORKFLOW-`, Stage 5
ticket, route, UI element, action, validation, and evidence references.

Launch readiness must also validate production build proof, deployment dry-run evidence, smoke test evidence, rollback verification, environment verification, and monitoring alert proof when they are required by the active stage contract profile.

This skill contributes to:

```text
Build-Plans/Stage-7/01-launch-readiness.json
```
