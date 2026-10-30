---
name: analytics-framework-planning
description: The analytics-framework-planning skill defines how product success and user behavior will be measured after launch.
compatibility: opencode
---

# Skill — analytics-framework-planning

# Purpose

The `analytics-framework-planning` skill defines how product success and user behavior will be measured after launch.

It plans:

* analytics events
* product metrics
* activation metrics
* retention metrics
* dashboards
* analytics risks

---

# Core Responsibilities

## Event Model

Define user, system, and business events needed to measure the Stage 1 success framework and Stage 7 launch outcomes.

## Metrics Model

Define:

* activation metrics
* retention metrics
* usage metrics
* conversion metrics
* reliability metrics
* product success metrics

## Dashboard And Evidence Plan

Identify dashboard needs, data sources, missing instrumentation, and evidence quality limitations.

---

# Inputs

```json
{
  "success_framework": {},
  "launch_readiness": {},
  "monitoring_systems": {},
  "product_model": {},
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
  "analytics_framework": {},
  "events": [],
  "metrics": [],
  "dashboards": [],
  "analytics_risks": []
}
```

This skill contributes to:

```text
Build-Plans/Stage-7/04-analytics-framework.json
```

