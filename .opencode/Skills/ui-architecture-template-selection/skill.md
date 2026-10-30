---
name: ui-architecture-template-selection
description: The ui-architecture-template-selection skill selects the structural UI architecture template and extensions that ui-blueprint-specification should use when generating page/component blueprints.
compatibility: opencode
---

# Skill — ui-architecture-template-selection

# Purpose

The `ui-architecture-template-selection` skill selects the structural UI architecture template and extensions that `ui-blueprint-specification` should use when generating page/component blueprints.

It defines:

* primary UI architecture template
* selected extensions
* page archetype defaults
* navigation pattern defaults
* layout pattern defaults
* component-family guidance
* template deviations and override reasons

This skill is the structural template-selection layer for Stage 4. It does not generate frontend code, final visual styling, or implementation tickets.

---

# Reference Library

Read the library index first:

```text
.opencode/Skills/ui-blueprint-specification/references/ui-component-system/README.md
.opencode/Skills/ui-blueprint-specification/references/ui-component-system/TEMPLATE-SELECTOR.md
.opencode/Skills/ui-blueprint-specification/references/ui-component-system/NORMALIZED-VALUES.md
.opencode/Skills/ui-blueprint-specification/references/ui-component-system/PRECEDENCE-RULES.md
.opencode/Skills/ui-blueprint-specification/references/ui-component-system/TEMPLATE-REGISTRY.md
```

Then load only the selected primary template, selected extensions, and directly relevant patterns.

Normal Stage 4 runs must treat the library as read-only. If a run discovers a missing pattern, conflicting rule, or bad recommendation, record a template gap or deviation in Stage 4 state.

---

# Inputs

```json
{
  "stage_1_inputs": {},
  "stage_2_inputs": {},
  "stage_3_inputs": {},
  "user_journeys": {},
  "interaction_architecture": {},
  "screen_system": {},
  "feature_behaviors": {},
  "state_transition_map": {},
  "accessibility_framework": {},
  "design_system_foundation": {},
  "existing_state": {}
}
```

Read and update shared UX state from:

```text
Build-Plans/Build-status/UX-state.json
```

---

# Selection Responsibilities

Determine:

* product category
* primary platform
* primary user behavior
* dominant workflow
* content type
* information density
* comparison needs
* collaboration level
* transaction model
* session frequency

Select one primary template:

```text
marketing-website
saas-dashboard
ecommerce-storefront
mobile-utility
```

Select relevant extensions only when upstream product/workflow evidence justifies them:

```text
analytics
role-based-access
onboarding
billing
collaboration
messaging
file-management
```

Apply precedence:

```text
1. project-specific requirements
2. explicit project overrides
3. selected extensions
4. primary template
5. base template
```

---

# Output Shape

Update shared UX state with:

```json
{
  "ui_architecture_template_selection": {
    "primary_template": "",
    "confidence": "high | medium | low",
    "alternative_templates": [],
    "selected_extensions": [],
    "reasons": [],
    "unresolved_questions": [],
    "template_deviations": [],
    "template_gaps": [],
    "source_refs": []
  }
}
```

Template deviations must include:

```json
{
  "subject": "",
  "template_default": "",
  "project_choice": "",
  "reason": "",
  "source_refs": []
}
```

Template gaps must include:

```json
{
  "gap": "",
  "project_context": "",
  "recommended_resolution": "",
  "source_refs": []
}
```

---

# Interactive Guidance Responsibilities

Ask the user only when:

* primary template confidence is low
* two templates would produce materially different page inventory or navigation
* an extension would add launch-critical pages or workflows not clearly supported by upstream inputs
* a project override changes navigation, page archetype, layout pattern, or Stage 5 frontend scope

Otherwise infer the template and extensions from upstream product, workflow, role, platform, and journey evidence. Record assumptions in:

```text
interactive_guidance.assumptions_made
```

---

# Shared State Updates

Update:

```text
ui_architecture_template_selection
ux_decisions
ux_risks
open_questions
interactive_guidance
```

Persist updates to:

```text
Build-Plans/Build-status/UX-state.json
```

---

# Validation Responsibilities

Validate:

* one primary template is selected or a blocking reason is recorded
* selected extensions are compatible with the primary template or a deviation is recorded
* template reasons cite upstream product, workflow, role, platform, journey, feature, or route evidence
* project-specific requirements override template defaults when they conflict
* no template default silently changes Stage 1 product scope or Stage 3 architecture
* template gaps are recorded instead of modifying the library during normal Stage 4 execution

