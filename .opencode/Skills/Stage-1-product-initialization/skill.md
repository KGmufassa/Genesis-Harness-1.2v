---
name: stage-1-product-initialization
description: The Stage-1-product-initialization command orchestrates the Stage 1 skills in sequence.
compatibility: opencode
---

# Command — Stage-1-product-initialization

# Purpose

The `Stage-1-product-initialization` command orchestrates the Stage 1 skills in sequence.

It transforms:

* raw product ideas
* incomplete concepts
* fragmented planning
* user goals

into:

* structured product foundations
* user-system models
* workflow architecture
* capability and feature structures
* dependency-aware product models
* MVP operational definitions
* architecture-ready Stage 1 outputs

This command is the Stage 1 orchestration layer.

---

# Output Directory

All Stage 1 command outputs must be recorded in:

```text
Build-Plans/Stage-1/
```

The command must create this folder if it does not exist.

---

# Orchestrated Skills

Run the Stage 1 skills in this order:

```text
1. product-intelligence
2. workflow-and-capability-synthesis
3. dependency-and-risk-analysis
4. mvp-and-optimization
5. product-synthesis
```

---

# Command Responsibilities

The command is responsible for:

* initializing Stage 1 shared state
* passing each skill the required upstream outputs
* ensuring each skill records owned outputs in `Build-Plans/Stage-1/`
* preserving valid existing output content when a skill updates only part of a file
* detecting missing information and unresolved planning gaps
* guiding the user interactively until Stage 1 objectives are satisfied
* asking targeted questions only when missing information materially affects Stage 1 outputs
* recording assumptions when the command proceeds without user confirmation
* running final synthesis after all upstream skills complete
* validating that all required Stage 1 files exist
* determining whether Stage 1 is ready for Stage 2

---

# Inputs

```json
{
  "raw_user_input": "",
  "conversation_history": [],
  "existing_stage_1_outputs": {},
  "existing_state": {}
}
```

---

# Shared State

The command maintains a shared Stage 1 state object:

The shared state must be written to:

```text
Build-Plans/Build-status/Planning-state.json
```

The command must load this file at the beginning of Stage 1, update it after each skill runs, and preserve it as the durable orchestration state for the build.

```json
{
  "product_identity": {},
  "strategic_intent": {},
  "user_profiles": {},
  "recommendations": [],
  "confidence_scores": {},
  "missing_information": [],
  "workflows": {},
  "capabilities": {},
  "feature_groups": {},
  "operational_boundaries": {},
  "workflow_relationships": {},
  "dependencies": {},
  "technical_risks": [],
  "business_risks": [],
  "compliance_risks": [],
  "operational_risks": [],
  "risk_severity": {},
  "mvp_scope": {},
  "feature_priorities": {},
  "deferred_features": [],
  "implementation_phases": {},
  "optimization_recommendations": [],
  "interactive_guidance": {
    "open_questions": [],
    "answered_questions": [],
    "assumptions_made": [],
    "blocked_decisions": [],
    "user_confirmations": [],
    "confidence_gaps": []
  },
  "final_outputs": {},
  "completion_status": {}
}
```

Each skill reads the current shared state and writes its updates back into the shared state before the next skill runs.

After each skill completes, the command must persist the updated shared state to:

```text
Build-Plans/Build-status/Planning-state.json
```

---

# Interactive Guidance Rules

The command should behave like a guided product initialization interview.

## Initialization Intake

When the command is initialized, inspect `System-References/PRD Docs/` before asking intake questions.

If the folder contains readable supported PRD source files, treat those files as initial product intent and proceed to `product-intelligence`.

When the folder is empty or contains no readable supported files and no usable raw product intent exists yet, first ask the user:

```text
1. What app do you want to build?
2. Who is the app for?
3. What features or capabilities do you already know you want included?
```

If the user already provided the app idea but not features, ask only for the missing feature or capability details.

If the user provided features but not the core app idea or target user, ask only for the missing product identity or user details.

Record the user's answer as the initial `raw_product_intent` and seed:

```text
product_identity
strategic_intent
user_profiles
feature_groups
interactive_guidance.answered_questions
```

Do not run downstream Stage 1 subskills until there is enough initial app intent to identify:

* app idea
* primary user or audience
* initial feature or capability list

Use this decision rule:

```text
Ask only for decisions that materially affect Stage 1 outputs.
Infer common defaults when risk is low.
Record assumptions when proceeding without confirmation.
Block only when a missing answer prevents safe Stage 1 completion.
```

When asking the user questions:

* ask 1-3 questions at a time
* prioritize the highest-impact missing decisions
* avoid asking questions that can be safely inferred
* explain why each question matters when the impact is not obvious
* update `interactive_guidance.open_questions`
* move answered questions into `interactive_guidance.answered_questions`
* record inferred defaults in `interactive_guidance.assumptions_made`

The command should continue automatically when assumptions are low-risk.

The command should pause for user input when:

* product identity is unclear
* primary user is unknown
* core user outcome is unknown
* workflow start or end state is ambiguous
* MVP boundary cannot be determined
* a critical dependency decision blocks output generation
* a contradiction prevents coherent product synthesis

---

# Execution Sequence

## 1. Initialize Stage 1

Prepare the output directory:

```text
Build-Plans/Stage-1/
```

Prepare the build status directory:

```text
Build-Plans/Build-status/
```

Load any existing Stage 1 output files from the folder and merge them into shared state when they contain valid content.

Load the current shared planning state from:

```text
Build-Plans/Build-status/Planning-state.json
```

Do not discard existing valid planning outputs unless the user explicitly requests a clean restart.

Before running `product-intelligence`, first check whether `System-References/PRD Docs/` contains readable PRD source files. If it does, treat those files as sufficient initial app-intent input and let `product-intelligence` extract product details and features from them before asking the user intake questions.

If `System-References/PRD Docs/` is empty or contains no readable supported files, verify that `raw_user_input`, conversation context, existing Stage 1 outputs, or planning state contains enough initial app intent.

If the app idea, primary user, or initial features are missing, pause and ask the initialization intake questions instead of continuing.

---

## 2. Run `product-intelligence`

Purpose:

* interpret the raw idea
* identify product type and strategic intent
* identify users and user needs
* detect gaps and ambiguities
* generate recommendations and clarification needs

Record or update:

```text
Build-Plans/Stage-1/01-product-foundation.json
Build-Plans/Stage-1/02-user-system-map.json
Build-Plans/Stage-1/10-success-framework.json
```

Required shared state updates:

```text
product_identity
strategic_intent
user_profiles
recommendations
confidence_scores
missing_information
interactive_guidance
```

Interactive focus:

```text
Guide the user toward clear product identity, user definition, problem framing, strategic intent, and success criteria.
```

---

## 3. Run `workflow-and-capability-synthesis`

Purpose:

* infer workflows
* structure user journeys
* identify product capabilities
* organize feature groups
* detect operational boundaries

Record or update:

```text
Build-Plans/Stage-1/03-workflow-architecture.json
Build-Plans/Stage-1/04-product-capabilities.json
Build-Plans/Stage-1/05-feature-structure.json
Build-Plans/Stage-1/06-product-boundaries.json
```

Required shared state updates:

```text
workflows
capabilities
feature_groups
operational_boundaries
workflow_relationships
capability_dependencies
interactive_guidance
```

Interactive focus:

```text
Guide the user from vague product behavior into concrete workflows, user actions, system actions, and operational boundaries.
```

---

## 4. Run `dependency-and-risk-analysis`

Purpose:

* infer hidden dependencies
* detect missing operational systems
* identify technical, business, compliance, and operational risks
* surface architecture-sensitive concerns early

Record or update:

```text
Build-Plans/Stage-1/07-dependency-map.json
Build-Plans/Stage-1/09-risk-and-constraints.json
```

Required shared state updates:

```text
dependencies
technical_risks
business_risks
compliance_risks
operational_risks
missing_information
risk_severity
interactive_guidance
```

Interactive focus:

```text
Guide the user through hidden system decisions such as authentication, permissions, storage, payments, integrations, compliance, moderation, and operational support.
```

---

## 5. Run `mvp-and-optimization`

Purpose:

* define realistic MVP scope
* prioritize features
* defer non-critical complexity
* preserve workflow integrity
* define implementation phases

Record or update:

```text
Build-Plans/Stage-1/08-mvp-operational-model.json
```

Required shared state updates:

```text
mvp_scope
feature_priorities
deferred_features
launch_critical_systems
implementation_phases
optimization_recommendations
complexity_reductions
interactive_guidance
```

Interactive focus:

```text
Guide the user toward a realistic launch scope, must-have workflows, deferred complexity, and acceptable MVP tradeoffs.
```

---

## 6. Run `product-synthesis`

Purpose:

* reconcile all Stage 1 skill outputs
* normalize the product model
* remove contradictions and duplication
* ensure all ten output files are architecture-ready
* produce final Stage 1 completion status

