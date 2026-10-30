# Stage 2 — Research & Validation Skill Architecture

# Core Philosophy

Stage 2 is centered around:

```text id="jlwm192"
validation intelligence
```

NOT:

* product structuring
* workflow decomposition
* feature categorization

Those responsibilities were completed in Stage 1.

Stage 2 is responsible for validating whether the assumptions behind the product survive real-world constraints and evidence.

The stage focuses on:

* evidence gathering
* feasibility analysis
* confidence scoring
* contradiction detection
* scalability reasoning
* assumption validation

---

# Stage 2 Core Purpose

Transform:

* product assumptions
* inferred workflows
* operational hypotheses

into:

* validated product intelligence
* evidence-backed feasibility
* architecture readiness confidence
* risk-aware product models

---

# Recommended Stage 2 Architecture

```text id="jlwm193"
stage-2-research-and-validation (command)
│
├── assumption-analysis
├── market-and-competitive-validation
├── technical-and-operational-validation
├── business-and-scalability-validation
└── validation-synthesis
```

---

# Stage 2 Command

# Command — stage-2-research-and-validation

## Purpose

The `stage-2-research-and-validation` command orchestrates:

* assumption extraction
* validation prioritization
* evidence analysis
* confidence modeling
* validation synthesis

The command manages:

* validation sequencing
* shared validation state
* confidence progression
* completion determination

---

# Output Directory

All final Stage 2 outputs must be recorded in:

```text
Build-Plans/Stage-2/
```

The command must create this folder if it does not exist.

---

# Interactive Guidance Rules

The Stage 2 command should behave like a guided validation interview.

Use this decision rule:

```text
Ask only for validation decisions that materially affect confidence, evidence quality, or architecture readiness.
Infer low-risk validation assumptions when Stage 1 outputs and available evidence support the inference.
Record assumptions when proceeding without user confirmation.
Block only when a missing answer prevents trustworthy validation or safe Stage 3 progression.
```

Pause for user input when:

* a core assumption cannot be classified or prioritized
* evidence is too weak for an architecture-critical assumption
* a technical feasibility decision depends on an unknown constraint
* monetization or cost assumptions materially affect viability
* a contradiction cannot be resolved through evidence or mitigation
* Stage 3 readiness depends on an unresolved critical unknown

---

# Command Responsibilities

```text id="’winijlwm"
1. Load Stage 1 outputs
2. Extract assumptions
3. Classify assumptions
4. Prioritize validation targets
5. Run validation skills
6. Track confidence scores
7. Detect weak assumptions
8. Generate recommendations
9. Produce validated product model
10. Determine stage completion
```

---

# Shared Validation State

The command maintains continuously evolving validation state.

All validation skills:

* read shared state
* update confidence
* detect contradictions
* refine validation intelligence

---

# Shared State Structure

```json id="’winijlwm2"
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
  "stage_3_handoff": {},
  "completion_status": {}
}
```

---

# Stage 3 Handoff Contract

Stage 2 must produce a concrete Stage 3 handoff.

The `stage_3_handoff` object must include:

```json
{
  "stage_2_output_directory": "Build-Plans/Stage-2/",
  "validated_product_model": {},
  "architecture_readiness": {},
  "validated_assumption_ids": [],
  "architecture_critical_assumption_ids": [],
  "technical_feasibility_summary": {},
  "operational_constraints": [],
  "business_constraints": [],
  "scalability_constraints": [],
  "risk_ids_for_architecture": [],
  "open_contradictions": [],
  "critical_unknowns": [],
  "recommended_architecture_focus": [],
  "completion_status": {}
}
```

---

# Traceability Rules

Every Stage 2 finding must trace back to one or more Stage 1 source IDs or files.

Every Stage 2 output should preserve:

```text
Stage 1 feature/workflow/dependency/risk -> assumption ID -> validation finding -> confidence score -> Stage 3 architecture implication
```

---

# Skill — assumption-analysis

# Purpose

The `assumption-analysis` skill extracts:

* explicit assumptions
* implicit assumptions
* hidden operational assumptions
* business assumptions
* scalability assumptions

from the Stage 1 product model.

This skill acts as the assumption extraction and validation targeting engine.

---

# Core Responsibilities

## Assumption Extraction

Identify:

* market assumptions
* workflow assumptions
* AI assumptions
* monetization assumptions
* operational assumptions
* scalability assumptions

---

## Assumption Classification

Group assumptions into:

* user assumptions
* technical assumptions
* business assumptions
* operational assumptions
* scalability assumptions

---

## Risk Prioritization

Determine:

* high-risk assumptions
* low-confidence assumptions
* architecture-critical assumptions

---

# Inputs

