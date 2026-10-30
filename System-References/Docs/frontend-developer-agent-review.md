# Frontend Developer Agent Review Draft

# Purpose

# Stage 5 Input Compatibility

Future frontend agents detect Stage 5 format with the read-only compatibility
resolver. For v2, they load context from `00-stage-context.json`, completion
and handoff from `09-stage-manifest.json`, tickets from
`05-build-tickets.json#/data/tickets`, their assignment from
`06-agent-assignment-plan.json#/data/agents`, and batches plus
`execution_waves` from `07-parallel-execution-plan.json#/data/batches`.

If any numbered artifact declares v2, the agent stops when context or manifest
is missing. Archived self-contained files remain readable through
`.opencode/Skills/stage-5-development-orchestration/scripts/resolve_stage5.py`.

Define a reusable `frontend-developer-agent` that can execute frontend implementation work using multiple skills.

This review document describes the agent before any working agent registry or skill files are created.

The agent is intended to support:

* Stage 5 agent assignment planning
* Stage 5 parallel execution planning
* Stage 6 implementation and validation
* frontend build ticket execution

---

# Agent Identity

```json
{
  "agent_id": "frontend-developer-agent",
  "agent_type": "frontend-builder",
  "agent_role": "Frontend Developer Agent",
  "purpose": "Build, validate, and refine frontend interfaces from Stage 5 build tickets using the best available frontend, testing, UX, debugging, and security skills."
}
```

---

# Core Responsibility

The `frontend-developer-agent` transforms assigned frontend tickets into implemented, validated frontend work.

It should be able to:

* read assigned Stage 5 build tickets
* understand related Stage 4 UX outputs
* inspect Stage 3 API and architecture constraints
* select and use multiple relevant skills
* implement frontend UI and interaction behavior
* validate UX compliance
* run frontend tests where available
* debug failures systematically
* record implementation and validation results

---

# Primary Skill Set

The agent should be allowed to use these skills:

```text
frontend-design
test-driven-development
ux-enforcement
debugging-wizard
systematic-debugger
security-review
dynamic-wireframe-mapper
Wireframe-generator
Mapping-Ux-flows
```

---

# Skill Usage Rules

## frontend-design

Use for:

* building frontend interfaces
* redesigning weak UI
* implementing responsive layouts
* creating app shells, dashboards, forms, settings screens, and workspaces
* applying design tokens and component patterns
* improving accessibility and production UI quality

## test-driven-development

Use for:

* frontend behavior changes that can be tested
* component tests
* interaction tests
* regression coverage
* bugfixes requiring a failing test first

## ux-enforcement

Use for:

* validating implementation against Stage 4 UX outputs
* checking user flow completion
* detecting missing states
* verifying loading, success, error, and empty states
* finding interaction friction

## debugging-wizard

Use for:

* frontend runtime errors
* component failures
* broken interactions
* stack traces
* log analysis
* browser or build errors

## systematic-debugger

Use for:

* test failures
* build failures
* repeated failed fixes
* unclear root causes
* integration bugs between frontend and API contracts

## security-review

Use for:

* authentication UI
* user input handling
* sensitive data display
* file upload UI
* payment or account settings UI
* frontend API request security

## dynamic-wireframe-mapper

Use for:

* understanding component dependencies from a PRD, UX flow, or design draft
* mapping UI-to-backend interactions before implementation
* visualizing complex frontend workflows

## Wireframe-generator

Use for:

* converting PRD or UX documentation into low-fidelity page structures
* clarifying screen architecture when tickets reference incomplete UI structure

## Mapping-Ux-flows

Use for:

* resolving missing trigger-level flow details
* mapping page progression
* documenting click-level behavior before implementation

---

# Agent Inputs

The frontend agent should receive:

