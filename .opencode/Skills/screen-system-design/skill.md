---
name: screen-system-design
description: The screen-system-design skill defines the screen architecture needed to support user journeys and interactions.
compatibility: opencode
---

# Skill — screen-system-design

# Purpose

The `screen-system-design` skill defines the screen architecture needed to support user journeys and interactions.

It determines:

* screens
* screen groups
* layout responsibilities
* information hierarchy
* navigation structure
* role-based screen access
* MVP screen boundaries

This skill is the screen architecture layer for Stage 4.

---

# Inputs

```json
{
  "user_journeys": {},
  "interaction_architecture": {},
  "feature_structure": {},
  "data_architecture": {},
  "security_foundations": {},
  "existing_state": {}
}
```

Read and update shared UX state from:

```text
Build-Plans/Build-status/UX-state.json
```

---

# Core Responsibilities

## Screen Architecture

Define:

* required screens
* screen purpose
* screen inputs
* screen outputs
* screen-level user actions
* screen data requirements
* screen permissions
* screen relationships

## Screen System Consistency

Validate:

* screens map to journeys
* screens support feature behavior
* screen groups are coherent
* navigation is complete
* MVP screens are not over-scoped

## Interactive Element Mapping

Each screen must enumerate every interactive element (buttons, links, inputs) it contains:

```json
{
  "screen_id": "",
  "name": "",
  "route_or_location_hint": "",
  "owning_journey_ids": [],
  "supported_feature_ids": [],
  "role_access": [],
  "required_data": [],
  "user_actions": [],
  "system_actions": [],
  "states": [],
  "interactive_elements": [
    {
      "element_id": "",
      "element_type": "button | link | icon_button | menu_item | tab | toggle | checkbox | radio | select | text_input | search_input | file_upload | date_picker",
      "label": "",
      "route_target": "",
      "action_id": "",
      "behavior": "navigate | submit | open_modal | open_drawer | toggle | trigger_action | open_link | download | call_api | scroll_to | no_navigation",
      "behavior_target": "",
      "route_type": "internal_page | external_url | modal | drawer | anchored_section | file_download | api_action | state_transition | no_navigation",
      "permission_required": "",
      "confirmation_required": false,
      "states": {},
      "owning_component": "",
      "owning_section": ""
    }
  ],
  "responsive_requirements": [],
  "accessibility_requirement_ids": [],
  "stage_5_ticket_hints": []
}
```

Every screen's interactive_elements must be cross-referenced with the UI blueprint's section -> component -> interactive_elements hierarchy during ui-blueprint-specification.

Infer elements from upstream workflows, journeys, feature behaviors, role permissions, screen purpose, page type, state transitions, accessibility requirements, and the design-system foundation. Include non-button click targets such as cards, table rows, breadcrumbs, pagination, menus, tabs, disclosures, and modal or drawer triggers.

Do not ask the broad question "what interactive elements should be on this page?". Present an inferred inventory and request confirmation only when an element changes workflow scope, permissions, destructive behavior, navigation, accessibility, or implementation scope.

## Screen Risk Detection

Identify:

* missing screens
* redundant screens
* unclear screen ownership
* overloaded screens
* role-based access confusion
* unsupported workflow steps

---

# Interactive Guidance Responsibilities

This skill should guide the user through screen decisions that affect workflow completeness or interface consistency.

Ask targeted questions when any of these are unclear:

* whether a workflow step needs its own screen
* whether admin/operator screens are required
* which screens are MVP-critical
* how role-based access changes screens
* whether a screen should support creation, editing, review, or reporting
* whether a dashboard, detail view, or list view is needed

Infer standard screen patterns when the journey is simple and low-risk.

Record assumptions in:

```text
interactive_guidance.assumptions_made
```

Pause for user input when screen architecture affects journey completion, permissions, or Stage 5 implementation scope.

---

# Outputs

```json
{
  "screen_system": {},
  "screen_groups": [],
  "screen_inventory": [],
  "navigation_structure": {},
  "screen_risks": [],
  "open_questions": []
}
```

---

# Shared State Updates

Update:

```text
screen_system
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

* every required journey has screen support
* screen inventory maps to launch-critical features
* role-based access is represented
* screen risks are recorded
* every screen records its interactive elements with route_targets and behavior
* every interactive element references a valid route or action
* every screen in `page_inventory` or `ui_blueprints` has a matching interaction contract
* every element uses a stable `UI-ELEMENT-` ID and records a route, action, or `no_navigation` classification
* nested clickable containers and controls have unambiguous activation behavior