```json id="’winijlwm3"
{
  "stage_1_outputs": {},
  "existing_state": {}
}
```

---

# Outputs

```json id="’winijlwm4"
{
  "assumptions": [],
  "validation_targets": [],
  "high_risk_assumptions": [],
  "confidence_gaps": []
}
```

---

# Example Behavior

## Product Statement

```text id="’winijlwm5"
"We want AI-generated schedules."
```

## Extracted Assumptions

```text id="’winijlwm6"
- users trust AI schedules
- schedules improve outcomes
- users provide enough data
- AI generation is technically feasible
- scheduling workflows scale operationally
```

---

# Shared State Updates

```text id="’winijlwm7"
assumptions
validation_targets
confidence_scores
critical_unknowns
```

---

# Skill — market-and-competitive-validation

# Purpose

The `market-and-competitive-validation` skill validates:

* market demand
* competitive landscape
* user pain validity
* differentiation viability
* positioning opportunities

This skill acts as the market intelligence and competitive validation engine.

---

# Core Responsibilities

## Market Validation

Determine:

* demand strength
* audience viability
* market timing
* market maturity

---

## Competitive Analysis

Identify:

* direct competitors
* indirect competitors
* saturation risk
* differentiation opportunities

---

## User Validation

Validate:

* workflow realism
* user behavior assumptions
* habit change feasibility
* adoption likelihood

---

## Positioning Analysis

Determine:

* product positioning
* category alignment
* strategic differentiation
* competitive advantages

---

# Inputs

```json id="’winijlwm8"
{
  "assumptions": {},
  "product_identity": {},
  "existing_state": {}
}
```

---

# Outputs

```json id="’winijlwm9"
{
  "market_confidence": 0.0,
  "competitive_landscape": {},
  "user_validation": {},
  "positioning_analysis": {},
  "market_risks": []
}
```

---

# Shared State Updates

```text id="’winijlwm10"
market_validation
competitive_landscape
user_validation
confidence_scores
market_risks
```

---

# Skill — technical-and-operational-validation

# Purpose

The `technical-and-operational-validation` skill validates:

* technical feasibility
* operational sustainability
* infrastructure realism
* integration feasibility
* AI capability realism
* scalability assumptions

This skill acts as the technical feasibility and operational validation engine.

---

# Core Responsibilities

## Technical Feasibility

Determine:

* implementation realism
* infrastructure complexity
* integration viability
* AI capability realism

---

## Operational Validation

Validate:

* workflow scalability
* operational sustainability
* support burden
* execution feasibility

---

## Architecture Risk Detection

Identify:

* scalability bottlenecks
* infrastructure weaknesses
* fragile dependencies
* operational complexity risks

---

## Infrastructure Validation

Determine:

* infrastructure sustainability
* hosting viability
* scaling requirements
* orchestration feasibility

---

# Inputs

```json id="’winijlwm11"
{
  "assumptions": {},
  "workflows": {},
  "dependencies": {},
  "existing_state": {}
}
```

---

# Outputs

```json id="’winijlwm12"
{
  "technical_confidence": 0.0,
  "operational_confidence": 0.0,
  "technical_risks": [],
  "scalability_risks": [],
  "infrastructure_constraints": []
}
```

---

# Shared State Updates

```text id="’winijlwm13"
technical_validation
operational_validation
technical_risks
scalability_risks
confidence_scores
```

---

# Skill — business-and-scalability-validation

# Purpose

The `business-and-scalability-validation` skill validates:

* monetization viability
* business sustainability
* growth assumptions
* scalability economics
* operational scalability

This skill acts as the business viability and scalability intelligence engine.

---

# Core Responsibilities

## Monetization Validation

Determine:

* pricing realism
* payment willingness
* revenue sustainability
* monetization feasibility

---

## Growth Validation

Validate:

* growth assumptions
* adoption scalability
* customer acquisition viability
* retention feasibility

---

## Scalability Validation

Determine:

* AI cost sustainability
* infrastructure cost growth
* support scalability
* operational scalability

---

## Business Risk Detection

Identify:

* CAC risks
* retention risks
* dependency risks
* growth bottlenecks

---

# Inputs

```json id="’winijlwm14"
{
  "assumptions": {},
  "market_validation": {},
  "technical_validation": {},
  "existing_state": {}
}
```

---

# Outputs

```json id="’winijlwm15"
{
  "business_confidence": 0.0,
  "monetization_analysis": {},
  "growth_risks": [],
  "scalability_analysis": {},
  "business_constraints": []
}
```

---

# Shared State Updates

```text id="’winijlwm16"
business_validation
scalability_analysis
growth_risks
confidence_scores
business_constraints
```

---

# Skill — validation-synthesis

# Purpose

