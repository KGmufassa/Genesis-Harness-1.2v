---
name: interaction-architecture-design
description: The interaction-architecture-design skill defines how users interact with product workflows and system responses.
compatibility: opencode
---

# Skill — interaction-architecture-design

# Purpose

The `interaction-architecture-design` skill defines how users interact with product workflows and system responses.

It determines:

* interaction patterns
* navigation model
* decision points
* command flows
* feedback patterns
* error and recovery interactions
* role-based interaction differences

This skill is the interaction architecture layer for Stage 4.

---

# Inputs

```json
{
  "user_journeys": {},
  "workflows": {},
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

## Interaction Model

Define:

* navigation paths
* action patterns
* confirmation patterns
* feedback and notification behavior
* user input patterns
* system response patterns
* recovery behavior

## Interaction Constraints

Map constraints from:

* system topology
* APIs
* permissions
* data ownership
* asynchronous processing
* security requirements

## Interaction Risk Detection

Identify:

* confusing flows
* missing feedback
* hidden system delays
* unsafe destructive actions
* permission ambiguity
* unsupported recovery paths

---

# Interactive Guidance Responsibilities

This skill should guide the user through interaction decisions that materially affect workflow usability.

Ask targeted questions when any of these are unclear:

* navigation model
* whether a user action needs confirmation
* how async processing should be communicated
* how errors or failed actions should be handled
* whether actions are reversible
* how users move between related workflows
* how permission limits should appear to users

Infer standard interaction defaults when risk is low, but record the assumption in:

```text
interactive_guidance.assumptions_made
```

Pause for user input when an interaction decision changes workflow completion, safety, permissions, or recovery.

---

# Outputs

```json
{
  "interaction_architecture": {},
  "navigation_model": {},
  "interaction_patterns": [],
  "feedback_patterns": [],
  "recovery_patterns": [],
  "interaction_risks": []
}
```

---

# Shared State Updates

Update:

```text
interaction_architecture
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

* interactions support user journeys
* system delays and async states have user feedback
* error and recovery paths are represented
* permission constraints are visible in interaction behavior

