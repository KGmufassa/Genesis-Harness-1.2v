---
name: development-roadmap-planning
description: Define the canonical Stage 5 development roadmap payload.
compatibility: opencode
---

# Skill — development-roadmap-planning

# Purpose

The `development-roadmap-planning` skill defines the engineering roadmap for Stage 5.

It determines:

* development phases
* workstreams
* milestones
* MVP build boundaries
* post-MVP deferrals
* engineering priorities

This skill is the roadmap planning layer for Stage 5.

---

# Inputs

```json
{
  "mvp_scope": {},
  "feature_structure": {},
  "architecture_outputs": {},
  "ux_outputs": {},
  "existing_state": {}
}
```

Read and update shared development state from:

```text
Build-Plans/Build-status/Development-state.json
```

---

# Core Responsibilities

## Roadmap Structuring

Define:

* phase names
* phase goals
* launch-critical deliverables
* deferred deliverables
* workstreams
* milestone checkpoints
* readiness criteria per phase

## Scope Alignment

Validate:

* roadmap aligns with MVP scope
* roadmap respects architecture constraints
* roadmap supports UX flows
* roadmap avoids premature non-MVP complexity

## Roadmap Risk Detection

Identify:

* oversized phases
* unclear deliverables
* missing prerequisites
* risky parallel work
* unclear milestone criteria

---

# Interactive Guidance Responsibilities

Guide the user only when roadmap scope or phase boundaries cannot be inferred safely.

Ask targeted questions when any of these are unclear:

* launch deadline or target milestone
* MVP vs post-MVP scope
* preferred phase granularity
* acceptable manual workarounds
* highest-priority user outcome
* whether risky features should be sequenced early or deferred

Infer standard roadmap phases when MVP scope and architecture are clear, but record the assumption in:

```text
interactive_guidance.assumptions_made
```

Pause for user input when roadmap scope changes release readiness, sequencing, or Stage 6 execution.

---

# Outputs

```json
{
  "development_roadmap": {},
  "workstreams": [],
  "milestones": [],
  "deferred_work": [],
  "roadmap_risks": [],
  "open_questions": []
}
```

---

# Shared State Updates

Update:

```text
development_roadmap
workstreams
milestones
execution_risks
open_questions
interactive_guidance
```

Persist updates to:

```text
Build-Plans/Build-status/Development-state.json
```

---

# Validation Responsibilities

Validate:

* every MVP feature is assigned to a roadmap phase or explicit deferral
* each phase has a purpose and readiness criteria
* architecture and UX dependencies are acknowledged
* launch-critical deliverables are not buried behind optional work
* roadmap risks are recorded with mitigation paths when high or critical

---

# Normalized Stage 5 v2 Output

Return only the canonical roadmap payload for
`01-development-roadmap.json.data.roadmap`. Use ID references for risks,
tickets, slices, agents, and batches; shared context belongs only in file `00`.
