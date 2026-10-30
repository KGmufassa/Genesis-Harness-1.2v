---
name: stage-2-research-and-validation
description: The stage-2-research-and-validation command orchestrates Stage 2.
compatibility: opencode
---

# Command — stage-2-research-and-validation

# Purpose

The `stage-2-research-and-validation` command orchestrates Stage 2.

It transforms:

* Stage 1 product outputs
* product assumptions
* inferred workflows
* operational hypotheses

into:

* validated product intelligence
* evidence-backed feasibility analysis
* risk-aware product models
* architecture readiness confidence
* progression guidance for Stage 3

This is the Stage 2 command skill. It is not a single validation subskill.

---

# Cognitive Boundary

Stage 2 asks:

```text
Do the assumptions behind this product survive reality?
```

Stage 2 must not perform Stage 1 product structuring or Stage 3 system design. It validates whether the Stage 1 product model is safe to pass into architecture.

---

# Output Directory

All final Stage 2 outputs must be recorded in:

```text
Build-Plans/Stage-2/
```

The command must create this folder if it does not exist.

---

# Shared Validation State

The command maintains a shared Stage 2 validation state object.

The shared validation state must be written to:

```text
Build-Plans/Build-status/Validation-state.json
```

The command must load this file at the beginning of Stage 2, update it after each validation skill runs, and preserve it as the durable validation state for the build.

```json
{
  "stage": "Stage 2",
  "command": "stage-2-research-and-validation",
  "status": "not_started",
  "stage_1_inputs": {},
  "preflight": {},
  "assumptions": [],
  "validation_targets": [],
  "assumption_registry": [],
  "confidence_scores": {
    "market": 0.0,
    "user": 0.0,
    "competitive": 0.0,
    "technical": 0.0,
    "operational": 0.0,
    "business": 0.0,
    "scalability": 0.0,
    "architecture_readiness": 0.0
  },
  "market_validation": {},
  "competitive_landscape": {},
  "user_validation": {},
  "technical_validation": {},
  "operational_validation": {},
  "business_validation": {},
  "scalability_analysis": {},
  "critical_unknowns": [],
  "contradictions": [],
  "risk_registry": [],
  "recommendations": [],
  "interactive_guidance": {
    "open_questions": [],
    "answered_questions": [],
    "assumptions_made": [],
    "blocked_decisions": [],
    "user_confirmations": [],
    "validation_confidence_gaps": []
  },
  "architecture_readiness": {},
  "completion_status": {}
}
```

---

# A-Grade Workflow Compliance

Stage 2 must consume `stage_contract_profile` and `guidance_policy`.

Stage 2 must reference:

```text
System-References/Schemas/stage-2-output.schema.json
```

Stage 2 evidence findings should create or reference artifacts in:

```text
Build-Plans/Build-status/Artifact-evidence-registry.json
```

Architecture-critical assumptions require evidence quality of `medium` or higher unless explicitly accepted as risk.

Before using `ready_for_stage_3`, Stage 2 must provide `schema_validation`, `reference_integrity`, `risk_acceptance_ledger`, and `revision_loops` in the readiness audit or stage state.

Accepted high and critical validation risks must be recorded in:

```text
Build-Plans/Build-status/Risk-acceptance-ledger.json
```

Failed readiness checks must become revision-loop actions with owning output, owning skill, required change, and next action.

Stage 2 evidence entries must distinguish:

```text
evidence-backed finding
inference
unsupported assumption
critical unknown
```

Each evidence entry must include source type, freshness, evidence quality, confidence effect, confidence delta, inference flag, limitations, and external research needs.

Each subskill reads the current validation state and writes its updates back into the shared state before the next skill runs.

After each subskill completes, the command must persist the updated shared state to:

```text
Build-Plans/Build-status/Validation-state.json
```

---

# Interactive Guidance Rules

The Stage 2 command should behave like a guided validation interview.

Use this decision rule:

