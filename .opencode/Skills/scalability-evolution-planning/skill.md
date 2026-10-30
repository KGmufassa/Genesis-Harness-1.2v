---
name: scalability-evolution-planning
description: The scalability-evolution-planning skill analyzes scaling, performance, cost, and operational capacity signals after launch.
compatibility: opencode
---

# Skill — scalability-evolution-planning

# Purpose

The `scalability-evolution-planning` skill analyzes scaling, performance, cost, and operational capacity signals after launch.

It identifies:

* performance findings
* cost findings
* scaling bottlenecks
* infrastructure evolution needs
* operational scaling risks

---

# Core Responsibilities

## Scaling Signal Review

Analyze usage growth, traffic patterns, infrastructure metrics, AI usage cost, support volume, latency, error rates, and dependency limits.

## Evolution Planning

Recommend scaling improvements, cost optimizations, infrastructure changes, operational capacity changes, and Stage 3 architecture feedback when needed.

---

# Inputs

```json
{
  "telemetry_analysis": {},
  "monitoring_data": {},
  "cost_metrics": {},
  "performance_metrics": {},
  "operational_optimization": {},
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
  "scalability_evolution": {},
  "performance_findings": [],
  "cost_findings": [],
  "scaling_recommendations": [],
  "scalability_risks": []
}
```

This skill contributes to:

```text
Build-Plans/Stage-8/05-scalability-evolution.json
```

---

# Feedback Routing Responsibilities

When scalability findings require work owned by an earlier stage, produce `feedback_route_candidates` with source signal IDs, severity, evidence references, recommended target stage, recommended action, and whether the route blocks current evolution.

Route examples:

* scale changes that alter MVP scope or workflow boundaries -> Stage 1
* scaling assumptions that need external validation -> Stage 2
* performance, capacity, infrastructure, data, AI cost, security, or integration architecture changes -> Stage 3
* scale-driven UI, navigation, loading, empty, error, or responsive behavior changes -> Stage 4
* execution sequencing, ticket, agent, or rollout plan changes -> Stage 5
* implementation repairs, regression fixes, or validation coverage gaps -> Stage 6
* monitoring, alerting, deployment, support, rollback, or runbook gaps -> Stage 7
