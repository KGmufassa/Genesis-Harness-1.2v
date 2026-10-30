---
name: system-topology-design
description: The system-topology-design skill defines the high-level technical system shape.
compatibility: opencode
---

# Skill — system-topology-design

# Purpose

The `system-topology-design` skill defines the high-level technical system shape.

It determines:

* primary systems
* subsystems
* runtime boundaries
* user-facing vs backend systems
* internal operational systems
* AI or automation systems
* external system touchpoints

This skill is the topology design layer for Stage 3.

---

# Inputs

```json
{
  "stage_1_inputs": {},
  "stage_2_inputs": {},
  "existing_state": {}
}
```

Read and update shared architecture state from:

```text
Build-Plans/Build-status/Architecture-state.json
```

---

# Core Responsibilities

## Topology Design

Identify:

* frontend applications
* backend services
* databases
* queues
* workers
* AI services
* storage systems
* notification systems
* admin or operational tooling
* external integrations

## Architecture Drivers

Extract architecture drivers from:

* validated assumptions
* workflows
* capabilities
* MVP scope
* dependency map
* risk validation
* scalability needs

## Boundary Mapping

Define:

* system boundaries
* data flow boundaries
* trust boundaries
* ownership boundaries
* external dependency boundaries

---

# Interactive Guidance Responsibilities

This skill should guide the user only when the high-level system shape cannot be inferred safely.

Ask targeted questions when any of these are unclear:

* whether the product needs one app or multiple apps
* whether admin or operator tooling is required
* whether AI processing is synchronous or asynchronous
* whether collaboration requires real-time architecture
* which external systems are mandatory for MVP
* whether user-facing and internal systems need separate boundaries

Infer standard topology defaults when the product category and MVP scope make them obvious, but record the assumption in:

```text
interactive_guidance.assumptions_made
```

Pause for user input when the topology choice changes service boundaries, infrastructure, or Stage 4 handoff.

---

# Outputs

```json
{
  "system_topology": {},
  "architecture_drivers": [],
  "system_boundaries": [],
  "topology_risks": [],
  "open_questions": []
}
```

---

# Shared State Updates

Update:

```text
system_topology
architecture_drivers
architecture_risks
open_questions
interactive_guidance
```

Persist updates to:

```text
Build-Plans/Build-status/Architecture-state.json
```

---

# Validation Responsibilities

Validate:

* every major capability has a system placement
* MVP scope is supported by the topology
* Stage 2 technical feasibility constraints are represented
* external dependency boundaries are explicit
* trust and data flow boundaries are visible

