---
name: market-and-competitive-validation
description: The market-and-competitive-validation skill validates -
compatibility: opencode
---

# Skill — market-and-competitive-validation

# Purpose

The `market-and-competitive-validation` skill validates:

* market demand
* audience viability
* user pain validity
* workflow realism
* competitive landscape
* differentiation viability
* positioning opportunities

This skill is the market intelligence and competitive validation engine for Stage 2.

---

# Inputs

```json
{
  "assumptions": {},
  "product_identity": {},
  "user_profiles": {},
  "workflows": {},
  "existing_state": {}
}
```

---

# Evidence Quality Responsibilities

Market and competitive findings must record source type, freshness, evidence quality, confidence delta, inference status, limitations, and whether external research is still required.

Low-evidence positioning or demand claims must be marked provisional.

Read and update shared validation state from:

```text
Build-Plans/Build-status/Validation-state.json
```

---

# Core Responsibilities

## Market Validation

Determine:

* demand strength
* audience viability
* market timing
* market maturity
* adoption likelihood

## Competitive Analysis

Identify:

* direct competitors
* indirect competitors
* existing alternatives
* saturation risk
* differentiation opportunities
* switching barriers

## User Validation

Validate:

* user pain realism
* workflow realism
* habit-change difficulty
* user motivation strength
* willingness to adopt

## Positioning Analysis

Determine:

* product positioning
* category alignment
* strategic differentiation
* competitive advantages
* weak positioning claims

---

# Interactive Guidance Responsibilities

This skill should guide the user through validation gaps that affect market, user, competitor, or positioning confidence.

Ask targeted questions when any of these are unclear:

* target market or audience segment
* primary user pain
* existing alternatives users rely on
* direct or indirect competitors
* differentiation claim
* adoption barrier
* willingness-to-pay signal
* positioning category

Ask no more than 1-3 market validation questions at once.

Infer low-risk market or competitor assumptions only when Stage 1 and available evidence strongly support them, but record them in:

```text
interactive_guidance.assumptions_made
```

Pause for user input when:

* the target audience is too broad or ambiguous
* competitor category is unclear
* differentiation cannot be validated
* user pain is weak or unsupported
* market confidence cannot reach threshold without user-provided evidence

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

When external research is unavailable, record the limitation as a critical unknown or validation recommendation.

When external sources are used, include source links in `evidence`.

Low-evidence recommendations must be marked provisional.

---

# Outputs

```json
{
  "market_confidence": 0.0,
  "competitive_landscape": {},
  "user_validation": {},
  "positioning_analysis": {},
  "market_risks": []
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
    "market": 0.0,
    "user": 0.0,
    "competitive": 0.0
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
market_validation
competitive_landscape
user_validation
confidence_scores
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

For every market, user, or competitive assumption reviewed:

* update its status
* add evidence or mark evidence gap
* update confidence
* add contradiction IDs when needed
* set next action

Do not produce isolated findings that are disconnected from assumption IDs.

---

# Risk Detection

Record risks for:

* weak demand
* narrow audience
* crowded market
* unclear differentiation
* difficult habit change
* low willingness to pay
* unsupported positioning claims