```text
Ask only for validation decisions that materially affect confidence, evidence quality, or architecture readiness.
Infer low-risk validation assumptions when Stage 1 and Stage 2 evidence support the inference.
Record assumptions when proceeding without user confirmation.
Block only when a missing answer prevents trustworthy validation or safe Stage 3 progression.
```

When asking the user questions:

* ask 1-3 questions at a time
* prioritize architecture-critical validation gaps first
* avoid asking questions already answered by Stage 1 outputs
* explain what assumption, risk, or confidence score each question affects
* prefer concrete choices when the tradeoff is known
* update `interactive_guidance.open_questions`
* move answered questions into `interactive_guidance.answered_questions`
* record inferred defaults in `interactive_guidance.assumptions_made`
* record unresolved blockers in `interactive_guidance.blocked_decisions`
* record weak-confidence areas in `interactive_guidance.validation_confidence_gaps`

The command should continue automatically when a validation gap is low-risk and can be marked as an assumption.

The command should pause for user input when:

* the product's target market or user segment is ambiguous
* a core assumption cannot be classified or prioritized
* evidence is too weak for an architecture-critical assumption
* a technical feasibility decision depends on an unknown constraint
* monetization or cost assumptions materially affect viability
* a contradiction cannot be resolved through evidence or mitigation
* Stage 3 readiness depends on an unresolved critical unknown

The command should not ask the user to make architecture decisions that belong to Stage 3. It may ask only for validation facts, constraints, evidence, or priority decisions needed to validate readiness.

---

# Stage 2 Input Contract

Load Stage 1 outputs from:

```text
Build-Plans/Stage-1/
```

Required Stage 1 files:

```text
01-product-foundation.json
02-user-system-map.json
03-workflow-architecture.json
04-product-capabilities.json
05-feature-structure.json
06-product-boundaries.json
07-dependency-map.json
08-mvp-operational-model.json
09-risk-and-constraints.json
10-success-framework.json
```

Minimum viable input set:

```text
01-product-foundation.json
02-user-system-map.json
03-workflow-architecture.json
07-dependency-map.json
08-mvp-operational-model.json
09-risk-and-constraints.json
10-success-framework.json
```

If required files are missing but the minimum viable input set exists, continue and record missing files in `preflight.missing_stage_1_files`.

If the minimum viable input set is missing, stop and set:

```text
completion_status.status = "blocked"
completion_status.reason = "missing_stage_1_foundation"
```

---

# Preflight Validation

Before assumption extraction, validate:

* Stage 1 output directory exists
* minimum viable Stage 1 inputs exist
* Stage 1 files are readable
* Stage 1 outputs contain enough content to extract assumptions
* Stage 1 completion status does not explicitly block validation

Record preflight results in:

```text
preflight
critical_unknowns
recommendations
interactive_guidance
```

---

# Orchestrated Skills

Run Stage 2 skills in this order:

```text
1. assumption-analysis
2. market-and-competitive-validation
3. technical-and-operational-validation
4. business-and-scalability-validation
5. validation-synthesis
```

---

# Execution Sequence

## 1. Load Stage 1 Outputs

Load the required Stage 1 files from `Build-Plans/Stage-1/`.

Normalize them into:

```text
stage_1_inputs
```

Do not modify Stage 1 outputs during Stage 2.

---

## 2. Initialize Shared Validation State

Create or load:

```text
Build-Plans/Build-status/Validation-state.json
```

Initialize missing fields using the shared validation state schema.

---

## 3. Run `assumption-analysis`

Purpose:

* extract explicit assumptions
* infer implicit assumptions
* classify assumptions by domain
* identify high-risk assumptions
* identify architecture-critical assumptions
* populate the assumption registry
* prioritize validation targets

Required shared state updates:

```text
assumptions
validation_targets
assumption_registry
confidence_scores
critical_unknowns
interactive_guidance
```

Interactive focus:

```text
Guide the user to clarify, prioritize, or confirm assumptions that are architecture-critical, high-risk, or too ambiguous to validate.
```

