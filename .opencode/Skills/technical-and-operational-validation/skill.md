---
name: technical-and-operational-validation
description: The technical-and-operational-validation skill validates -
compatibility: opencode
---

# Skill — technical-and-operational-validation

# Purpose

The `technical-and-operational-validation` skill validates:

* technical feasibility
* implementation realism
* AI capability realism
* integration feasibility
* infrastructure sustainability
* operational scalability
* support burden

This skill is the technical feasibility and operational validation engine for Stage 2.

---

# Inputs

```json
{
  "assumptions": {},
  "workflows": {},
  "capabilities": {},
  "dependencies": {},
  "mvp_scope": {},
  "existing_state": {}
}
```

---

# Evidence Quality Responsibilities

Technical and operational findings must record source type, evidence quality, confidence delta, inference status, limitations, and whether implementation proof or external validation is required.

Architecture-critical technical assumptions require medium or high evidence quality or must be carried as Stage 3 risks.

Read and update shared validation state from:

```text
Build-Plans/Build-status/Validation-state.json
```

---

# Core Responsibilities

## Technical Feasibility

Validate:

* implementation realism
* AI capability assumptions
* integration viability
* infrastructure complexity
* data handling realism
* reliability expectations

## Operational Validation

Validate:

* workflow scalability
* operational sustainability
* support burden
* moderation or review needs
* execution feasibility
* manual workaround viability

## Architecture Risk Detection

Identify:

* scalability bottlenecks
* infrastructure weaknesses
* fragile dependencies
* operational complexity risks
* AI reliability risks
* compliance-sensitive technical risks

## Infrastructure Validation

Determine:

* hosting viability
* scaling requirements
* orchestration feasibility
* storage and queueing needs
* integration constraints
* monitoring needs

---

# Interactive Guidance Responsibilities

This skill should guide the user through validation gaps that affect technical feasibility, operational sustainability, AI realism, integrations, or scalability.

Ask targeted questions when any of these are unclear:

* AI capability expectations
* data volume or file/media handling needs
* required integrations
* synchronous vs asynchronous processing expectations
* moderation or human review requirements
* operational support expectations
* reliability requirements
* infrastructure constraints
* compliance-sensitive technical requirements

Ask no more than 1-3 technical or operational validation questions at once.

Infer low-risk technical assumptions when the workflow and dependencies make the architecture implication obvious, but record them in:

```text
interactive_guidance.assumptions_made
```

Pause for user input when:

* technical feasibility depends on an unknown external API or platform
* AI capability realism is uncertain
* operational support burden could change MVP viability
* integration feasibility is required but unverified
* infrastructure cost or scale risk could block Stage 3 readiness
* sensitive data handling affects technical feasibility

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

When technical feasibility requires external documentation or platform verification and that research is unavailable, record the unknown explicitly.

Low-evidence technical recommendations must be marked provisional.

---

# Outputs

```json
{
  "technical_confidence": 0.0,
  "operational_confidence": 0.0,
  "technical_risks": [],
  "scalability_risks": [],
  "infrastructure_constraints": []
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
    "technical": 0.0,
    "operational": 0.0,
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
technical_validation
operational_validation
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

For every technical, operational, scalability, AI, integration, infrastructure, or compliance-sensitive assumption reviewed:

* update its status
* add evidence or mark evidence gap
* update confidence
* add contradiction IDs when needed
* set next action

Do not produce isolated findings that are disconnected from assumption IDs.

---

# Risk Detection

Record risks for:

* unverified AI capability
* unclear data pipeline
* fragile third-party dependency
* excessive infrastructure complexity
* high support burden
* scaling bottleneck
* unclear moderation responsibility
* security or compliance exposure