The `validation-synthesis` skill combines all validation intelligence into:

* validated product models
* confidence frameworks
* risk-aware progression models
* architecture readiness assessments

This skill acts as the final validation synthesis and progression intelligence engine.

---

# Core Responsibilities

## Confidence Modeling

Track:

* validation confidence
* unresolved uncertainty
* architecture readiness
* operational confidence

---

## Contradiction Detection

Identify:

* conflicting assumptions
* unsupported planning
* weak validation areas
* unresolved critical unknowns

---

## Recommendation Generation

Generate:

* validation recommendations
* architecture warnings
* strategic refinements
* progression guidance

---

## Completion Determination

Determine:

* whether validation is sufficient
* whether architecture progression is safe
* whether critical unknowns remain

---

# Inputs

```json id="’winijlwm17"
{
  "market_validation": {},
  "technical_validation": {},
  "business_validation": {},
  "operational_validation": {},
  "existing_state": {}
}
```

---

# Outputs

```json id="’winijlwm18"
{
  "validated_product_model": {},
  "confidence_scores": {},
  "critical_unknowns": [],
  "architecture_readiness": {},
  "validation_recommendations": [],
  "completion_status": {}
}
```

---

# Shared State Updates

```text id="’winijlwm19"
validated_product_model
confidence_scores
critical_unknowns
architecture_readiness
completion_status
```

---

# Recommended Completion Philosophy

Stage 2 completion should NOT mean:

```text id="’winijlwm20"
"All research completed."
```

Instead it should mean:

```text id="’winijlwm21"
"The product assumptions have been sufficiently validated for safe architectural progression."
```

---

# Stage Decision Brief

Before Stage 2 may run final synthesis or use `ready_for_stage_3`, it must generate:

```text
Build-Plans/Stage-2/00-stage-decision-brief.md
```

Purpose:

```text
Confirm whether the validated product assumptions are strong enough to continue into architecture.
```

The brief must include:

* key assumptions
* validated assumptions
* weakened assumptions
* contradicted assumptions
* critical unknowns
* evidence confidence
* risks
* recommended decision

Approval question:

```text
Do you want to proceed with this validated product direction, revise it, or run deeper validation?
```

Approval options:

```text
Proceed to architecture
Revise product assumptions
Accept known risks
Run deeper validation
Block progression
```

Stage 2 shared state must include:

```json
{
  "stage_decision_brief": {
    "brief_id": "",
    "stage": "Stage 2",
    "brief_path": "Build-Plans/Stage-2/00-stage-decision-brief.md",
    "recommended_direction": "",
    "alternatives_considered": [],
    "key_decisions": [],
    "assumptions": [],
    "risks": [],
    "downstream_impact": [],
    "user_decision_required": true,
    "approval_status": "pending | approved | revise | rejected",
    "approved_by": "",
    "approved_at": "",
    "revision_notes": []
  }
}
```

Stage 2 may not lock validation direction or run readiness as `ready_for_stage_3` unless:

```text
stage_decision_brief.approval_status = approved
```

---

# Recommended Completion Criteria

Before Stage 2 may use `ready_for_stage_3`, it must run `global-stage-readiness-audit` and write:

```text
Build-Plans/Build-status/Stage-2-readiness-audit.json
```

The audit must pass according to:

```text
System-References/Docs/Global-Stage-Workflow-Contract.md
```

Stage 2 is complete when:

| Domain       | Requirement                       |
| ------------ | --------------------------------- |
| Market       | Viability confidence acceptable   |
| Users        | User problems validated           |
| Competition  | Competitive landscape understood  |
| Technical    | Feasibility validated             |
| Monetization | Business viability acceptable     |
| Operations   | Operational risks identified      |
| Scalability  | Major scaling blockers understood |

AND:

```text id="’winijlwm22"
No critical unknowns remain unresolved.
```

AND:

```text
Stage 2 decision brief exists and is approved.
```

---

# Assumption Registry

Stage 2 should maintain a centralized assumption registry.

---

# Evidence Quality Rules

Every Stage 2 finding must distinguish:

```text
evidence-backed finding
inference
unsupported assumption
critical unknown
```

Evidence entries must use:

```json
{
  "evidence_id": "",
  "claim_or_assumption_id": "",
  "source_type": "primary | secondary | user_provided | inferred | unavailable",
  "source_url": "",
  "source_date": "",
  "freshness": "current | recent | stale | unknown",
  "evidence_quality": "none | low | medium | high",
  "confidence_effect": "increase | decrease | neutral",
  "confidence_delta": 0.0,
  "summary": "",
  "is_inference": false,
  "limitations": [],
  "requires_external_research": false
}
```