---

## 4. Run `market-and-competitive-validation`

Purpose:

* validate market demand
* validate user pain and workflow realism
* analyze direct and indirect competitors
* identify saturation and differentiation risks
* assess positioning opportunities

Required shared state updates:

```text
market_validation
competitive_landscape
user_validation
confidence_scores
contradictions
risk_registry
recommendations
interactive_guidance
```

Interactive focus:

```text
Guide the user through market, competitor, user pain, adoption, and positioning questions that materially affect validation confidence.
```

---

## 5. Run `technical-and-operational-validation`

Purpose:

* validate technical feasibility
* validate AI capability assumptions
* validate integration feasibility
* validate infrastructure realism
* detect operational complexity and scalability risks

Required shared state updates:

```text
technical_validation
operational_validation
scalability_analysis
confidence_scores
contradictions
risk_registry
recommendations
interactive_guidance
```

Interactive focus:

```text
Guide the user through technical, operational, AI, infrastructure, integration, and scalability constraints that materially affect feasibility confidence.
```

---

## 6. Run `business-and-scalability-validation`

Purpose:

* validate monetization assumptions
* validate pricing realism
* assess acquisition and retention assumptions
* analyze AI and infrastructure cost sustainability
* identify growth bottlenecks

Required shared state updates:

```text
business_validation
scalability_analysis
confidence_scores
contradictions
risk_registry
recommendations
interactive_guidance
```

Interactive focus:

```text
Guide the user through monetization, pricing, acquisition, retention, cost, and growth assumptions that materially affect business viability.
```

---

## 7. Run `validation-synthesis`

Purpose:

* combine validation results
* normalize confidence scores
* detect unresolved contradictions
* identify remaining critical unknowns
* generate architecture readiness assessment
* determine completion status
* produce Stage 3 progression guidance

Required shared state updates:

```text
validated_product_model
confidence_scores
critical_unknowns
architecture_readiness
completion_status
recommendations
interactive_guidance
```

Interactive focus:

```text
Detect unresolved validation gaps before finalizing Stage 2. If Stage 2 is not ready, return the minimum set of questions needed to reach a reliable completion status.
```

---

# Subskill Output Contract

Every validation subskill must return:

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

Allowed recommendations:

```text
continue
revise
block
```

Subskills must update the centralized assumption registry instead of producing isolated findings.

---

# Assumption Registry Contract

Every assumption must include:

```json
{
  "id": "",
  "assumption": "",
  "domain": "",
  "source_stage_1_file": "",
  "explicit_or_implicit": "",
  "risk_if_false": "",
  "architecture_critical": false,
  "status": "unvalidated",
  "confidence": 0.0,
  "evidence": [],
  "evidence_quality": "none",
  "contradictions": [],
  "next_action": ""
}
```

Allowed assumption statuses:

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

Allowed risk values:

```text
low
medium
high
critical
```

---

# Confidence Scoring Rules

Use a confidence scale from `0.0` to `1.0`.

Default starting confidence:

```text
unvalidated assumption: 0.30
unknown assumption: 0.20
low evidence: 0.40
medium evidence: 0.65
high evidence: 0.80
validated assumption: 0.75 or higher
contradicted assumption: 0.20 or lower
```

Evidence quality affects confidence:

* `none`: confidence cannot exceed `0.35`
* `low`: confidence cannot exceed `0.55`
* `medium`: confidence can reach `0.75`
* `high`: confidence can reach `1.0`

Contradictions reduce confidence based on severity:

* low: reduce by `0.05`
* medium: reduce by `0.10`
* high: reduce by `0.20`
* critical: reduce by `0.35` and block readiness until resolved or mitigated

Unknown architecture-critical assumptions reduce architecture readiness and may block Stage 3 progression.

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

---

# Evidence Rules

Findings must distinguish:

```text
evidence
inference
assumption
recommendation
```

Unsupported claims must be marked as assumptions.

