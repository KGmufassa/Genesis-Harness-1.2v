# Stage 4 — UX & Interaction Architecture Command & Skill Draft

# Core Philosophy

Stage 4 is centered around:

```text
human interaction architecture cognition
```

NOT:

* product discovery
* market validation
* system architecture
* implementation scheduling
* visual polish as decoration

Those responsibilities belong to other stages.

Stage 4 is responsible for transforming validated product and technical architecture into a coherent human interaction model.

The stage focuses on:

* user journeys
* interaction architecture
* screen systems
* feature behavior
* state transitions
* accessibility foundations
* interface consistency

---

# Stage 4 Core Purpose

Transform:

* Stage 1 product workflows
* Stage 2 validation findings
* Stage 3 architecture outputs
* user profiles
* capabilities and feature structures
* MVP boundaries

into:

* user journey architecture
* interaction architecture
* screen system architecture
* feature behavior specifications
* state transition map
* accessibility framework
* UI architecture template selection
* user-approved Stitch prototype evidence
* implementation-ready UI blueprints
* frontend build package

---

# Recommended Stage 4 Architecture

```text
stage-4-ux-interaction-architecture (command)
│
├── user-journey-design
├── interaction-architecture-design
├── screen-system-design
├── feature-behavior-specification
├── state-transition-and-accessibility-design
├── design-system-foundation
├── ui-architecture-template-selection
├── Stitch MCP prototype and page-confirmation loop
├── ui-blueprint-specification
└── ux-interaction-synthesis
```

The Stitch MCP loop is a command phase, not a replacement for a Stage 4 skill. It supplies visual and interaction evidence that is reconciled into the existing canonical Stage 4 contracts.

---

# Stage 4 Command

# Command — stage-4-ux-interaction-architecture

# Purpose

The `stage-4-ux-interaction-architecture` command orchestrates Stage 4.

It transforms product, validation, and system architecture intelligence into a UX and interaction architecture package that is ready for Stage 5 development orchestration.

Stage 4 must also transform UX requirements into implementation-ready UI blueprints that can be consumed by frontend design skills, frontend builder skills, task generators, and agent builders without generating frontend code.

This is the Stage 4 command skill. It is not a single UX subskill.

---

# Cognitive Boundary

Stage 4 asks:

```text
How should users move through and interact with the validated product?
```

Stage 4 must not:

* redefine the product concept
* perform market validation
* redesign backend system architecture
* write implementation tickets
* produce final UI art direction as decoration
* generate frontend code
* plan engineering sprints

Stage 4 may recommend product or architecture revisions only when interaction design exposes a blocking contradiction.

---

# Output Directory

All final Stage 4 outputs must be recorded in:

```text
Build-Plans/Stage-4/
```

The command must create this folder if it does not exist.

---

# Shared UX State

The command maintains a shared Stage 4 UX state object.

The shared UX state must be written to:

```text
Build-Plans/Build-status/UX-state.json
```

The command must load this file at the beginning of Stage 4, update it after each UX skill runs, and preserve it as the durable interaction architecture state for the build.

```json
{
  "stage": "Stage 4",
  "command": "stage-4-ux-interaction-architecture",
  "status": "not_started",
  "stage_1_inputs": {},
  "stage_2_inputs": {},
  "stage_3_inputs": {},
  "preflight": {},
  "user_journeys": {},
  "interaction_architecture": {},
  "screen_system": {},
  "feature_behaviors": {},
  "state_transition_map": {},
  "accessibility_framework": {},
  "ui_architecture_template_selection": {
    "primary_template": "",
    "confidence": "",
    "alternative_templates": [],
    "selected_extensions": [],
    "reasons": [],
    "unresolved_questions": [],
    "template_deviations": [],
    "template_gaps": [],
    "source_refs": []
  },
  "stitch_prototyping": {
    "availability": "unchecked",
    "visual_source_control": {
      "enabled": true,
      "mode": "stitch_visual_source_of_truth",
      "scope": "visual_only",
      "suggestion_review_required": true,
      "approval_status": "pending",
      "approved_by": "",
      "approved_at": null,
      "locked_screenshot_refs": [],
      "locked_stitch_screen_refs": [],
      "applies_to": [
        "visual_spec_inventory",
        "design_system_foundation",
        "visual_reference_selection",
        "ui_blueprints.visual_spec",
        "complete_app_blueprint_markdown"
      ],
      "excluded_from": [
        "stage_5_handoff",
        "route_inventory",
        "action_inventory",
        "permissions",
        "api_contracts",
        "product_scope"
      ],
      "rationale": ""
    },
    "project_id": "",
    "project_name": "",
    "screen_refs": [],
    "prototype_constraints": {},
    "proposed_pages": [],
    "page_approval_ledger": [],
    "approved_page_refs": [],
    "rejected_page_refs": [],
    "screenshot_evidence": [],
    "suggestion_review_ledger": [],
    "component_extraction": [],
    "divergence_log": [],
    "responsive_review": [],
    "accessibility_review": [],
    "reconciliation_status": "not_started",
    "confidence_gaps": []
  },
  "ui_blueprints": {},
  "page_inventory": [],
  "interaction_contracts": [],
  "interactive_element_inventory": [],
  "route_inventory": [],
  "action_inventory": [],
  "navigation_inventory": [],
  "visual_spec_inventory": [],
  "design_system_foundation": {},
  "visual_reference_selection": {
    "primary_reference": {},
    "secondary_references": [],
    "rejected_references": []
  },
  "frontend_build_package": {},
  "ux_decisions": [],
  "ux_risks": [],
  "interaction_tradeoffs": [],
  "open_questions": [],
  "interactive_guidance": {
    "open_questions": [],
    "answered_questions": [],
    "assumptions_made": [],
    "blocked_decisions": [],
    "user_confirmations": [],
    "ux_confidence_gaps": []
  },
  "stage_5_handoff": {},
  "completion_status": {}
}
```

Each subskill reads the current UX state and writes its updates back into the shared state before the next skill runs.

After each subskill completes, the command must persist the updated shared state to:

```text
Build-Plans/Build-status/UX-state.json
```

---

# Interactive Guidance Rules

The Stage 4 command should behave like a guided interaction design interview.

Use this decision rule:

```text
Ask only for UX decisions that materially affect user journeys, interaction behavior, screen structure, accessibility, or Stage 5 implementation planning.
Infer standard interaction defaults when risk is low and the product workflow supports the inference.
Record assumptions when proceeding without user confirmation.
Block only when a missing decision prevents coherent interaction architecture.
```

When asking the user questions:

* ask 1-3 questions at a time
* prioritize workflow-blocking or accessibility-critical questions first
* avoid asking questions already answered by Stage 1, Stage 2, or Stage 3 outputs
* explain what journey, screen, state, or behavior each question affects
* prefer concrete options over open-ended questions when the tradeoff is known
* update `interactive_guidance.open_questions`
* move answered questions into `interactive_guidance.answered_questions`
* record inferred defaults in `interactive_guidance.assumptions_made`
* record unresolved blockers in `interactive_guidance.blocked_decisions`

The command should continue automatically when a UX decision has a low-risk default.

The command should pause for user input when:

* primary user journey is unclear
* user role differences change screens or permissions
* a workflow has no clear start, success, or failure state
* feature behavior depends on an unresolved product decision
* accessibility requirements materially affect interaction design
* the screen system cannot support a core workflow
* a Stage 3 architecture constraint changes user interaction

The command should not ask the user to choose implementation details that belong to Stage 5 unless the decision changes Stage 4 interaction architecture.

When Stitch MCP is available, Stage 4 must use page-level confirmation first. Confirm the page set and each page's major layout and feature regions before treating its component inventory as final.

Stitch is an internal Stage 4 prototyping and review aid. Approved prototypes refine Stage 4 outputs, but the structured Stage 4 page, component, route, action, state, accessibility, and design-system contracts remain canonical.

Keep Stitch-specific metadata in `stitch_prototyping`, the Stage 4 decision brief, or other Stage-4-local evidence. Do not add Stitch-specific required fields to `stage_5_handoff`.

---

# Stage 4 Input Contract

Load Stage 1 outputs from:

```text
Build-Plans/Stage-1/
```

Load Stage 2 outputs from:

```text
Build-Plans/Stage-2/
```

Load Stage 3 outputs from:

```text
Build-Plans/Stage-3/
```

Required Stage 1 files:

```text
02-user-system-map.json
03-workflow-architecture.json
04-product-capabilities.json
05-feature-structure.json
06-product-boundaries.json
08-mvp-operational-model.json
10-success-framework.json
```

Required Stage 2 files:

```text
01-market-analysis.json
05-risk-validation.json
06-strategic-positioning.json
```

Required Stage 3 files:

```text
01-system-topology.json
02-service-architecture.json
03-data-architecture.json
04-api-architecture.json
06-security-foundations.json
08-scalability-framework.json
```

Minimum viable input set:

