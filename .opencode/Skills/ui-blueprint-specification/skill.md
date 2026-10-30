---
name: ui-blueprint-specification
description: The ui-blueprint-specification skill transforms Stage 4 UX requirements into implementation-ready UI blueprints without generating frontend code.
compatibility: opencode
---

# Skill — ui-blueprint-specification

# Purpose

The `ui-blueprint-specification` skill transforms Stage 4 UX requirements into implementation-ready UI blueprints without generating frontend code.

It defines:

* pages
* screens
* layouts
* components
* UI architecture template and extension usage
* page archetypes
* layout pattern decisions
* component-family decisions
* navigation
* user actions
* forms
* tables
* cards
* modals
* drawers
* loading states
* empty states
* error states
* frontend build package inputs

This skill is the bridge between Stage 4 UX architecture and Stage 5 frontend implementation planning.

It consumes the selected Stage 4 design system and visual references from `design-system-foundation`. It applies those decisions per page instead of inventing a separate visual direction for each blueprint.

It also consumes the selected structural UI architecture template and extensions from `ui-architecture-template-selection`. It applies those references to page archetype, layout pattern, component family, responsive, state, and accessibility decisions without replacing Stage 4's stable UI blueprint, route, action, and interactive element contracts.

When Stitch visual source control is enabled, this skill may use approved Stitch
screens and locked screenshot evidence as visual-only guidance for page visual
hierarchy, component visual treatment, and responsive visual treatment. It must
not use Stitch to add or change product scope, routes, actions, permissions,
data/API contracts, accessibility requirements, or Stage 5 handoff fields.

---

# Operating Rule

Do not ask broad questions such as:

```text
What should this dashboard look like?
```

Force every launch-critical page through the page-definition matrix:

```text
PAGE
Purpose
Primary User
Screen Type
Page Archetype
Layout Type
Layout Pattern Decision
Sections
Components
Component Family Decisions
Actions
Data Needed
States
Validation
Navigation
```

Then force every launch-critical page through the visual spec matrix:

```text
VISUAL SPEC
Visual Style
Design System Refs
Visual Reference Refs
Density
Color Direction
Typography Feel
Component Style
Primary Visual Focus
Responsive Behavior
Visual Do Rules
Visual Don't Rules
Reference Apps
Design System Alignment
Visual Acceptance Criteria
User Approval Status
Stitch Visual Source Refs
Reviewed Stitch Suggestion Refs
```

---

# Controlled Choices

Before selecting page archetypes, layout patterns, or component families, read the UI component system library:

```text
.opencode/Skills/ui-blueprint-specification/references/ui-component-system/README.md
.opencode/Skills/ui-blueprint-specification/references/ui-component-system/NORMALIZED-VALUES.md
.opencode/Skills/ui-blueprint-specification/references/ui-component-system/PRECEDENCE-RULES.md
.opencode/Skills/ui-blueprint-specification/references/ui-component-system/OUTPUT-CHECKLIST.md
.opencode/Skills/ui-blueprint-specification/references/ui-component-system/CONTRADICTION-RULES.md
```

Then load only the selected primary template, selected extensions, and directly relevant layout, page, interaction, navigation, and state pattern references.

Screen type options:

```text
Dashboard
List
Detail View
Form
Wizard
Settings
Profile
Analytics
Messaging
Landing Page
Hero Page
Marketing Page
Onboarding
Pricing
Authentication
Admin
Checkout
Custom
```

Screen/page type selection must be contextual.

These options are a controlled vocabulary, not a required checklist. Include only page or screen types justified by:

* Stage 1 product category and MVP scope
* Stage 1 workflows and feature structure
* Stage 3 selected stack and architecture constraints
* Stage 4 user journeys and launch-critical interactions
* user roles, permissions, and navigation needs

Do not add `Landing Page`, `Hero Page`, `Dashboard`, `Admin`, `Checkout`, `Authentication`, `Pricing`, or any other page type unless the product model requires it.

For each selected page type, record:

```json
{
  "page_name": "",
  "screen_type": "",
  "included_because": [],
  "source_refs": [],
  "excluded_page_types": [
    {
      "screen_type": "",
      "reason": ""
    }
  ]
}
```

Ask the user only when a launch-critical page type is ambiguous. Otherwise infer the page type from upstream workflow, role, feature, and route evidence, and record the assumption.

Layout type options:

```text
Sidebar
Top Navigation
Split View
Card Grid
Table
Mobile First
Full Screen
Custom
```

Layout pattern options:

```text
single-column
two-column
responsive-grid
dashboard-grid
card-grid
data-table
content-list
master-detail
split-pane
form-layout
settings-layout
custom
```

Use `data-table` for dense comparable records, sorting, filtering, pagination, and bulk actions.

Use `card-grid` for visual browsing, media-rich items, summaries, and non-uniform item content.

Use `content-list` for chronological scanning, activity, messages, or simple repeated records.

Use `master-detail` when users browse records while repeatedly inspecting or editing one selected item.

Use `dashboard-grid` for metric, chart, alert, and operational summary surfaces.

Use `form-layout` for create, edit, setup, review, or submission workflows.

Use `settings-layout` for grouped preferences, integrations, permissions, billing, or account configuration.

Use `split-pane` when two related work surfaces must remain visible together.

Component options:

```text
Cards
Charts
Tables
Search
Filters
Forms
Tabs
Modals
Drawers
Notifications
File Upload
Comments
Timeline
Maps
Calendar
```

Component family options:

```text
navigation
actions
forms
data-display
feedback
overlays
search-and-filtering
analytics
commerce
collaboration
file-management
messaging
```

Action options:

```text
Create
Read
Update
Delete
Export
Share
Invite
Approve
Reject
Upload
Download
```

Visual style options:

```text
Minimal
Enterprise
Editorial
Consumer App
SaaS Dashboard
Data Dense
Playful
Luxury
Utility
Custom
```

Density options:

```text
Compact
Balanced
Spacious
Data Dense
Mobile First
Custom
```

Component style options:

```text
Flat
Outlined
Soft Card
High Contrast
Dense Utility
Media Rich
Custom
```

---

# Complete App Blueprint Markdown

Generate a readable complete app blueprint tree at:

```text
Build-Plans/Stage-4/09-complete-app-blueprint.md
```

The markdown tree must use this structure, adapted to the app being built. The example page names below are illustrative only; the generated tree must include the pages required by the actual product:

```text
Complete App Blueprint
│
├── Pages
│   ├── Example Landing Page
│   │   ├── Hero
│   │   ├── Feature Preview
│   │   ├── CTA
│   │   └── Footer
│   ├── Example Dashboard
│   │   ├── Summary Cards
│   │   ├── Activity Feed
│   │   └── Task Table
│
├── Components
│
├── Shared Components
│
├── Navigation
│
├── Routes
│
├── Actions
│
├── States
│
├── Data Requirements
│
└── Frontend Build Package
```

Every launch-critical page in the markdown tree must map to a `ui_blueprint_id` and include its sections, components, primary actions, route, states, and data requirements.

The complete app blueprint must also include:

* one compact Mermaid app route map covering every created page
* page-level Mermaid interaction maps for launch-critical or complex pages
* critical workflow Mermaid maps that include success, failure, and recovery branches
* destructive or mutation Mermaid maps that include confirmation and result states

Require a page-level Mermaid map when a page has multiple interaction branches, destructive or mutation actions, modal or drawer flows, or complex routing. A trivial page may rely on its interaction contract and inventories when the app route map already covers it.

---

# Visual Hierarchy Model

Each page blueprint must preserve:

```text
Page
├─ Section
│  ├─ Component
│  │  ├─ Interactive Element
│  │  │  └─ Route, Action, Or No Navigation
│  │  ├─ Data Source
│  │  ├─ Validation
│  │  └─ States
```

---

# Interactive Element Schema

Every interactive element on a page (button, link, icon button, menu item, tab, input, etc.) must be enumerated with:

```json
{
  "element_id": "UI-ELEMENT-001",
  "element_type": "button | link | icon_button | menu_item | tab | toggle | checkbox | radio | select | text_input | search_input | file_upload | date_picker | breadcrumb | pagination | clickable_card | clickable_row | disclosure",
  "label": "",
  "accessible_name": "",
  "icon": "",
  "owning_page_ref": "",
  "owning_section_ref": "",
  "owning_component_ref": "",
  "route_id": "",
  "route_target": "",
  "route_type": "internal_page | external_url | modal | drawer | anchored_section | file_download | api_action | state_transition | no_navigation",
  "action_id": "ACTION-001",
  "behavior": "navigate | submit | open_modal | open_drawer | toggle | trigger_action | open_link | download | call_api | scroll_to | no_navigation",
  "behavior_target": "",
  "design_system_component": "",
  "states": {
    "default": {},
    "loading": {},
    "disabled": {},
    "active": {},
    "hover": {}
  },
  "permission_required": "",
  "permission_denied_behavior": "",
  "confirmation_required": false,
  "responsive_behavior": {},
  "accessibility_behavior": {},
  "analytics_event": "",
  "source_trace": []
}
```

