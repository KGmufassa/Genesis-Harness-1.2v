---
name: release-plan-orchestration
description: Define the canonical Stage 5 release plan and readiness gates.
compatibility: opencode
---

# Skill — release-plan-orchestration

# Purpose

The `release-plan-orchestration` skill defines rollout sequencing and release readiness.

It determines:

* release phases
* launch scope
* rollout gates
* release readiness criteria
* deployment preparation needs
* rollback and recovery planning
* Stage 7 handoff implications

This skill is the release orchestration layer for Stage 5.

---

# Inputs

```json
{
  "development_roadmap": {},
  "implementation_sequence": {},
  "engineering_dependencies": {},
  "testing_strategy": {},
  "build_tickets": {},
  "agent_assignment_plan": {},
  "parallel_execution_plan": {},
  "mvp_scope": {},
  "existing_state": {}
}
```

Read and update shared development state from:

```text
Build-Plans/Build-status/Development-state.json
```

---

# Core Responsibilities

## Release Planning

Define:

* release phases
* MVP launch package
* launch gates
* release checklist
* rollout sequencing
* rollback requirements
* operational readiness needs

## Release Risk Detection

Identify:

* launch-blocking dependencies
* missing readiness criteria
* unsupported rollback
* fragile integrations
* unclear support expectations
* monitoring gaps

## Stage 7 Handoff Awareness

Prepare:

* deployment preparation notes
* monitoring needs
* analytics needs
* support needs
* operational tooling needs

---

# Interactive Guidance Responsibilities

Guide the user through release decisions that affect launch readiness and Stage 7 operationalization.

Ask targeted questions when any of these are unclear:

* whether release should be private, beta, staged, or public
* what must be included in MVP launch
* what can be released after launch
* what conditions block release
* whether rollback or manual recovery is required
* what monitoring or support is needed at launch

Infer a conservative staged rollout when risk is moderate and launch constraints are unclear, but record the assumption in:

```text
interactive_guidance.assumptions_made
```

Pause for user input when release strategy changes implementation scope, testing scope, or operational readiness.

---

# Outputs

```json
{
  "release_plan": {},
  "release_phases": [],
  "release_gates": [],
  "rollback_requirements": [],
  "stage_7_handoff_notes": {},
  "release_risks": []
}
```

---

# Shared State Updates

Update:

```text
release_plan
execution_risks
coordination_notes
stage_6_handoff
interactive_guidance
```

Persist updates to:

```text
Build-Plans/Build-status/Development-state.json
```

---

# Validation Responsibilities

Validate:

* release gates align with testing strategy
* MVP launch package aligns with roadmap and implementation sequence
* build tickets support the release gates and launch package
* agent assignment plan supports release ownership and validation responsibilities
* parallel execution plan supports release sequencing, merge strategy, and batch validation gates
* rollback or recovery expectations are explicit
* Stage 7 handoff needs are captured
* release-blocking risks include mitigation or escalation paths

---

# Normalized Stage 5 v2 Output

Keep all release collections inside
`08-release-plan.json.data.release_plan`. Release views use IDs or compact
indexes and `risk_refs`; completion and the Stage 6 handoff belong only in the
manifest.
