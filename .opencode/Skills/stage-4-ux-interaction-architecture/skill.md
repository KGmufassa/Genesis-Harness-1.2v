---
name: stage-4-ux-interaction-architecture
description: The stage-4-ux-interaction-architecture command orchestrates Stage 4.
compatibility: opencode
---

# Command — stage-4-ux-interaction-architecture

# Purpose

The `stage-4-ux-interaction-architecture` command orchestrates Stage 4.

It transforms:

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
* treat Stitch prototypes as canonical product, route, action, permission, or data contracts

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

For every created page, infer a complete interactive element proposal before asking the user. A created page is any page or screen recorded in `page_inventory` or `ui_blueprints`.

Classify each created page as:

```text
launch_critical
standard
supporting
deferred
```

Present the proposed interactive elements for approval only when the choice materially changes workflow scope, permissions, destructive behavior, route or action outcomes, accessibility, or Stage 5 implementation. Ask the user to approve, remove, rename, reroute, or add elements. Record low-risk inferred elements in `interactive_guidance.assumptions_made`.

Every page interaction contract must use one approval status:

```text
approved
assumed_low_risk
needs_user_review
blocked
```

When Stitch MCP is available, confirm the proposed page set and each page's major layout and feature regions before finalizing component inventories. Do not ask the user to approve individual low-risk components until the page-level decision is recorded.

Stitch is an internal Stage 4 prototyping and review aid. Approved prototypes refine Stage 4 outputs, but the structured Stage 4 page, component, route, action, state, accessibility, and design-system contracts remain canonical. Keep Stitch-specific metadata out of `stage_5_handoff`.

Do not add, remove, rename, or repurpose any `stage_5_handoff` fields because Stitch was used. Stage 5 must consume the same canonical Stage 4 handoff regardless of whether Stitch was available.

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

The Stitch MCP loop is a command phase, not a replacement for a Stage 4 skill.

---

# Execution Sequence

## 1. Load Stage 1, Stage 2, And Stage 3 Outputs

Load Stage 1 outputs from `Build-Plans/Stage-1/`.

Load Stage 2 outputs from `Build-Plans/Stage-2/`.

Load Stage 3 outputs from `Build-Plans/Stage-3/`.

Normalize them into:

```text
stage_1_inputs
stage_2_inputs
stage_3_inputs
```

Do not modify earlier stage outputs during Stage 4.

---

## 2. Initialize Shared UX State

Create or load:

```text
Build-Plans/Build-status/UX-state.json
```

Initialize missing fields using the shared UX state schema.

---

## 3. Run `user-journey-design`

Required shared state updates:

```text
user_journeys
ux_decisions
ux_risks
open_questions
interactive_guidance
```

---

## 4. Run `interaction-architecture-design`

Required shared state updates:

```text
interaction_architecture
ux_decisions
ux_risks
interaction_tradeoffs
interactive_guidance
```

---

## 5. Run `screen-system-design`

Required shared state updates:

```text
screen_system
ux_decisions
ux_risks
open_questions
interactive_guidance
```

---

## 6. Run `feature-behavior-specification`

Required shared state updates:

```text
feature_behaviors
ux_decisions
ux_risks
interaction_tradeoffs
interactive_guidance
```

---

## 7. Run `state-transition-and-accessibility-design`

Required shared state updates:

```text
state_transition_map
accessibility_framework
ux_decisions
ux_risks
interactive_guidance
```

---

## 8. Run `design-system-foundation`

Required shared state updates:

```text
design_system_foundation
visual_reference_selection
visual_spec_inventory
stage_5_handoff
ux_confidence_gaps
interactive_guidance
```

---

## 9. Run `ui-architecture-template-selection`

Required shared state updates:

```text
ui_architecture_template_selection
ux_decisions
ux_risks
open_questions
interactive_guidance
```

The skill must select one primary structural UI architecture template and any justified extensions from:

```text
.opencode/Skills/ui-blueprint-specification/references/ui-component-system/
```

The library is read-only during normal Stage 4 runs. Record template deviations and template gaps in shared state instead of modifying library files.

---

## 10. Run The Stitch MCP Prototype And Page-Confirmation Loop

Use the selected design system, UI architecture template, journeys, screen system, feature behaviors, states, accessibility constraints, and upstream scope to create or update Stitch screens.

Run a read-only capability preflight before generating anything. Record the discovered MCP server and tool names for project create/reuse, screen generate/update, screen list/read, and screenshot/export operations in `stitch_prototyping.prototype_constraints`. Set `stitch_prototyping.availability` to `available`, `unavailable`, or `partial`. Missing create, read, or screenshot capability makes availability `partial` and requires the same explicit fallback decision as an unavailable server.

