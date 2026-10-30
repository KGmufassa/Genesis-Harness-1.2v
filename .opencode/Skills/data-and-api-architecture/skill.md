---
name: data-and-api-architecture
description: The data-and-api-architecture skill designs the data model and API architecture.
compatibility: opencode
---

# Skill — data-and-api-architecture

# Purpose

The `data-and-api-architecture` skill designs the data model and API architecture.

It determines:

* core entities
* data ownership
* persistence needs
* read/write patterns
* API surfaces
* API contracts
* data lifecycle

This skill is the data and API architecture layer for Stage 3.

---

# Inputs

```json
{
  "system_topology": {},
  "service_architecture": {},
  "workflows": {},
  "feature_structure": {},
  "security_requirements": {},
  "existing_state": {}
}
```

Read and update shared architecture state from:

```text
Build-Plans/Build-status/Architecture-state.json
```

---

# Core Responsibilities

## Data Architecture

Define:

* domain entities
* entity relationships
* data ownership by service
* persistence model
* data lifecycle
* audit and history needs
* privacy-sensitive data

## API Architecture

Define:

* API boundaries
* primary endpoints or operations
* request/response concepts
* authentication and authorization requirements
* external API exposure
* internal API usage

## Data Risk Detection

Identify:

* unclear data ownership
* excessive coupling
* sensitive data exposure
* missing auditability
* reporting or analytics data needs
* schema evolution risks

---

# Interactive Guidance Responsibilities

This skill should guide the user through data ownership, sensitive data, and API exposure decisions.

Ask targeted questions when any of these are unclear:

* which entities are core business objects
* who owns or can modify critical data
* whether sensitive or regulated data is present
* whether audit history is required
* whether APIs are internal only or externally exposed
* whether users need exports, imports, or reporting access
* whether data must support real-time collaboration

Infer standard CRUD-style data and API structures only when the workflow is simple and low-risk.

Record assumptions in:

```text
interactive_guidance.assumptions_made
```

Pause for user input when data ownership, privacy, auditability, or external API exposure is unclear.

---

# Outputs

```json
{
  "data_architecture": {},
  "api_architecture": {},
  "data_entities": [],
  "api_surfaces": [],
  "data_risks": [],
  "open_questions": []
}
```

---

# Shared State Updates

Update:

```text
data_architecture
api_architecture
architecture_decisions
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

* core workflows have supporting data entities
* data ownership is explicit
* APIs support required workflows
* sensitive data is identified
* data and API risks are recorded

