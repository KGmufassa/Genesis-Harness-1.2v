---
name: service-boundary-architecture
description: The service-boundary-architecture skill converts system topology into service-level architecture.
compatibility: opencode
---

# Skill — service-boundary-architecture

# Purpose

The `service-boundary-architecture` skill converts system topology into service-level architecture.

It determines:

* service boundaries
* service responsibilities
* ownership domains
* communication patterns
* synchronous vs asynchronous interactions
* shared service risks

This skill is the service decomposition layer for Stage 3.

---

# Inputs

```json
{
  "system_topology": {},
  "capabilities": {},
  "dependencies": {},
  "mvp_scope": {},
  "existing_state": {}
}
```

Read and update shared architecture state from:

```text
Build-Plans/Build-status/Architecture-state.json
```

---

# Core Responsibilities

## Service Modeling

Define:

* service names
* service purpose
* responsibilities
* owned data
* upstream dependencies
* downstream dependencies
* failure modes

## Boundary Validation

Validate:

* services map to product capabilities
* service boundaries are not over-fragmented
* shared dependencies are explicit
* MVP architecture remains implementable
* future scaling needs are not blocked

## Communication Patterns

Determine:

* request-response flows
* event-driven flows
* queue usage
* background jobs
* retry and failure handling needs

---

# Interactive Guidance Responsibilities

This skill should guide the user through service boundary tradeoffs without forcing premature implementation detail.

Ask targeted questions when any of these are unclear:

* whether a capability should be isolated or kept inside a shared service
* whether a workflow requires synchronous or asynchronous processing
* whether user roles require separate permission boundaries
* whether AI, billing, notifications, or integrations require dedicated service ownership
* whether MVP simplicity should override future service separation

Infer simpler MVP-oriented boundaries when risk is low, but record the assumption in:

```text
interactive_guidance.assumptions_made
```

Pause for user input when a service boundary affects security, data ownership, scaling, or operational responsibility.

---

# Outputs

```json
{
  "service_architecture": {},
  "service_boundaries": [],
  "communication_patterns": [],
  "service_risks": [],
  "tradeoffs": []
}
```

---

# Shared State Updates

Update:

```text
service_architecture
architecture_decisions
architecture_risks
tradeoffs
interactive_guidance
```

Persist updates to:

```text
Build-Plans/Build-status/Architecture-state.json
```

---

# Validation Responsibilities

Validate:

* services support core workflows
* service responsibilities do not overlap unnecessarily
* service boundaries align with capability boundaries
* async workflows are explicit
* MVP complexity remains controlled

