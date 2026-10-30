---
name: mvp-and-optimization
description: The mvp-and-optimization skill is responsible for -
compatibility: opencode
---

# Skill — mvp-and-optimization

# Purpose

The `mvp-and-optimization` skill is responsible for:

* intelligently reducing product scope
* prioritizing implementation feasibility
* minimizing engineering complexity
* preserving workflow integrity
* maintaining strategic value
* optimizing launch readiness

This skill acts as the scope reduction and operational optimization engine of the harness.

---

# Core Responsibilities

## MVP Operationalization

Determine:

* minimum viable workflows
* launch-critical systems
* required operational functionality
* non-essential systems

---

## Scope Reduction

Reduce:

* unnecessary complexity
* feature overload
* implementation risk
* infrastructure burden

while preserving:

* core user outcomes
* workflow continuity
* product value

---

## Feature Prioritization

Classify:

* must-have features
* should-have features
* optional features
* deferred features

---

## Complexity Optimization

Identify:

* high-complexity systems
* operational bottlenecks
* engineering-heavy features
* risky implementation areas

Then:

* recommend simplifications
* recommend phased rollout approaches
* suggest operational reductions

---

## Launch Readiness Optimization

Determine:

* realistic MVP boundaries
* launch feasibility
* implementation sequencing
* operational readiness

---

# Interactive Guidance Responsibilities

This skill should guide the user toward a realistic MVP.

Ask targeted questions when any of these are unclear:

* must-have user outcome
* launch-critical workflow
* features that can be deferred
* acceptable manual workarounds
* timeline constraints
* budget or complexity tolerance
* operational support limits
* launch quality expectations

Ask no more than 1-3 MVP tradeoff questions at once.

Infer simplifications when they reduce complexity without damaging the core user outcome, but record them in:

```text
interactive_guidance.assumptions_made
```

Pause for user input when:

* MVP scope is too broad
* no clear launch-critical workflow exists
* required features exceed realistic implementation complexity
* the product cannot preserve core value after scope reduction
* manual workaround acceptability is unknown

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

```json id="jlwm109"
{
  "workflows": {},
  "capabilities": {},
  "feature_groups": {},
  "dependencies": {},
  "technical_risks": [],
  "existing_state": {}
}
```

---

# Outputs

Record this skill's Stage 1 outputs in:

```text
Build-Plans/Stage-1/
```

```json id="jlwm110"
{
  "mvp_scope": {},
  "feature_priorities": {},
  "deferred_features": [],
  "launch_critical_systems": [],
  "optimization_recommendations": [],
  "complexity_reductions": [],
  "implementation_phases": {}
}
```

Write or update this file:

```text
Build-Plans/Stage-1/08-mvp-operational-model.json
```

Use `08-mvp-operational-model.json` for MVP scope, feature priorities, deferred features, launch-critical systems, implementation phases, optimization recommendations, and complexity reductions.

When recording outputs, preserve existing valid content in this file and update only the sections this skill owns.

---

# Internal Responsibilities

## Workflow Preservation

Ensure:

* MVP still delivers user value
* workflows remain operationally complete
* user outcomes remain achievable

---

## Feature Reduction Logic

Identify:

* features with low MVP value
* high-complexity low-impact systems
* unnecessary launch dependencies

---

## Engineering Complexity Detection

Examples:

* real-time systems
* advanced AI orchestration
* marketplace infrastructure
* multi-tenant enterprise systems

---

## Phased Rollout Planning

Recommend:

* post-MVP systems
* staged implementation
* progressive expansion paths

---

# Example Behaviors

## Example 1

### Product Input

```text id="jlwm111"
AI-powered collaborative design platform with:
- real-time collaboration
- AI generation
- marketplace
- social feed
- analytics
```

### MVP Optimization

```text id="jlwm112"
Recommended MVP:
- authentication
- project creation
- AI generation
- basic collaboration

Deferred:
- marketplace
- analytics
- social feed
- advanced synchronization
```

---

## Example 2

### Product Input

```text id="jlwm113"
Users upload long-form videos for AI analysis.
```

### Optimization Output

```text id="jlwm114"
Optimization Recommendations:
- limit upload duration initially
- asynchronous processing only
- defer real-time analysis
- use queued processing pipeline
```

---

# Shared State Updates

This skill updates:

```text id="jlwm115"
mvp_scope
feature_priorities
deferred_features
implementation_phases
optimization_recommendations
```

---

# Validation Responsibilities

The skill should validate:

* MVP realism
* workflow completeness
* implementation feasibility
* operational coherence
* launch viability

---

# Final Role

The `mvp-and-optimization` skill acts as:

```text id="jlwm116"
the product scope reduction and launch optimization engine
```

for the harness.

It transforms:

* oversized product visions

into:

* realistic
* coherent
* launch-ready operational MVP structures.
