---
name: workflow-and-capability-synthesis
description: The workflow-and-capability-synthesis skill is responsible for transforming -
compatibility: opencode
---

# Skill — workflow-and-capability-synthesis

# Purpose

The `workflow-and-capability-synthesis` skill is responsible for transforming:

* user goals
* operational intentions
* product behaviors

into:

* structured workflows
* operational product systems
* capability architecture
* feature structures
* operational product topology

This skill acts as the operational decomposition engine of the harness.

---

# Core Responsibilities

## Workflow Inference

Infer:

* user flows
* operational sequences
* system interactions
* product journeys

---

## Capability Categorization

Identify:

* major product systems
* operational domains
* system groupings
* platform capabilities

Examples:

* Authentication
* AI Processing
* Collaboration
* Notifications
* Payments
* Analytics

---

## Feature Structuring

Organize:

* concrete functionality
* feature groups
* capability-linked features
* feature relationships

---

## Workflow Normalization

Transform:

* vague flows
* duplicated actions
* inconsistent behaviors

into:

* coherent operational workflows

---

## Operational Boundary Detection

Identify:

* system boundaries
* ownership domains
* operational separations
* capability segmentation

---

# Interactive Guidance Responsibilities

This skill should guide the user from product intent into concrete operational workflows.

Ask targeted questions when any of these are unclear:

* primary workflow
* workflow start state
* workflow end state
* user roles
* required user actions
* required system actions
* collaboration requirements
* workflow frequency
* feature boundaries

Ask no more than 1-3 workflow questions at once.

Infer common workflow steps when they are standard for the product category, but record them in:

```text
interactive_guidance.assumptions_made
```

Pause for user input when:

* the core workflow cannot be inferred
* user roles change the workflow architecture
* collaboration or permissions materially affect the product model
* the boundary between features and capabilities is unclear

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

```json id="jlwm94"
{
  "product_identity": {},
  "user_profiles": {},
  "strategic_intent": {},
  "recommendations": {},
  "existing_state": {}
}
```

---

# Outputs

Record this skill's Stage 1 outputs in:

```text
Build-Plans/Stage-1/
```

```json id="jlwm95"
{
  "workflows": {},
  "capabilities": {},
  "feature_groups": {},
  "operational_boundaries": {},
  "workflow_relationships": {},
  "capability_dependencies": {}
}
```

Write or update these files:

```text
Build-Plans/Stage-1/03-workflow-architecture.json
Build-Plans/Stage-1/04-product-capabilities.json
Build-Plans/Stage-1/05-feature-structure.json
Build-Plans/Stage-1/06-product-boundaries.json
```

Use `03-workflow-architecture.json` for workflows, journeys, workflow sequencing, and workflow relationships.
Use `04-product-capabilities.json` for capability groups, operational domains, and capability dependencies.
Use `05-feature-structure.json` for feature groups, feature relationships, and capability-linked functionality.
Use `06-product-boundaries.json` for operational boundaries, system boundaries, and ownership separations.

When recording outputs, preserve existing valid content in these files and update only the sections this skill owns.

---

# Internal Responsibilities

## User Outcome Mapping

Determine:

* what users are trying to achieve
* workflow goals
* operational success states

---

## Workflow Sequencing

Map:

* start states
* user actions
* system actions
* end states

---

## Capability Architecture

Generate:

* major product systems
* operational groupings
* platform domains

---

## Feature Relationship Mapping

Identify:

* feature grouping
* feature overlap
* shared dependencies
* operational coupling

---

# Example Behaviors

## Example 1

### User Input

```text id="jlwm96"
"Users can create shared trip itineraries."
```

### Skill Output

```text id="jlwm97"
Workflow:
Create Trip
→ Invite Members
→ Add Itinerary Items
→ Share Updates
→ Finalize Trip

Capabilities:
- Trip Management
- Collaboration
- Notifications

Features:
- itinerary editing
- shared access
- trip invitations
- itinerary comments
```

---

## Example 2

### User Input

```text id="jlwm98"
"Users upload videos for AI analysis."
```

### Skill Output

```text id="jlwm99"
Capabilities:
- Media Management
- AI Processing
- Storage System

Features:
- upload videos
- process analysis
- display results
- save history
```

---

# Shared State Updates

This skill updates:

```text id="jlwm100"
workflows
capabilities
feature_groups
operational_boundaries
workflow_relationships
```

---

# Validation Responsibilities

The skill should validate:

* workflow coherence
* feature alignment
* capability completeness
* operational consistency
* workflow sequencing integrity

---

# Final Role

The `workflow-and-capability-synthesis` skill acts as:

```text id="jlwm101"
the operational product decomposition and structuring engine
```

for the harness.

It transforms:

* strategic product thinking

into:

* operational product systems
* structured workflows
* capability architecture
* feature topology.