Record or update all final Stage 1 files:

```text
Build-Plans/Stage-1/01-product-foundation.json
Build-Plans/Stage-1/02-user-system-map.json
Build-Plans/Stage-1/03-workflow-architecture.json
Build-Plans/Stage-1/04-product-capabilities.json
Build-Plans/Stage-1/05-feature-structure.json
Build-Plans/Stage-1/06-product-boundaries.json
Build-Plans/Stage-1/07-dependency-map.json
Build-Plans/Stage-1/08-mvp-operational-model.json
Build-Plans/Stage-1/09-risk-and-constraints.json
Build-Plans/Stage-1/10-success-framework.json
```

Required shared state updates:

```text
final_outputs
normalized_product_model
product_topology
completion_status
interactive_guidance
```

Interactive focus:

```text
Detect unresolved gaps before finalizing Stage 1. If Stage 1 is not ready, return the minimum set of questions needed to reach readiness.
```

---

# Stage Decision Brief

Before final synthesis or `ready_for_stage_2`, generate:

```text
Build-Plans/Stage-1/00-stage-decision-brief.md
```

The brief confirms the app idea, feature direction, MVP boundary, and how the app should work before Stage 2 validation.

Ask:

```text
Does this correctly describe the app you want to build, the features it should include, and how it should work?
```

Allowed user decisions:

```text
Approve direction
Revise app idea
Add/remove features
Change how the app works
Redefine MVP scope
```

Record the brief in shared planning state as `stage_decision_brief`.

Do not use `ready_for_stage_2` unless:

```text
stage_decision_brief.approval_status = approved
```

---

# Completion Gate

Before Stage 1 may use `ready_for_stage_2`, run `global-stage-readiness-audit`.

The audit must write:

```text
Build-Plans/Build-status/Stage-1-readiness-audit.json
```

The audit must pass according to:

```text
System-References/Docs/Global-Stage-Workflow-Contract.md
```

If the audit does not pass, do not use `ready_for_stage_2`.

Stage 1 is complete only when:

* all ten final output files exist in `Build-Plans/Stage-1/`
* the product identity is clear enough for validation
* primary users are identified
* core workflows are structured
* capabilities and feature groups are defined
* operational boundaries are identified
* major dependencies and risks are recorded
* MVP scope is defined
* success framework is present
* Stage 1 decision brief exists and is approved
* all critical interactive guidance questions are answered or converted into recorded assumptions
* no critical Stage 1 planning gap blocks Stage 2 validation

---

# Completion Status Values

```text
ready_for_stage_2
needs_more_product_input
needs_scope_reduction
blocked_by_missing_foundation
```

Use `ready_for_stage_2` only when Stage 2 can safely validate the product assumptions using the generated Stage 1 files and `stage_decision_brief.approval_status = approved`.

---

# Final Outputs

```text
Build-Plans/Stage-1/01-product-foundation.json
Build-Plans/Stage-1/02-user-system-map.json
Build-Plans/Stage-1/03-workflow-architecture.json
Build-Plans/Stage-1/04-product-capabilities.json
Build-Plans/Stage-1/05-feature-structure.json
Build-Plans/Stage-1/06-product-boundaries.json
Build-Plans/Stage-1/07-dependency-map.json
Build-Plans/Stage-1/08-mvp-operational-model.json
Build-Plans/Stage-1/09-risk-and-constraints.json
Build-Plans/Stage-1/10-success-framework.json
```

---

# Command Rule

The command must not skip directly to final synthesis.

It must run the Stage 1 skills in sequence, because each skill depends on the structured intelligence produced by the previous skill.

---

# A-Grade Workflow Compliance

Stage 1 must initialize or confirm `stage_contract_profile` and `guidance_policy`.

Stage 1 must reference:

```text
System-References/Schemas/stage-1-output.schema.json
```

Stage 1 should infer the initial app profile when possible and record the rationale in `interactive_guidance.assumptions_made`.

Planning artifacts, source notes, and user-provided intake evidence should be recorded or referenced in:

```text
Build-Plans/Build-status/Artifact-evidence-registry.json
```

Before using `ready_for_stage_2`, Stage 1 must provide `schema_validation`, `reference_integrity`, `risk_acceptance_ledger`, and `revision_loops` in the readiness audit or stage state.

Accepted high and critical risks must be recorded in:

```text
Build-Plans/Build-status/Risk-acceptance-ledger.json
```

Failed readiness checks must become revision-loop actions with owning output, owning skill, required change, and next action.
