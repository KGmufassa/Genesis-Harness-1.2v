---
name: dependency-and-risk-analysis
description: The dependency-and-risk-analysis skill is responsible for -
compatibility: opencode
---

# Skill — dependency-and-risk-analysis

# Purpose

The `dependency-and-risk-analysis` skill is responsible for:

* inferring hidden operational systems
* detecting technical dependencies
* identifying scalability concerns
* detecting operational risks
* identifying execution weaknesses
* surfacing architectural concerns early

This skill acts as the hidden systems intelligence layer of the harness.

---

# Core Responsibilities

## Dependency Detection

Infer:

* hidden supporting systems
* technical dependencies
* operational dependencies
* workflow dependencies

Examples:

* authentication
* notifications
* queues
* synchronization
* storage
* moderation
* billing systems

---

## Operational Requirement Inference

Identify:

* unseen infrastructure requirements
* supporting platform needs
* orchestration requirements
* execution dependencies

---

## Technical Risk Detection

Detect:

* scalability concerns
* system complexity risks
* infrastructure weaknesses
* integration risks
* AI reliability concerns

---

## Business Risk Detection

Identify:

* monetization uncertainty
* adoption risk
* market dependency risks
* operational feasibility concerns

---

## Compliance & Security Risk Detection

Infer:

* privacy concerns
* compliance exposure
* moderation requirements
* data handling risks

---

# Interactive Guidance Responsibilities

This skill should guide the user through hidden dependency and risk decisions.

Ask targeted questions when any of these materially affect the product model:

* authentication
* user permissions
* data storage
* file uploads
* AI processing
* payments or billing
* third-party integrations
* notifications
* moderation
* sensitive data
* compliance exposure
* audit or logging needs

Ask no more than 1-3 dependency or risk questions at once.

Infer standard dependencies when they are obvious from the workflow, but record them in:

```text
interactive_guidance.assumptions_made
```

Pause for user input when:

* sensitive data handling is unclear
* payments are possible but not confirmed
* permissions affect core workflows
* integrations are required but unspecified
* compliance risk could change the MVP boundary
* a missing dependency blocks architecture readiness

Update:

```text
interactive_guidance.open_questions
interactive_guidance.answered_questions
interactive_guidance.assumptions_made
interactive_guidance.blocked_decisions
interactive_guidance.confidence_gaps
```

---

# Inputs

```json id="jlwm102"
{
  "product_identity": {},
  "workflows": {},
  "capabilities": {},
  "feature_groups": {},
  "existing_state": {}
}
```

---

# Outputs

Record this skill's Stage 1 outputs in:

```text
Build-Plans/Stage-1/
```

```json id="jlwm103"
{
  "dependencies": {},
  "technical_risks": [],
  "business_risks": [],
  "compliance_risks": [],
  "operational_risks": [],
  "missing_systems": [],
  "risk_severity": {}
}
```

Write or update these files:

```text
Build-Plans/Stage-1/07-dependency-map.json
Build-Plans/Stage-1/09-risk-and-constraints.json
```

Use `07-dependency-map.json` for dependencies, missing systems, dependency relationships, and supporting infrastructure requirements.
Use `09-risk-and-constraints.json` for technical risks, business risks, compliance risks, operational risks, constraints, and risk severity.

When recording outputs, preserve existing valid content in these files and update only the sections this skill owns.

---

# Internal Responsibilities

## Hidden System Inference

Examples:

### Collaboration

```text id="jlwm104"
collaboration
→ permissions
→ synchronization
→ invitations
→ notifications
```

---

### AI Generation

```text id="jlwm105"
AI generation
→ queues
→ retries
→ storage
→ moderation
→ usage tracking
```

---

### Marketplace

```text id="jlwm106"
marketplace
→ payments
→ dispute handling
→ moderation
→ seller verification
```

---

## Dependency Graph Construction

Generate:

* dependency relationships
* system requirement chains
* supporting infrastructure mapping

---

## Risk Severity Classification

Classify:

* low risk
* moderate risk
* high risk
* critical risk

---

# Shared State Updates

This skill updates:

```text id="jlwm107"
dependencies
technical_risks
business_risks
compliance_risks
missing_information
risk_severity
```

---

# Validation Responsibilities

The skill should validate:

* dependency completeness
* infrastructure realism
* operational viability
* scalability assumptions
* compliance awareness

---

# Final Role

The `dependency-and-risk-analysis` skill acts as:

```text id="jlwm108"
the hidden operational systems and risk intelligence engine
```

for the harness.

It transforms:

* incomplete product assumptions

into:

* dependency-aware operational understanding
* risk-aware planning intelligence
* architecture-sensitive product models.
