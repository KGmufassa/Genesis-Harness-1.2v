---
name: security-and-scalability-architecture
description: The security-and-scalability-architecture skill defines security foundations and scalability strategy.
compatibility: opencode
---

# Skill — security-and-scalability-architecture

# Purpose

The `security-and-scalability-architecture` skill defines security foundations and scalability strategy.

It determines:

* authentication foundations
* authorization model
* data protection needs
* trust boundaries
* compliance-sensitive controls
* scalability bottlenecks
* performance strategy
* resilience strategy

This skill is the security and scalability architecture layer for Stage 3.

---

# Inputs

```json
{
  "system_topology": {},
  "service_architecture": {},
  "data_architecture": {},
  "api_architecture": {},
  "infrastructure_model": {},
  "risk_validation": {},
  "existing_state": {}
}
```

Read and update shared architecture state from:

```text
Build-Plans/Build-status/Architecture-state.json
```

---

# Core Responsibilities

## Security Foundations

Define:

* authentication model
* authorization model
* roles and permissions
* sensitive data handling
* audit logging needs
* trust boundaries
* abuse and moderation controls
* compliance considerations

## Scalability Framework

Define:

* expected load assumptions
* scaling bottlenecks
* performance-sensitive workflows
* caching needs
* async processing needs
* AI or compute cost scaling
* resilience and failure handling

## Security and Scalability Risks

Identify:

* missing access controls
* unclear privacy requirements
* expensive scaling paths
* single points of failure
* data exposure risks
* unbounded AI usage

---

# Interactive Guidance Responsibilities

This skill should guide the user through security and scale decisions that materially affect architecture.

Ask targeted questions when any of these are unclear:

* authentication requirements
* user roles and permissions
* sensitive data handling
* audit logging needs
* abuse, moderation, or rate-limit needs
* expected user or request volume
* AI usage limits
* performance-sensitive workflows
* resilience expectations

Infer standard security foundations only when the product has simple user roles and no sensitive data exposure.

Record assumptions in:

```text
interactive_guidance.assumptions_made
```

Pause for user input when access control, privacy, compliance, scale, or abuse prevention is unclear.

---

# Outputs

```json
{
  "security_foundations": {},
  "scalability_framework": {},
  "security_risks": [],
  "scalability_risks": [],
  "architecture_warnings": []
}
```

---

# Shared State Updates

Update:

```text
security_foundations
scalability_framework
architecture_risks
architecture_decisions
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

* authentication and authorization foundations exist
* sensitive data controls are identified
* trust boundaries are explicit
* scalability risks are recorded
* security controls map to Stage 2 risk validation

