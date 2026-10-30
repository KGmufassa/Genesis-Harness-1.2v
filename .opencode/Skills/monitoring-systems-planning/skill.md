---
name: monitoring-systems-planning
description: The monitoring-systems-planning skill defines the operational monitoring model for production.
compatibility: opencode
---

# Skill — monitoring-systems-planning

# Purpose

The `monitoring-systems-planning` skill defines the operational monitoring model for production.

It plans:

* health checks
* logs
* alerts
* uptime checks
* incident triggers
* monitoring risks

---

# Core Responsibilities

## Monitoring Model

Define:

* system health signals
* application logs
* error tracking needs
* uptime checks
* performance checks
* dependency checks

## Alerting And Incident Triggers

Define alert conditions, severity, owners, expected response, and escalation path.

## Coverage Gaps

Identify launch-critical behavior that cannot be monitored yet and record it as a risk or setup action.

---

# Inputs

```json
{
  "launch_readiness": {},
  "deployment_framework": {},
  "system_health": {},
  "validation_results": {},
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
  "monitoring_systems": {},
  "alerts": [],
  "health_checks": [],
  "incident_triggers": [],
  "monitoring_risks": []
}
```

This skill contributes to:

```text
Build-Plans/Stage-7/03-monitoring-systems.json
```

