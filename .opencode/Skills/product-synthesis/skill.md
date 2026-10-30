---
name: product-synthesis
description: The product-synthesis skill reconciles all Stage 1 outputs into a complete product initialization package.
compatibility: opencode
---

# Skill — product-synthesis

# Purpose

The `product-synthesis` skill reconciles all Stage 1 outputs into a complete product initialization package.

It combines:

* product foundation
* user-system map
* workflow architecture
* capabilities
* feature structure
* boundaries
* dependencies
* MVP model
* risks and constraints
* success framework

This skill is the final Stage 1 synthesis and handoff layer.

---

# Core Responsibilities

## Product Model Reconciliation

Normalize:

* duplicated concepts
* conflicting feature names
* inconsistent user roles
* mismatched workflows and capabilities
* unclear product boundaries

## Completion Review

Verify:

* all required Stage 1 files exist or are explicitly blocked
* all files are valid JSON
* output IDs and references are consistent
* unresolved questions are captured
* assumptions are ready for Stage 2 validation
* `Build-Plans/Stage-1/00-stage-decision-brief.md` exists
* `stage_decision_brief.approval_status` is `approved`

## Stage 2 Handoff

Produce handoff data that lets Stage 2 validate assumptions without redoing Stage 1 synthesis.

The handoff must include:

* product identity
* MVP boundaries
* assumption candidates
* validation targets
* high-risk unknowns
* architecture-sensitive concerns
* success framework
* completion status

---

# Interactive Guidance Responsibilities

Ask targeted questions only when synthesis cannot safely complete without user input.

Ask no more than 1-3 questions at once.

Pause for user input when:

* the product model contains unresolved contradictions
* MVP scope and success criteria conflict
* Stage 2 would not have enough assumptions to validate
* a blocked decision affects product boundaries
* the Stage 1 decision brief has not been approved

Update:

```text
interactive_guidance.open_questions
interactive_guidance.answered_questions
interactive_guidance.assumptions_made
interactive_guidance.blocked_decisions
interactive_guidance.confidence_gaps
```

---

# Inputs

```json
{
  "product_foundation": {},
  "user_system_map": {},
  "workflow_architecture": {},
  "product_capabilities": {},
  "feature_structure": {},
  "product_boundaries": {},
  "dependency_map": {},
  "mvp_operational_model": {},
  "risk_and_constraints": {},
  "success_framework": {},
  "existing_state": {}
}
```

---

# Outputs

Record final Stage 1 outputs in:

```text
Build-Plans/Stage-1/
```

The skill must write or normalize all final Stage 1 files:

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

It must also update:

```text
Build-Plans/Build-status/Planning-state.json
```

with:

```json
{
  "stage": "Stage 1",
  "completion_status": {},
  "stage_2_handoff": {},
  "interactive_guidance": {},
  "traceability": {},
  "remaining_gaps": []
}
```

Use `ready_for_stage_2` only after `global-stage-readiness-audit` passes.

Before using `ready_for_stage_2`, this skill must generate or verify:

```text
Build-Plans/Stage-1/00-stage-decision-brief.md
```

The brief must confirm the app idea, feature direction, MVP boundary, and how the app should work. If `stage_decision_brief.approval_status` is not `approved`, return the brief for user review instead of locking Stage 1.