Architecture-critical assumptions cannot be marked `validated` unless evidence quality is `medium` or `high`, the risk is explicitly accepted and carried into Stage 3, or the assumption remains a critical unknown blocking architecture progression.

---

# Example Structure

```json id="’winijlwm23"
{
  "id": "",
  "assumption": "Users trust AI-generated schedules",
  "domain": "user_validation",
  "source_stage_1_file": "",
  "explicit_or_implicit": "",
  "architecture_critical": false,
  "confidence": 0.73,
  "validation_sources": [],
  "risk_if_false": "high",
  "status": "unvalidated",
  "evidence": [],
  "evidence_quality": "none",
  "contradictions": [],
  "next_action": ""
}
```

This registry becomes:

* the validation backbone
* the confidence engine
* the progression gating layer

---

# Evidence, Confidence, And Risk Rules

Findings must distinguish:

```text
evidence
inference
assumption
recommendation
```

Unsupported claims must be marked as assumptions.

When external research is unavailable, record the limitation in `critical_unknowns` and mark affected recommendations as provisional.

When external research is used, include source links in `evidence`.

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

High and critical risks must include mitigation paths.

Critical open contradictions block Stage 3 progression.

---

# Final Output Schemas

`01-market-analysis.json` must follow this structure:

```json
{
  "stage": "Stage 2",
  "status": "",
  "market_validation": {},
  "user_validation": {},
  "demand_strength": {},
  "validated_assumption_ids": [],
  "confidence": 0.0,
  "evidence": [],
  "risks": []
}
```

`02-competitive-landscape.json` must follow this structure:

```json
{
  "stage": "Stage 2",
  "status": "",
  "competitive_landscape": {},
  "direct_competitors": [],
  "indirect_competitors": [],
  "differentiation_opportunities": [],
  "validated_assumption_ids": [],
  "confidence": 0.0,
  "evidence": [],
  "risks": []
}
```

`03-technical-feasibility.json` must follow this structure:

```json
{
  "stage": "Stage 2",
  "status": "",
  "technical_validation": {},
  "operational_validation": {},
  "integration_feasibility": {},
  "ai_capability_realism": {},
  "validated_assumption_ids": [],
  "confidence": 0.0,
  "evidence": [],
  "architecture_implications": []
}
```

`04-business-viability.json` must follow this structure:

```json
{
  "stage": "Stage 2",
  "status": "",
  "business_validation": {},
  "monetization_analysis": {},
  "growth_risks": [],
  "scalability_analysis": {},
  "validated_assumption_ids": [],
  "confidence": 0.0,
  "evidence": [],
  "constraints": []
}
```

`05-risk-validation.json` must follow this structure:

```json
{
  "stage": "Stage 2",
  "status": "",
  "risk_registry": [],
  "critical_unknowns": [],
  "contradictions": [],
  "mitigation_paths": [],
  "architecture_blockers": [],
  "evidence": []
}
```

`06-strategic-positioning.json` must follow this structure:

```json
{
  "stage": "Stage 2",
  "status": "",
  "strategic_positioning": {},
  "validated_product_model": {},
  "architecture_readiness": {},
  "stage_3_handoff": {},
  "recommendations": [],
  "completion_status": {}
}
```

---

# Final Stage 2 Philosophy

# Stage 1

```text id="’winijlwm24"
"What are we building?"
```

# Stage 2

```text id="’winijlwm25"
"Do the assumptions behind this product survive reality?"
```

This creates a clean cognition boundary between:

* product synthesis
  and
* evidence-backed validation.

---

# Final Definition

Stage 2 is:

```text id="’winijlwm26"
an evidence-driven validation cognition framework
```

designed to transform:

* product assumptions
* inferred operational models
* strategic hypotheses

into:

* validated product intelligence
* risk-aware feasibility analysis
* architecture-ready confidence models.

---

# A-Grade Workflow Compliance

Stage 2 must consume `stage_contract_profile` and `guidance_policy`.

Stage 2 output validation should reference:

```text
System-References/Schemas/stage-2-output.schema.json
```

Stage 2 evidence findings should create or reference artifacts in:

```text
Build-Plans/Build-status/Artifact-evidence-registry.json
```

Architecture-critical assumptions require evidence quality of `medium` or higher unless explicitly accepted as risk.

Stage 2 readiness must also record:

```json
{
  "schema_validation": {},
  "reference_integrity": {},
  "risk_acceptance_ledger": {},
  "revision_loops": []
}
```

Stage 2 may not use `ready_for_stage_3` until required schema validation passes, assumption and evidence references resolve to Stage 1 sources, accepted high and critical validation risks are written to `Build-Plans/Build-status/Risk-acceptance-ledger.json`, and failed readiness checks are converted into revision-loop actions.
