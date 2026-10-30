---
name: product-intelligence
description: The product-intelligence skill interprets raw product intent and turns it into the first structured Stage 1 product model.
compatibility: opencode
---

# Skill — product-intelligence

# Purpose

The `product-intelligence` skill interprets raw product intent and turns it into the first structured Stage 1 product model.

It identifies:

* product identity
* product category
* strategic intent
* target users
* user needs
* success criteria
* planning ambiguity
* clarification questions

This skill is the first discovery layer for Stage 1. It must not perform market validation, system architecture, UX design, implementation planning, or build execution.

---

# PRD Docs Preflight

Before using `raw_product_intent`, user notes, conversation context, or intake questions, inspect:

```text
System-References/PRD Docs/
```

If this folder contains any readable files, treat those files as the primary product-intelligence source. Read all supported text-based PRD files in the folder, including nested files, and extract initial product details, target users, product features, constraints, success criteria, and open questions.

Supported PRD source files include:

```text
.md
.mdx
.txt
.json
.yaml
.yml
.csv
```

When PRD Docs contains readable source files:

* prefer PRD evidence over generic inference
* preserve source references to the PRD file paths
* use conversation context only to fill gaps or resolve ambiguity
* ask clarification questions only for gaps that remain after reading the PRD files
* record contradictions between PRD files and user notes in `interactive_guidance.confidence_gaps`

If `System-References/PRD Docs/` is empty or contains no readable supported files, continue with the original workflow using `raw_product_intent`, user notes, existing state, and targeted intake questions.

---

# Core Responsibilities

## Product Identity

Define:

* product name or working title
* product type
* product category
* core problem
* core promise
* primary user outcome

## User And Outcome Mapping

Identify:

* primary users
* secondary users
* user motivations
* user pain points
* desired outcomes
* success indicators

## Strategic Intent

Clarify:

* why the product should exist
* what must be true for the product to matter
* which user behavior the product depends on
* what should be excluded from the initial product concept

## Ambiguity Detection

Detect:

* vague product goals
* missing user roles
* unclear success criteria
* conflicting product direction
* unsupported assumptions

---

# Interactive Guidance Responsibilities

Ask targeted questions when product identity, users, user outcomes, or success criteria are unclear.

Ask no more than 1-3 questions at once.

Infer common product attributes when they are obvious from the user's description, but record them in:

```text
interactive_guidance.assumptions_made
```

Pause for user input when:

* the core product problem is unclear
* the primary user cannot be identified
* success criteria would materially change product direction
* conflicting product goals cannot be reconciled

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

```json
{
  "raw_product_intent": "",
  "user_notes": {},
  "existing_state": {}
}
```

---

# Outputs

Record this skill's Stage 1 outputs in:

```text
Build-Plans/Stage-1/
```

```json
{
  "product_identity": {},
  "product_category": {},
  "strategic_intent": {},
  "user_profiles": [],
  "user_needs": [],
  "success_criteria": [],
  "clarification_questions": [],
  "assumptions": []
}
```

Write or update these files:

```text
Build-Plans/Stage-1/01-product-foundation.json
Build-Plans/Stage-1/02-user-system-map.json
Build-Plans/Stage-1/10-success-framework.json
```

Use `01-product-foundation.json` for product identity, category, strategic intent, product problem, and product promise.
Use `02-user-system-map.json` for users, roles, needs, motivations, and outcome relationships.
Use `10-success-framework.json` for success criteria, outcome indicators, and early measurement assumptions.

Preserve existing valid content and update only the sections this skill owns.
