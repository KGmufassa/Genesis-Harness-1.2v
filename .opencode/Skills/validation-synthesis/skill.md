---
name: validation-synthesis
description: The validation-synthesis skill combines all Stage 2 validation intelligence into -
compatibility: opencode
---

# Skill — validation-synthesis

# Purpose

The `validation-synthesis` skill combines all Stage 2 validation intelligence into:

* validated product models
* confidence frameworks
* contradiction analysis
* risk-aware progression models
* architecture readiness assessments
* Stage 3 progression guidance

This skill is the final validation synthesis and progression intelligence engine for Stage 2.

---

# Inputs

```json
{
  "market_validation": {},
  "competitive_landscape": {},
  "user_validation": {},
  "technical_validation": {},
  "operational_validation": {},
  "business_validation": {},
  "scalability_analysis": {},
  "assumption_registry": [],
  "risk_registry": [],
  "contradictions": [],
  "existing_state": {}
}
```

---

# Evidence Quality Responsibilities

Before Stage 2 completion, synthesize evidence quality across all validated assumptions.

The synthesis must identify:

* evidence-backed findings
* inferences
* unsupported assumptions
* critical unknowns
* architecture-critical assumptions below evidence threshold

Stage 3 handoff must include evidence quality and confidence rationale for architecture-critical assumptions.

Read and update shared validation state from:

```text
Build-Plans/Build-status/Validation-state.json
```

---

# Core Responsibilities

## Confidence Modeling

Normalize:

* market confidence
* user confidence
* competitive confidence
* technical confidence
* operational confidence
* business confidence
* scalability confidence
* architecture readiness confidence

Every confidence score must include a rationale.

---

## Contradiction Detection

Identify:

* conflicting assumptions
* unsupported planning
* weak validation areas
* unresolved critical unknowns
* contradictions between market, technical, operational, and business findings

Critical open contradictions block Stage 3 progression.

---

## Recommendation Generation

Generate:

* validation recommendations
* architecture warnings
* strategic refinements
* mitigation paths
* progression guidance
* product revision guidance when validation fails

---

## Completion Determination

Determine:

* whether validation is sufficient
* whether architecture progression is safe
* whether critical unknowns remain
* whether the product needs revision before Stage 3
* whether `Build-Plans/Stage-2/00-stage-decision-brief.md` exists and is approved

---

# Interactive Guidance Responsibilities

This skill should not finalize Stage 2 if validation-critical questions remain unresolved.

Before writing final outputs, inspect:

```text
interactive_guidance.open_questions
interactive_guidance.blocked_decisions
interactive_guidance.validation_confidence_gaps
critical_unknowns
contradictions
risk_registry
assumption_registry
```

Classify unresolved guidance items as:

```text
safe_to_assume
needs_user_confirmation
blocks_stage_2_completion
```

Ask the minimum number of final questions needed to determine a reliable completion status.

Do not ask broad research or architecture questions at this stage. Only ask questions tied directly to:

* unresolved architecture-critical assumptions
* unresolved contradictions
* missing evidence for threshold confidence
* high or critical risks without mitigation
* critical unknowns that affect Stage 3 readiness
* final output fields that cannot be completed honestly
* unapproved Stage 2 decision brief

If proceeding with assumptions, record them in:

```text
interactive_guidance.assumptions_made
```

If Stage 2 cannot complete, set `completion_status` to one of:

```text
needs_more_validation
requires_product_revision
blocked
```

and return the specific questions or decisions required.

---

# Confidence Thresholds

Minimum readiness thresholds:

```json
{
  "market_confidence_min": 0.70,
  "technical_confidence_min": 0.75,
  "business_confidence_min": 0.65,
  "operational_confidence_min": 0.70,
  "architecture_readiness_min": 0.75
}
```

If any threshold is missed, Stage 2 cannot be marked `ready_for_stage_3`.

---

# Completion Gate

Stage 2 may complete only when:

