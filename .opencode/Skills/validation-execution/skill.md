---
name: validation-execution
description: Execute Stage 6 validation against canonical Stage 5 ticket and testing payloads.
compatibility: opencode
---

# Skill — validation-execution

# Purpose

The `validation-execution` skill runs or coordinates planned validation for Stage 6.

It is responsible for:

* running or coordinating planned validation
* mapping tests to features, workflows, tickets, agents, and acceptance criteria
* validating ticket acceptance criteria
* validating agent-reported results
* validating batch-level gates from the parallel execution plan
* recording pass/fail status
* identifying missing coverage

This skill is the validation layer for Stage 6.

---

# Inputs

```json
{
  "implementation_status": {},
  "build_tickets": {},
  "agent_assignment_plan": {},
  "parallel_execution_plan": {},
  "testing_strategy": {},
  "ui_blueprint_inputs": {},
  "visual_reference_inputs": {},
  "existing_state": {}
}
```

Read and update shared implementation state from:

```text
Build-Plans/Build-status/Implementation-state.json
```

---

# Validation Execution Rules

Use validation steps from:

* Stage 5 testing strategy
* build ticket `validation_steps`
* ticket acceptance criteria
* agent validation requirements
* parallel batch validation gates
* Stage 4 UI blueprint specification for frontend tickets with `ui_blueprint_refs`
* Stage 4 UI architecture template, page archetype, layout pattern, component-family, and template-deviation requirements for frontend tickets with structural UI architecture refs
* Stage 4 page interaction contracts and complete app Mermaid maps for frontend tickets with `interaction_contract_refs`
* Stage 4 visual spec matrix for frontend tickets with `visual_spec_refs`
* Stage 4 selected visual style references for frontend tickets with `visual_reference_refs`
* Stage 4 design system foundation for frontend tickets with `design_system_refs`
* repository test scripts when available

Do not guess missing test commands blindly.

If validation cannot run because a command or check is undefined, mark validation as blocked and record:

```text
missing_validation_command
```

If validation fails, record the failure and route it to `repair-workflow`.

For frontend tickets with `ui_blueprint_refs`, validate implementation against:

```text
Build-Plans/Stage-4/07-ui-blueprint-specification.json
```

Confirm referenced page structure, layout, sections, components, shared components, routes, actions, states, data requirements, validation requirements, accessibility requirements, responsive requirements, visual requirements, visual reference requirements, visual acceptance criteria, and design system compliance.

Confirm referenced UI architecture context, page archetype, selected layout pattern, layout decision factors, layout rationale, rejected plausible patterns, component-family decisions, template deviations, and desktop/tablet/mobile transformations.

For `data-table` layout requirements, verify sorting, filtering, loading, empty, no-results, error, mobile transformation, and bulk-selection behavior where applicable. For comparison-heavy pages, treat unapproved replacement with `card-grid` or another weaker comparison pattern as UI blueprint drift.

For every referenced `UI-ELEMENT-`, verify existence, label or accessible name, behavior, owning component, route or action resolution, route type, state behavior, permissions, confirmation, responsive behavior, accessibility behavior, and design-system component mapping. Verify `ACTION-` success, failure, loading, denied, and recovery outcomes where applicable. Reconcile complex flows with the applicable Mermaid map.

For frontend tickets with `visual_qa_required`, validate through available visual evidence such as screenshots, browser preview, responsive viewport checks, Playwright checks, or documented manual review. Record visual drift as:

```text
visual_match
minor_visual_drift
major_visual_drift
requires_user_review
```

Classify visual drift source when possible:

```text
ui_blueprint_drift
visual_spec_drift
visual_reference_drift
design_system_drift
implementation_only_drift
```

---

# Outputs

```json
{
  "validation_results": {},
  "ticket_validation_results": [],
  "agent_validation_results": [],
  "batch_validation_results": [],
  "ui_blueprint_validation_results": [],
  "interaction_contract_validation_results": [],
  "interactive_element_validation_results": [],
  "route_validation_results": [],
  "action_validation_results": [],
  "approved_interaction_deviations": [],
  "visual_spec_validation_results": [],
  "visual_reference_validation_results": [],
  "design_system_validation_results": [],
  "visual_qa_results": [],
  "responsive_validation_results": [],
  "visual_drift_results": [],
  "workflow_evidence": [],
  "dead_control_validation": {},
  "runtime_data_source_validation": {},
  "artifact_evidence_updates": [],
  "passed_checks": [],
  "failed_checks": [],
  "coverage_gaps": [],
  "validation_risks": []
}
```

---

# Shared State Updates

Update:

```text
validation_results
test_failures
system_health
interactive_guidance
```

Persist updates to:

```text
Build-Plans/Build-status/Implementation-state.json
```

---

# Validation Responsibilities

Validate:

* every implemented ticket has pass/fail status for acceptance criteria
* every launch-critical workflow smoke test has pass/fail/deferred/blocked status
* workflow evidence proves the declared user outcome, not only build or API existence
* every visible launch-critical button, form, link, menu item, and primary action is wired to working behavior or explicitly disabled with a reason
* launch-critical runtime screens fetch from live database/API/queue/storage/service data rather than fixtures, unless deferred or accepted as risk
* every assigned agent has validation results when work was executed
* every parallel batch has validation gate results
* failed checks include error output or failure reason when available
* coverage gaps are explicit
* validation results map back to ticket IDs
* frontend validation results map to referenced UI blueprint IDs when present
* frontend validation results map to interaction contract, `UI-ELEMENT-`, `ROUTE-`, and `ACTION-` IDs when present
* frontend validation results map to referenced visual spec IDs when present
* frontend validation results map to referenced visual style references when present
* frontend validation results map to referenced design system IDs when present
* frontend tickets with UI blueprint refs validate required page, component, route, action, state, interactive element (element_type, label, route_target, behavior), accessibility, responsive, and visual behavior
* frontend tickets validate confirmation, permission-denied, success, failure, loading, and recovery outcomes where applicable
* dropped, renamed, rerouted, or behavior-changed interactions fail unless an approved deviation is recorded
* complex interaction implementations reconcile with required complete app blueprint Mermaid maps
* frontend tickets with visual spec refs validate visual acceptance criteria and report any visual gaps
* frontend tickets with visual reference refs validate that the implemented visual direction preserves the selected reference intent after conversion through the design system
* frontend tickets with visual QA requirements report visual QA evidence and visual drift status
* frontend tickets with design system refs report design system compliance
* validation outputs, screenshots, preview URLs, logs, and reports are recorded or queued for `Build-Plans/Build-status/Artifact-evidence-registry.json`
* v2 Stage 5 ticket evidence uses `related_stage_output = "Build-Plans/Stage-5/05-build-tickets.json"` and `related_stage_data_path = "/data/tickets"`
