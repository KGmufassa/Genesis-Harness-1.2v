---
name: assumption-analysis
description: The assumption-analysis skill extracts and prioritizes assumptions from Stage 1 outputs.
compatibility: opencode
---

# Skill — assumption-analysis

# Purpose

The `assumption-analysis` skill extracts and prioritizes assumptions from Stage 1 outputs.

It transforms:

* product foundation
* user-system map
* workflow architecture
* capabilities
* feature structure
* dependency map
* MVP operational model
* risk and constraints
* success framework

into:

* explicit assumptions
* implicit assumptions
* validation targets
* architecture-critical assumptions
* confidence gaps
* the initial assumption registry

This skill is the assumption extraction and validation targeting engine for Stage 2.

---

# Inputs

```json
{
  "stage_1_outputs": {},
  "existing_state": {}
}
```

---

# Evidence Quality Responsibilities

When extracting assumptions, initialize evidence metadata with:

```text
source_type
freshness
evidence_quality
is_inference
requires_external_research
```

Do not mark inferred assumptions as validated. Mark them as `unvalidated` or `unknown` until a validation skill attaches evidence.

Read Stage 1 outputs from:

```text
Build-Plans/Stage-1/
```

Read and update shared validation state from:

```text
Build-Plans/Build-status/Validation-state.json
```

---

# Core Responsibilities

## Assumption Extraction

Identify assumptions across these domains:

* user
* market
* technical
* business
* operational
* scalability
* compliance

Extract explicit assumptions directly stated in Stage 1 outputs.

Infer implicit assumptions from:

* workflows
* capabilities
* dependencies
* risks
* MVP scope
* implementation phases
* success criteria
* confidence gaps

---

## Assumption Classification

Classify each assumption by:

* domain
* source Stage 1 file
* explicit or implicit status
* risk if false
* architecture criticality
* current confidence
* validation priority

---

## Risk Prioritization

Prioritize assumptions when they are:

* high risk if false
* low confidence
* architecture critical
* tied to MVP viability
* tied to AI feasibility
* tied to monetization
* tied to compliance or sensitive data
* required before Stage 3 architecture

---

# Interactive Guidance Responsibilities

This skill should guide the user only when assumptions cannot be extracted, classified, or prioritized with enough confidence.

Ask targeted questions when any of these are unclear:

* whether an assumption is explicit or implicit
* whether an assumption is architecture-critical
* which user, market, technical, business, operational, scalability, or compliance domain owns the assumption
* what risk level applies if the assumption is false
* whether a Stage 1 gap should become a validation target
* which assumptions should be validated before architecture

Ask no more than 1-3 assumption questions at once.

Infer low-risk assumption classifications when Stage 1 outputs make the answer obvious, but record them in:

```text
interactive_guidance.assumptions_made
```

Pause for user input when:

* a core assumption cannot be classified
* architecture-critical status is ambiguous
* risk-if-false is potentially high or critical
* assumption priority changes the validation sequence
* missing Stage 1 context prevents reliable assumption extraction

Update:

```text
interactive_guidance.open_questions
interactive_guidance.answered_questions
interactive_guidance.assumptions_made
interactive_guidance.blocked_decisions
interactive_guidance.validation_confidence_gaps
```

---

# Assumption Registry Contract

Every assumption must use this structure:

```json
{
  "id": "A-001",
  "assumption": "",
  "domain": "",
  "source_stage_1_file": "",
  "explicit_or_implicit": "",
  "risk_if_false": "low",
  "architecture_critical": false,
  "status": "unvalidated",
  "confidence": 0.3,
  "evidence": [],
  "evidence_quality": "none",
  "contradictions": [],
  "next_action": ""
}
```

Allowed statuses:

```text
unvalidated
validated
weakened
contradicted
unknown
```

Allowed evidence quality values:

```text
none
low
medium
high
```

---

# Outputs

```json
{
  "assumptions": [],
  "validation_targets": [],
  "high_risk_assumptions": [],
  "confidence_gaps": [],
  "assumption_registry": []
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
  "confidence_delta": {},
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
assumptions
validation_targets
assumption_registry
confidence_scores
critical_unknowns
recommendations
interactive_guidance
```

Persist updates to:

```text
Build-Plans/Build-status/Validation-state.json
```

---

# Validation Targeting Rules

Set `validation_targets` from assumptions that are:

* `architecture_critical = true`
* `risk_if_false = high`
* `risk_if_false = critical`
* `confidence < 0.60`
* needed to validate market demand
* needed to validate technical feasibility
* needed to validate business viability
* needed to validate operational scalability

---

# Example Behavior

Product statement:

```text
Users can generate AI schedules.
```

Extracted assumptions:

```text
A-001 users trust AI-generated schedules
A-002 schedules improve user outcomes
A-003 users provide enough data for schedule generation
A-004 AI generation is technically feasible
A-005 generated schedules can be operationally reviewed or corrected
A-006 scheduling workflows scale without excessive support burden
```