* no critical assumptions remain `unknown`
* no architecture-critical assumptions are below threshold
* no unresolved contradictions remain
* all high-risk assumptions have mitigation paths
* architecture readiness status is `ready`
* Stage 2 decision brief exists and is approved

Possible completion statuses:

```text
ready_for_stage_3
needs_more_validation
requires_product_revision
blocked
```

Use `ready_for_stage_3` only when the product assumptions have been sufficiently validated for safe architectural progression and `stage_decision_brief.approval_status = approved`.

Before using `ready_for_stage_3`, this skill must generate or verify:

```text
Build-Plans/Stage-2/00-stage-decision-brief.md
```

If the decision brief is not approved, return the brief for user review instead of locking Stage 2.

---

# Final Stage 2 Outputs

Write or update:

```text
Build-Plans/Stage-2/01-market-analysis.json
Build-Plans/Stage-2/02-competitive-landscape.json
Build-Plans/Stage-2/03-technical-feasibility.json
Build-Plans/Stage-2/04-business-viability.json
Build-Plans/Stage-2/05-risk-validation.json
Build-Plans/Stage-2/06-strategic-positioning.json
```

Each output must include:

* related assumption IDs
* evidence
* evidence quality
* confidence score
* confidence rationale
* risks
* unresolved unknowns
* recommendations

---

# Output Responsibilities

## `01-market-analysis.json`

Include:

* market confidence
* demand validation
* audience viability
* user pain validation
* adoption likelihood
* market risks
* related assumption IDs

## `02-competitive-landscape.json`

Include:

* direct competitors
* indirect competitors
* existing alternatives
* saturation risk
* differentiation opportunities
* positioning gaps
* related assumption IDs

## `03-technical-feasibility.json`

Include:

* technical confidence
* AI feasibility
* infrastructure constraints
* integration feasibility
* operational feasibility
* scalability risks
* architecture warnings
* related assumption IDs

## `04-business-viability.json`

Include:

* business confidence
* monetization analysis
* pricing realism
* acquisition assumptions
* retention feasibility
* cost sustainability
* business constraints
* related assumption IDs

## `05-risk-validation.json`

Include:

* risk registry
* contradictions
* critical unknowns
* mitigation paths
* unresolved blockers
* Stage 3 carry-forward risks
* related assumption IDs

## `06-strategic-positioning.json`

Include:

* validated product model
* positioning analysis
* strategic differentiation
* architecture readiness
* validation recommendations
* progression guidance
* completion status
* related assumption IDs

---

# Outputs

```json
{
  "validated_product_model": {},
  "confidence_scores": {},
  "critical_unknowns": [],
  "architecture_readiness": {},
  "validation_recommendations": [],
  "completion_status": {}
}
```

Use the shared subskill output contract:

```json
{
  "validated_assumptions": [],
  "weakened_assumptions": [],
  "contradicted_assumptions": [],
  "unknown_assumptions": [],
  "critical_unknowns": [],
  "contradictions": [],
  "confidence_delta": {
    "architecture_readiness": 0.0
  },
  "evidence": [],
  "evidence_quality": "none",
  "risks": [],
  "recommendation": "continue"
}
```

---

# Shared State Updates

Update:

```text
validated_product_model
confidence_scores
critical_unknowns
architecture_readiness
completion_status
recommendations
contradictions
risk_registry
assumption_registry
interactive_guidance
```

Persist updates to:

```text
Build-Plans/Build-status/Validation-state.json
```

---

# Validation Checklist

Before marking Stage 2 complete, confirm:

* all Stage 1 assumptions were reviewed
* every high-risk assumption has a validation status
* every architecture-critical assumption has a confidence score
* every confidence score has a rationale
* every critical unknown has a next action
* every high or critical risk has a mitigation path
* every final output file references assumption IDs
* completion status follows the gate rules
* critical interactive guidance questions are answered or converted into recorded assumptions
* Stage 2 has not performed Stage 1 product structuring
* Stage 2 has not performed Stage 3 system design
