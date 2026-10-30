---
name: post-launch-evolution-synthesis
description: The post-launch-evolution-synthesis skill combines Stage 8 findings into a coherent evolution plan.
compatibility: opencode
---

# Skill — post-launch-evolution-synthesis

# Purpose

The `post-launch-evolution-synthesis` skill combines Stage 8 findings into a coherent evolution plan.

It synthesizes:

* telemetry analysis
* operational optimization
* AI improvement planning
* roadmap evolution
* scalability evolution

---

# Core Responsibilities

## Evidence Coherence

Verify:

* findings distinguish evidence from inference
* low-evidence recommendations are marked provisional
* missing telemetry is recorded
* risks are routed to the correct owner stage
* roadmap changes are justified by post-launch signals

## Evolution Plan

Produce a prioritized plan with owner stage, action type, evidence quality, expected impact, risk, and next action.

## Completion Determination

Use one of:

```text
evolution_plan_ready
needs_more_telemetry
needs_operational_review
blocked
```

Use `evolution_plan_ready` only after `global-stage-readiness-audit` passes.

---

# Inputs

```json
{
  "telemetry_analysis": {},
  "operational_optimization": {},
  "ai_improvement_plan": {},
  "roadmap_evolution": {},
  "scalability_evolution": {},
  "existing_state": {}
}
```

---

# Feedback Routing Responsibilities

Synthesize telemetry, operational, AI, roadmap, and scalability findings into feedback routes when live signals reveal issues owned by earlier stages.

Every critical feedback route must include evidence refs, target stage, severity, recommended action, and ownership or next action.

---

# Outputs

Write final Stage 8 outputs:

```text
Build-Plans/Stage-8/01-telemetry-analysis.json
Build-Plans/Stage-8/02-operational-optimization.json
Build-Plans/Stage-8/03-ai-improvement-plan.json
Build-Plans/Stage-8/04-roadmap-evolution.json
Build-Plans/Stage-8/05-scalability-evolution.json
```

Update:

```text
Build-Plans/Build-status/Evolution-state.json
```

with `completion_status`, prioritized evolution actions, routed prior-stage feedback, unresolved telemetry gaps, and remaining risks.
