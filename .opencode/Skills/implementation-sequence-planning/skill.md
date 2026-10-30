---
name: implementation-sequence-planning
description: Convert the Stage 5 roadmap into canonical dependency-aware implementation slices.
compatibility: opencode
---

# Skill — implementation-sequence-planning

# Purpose

The `implementation-sequence-planning` skill converts the roadmap into an ordered build sequence.

It determines:

* implementation order
* vertical slices
* foundational build steps
* feature sequencing
* dependency-aware task ordering
* Stage 6 execution readiness

This skill is the build sequencing layer for Stage 5.

---

# Inputs

```json
{
  "development_roadmap": {},
  "service_architecture": {},
  "data_architecture": {},
  "api_architecture": {},
  "screen_system": {},
  "feature_behaviors": {},
  "ui_blueprints": {},
  "frontend_build_package": {},
  "existing_state": {}
}
```

Read and update shared development state from:

```text
Build-Plans/Build-status/Development-state.json
```

---

# Core Responsibilities

## Sequence Planning

Define:

* foundation-first work
* service implementation order
* data model implementation order
* API implementation order
* UX implementation order
* UI blueprint implementation order
* shared component implementation order
* interaction contract implementation order
* integration implementation order
* validation checkpoints

## Slice Definition

Identify:

* end-to-end slices
* workflow-based slices
* page-based frontend slices
* shared component slices
* infrastructure setup slices
* integration slices
* testing slices

## Sequence Risk Detection

Identify:

* blocked work
* premature feature work
* hidden prerequisites
* risky late integrations
* page work scheduled before shared layout, route, or component foundations
* missing validation checkpoints

---

# Interactive Guidance Responsibilities

Guide the user through sequencing decisions that affect engineering feasibility.

Ask targeted questions when any of these are unclear:

* whether to build by feature, workflow, service, or vertical slice
* which workflow should be implemented first
* whether risky integrations should be built early
* whether manual workflows are acceptable initially
* whether foundation work should precede user-facing work
* what must be demonstrable at each milestone

Infer a vertical-slice-first approach when product and UX workflows are clear, but record the assumption in:

```text
interactive_guidance.assumptions_made
```

Pause for user input when sequencing affects risk, timeline, validation, or implementation feasibility.

---

# Outputs

```json
{
  "implementation_sequence": {},
  "implementation_slices": [],
  "sequence_dependencies": [],
  "validation_checkpoints": [],
  "sequence_risks": []
}
```

---

# Shared State Updates

Update:

```text
implementation_sequence
engineering_dependencies
execution_risks
coordination_notes
interactive_guidance
```

Persist updates to:

```text
Build-Plans/Build-status/Development-state.json
```

---

# Validation Responsibilities

Validate:

* every launch-critical workflow has a build path
* frontend sequencing uses the Stage 4 frontend build package when available
* shared components, layout systems, navigation, and route foundations precede dependent page work
* interactive elements (modals, drawers, nested routes) are sequenced after their parent pages and components
* shared design-system interaction primitives and route foundations precede dependent `UI-ELEMENT-` implementations
* action handlers, confirmation flows, permission states, and success or failure destinations are sequenced before their dependent high-risk interactions are considered complete
* foundational infrastructure and data work precedes dependent features
* integrations are not pushed so late that they threaten release readiness
* each implementation slice has a validation checkpoint
* unresolved blockers are recorded in `open_questions` or `interactive_guidance.blocked_decisions`

---

# Normalized Stage 5 v2 Output

Return only canonical slices for
`02-implementation-sequence.json.data.slices`. Secondary ordering and dependency
views use slice and ticket IDs rather than copied objects.
