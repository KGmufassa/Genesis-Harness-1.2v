---
name: repair-workflow
description: The repair-workflow skill proposes, tracks, and verifies repairs during Stage 6.
compatibility: opencode
---

# Skill — repair-workflow

# Purpose

The `repair-workflow` skill proposes, tracks, and verifies repairs during Stage 6.

It is responsible for:

* proposing and tracking repairs
* prioritizing fixes
* verifying repaired behavior
* documenting repair decisions
* routing repair work back to the responsible ticket, agent, or batch
* preserving ticket-required skill instructions during repair

This skill is the repair orchestration layer for Stage 6.

---

# Inputs

```json
{
  "validation_results": {},
  "regression_analysis": {},
  "implementation_status": {},
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

# Repair Rules

For every repair:

* identify the failed ticket, agent, batch, check, or workflow
* preserve ticket `agent_required_skills`
* preserve ticket `agent_skill_instructions`
* assign repair to the responsible agent or manual owner
* require revalidation after repair
* record repair decision and outcome

If multiple repair paths are valid and materially affect behavior, architecture, UX, or release readiness, pause for user input.

---

# Outputs

```json
{
  "repair_log": [],
  "repair_actions": [],
  "ticket_repairs": [],
  "agent_repair_assignments": [],
  "repair_status": {},
  "remaining_defects": [],
  "repair_risks": []
}
```

---

# Shared State Updates

Update:

```text
repair_log
validation_results
system_health
interactive_guidance
```

When a repair touches a launch-critical workflow, re-run the associated workflow
smoke test and update `workflow_evidence`, `dead_control_validation`, and
`runtime_data_source_validation`. A repaired API or component does not clear the
blocker until the user-facing workflow evidence passes or is explicitly
deferred/accepted as risk.

Persist updates to:

```text
Build-Plans/Build-status/Implementation-state.json
```

---

# Validation Responsibilities

Validate:

* high and critical defects have repair paths
* repaired behavior is revalidated
* remaining defects are explicit
* repairs map back to tickets, agents, batches, or checks
* repair decisions do not silently alter Stage 5 sequencing or release strategy
