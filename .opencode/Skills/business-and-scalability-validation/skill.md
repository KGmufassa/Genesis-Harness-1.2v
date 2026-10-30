---
name: business-and-scalability-validation
description: The business-and-scalability-validation skill validates -
compatibility: opencode
---

# Skill — business-and-scalability-validation

# Purpose

The `business-and-scalability-validation` skill validates:

* monetization viability
* pricing realism
* business sustainability
* customer acquisition assumptions
* retention feasibility
* AI and infrastructure cost sustainability
* operational scalability

This skill is the business viability and scalability intelligence engine for Stage 2.

---

# Inputs

```json
{
  "assumptions": {},
  "market_validation": {},
  "technical_validation": {},
  "operational_validation": {},
  "mvp_scope": {},
  "existing_state": {}
}
```

---

# Evidence Quality Responsibilities

Business, monetization, growth, and scalability findings must record source type, freshness, evidence quality, confidence delta, inference status, limitations, and external research needs.

Low-evidence revenue, pricing, CAC, retention, or scaling claims must be marked provisional.

Read and update shared validation state from:

```text
Build-Plans/Build-status/Validation-state.json
```

---

# Core Responsibilities

## Monetization Validation

Determine:

* pricing realism
* payment willingness
* revenue sustainability
* monetization feasibility
* margin pressure

## Growth Validation

Validate:

* growth assumptions
* customer acquisition viability
* retention feasibility
* adoption scalability
* go-to-market assumptions

## Scalability Validation

Determine:

* AI cost sustainability
* infrastructure cost growth
* support scalability
* operational scalability
* dependency cost exposure

## Business Risk Detection

Identify:

* CAC risks
* retention risks
* pricing risks
* margin risks
* dependency risks
* growth bottlenecks

---

# Interactive Guidance Responsibilities

This skill should guide the user through validation gaps that affect business viability, monetization, growth, cost, or scalability confidence.

Ask targeted questions when any of these are unclear:

* monetization model
* pricing expectation
* willingness-to-pay evidence
* buyer vs user distinction
* customer acquisition path
* retention mechanism
* AI or infrastructure cost tolerance
* manual support limits
* growth assumptions

Ask no more than 1-3 business validation questions at once.

Infer low-risk business assumptions only when Stage 1 outputs and Stage 2 market/technical findings support them, but record them in:

```text
interactive_guidance.assumptions_made
```

Pause for user input when:

* monetization is required but undefined
* pricing or payment willingness drives viability
* cost sustainability is uncertain
* acquisition or retention assumptions are unsupported
* scalability economics could block Stage 3 readiness
* business confidence cannot reach threshold without user-provided constraints or evidence

Update:

```text
interactive_guidance.open_questions
interactive_guidance.answered_questions
interactive_guidance.assumptions_made
interactive_guidance.blocked_decisions
interactive_guidance.validation_confidence_gaps
```

---

# Evidence Rules

Separate:

```text
evidence
inference
assumption
recommendation
```

When pricing, acquisition, retention, or unit economics require external validation and that research is unavailable, record the unknown explicitly.

Low-evidence business recommendations must be marked provisional.

---

# Outputs

```json
{
  "business_confidence": 0.0,
  "monetization_analysis": {},
  "growth_risks": [],
  "scalability_analysis": {},
  "business_constraints": []
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
    "business": 0.0,
    "scalability": 0.0
  },
  "evidence": [],
  "evidence_quality": "none",
  "risks": [],
  "recommendation": "continue"
}
```

Allowed recommendations:

```text
continue
revise
block
```

---

# Shared State Updates

Update:

```text
business_validation
scalability_analysis
confidence_scores
critical_unknowns
contradictions
risk_registry
recommendations
assumption_registry
interactive_guidance
```

Persist updates to:

```text
Build-Plans/Build-status/Validation-state.json
```

---

# Assumption Registry Behavior

For every business, monetization, growth, scalability, pricing, retention, acquisition, or cost assumption reviewed:

* update its status
* add evidence or mark evidence gap
* update confidence
* add contradiction IDs when needed
* set next action

Do not produce isolated findings that are disconnected from assumption IDs.

---

# Risk Detection

Record risks for:

* weak monetization logic
* unsupported pricing
* unclear willingness to pay
* unsustainable AI costs
* expensive infrastructure growth
* high customer acquisition cost
* weak retention mechanism
* operational support growth
