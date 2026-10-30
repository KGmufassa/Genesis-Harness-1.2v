---
name: operational-tooling-planning
description: The operational-tooling-planning skill defines the operational tools and support workflows needed after launch.
compatibility: opencode
---

# Skill — operational-tooling-planning

# Purpose

The `operational-tooling-planning` skill defines the operational tools and support workflows needed after launch.

It plans:

* admin tools
* support workflows
* review or moderation workflows
* operational dashboards
* runbooks
* ticket triage rules

---

# Core Responsibilities

## Support Model

Define support flows, issue categories, escalation paths, triage rules, and operational owners.

## Admin And Operational Tools

Identify required tooling for user support, monitoring, data review, moderation, configuration, and incident handling.

## Runbooks

Create runbook outlines for launch-critical operational scenarios and known failure modes.

---

# Inputs

```json
{
  "launch_readiness": {},
  "deployment_framework": {},
  "monitoring_systems": {},
  "analytics_framework": {},
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
  "operational_tooling": {},
  "support_model": {},
  "runbooks": [],
  "admin_tools": [],
  "tooling_risks": []
}
```

This skill contributes to:

```text
Build-Plans/Stage-7/05-operational-tooling.json
```

