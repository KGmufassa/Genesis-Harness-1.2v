# Plan: Stage 4 Button-Level Action→Route Granularity

## Approved Tightened Scope

Implement the interaction contract across Stage 4 through Stage 8. Do not update the optional Stage 1–3 producer contracts.

1. Stage 4 is the source of truth for every created page, defined as every page in `page_inventory` or `ui_blueprints`.
1. Every created page receives a criticality, compact interaction contract, approval status, and complete clickable-element inventory.
1. Use stable `UI-ELEMENT-`, `ROUTE-`, and `ACTION-` IDs and preserve them through tickets, implementation, validation, launch, and telemetry.
1. Infer interactive elements from workflows, journeys, behaviors, permissions, states, accessibility, page type, and design-system direction. Ask the user to approve, remove, rename, reroute, or add elements only when the decision is material.
1. Record route types and action outcomes, including confirmation, success, failure, loading, permission-denied, undo, and recovery behavior where applicable.
1. Use `design-system-foundation` to define button hierarchy, links, menus, tabs, interactive containers, states, responsive affordances, and accessibility treatment.
1. Require an app-level Mermaid route map and page or workflow maps for branching, destructive, mutation, modal, drawer, or complex routing flows. Permit trivial pages to rely on reconciled inventories.
1. Stage 5 tickets, sequencing, agent assignments, and handoffs must consume the interaction contracts and stable IDs.
1. Stage 6 must validate exact conformance and record approved deviations for dropped, renamed, rerouted, or behavior-changed interactions.
1. Stage 7 must treat unresolved launch-critical interaction failures as launch blockers or accepted risks tied to stable IDs.
1. Stage 8 must map telemetry and findings to stable interaction IDs and related Stage 5 ticket and Stage 6 validation references.

Implementation status: applied to Stage 4–8 skill contracts, related draft contracts, Stage 4 schema, and global ID standards. Optional Stage 1–3 updates remain excluded.

---

## Objective

Enhance Stage 4 UI blueprints to enumerate every interactive element (button, link, menu item, etc.) on every page:
- `element_type` (button, link, icon_button, etc.)
- `label` (visible text)
- `route_target` (where it navigates, e.g. `/dashboard/stats/{id}`)
- `behavior` (navigate, submit, open_modal, toggle, etc.)
- `states` (default, loading, disabled, active, hover)
- `permission_required`

Plus: global `route_inventory` (every route path + owning page), global `action_inventory` (every action → page/component/route).

---

## Execution Order (3 Phases)

### Phase 1: Stage 4 Draft Doc (Review Document)
### Phase 2: Stage 4 Command Skill + Subskills
### Phase 3: Dependent Stage Docs + Downstream Skills

---

## Phase 1 — Stage 4 Draft Doc First

### File: `System-References/Docs/Stage-4-ux-interaction-architecture-draft.md`

#### 1a — Add interactive element, action inventory, route inventory, navigation inventory schemas

**Location:** After line 603 (end of Blueprint structure JSON), before "Orchestrated Skills"

**Action:** Insert these 4 new schema blocks:

--- Interactive Element Schema ---
Every interactive element on a page must be enumerated with:
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

