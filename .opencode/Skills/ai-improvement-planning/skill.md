---
name: ai-improvement-planning
description: The ai-improvement-planning skill evaluates AI quality signals and plans AI system improvements.
compatibility: opencode
---

# Skill — ai-improvement-planning

# Purpose

The `ai-improvement-planning` skill evaluates AI quality signals and plans AI system improvements.

It covers:

* model quality
* prompt quality
* evaluation gaps
* workflow fit
* data needs
* AI safety and reliability risks

---

# Core Responsibilities

## AI Quality Review

Analyze AI outputs, user feedback, validation failures, support issues, and quality metrics.

When AI behavior is exposed through planned UI interactions, map findings to the affected `UI-ELEMENT-`, `ROUTE-`, and `ACTION-` IDs and preserve related Stage 5 ticket and Stage 6 validation references.

## Improvement Planning

Recommend prompt changes, evaluation additions, data improvements, model changes, fallback behavior, or workflow refinements.

Do not recommend retraining or model replacement without evidence and risk rationale.

---

# Inputs

```json
{
  "telemetry_analysis": {},
  "user_feedback": {},
  "ai_quality_reports": {},
  "validation_results": {},
  "support_signals": {},
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
  "ai_improvement_plan": {},
  "quality_gaps": [],
  "training_or_prompt_needs": [],
  "evaluation_needs": [],
  "interaction_findings": [],
  "ai_risks": []
}
```

This skill contributes to:

```text
Build-Plans/Stage-8/03-ai-improvement-plan.json
```

---

# Feedback Routing Responsibilities

When AI quality findings indicate that the root issue belongs to an earlier stage, produce `feedback_route_candidates` instead of treating the issue only as a Stage 8 AI optimization.

Route examples:

* AI behavior does not fit the intended product outcome -> Stage 1
* AI assumptions were not sufficiently validated -> Stage 2
* AI endpoint, data, security, infrastructure, or integration constraints are architectural -> Stage 3
* AI interaction, explanation, error, loading, or recovery behavior is confusing -> Stage 4
* AI work was under-scoped or incorrectly sequenced in build tickets -> Stage 5
* AI defects, regressions, missing tests, or validation gaps remain -> Stage 6
* AI monitoring, support, abuse handling, or production operations are insufficient -> Stage 7

Each route candidate must include source signal IDs, affected interaction IDs and downstream ticket or validation references when applicable, severity, evidence references, recommended target stage, recommended action, and whether it blocks current evolution.