Required shared state updates:

```text
stitch_prototyping
interactive_guidance
ux_decisions
ux_risks
open_questions
```

Apply this sequence:

```text
constrain prototype prompt
-> reuse or create Stitch project
-> generate launch-critical page candidates
-> capture prototype screenshot evidence
-> review Stitch visual, component, data-display, interaction, and feature-extension suggestions
-> review major responsive and accessibility behavior
-> confirm pages and major feature regions with the user
-> inventory components for approved pages
-> reconcile every interactive component to route, action, or no_navigation
-> record divergences and confidence gaps
```

Do not let Stitch introduce unsupported product scope, backend concepts, permissions, routes, or actions. Record conflicts in `stitch_prototyping.divergence_log` and resolve them in favor of canonical upstream constraints unless the user approves a routed revision.

If Stitch MCP is unavailable, record the failure and confidence gap. Continue with the existing Stage 4 workflow only when the user explicitly accepts the non-Stitch fallback; otherwise use `blocked`.

Never delete a Stitch project or screen without explicit user approval.

Store Stitch screenshot evidence locally in:

```text
Build-Plans/Stage-4/Screen-shots/
```

Record screenshot evidence in `stitch_prototyping.screenshot_evidence`. Capture at least one desktop screenshot for every proposed page, one mobile screenshot for every launch-critical approved page, and extra screenshots for modals, drawers, branching flows, or complex interaction states. Screenshot evidence is Stage-4-local and must not be added to `stage_5_handoff`.

By default, `stitch_prototyping.visual_source_control.enabled` is `true`. When enabled, approved Stitch screens and locked screenshot evidence are the Stage 4 visual source of truth for visual specs, design-system derivation, component visual treatment, page-level visual hierarchy, and responsive visual treatment.

Stitch visual source of truth is visual-only. It must not control product scope, routes, actions, permissions, data/API contracts, accessibility requirements, or Stage 5 handoff fields.

Record every Stitch-suggested visual pattern, component, data display, interaction, navigation item, workflow change, or feature extension in `stitch_prototyping.suggestion_review_ledger` before including it in canonical Stage 4 outputs. Each suggestion must be explicitly included, excluded, revised, deferred, or routed to a prior stage. Include suggestions only when they align with PRD, workflow, feature, route, action, data, or design-system references, or when the user approves the appropriate Stage 4 or prior-stage revision.

---

## 11. Run `ui-blueprint-specification`

Required shared state updates:

```text
ui_blueprints
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
ux_confidence_gaps
interactive_guidance
```

---

## 12. Run `ux-interaction-synthesis`

Required shared state updates:

```text
ui_blueprints
visual_spec_inventory
design_system_foundation
visual_reference_selection
frontend_build_package
ux_decisions
ux_risks
interaction_tradeoffs
stage_5_handoff
completion_status
interactive_guidance
```

---

# Final Stage 4 Outputs

Generate:

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

When useful for human review and Stage 5 handoff, also derive:

```text
Build-Plans/Stage-4/UI-COMPONENTS.md
```

`UI-COMPONENTS.md` is a generated companion artifact. It is not the canonical Stage 4 source of truth.

`09-complete-app-blueprint.md` must render approved pages using the exact `Page -> Section -> Component -> Interactive Element -> Route, Action, Or No Navigation` hierarchy. `UI-COMPONENTS.md` must remain reconcilable with that same ownership chain and must not flatten page, section, component, or interactive-element levels into summary prose.

Each output must include:

* related Stage 1 workflows or features
* related Stage 3 architecture constraints where applicable
* UX decisions
* risks and constraints
* unresolved questions
* Stage 5 handoff notes when relevant

---

# Stage Decision Brief

Before final synthesis or `ready_for_stage_5`, generate:

```text
Build-Plans/Stage-4/00-stage-decision-brief.md
```

The brief uses the recommended approach to propose UX/UI direction before build tickets are generated.

The brief must include Stitch visual source-of-truth status when Stitch was available or used:

* whether `stitch_prototyping.visual_source_control.enabled` is on or off
* locked Stitch screen and screenshot references used as visual source evidence
* included Stitch suggestions
* excluded Stitch suggestions
* deferred or prior-stage-routed Stitch suggestions
* any approved visual deviations from Stitch
* confirmation that Stage 5 handoff impact is `none`

Ask:

```text
Do you approve this recommended UX/UI direction?
```

Allowed user decisions:

```text
Approve recommended UI direction
Revise visual style
Revise page/screen structure
Revise navigation/layout
Revise component priorities
```

Record the brief in shared UX state as `stage_decision_brief`.

Do not use `ready_for_stage_5` unless:

```text
stage_decision_brief.approval_status = approved
```