```text
Stage 1:
02-user-system-map.json
03-workflow-architecture.json
05-feature-structure.json
08-mvp-operational-model.json

Stage 3:
01-system-topology.json
03-data-architecture.json
04-api-architecture.json
06-security-foundations.json
```

If the minimum viable input set is missing, stop and set:

```text
completion_status.status = "blocked"
completion_status.reason = "missing_ux_inputs"
```

If Stage 3 completion status is not `ready_for_stage_4`, continue only if unresolved issues are not interaction-blocking. Record all carry-forward risks in `ux_risks`.

---

# Preflight Validation

Before UX architecture design, validate:

* Stage 1 user and workflow outputs exist and are readable
* Stage 3 architecture outputs exist and are readable
* primary users are defined
* MVP workflows are defined
* feature structure is clear enough for behavior design
* security and permission constraints are available
* API and data constraints are available
* architecture risks do not block UX architecture

Record preflight results in:

```text
preflight
ux_risks
open_questions
interactive_guidance
completion_status
```

---

# Stage 5 Handoff Contract

Stage 4 must produce a concrete Stage 5 handoff for development orchestration.

The `stage_5_handoff` object must include:

```json
{
  "stage_4_output_directory": "Build-Plans/Stage-4/",
  "launch_critical_journey_ids": [],
  "screen_ids": [],
  "feature_behavior_ids": [],
  "state_transition_ids": [],
  "accessibility_requirement_ids": [],
  "ui_architecture_template_selection": {},
  "ui_architecture_template_refs": [],
  "selected_ui_architecture_extensions": [],
  "template_deviations": [],
  "ui_blueprint_ids": [],
  "visual_spec_ids": [],
  "visual_reference_refs": [],
  "design_system_ref": "Build-Plans/Stage-4/08-design-system-foundation.json",
  "component_candidates": [],
  "component_inventory": [],
  "component_family_decisions": [],
  "shared_component_candidates": [],
  "route_inventory": [],
  "action_inventory": [],
  "visual_acceptance_criteria": [],
  "frontend_implementation_units": [],
  "frontend_build_package": {},
  "validation_requirements": [],
  "responsive_requirements": [],
  "layout_pattern_decisions": [],
  "role_permission_interaction_constraints": [],
  "ux_risks": [],
  "known_interaction_blockers": [],
  "completion_status": {}
}
```

Stage 5 should be able to generate build tickets from this handoff without reinterpreting Stage 4 UX intent.

Stitch does not add a downstream dependency. Do not require Stage 5 to connect to Stitch or consume Stitch project IDs, screen IDs, prompts, approval-ledger records, or divergence logs. Do not add, remove, rename, or repurpose any `stage_5_handoff` fields because Stitch was used. Reconcile all approved prototype evidence into the existing canonical handoff fields above.

---

# UX Contract Formats

Every journey entry must include:

```json
{
  "journey_id": "",
  "name": "",
  "user_role_ids": [],
  "goal": "",
  "entry_points": [],
  "steps": [],
  "success_state": "",
  "failure_states": [],
  "recovery_paths": [],
  "mvp_critical": false,
  "related_workflow_ids": [],
  "related_feature_ids": []
}
```

Every screen entry must include:

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
      "behavior": "navigate | submit | open_modal | open_drawer | toggle | trigger_action | open_link | download | call_api | scroll_to",
      "behavior_target": "",
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

Every feature behavior entry must include:

```json
{
  "behavior_id": "",
  "feature_id": "",
  "trigger": "",
  "user_action": "",
  "system_response": "",
  "validation_rules": [],
  "permission_rules": [],
  "error_behaviors": [],
  "acceptance_criteria": [],
  "related_screen_ids": [],
  "related_api_ids": []
}
```

Every state transition entry must include:

```json
{
  "transition_id": "",
  "scope": "workflow",
  "source_state": "",
  "target_state": "",
  "trigger": "",
  "loading_behavior": "",
  "success_behavior": "",
  "failure_behavior": "",
  "recovery_behavior": "",
  "affected_screen_ids": [],
  "affected_behavior_ids": []
}
```

Every accessibility requirement must include:

```json
{
  "accessibility_id": "",
  "scope": "",
  "requirement": "",
  "affected_screen_ids": [],
  "affected_interaction_ids": [],
  "keyboard_requirement": "",
  "screen_reader_requirement": "",
  "focus_management": "",
  "error_messaging_requirement": "",
  "validation_method": ""
}
```

## UI Blueprint Contract

The UI blueprint layer must convert screens and interaction requirements into implementation-ready UI specifications without producing frontend code.

Each page or screen must be defined through a visual page-definition matrix:

```text
PAGE:
Purpose:
Primary User:
Screen Type:
Page Archetype:
Layout Type:
Layout Pattern Decision:
Sections:
Components:
Component Family Decisions:
Actions:
Data Needed:
States:
Validation:
Navigation:
```

The skill must avoid vague prompts such as:

```text
What should this dashboard look like?
```

Instead, it must force controlled choices.

Screen type options:

```text
1. Dashboard
2. List
3. Detail View
4. Form
5. Wizard
6. Settings
7. Profile
8. Analytics
9. Messaging
10. Landing Page
11. Hero Page
12. Marketing Page
13. Onboarding
14. Pricing
15. Authentication
16. Admin
17. Checkout
18. Custom
```

Screen/page type selection must be contextual.

These options are a controlled vocabulary, not a required checklist. Stage 4 must only include page or screen types that are justified by:

* Stage 1 product category and MVP scope
* Stage 1 workflows and feature structure
* Stage 3 selected stack and architecture constraints
* Stage 4 user journeys and launch-critical interactions
* user roles, permissions, and navigation needs

Do not add `Landing Page`, `Hero Page`, `Dashboard`, `Admin`, `Checkout`, `Authentication`, `Pricing`, or any other page type unless the product model requires it.

Each selected page type must record a rationale:

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
1. Sidebar
2. Top Navigation
3. Split View
4. Card Grid
5. Table
6. Mobile First
7. Full Screen
8. Custom
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

Stage 4 must select a layout pattern for every launch-critical page and record why that pattern fits the page's workflow, information density, comparison needs, scan behavior, primary user task, record count, bulk-action needs, and responsive behavior.

Use `data-table` for dense comparable records, sorting, filtering, pagination, and bulk actions.

Use `card-grid` for visual browsing, media-rich items, summaries, and non-uniform item content.

Use `content-list` for chronological scanning, activity, messages, or simple repeated records.

Use `master-detail` when users browse records while repeatedly inspecting or editing one selected item.

Use `dashboard-grid` for metric, chart, alert, and operational summary surfaces.

Use `form-layout` for create, edit, setup, review, or submission workflows.

Use `settings-layout` for grouped preferences, integrations, permissions, billing, or account configuration.

Use `split-pane` when two related work surfaces must remain visible together.

Component selection options:

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

Action mapping options:

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

Each blueprint must preserve this exact visual hierarchy:

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

This hierarchy is mandatory, not illustrative.

* `09-complete-app-blueprint.md` must render every approved page using this exact nesting order.
* `UI-COMPONENTS.md` must expand the same hierarchy without changing the ownership chain.
* Do not skip levels, flatten `Section` into `Page`, flatten `Interactive Element` into `Component`, or collapse route/action resolution into freeform notes.

Blueprint structure:

```json
{
  "ui_blueprint_id": "UI-BLUEPRINT-001",
  "page_or_screen_id": "",
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
              "element_type": "button | link | icon_button | menu_item | tab | toggle | checkbox | radio | select",
              "label": "",
              "route_target": "",
              "action_id": "",
              "behavior": "navigate | submit | open_modal | open_drawer | toggle | trigger_action | open_link | download | call_api | scroll_to",
              "behavior_target": "",
              "states": {},
              "permission_required": "",
              "confirmation_required": false
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
      "element_type": "button | link | icon_button | menu_item | tab",
      "label": "",
      "route_target": "",
      "action_id": "",
      "behavior": "navigate | submit | open_modal | open_drawer | toggle | trigger_action",
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
  "recommended_skills": [
    "frontend-design",
    "frontend-builder"
  ],
  "visual_spec": {
    "visual_style": "",
    "density": "",
    "color_direction": "",
    "typography_feel": "",
    "component_style": "",
    "primary_visual_focus": "",
    "responsive_behavior": "",
    "visual_do_rules": [],
    "visual_dont_rules": [],
    "reference_apps": [],
    "visual_acceptance_criteria": [],
    "user_approval_status": "unconfirmed"
  },
  "source_trace": []
}
```

The UI blueprint package must produce a readable complete app blueprint tree:

```text
Build-Plans/Stage-4/09-complete-app-blueprint.md
```

The complete app blueprint must use a markdown tree format that exposes all launch-critical pages and their implementation-relevant structure. The example page names below are illustrative only; the generated tree must include the pages required by the actual product and must preserve the exact `Page -> Section -> Component -> Interactive Element -> Route, Action, Or No Navigation` hierarchy:

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

Every page in `09-complete-app-blueprint.md` must map to a `ui_blueprint_id`. Every launch-critical page must show its sections, components, primary actions, route, states, and data requirements.