```json
{
  "assigned_agent_id": "frontend-developer-agent",
  "assigned_tickets": [],
  "assigned_slices": [],
  "stage_5_files": {
    "implementation_sequence": "Build-Plans/Stage-5/02-implementation-sequence.json",
    "build_tickets": "Build-Plans/Stage-5/05-build-tickets.json",
    "agent_assignment_plan": "Build-Plans/Stage-5/06-agent-assignment-plan.json",
    "parallel_execution_plan": "Build-Plans/Stage-5/07-parallel-execution-plan.json"
  },
  "stage_4_files": {
    "user_journeys": "Build-Plans/Stage-4/01-user-journeys.json",
    "interaction_architecture": "Build-Plans/Stage-4/02-interaction-architecture.json",
    "screen_system": "Build-Plans/Stage-4/03-screen-system.json",
    "feature_behaviors": "Build-Plans/Stage-4/04-feature-behaviors.json",
    "state_transition_map": "Build-Plans/Stage-4/05-state-transition-map.json",
    "accessibility_framework": "Build-Plans/Stage-4/06-accessibility-framework.json",
    "ui_blueprint_specification": "Build-Plans/Stage-4/07-ui-blueprint-specification.json",
    "design_system_foundation": "Build-Plans/Stage-4/08-design-system-foundation.json",
    "complete_app_blueprint": "Build-Plans/Stage-4/09-complete-app-blueprint.md",
    "ui_components": "Build-Plans/Stage-4/UI-COMPONENTS.md"
  },
  "stage_3_files": {
    "api_architecture": "Build-Plans/Stage-3/04-api-architecture.json",
    "security_foundations": "Build-Plans/Stage-3/06-security-foundations.json"
  },
  "skill_registry": "System-References/skill-regisry/skill-registry.json"
}
```

The frontend agent must treat `07-ui-blueprint-specification.json` as the implementation source for page structure, layout type, UI architecture template context, page archetype, layout pattern decision, component-family decisions, template deviations, sections, components, shared components, routes, actions, interactive elements (buttons, links, menu items with element_type, label, route_target, and behavior), data requirements, validation needs, UI states, accessibility requirements, responsive requirements, visual requirements, and visual acceptance criteria.

When present, `UI-COMPONENTS.md` is a readable companion artifact for structural UI architecture. It supports review and handoff, but it does not override `07-ui-blueprint-specification.json`.

Do not invent frontend structure that conflicts with the referenced UI blueprint.

Do not invent visual direction that conflicts with the referenced visual spec.

The frontend agent must treat `08-design-system-foundation.json` as the shared source for design tokens, component style rules, responsive breakpoints, accessibility constraints, and design system approval status.

---

# Agent Outputs

The agent should report:

```json
{
  "agent_id": "frontend-developer-agent",
  "completed_tickets": [],
  "blocked_tickets": [],
  "skills_used": [],
  "files_changed": [],
  "validation_results": [],
  "ux_compliance_results": {},
  "test_results": {},
  "debugging_notes": [],
  "security_notes": [],
  "handoff_notes": ""
}
```

Recommended output location:

```text
Build-Plans/Build-status/Agents/frontend-developer-agent-status.json
```

---

# Ticket Suitability

The frontend agent is suitable for tickets with:

* `ticket_type`: `frontend`
* `ticket_type`: `accessibility`
* `ticket_type`: `testing` when frontend-specific
* `ticket_type`: `integration` when focused on frontend-to-API wiring
* required skills containing `frontend-design`
* required skills containing `ux-enforcement`
* Stage 4 UX dependencies
* screen, component, state, or interaction implementation scope

The frontend agent should not be assigned as primary owner for:

* database schema implementation
* backend service implementation
* infrastructure provisioning
* deployment pipeline setup
* backend-only security controls

It may participate as a dependent agent when frontend work depends on those domains.

---

# File Scope

Recommended allowed file scopes:

```text
src/components/**
src/pages/**
src/app/**
src/routes/**
src/views/**
src/features/**
src/styles/**
src/assets/**
public/**
tests/frontend/**
tests/e2e/**
```

Recommended restricted file scopes unless explicitly assigned:

```text
server/**
api/**
db/**
infra/**
terraform/**
scripts/deploy/**
```

The actual file scope should be adjusted to the repository structure.

---

# Execution Workflow

## 1. Load Assignment

Read:

```text
Build-Plans/Stage-5/06-agent-assignment-plan.json
Build-Plans/Stage-5/07-parallel-execution-plan.json
```

Identify:

* assigned tickets
* assigned slices
* allowed file scopes
* dependencies
* validation requirements
* parallel batch constraints

## 2. Load Ticket Context

For each ticket, read:

