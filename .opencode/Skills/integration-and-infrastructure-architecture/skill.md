---
name: integration-and-infrastructure-architecture
description: The integration-and-infrastructure-architecture skill designs the external integration model and infrastructure foundation.
compatibility: opencode
---

# Skill — integration-and-infrastructure-architecture

# Purpose

The `integration-and-infrastructure-architecture` skill designs the external integration model and infrastructure foundation.

It determines:

* integration points
* external service dependencies
* hosting model
* runtime infrastructure
* storage infrastructure
* queue and worker infrastructure
* observability foundations

This skill is the integration and infrastructure architecture layer for Stage 3.

---

# Inputs

```json
{
  "service_architecture": {},
  "data_architecture": {},
  "api_architecture": {},
  "dependency_map": {},
  "technical_feasibility": {},
  "existing_state": {}
}
```

Read and update shared architecture state from:

```text
Build-Plans/Build-status/Architecture-state.json
```

---

# Core Responsibilities

## Integration Architecture

Define:

* external APIs
* third-party services
* integration ownership
* authentication method per integration
* failure handling
* rate-limit considerations
* fallback behavior

## Infrastructure Model

Define:

* hosting approach
* compute model
* database model
* object storage needs
* queueing needs
* background worker needs
* environment strategy
* observability requirements

## Infrastructure Risk Detection

Identify:

* fragile external dependencies
* unclear deployment assumptions
* cost-sensitive infrastructure choices
* scaling bottlenecks
* operational blind spots

---

# Interactive Guidance Responsibilities

This skill should guide the user through integration and infrastructure decisions that affect feasibility, cost, or reliability.

Ask targeted questions when any of these are unclear:

* required third-party integrations
* payment, email, notification, storage, analytics, or AI providers
* whether integrations are MVP-critical or deferrable
* expected file, media, or data volume
* whether background jobs or queues are required
* whether the system needs staging, production, or multi-environment support
* whether observability is required at launch

Infer standard infrastructure defaults when they are low-risk and aligned with MVP scope.

Record assumptions in:

```text
interactive_guidance.assumptions_made
```

Pause for user input when a provider, integration, or infrastructure choice changes architecture risk or cost.

---

# Outputs

```json
{
  "integration_architecture": {},
  "infrastructure_model": {},
  "integration_risks": [],
  "infrastructure_risks": [],
  "observability_requirements": []
}
```

---

# Shared State Updates

Update:

```text
integration_architecture
infrastructure_model
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

* every required external dependency has an integration strategy
* infrastructure supports MVP scope
* async processing needs are explicit
* observability needs are recorded
* integration and infrastructure risks are recorded

