---
name: design-system-foundation
description: The design-system-foundation skill defines the shared visual system that all Stage 4 UI blueprints must follow.
compatibility: opencode
---

# Skill — design-system-foundation

# Purpose

The `design-system-foundation` skill defines the shared visual system that all Stage 4 UI blueprints must follow.

It produces an implementation-ready design contract without generating frontend code.

It defines:

* design system identity
* color tokens
* typography tokens
* spacing scale
* radius rules
* elevation and shadow rules
* icon rules
* button styles
* card styles
* form styles
* table styles
* modal and drawer styles
* navigation styles
* responsive breakpoints
* visual reference handling
* design approval status

This skill turns page-level visual intent into a shared UI consistency foundation.

---

# Operating Rule

Do not generate frontend code or mockups.

Do not ask broad questions such as:

```text
What should the app look like?
```

Use structured choices and targeted confirmation questions to define a reusable design system.

---

# Visual Reference Selection

Use the visual direction library as source material for structured design decisions, not as loose inspiration.

Read first:

```text
.opencode/Skills/design-system-foundation/references/visual-direction-index.md
```

Then select the smallest useful reference set:

* one primary visual reference
* zero or one secondary visual reference as a modifier
* rejected references when they were plausible but not suitable

Read only the selected reference files after consulting the index.

Record why each selected reference fits the product category, primary users, launch-critical surfaces, density needs, accessibility constraints, and Stage 4 visual specs.

Reject references that conflict with:

* launch-critical workflow clarity
* required information density
* accessibility or contrast needs
* product trust requirements
* implementation feasibility for Stage 5

Convert selected references into design-system tokens and rules before UI blueprints apply them.

The traceability path is:

```text
visual style reference -> design system -> UI blueprint visual spec -> Stage 5 ticket -> Stage 6 visual QA
```

---

# Design System Matrix

Force the shared app design system through this matrix:

```text
DESIGN SYSTEM
Product Visual Personality
Design Style
Color System
Typography System
Spacing System
Radius System
Elevation System
Icon Style
Button Rules
Card Rules
Form Rules
Table Rules
Modal And Drawer Rules
Navigation Rules
Responsive Breakpoints
Visual References
Primary Visual Reference
Secondary Visual References
Rejected Visual References
Liked Patterns
Disliked Patterns
Accessibility Constraints
Design Do Rules
Design Don't Rules
Design Approval Status
```

---

# Inputs

```json
{
  "user_journeys": {},
  "interaction_architecture": {},
  "screen_system": {},
  "accessibility_framework": {},
  "ui_blueprints": {},
  "visual_spec_inventory": [],
  "stitch_prototyping": {},
  "existing_state": {}
}
```

Read and update shared UX state from:

```text
Build-Plans/Build-status/UX-state.json
```

---

# Outputs

Write or update:

```text
Build-Plans/Stage-4/08-design-system-foundation.json
```

The output must include:

```json
{
  "stage": "Stage 4",
  "status": "",
  "design_system": {
    "design_system_id": "",
    "product_visual_personality": "",
    "design_style": "",
    "color_tokens": {},
    "typography_tokens": {},
    "spacing_scale": {},
    "radius_rules": {},
    "elevation_rules": {},
    "icon_rules": {},
    "component_style_rules": {
      "buttons": {},
      "links": {},
      "menus": {},
      "tabs": {},
      "interactive_cards_and_rows": {},
      "cards": {},
      "forms": {},
      "tables": {},
      "modals": {},
      "drawers": {},
      "navigation": {}
    },
    "interactive_component_mapping": {
      "primary_action": "Button.Primary",
      "secondary_action": "Button.Secondary",
      "destructive_action": "Button.Destructive",
      "navigation_link": "Link.Navigation",
      "menu_item": "Menu.Item",
      "tab_item": "Tab.Item"
    },
    "interaction_state_rules": {
      "hover": {},
      "focus_visible": {},
      "pressed": {},
      "selected": {},
      "disabled": {},
      "loading": {},
      "error": {}
    },
    "responsive_breakpoints": {
      "desktop": "",
      "tablet": "",
      "mobile": "",
      "collapse_rules": [],
      "mobile_priority_content": []
    },
    "visual_references": [],
    "visual_reference_selection": {
      "primary_reference": {
        "name": "",
        "path": "",
        "selected_because": [],
        "applicable_surfaces": [],
        "token_implications": [],
        "component_implications": [],
        "accessibility_risks": []
      },
      "secondary_references": [],
      "rejected_references": []
    },
    "liked_patterns": [],
    "disliked_patterns": [],
    "accessibility_constraints": [],
    "design_do_rules": [],
    "design_dont_rules": [],
    "design_approval_status": "unconfirmed"
  },
  "ui_blueprint_alignment": [],
  "stage_5_handoff": {}
}
```

When `stitch_prototyping.visual_source_control.enabled` is true, derive visual
tokens, component visual treatment, page-level hierarchy, and responsive visual
treatment from approved Stitch screens and locked screenshot evidence where they
exist. This is visual-only input. Do not let Stitch alter product scope, routes,
actions, permissions, data/API contracts, accessibility requirements, or Stage 5
handoff fields.

Before using a Stitch-suggested visual pattern, component, data display, or
visual treatment, confirm the suggestion has an approved
`stitch_prototyping.suggestion_review_ledger` entry. Unreviewed suggestions must
remain excluded from canonical design-system output.

---

# Interactive Guidance Responsibilities

Ask the user to confirm or choose:

* product visual personality
* design style
* color direction
* typography feel
* density and spacing
* component style direction
* button hierarchy and link, menu, tab, interactive card, and row-action treatment
* destructive, disabled, loading, selected, pressed, hover, and focus-visible treatment
* visual references
* primary visual reference
* secondary visual reference when needed
* liked and disliked patterns
* approval status for the shared design system

Ask no more than 1-3 design-system questions at once.

Infer low-risk defaults only when they are strongly implied by the product category and visual specs. Record assumptions in:

```text
interactive_guidance.assumptions_made
```

Pause for user input when:

* launch-critical visual specs conflict with each other
* product visual personality is unclear
* no primary visual reference can be selected from the visual direction index
* color or typography direction is missing
* component style rules are too vague for frontend implementation
* launch-critical interactive elements cannot be mapped to a shared component treatment
* responsive breakpoints or collapse rules are missing
* design approval status is unconfirmed

---

# Shared State Updates

Update:

```text
design_system_foundation
visual_reference_selection
visual_spec_inventory
stage_5_handoff
interactive_guidance
ux_confidence_gaps
```

Persist updates to:

```text
Build-Plans/Build-status/UX-state.json
```

---

# Validation Responsibilities

Validate:

* shared design system exists for launch-critical frontend work
* design system includes color, typography, spacing, radius, elevation, icon, component, and responsive rules
* design system records selected visual references, liked patterns, disliked patterns, and accessibility constraints when provided
* selected visual references are converted into tokens, component rules, responsive rules, and accessibility constraints
* shared rules define button hierarchy, links, menus, tabs, destructive controls, disabled and loading states, focus-visible behavior, and mobile interaction affordances
* launch-critical `UI-ELEMENT-` entries map to a design-system component treatment or record an intentional deviation
* rejected visual references include a reason when they were plausible candidates
* launch-critical UI blueprints reference or align with the design system
* design approval status is recorded
* Stage 5 can consume the design system without inventing visual direction
* no frontend code is generated