--- Action Inventory Schema ---
```json
{
  "action_id": "",
  "name": "",
  "element_type": "button | link | icon_button | ...",
  "label": "",
  "route_target": "",
  "behavior": "navigate | submit | ...",
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

--- Route Inventory Schema ---
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

--- Navigation Inventory Schema ---
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

#### 1b — Expand UI blueprint structure

**Location:** Lines 564-603 (blueprint JSON block)

**Action:** Replace the current blueprint structure with:
```json
{
  "ui_blueprint_id": "UI-BLUEPRINT-001",
  "page_or_screen_id": "",
  "page_name": "",
  "purpose": "",
  "primary_user_role": "",
  "screen_type": "",
  "layout_type": "",
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
              "element_type": "button | link | icon_button | ...",
              "label": "",
              "route_target": "",
              "action_id": "",
              "behavior": "navigate | submit | ...",
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

#### 1c — Update screen entry schema

**Location:** Lines 388-403 (screen entry)

**Action:** Add `interactive_elements` array with:
```json
"interactive_elements": [
  {
    "element_id": "",
    "element_type": "button | link | icon_button | ...",
    "label": "",
    "route_target": "",
    "action_id": "",
    "behavior": "navigate | submit | ...",
    "behavior_target": "",
    "permission_required": "",
    "confirmation_required": false,
    "states": {},
    "owning_component": "",
    "owning_section": ""
  }
]
```

#### 1d — Update completion gate conditions

**Location:** Near end of draft (completion gate section)

**Action:** Add after "no interaction-blocking Stage 3 unknowns remain unresolved":
```
* every launch-critical UI blueprint enumerates every interactive element (buttons, links, menu items, etc.) on the page
* every interactive element with navigate behavior has a route_target that exists in the route inventory
* action_inventory is complete for all launch-critical pages and maps every action to its route_target
* route_inventory covers all navigation paths used by interactive elements
```

#### 1e — Update validation checklist

**Location:** Near end of draft (validation checklist)

**Action:** Add:
```
* every UI blueprint maps page → section → component → interactive element → route_target
* every launch-critical button, link, and interactive element has a defined route_target or action behavior
* route_inventory contains every path used by interactive elements across all pages
* action_inventory maps every interactive element to its owning page, component, and route
* navigation items have structured route_target entries that resolve in route_inventory
```

---

## Phase 2 — Stage 4 Command Skill + Subskills

### 2a: `.opencode/Skills/ui-blueprint-specification/skill.md`

**Change:** Add interactive element + inventory schemas after Visual Hierarchy Model section
**Change:** Replace ui_blueprints[] entry (lines 301-322) with expanded section→component→interactive_elements hierarchy
**Change:** Replace validation responsibilities with button-level rules

### 2b: `.opencode/Skills/stage-4-ux-interaction-architecture/skill.md`

**Change:** Add 4 new completion gate conditions (matching Phase 1d)
**Change:** Add 5 new validation checklist items (matching Phase 1e)

### 2c: `.opencode/Skills/screen-system-design/skill.md`

**Change:** Add `interactive_elements` array to the screen entry schema definition
**Change:** Add 2 validation rules: "every screen records its interactive elements with route_targets and behavior", "every interactive element references a valid route or action"

### 2d: `.opencode/Skills/ux-interaction-synthesis/skill.md`

**Change:** Add 5 validation checklist items (same as Phase 1e)

---

## Phase 3 — Dependent Stage Docs + Downstream Skills

### 3a: Stage 5 Chain

| File | Changes |
|------|---------|
| `System-References/Docs/Stage-5-development-orchestration-draft.md` | Update preflight check (line 334) to also verify interactive element completeness. Update build ticket contract to reference interactive_element_ids alongside action_refs. |
| `.opencode/Skills/stage-5-development-orchestration/skill.md` | Update preflight validation and validation checklist to cover interactive element granularity. |
| `.opencode/Skills/build-ticket-generation/skill.md` | No structural changes needed — `action_refs` already exists. Add validation rule: frontend tickets with `ui_blueprint_refs` must reference interactive elements where applicable. |
| `.opencode/Skills/agent-assignment-planning/skill.md` | No structural changes needed. Add validation: agent handoffs include interactive element definitions from UI blueprints. |
| `.opencode/Skills/implementation-sequence-planning/skill.md` | Add sequencing note: interactive element dependencies (modals, drawers, nested routes) should be sequenced after their parent pages. |

### 3b: Stage 6 Chain

| File | Changes |
|------|---------|
| `System-References/Docs/Stage-6-implementation-validation-draft.md` | Update UI blueprint validation section (lines 489-502) to include interactive element validation. Update completion gate (line 1292) to preserve interactive element → route mapping. |
| `.opencode/Skills/implementation-execution/skill.md` | Add validation: every executed frontend ticket preserves interactive element definitions and route targets. |
| `.opencode/Skills/validation-execution/skill.md` | Add validation: frontend validation results map interactive elements to route targets. |
| `.opencode/Skills/stage-6-implementation-validation/skill.md` | Update completion gate (line 474) to include interactive element preservation. |

### 3c: Other Docs

| File | Changes |
|------|---------|
| `System-References/Docs/frontend-developer-agent-review.md` | Reference interactive element → route mapping section in UI blueprint. |
| `System-References/Docs/Global-Stage-Readiness-Audit.md` | No structural changes — `ui_blueprint_refs_present` already covers blueprint presence. |

---

## Change Type Summary

| Type | Count | Files |
|------|-------|-------|
| **Structural** (new schemas, expanded fields) | 3 | Stage 4 draft doc, ui-blueprint-specification skill, screen-system-design skill |
| **Checklist/gate** (new conditions, new validations) | 7 | stage-4 command, ux-interaction-synthesis, stage-5 draft, stage-5 command, stage-6 draft, stage-6 command, build-ticket-generation |
| **Validation-only** (consumer checklist items) | 5 | implementation-execution, validation-execution, agent-assignment-planning, implementation-sequence-planning, frontend-developer-agent-review |
| **Design direction** | 1 | design-system-foundation skill |
| **No change needed** | 1 | Global-Stage-Readiness-Audit |