# Action Inventory Schema

Every action across all pages must be recorded in a global action inventory:

```json
{
  "action_id": "ACTION-001",
  "name": "",
  "element_type": "button | link | icon_button | menu_item | tab | toggle | checkbox | radio | select",
  "label": "",
  "route_target": "",
  "behavior": "navigate | submit | open_modal | open_drawer | toggle | trigger_action | open_link | download | call_api | scroll_to",
  "behavior_target": "",
  "owning_page_refs": [],
  "owning_component_refs": [],
  "triggering_element_refs": [],
  "permission_required": "",
  "confirmation_required": false,
  "success_destination": "",
  "failure_destination": "",
  "loading_state": "",
  "empty_state": "",
  "permission_denied_behavior": "",
  "undo_or_recovery_path": "",
  "states": {},
  "analytics_event": "",
  "source_trace": []
}
```

# Route Inventory Schema

Every route across all pages must be recorded in a global route inventory:

```json
{
  "route_id": "ROUTE-001",
  "path": "",
  "page_ref": "",
  "page_name": "",
  "screen_type": "",
  "is_launch_critical": false,
  "role_access": [],
  "owning_journey_ids": [],
  "related_routes": [],
  "source_trace": []
}
```

# Navigation Inventory Schema

Every navigation item across the app must be recorded:

```json
{
  "nav_item_id": "",
  "label": "",
  "route_target": "",
  "icon": "",
  "order": 0,
  "group": "",
  "permission_required": "",
  "children": [],
  "owning_page_refs": []
}
```

# Page Interaction Contract

Create one compact contract for every page recorded in `page_inventory` or `ui_blueprints`:

```json
{
  "page_ref": "",
  "ui_blueprint_id": "UI-BLUEPRINT-001",
  "route_id": "ROUTE-001",
  "criticality": "launch_critical | standard | supporting | deferred",
  "interactive_element_count": 0,
  "interactive_element_refs": [],
  "unresolved_element_refs": [],
  "assumptions": [],
  "approval_status": "approved | assumed_low_risk | needs_user_review | blocked",
  "mermaid_map_required": false
}
```

Apply deeper design-system, mobile, accessibility, state, and user-confirmation detail to launch-critical pages. Apply confirmation, success, failure, loading, permission-denied, undo, and recovery detail to destructive, security-sensitive, payment, admin, permission-sensitive, and mutation actions.

---

# Interactive Guidance Responsibilities

Ask the user to confirm or choose:

* screen type
* layout type
* page archetype when ambiguous
* layout pattern when competing patterns materially change usability or implementation scope
* sections
* components
* component family decisions
* user actions
* required states
* shared components
* route and navigation expectations
* visual style
* density
* color direction
* typography feel
* component style
* primary visual focus
* visual do and don't rules
* visual acceptance criteria
* user approval status

Infer the full interactive element inventory before asking. Present the proposal and ask the user to approve, remove, rename, reroute, or add elements only when the decision is material. Do not ask the broad question "what interactive elements should be on this page?".

Ask no more than 1-3 page-definition questions at once.

Infer common UI patterns when strongly implied by screen type and workflow, but record assumptions in:

```text
interactive_guidance.assumptions_made
```

Pause for user input when:

* a launch-critical page lacks purpose
* a screen type cannot be inferred
* layout choice materially affects navigation, usability, accessibility, or implementation
* multiple layout patterns are plausible and would materially change the workflow
* required components or actions are ambiguous
* required states are missing for a launch-critical interaction
* visual style, density, or primary visual focus is missing for a launch-critical page
* the user has not approved the visual spec for a launch-critical page

---

# Inputs

```json
{
  "user_journeys": {},
  "interaction_architecture": {},
  "screen_system": {},
  "feature_behaviors": {},
  "state_transition_map": {},
  "accessibility_framework": {},
  "design_system_foundation": {},
  "visual_reference_selection": {},
  "ui_architecture_template_selection": {},
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
Build-Plans/Stage-4/07-ui-blueprint-specification.json
```

The output must include:

```json
{
  "stage": "Stage 4",
  "status": "",
  "ui_blueprints": [],
  "ui_architecture_template_selection": {},
  "page_inventory": [],
  "interaction_contracts": [],
  "interactive_element_inventory": [],
  "page_type_selection_rationale": [],
  "component_inventory": [],
  "visual_spec_inventory": [],
  "visual_reference_selection": {},
  "shared_components": [],
  "navigation_inventory": [],
  "route_inventory": [],
  "state_inventory": [],
  "action_inventory": [],
  "frontend_build_package": {
    "page_count": 0,
    "component_count": 0,
    "shared_component_count": 0,
    "frontend_tasks": [],
    "recommended_skills": [
      "frontend-design",
      "frontend-builder"
    ],
    "task_generator_notes": [],
    "agent_builder_notes": []
  },
  "visual_approval_status": {},
  "ui_blueprint_markdown_path": "",
  "ui_components_markdown_path": "Build-Plans/Stage-4/UI-COMPONENTS.md",
  "complete_app_blueprint_markdown_path": "Build-Plans/Stage-4/09-complete-app-blueprint.md",
  "stage_5_handoff": {}
}
```

Each `ui_blueprints[]` entry must include the page-definition matrix, interactive element hierarchy, and visual spec:

```json
{
  "ui_blueprint_id": "",
  "page_ref": "",
  "page_name": "",
  "purpose": "",
  "primary_user_role": "",
  "screen_type": "",
  "layout_type": "",
  "ui_architecture": {
    "primary_template": "",
    "selected_extensions": [],
    "page_archetype": "",
    "navigation_pattern": "",
    "layout_pattern_decision": {
      "selected_pattern": "",
      "rejected_patterns": [],
      "decision_factors": {
        "information_density": "",
        "comparison_need": "",
        "scan_behavior": "",
        "primary_user_task": "",
        "record_count": "",
        "bulk_actions_required": false,
        "mobile_behavior_required": true
      },
      "reasons": [],
      "source_refs": [],
      "responsive_transformation": {
        "desktop": "",
        "tablet": "",
        "mobile": ""
      }
    },
    "component_family_decisions": [],
    "template_deviations": []
  },
  "route": "",
  "route_id": "ROUTE-001",
  "criticality": "launch_critical | standard | supporting | deferred",
  "interaction_approval_status": "approved | assumed_low_risk | needs_user_review | blocked",
  "design_system_refs": [],
  "visual_reference_refs": [],
  "design_system_alignment": {
    "aligned": false,
    "alignment_notes": [],
    "intentional_deviations": []
  },
  "sections": [
    {
      "section_id": "",
      "name": "",
      "components": [
        {
          "component_id": "",
          "component_type": "",
          "interactive_elements": [
            {
              "element_id": "",
              "element_type": "button | link | icon_button | ...",
              "label": "",
              "route_target": "",
              "route_id": "",
              "route_type": "internal_page | external_url | modal | drawer | anchored_section | file_download | api_action | state_transition | no_navigation",
              "action_id": "",
              "behavior": "navigate | submit | open_modal | open_drawer | toggle | trigger_action | open_link | download | call_api | scroll_to | no_navigation",
              "behavior_target": "",
              "states": {},
              "permission_required": "",
              "permission_denied_behavior": "",
              "confirmation_required": false,
              "design_system_component": "",
              "responsive_behavior": {},
              "accessibility_behavior": {},
              "source_trace": []
            }
          ],
          "data_source": "",
          "validation": ""
        }
      ]
    }
  ],
  "navigation": [
    {
      "nav_item_id": "",
      "label": "",
      "route_target": "",
      "icon": "",
      "permission_required": "",
      "children": []
    }
  ],
  "global_actions": [
    {
      "element_id": "",
      "element_type": "button | link | ...",
      "label": "",
      "route_target": "",
      "action_id": "",
      "behavior": "navigate | submit | ...",
      "behavior_target": ""
    }
  ],
  "states": {
    "loading": {},
    "empty": {},
    "error": {},
    "success": {},
    "populated": {}
  },
  "data_requirements": [],
  "validation_requirements": [],
  "accessibility_requirements": [],
  "responsive_requirements": [],
  "frontend_task_hints": [],
  "recommended_skills": ["frontend-design", "frontend-builder"],
  "visual_spec": {
    "visual_style": "",
    "design_system_refs": [],
    "visual_reference_refs": [],
    "density": "",
    "color_direction": "",
    "typography_feel": "",
    "component_style": "",
    "primary_visual_focus": "",
    "responsive_behavior": "",
    "visual_do_rules": [],
    "visual_dont_rules": [],
    "reference_apps": [],
    "design_system_alignment": {
      "aligned": false,
      "alignment_notes": [],
      "intentional_deviations": []
    },
    "visual_acceptance_criteria": [],
    "user_approval_status": "unconfirmed"
  },
  "source_trace": []
}
```

