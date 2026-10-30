---
name: regression-analysis
description: The regression-analysis skill detects and analyzes behavior regressions during Stage 6.
compatibility: opencode
---

# Skill — regression-analysis

# Purpose

The `regression-analysis` skill detects and analyzes behavior regressions during Stage 6.

It is responsible for:

* detecting behavior regressions
* comparing current behavior to planned workflows
* identifying broken dependencies
* identifying regressions introduced by specific tickets, agents, or parallel batches
* assessing blast radius

This skill is the regression intelligence layer for Stage 6.

---

# Inputs

```json
{
  "implementation_status": {},
  "validation_results": {},
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

# Core Responsibilities

## Regression Detection

Identify regressions from:

* failed validation checks
* changed behavior against acceptance criteria
* broken workflows
* broken integrations
* failing tests after implementation
* agent or batch merge conflicts

## Blast Radius Analysis

Map regressions to:

* affected tickets
* affected agents
* affected batches
* affected features
* affected workflows
* affected architecture or UX assumptions

---

# Outputs

```json
{
  "regression_analysis": {},
  "regressions": [],
  "affected_features": [],
  "affected_workflows": [],
  "affected_tickets": [],
  "affected_agents": [],
  "affected_batches": [],
  "severity": {}
}
```

---

# Shared State Updates

Update:

```text
regression_analysis
system_health
execution_blockers
interactive_guidance
```

Persist updates to:

```text
Build-Plans/Build-status/Implementation-state.json
```

---

# Validation Responsibilities

Validate:

* each regression has severity
* each regression has affected ticket, agent, or batch when traceable
* each critical regression blocks Stage 7 readiness
* each regression has a recommended repair or escalation path