When browsing, market research, source access, or external validation is unavailable, record that limitation in:

```text
critical_unknowns
recommendations
```

When external research is used, include source links in `evidence`.

Low-evidence recommendations must be marked as provisional.

---

# Contradiction Handling

Each contradiction must use this structure:

```json
{
  "id": "",
  "assumption_ids": [],
  "description": "",
  "severity": "",
  "impact": "",
  "resolution_path": "",
  "status": "open"
}
```

Allowed contradiction statuses:

```text
open
mitigated
resolved
```

Critical open contradictions block Stage 3 progression.

---

# Risk Registry Rules

Each risk must use this structure:

```json
{
  "id": "",
  "risk": "",
  "domain": "",
  "severity": "",
  "likelihood": "",
  "affected_assumptions": [],
  "mitigation": "",
  "owner_stage": "Stage 2"
}
```

High and critical risks must include mitigation paths.

Unresolved architecture risks must be carried into Stage 3 guidance.

---

# Final Output Files

Generate:

```text
Build-Plans/Stage-2/01-market-analysis.json
Build-Plans/Stage-2/02-competitive-landscape.json
Build-Plans/Stage-2/03-technical-feasibility.json
Build-Plans/Stage-2/04-business-viability.json
Build-Plans/Stage-2/05-risk-validation.json
Build-Plans/Stage-2/06-strategic-positioning.json
```

Every output must reference relevant assumption IDs and include confidence and evidence metadata.

---

# Stage Decision Brief

Before final synthesis or `ready_for_stage_3`, generate:

```text
Build-Plans/Stage-2/00-stage-decision-brief.md
```

The brief confirms whether the validated product assumptions are strong enough to continue into architecture.

Ask:

```text
Do you want to proceed with this validated product direction, revise it, or run deeper validation?
```

Allowed user decisions:

```text
Proceed to architecture
Revise product assumptions
Accept known risks
Run deeper validation
Block progression
```

Record the brief in shared validation state as `stage_decision_brief`.

Do not use `ready_for_stage_3` unless:

```text
stage_decision_brief.approval_status = approved
```

---

# Completion Gate

Before Stage 2 may use `ready_for_stage_3`, run `global-stage-readiness-audit`.

The audit must write:

```text
Build-Plans/Build-status/Stage-2-readiness-audit.json
```

The audit must pass according to:

```text
System-References/Docs/Global-Stage-Workflow-Contract.md
```

If the audit does not pass, do not use `ready_for_stage_3`.

Stage 2 may complete only when:

* no critical assumptions remain `unknown`
* no architecture-critical assumptions are below threshold
* no unresolved contradictions remain
* all high-risk assumptions have mitigation paths
* architecture readiness status is `ready`
* Stage 2 decision brief exists and is approved
* all critical interactive guidance questions are answered or converted into recorded assumptions

Possible completion statuses:

```text
ready_for_stage_3
needs_more_validation
requires_product_revision
blocked
```

Use `ready_for_stage_3` only when the product assumptions have been sufficiently validated for safe architectural progression and `stage_decision_brief.approval_status = approved`.

---

# Validation Checklist

Before completing Stage 2, confirm:

* all Stage 1 assumptions were reviewed
* every high-risk assumption was assigned a validation status
* every confidence score has a rationale
* every critical unknown has a next action
* every final output file references assumption IDs
* completion status follows the gate rules

---

# Command Examples

## Example Blocked Completion

```json
{
  "completion_status": {
    "status": "blocked",
    "reason": "minimum viable Stage 1 inputs are missing",
    "next_actions": [
      "Complete Stage 1 product foundation",
      "Complete Stage 1 workflow architecture"
    ]
  }
}
```

## Example Ready Completion

```json
{
  "completion_status": {
    "status": "ready_for_stage_3",
    "reason": "Market, technical, business, operational, and scalability assumptions meet readiness thresholds.",
    "next_stage": "Stage 3 - System Architecture"
  }
}
```