---

# Completion Gate

Before Stage 4 may use `ready_for_stage_5`, run `global-stage-readiness-audit`.

The audit must write:

```text
Build-Plans/Build-status/Stage-4-readiness-audit.json
```

The audit must pass according to:

```text
System-References/Docs/Global-Stage-Workflow-Contract.md
```

If the audit does not pass, do not use `ready_for_stage_5`.

Stage 4 may complete only when:

* all nine UX, UI blueprint, design system, and complete app blueprint outputs exist
* primary user journeys are defined
* interaction architecture supports MVP workflows
* screen system supports all launch-critical journeys
* feature behaviors are specified
* state transitions are mapped
* accessibility framework exists
* one primary UI architecture template is selected, or a blocking reason is recorded
* selected UI architecture extensions are compatible with the primary template or documented as project deviations
* Stitch availability, project reuse or creation, screen references, and any accepted fallback are recorded in Stage 4 shared state
* Stitch visual source control is recorded, defaults on, and has approval status before final synthesis
* Stitch screenshot evidence is recorded in `stitch_prototyping.screenshot_evidence` when Stitch generated pages are used for page approval
* every Stitch-suggested component, data display, interaction, navigation item, workflow change, or feature extension has an include, exclude, revise, defer, or route decision before final synthesis
* every proposed Stitch page used for approval has at least one desktop screenshot or an approved evidence exception
* every launch-critical approved Stitch page has at least one mobile screenshot or an approved evidence exception
* Stitch pages with modal, drawer, branching, destructive, mutation, or complex interaction states have extra screenshots or approved evidence exceptions
* every approved Stitch page is reconciled to exactly one canonical page or screen reference, and every rejected or deferred prototype page is recorded
* page-level approval is recorded before component extraction is treated as final
* UI blueprints exist for all launch-critical pages and screens
* each launch-critical UI blueprint includes page purpose, primary user, screen type, layout type, sections, components, actions, data needs, states, validation, and navigation
* each launch-critical UI blueprint includes a page archetype and layout pattern decision with reasons, source references, rejected plausible patterns, and responsive transformation
* each selected page or screen type includes `page_type_selection_rationale`
* each launch-critical UI blueprint includes visual style, density, color direction, typography feel, component style, primary visual focus, responsive behavior, visual do and don't rules, visual acceptance criteria, and user approval status
* complete app blueprint markdown exists at `Build-Plans/Stage-4/09-complete-app-blueprint.md`
* complete app blueprint markdown includes every launch-critical page and maps each page to a `ui_blueprint_id`
* complete app blueprint markdown includes page sections, components, actions, routes, states, data requirements, and frontend build package summary
* complete app blueprint markdown includes an app-level Mermaid route map and Mermaid detail maps for launch-critical or complex interaction flows
* design system foundation exists and defines shared color, typography, spacing, radius, elevation, icon, component, and responsive rules
* design system foundation records selected visual style references and converts them into shared design-system rules
* launch-critical visual specs reference or align with the design system foundation
* launch-critical visual specs reference selected visual style references or explicitly record why no visual reference applies
* launch-critical visual specs and design system approval statuses are approved or explicitly accepted as assumptions
* frontend build package includes page inventory, component inventory, shared components, routes, actions, states, frontend task hints, and recommended frontend skills
* template deviations and template gaps are recorded when project needs override or exceed the selected UI architecture template
* high and critical UX risks have mitigation paths
* critical interactive guidance questions are answered or converted into recorded assumptions
* no interaction-blocking Stage 3 unknowns remain unresolved
* every created page has a page interaction contract, criticality, and approval status
* every created page enumerates every clickable or interactive element, including buttons, links, icon controls, menus, tabs, form controls, clickable cards or rows, pagination, breadcrumbs, modal or drawer triggers, downloads, and global navigation
* every component extracted from an approved Stitch page is classified as static or interactive and maps to its owning page, section, and canonical component reference
* every extracted interactive component exposes its triggering elements and embeds the applicable canonical route and action references; static components explicitly carry no interaction mappings
* every interactive element uses a stable `UI-ELEMENT-` ID and resolves to a `ROUTE-` ID, an `ACTION-` ID, or an explicit `no_navigation` behavior
* every navigate or open-link element has a route target that exists in the route inventory or is recorded as an external URL
* action_inventory is complete for all created pages and maps every action to its owning page, component, triggering element, and outcome
* route_inventory covers all navigation paths used by interactive elements
* destructive, security-sensitive, payment, admin, permission-sensitive, and mutation actions define confirmation, success, failure, loading, permission-denied, and recovery behavior where applicable
* launch-critical interactive elements map to design-system components and define responsive and accessibility behavior, or record an approved exception
* approved Stitch pages have desktop, tablet, and mobile review results plus keyboard, focus, labeling, contrast, and error-state accessibility review results or recorded approved exceptions
* no approved prototype contains an orphan page, component, route, action, or interactive element
* pages with branching, destructive, mutation, modal, drawer, or complex routing behavior have Mermaid interaction maps in `09-complete-app-blueprint.md`
* no required interaction contract remains `needs_user_review` or `blocked`
* Stage 4 decision brief exists and is approved

