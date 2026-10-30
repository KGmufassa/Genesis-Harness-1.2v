---
name: feature-behavior-specification
description: The feature-behavior-specification skill defines how product features behave in response to user actions and system conditions.
compatibility: opencode
---

# Skill — feature-behavior-specification

# Purpose

The `feature-behavior-specification` skill defines how product features behave in response to user actions and system conditions.

It determines:

* feature behavior
* user-triggered behavior
* system-triggered behavior
* validation rules
* permission behavior
* error behavior
* empty, loading, success, and failure states

This skill is the feature behavior architecture layer for Stage 4.

---

# Inputs

```json
{
  "feature_structure": {},
  "user_journeys": {},
  "interaction_architecture": {},
  "screen_system": {},
  "api_architecture": {},
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

## Behavior Specification

Define:

* feature purpose
* trigger actions
* system responses
* required inputs
* expected outputs
* validation rules
* permission checks
* error and recovery behavior

## Behavior Consistency

Validate:

* feature behavior supports journeys
* behavior aligns with APIs and data model
* behavior respects permissions
* behavior supports MVP scope
* behavior exposes clear feedback

## Behavior Risk Detection

Identify:

* ambiguous feature behavior
* missing validation rules
* unsafe destructive behavior
* unclear permissions
* hidden async states
* missing empty or error states

---

# Interactive Guidance Responsibilities

This skill should guide the user through feature behavior decisions that affect user trust, safety, and implementation clarity.

Ask targeted questions when any of these are unclear:

* what triggers a feature
* what happens after a user action
* what validation rules apply
* what users can edit, delete, submit, approve, or cancel
* how errors should be handled
* whether actions are reversible
* what states the feature must support

Infer standard behavior only when feature purpose and workflow context are clear.

Record assumptions in:

```text
interactive_guidance.assumptions_made
```

Pause for user input when feature behavior affects safety, permissions, validation, or implementation scope.

---

# Outputs

```json
{
  "feature_behaviors": {},
  "behavior_rules": [],
  "validation_rules": [],
  "permission_behaviors": [],
  "error_behaviors": [],
  "behavior_risks": []
}
```

---

# Shared State Updates

Update:

```text
feature_behaviors
ux_decisions
ux_risks
interaction_tradeoffs
interactive_guidance
```

Persist updates to:

```text
Build-Plans/Build-status/UX-state.json
```

---

# Validation Responsibilities

Validate:

* every launch-critical feature has behavior rules
* permissions and validation behavior are explicit
* loading, empty, success, error, and recovery states are represented
* behavior risks are recorded