Also produce the required complete app blueprint tree under:

```text
Build-Plans/Stage-4/09-complete-app-blueprint.md
```

When useful, also produce a readable `UI_BLUEPRINT.md` reference under:

```text
Build-Plans/Stage-4/UI_BLUEPRINT.md
```

When useful for human review, template-selection audit, and Stage 5 handoff, also derive:

```text
Build-Plans/Stage-4/UI-COMPONENTS.md
```

`UI-COMPONENTS.md` must be generated from Stage 4 structured outputs. It is not the canonical source of truth.

---

# Shared State Updates

Update:

```text
ui_blueprints
ui_architecture_template_selection
page_inventory
interaction_contracts
interactive_element_inventory
route_inventory
action_inventory
navigation_inventory
visual_spec_inventory
visual_reference_selection
frontend_build_package
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

* every launch-critical page has a UI blueprint
* every page in `page_inventory` or `ui_blueprints` has one page interaction contract
* every launch-critical page appears in `Build-Plans/Stage-4/09-complete-app-blueprint.md`
* every selected page type has an inclusion rationale tied to upstream product, workflow, role, feature, journey, or route evidence
* every launch-critical page records the selected primary UI architecture template and any selected extensions that influence it
* every launch-critical page has a `page_archetype`
* every launch-critical page has a `layout_pattern_decision.selected_pattern`
* every selected layout pattern records decision factors, reasons, source references, rejected plausible patterns, and desktop/tablet/mobile transformation
* every component family decision maps to a page section, purpose, and related component refs
* template deviations record subject, template default, project choice, reason, and source refs
* comparison-heavy pages do not use `card-grid` unless explicitly justified
* `data-table` pages define sorting, filtering, loading, empty, no-results, error, mobile transformation, and bulk-selection behavior where applicable
* bulk-action pages define selection behavior and action outcomes
* mobile-first pages do not use desktop-only navigation or layout behavior without a recorded responsive transformation
* every UI blueprint has purpose, primary user, screen type, layout type, sections, components, actions, data needs, states, validation, and navigation
* every launch-critical UI blueprint has a visual spec with style, density, color direction, typography feel, component style, primary visual focus, responsive behavior, visual do and don't rules, visual acceptance criteria, and user approval status
* every launch-critical UI blueprint references the selected design system or explicitly records why no design system applies
* every launch-critical UI blueprint references selected visual style references or explicitly records why no visual reference applies
* every launch-critical UI blueprint records design system alignment and any intentional deviations
* every UI blueprint maps page -> section -> component -> interactive element -> route, action, or `no_navigation` -> outcome -> data source -> validation -> states
* every interactive element uses a stable `UI-ELEMENT-` ID and has an element_type, label or accessible name, owner, behavior, source trace, and route, action, or `no_navigation` classification
* every interactive element with navigate behavior has a route_target that exists in route_inventory
* every action in action_inventory maps back to its owning page and component
* every action uses a stable `ACTION-` ID and records triggering elements and outcome fields when applicable
* every route in route_inventory maps to a blueprint page_ref
* every internal route uses a stable `ROUTE-` ID
* every navigation item has a route_target pointing to a valid route in route_inventory
* every created page enumerates every clickable or interactive element in every component and section
* launch-critical elements map to design-system components and define responsive and accessibility behavior, or record an approved exception
* destructive, security-sensitive, payment, admin, permission-sensitive, and mutation actions define confirmation and result or recovery behavior
* labels without behaviors, navigation without targets, missing inventory targets, conflicting duplicate labels, unconfirmed destructive actions, missing permission-denied states, and nested click-target conflicts fail validation
* every frontend build package can reference visual specs for frontend tickets
* component inventory, shared components, routes, states, actions, and interactive elements are defined
* complete app blueprint markdown maps every launch-critical page to a `ui_blueprint_id`
* complete app blueprint markdown includes page sections, components, actions, routes, states, data requirements, and frontend build package summary
* complete app blueprint markdown includes an app route Mermaid map and all required page, workflow, destructive, and recovery Mermaid maps
* Mermaid nodes reconcile with stable page, `UI-ELEMENT-`, `ROUTE-`, and `ACTION-` references
* frontend build package is usable by frontend-design, frontend-builder, task generators, and agent builders
* no frontend code is generated
