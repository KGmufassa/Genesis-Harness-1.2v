---
name: roadmap-evolution-planning
description: The roadmap-evolution-planning skill evolves the roadmap using post-launch evidence.
compatibility: opencode
---

# Skill — roadmap-evolution-planning

# Purpose

The `roadmap-evolution-planning` skill evolves the roadmap using post-launch evidence.

It decides whether to:

* expand
* simplify
* refine
* defer
* revisit earlier-stage assumptions

---

# Core Responsibilities

## Evidence-Based Roadmap Review

Compare telemetry, success signals, user feedback, support signals, operational findings, and AI quality findings against original product assumptions.

## Prioritization

Prioritize improvements by evidence strength, user impact, business impact, operational burden, implementation complexity, and risk.

## Prior-Stage Feedback

Route changes back to the correct earlier stage when the finding changes product, validation, architecture, UX, development, implementation, or operational assumptions.

---

# Inputs

```json
{
  "telemetry_analysis": {},
  "operational_optimization": {},
  "ai_improvement_plan": {},
  "user_feedback": {},
  "prior_stage_outputs": {},
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
  "roadmap_evolution": {},
  "new_opportunities": [],
  "deferred_items_to_revisit": [],
  "roadmap_risks": []
}
```

This skill contributes to:

```text
Build-Plans/Stage-8/04-roadmap-evolution.json
```

---

# Feedback Routing Responsibilities

When roadmap findings require work owned by an earlier stage, produce `feedback_route_candidates` with source signal IDs, severity, evidence references, recommended target stage, recommended action, and whether the route blocks current evolution.

Route examples:

* product scope, user, workflow, or MVP boundary changes -> Stage 1
* assumption, demand, market, or business validation changes -> Stage 2
* architecture, data, integration, security, or infrastructure changes -> Stage 3
* UX, UI blueprint, navigation, visual specification, accessibility, or state changes -> Stage 4
* slicing, ticketing, sequencing, agent, or release planning changes -> Stage 5
* implementation defect, regression, repair, or validation changes -> Stage 6
* deployment, monitoring, onboarding, support, analytics, or launch operation changes -> Stage 7
