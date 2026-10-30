---
name: telemetry-analysis
description: The telemetry-analysis skill analyzes live product signals after launch.
compatibility: opencode
---

# Skill — telemetry-analysis

# Purpose

The `telemetry-analysis` skill analyzes live product signals after launch.

It identifies:

* usage patterns
* activation signals
* retention signals
* friction points
* success signals
* telemetry gaps

---

# Core Responsibilities

## Signal Review

Review telemetry, analytics, monitoring, support, incident, and user feedback data.

Distinguish evidence from inference. If signals are missing, mark findings as provisional and record the telemetry gap.

## Behavior Analysis

Identify behavior patterns that support, weaken, or contradict the Stage 1 success framework and Stage 7 launch expectations.

Map interaction signals to stable `UI-ELEMENT-`, `ROUTE-`, and `ACTION-` IDs. Preserve related Stage 5 ticket and Stage 6 validation references so findings identify the planned interaction, implementation work, and prior validation evidence. Mark telemetry that cannot be mapped as an instrumentation gap.

---

# Inputs

```json
{
  "stage_7_handoff": {},
  "telemetry_data": {},
  "analytics_data": {},
  "support_signals": {},
  "incident_signals": {},
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
  "telemetry_analysis": {},
  "usage_patterns": [],
  "interaction_signal_map": [],
  "ui_element_findings": [],
  "route_findings": [],
  "action_findings": [],
  "friction_points": [],
  "success_signals": [],
  "telemetry_gaps": []
}
```

This skill contributes to:

```text
Build-Plans/Stage-8/01-telemetry-analysis.json
```

---

# Feedback Routing Responsibilities

When telemetry reveals a problem that belongs to an earlier stage, produce `feedback_route_candidates` instead of absorbing the issue only as Stage 8 optimization.

Route examples:

* unclear user value, abandoned workflow, or wrong target user -> Stage 1
* weak demand, positioning mismatch, or invalid assumption -> Stage 2
* performance, scale, integration, or security architecture issue -> Stage 3
* confusing navigation, poor screen flow, poor layout pattern fit, component-family mismatch, or visual mismatch -> Stage 4
* ticket sequencing, agent assignment, or rollout planning issue -> Stage 5
* defects, regressions, or validation gaps -> Stage 6
* deployment, monitoring, onboarding, support, or launch-readiness issue -> Stage 7

Each route candidate must include source signal IDs, affected `UI-ELEMENT-`, `ROUTE-`, and `ACTION-` IDs when applicable, related Stage 5 ticket and Stage 6 validation references, severity, evidence references, recommended target stage, recommended action, and whether it blocks current evolution.
