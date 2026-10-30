---
name: system-health-synthesis
description: Synthesize Stage 6 implementation health, evidence, and readiness.
compatibility: opencode
---

# Skill — system-health-synthesis

# Purpose

The `system-health-synthesis` skill synthesizes Stage 6 implementation, validation, regression, and repair results.

It is responsible for:

* synthesizing implementation, validation, regression, and repair results
* determining readiness for Stage 7
* producing final Stage 6 outputs
* verifying all assigned tickets, agents, and parallel batches are accounted for

This skill is the final synthesis and completion gate for Stage 6.

---

# Inputs

```json
{
  "implementation_status": {},
  "validation_results": {},
  "regression_analysis": {},
  "repair_log": [],
  "build_tickets": {},
  "agent_assignment_plan": {},
  "parallel_execution_plan": {},
  "existing_state": {}
}
```

Read and update shared implementation state from:

```text
Build-Plans/Build-status/Implementation-state.json
```

---

# Final Stage 6 Output Files

Write or update:

```text
Build-Plans/Stage-6/01-implementation-status.json
Build-Plans/Stage-6/02-validation-results.json
Build-Plans/Stage-6/03-regression-analysis.json
Build-Plans/Stage-6/04-system-health.json
Build-Plans/Stage-6/05-repair-log.json
```

Each output must include references to relevant:

* Stage 5 ticket IDs
* implementation slice IDs
* agent IDs
* parallel batch IDs
* required skills used
* validation gates
* UI blueprint IDs
* visual spec IDs
* visual style reference refs
* design system IDs
* unresolved blockers

---

# Output Requirements

The implementation status output must include:

* implemented tickets
* pending tickets
* blocked tickets
* agent execution results
* parallel batch results
* files changed when available
* ticket skill usage notes

The validation results output must include:

* ticket validation results
* agent validation results
* batch validation results
* acceptance criteria status
* test/check results
* coverage gaps
* visual QA results
* responsive validation results
* visual reference compliance results
* design system compliance results
* visual drift status

The regression analysis output must include:

* affected tickets
* affected agents
* affected batches
* affected features
* affected workflows
* severity and blast radius

The repair log output must include:

* ticket repairs
* agent repair assignments
* repair verification status
* remaining defects
* unresolved repair risks

---

# Shared State Updates

Update:

```text
implementation_status
validation_results
regression_analysis
system_health
repair_log
stage_7_handoff
completion_status (include completed_at and recorded_at)
interactive_guidance
```

Persist updates to:

```text
Build-Plans/Build-status/Implementation-state.json
```

---

# Completion Gate

Stage 6 may complete only when:

* all assigned Stage 5 build tickets are implemented, blocked with reason, deferred with approval, or explicitly marked not applicable
* every executed ticket followed its `agent_required_skills` and `agent_skill_instructions`
* every generated or assigned agent reported execution status
* every parallel batch has validation results
* all required validation gates have pass/fail status
* regressions are analyzed and assigned severity
* high and critical defects have repairs, blockers, or escalation paths
* repair work has been revalidated
* system health is synthesized from implementation, validation, regression, and repair results
* launch-critical frontend tickets include visual QA, responsive validation, visual reference compliance, design system compliance, and visual drift status when required
* launch-critical frontend tickets include UI architecture, page archetype, layout pattern, component-family, and template-deviation compliance results when referenced by Stage 5 tickets
* ticket `expected_artifacts` are recorded in `Build-Plans/Build-status/Artifact-evidence-registry.json` or documented as blockers
* v2 Stage 5 evidence points to `Build-Plans/Stage-5/05-build-tickets.json` with `related_stage_data_path = "/data/tickets"`
* launch-critical workflow evidence is present and tied to Stage 5 smoke tests
* dead-control validation has no unresolved launch-critical failures
* runtime data source validation has no unresolved launch-critical fixture dependencies
* Stage 7 handoff contains unresolved operational, deployment, monitoring, analytics, and support needs

Stage 6 is `ready_for_stage_7` only when:

* no critical implementation blockers remain
* no unresolved critical validation failures remain
* no unresolved critical regressions remain
* all launch-critical tickets are implemented and validated
* all launch-critical user workflows are `local_e2e_passed`, `staging_e2e_passed`, or explicitly deferred/accepted as known risk
* no launch-critical frontend ticket has unresolved `major_visual_drift`
* visual reference compliance is validated or explicitly accepted as known risk for launch-critical frontend work
* UI architecture and layout pattern compliance is validated or explicitly accepted as known risk for launch-critical frontend work
* design system compliance is validated or explicitly accepted as known risk for launch-critical frontend work
* all high-risk repairs are verified or explicitly accepted as known risk

Possible completion statuses:

```text
ready_for_stage_7
needs_repair
needs_revalidation
blocked
```

## Global Workflow State Update

After setting completion_status and before declaring stage completion, update:

```text
Build-Plans/Build-status/Global-workflow-state.json
```

Set:

* `stages.stage_6.status` — the completion status value
* `stages.stage_6.ready_for_next_stage` — true if `ready_for_stage_7`, false otherwise
* `stages.stage_6.audit_file` — path to the readiness audit file
* `current_stage` — advance to `stage_7` when ready
* `last_audit` — ISO timestamp
* `next_recommended_action` — audit-driven next action

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
* expected artifact evidence maps back to Stage 5 ticket IDs
* frontend validation results map to UI blueprint IDs, UI architecture/template refs, page archetype refs, layout pattern refs, component-family refs, template-deviation refs, visual spec IDs, visual style reference refs, and design system IDs when present
* visual QA and responsive validation results are included for frontend tickets when required
* regression analysis maps failures back to affected tickets, agents, batches, workflows, and features
* repair log includes verification results
* completion_status includes completed_at and recorded_at timestamps
* Global-workflow-state.json reflects the stage completion status
* Stage 7 handoff is usable for launch and operationalization
