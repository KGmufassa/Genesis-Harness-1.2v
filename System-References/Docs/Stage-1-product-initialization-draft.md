# Stage 1 — Product Initialization Command & Skill Draft

# Core Philosophy

Stage 1 is centered around:

```text
product initialization cognition
```

NOT:

* market validation
* system architecture
* UX architecture
* implementation planning
* production execution

Stage 1 transforms vague product ideas, fragmented concepts, and incomplete planning into a structured product model that can be validated in Stage 2.

---

# Stage 1 Core Purpose

Transform:

* raw product ideas
* incomplete concepts
* user goals
* fragmented planning

into:

* structured product foundations
* user-system models
* workflow architecture
* capability and feature structures
* dependency-aware product models
* MVP operational definitions
* Stage 2 validation-ready assumptions

---

# Recommended Stage 1 Architecture

```text
Stage-1-product-initialization (command)
│
├── product-intelligence
├── workflow-and-capability-synthesis
├── dependency-and-risk-analysis
├── mvp-and-optimization
└── product-synthesis
```

---

# Command — Stage-1-product-initialization

# Purpose

The `Stage-1-product-initialization` command orchestrates Stage 1.

It transforms raw product intent into a complete product planning package that is ready for Stage 2 research and validation.

This is the Stage 1 command skill. It is not a single product planning subskill.

---

# Cognitive Boundary

Stage 1 asks:

```text
What are we building, for whom, through which workflows, with what MVP boundary?
```

Stage 1 must not:

* validate market evidence
* design technical architecture
* design detailed screens
* create implementation tickets
* run build or test workflows

Stage 1 may flag research, architecture, UX, or implementation concerns only as downstream risks or validation targets.

---

# Output Directory

All final Stage 1 outputs must be recorded in:

```text
Build-Plans/Stage-1/
```

The command must create this folder if it does not exist.

---

# Shared Planning State

The shared Stage 1 planning state must be written to:

```text
Build-Plans/Build-status/Planning-state.json
```

The command must load this file at the beginning of Stage 1, update it after each skill runs, and preserve it as durable planning state.

```json
{
  "stage": "Stage 1",
  "command": "Stage-1-product-initialization",
  "status": "not_started",
  "product_identity": {},
  "strategic_intent": {},
  "problem_framing": {},
  "user_profiles": {},
  "user_system_map": {},
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
  "launch_critical_systems": [],
  "implementation_phases": {},
  "optimization_recommendations": [],
  "assumption_seed_registry": [],
  "traceability": {},
  "interactive_guidance": {
    "open_questions": [],
    "answered_questions": [],
    "assumptions_made": [],
    "blocked_decisions": [],
    "user_confirmations": [],
    "confidence_gaps": []
  },
  "stage_2_handoff": {},
  "final_outputs": {},
  "completion_status": {}
}
```

---

# Interactive Guidance Rules

The Stage 1 command should behave like a guided product initialization interview.

## Initialization Intake

When the Stage 1 command is initialized, inspect `System-References/PRD Docs/` before asking intake questions.

If the folder contains readable supported PRD source files, treat those files as initial product intent and proceed to `product-intelligence`.

When the folder is empty or contains no readable supported files and no usable raw product intent exists yet, ask the user to explain:

```text
1. What app do you want to build?
2. Who is the app for?
3. What features or capabilities do you already know you want included?
```

If the user already provided a product idea but not features, ask only for the missing feature/capability details.

If the user provided features but not the core app idea or target user, ask only for the missing product identity or user details.

Record the user's answer as the initial `raw_product_intent` and seed:

```text
product_identity
strategic_intent
user_profiles
feature_groups
interactive_guidance.answered_questions
```

Do not run the downstream Stage 1 subskills until there is enough initial app intent to identify at least:

* app idea
* primary user or audience
* initial feature or capability list

Use this decision rule:

```text
Ask only for decisions that materially affect Stage 1 outputs.
Infer common defaults when risk is low.
Record assumptions when proceeding without confirmation.
Block only when a missing answer prevents safe Stage 1 completion or Stage 2 validation.
```

Ask 1-3 questions at a time. Prioritize questions that affect product identity, primary users, core outcomes, MVP boundaries, dependencies, risks, or Stage 2 validation readiness.

Pause for user input when:

* product identity is unclear
* primary user is unknown
* core user outcome is unknown
* workflow start or end state is ambiguous
* MVP boundary cannot be determined
* a critical dependency decision blocks output generation
* a contradiction prevents coherent product synthesis

---

# Stage 2 Handoff Contract

Stage 1 must produce a concrete Stage 2 handoff.

The `stage_2_handoff` object must include:

```json
{
  "stage_1_output_directory": "Build-Plans/Stage-1/",
  "required_files": [
    "01-product-foundation.json",
    "02-user-system-map.json",
    "03-workflow-architecture.json",
    "04-product-capabilities.json",
    "05-feature-structure.json",
    "06-product-boundaries.json",
    "07-dependency-map.json",
    "08-mvp-operational-model.json",
    "09-risk-and-constraints.json",
    "10-success-framework.json"
  ],
  "validation_seed_assumptions": [],
  "high_risk_assumption_candidates": [],
  "architecture_critical_assumption_candidates": [],
  "market_validation_targets": [],
  "technical_validation_targets": [],
  "business_validation_targets": [],
  "operational_validation_targets": [],
  "scalability_validation_targets": [],
  "known_planning_gaps": [],
  "recorded_assumptions": [],
  "completion_status": {}
}
```

