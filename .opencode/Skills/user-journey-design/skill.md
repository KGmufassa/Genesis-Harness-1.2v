---
name: user-journey-design
description: The user-journey-design skill defines the main user journeys and outcome paths.
compatibility: opencode
---

# Skill — user-journey-design

# Purpose

The `user-journey-design` skill defines the main user journeys and outcome paths.

It determines:

* primary user journeys
* secondary user journeys
* entry points
* success states
* failure states
* role-specific journey differences
* MVP journey boundaries

This skill is the journey architecture layer for Stage 4.

---

# Inputs

```json
{
  "user_profiles": {},
  "workflows": {},
  "feature_structure": {},
  "mvp_scope": {},
  "existing_state": {}
}
```

Read and update shared UX state from:

```text
Build-Plans/Build-status/UX-state.json
```

---

# Core Responsibilities

## Journey Mapping

Define:

* user goals
* journey start states
* user actions
* system responses
* decision points
* success outcomes
* failure outcomes
* recovery paths

## Role and Persona Mapping

Map journeys across:

* primary users
* secondary users
* admins or operators
* guest or unauthenticated users
* permission-based user roles

## Journey Risk Detection

Identify:

* missing user goals
* unclear success states
* excessive friction
* unsupported failure recovery
* role conflicts
* MVP journey gaps

---

# Interactive Guidance Responsibilities

This skill should guide the user only when journeys cannot be inferred safely.

Ask targeted questions when any of these are unclear:

* primary user goal
* first action in the journey
* successful end state
* failure or recovery behavior
* role-specific journey differences
* whether a journey is MVP-critical or deferred

Infer common journey defaults when the workflow and user profile make them obvious, but record the assumption in:

```text
interactive_guidance.assumptions_made
```

Pause for user input when a journey decision changes screens, permissions, feature behavior, or MVP scope.

---

# Outputs

```json
{
  "user_journeys": {},
  "journey_roles": [],
  "entry_points": [],
  "success_states": [],
  "failure_states": [],
  "journey_risks": [],
  "open_questions": []
}
```

---

# Shared State Updates

Update:

```text
user_journeys
ux_decisions
ux_risks
open_questions
interactive_guidance
```

Persist updates to:

```text
Build-Plans/Build-status/UX-state.json
```

---

# Validation Responsibilities

Validate:

* every MVP workflow has a journey
* journeys have start, success, failure, and recovery paths
* role-specific differences are explicit
* journey risks are recorded