Every approved page in `09-complete-app-blueprint.md` must:

* render `Page`, `Section`, `Component`, and `Interactive Element` as separate levels
* show each interactive element's reconciled `ROUTE-` reference, `ACTION-` reference, or explicit `no_navigation`
* keep interactive elements nested under their owning component, and components nested under their owning section
* avoid freeform summaries that replace the required tree

Do not include every screen type from the controlled vocabulary in the markdown tree. Include only selected pages with recorded rationale.

The UI blueprint package may also produce a readable `UI_BLUEPRINT.md` view when useful, with sections for:

```text
/pages
/components
/shared-components
/navigation
/routes
/states
/actions
/forms
/data-requirements
/frontend-build-package
```

The UI blueprint package may also derive a readable companion file:

```text
Build-Plans/Stage-4/UI-COMPONENTS.md
```

`UI-COMPONENTS.md` is generated from Stage 4 structured outputs. It is not the canonical source of truth.

`UI-COMPONENTS.md` must remain reconcilable with `09-complete-app-blueprint.md`. Each rendered component entry must identify its owning page and section, keep its interactive elements nested under that component, and show each element's reconciled route, action, or explicit `no_navigation`.

---

# Interactive Element Schema

Every interactive element on a page (button, link, icon button, menu item, tab, input, etc.) must be enumerated with:

```json
{
  "element_id": "",
  "element_type": "button | link | icon_button | menu_item | tab | toggle | checkbox | radio | select | text_input | search_input | file_upload | date_picker",
  "label": "",
  "icon": "",
  "route_target": "",
  "action_id": "",
  "behavior": "navigate | submit | open_modal | open_drawer | toggle | trigger_action | open_link | download | call_api | scroll_to",
  "behavior_target": "",
  "states": {
    "default": {},
    "loading": {},
    "disabled": {},
    "active": {},
    "hover": {}
  },
  "permission_required": "",
  "confirmation_required": false,
  "analytics_event": "",
  "source_trace": []
}
```

# Action Inventory Schema

Every action across all pages must be recorded in a global action inventory:

```json
{
  "action_id": "",
  "name": "",
  "element_type": "button | link | icon_button | menu_item | tab | toggle | checkbox | radio | select",
  "label": "",
  "route_target": "",
  "behavior": "navigate | submit | open_modal | open_drawer | toggle | trigger_action | open_link | download | call_api | scroll_to",
  "behavior_target": "",
  "owning_page_refs": [],
  "owning_component_refs": [],
  "permission_required": "",
  "confirmation_required": false,
  "states": {},
  "analytics_event": "",
  "source_trace": []
}
```

# Route Inventory Schema

Every route across all pages must be recorded in a global route inventory:

```json
{
  "route_id": "",
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

# Page Interaction Contract Addendum

Apply this contract to every page recorded in `page_inventory` or `ui_blueprints`, not only launch-critical pages:

```json
{
  "page_ref": "",
  "ui_blueprint_id": "UI-BLUEPRINT-001",
  "route_id": "ROUTE-001",
  "criticality": "launch_critical | standard | supporting | deferred",
  "interactive_element_refs": [],
  "unresolved_element_refs": [],
  "approval_status": "approved | assumed_low_risk | needs_user_review | blocked",
  "mermaid_map_required": false
}
```

Use stable `UI-ELEMENT-`, `ROUTE-`, and `ACTION-` IDs. Every element must resolve to a route, action, or explicit `no_navigation`. Record route type, ownership, source trace, design-system component, responsive behavior, accessibility behavior, permissions, and confirmation. For mutations and other high-risk actions, record success, failure, loading, permission-denied, undo, and recovery behavior.

Infer the element inventory before asking the user. Request approval only for material workflow, permission, destructive, navigation, accessibility, or implementation decisions.

`09-complete-app-blueprint.md` must include an app-level Mermaid route map and detailed Mermaid maps for branching, destructive, mutation, modal, drawer, or complex routing flows. Trivial pages may rely on reconciled inventories.

Rendered markdown artifacts must remain projections of canonical structured outputs:

* `09-complete-app-blueprint.md` must project `page_inventory`, `ui_blueprints.sections[].components[]`, and `interactive_element_inventory`
* `UI-COMPONENTS.md` must project the same ownership chain and route/action/no-navigation resolution
* if rendered markdown conflicts with canonical structured outputs, fix the markdown and preserve the canonical structured outputs as the source of truth

---

# UI Architecture Template Selection Contract

The UI architecture template-selection layer must choose structural UI architecture references before UI blueprints are finalized.

The selected template and extensions inform page archetype, navigation, layout pattern, component family, responsive behavior, state, and accessibility decisions. They do not replace Stage 1 product scope, Stage 3 architecture, Stage 4 journeys, or stable UI blueprint route/action/element contracts.

Reference library:

```text
.opencode/Skills/ui-blueprint-specification/references/ui-component-system/
```

Primary template options:

```text
marketing-website
saas-dashboard
ecommerce-storefront
mobile-utility
```

Extension options:

```text
analytics
role-based-access
onboarding
billing
collaboration
messaging
file-management
```

Template selection output:

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

Normal Stage 4 runs must treat the template library as read-only. If a repeated missing pattern or poor recommendation is discovered, Stage 4 records a template gap instead of modifying the library.

Apply precedence:

```text
1. project-specific requirements
2. explicit project overrides
3. selected extensions
4. primary template
5. base template
```

---

# Stitch MCP Prototype And Reconciliation Contract

The Stitch MCP phase converts the current Stage 4 interaction architecture into reviewable prototype pages before final UI blueprints are produced.

Stitch prototypes are evidence and discovery artifacts. They do not replace canonical Stage 4 IDs, inventories, approval records, upstream scope, or Stage 3 architecture constraints.

Apply this workflow:

```text
Stage 4 UX foundations and design constraints
-> constrained Stitch prototype prompt
-> generated launch-critical page candidates
-> screenshot evidence capture
-> visual-source and suggestion review
-> page-level user confirmation
-> approved-page component extraction
-> route/action/no_navigation reconciliation
-> responsive and accessibility review
-> canonical UI blueprint specification
```

## Connection And Project Rules

- Check that the Stitch MCP tools are available before beginning the prototype phase.
- List accessible projects before creating a project.
- Reuse the project recorded in `stitch_prototyping.project_id` when it exists and matches the current product.
- Create one Stage 4 project only when no matching configured project exists.
- Record every generated or edited Stitch screen in `stitch_prototyping.screen_refs`.
- Never delete a Stitch project or screen without explicit user approval.
- If Stitch is unavailable, record the failure and confidence gap. Continue without Stitch only after the user explicitly accepts the fallback; otherwise set Stage 4 to `blocked`.

## Screenshot Evidence

Store Stitch screenshot evidence locally in:

```text
Build-Plans/Stage-4/Screen-shots/
```

Screenshot evidence is Stage-4-local review evidence. It must not be added to `stage_5_handoff`, Stage 5 required inputs, or downstream readiness requirements.

Capture:

- one desktop screenshot for every proposed Stitch page used for page approval
- one mobile screenshot for every launch-critical approved Stitch page
- extra screenshots for modal, drawer, branching, destructive, mutation, or complex interaction states

When a required screenshot cannot be captured, record an approved evidence exception with the reason and the replacement evidence used for review.

Record each screenshot in `stitch_prototyping.screenshot_evidence`:

```json
{
  "screenshot_ref": "",
  "prototype_page_ref": "",
  "stitch_screen_ref": "",
  "canonical_page_ref": "",
  "screenshot_path": "Build-Plans/Stage-4/Screen-shots/",
  "viewport": "desktop | tablet | mobile | state_detail",
  "captured_state": "default | loading | empty | error | success | modal | drawer | branching | destructive | mutation | custom",
  "captured_at": null,
  "approval_status": "proposed | approved | exception",
  "evidence_exception_reason": "",
  "source_refs": []
}
```

## Visual Source Control

By default, `stitch_prototyping.visual_source_control.enabled` is `true`.

When enabled, approved Stitch screens and locked screenshot evidence are the Stage 4 visual source of truth for:

- `visual_spec_inventory`
- `design_system_foundation`
- `visual_reference_selection`
- `ui_blueprints.visual_spec`
- page-level visual hierarchy
- component visual treatment
- responsive visual treatment
- `09-complete-app-blueprint.md` visual representation

Stitch visual source of truth is visual-only. It must not control product scope, routes, actions, permissions, data/API contracts, accessibility requirements, or Stage 5 handoff fields.

The user may turn visual source control off by setting:

```text
stitch_prototyping.visual_source_control.enabled = false
```

When disabled, Stitch returns to supporting evidence only, and canonical Stage 4 visual decisions come from the regular visual reference selection, visual specs, and design-system foundation workflow.

## Stitch Suggestion Review

Record every Stitch-suggested visual pattern, component, data display, interaction, navigation item, workflow change, or feature extension before including it in canonical Stage 4 outputs.

Use this ledger entry:

```json
{
  "suggestion_id": "",
  "prototype_page_ref": "",
  "stitch_screen_ref": "",
  "screenshot_refs": [],
  "suggestion_type": "visual_pattern | component | data_display | interaction | feature_extension | navigation | workflow_change",
  "suggestion": "",
  "prd_alignment": "direct | adjacent | unsupported | conflicts",
  "canonical_alignment_refs": [],
  "decision": "include | exclude | revise | defer | route_to_prior_stage",
  "decision_reason": "",
  "canonical_refs_created_or_updated": [],
  "approval_status": "pending | approved | rejected",
  "source_refs": []
}
```

Include suggestions only when they map to PRD, workflow, feature, route, action, data, or design-system references, or when the user approves the appropriate Stage 4 or prior-stage revision.

Visual-only suggestions may update `visual_spec_inventory`, `design_system_foundation`, `visual_reference_selection`, and UI blueprint visual specs. Suggestions that introduce a new route, action, workflow, permission, API, entity, launch-critical feature, or MVP scope cannot be auto-included.

## Prototype Constraints Prompt

Build every Stitch prompt from canonical Stage 1 through Stage 4 evidence. The prompt must constrain:

- approved product and MVP scope
- supported user roles and permissions
- candidate page purpose and owning journeys
- approved features and behaviors
- known routes and navigation boundaries
- known actions, mutations, confirmations, and outcomes
- required data concepts without inventing backend entities or APIs
- selected UI architecture template and extensions
- design-system tokens, component rules, and visual references
- loading, empty, no-results, populated, success, error, permission-denied, and recovery states where applicable
- desktop, tablet, and mobile expectations
- keyboard, focus, labeling, contrast, validation, and error-message expectations
- explicit exclusions and deferred page types

Use this prompt structure:

```text
PRODUCT AND MVP BOUNDARY:
USER ROLES AND PERMISSIONS:
JOURNEYS AND PAGE PURPOSES:
APPROVED FEATURES AND BEHAVIORS:
ROUTE AND NAVIGATION CONSTRAINTS:
ACTION AND STATE CONSTRAINTS:
DATA CONCEPTS:
UI ARCHITECTURE AND DESIGN SYSTEM:
RESPONSIVE REQUIREMENTS:
ACCESSIBILITY REQUIREMENTS:
EXCLUSIONS AND DEFERRED SCOPE:
PROTOTYPE REQUEST:
```

Before the prototype request, run a read-only MCP capability preflight and record the discovered server and tool names for project create/reuse, screen generate/update, screen list/read, and screenshot/export operations. Mark availability `available`, `partial`, or `unavailable`; partial capability requires the same explicit fallback decision as unavailability.

The prototype request should ask Stitch to propose launch-critical pages, major feature regions, reusable components, and interaction affordances. It must not ask Stitch to invent product scope, backend services, permissions, or implementation tickets.

## Page-Level Confirmation

Confirm the page set before final component extraction. Present each proposed page with:

- Stitch screen reference
- proposed canonical page name
- purpose
- supported user roles
- owning journey and feature references
- route or location hint
- major layout regions
- major features represented
- responsive summary
- screenshot evidence refs
- known divergences or confidence gaps

Use this approval ledger entry:

```json
{
  "prototype_page_ref": "",
  "stitch_screen_ref": "",
  "proposed_page_name": "",
  "canonical_page_ref": "",
  "status": "proposed | approved | revise | rejected | deferred",
  "major_regions": [],
  "represented_feature_refs": [],
  "screenshot_refs": [],
  "rationale": "",
  "approved_by": "",
  "approved_at": null,
  "source_refs": []
}
```

Do not treat component extraction as final while its owning page is `proposed` or `revise`. Rejected and deferred pages must remain in the ledger so they cannot silently reappear during blueprint synthesis.

## Approved-Page Component Extraction

For every approved page, inventory all visible and behavioral components, including:

- navigation and breadcrumbs
- headers, toolbars, filters, search, and sorting controls
- forms and validation messaging
- tables, lists, cards, charts, metrics, and data visualizations
- tabs, accordions, pagination, and view controls
- buttons, links, icon controls, clickable rows, and clickable cards
- menus, modals, drawers, popovers, and confirmation surfaces
- uploads, downloads, media, and file controls
- loading, empty, no-results, error, success, permission-denied, and recovery surfaces
- notifications, alerts, toasts, and inline feedback
- responsive-only or role-specific variants

Use this extraction shape:

```json
{
  "prototype_page_ref": "",
  "canonical_page_ref": "",
  "section_ref": "",
  "component_ref": "",
  "component_name": "",
  "component_family": "",
  "classification": "static | interactive",
  "interactive_elements": [
    {
      "element_ref": "",
      "route_ref": "",
      "action_ref": "",
      "no_navigation_behavior": ""
    }
  ],
  "route_refs": [],
  "action_refs": [],
  "required_states": [],
  "responsive_behavior": {},
  "accessibility_requirements": [],
  "source_refs": []
}
```

Every interactive component must expose each triggering element separately and aggregate its canonical route and action references in `route_refs` and `action_refs`. Do not use a single component-level action to hide multiple buttons, links, menus, row actions, tabs, or form controls. Static components may use empty route and action arrays.

## Route And Action Reconciliation

After page approval and component extraction, reconcile all interactive elements into canonical Stage 4 contracts.

Every interactive element must map to:

```text
stable UI-ELEMENT- ID
+ owning UI-BLUEPRINT- and component reference
+ ROUTE- ID, ACTION- ID, or explicit no_navigation behavior
+ states, permissions, confirmation, outcome, and recovery behavior where applicable
```

- Use `ROUTE-` for navigation to an internal canonical page or recorded external URL.
- Use `ACTION-` for mutations, commands, submissions, toggles, downloads, uploads, modal or drawer behavior, and other non-navigation outcomes.
- Use `no_navigation` only for intentionally non-navigating controls and record their behavior target.
- Record a proposed route or action as unresolved when it conflicts with upstream scope; do not silently create it from the prototype.
- Reject Stage 4 completion when an approved page has an orphan component, interactive element, route, or action.

## Divergence Rules

When Stitch differs from canonical Stage 1 through Stage 4 evidence, record:

```json
{
  "divergence_id": "",
  "prototype_ref": "",
  "prototype_proposal": "",
  "conflicting_constraint": "",
  "constraint_source_refs": [],
  "resolution": "use_canonical | approved_stage_4_revision | route_to_prior_stage | defer | reject",
  "rationale": "",
  "affected_refs": [],
  "approval_status": ""
}
```

Canonical upstream constraints win by default. A Stitch proposal may change the Stage 4 page, component, route, or action contract only after user approval and traceable reconciliation. Product-scope or backend-architecture changes must use the established prior-stage revision path.

## Responsive And Accessibility Review

Review every approved launch-critical page at desktop, tablet, and mobile sizes. Record content priority, navigation transformation, component reflow, data-density changes, touch targets, overflow, and interaction substitutions.

After component extraction, review keyboard operation, focus order and restoration, accessible names, landmarks, headings, labels, instructions, contrast, status announcements, validation, error messaging, permission-denied behavior, and modal or drawer focus containment.

Record review results in `stitch_prototyping.responsive_review` and `stitch_prototyping.accessibility_review`. Reconcile requirements into canonical blueprint and accessibility contracts; the prototype image alone is not accessibility evidence.

## Downstream Compatibility

The Stitch phase must not change Stage 5 through Stage 8 contracts.

- Keep existing Stage 4 filenames and final output shapes.
- Keep `ui_blueprints`, `page_inventory`, `component_inventory`, `interactive_element_inventory`, `route_inventory`, `action_inventory`, `frontend_build_package`, and `stage_5_handoff` canonical.
- Keep Stitch project IDs, screen IDs, prompt history, approval ledger, and divergence logs Stage-4-local.
- Require Stage 5 to consume the same canonical Stage 4 handoff fields regardless of whether Stitch was used.
- Treat Stitch as strictly a Stage 4 action. Stage 5 must not branch, validate, block, ticket, or alter sequencing based on whether Stitch was used.

---

# Orchestrated Skills

Run Stage 4 skills and the prototype phase in this order:

```text
1. user-journey-design
2. interaction-architecture-design
3. screen-system-design
4. feature-behavior-specification
5. state-transition-and-accessibility-design
6. design-system-foundation
7. ui-architecture-template-selection
8. Stitch MCP prototype and page-confirmation loop
9. ui-blueprint-specification
10. ux-interaction-synthesis
```

---

# Skill — user-journey-design

# Purpose

The `user-journey-design` skill defines the main user journeys and outcome paths.

It determines:

* primary user journeys
* secondary user journeys
* entry points
* success states
* failure states
* role-specific journey differences
* MVP journey boundaries

---

# Core Responsibilities

## Journey Mapping

Define:

* user goals
* journey start states
* user actions
* system responses
* decision points
* success outcomes
* failure outcomes
* recovery paths

## Role and Persona Mapping

Map journeys across:

* primary users
* secondary users
* admins or operators
* guest or unauthenticated users
* permission-based user roles

## Journey Risk Detection

Identify:

* missing user goals
* unclear success states
* excessive friction
* unsupported failure recovery
* role conflicts
* MVP journey gaps

---

# Interactive Guidance Responsibilities

This skill should guide the user only when journeys cannot be inferred safely.

Ask targeted questions when any of these are unclear:

* primary user goal
* first action in the journey
* successful end state
* failure or recovery behavior
* role-specific journey differences
* whether a journey is MVP-critical or deferred

Infer common journey defaults when the workflow and user profile make them obvious, but record the assumption in:

```text
interactive_guidance.assumptions_made
```

Pause for user input when a journey decision changes screens, permissions, feature behavior, or MVP scope.

---

# Inputs

```json
{
  "user_profiles": {},
  "workflows": {},
  "feature_structure": {},
  "mvp_scope": {},
  "existing_state": {}
}
```

---

# Outputs

```json
{
  "user_journeys": {},
  "journey_roles": [],
  "entry_points": [],
  "success_states": [],
  "failure_states": [],
  "journey_risks": [],
  "open_questions": []
}
```

---

# Shared State Updates

```text
user_journeys
ux_decisions
ux_risks
open_questions
interactive_guidance
```

---

# Skill — interaction-architecture-design

# Purpose

The `interaction-architecture-design` skill defines how users interact with product workflows and system responses.

It determines:

* interaction patterns
* navigation model
* decision points
* command flows
* feedback patterns
* error and recovery interactions
* role-based interaction differences

---

# Core Responsibilities

## Interaction Model

Define:

* navigation paths
* action patterns
* confirmation patterns
* feedback and notification behavior
* user input patterns
* system response patterns
* recovery behavior

## Interaction Constraints

Map constraints from:

* system topology
* APIs
* permissions
* data ownership
* asynchronous processing
* security requirements

## Interaction Risk Detection

Identify:

* confusing flows
* missing feedback
* hidden system delays
* unsafe destructive actions
* permission ambiguity
* unsupported recovery paths

---

# Interactive Guidance Responsibilities

This skill should guide the user through interaction decisions that materially affect workflow usability.

Ask targeted questions when any of these are unclear:

* navigation model
* whether a user action needs confirmation
* how async processing should be communicated
* how errors or failed actions should be handled
* whether actions are reversible
* how users move between related workflows
* how permission limits should appear to users

Infer standard interaction defaults when risk is low, but record the assumption in:

```text
interactive_guidance.assumptions_made
```

Pause for user input when an interaction decision changes workflow completion, safety, permissions, or recovery.

---

# Inputs

```json
{
  "user_journeys": {},
  "workflows": {},
  "api_architecture": {},
  "security_foundations": {},
  "existing_state": {}
}
```

---

# Outputs

```json
{
  "interaction_architecture": {},
  "navigation_model": {},
  "interaction_patterns": [],
  "feedback_patterns": [],
  "recovery_patterns": [],
  "interaction_risks": []
}
```

---

# Shared State Updates

```text
interaction_architecture
ux_decisions
ux_risks
interaction_tradeoffs
interactive_guidance
```

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

```text
screen_system
ux_decisions
ux_risks
open_questions
interactive_guidance
```

---

# Skill — feature-behavior-specification

# Purpose

The `feature-behavior-specification` skill defines how product features behave in response to user actions and system conditions.

It determines:

* feature behavior
* user-triggered behavior
* system-triggered behavior
* validation rules
* permission behavior
* error behavior
* empty, loading, success, and failure states

---

# Core Responsibilities

## Behavior Specification

Define:

* feature purpose
* trigger actions
* system responses
* required inputs
* expected outputs
* validation rules
* permission checks
* error and recovery behavior

## Behavior Consistency

Validate:

* feature behavior supports journeys
* behavior aligns with APIs and data model
* behavior respects permissions
* behavior supports MVP scope
* behavior exposes clear feedback

## Behavior Risk Detection

Identify:

* ambiguous feature behavior
* missing validation rules
* unsafe destructive behavior
* unclear permissions
* hidden async states
* missing empty or error states

---

# Interactive Guidance Responsibilities

This skill should guide the user through feature behavior decisions that affect user trust, safety, and implementation clarity.

Ask targeted questions when any of these are unclear:

* what triggers a feature
* what happens after a user action
* what validation rules apply
* what users can edit, delete, submit, approve, or cancel
* how errors should be handled
* whether actions are reversible
* what states the feature must support

Infer standard behavior only when feature purpose and workflow context are clear.

Record assumptions in:

```text
interactive_guidance.assumptions_made
```

Pause for user input when feature behavior affects safety, permissions, validation, or implementation scope.

---

# Inputs

```json
{
  "feature_structure": {},
  "user_journeys": {},
  "interaction_architecture": {},
  "screen_system": {},
  "api_architecture": {},
  "security_foundations": {},
  "existing_state": {}
}
```

---

# Outputs

```json
{
  "feature_behaviors": {},
  "behavior_rules": [],
  "validation_rules": [],
  "permission_behaviors": [],
  "error_behaviors": [],
  "behavior_risks": []
}
```

---

# Shared State Updates

```text
feature_behaviors
ux_decisions
ux_risks
interaction_tradeoffs
interactive_guidance
```

---

# Skill — state-transition-and-accessibility-design

# Purpose

The `state-transition-and-accessibility-design` skill defines user-visible state transitions and accessibility foundations.

It determines:

* workflow states
* screen states
* feature states
* transition triggers
* loading and async states
* accessibility requirements
* inclusive interaction constraints

---

# Core Responsibilities

## State Transition Mapping

Define:

* start states
* intermediate states
* success states
* failure states
* loading states
* empty states
* permission-denied states
* transition triggers

## Accessibility Framework

Define:

* keyboard interaction requirements
* screen reader expectations
* focus management needs
* contrast and readability needs
* form accessibility requirements
* error messaging accessibility
* motion and animation constraints

## State and Accessibility Risk Detection

Identify:

* missing state transitions
* unclear loading behavior
* inaccessible interaction patterns
* missing focus or keyboard behavior
* unclear error messaging
* visual-only feedback risks

---

# Interactive Guidance Responsibilities

This skill should guide the user through state and accessibility decisions that affect task completion and inclusive use.

Ask targeted questions when any of these are unclear:

* what states a workflow can enter
* how users know something is processing
* how users recover from failure
* whether keyboard-only use is required
* whether screen reader support is required
* whether motion, timing, or contrast constraints matter
* how permission-denied or unavailable states should behave

Infer baseline accessibility requirements as required, not optional.

Record assumptions in:

```text
interactive_guidance.assumptions_made
```

Pause for user input when a state or accessibility decision affects core task completion or legal/compliance expectations.

---

# Inputs

```json
{
  "user_journeys": {},
  "interaction_architecture": {},
  "screen_system": {},
  "feature_behaviors": {},
  "security_foundations": {},
  "existing_state": {}
}
```

---

# Outputs

```json
{
  "state_transition_map": {},
  "workflow_states": [],
  "screen_states": [],
  "feature_states": [],
  "accessibility_framework": {},
  "accessibility_risks": []
}
```

---

# Shared State Updates

```text
state_transition_map
accessibility_framework
ux_decisions
ux_risks
interactive_guidance
```

---

# Skill — ui-architecture-template-selection

# Purpose

The `ui-architecture-template-selection` skill selects the structural UI architecture template and extensions that `ui-blueprint-specification` should use when generating page/component blueprints.

It determines:

* primary UI architecture template
* selected extensions
* page archetype defaults
* navigation pattern defaults
* layout pattern defaults
* component-family guidance
* template deviations and override reasons

This skill is the structural template-selection layer for Stage 4. It does not generate frontend code, final visual styling, or implementation tickets.

---

# Core Responsibilities

## Reference Selection

Read:

```text
.opencode/Skills/ui-blueprint-specification/references/ui-component-system/README.md
.opencode/Skills/ui-blueprint-specification/references/ui-component-system/TEMPLATE-SELECTOR.md
.opencode/Skills/ui-blueprint-specification/references/ui-component-system/NORMALIZED-VALUES.md
.opencode/Skills/ui-blueprint-specification/references/ui-component-system/PRECEDENCE-RULES.md
.opencode/Skills/ui-blueprint-specification/references/ui-component-system/TEMPLATE-REGISTRY.md
```

Then load only the selected primary template, selected extensions, and directly relevant patterns.

## Template Selection

Select one primary template:

```text
marketing-website
saas-dashboard
ecommerce-storefront
mobile-utility
```

Select extensions only when upstream evidence justifies them:

```text
analytics
role-based-access
onboarding
billing
collaboration
messaging
file-management
```

## Risk Detection

Identify:

* low-confidence template selection
* incompatible extensions
* project-specific overrides
* missing template patterns
* template defaults that conflict with Stage 1 product scope, Stage 3 architecture, or Stage 4 journey needs

---

# Interactive Guidance Responsibilities

Ask the user only when:

* primary template confidence is low
* two templates would produce materially different page inventory or navigation
* an extension would add launch-critical pages or workflows not clearly supported by upstream inputs
* a project override changes navigation, page archetype, layout pattern, or Stage 5 frontend scope

Otherwise infer from upstream product, workflow, role, platform, and journey evidence. Record assumptions in:

```text
interactive_guidance.assumptions_made
```

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

---

# Outputs

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

---

# Shared State Updates

```text
ui_architecture_template_selection
ux_decisions
ux_risks
open_questions
interactive_guidance
```

---

# Skill — ui-blueprint-specification

# Purpose

The `ui-blueprint-specification` skill transforms UX requirements into implementation-ready UI blueprints without generating frontend code.

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
* states
* forms
* tables
* cards
* modals
* drawers
* empty states
* loading states
* error states
* frontend build package inputs

This skill is the bridge between Stage 4 UX architecture and Stage 5 frontend implementation planning.

It consumes the selected Stage 4 design system and visual references from `design-system-foundation`, the selected structural UI architecture template and extensions from `ui-architecture-template-selection`, and approved Stitch page evidence from `stitch_prototyping`.

It must reconcile approved Stitch pages and extracted components into canonical Stage 4 IDs and inventories. It must not copy an unsupported prototype route, action, permission, data concept, or feature into the final blueprint.

---

# Core Responsibilities

## Page Definition Matrix

Force each page or screen through a structured matrix:

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

The skill must ask controlled UI questions using screen type, layout type, component selection, and action mapping options instead of broad visual preference questions.

Every launch-critical page must record why its selected layout pattern fits the workflow, information density, comparison needs, scan behavior, primary user task, record count, bulk-action needs, and responsive behavior.

## Visual Spec Matrix

Force each launch-critical page or screen through a visual specification matrix:

```text
VISUAL SPEC
Visual Style
Density
Color Direction
Typography Feel
Component Style
Primary Visual Focus
Responsive Behavior
Visual Do Rules
Visual Don't Rules
Reference Apps
Visual Acceptance Criteria
User Approval Status
```

The visual spec matrix captures how the UI should visually feel and what the frontend builder must preserve. It must not generate frontend code or mockups.

## Visual Hierarchy Modeling

Represent each page as:

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

## Frontend Build Package

Generate a frontend build package containing:

* page inventory
* UI architecture template selection
* component inventory
* component family decisions
* shared components
* navigation inventory
* route inventory
* state inventory
* action inventory
* frontend tasks
* recommended frontend skills

---

# Interactive Guidance Responsibilities

Ask the user to confirm or choose:

* unresolved differences between approved Stitch pages and canonical Stage 4 constraints
* screen type
* layout type
* page archetype when ambiguous
* layout pattern when competing patterns materially change usability or implementation scope
* sections
* component selections
* component family decisions
* user actions
* required states
* shared components
* route/navigation expectations
* visual style
* density
* color direction
* typography feel
* component style
* primary visual focus
* visual do and don't rules
* visual acceptance criteria
* user approval status

Ask no more than 1-3 page-definition questions at once.

Infer common UI patterns when they are strongly implied by the screen type and workflow, but record them in:

```text
interactive_guidance.assumptions_made
```

Pause for user input when:

* a launch-critical page lacks purpose
* a screen type cannot be inferred
* a layout choice materially affects navigation, usability, accessibility, or implementation
* multiple layout patterns are plausible and would materially change the workflow
* required components or actions are ambiguous
* required states are missing for a launch-critical interaction
* visual style, density, or primary visual focus is missing for a launch-critical page
* the user has not approved the visual spec for a launch-critical page
* a Stitch page remains `proposed` or `revise` and would materially affect the canonical page inventory
* a prototype component implies an unsupported route, action, permission, data concept, or product feature

Update:

```text
interactive_guidance.open_questions
interactive_guidance.answered_questions
interactive_guidance.assumptions_made
interactive_guidance.blocked_decisions
interactive_guidance.ux_confidence_gaps
```

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
  "stitch_prototyping": {},
  "ui_blueprints": {},
  "frontend_build_package": {},
  "existing_state": {}
}
```

