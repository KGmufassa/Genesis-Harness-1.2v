---
name: state-transition-and-accessibility-design
description: The state-transition-and-accessibility-design skill defines user-visible state transitions and accessibility foundations.
compatibility: opencode
---

# Skill — state-transition-and-accessibility-design

# Purpose

The `state-transition-and-accessibility-design` skill defines user-visible state transitions and accessibility foundations.

It determines:

* workflow states
* screen states
* feature states
* transition triggers
* loading and async states
* accessibility requirements
* inclusive interaction constraints

This skill is the state and accessibility architecture layer for Stage 4.

---

# Inputs

```json
{
  "user_journeys": {},
  "interaction_architecture": {},
  "screen_system": {},
  "feature_behaviors": {},
  "security_foundations": {},
  "existing_state": {}
}
```

Read and update shared UX state from:

```text
Build-Plans/Build-status/UX-state.json
```

---

# Core Responsibilities

## State Transition Mapping

Define:

* start states
* intermediate states
* success states
* failure states
* loading states
* empty states
* permission-denied states
* transition triggers

## Accessibility Framework

Define:

* keyboard interaction requirements
* screen reader expectations
* focus management needs
* contrast and readability needs
* form accessibility requirements
* error messaging accessibility
* motion and animation constraints

## State and Accessibility Risk Detection

Identify:

* missing state transitions
* unclear loading behavior
* inaccessible interaction patterns
* missing focus or keyboard behavior
* unclear error messaging
* visual-only feedback risks

---

# Interactive Guidance Responsibilities

This skill should guide the user through state and accessibility decisions that affect task completion and inclusive use.

Ask targeted questions when any of these are unclear:

* what states a workflow can enter
* how users know something is processing
* how users recover from failure
* whether keyboard-only use is required
* whether screen reader support is required
* whether motion, timing, or contrast constraints matter
* how permission-denied or unavailable states should behave

Infer baseline accessibility requirements as required, not optional.

Record assumptions in:

```text
interactive_guidance.assumptions_made
```

Pause for user input when a state or accessibility decision affects core task completion or legal/compliance expectations.

---

# Outputs

```json
{
  "state_transition_map": {},
  "workflow_states": [],
  "screen_states": [],
  "feature_states": [],
  "accessibility_framework": {},
  "accessibility_risks": []
}
```

---

# Shared State Updates

Update:

```text
state_transition_map
accessibility_framework
ux_decisions
ux_risks
interactive_guidance
```

Persist updates to:

```text
Build-Plans/Build-status/UX-state.json
```

---

# Validation Responsibilities

Validate:

* every core workflow has visible states
* error and recovery behavior is represented
* accessibility requirements are baseline requirements
* accessibility risks are recorded

