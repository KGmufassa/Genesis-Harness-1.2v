---
name: operational-optimization
description: The operational-optimization skill analyzes operational burden after launch and recommends improvements.
compatibility: opencode
---

# Skill — operational-optimization

# Purpose

The `operational-optimization` skill analyzes operational burden after launch and recommends improvements.

It focuses on:

* support workload
* tooling gaps
* incident patterns
* monitoring usefulness
* operational friction

---

# Core Responsibilities

## Operational Burden Analysis

Identify support-heavy workflows, repeated incidents, manual operations, fragile tooling, and missing runbooks.

## Improvement Planning

Recommend support, tooling, runbook, monitoring, or workflow improvements with evidence quality and expected impact.

---

# Inputs

```json
{
  "stage_7_handoff": {},
  "telemetry_analysis": {},
  "support_signals": {},
  "incident_signals": {},
  "operational_metrics": {},
  "existing_state": {}
}
```

---

# Outputs

Update shared Stage 8 state in:

```text
Build-Plans/Build-status/Evolution-state.json
```

Return:

```json
{
  "operational_optimization": {},
  "support_improvements": [],
  "tooling_improvements": [],
  "operational_risks": []
}
```

This skill contributes to:

```text
Build-Plans/Stage-8/02-operational-optimization.json
```

---

# Feedback Routing Responsibilities

When operational findings indicate that the root issue belongs to an earlier stage, produce `feedback_route_candidates` instead of treating the issue only as a Stage 8 optimization.

Route examples:

* workflow burden caused by unclear product scope -> Stage 1
* support demand caused by invalid assumptions or market mismatch -> Stage 2
* operational fragility caused by architecture, infrastructure, or integration choices -> Stage 3
* user confusion caused by interaction, screen, visual, or state design -> Stage 4
* support-heavy rollout caused by execution planning gaps -> Stage 5
* recurring defects or insufficient validation -> Stage 6
* monitoring, onboarding, runbook, support, or deployment readiness gaps -> Stage 7

Each route candidate must include source signal IDs, severity, evidence references, recommended target stage, recommended action, and whether it blocks current evolution.