---

# Outputs

```json
{
  "ui_blueprints": [],
  "ui_architecture_template_selection": {},
  "page_inventory": [],
  "component_inventory": [],
  "component_family_decisions": [],
  "visual_spec_inventory": [],
  "visual_reference_selection": {},
  "shared_components": [],
  "navigation_inventory": [],
  "route_inventory": [],
  "state_inventory": [],
  "action_inventory": [],
  "frontend_build_package": {},
  "visual_approval_status": {},
  "ui_components_markdown_path": "Build-Plans/Stage-4/UI-COMPONENTS.md",
  "frontend_task_hints": [],
  "open_questions": []
}
```

---

# Shared State Updates

```text
ui_blueprints
ui_architecture_template_selection
stitch_prototyping
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

---

# Skill — design-system-foundation

# Purpose

The `design-system-foundation` skill defines the shared design system that all Stage 4 UI blueprints must follow.

It produces an implementation-ready visual contract without generating frontend code.

It defines:

* product visual personality
* design style
* color tokens
* typography tokens
* spacing scale
* radius rules
* elevation rules
* icon rules
* component style rules
* responsive breakpoints
* visual references
* liked and disliked patterns
* accessibility constraints
* design approval status

---

# Core Responsibilities

## Design System Matrix

Force the shared app design system through:

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
Liked Patterns
Disliked Patterns
Accessibility Constraints
Design Do Rules
Design Don't Rules
Design Approval Status
```

