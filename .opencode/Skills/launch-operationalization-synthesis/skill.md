---
name: launch-operationalization-synthesis
description: The launch-operationalization-synthesis skill combines Stage 7 readiness, deployment, monitoring, analytics, and tooling work into a launch-ready operational package.
compatibility: opencode
---

# Skill — launch-operationalization-synthesis

# Purpose

The `launch-operationalization-synthesis` skill combines Stage 7 readiness, deployment, monitoring, analytics, and tooling work into a launch-ready operational package.

It determines whether Stage 7 can hand off to Stage 8.

---

# Core Responsibilities

## Operational Coherence

Verify:

* launch readiness gates are resolved or accepted
* deployment and rollback are defined
* monitoring covers launch-critical behavior
* analytics can measure success
* support and runbooks cover expected incidents
* operational blockers have owners and next actions
* launch-critical workflow evidence is present or explicitly accepted as launch risk
* dead controls and fixture-backed runtime dependencies are resolved before launch

## Stage 8 Handoff

Produce handoff data containing launch status, monitoring sources, analytics sources, support signals, incident signals, operational risks, and completion status.

## Completion Determination

Use one of:

```text
ready_for_stage_8
needs_launch_readiness_work
needs_operational_revision
blocked
```

Use `ready_for_stage_8` only after `global-stage-readiness-audit` passes.

---

# Inputs

```json
{
  "launch_readiness": {},
  "deployment_framework": {},
  "monitoring_systems": {},
  "analytics_framework": {},
  "operational_tooling": {},
  "existing_state": {}
}
```

---

# Deployment Proof Synthesis

Before Stage 7 can complete, synthesize deployment proof from launch readiness and deployment planning.

The synthesis must identify missing production build proof, deployment dry-run evidence, smoke test evidence, rollback verification, environment verification, monitoring alert proof, and accepted launch risk evidence.

Missing launch-critical proof must become a launch blocker unless explicitly accepted as known risk.

Missing launch-critical workflow evidence must also become a launch blocker.
Stage 7 may not convert `contract_only`, `api_exists_not_wired`,
`ui_wired_not_validated`, `runtime_persistence_failed`, unresolved dead-control,
or unresolved fixture-runtime findings into ready status without explicit risk
acceptance.

---

# Outputs

Write final Stage 7 outputs:

```text
Build-Plans/Stage-7/01-launch-readiness.json
Build-Plans/Stage-7/02-deployment-framework.json
Build-Plans/Stage-7/03-monitoring-systems.json
Build-Plans/Stage-7/04-analytics-framework.json
Build-Plans/Stage-7/05-operational-tooling.json
```

Update:

```text
Build-Plans/Build-status/Operationalization-state.json
```

with `stage_8_handoff`, `completion_status`, unresolved blockers, and launch risks.