Stage 2 should be able to extract and prioritize assumptions from this handoff without redoing Stage 1 product structuring.

---

# Traceability Rules

Stage 1 must preserve IDs that downstream stages can reference.

Recommended ID prefixes:

```text
USER-
WORKFLOW-
CAP-
FEATURE-
BOUNDARY-
DEP-
RISK-
MVP-
SUCCESS-
ASSUMPTION-SEED-
```

Every launch-critical feature should trace to:

```text
user -> workflow -> capability -> feature -> MVP priority -> risk/dependency -> success criterion
```

---

# Orchestrated Skills

Run Stage 1 skills in this order:

```text
1. product-intelligence
2. workflow-and-capability-synthesis
3. dependency-and-risk-analysis
4. mvp-and-optimization
5. product-synthesis
```

---

# Skill — product-intelligence

Purpose:

* interpret raw product intent
* inspect `System-References/PRD Docs/` first for initial product details and features
* identify product type, category, and strategic intent
* identify users, needs, motivations, and success criteria
* detect incomplete planning and ambiguity
* generate recommendations and clarification questions

Writes:

```text
Build-Plans/Stage-1/01-product-foundation.json
Build-Plans/Stage-1/02-user-system-map.json
Build-Plans/Stage-1/10-success-framework.json
```

Before using raw user input or intake questions, inspect:

```text
System-References/PRD Docs/
```

If this folder contains readable PRD source files, use them as the primary product-intelligence source and extract product details, target users, features, constraints, success criteria, and open questions from those files. Preserve PRD file path references in the generated Stage 1 outputs.

If the folder is empty or contains no readable supported files, continue with the original workflow using raw user input, conversation context, existing Stage 1 outputs, planning state, and targeted intake questions.

---

# Skill — workflow-and-capability-synthesis

Purpose:

* infer and normalize workflows
* define user and system actions
* categorize product capabilities
* structure feature groups
* identify operational boundaries

Writes:

```text
Build-Plans/Stage-1/03-workflow-architecture.json
Build-Plans/Stage-1/04-product-capabilities.json
Build-Plans/Stage-1/05-feature-structure.json
Build-Plans/Stage-1/06-product-boundaries.json
```

---

# Skill — dependency-and-risk-analysis

Purpose:

* infer hidden supporting systems
* identify technical, business, compliance, and operational risks
* detect architecture-sensitive concerns
* identify missing systems and constraints

Writes:

```text
Build-Plans/Stage-1/07-dependency-map.json
Build-Plans/Stage-1/09-risk-and-constraints.json
```

---

# Skill — mvp-and-optimization

Purpose:

* define realistic MVP scope
* prioritize features
* defer non-critical complexity
* preserve workflow integrity
* define implementation phases and launch-critical systems

Writes:

```text
Build-Plans/Stage-1/08-mvp-operational-model.json
```

---

# Skill — product-synthesis

Purpose:

* reconcile all Stage 1 skill outputs
* normalize product model
* remove contradictions and duplication
* generate all final Stage 1 outputs
* produce Stage 2 handoff and completion status

Writes all final Stage 1 files.

---

# Final Output Schemas

`01-product-foundation.json` must follow this structure:

```json
{
  "stage": "Stage 1",
  "status": "",
  "product_identity": {},
  "strategic_intent": {},
  "problem_framing": {},
  "business_direction": {},
  "differentiation_hypotheses": [],
  "known_constraints": [],
  "source_trace": []
}
```

`02-user-system-map.json` must follow this structure:

```json
{
  "stage": "Stage 1",
  "status": "",
  "primary_users": [],
  "secondary_users": [],
  "user_goals": [],
  "user_needs": [],
  "user_system_relationships": [],
  "role_or_permission_hints": [],
  "source_trace": []
}
```

`03-workflow-architecture.json` must follow this structure:

```json
{
  "stage": "Stage 1",
  "status": "",
  "workflows": [],
  "workflow_relationships": [],
  "start_states": [],
  "success_states": [],
  "failure_or_recovery_hints": [],
  "source_trace": []
}
```

`04-product-capabilities.json` must follow this structure:

```json
{
  "stage": "Stage 1",
  "status": "",
  "capabilities": [],
  "capability_groups": [],
  "operational_domains": [],
  "capability_dependencies": [],
  "source_trace": []
}
```

`05-feature-structure.json` must follow this structure:

```json
{
  "stage": "Stage 1",
  "status": "",
  "features": [],
  "feature_groups": [],
  "feature_relationships": [],
  "capability_feature_map": [],
  "launch_critical_features": [],
  "deferred_features": [],
  "source_trace": []
}
```

`06-product-boundaries.json` must follow this structure:

```json
{
  "stage": "Stage 1",
  "status": "",
  "mvp_boundaries": [],
  "operational_boundaries": [],
  "system_boundaries": [],
  "ownership_boundaries": [],
  "out_of_scope_items": [],
  "source_trace": []
}
```

`07-dependency-map.json` must follow this structure:

```json
{
  "stage": "Stage 1",
  "status": "",
  "dependencies": [],
  "dependency_relationships": [],
  "missing_systems": [],
  "external_dependency_candidates": [],
  "architecture_sensitive_dependencies": [],
  "source_trace": []
}
```

`08-mvp-operational-model.json` must follow this structure:

```json
{
  "stage": "Stage 1",
  "status": "",
  "mvp_scope": {},
  "launch_critical_workflows": [],
  "launch_critical_systems": [],
  "feature_priorities": {},
  "deferred_features": [],
  "implementation_phases": {},
  "manual_workaround_candidates": [],
  "complexity_reductions": [],
  "source_trace": []
}
```

`09-risk-and-constraints.json` must follow this structure:

```json
{
  "stage": "Stage 1",
  "status": "",
  "technical_risks": [],
  "business_risks": [],
  "compliance_risks": [],
  "operational_risks": [],
  "risk_severity": {},
  "constraints": [],
  "mitigation_hints": [],
  "source_trace": []
}
```

`10-success-framework.json` must follow this structure:

```json
{
  "stage": "Stage 1",
  "status": "",
  "success_criteria": [],
  "validation_needs": [],
  "confidence_scores": {},
  "success_assumptions": [],
  "stage_2_handoff": {},
  "completion_status": {}
}
```

---

# Stage Decision Brief

Before Stage 1 may run final synthesis or use `ready_for_stage_2`, it must generate:

```text
Build-Plans/Stage-1/00-stage-decision-brief.md
```

Purpose:

```text
Confirm the app idea, features, MVP direction, and how the app should work before Stage 2 validation.
```

The brief must include:

* app concept
* target users
* core problem
* main user outcomes
* proposed feature list
* feature priorities
* how the app workflow should operate
* MVP boundary
* assumptions
* intentionally out-of-scope items

Approval question:

```text
Does this correctly describe the app you want to build, the features it should include, and how it should work?
```

Approval options:

```text
Approve direction
Revise app idea
Add/remove features
Change how the app works
Redefine MVP scope
```

Stage 1 shared state must include:

```json
{
  "stage_decision_brief": {
    "brief_id": "",
    "stage": "Stage 1",
    "brief_path": "Build-Plans/Stage-1/00-stage-decision-brief.md",
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

Stage 1 may not lock product direction or run readiness as `ready_for_stage_2` unless:

```text
stage_decision_brief.approval_status = approved
```

---

# Completion Gate

Before Stage 1 may use `ready_for_stage_2`, it must run `global-stage-readiness-audit` and write:

```text
Build-Plans/Build-status/Stage-1-readiness-audit.json
```

The audit must pass according to:

```text
System-References/Docs/Global-Stage-Workflow-Contract.md
```

Stage 1 may complete only when:

* all ten final output files exist
* product identity is clear enough for validation
* primary users are identified
* core workflows are structured
* capabilities and feature groups are defined
* operational boundaries are identified
* major dependencies and risks are recorded
* MVP scope is defined
* success framework is present
* Stage 2 handoff includes validation seed assumptions
* Stage 1 decision brief exists and is approved
* all critical interactive guidance questions are answered or converted into recorded assumptions
* no critical Stage 1 planning gap blocks Stage 2 validation

Completion statuses:

```text
ready_for_stage_2
needs_more_product_input
needs_scope_reduction
blocked_by_missing_foundation
```

Use `ready_for_stage_2` only when Stage 2 can safely validate product assumptions using the generated Stage 1 files and `stage_decision_brief.approval_status = approved`.

---

# Validation Checklist

Before completing Stage 1, confirm:

* Stage 1 did not perform market validation
* Stage 1 did not design technical architecture
* Stage 1 did not produce UX screens or implementation tickets
* every launch-critical feature maps to a workflow and capability
* every MVP workflow has a user, start state, and success state
* major dependencies and risks are recorded
* assumptions and gaps are visible for Stage 2
* Stage 2 handoff is usable for research and validation

---

# A-Grade Workflow Compliance

Stage 1 must initialize or confirm `stage_contract_profile` and `guidance_policy`.

Stage 1 output validation should reference:

```text
System-References/Schemas/stage-1-output.schema.json
```

Stage 1 planning artifacts, source notes, and user-provided intake evidence should be recorded or referenced in:

```text
Build-Plans/Build-status/Artifact-evidence-registry.json
```

Stage 1 readiness must also record:

```json
{
  "schema_validation": {},
  "reference_integrity": {},
  "risk_acceptance_ledger": {},
  "revision_loops": []
}
```

Stage 1 may not use `ready_for_stage_2` until required schema validation passes, blocking reference errors are resolved or accepted, accepted high and critical risks are written to `Build-Plans/Build-status/Risk-acceptance-ledger.json`, and failed readiness checks are converted into revision-loop actions.