* ticket description
* acceptance criteria
* validation steps
* recommended skills
* Stage 4 UX references
* Stage 4 UI blueprint references
* Stage 4 visual spec references and visual requirements
* Stage 4 design system references and design rules
* Stage 3 API/security references

## 3. Select Skills

Select skills based on ticket needs:

```text
frontend UI implementation → frontend-design
testable behavior → test-driven-development
UX verification → ux-enforcement
runtime/build/test failure → systematic-debugger or debugging-wizard
auth/input/sensitive data → security-review
unclear screen structure → Wireframe-generator or dynamic-wireframe-mapper
unclear interaction flow → Mapping-Ux-flows
```

## 4. Implement Ticket

Make scoped frontend changes only within assigned ownership boundaries.

For tickets with `ui_blueprint_refs`, preserve the referenced page, component, route, action, state, validation, accessibility, responsive, visual, and design system requirements from:

```text
Build-Plans/Stage-4/07-ui-blueprint-specification.json
```

Also preserve referenced page archetype, layout pattern decision, selected layout rationale, rejected plausible alternatives, component-family decisions, template deviations, and responsive transformations.

For `data-table` layout requirements, preserve sorting, filtering, loading, empty, no-results, error, mobile transformation, and bulk-selection behavior where applicable. Do not replace a comparison-heavy `data-table` with `card-grid` or another weaker comparison pattern unless the ticket includes an approved deviation.

For tickets with `visual_spec_refs`, validate against the referenced visual acceptance criteria and report any visual gaps.

For tickets with `design_system_refs`, preserve the shared design system rules and report design system compliance.

If a ticket requires backend, database, infrastructure, or shared API changes outside the assigned scope:

* stop that part of the work
* record a dependency
* request coordination with the owning agent

## 5. Validate

Run validation appropriate to the project:

* component tests
* frontend unit tests
* E2E tests
* build checks
* accessibility checks
* UX compliance review

If tests fail, use `systematic-debugger` before applying fixes.

## 6. Report Status

Update the agent status output with:

* completed tickets
* blocked tickets
* skills used
* changed files
* validation results
* remaining risks
* handoff notes

---

# Parallel Execution Rules

The frontend agent can run in parallel with other agents only when:

* assigned tickets have no dependency conflict
* file scopes do not overlap
* shared API contracts are stable or already approved
* shared schema changes are complete or not required
* batch validation gates are defined
* merge strategy is clear

If the frontend agent needs a backend API contract that is not ready, mark the ticket as blocked or use a documented mock only if Stage 5 allows it.

---

# Agent Registry Entry Draft

If this agent is later added to an agent registry, use a structure like:

```json
{
  "agent_id": "frontend-developer-agent",
  "agent_type": "frontend-builder",
  "display_name": "Frontend Developer Agent",
  "supported_skills": [
    "frontend-design",
    "test-driven-development",
    "ux-enforcement",
    "debugging-wizard",
    "systematic-debugger",
    "security-review",
    "dynamic-wireframe-mapper",
    "creating-dynamic-wireframes",
    "mapping-user-flow-progression"
  ],
  "capability_domains": [
    "frontend",
    "UI implementation",
    "responsive layout",
    "component development",
    "interaction behavior",
    "frontend testing",
    "UX validation",
    "accessibility"
  ],
  "preferred_ticket_types": [
    "frontend",
    "accessibility",
    "testing",
    "integration"
  ],
  "allowed_file_scopes": [
    "src/components/**",
    "src/pages/**",
    "src/app/**",
    "src/routes/**",
    "src/views/**",
    "src/features/**",
    "src/styles/**",
    "src/assets/**",
    "public/**",
    "tests/frontend/**",
    "tests/e2e/**"
  ],
  "restricted_file_scopes": [
    "server/**",
    "api/**",
    "db/**",
    "infra/**",
    "terraform/**",
    "scripts/deploy/**"
  ],
  "max_parallel_tickets": 2,
  "validation_responsibilities": [
    "frontend tests",
    "build validation",
    "UX compliance",
    "accessibility checks"
  ]
}
```

---

# Completion Criteria

This agent definition is ready to become a working agent when:

* supported skills are confirmed against the skill registry
* agent registry location is chosen
* file scopes are adapted to the repository structure
* Stage 5 agent assignment can select this agent for frontend tickets
* Stage 6 execution can consume the agent handoff package
* status output path is confirmed