## UI Blueprint Alignment

Validate that launch-critical UI blueprints and visual specs reference or align with the shared design system.

---

# Interactive Guidance Responsibilities

Ask the user to confirm or choose:

* product visual personality
* design style
* color direction
* typography feel
* density and spacing
* component style direction
* visual references
* liked and disliked patterns
* design approval status

Pause for user input when:

* launch-critical visual specs conflict with each other
* color, typography, spacing, or component style rules are too vague for frontend implementation
* responsive breakpoints or collapse rules are missing
* design approval status is unconfirmed

---

# Outputs

```json
{
  "design_system_foundation": {},
  "ui_blueprint_alignment": [],
  "stage_5_handoff": {},
  "open_questions": []
}
```

# Shared State Updates

```text
design_system_foundation
visual_spec_inventory
stage_5_handoff
ux_confidence_gaps
```

---

# Skill — ux-interaction-synthesis

# Purpose

The `ux-interaction-synthesis` skill combines all Stage 4 UX and interaction intelligence into final outputs.

It produces:

* user journey architecture
* interaction architecture
* screen system
* feature behavior specifications
* state transition map
* accessibility framework
* UI architecture template selection
* UI blueprint specification
* design system foundation
* complete app blueprint markdown tree
* handoff guidance for Stage 5

---

# Core Responsibilities

## UX Coherence

Validate:

* user journeys align with Stage 1 workflows
* interactions support user goals
* screens support journeys and feature behavior
* feature behavior aligns with API and permission constraints
* state transitions are complete
* accessibility requirements are represented
* primary UI architecture template selection exists or a blocking reason is recorded
* selected UI architecture extensions are compatible with the primary template or documented as deviations
* launch-critical page archetypes and layout pattern decisions are justified by upstream evidence and selected UI architecture references
* layout pattern decisions include selected pattern, decision factors, reasons, rejected plausible alternatives, source references, and responsive transformations
* component family decisions map to page sections and component refs
* template deviations and template gaps are recorded when project needs override or exceed the selected template or extensions
* every approved Stitch page reconciles to exactly one canonical page or screen reference
* rejected and deferred Stitch pages remain excluded from canonical launch scope unless a later approval supersedes them
* component extraction is complete for every approved page
* every extracted interactive element resolves to a canonical route, action, or explicit `no_navigation` behavior
* Stitch divergences, responsive reviews, accessibility reviews, and accepted fallback decisions are resolved or recorded as blocking gaps
* no approved prototype page, component, route, action, or interactive element is orphaned

## Tradeoff Documentation

Record:

* major UX decisions
* interaction tradeoffs
* accepted UX risks
* deferred UX concerns
* Stage 5 implementation implications

## Completion Determination

Determine whether Stage 4 is:

```text
ready_for_stage_5
needs_ux_revision
needs_stage_3_revision
blocked
```

---

# Interactive Guidance Responsibilities

This skill should not finalize Stage 4 if interaction-blocking questions remain unresolved.

Before writing final outputs, inspect:

```text
interactive_guidance.open_questions
interactive_guidance.blocked_decisions
interactive_guidance.ux_confidence_gaps
ux_risks
open_questions
interaction_tradeoffs
```

Classify unresolved guidance items as:

```text
safe_to_assume
needs_user_confirmation
blocks_stage_4_completion
```

Ask the minimum number of final questions needed to complete Stage 4.

Do not ask broad aesthetic preference questions at this stage. Only ask questions tied directly to:

* missing final UX output fields
* unresolved journey decisions
* unresolved screen system decisions
* unresolved feature behavior decisions
* unresolved UI architecture template decisions
* unresolved Stitch page approvals or prototype divergences
* unresolved UI blueprint decisions
* unresolved accessibility decisions
* UX risks that block Stage 5 handoff

If proceeding with assumptions, record them in:

```text
interactive_guidance.assumptions_made
```

If Stage 4 cannot complete, set `completion_status` to one of:

```text
needs_ux_revision
needs_stage_3_revision
blocked
```

and return the specific questions or decisions required.

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
  "ui_architecture_template_selection": {},
  "stitch_prototyping": {},
  "ui_blueprints": {},
  "visual_spec_inventory": [],
  "design_system_foundation": {},
  "visual_reference_selection": {},
  "complete_app_blueprint_markdown_path": "",
  "ui_components_markdown_path": "",
  "frontend_build_package": {},
  "existing_state": {}
}
```

---

# Outputs

```json
{
  "ux_outputs": {},
  "ux_decisions": [],
  "ux_risks": [],
  "interaction_tradeoffs": [],
  "ui_blueprints": {},
  "visual_spec_inventory": [],
  "design_system_foundation": {},
  "visual_reference_selection": {},
  "ui_architecture_template_selection": {},
  "complete_app_blueprint_markdown_path": "Build-Plans/Stage-4/09-complete-app-blueprint.md",
  "ui_components_markdown_path": "Build-Plans/Stage-4/UI-COMPONENTS.md",
  "frontend_build_package": {},
  "stage_5_handoff": {},
  "completion_status": {}
}
```

---

# Final Stage 4 Outputs

Write or update:

```text
Build-Plans/Stage-4/01-user-journeys.json
Build-Plans/Stage-4/02-interaction-architecture.json
Build-Plans/Stage-4/03-screen-system.json
Build-Plans/Stage-4/04-feature-behaviors.json
Build-Plans/Stage-4/05-state-transition-map.json
Build-Plans/Stage-4/06-accessibility-framework.json
Build-Plans/Stage-4/07-ui-blueprint-specification.json
Build-Plans/Stage-4/08-design-system-foundation.json
Build-Plans/Stage-4/09-complete-app-blueprint.md
```

When useful, also write or update:

```text
Build-Plans/Stage-4/UI-COMPONENTS.md
```

`UI-COMPONENTS.md` is a generated companion artifact derived from structured Stage 4 outputs. It is not the canonical source of truth.

Each output must include:

* related Stage 1 workflows or features
* related Stage 3 architecture constraints where applicable
* UX decisions
* risks and constraints
* unresolved questions
* Stage 5 handoff notes when relevant

---

# Final Output Schemas

`01-user-journeys.json` must include:

```json
{
  "stage": "Stage 4",
  "status": "",
  "user_journeys": [],
  "journey_roles": [],
  "entry_points": [],
  "success_states": [],
  "failure_states": [],
  "recovery_paths": [],
  "stage_5_handoff_refs": []
}
```

`02-interaction-architecture.json` must include:

```json
{
  "stage": "Stage 4",
  "status": "",
  "navigation_model": {},
  "interaction_patterns": [],
  "feedback_patterns": [],
  "recovery_patterns": [],
  "permission_interactions": [],
  "async_interaction_behaviors": [],
  "interaction_risks": []
}
```

`03-screen-system.json` must include:

```json
{
  "stage": "Stage 4",
  "status": "",
  "screen_inventory": [],
  "screen_groups": [],
  "navigation_structure": {},
  "role_screen_access": [],
  "component_candidates": [],
  "responsive_requirements": [],
  "screen_risks": []
}
```

`04-feature-behaviors.json` must include:

```json
{
  "stage": "Stage 4",
  "status": "",
  "feature_behaviors": [],
  "behavior_rules": [],
  "validation_rules": [],
  "permission_behaviors": [],
  "error_behaviors": [],
  "acceptance_criteria": [],
  "stage_5_ticket_hints": []
}
```

`05-state-transition-map.json` must include:

```json
{
  "stage": "Stage 4",
  "status": "",
  "workflow_states": [],
  "screen_states": [],
  "feature_states": [],
  "state_transitions": [],
  "loading_states": [],
  "empty_states": [],
  "permission_denied_states": [],
  "recovery_behaviors": []
}
```

`06-accessibility-framework.json` must include:

```json
{
  "stage": "Stage 4",
  "status": "",
  "accessibility_requirements": [],
  "keyboard_requirements": [],
  "screen_reader_requirements": [],
  "focus_management_requirements": [],
  "contrast_and_readability_requirements": [],
  "form_accessibility_requirements": [],
  "accessibility_validation_requirements": [],
  "accessibility_risks": [],
  "stage_5_handoff": {}
}
```

`07-ui-blueprint-specification.json` must include:

```json
{
  "stage": "Stage 4",
  "status": "",
  "ui_blueprints": [],
  "ui_architecture_template_selection": {},
  "page_inventory": [],
  "page_type_selection_rationale": [],
  "component_inventory": [],
  "visual_spec_inventory": [],
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

The rendered markdown artifacts referenced by `complete_app_blueprint_markdown_path` and `ui_components_markdown_path` must preserve the canonical Stage 4 hierarchy:

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

Do not treat these markdown artifacts as optional formatting views. They must remain structurally reconcilable with the canonical JSON outputs.

Each `ui_blueprints[]` entry must include:

```json
{
  "ui_blueprint_id": "",
  "page_ref": "",
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
  "design_system_refs": [],
  "visual_reference_refs": [],
  "design_system_alignment": {
    "aligned": false,
    "alignment_notes": [],
    "intentional_deviations": []
  },
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
  }
}
```

`08-design-system-foundation.json` must include:

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
      "cards": {},
      "forms": {},
      "tables": {},
      "modals": {},
      "drawers": {},
      "navigation": {}
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
      "primary_reference": {},
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

---

# Stage Decision Brief

Before Stage 4 may run final synthesis or use `ready_for_stage_5`, it must generate:

```text
Build-Plans/Stage-4/00-stage-decision-brief.md
```

Purpose:

```text
Use the recommended approach to propose UX/UI direction before build tickets are generated.
```

The brief must include:

* recommended UX approach
* recommended navigation model
* recommended page and screen inventory
* recommended layout direction
* recommended component approach
* recommended visual style
* recommended design system direction
* mobile and desktop priority
* Stitch visual source-of-truth mode status
* locked Stitch screen and screenshot references used as visual source evidence
* included Stitch suggestions
* excluded Stitch suggestions
* deferred or prior-stage-routed Stitch suggestions
* approved visual deviations from Stitch
* confirmation that Stage 5 handoff impact is `none`
* alternatives considered
* what the user should approve or revise

Approval question:

```text
Do you approve this recommended UX/UI direction?
```

Approval options:

```text
Approve recommended UI direction
Revise visual style
Revise page/screen structure
Revise navigation/layout
Revise component priorities
```

Stage 4 shared state must include:

```json
{
  "stage_decision_brief": {
    "brief_id": "",
    "stage": "Stage 4",
    "brief_path": "Build-Plans/Stage-4/00-stage-decision-brief.md",
    "recommended_direction": "",
    "stitch_visual_source_mode": {
      "enabled": true,
      "mode": "stitch_visual_source_of_truth",
      "locked_stitch_visual_refs": [],
      "included_stitch_suggestions": [],
      "excluded_stitch_suggestions": [],
      "deferred_or_routed_suggestions": [],
      "approved_visual_deviations": [],
      "stage_5_handoff_impact": "none"
    },
    "alternatives_considered": [],
    "key_decisions": [],
    "assumptions": [],
    "risks": [],
    "downstream_impact": [],
    "user_decision_required": true,
    "approval_status": "pending | approved | revise | rejected",
    "approved_by": "",
    "approved_at": "",
    "revision_notes": []
  }
}
```

Stage 4 may not lock UX/UI direction or use `ready_for_stage_5` unless:

```text
stage_decision_brief.approval_status = approved
```

---

# Completion Gate

Before Stage 4 may use `ready_for_stage_5`, it must run `global-stage-readiness-audit` and write:

```text
Build-Plans/Build-status/Stage-4-readiness-audit.json
```

The audit must pass according to:

```text
System-References/Docs/Global-Stage-Workflow-Contract.md
```

Stage 4 may complete only when:

* all nine UX, UI blueprint, design system, and complete app blueprint outputs exist
* primary user journeys are defined
* interaction architecture supports MVP workflows
* screen system supports all launch-critical journeys
* feature behaviors are specified
* state transitions are mapped
* accessibility framework exists
* one primary UI architecture template is selected, or a blocking reason is recorded
* selected UI architecture extensions are compatible with the primary template or documented as deviations
* Stitch MCP availability, project reuse or creation, screen references, and any accepted non-Stitch fallback are recorded in shared Stage 4 state
* Stitch visual source control is recorded, defaults on, and has approval status before final synthesis
* Stitch screenshot evidence is recorded in `stitch_prototyping.screenshot_evidence` when Stitch generated pages are used for page approval
* every Stitch-suggested component, data display, interaction, navigation item, workflow change, or feature extension has an include, exclude, revise, defer, or route decision before final synthesis
* every proposed Stitch page used for approval has at least one desktop screenshot or an approved evidence exception
* every launch-critical approved Stitch page has at least one mobile screenshot or an approved evidence exception
* Stitch pages with modal, drawer, branching, destructive, mutation, or complex interaction states have extra screenshots or approved evidence exceptions
* every proposed Stitch page has a page approval ledger entry
* every approved Stitch page reconciles to exactly one canonical page or screen reference
* rejected and deferred Stitch pages remain recorded and excluded from canonical launch scope
* page-level approval occurs before component extraction is finalized
* every approved-page component is classified as static or interactive and maps to its owning page, section, and canonical component reference
* every interactive component exposes its triggering elements and aggregates its canonical route and action references
* UI blueprints exist for all launch-critical pages and screens
* each launch-critical UI blueprint includes page purpose, primary user, screen type, layout type, sections, components, actions, data needs, states, validation, and navigation
* each launch-critical UI blueprint includes a selected page archetype
* each launch-critical UI blueprint includes a layout pattern decision with selected pattern, reasons, source references, rejected plausible alternatives, and responsive transformation
* comparison-heavy pages avoid `card-grid` unless explicitly justified
* `data-table` pages define mobile transformation, sorting, filtering, loading, empty, no-results, error, and bulk-selection behavior where applicable
* template deviations include subject, template default, project choice, reason, and source references
* each selected page or screen type includes `page_type_selection_rationale`
* each launch-critical UI blueprint includes a visual spec with style, density, color direction, typography feel, component style, primary visual focus, responsive behavior, visual do and don't rules, visual acceptance criteria, and user approval status
* design system foundation exists and defines shared color, typography, spacing, radius, elevation, icon, component, responsive, selected visual style references, and accessibility rules
* launch-critical visual specs reference or align with the design system foundation
* launch-critical visual specs reference selected visual style references or explicitly record why no visual reference applies
* launch-critical visual specs and design system approval statuses are approved or explicitly accepted as assumptions
* frontend build package includes page inventory, component inventory, shared components, routes, actions, states, frontend task hints, and recommended frontend skills
* complete app blueprint markdown exists at `Build-Plans/Stage-4/09-complete-app-blueprint.md`
* complete app blueprint markdown includes every launch-critical page and maps each page to a `ui_blueprint_id`
* complete app blueprint markdown renders every approved page using the exact `Page -> Section -> Component -> Interactive Element -> Route, Action, Or No Navigation` hierarchy
* complete app blueprint markdown does not skip hierarchy levels or flatten sections, components, or interactive elements into summary bullets
* complete app blueprint markdown includes page sections, components, actions, routes, states, data requirements, and frontend build package summary
* complete app blueprint markdown includes structural UI architecture summary when template selection was used
* `UI-COMPONENTS.md` remains reconcilable with `09-complete-app-blueprint.md` and preserves the same page, section, component, and interactive-element ownership chain
* launch-critical screens include role access, required data, actions, states, responsive requirements, and accessibility requirements
* launch-critical feature behaviors include acceptance criteria and validation rules
* Stage 5 handoff includes implementation units, UI blueprint IDs, component inventory, frontend build package, validation requirements, responsive requirements, and UX risks
* high and critical UX risks have mitigation paths
* critical interactive guidance questions are answered or converted into recorded assumptions
* no interaction-blocking Stage 3 unknowns remain unresolved
* every created page has a reconciled interaction contract and enumerates every clickable or interactive element
* every element uses a stable `UI-ELEMENT-` ID and resolves to a `ROUTE-` ID, `ACTION-` ID, or explicit `no_navigation`
* no approved page omits a required `Section`, `Component`, or `Interactive Element` level when the element exists in canonical structured outputs
* approved Stitch pages contain no orphan component, interactive element, route, or action
* action_inventory is complete for all created pages and records triggering elements and outcomes
* route_inventory covers all navigation paths used by interactive elements
* launch-critical and high-risk interactions include required design-system, responsive, accessibility, confirmation, permission, outcome, and recovery behavior
* approved launch-critical Stitch pages have desktop, tablet, and mobile review results and post-extraction accessibility review results or approved exceptions
* every Stitch divergence has a canonical constraint, resolution, rationale, affected references, and approval status
* required Mermaid maps reconcile with page, element, route, action, and navigation inventories
* no required interaction contract remains `needs_user_review` or `blocked`
* Stage 4 decision brief exists and is approved

---

# Validation Checklist

Before completing Stage 4, confirm:

* Stage 4 did not redefine product strategy
* Stage 4 did not redesign backend architecture
* Stage 4 did not write implementation tickets
* Stage 4 did not generate frontend code
* every MVP workflow has a user journey
* every launch-critical feature has behavior rules
* every required screen maps to a journey or feature
* every launch-critical page has a UI blueprint
* every launch-critical page appears in `09-complete-app-blueprint.md`
* every selected page type has an inclusion rationale tied to upstream product, workflow, role, feature, journey, or route evidence
* every launch-critical page records UI architecture template context, page archetype, layout pattern decision, component-family decisions, and deviations when applicable
* every data-dense or comparison-heavy page uses an appropriate layout pattern or records an explicit deviation
* Stitch prototype prompts constrain scope, roles, routes, actions, data concepts, design-system usage, required states, responsive behavior, accessibility, and exclusions
* every proposed Stitch page has an approval ledger entry with status, rationale, approver, and source references
* every proposed Stitch page used for approval has screenshot evidence linked to the page ledger
* launch-critical approved Stitch pages include mobile screenshot evidence or an approved exception
* complex Stitch interaction states include screenshot evidence or an approved exception
* Stitch visual source control mode and suggestion review decisions are reflected in the Stage 4 decision brief
* only approved Stitch pages are reconciled into canonical UI blueprints
* every approved-page component was extracted after page-level approval
* every interactive component embeds applicable route and action references, while static components carry empty interaction mappings
* every extracted interactive element resolves to a canonical route, action, or `no_navigation` behavior
* every Stitch divergence is resolved without silently changing upstream product scope or backend architecture
* responsive review covers content priority, navigation transformation, component reflow, data density, touch targets, overflow, and interaction substitutions
* accessibility review covers keyboard operation, focus, accessible names, structure, labels, contrast, status announcements, validation, errors, and overlay behavior
* Stitch-specific metadata remains Stage-4-local and does not alter Stage 5 through Stage 8 contracts
* every UI blueprint uses the page-definition matrix
* every launch-critical UI blueprint uses the visual spec matrix
* every launch-critical UI blueprint includes visual acceptance criteria and user approval status
* design system foundation exists for launch-critical frontend work
* visual references, liked patterns, disliked patterns, and design approval status are recorded when available
* every created page maps page -> section -> component -> interactive element -> route, action, or `no_navigation` -> outcome
* every interactive element has a stable ID, owner, label or accessible name, behavior, source trace, and valid resolution
* every internal navigation target resolves in route_inventory and external targets are explicitly classified
* every action in action_inventory maps back to its owning page and component
* every route in route_inventory maps to a blueprint page_ref
* every navigation item has a route_target pointing to a valid route in route_inventory
* destructive and permission-gated interactions include confirmation, denied, and recovery behavior where applicable
* clickable containers do not conflict with nested controls and duplicate labels do not hide conflicting behavior
* required Mermaid maps reconcile with structured inventories
* component inventory, shared components, routes, states, actions, and interactive elements are defined
* frontend build package is usable by frontend-design, frontend-builder, task generators, and agent builders
* complete app blueprint markdown is usable by Stage 5 without reinterpreting page, component, route, action, state, or data requirements
* every core workflow has states and recovery behavior
* accessibility risks are recorded
* critical interactive guidance questions are answered or converted into recorded assumptions
* Stage 5 handoff is usable for development orchestration
* Stage 4 decision brief approval is recorded before Stage 5 handoff is used

---

# A-Grade Workflow Compliance

Stage 4 must consume `stage_contract_profile` and `guidance_policy`.

Stage 4 output validation should reference:

```text
System-References/Schemas/stage-4-output.schema.json
```

UI blueprints, visual specs, design system decisions, accessibility proof, and reference assets should be recorded or referenced in:

```text
Build-Plans/Build-status/Artifact-evidence-registry.json
```

Stage 4 readiness must also record:

```json
{
  "schema_validation": {},
  "reference_integrity": {},
  "risk_acceptance_ledger": {},
  "revision_loops": []
}
```

Stage 4 may not use `ready_for_stage_5` until required schema validation passes, UI blueprint, visual spec, design system, journey, screen, action, state, and accessibility references resolve to Stage 1-3 source IDs, accepted high and critical UX or visual risks are written to `Build-Plans/Build-status/Risk-acceptance-ledger.json`, and failed readiness checks are converted into revision-loop actions.