Possible completion statuses:

```text
ready_for_stage_5
needs_ux_revision
needs_stage_3_revision
blocked
```

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
* every launch-critical page has a selected page archetype and layout pattern decision
* every selected layout pattern has reasons, source references, rejected plausible alternatives, and desktop/tablet/mobile behavior
* data-table layouts define mobile transformation, sorting/filtering expectations, loading, empty, no-results, error, and bulk-selection behavior where applicable
* comparison-heavy pages do not use card-grid unless explicitly justified
* bulk-action pages define selection behavior
* required UI architecture template deviations are recorded with reasons
* Stitch prompts constrain scope, roles, routes, actions, data concepts, design-system usage, required states, responsive behavior, and accessibility expectations
* every proposed Stitch page has an approval-ledger entry with status, rationale, approver, and source references
* every proposed Stitch page used for approval has screenshot evidence linked to the page ledger
* launch-critical approved Stitch pages include mobile screenshot evidence or an approved exception
* Stitch visual source control mode and suggestion review decisions are reflected in the Stage 4 decision brief
* approved Stitch pages reconcile to canonical Stage 4 page IDs without adding unapproved scope
* Stitch divergence entries identify the prototype proposal, conflicting canonical constraint, resolution, and affected references
* Stitch-specific metadata remains Stage-4-local and is not required by Stage 5 or later stages
* Stage 5 behavior, sequencing, validation, and handoff consumption do not change based on whether Stitch was used
* every UI blueprint uses the page-definition matrix
* every launch-critical UI blueprint uses the visual spec matrix
* design system foundation exists for launch-critical frontend work
* selected visual style references are recorded before UI blueprints are finalized
* every approved page in `09-complete-app-blueprint.md` preserves the exact `page -> section -> component -> interactive element -> route/action/no_navigation` hierarchy
* complete app blueprint markdown does not skip hierarchy levels or flatten sections, components, or interactive elements into summary bullets
* every created page maps page -> section -> component -> interactive element -> route or action outcome
* `UI-COMPONENTS.md` remains structurally reconcilable with `09-complete-app-blueprint.md` and preserves the same ownership chain for pages, sections, components, and interactive elements
* every clickable or interactive element has a stable ID, label or accessible name, behavior, owner, source trace, and route, action, or `no_navigation` classification
* no approved page omits a required section, component, or interactive-element level when that level exists in canonical structured outputs
* route_inventory contains every path used by interactive elements across all pages
* action_inventory maps every action to its triggering elements, owning pages and components, and success, failure, loading, and recovery outcomes where applicable
* navigation items have structured route_target entries that resolve in route_inventory
* destructive actions define confirmation and recovery behavior
* permission-gated actions define allowed and denied states
* clickable containers do not conflict with nested controls or row actions
* duplicate labels do not resolve to conflicting behaviors without contextual accessible names
* required Mermaid maps reconcile with interaction, route, action, and navigation inventories
* component inventory, shared components, routes, states, actions, and interactive elements are defined
* complete app blueprint markdown is usable by Stage 5 without reinterpreting page, component, route, action, state, or data requirements
* every core workflow has states and recovery behavior
* accessibility risks are recorded
* critical interactive guidance questions are answered or converted into recorded assumptions
* Stage 5 handoff is usable for development orchestration
* Stage 4 decision brief approval is recorded before Stage 5 handoff is used

---

# A-Grade Workflow Compliance

Stage 4 must consume `stage_contract_profile` and `guidance_policy`.

Stage 4 must reference:

```text
System-References/Schemas/stage-4-output.schema.json
```

UI blueprints, visual specs, selected visual style references, design system decisions, accessibility proof, and reference assets should be recorded or referenced in:

```text
Build-Plans/Build-status/Artifact-evidence-registry.json
```

Before using `ready_for_stage_5`, Stage 4 must provide `schema_validation`, `reference_integrity`, `risk_acceptance_ledger`, and `revision_loops` in the readiness audit or stage state.

Accepted high and critical UX, visual, accessibility, or design-system risks must be recorded in:

```text
Build-Plans/Build-status/Risk-acceptance-ledger.json
```

Failed readiness checks must become revision-loop actions with owning output, owning skill, required change, and next action.
