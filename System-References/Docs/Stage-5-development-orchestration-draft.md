# Stage 5 — Development Orchestration Command & Skill Draft

# Core Philosophy

Stage 5 is centered around:

```text
software execution cognition
```

NOT:

* product discovery
* market validation
* system architecture design
* UX interaction design
* direct implementation

Those responsibilities belong to other stages.

Stage 5 is responsible for transforming product, architecture, and UX plans into an executable engineering plan.

The stage focuses on:

* development roadmap planning
* implementation sequencing
* dependency scheduling
* testing strategy
* engineering coordination
* release planning

---

# Stage 5 Core Purpose

Transform:

* Stage 1 product model
* Stage 2 validation outputs
* Stage 3 system architecture
* Stage 4 UX and interaction architecture
* known risks, dependencies, and constraints

into:

* development roadmap
* implementation sequence
* engineering dependency map
* testing strategy
* build tickets
* agent assignment plan
* parallel execution plan
* release plan

---

# Recommended Stage 5 Architecture

```text
stage-5-development-orchestration (command)
│
├── development-roadmap-planning
├── implementation-sequence-planning
├── engineering-dependency-planning
├── testing-strategy-planning
├── build-ticket-generation
├── agent-assignment-planning
├── parallel-execution-planning
├── release-plan-orchestration
└── development-orchestration-synthesis
```

---

# Stage 5 Command

# Command — stage-5-development-orchestration

# Purpose

# Normalized Stage 5 Output Contract — Version 2.0

This section supersedes legacy self-contained Stage 5 output examples elsewhere
in this draft.

Future intentional Stage 5 runs write:

```text
Build-Plans/Stage-5/00-stage-context.json
Build-Plans/Stage-5/01-development-roadmap.json
Build-Plans/Stage-5/02-implementation-sequence.json
Build-Plans/Stage-5/03-engineering-dependencies.json
Build-Plans/Stage-5/04-testing-strategy.json
Build-Plans/Stage-5/05-build-tickets.json
Build-Plans/Stage-5/06-agent-assignment-plan.json
Build-Plans/Stage-5/07-parallel-execution-plan.json
Build-Plans/Stage-5/08-release-plan.json
Build-Plans/Stage-5/09-stage-manifest.json
```

File `00` is the sole shared-context source. Files `01`-`08` use the normalized
v2 envelope and contain only canonical data under `data`. Tickets, agents, and
batches exist only at `/data/tickets`, `/data/agents`, and `/data/batches`.
Testing and release collections remain nested in their canonical strategies.
Secondary views use IDs or compact indexes and records use `risk_refs`.

File `09` indexes all numbered artifacts and their schema/data paths. Completion
status and the Stage 6 handoff exist only in this manifest. Schema validity may
be true only after validation executed.

The reusable implementation and validation rules are in:

```text
.opencode/Skills/stage-5-development-orchestration/scripts/stage5_contract.py
```

Before serialization they validate real Stage 1-4 stable IDs, file-plus-JSON-
Pointer targets, risk references, agent scope coverage, and dependency-safe
execution waves. Generation fails on validation errors. Visual acceptance
criteria without stable IDs use file-plus-JSON-Pointer references; identifiers
must never be fabricated.

For v2 expected-artifact evidence, future registry updates set
`related_stage_output` to `Build-Plans/Stage-5/05-build-tickets.json` and
`related_stage_data_path` to `/data/tickets`.

The `stage-5-development-orchestration` command orchestrates Stage 5.

It transforms the validated product model, technical architecture, and UX architecture into a development execution plan that is ready for Stage 6 implementation and validation.

This is the Stage 5 command skill. It is not a single planning subskill.

---

# Cognitive Boundary

Stage 5 asks:

```text
How should engineering execution be sequenced, coordinated, tested, and released?
```

Stage 5 must not:

* redefine product strategy
* perform validation research
* redesign system architecture
* redesign UX flows
* write production code
* perform QA execution

Stage 5 may recommend earlier-stage revision only when execution planning exposes a blocking dependency, missing specification, or unresolved contradiction.

---

# Output Directory

All final Stage 5 outputs must be recorded in:

```text
Build-Plans/Stage-5/
```

The command must create this folder if it does not exist.

---

# Shared Development Orchestration State

The command maintains a shared Stage 5 development orchestration state object.

The shared orchestration state must be written to:

```text
Build-Plans/Build-status/Development-state.json
```

The command must load this file at the beginning of Stage 5, update it after each orchestration skill runs, and preserve it as the durable engineering planning state for the build.

```json
{
  "stage": "Stage 5",
  "command": "stage-5-development-orchestration",
  "status": "not_started",
  "stage_1_inputs": {},
  "stage_2_inputs": {},
  "stage_3_inputs": {},
  "stage_4_inputs": {},
  "preflight": {},
  "ui_blueprint_inputs": {},
  "visual_spec_inputs": {},
  "visual_reference_inputs": {},
  "design_system_inputs": {},
  "frontend_build_package": {},
  "development_roadmap": {},
  "implementation_sequence": {},
  "engineering_dependencies": {},
  "testing_strategy": {},
  "build_tickets": {},
  "agent_assignment_plan": {},
  "parallel_execution_plan": {},
  "environment_execution_plan": {},
  "dev_server_plan": {},
  "validation_command_plan": {},
  "artifact_expectations": {},
  "retry_policy": {},
  "release_plan": {},
  "milestones": [],
  "workstreams": [],
  "execution_risks": [],
  "coordination_notes": [],
  "open_questions": [],
  "interactive_guidance": {
    "open_questions": [],
    "answered_questions": [],
    "assumptions_made": [],
    "blocked_decisions": [],
    "user_confirmations": [],
    "execution_confidence_gaps": []
  },
  "stage_6_handoff": {},
  "completion_status": {}
}
```

Each subskill reads the current development state and writes its updates back into the shared state before the next skill runs.

After each subskill completes, the command must persist the updated shared state to:

```text
Build-Plans/Build-status/Development-state.json
```

---

# Interactive Guidance Rules

The Stage 5 command should behave like a guided engineering execution planning interview.

Use this decision rule:

```text
Ask only for execution decisions that materially affect implementation order, dependency sequencing, testing scope, release readiness, or Stage 6 execution.
Infer standard engineering defaults when risk is low and earlier-stage outputs support the inference.
Record assumptions when proceeding without user confirmation.
Block only when a missing decision prevents coherent engineering orchestration.
```

When asking the user questions:

* ask 1-3 questions at a time
* prioritize implementation-blocking dependencies first
* avoid asking questions already answered by Stages 1-4
* explain what roadmap, sequence, dependency, test, or release decision each question affects
* prefer concrete options over open-ended questions when the tradeoff is known
* update `interactive_guidance.open_questions`
* move answered questions into `interactive_guidance.answered_questions`
* record inferred defaults in `interactive_guidance.assumptions_made`
* record unresolved blockers in `interactive_guidance.blocked_decisions`

The command should continue automatically when an engineering planning decision has a low-risk default.

The command should pause for user input when:

* MVP launch scope is still ambiguous
* implementation order depends on an unresolved product or architecture decision
* dependency sequencing changes engineering feasibility
* testing scope materially changes release confidence
* release strategy affects what must be built first
* manual workaround tolerance is unknown
* Stage 6 cannot begin without a missing execution decision

The command should not ask the user to choose low-level implementation details that belong to Stage 6 unless the choice changes Stage 5 sequencing, testing, or release planning.

---

# Stage 5 Input Contract

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

Load Stage 4 outputs from:

```text
Build-Plans/Stage-4/
```

Required Stage 3 files:

```text
01-system-topology.json
02-service-architecture.json
03-data-architecture.json
04-api-architecture.json
05-integration-architecture.json
06-security-foundations.json
07-infrastructure-model.json
08-scalability-framework.json
```

Stage 5 must also consume the approved Stage 3 `selected_stack` from the Stage 3 architecture state, decision brief, or Stage 3 handoff.

Stage 5 must not invent, change, or defer the implementation stack. If `selected_stack` is missing, incomplete, or contains unresolved alternatives, Stage 5 must block and create a revision loop back to Stage 3.

Required Stage 4 files:

```text
01-user-journeys.json
02-interaction-architecture.json
03-screen-system.json
04-feature-behaviors.json
05-state-transition-map.json
06-accessibility-framework.json
07-ui-blueprint-specification.json
08-design-system-foundation.json
09-complete-app-blueprint.md
```

Minimum viable input set:

```text
Stage 1:
05-feature-structure.json
08-mvp-operational-model.json
09-risk-and-constraints.json

Stage 3:
02-service-architecture.json
03-data-architecture.json
04-api-architecture.json
07-infrastructure-model.json

Stage 4:
03-screen-system.json
04-feature-behaviors.json
05-state-transition-map.json
07-ui-blueprint-specification.json
08-design-system-foundation.json
09-complete-app-blueprint.md
```

If the minimum viable input set is missing, stop and set:

```text
completion_status.status = "blocked"
completion_status.reason = "missing_development_orchestration_inputs"
```

If Stage 4 completion status is not `ready_for_stage_5`, continue only if unresolved issues are not execution-blocking. Record all carry-forward risks in `execution_risks`.

---

# Preflight Validation

Before development orchestration, validate:

* Stage 1 MVP scope exists
* Stage 3 architecture outputs exist and are readable
* Stage 3 `selected_stack` exists
* Stage 3 `selected_stack` has concrete choices for frontend, backend, database, auth, deployment, testing, and package manager
* Stage 3 `selected_stack` contains no unresolved alternatives such as `or`, `TBD`, `to decide later`, `optional`, or `depends`
* Stage 4 UX outputs exist and are readable
* Stage 4 UI blueprint output exists and is readable
* Stage 4 design system foundation exists and is readable
* Stage 4 complete app blueprint markdown exists and is readable
* Stage 4 UI architecture template selection exists or records why no template applies
* launch-critical features are known
* service, data, API, and infrastructure dependencies are available
* feature behaviors and state transitions are clear enough to sequence implementation
* UI blueprints define launch-critical pages, components, routes, actions, states, interactive elements (buttons, links, menu items, etc.) with route_targets, visual specs, visual acceptance criteria, and frontend build package hints
* launch-critical UI blueprints define structural UI architecture context, including page archetype, layout pattern decision, component-family decisions, selected template/extensions, and template deviations when applicable
* complete app blueprint markdown maps launch-critical pages to UI blueprint IDs and summarizes page sections, components, actions, routes, states, and data requirements
* complete app blueprint markdown summarizes UI architecture template selection, page archetypes, layout pattern decisions, component families, and template deviations when available
* Stage 5 does not require or consume Stitch project IDs, screen IDs, prompts, approval ledgers, divergence logs, or MCP availability metadata
* design system foundation defines shared visual tokens, component rules, responsive rules, and design approval status
* accessibility and security requirements are available for test planning
* earlier-stage risks do not block engineering planning

Record preflight results in:

```text
preflight
execution_risks
open_questions
interactive_guidance
completion_status
```

---

# Stage 6 Handoff Contract

Stage 5 must produce a concrete Stage 6 handoff, not general planning notes.

The `stage_6_handoff` object must include:

```json
{
  "build_tickets_file": "Build-Plans/Stage-5/05-build-tickets.json",
  "agent_assignment_file": "Build-Plans/Stage-5/06-agent-assignment-plan.json",
  "parallel_execution_file": "Build-Plans/Stage-5/07-parallel-execution-plan.json",
  "release_plan_file": "Build-Plans/Stage-5/08-release-plan.json",
  "execution_queue": [],
  "launch_critical_tickets": [],
  "manual_execution_tickets": [],
  "generated_agent_files": [],
  "required_skills_by_ticket": {},
  "ui_blueprint_refs_by_ticket": {},
  "visual_spec_refs_by_ticket": {},
  "visual_reference_refs_by_ticket": {},
  "design_system_refs_by_ticket": {},
  "visual_requirements_by_ticket": {},
  "frontend_build_package_refs": {},
  "validation_commands": {},
  "dev_server_plan": {},
  "environment_requirements": {},
  "file_scope_controls": {},
  "retry_policy": {},
  "artifact_expectations": {},
  "known_blockers": [],
  "accepted_risks": []
}
```

Stage 6 should be able to start from this handoff without reinterpreting Stage 5 intent.

---

# Environment And Dev Server Planning

Stage 5 must identify execution environment needs that Stage 6 should prepare before implementation.

The environment execution plan should include:

```json
{
  "detected_stack": [],
  "package_manager": "",
  "install_command": "",
  "setup_commands": [],
  "build_command": "",
  "test_commands": [],
  "lint_command": "",
  "typecheck_command": "",
  "required_environment_variables": [],
  "required_secrets": [],
  "external_services": [],
  "migration_commands": [],
  "seed_commands": [],
  "setup_risks": []
}
```

The dev server plan should include:

```json
{
  "dev_server_required": false,
  "dev_server_command": "",
  "expected_port": null,
  "expected_url": "",
  "smoke_test_url": "",
  "healthcheck_path": "",
  "startup_timeout_seconds": 60,
  "server_required_for_tickets": [],
  "server_risks": []
}
```

If Stage 5 cannot determine setup commands safely, it must leave the field empty and record the question or risk instead of inventing commands.

---

# Validation Command Planning

Stage 5 must make testing strategy executable for Stage 6 whenever possible.

The validation command plan should include:

```json
{
  "unit_test_command": "",
  "integration_test_command": "",
  "e2e_test_command": "",
  "lint_command": "",
  "typecheck_command": "",
  "build_command": "",
  "smoke_test_command": "",
  "accessibility_check_command": "",
  "manual_validation_required": [],
  "missing_validation_commands": []
}
```

Each validation command must indicate:

* source of the command
* tickets or workflows it validates
* whether it is launch-critical
* whether failure blocks Stage 6 completion

---

# Orchestrated Skills

Run Stage 5 skills in this order:

```text
1. development-roadmap-planning
2. implementation-sequence-planning
3. engineering-dependency-planning
4. testing-strategy-planning
5. build-ticket-generation
6. agent-assignment-planning
7. parallel-execution-planning
8. release-plan-orchestration
9. development-orchestration-synthesis
```

---

# Skill — development-roadmap-planning

# Purpose

The `development-roadmap-planning` skill defines the engineering roadmap.

It determines:

* development phases
* workstreams
* milestones
* MVP build boundaries
* post-MVP deferrals
* engineering priorities

---

# Core Responsibilities

## Roadmap Structuring

Define:

* phase names
* phase goals
* launch-critical deliverables
* deferred deliverables
* workstreams
* milestone checkpoints
* readiness criteria per phase

## Scope Alignment

Validate:

* roadmap aligns with MVP scope
* roadmap respects architecture constraints
* roadmap supports UX flows
* roadmap avoids premature non-MVP complexity

## Roadmap Risk Detection

Identify:

* oversized phases
* unclear deliverables
* missing prerequisites
* risky parallel work
* unclear milestone criteria

---

# Interactive Guidance Responsibilities

This skill should guide the user only when roadmap scope or phase boundaries cannot be inferred safely.

Ask targeted questions when any of these are unclear:

* launch deadline or target milestone
* MVP vs post-MVP scope
* preferred phase granularity
* acceptable manual workarounds
* highest-priority user outcome
* whether risky features should be sequenced early or deferred

Infer standard roadmap phases when MVP scope and architecture are clear, but record the assumption in:

```text
interactive_guidance.assumptions_made
```

Pause for user input when roadmap scope changes release readiness, sequencing, or Stage 6 execution.

---

# Inputs

```json
{
  "mvp_scope": {},
  "feature_structure": {},
  "architecture_outputs": {},
  "ux_outputs": {},
  "existing_state": {}
}
```

---

# Outputs

```json
{
  "development_roadmap": {},
  "workstreams": [],
  "milestones": [],
  "deferred_work": [],
  "roadmap_risks": [],
  "open_questions": []
}
```

---

# Shared State Updates

```text
development_roadmap
workstreams
milestones
execution_risks
open_questions
interactive_guidance
```

---

# Skill — implementation-sequence-planning

# Purpose

The `implementation-sequence-planning` skill converts the roadmap into an ordered build sequence.

It determines:

* implementation order
* vertical slices
* foundational build steps
* feature sequencing
* dependency-aware task ordering
* Stage 6 execution readiness

---

# Core Responsibilities

## Sequence Planning

Define:

* foundation-first work
* service implementation order
* data model implementation order
* API implementation order
* UX implementation order
* integration implementation order
* validation checkpoints

## Slice Definition

Identify:

* end-to-end slices
* workflow-based slices
* infrastructure setup slices
* integration slices
* testing slices

## Sequence Risk Detection

Identify:

* blocked work
* premature feature work
* hidden prerequisites
* risky late integrations
* missing validation checkpoints

---

# Interactive Guidance Responsibilities

This skill should guide the user through sequencing decisions that affect engineering feasibility.

Ask targeted questions when any of these are unclear:

* whether to build by feature, workflow, service, or vertical slice
* which workflow should be implemented first
* whether risky integrations should be built early
* whether manual workflows are acceptable initially
* whether foundation work should precede user-facing work
* what must be demonstrable at each milestone

Infer a vertical-slice-first approach when product and UX workflows are clear, but record the assumption in:

```text
interactive_guidance.assumptions_made
```

Pause for user input when sequencing affects risk, timeline, validation, or implementation feasibility.

---

# Inputs

```json
{
  "development_roadmap": {},
  "service_architecture": {},
  "data_architecture": {},
  "api_architecture": {},
  "screen_system": {},
  "feature_behaviors": {},
  "existing_state": {}
}
```

---

# Outputs

```json
{
  "implementation_sequence": {},
  "implementation_slices": [],
  "sequence_dependencies": [],
  "validation_checkpoints": [],
  "sequence_risks": []
}
```

---

# Shared State Updates

```text
implementation_sequence
engineering_dependencies
execution_risks
coordination_notes
interactive_guidance
```

---

# Skill — engineering-dependency-planning

# Purpose

The `engineering-dependency-planning` skill maps engineering dependencies and coordination needs.

It determines:

* technical prerequisites
* cross-workstream dependencies
* sequencing blockers
* shared resources
* coordination risks
* handoff needs

---

# Core Responsibilities

## Dependency Mapping

Define:

* service dependencies
* data dependencies
* API dependencies
* integration dependencies
* UX dependencies
* security dependencies
* testing dependencies

## Coordination Planning

Identify:

* parallelizable work
* serial work
* handoff points
* required decisions
* owner domains
* coordination checkpoints

## Dependency Risk Detection

Identify:

* circular dependencies
* unclear ownership
* missing prerequisites
* risky parallelization
* unblocked vs blocked work

---

# Interactive Guidance Responsibilities

This skill should guide the user through dependency and coordination decisions that affect execution order.

Ask targeted questions when any of these are unclear:

* who or what owns a dependency
* whether work can proceed in parallel
* whether a third-party integration blocks core development
* whether data or API work must precede screens
* whether security foundations block user-facing features
* whether testing requires special setup

Infer standard dependency ordering when architecture makes the dependency obvious, but record the assumption in:

```text
interactive_guidance.assumptions_made
```

Pause for user input when dependency uncertainty blocks sequencing or release planning.

---

# Inputs

```json
{
  "implementation_sequence": {},
  "service_architecture": {},
  "data_architecture": {},
  "api_architecture": {},
  "integration_architecture": {},
  "screen_system": {},
  "existing_state": {}
}
```

---

# Outputs

```json
{
  "engineering_dependencies": {},
  "dependency_graph": [],
  "parallel_workstreams": [],
  "blocked_work": [],
  "coordination_notes": [],
  "dependency_risks": []
}
```

---

# Shared State Updates

```text
engineering_dependencies
coordination_notes
execution_risks
open_questions
interactive_guidance
```

---

# Skill — testing-strategy-planning

# Purpose

The `testing-strategy-planning` skill defines the validation and testing approach for Stage 6 execution.

It determines:

* test scope
* test levels
* regression strategy
* feature validation checkpoints
* integration testing needs
* accessibility testing needs
* release readiness testing

---

# Core Responsibilities

## Testing Strategy

Define:

* unit testing scope
* integration testing scope
* end-to-end testing scope
* API testing needs
* accessibility testing needs
* security testing needs
* regression testing strategy
* acceptance criteria

## Test Sequencing

Map testing to:

* implementation slices
* milestones
* workflows
* feature behaviors
* state transitions
* release checkpoints

## Testing Risk Detection

Identify:

* untestable behavior
* unclear acceptance criteria
* high-risk integrations
* missing accessibility coverage
* missing regression coverage
* release-blocking test gaps

---

# Interactive Guidance Responsibilities

This skill should guide the user through test planning decisions that materially affect release confidence.

Ask targeted questions when any of these are unclear:

* acceptable test depth for MVP
* release-blocking workflows
* required accessibility testing level
* manual vs automated validation tolerance
* critical integrations requiring test coverage
* acceptance criteria for launch-critical features

Infer baseline testing requirements when risk is low, but record the assumption in:

```text
interactive_guidance.assumptions_made
```

Pause for user input when testing scope changes release readiness or Stage 6 validation obligations.

---

# Inputs

```json
{
  "implementation_sequence": {},
  "feature_behaviors": {},
  "state_transition_map": {},
  "api_architecture": {},
  "integration_architecture": {},
  "security_foundations": {},
  "accessibility_framework": {},
  "existing_state": {}
}
```

---

# Outputs

```json
{
  "testing_strategy": {},
  "test_levels": [],
  "acceptance_criteria": [],
  "regression_strategy": {},
  "validation_command_plan": {},
  "dev_server_validation_needs": {},
  "artifact_expectations": {},
  "testing_risks": [],
  "release_test_gates": []
}
```

---

# Shared State Updates

```text
testing_strategy
validation_command_plan
dev_server_plan
artifact_expectations
execution_risks
coordination_notes
interactive_guidance
```

---

# Skill — build-ticket-generation

# Purpose

The `build-ticket-generation` skill converts implementation slices into executable build tickets for Stage 6.

It determines:

* ticket boundaries
* ticket ordering
* ticket prerequisites
* assigned implementation slice
* best-suited skill from the skill registry
* supporting skill chain
* skill suitability rationale
* validation requirements
* acceptance criteria
* Stage 6 execution handoff details

This skill is the task decomposition layer between Stage 5 orchestration and Stage 6 implementation.

---

# Core Responsibilities

## Ticket Generation

Create build tickets from:

* implementation slices
* roadmap phases
* engineering dependencies
* testing strategy
* feature behaviors
* architecture constraints
* UX dependencies
* UI blueprints
* frontend build package hints

Each ticket must be small enough to execute in Stage 6, but large enough to represent meaningful engineering progress.

## Ticket Contract

Every build ticket must include:

```json
{
  "ticket_id": "",
  "slice_id": "",
  "title": "",
  "description": "",
  "ticket_type": "",
  "priority": "",
  "stage_1_feature_refs": [],
  "stage_3_architecture_refs": [],
  "stage_4_ux_refs": [],
  "ui_blueprint_refs": [],
  "ui_architecture_refs": [],
  "page_archetype": "",
  "layout_pattern_refs": [],
  "component_family_refs": [],
  "template_deviation_refs": [],
  "ui_components_markdown_refs": [],
  "interaction_contract_refs": [],
  "visual_spec_refs": [],
  "visual_reference_refs": [],
  "design_system_refs": [],
  "page_refs": [],
  "component_refs": [],
  "shared_component_refs": [],
  "route_refs": [],
  "state_refs": [],
  "action_refs": [],
  "interactive_element_refs": [],
  "complete_app_blueprint_refs": [],
  "interaction_requirements": {
    "route_types": [],
    "action_outcomes": [],
    "confirmation_requirements": [],
    "permission_denied_behaviors": [],
    "recovery_requirements": [],
    "design_system_component_mappings": [],
    "mobile_behaviors": [],
    "accessibility_behaviors": []
  },
  "layout_requirements": {
    "selected_pattern": "",
    "rejected_patterns": [],
    "decision_factors": {},
    "reasons": [],
    "source_refs": [],
    "responsive_transformation": {}
  },
  "component_family_requirements": [],
  "frontend_task_hint": "",
  "visual_requirements": {
    "visual_style": "",
    "visual_reference_refs": [],
    "design_system_refs": [],
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
    "user_approval_status": ""
  },
  "responsive_requirements": {
    "desktop_layout": "",
    "tablet_layout": "",
    "mobile_layout": "",
    "collapse_rules": [],
    "navigation_behavior": "",
    "priority_content_mobile": []
  },
  "visual_acceptance_criteria_refs": [],
  "preview_required": false,
  "visual_qa_required": false,
  "design_system_compliance_required": false,
  "prerequisites": [],
  "depends_on_tickets": [],
  "primary_skill": "",
  "recommended_skills": [],
  "agent_required_skills": [],
  "agent_skill_instructions": {
    "must_use": [],
    "use_if_needed": [],
    "skill_usage_order": [],
    "usage_notes": ""
  },
  "skill_match": {
    "primary_skill_score": 0.0,
    "matched_capabilities": [],
    "matched_task_triggers": [],
    "matched_domains": [],
    "risk_flags_considered": [],
    "selection_reason": "",
    "coverage_gaps": []
  },
  "acceptance_criteria": [],
  "validation_steps": [],
  "validation_layers": [],
  "validation_commands": [],
  "dev_server_required": false,
  "dev_server_validation": {
    "requires_localhost": false,
    "expected_url": "",
    "smoke_test_path": ""
  },
  "environment_requirements": [],
  "artifact_expectations": [],
  "execution_policy": {
    "max_repair_attempts": 3,
    "max_validation_attempts": 3,
    "max_agent_retry_attempts": 2,
    "escalation_path": ""
  },
  "risk_level": "",
  "handoff_notes": "",
  "completion_status": "not_started"
}
```

Allowed `ticket_type` values:

```text
foundation
data
backend
frontend
integration
testing
security
accessibility
devops
documentation
```

Allowed `priority` values:

```text
critical
high
medium
low
deferred
```

Allowed `completion_status` values:

```text
not_started
in_progress
implemented
needs_validation
validation_failed
needs_repair
repair_in_progress
needs_revalidation
blocked
complete
deferred
failed
not_applicable
```

Stage 5 tickets should usually start as `not_started`.

Terminal statuses used by Stage 6:

```text
complete
blocked
deferred
failed
not_applicable
```

## Skill Registry Compatibility

When creating each build ticket, assign the best-suited skill and supporting skill chain from the available non-stage skills in:

```text
System-References/skill-regisry/skill-registry.json
```

The ticket generator should match ticket needs against skill registry fields:

* `task_triggers`
* `capabilities`
* `domains`
* `input_requirements`
* `risk_flags`
* `selection_priority`

The ticket generator must set:

```text
primary_skill
recommended_skills
agent_required_skills
agent_skill_instructions
skill_match
```

`primary_skill` is the single best-suited skill to lead the ticket.

`recommended_skills` is the ordered supporting skill chain. It should include the `primary_skill` first, followed by validation, debugging, UX, security, or supporting skills as needed.

`agent_required_skills` is the exact set of skills the assigned agent must use to complete the ticket.

`agent_skill_instructions` tells the assigned agent how to use those skills:

* `must_use` lists skills required for the task
* `use_if_needed` lists conditional skills for debugging, security, UX clarification, or validation
* `skill_usage_order` defines the preferred execution order
* `usage_notes` explains how the skills apply to the ticket

## Skill Suitability Scoring

Score candidate skills using:

* ticket type match
* task trigger match
* capability match
* implementation domain match
* input requirement fit
* expected output fit
* risk flag relevance
* selection priority
* validation requirements

Prefer a skill as `primary_skill` when it has the strongest implementation fit for the ticket.

Examples:

```text
frontend ticket → frontend-design
backend/API ticket → backend-development
test-first implementation ticket → test-driven-development as supporting skill
UX validation ticket → ux-enforcement
security-sensitive ticket → security-review as required supporting skill
bug or failure ticket → systematic-debugger or debugging-wizard
```

If no skill adequately covers the ticket, set:

```json
{
  "primary_skill": "unassigned",
  "recommended_skills": [],
  "skill_match": {
    "coverage_gaps": ["No registry skill covers the required capability"]
  }
}
```

and record the gap in `ticket_risks`.

Example:

```json
{
  "ticket_id": "TICKET-004",
  "slice_id": "slice-001",
  "title": "Build login screen",
  "primary_skill": "frontend-design",
  "recommended_skills": [
    "frontend-design",
    "test-driven-development",
    "ux-enforcement"
  ],
  "agent_required_skills": [
    "frontend-design",
    "test-driven-development",
    "ux-enforcement"
  ],
  "agent_skill_instructions": {
    "must_use": [
      "frontend-design",
      "ux-enforcement"
    ],
    "use_if_needed": [
      "test-driven-development",
      "systematic-debugger"
    ],
    "skill_usage_order": [
      "frontend-design",
      "test-driven-development",
      "ux-enforcement",
      "systematic-debugger"
    ],
    "usage_notes": "Use frontend-design for implementation, test-driven-development for testable behavior, ux-enforcement to verify the Stage 4 flow, and systematic-debugger if validation fails."
  },
  "skill_match": {
    "primary_skill_score": 0.92,
    "matched_capabilities": [
      "build frontend interface",
      "implement responsive interfaces"
    ],
    "matched_task_triggers": [
      "build frontend interface",
      "design UI"
    ],
    "matched_domains": [
      "frontend",
      "UI design"
    ],
    "risk_flags_considered": [
      "accessibility-risk",
      "responsive-risk"
    ],
    "selection_reason": "The ticket is primarily a frontend UI implementation task with UX validation and test coverage needs.",
    "coverage_gaps": []
  }
}
```

## Ticket Risk Detection

Identify:

* tickets with unclear prerequisites
* tickets without acceptance criteria
* tickets with missing validation steps
* tickets with missing executable validation commands when launch-critical
* tickets with missing dev server expectations when UI validation is required
* tickets with missing `expected_artifacts`
* tickets with missing retry or escalation policy for high-risk work
* tickets that depend on unresolved architecture or UX decisions
* tickets that are too broad for Stage 6 execution
* tickets that require skills unavailable in the registry
* tickets without a best-suited primary skill
* tickets with low skill suitability confidence

---

# Interactive Guidance Responsibilities

This skill should guide the user only when ticket boundaries or skill assignments cannot be inferred safely.

Ask targeted questions when any of these are unclear:

* whether a slice should be split into multiple tickets
* whether a ticket should be implementation-only or include validation
* whether risky work should receive a dedicated spike ticket
* whether manual setup work should be ticketed
* whether a ticket should be deferred from MVP
* whether an unavailable skill requires a new skill or manual owner
* whether low-confidence skill matches should proceed or require a new skill

Infer standard ticket decomposition when slices, dependencies, and testing strategy are clear, but record the assumption in:

```text
interactive_guidance.assumptions_made
```

Pause for user input when ticket uncertainty blocks Stage 6 execution.

---

# Inputs

```json
{
  "development_roadmap": {},
  "implementation_sequence": {},
  "implementation_slices": [],
  "engineering_dependencies": {},
  "testing_strategy": {},
  "feature_behaviors": {},
  "stage_1_inputs": {},
  "stage_3_inputs": {},
  "stage_4_inputs": {},
  "skill_registry": {},
  "existing_state": {}
}
```

---

# Outputs

```json
{
  "build_tickets": {},
  "tickets": [],
  "ticket_groups": [],
  "ticket_dependency_graph": [],
  "ticket_skill_assignments": [],
  "ticket_risks": [],
  "stage_6_execution_queue": []
}
```

---

# Shared State Updates

```text
build_tickets
engineering_dependencies
execution_risks
coordination_notes
stage_6_handoff
interactive_guidance
```

---

# Skill — agent-assignment-planning

# Purpose

The `agent-assignment-planning` skill assigns implementation slices and build tickets to specific execution agents.

It determines:

* available execution agents
* agent capability profiles
* required agent roles
* agent-to-slice assignments
* agent-to-ticket assignments
* required skill coverage per agent
* suitability score per assignment
* handoff inputs per agent
* validation obligations per agent
* ownership boundaries

This skill is the agent routing layer between build ticket generation and parallel execution planning.

This skill does not choose the task skills from scratch. It consumes the ticket-level fields created by `build-ticket-generation`:

```text
primary_skill
recommended_skills
agent_required_skills
agent_skill_instructions
skill_match
```

Its job is to find, assign, or generate an agent capable of using those required skills.

---

# Core Responsibilities

## Available Agent Scan

Scan the available agent inventory before assigning work.

The skill should load available agents from the configured agent registry or agent inventory, such as:

```text
.opencode/agents/
System-References/agent-registry/agent-registry.json
System-References/agents/available-agents.json
Build-Plans/Stage-5/available-agents.json
```

If no formal agent registry exists, the skill may infer provisional agent profiles from:

* ticket `agent_required_skills`
* ticket `agent_skill_instructions`
* Stage 5 ticket types
* implementation domains
* validation requirements

When provisional agents are inferred, record the assumption in:

```text
interactive_guidance.assumptions_made
```

The available agent scan must extract:

* agent ID
* agent type
* supported skills
* capability domains
* preferred ticket types
* file scope permissions
* maximum parallel workload
* validation responsibilities
* unavailable or restricted capabilities
* current assignment status when available

## Agent Assignment

Assign build tickets using:

* available agent profiles
* implementation slices
* ticket dependencies
* ticket `agent_required_skills`
* ticket `agent_skill_instructions`
* ticket `skill_match`
* architecture domains
* UX domains
* validation requirements
* risk levels

## Suitability Matching

For each ticket, score available agents against:

* ticket `agent_required_skills`
* ticket `agent_skill_instructions`
* required skill coverage
* ticket type
* implementation domain
* architecture references
* UX references
* validation requirements
* risk level
* file ownership permissions
* workload capacity
* dependency and coordination fit

Prefer the highest-suitability agent when:

* required ticket skills are supported
* ticket skill usage instructions can be followed
* file scopes do not conflict
* workload capacity is available
* validation responsibilities are covered
* assignment does not introduce dependency or merge conflicts

If no suitable agent exists, do not force assignment. Mark the ticket as:

```text
requires_manual_assignment
```

or:

```text
requires_new_agent_profile
```

and record the reason in `assignment_risks`.

## Agent Profile Contract

Each agent assignment must include:

```json
{
  "agent_id": "",
  "agent_type": "",
  "source_agent_profile": "",
  "suitability_score": 0.0,
  "assignment_reason": "",
  "assigned_slices": [],
  "assigned_tickets": [],
  "ticket_required_skills": [],
  "ticket_skill_instructions": {},
  "matched_skills": [],
  "missing_skills": [],
  "handoff_inputs": [],
  "owned_domains": [],
  "allowed_file_scopes": [],
  "restricted_file_scopes": [],
  "validation_requirements": [],
  "coordination_dependencies": [],
  "risk_level": "",
  "execution_notes": ""
}
```

## Generated Agent File Contract

When a suitable existing agent does not exist, the skill may generate a new subagent definition from the ticket's required skills and skill usage instructions.

Generated agents should use this markdown structure:

```markdown
---
description: ""
mode: subagent
temperature: 0.1
permission:
  edit: deny
  bash: deny
---

You are assigned to complete or review specific Stage 6 work.

Focus on:

- assigned tickets
- required skills
- acceptance criteria
- validation requirements
- risk controls
```

The agent file must be generated from:

* assigned ticket types
* ticket `primary_skill`
* ticket `recommended_skills`
* ticket `agent_required_skills`
* ticket `agent_skill_instructions`
* ticket acceptance criteria
* validation steps
* file ownership boundaries
* risk level
* required execution mode

Recommended generated agent output path:

```text
.opencode/agents/[agent-id].md
```

The skill must create `.opencode/agents/` if it does not exist before writing generated agent files.

The generated agent frontmatter must include:

```yaml
description: ""
mode: subagent
temperature: 0.1
permission:
  edit: deny
  bash: deny
```

## Generated Agent Prompt Template

Generated agent files must include a prompt body after the frontmatter.

The prompt body must be generated from:

* agent type
* assigned tickets
* assigned slices
* ticket `agent_required_skills`
* ticket `agent_skill_instructions`
* allowed file scopes
* restricted file scopes
* handoff inputs
* validation requirements
* permission settings
* risk level
* reporting requirements

Use this structure:

```markdown
You are a [agent role] assigned to Stage 6 [implementation/review/validation] tickets.

Your assigned tickets are:
- [ticket-id]: [ticket title]

Use these required skills:
- [skill-id]

Skill usage order:
1. Use `[skill-id]` to [skill-specific purpose].

You may edit only:
- [allowed file scope]

Do not edit:
- [restricted file scope]

Use these handoff inputs:
- [handoff file]

Validation requirements:
- [validation requirement]

Rules:
- Do not modify files outside your allowed scope.
- Do not invent behavior that conflicts with earlier-stage outputs.
- Do not change shared contracts unless the ticket explicitly allows it.
- If a dependency is missing, mark the ticket blocked and record the dependency.
- If validation fails, use the assigned debugging skill before applying fixes.
- Record every skill used and why.

When finished, report:
- completed tickets
- files changed
- skills used
- validation results
- blockers
- handoff notes
```

## Agent Stage 6 Report Contract

Every generated or assigned agent must be instructed to report in a structure Stage 6 can consume:

```json
{
  "agent_id": "",
  "assigned_ticket_ids": [],
  "completed_ticket_ids": [],
  "partial_ticket_ids": [],
  "blocked_ticket_ids": [],
  "files_changed": [],
  "skills_used": [],
  "skill_usage_notes": [],
  "validation_claims": [],
  "artifacts_created": [],
  "blockers": [],
  "next_action": "",
  "handoff_notes": ""
}
```

Agent validation claims are not final validation results. Stage 6 must verify them through `validation-execution`.

Review-only agents should replace implementation instructions with review instructions and must include:

```text
Provide constructive feedback without making direct changes.
```

## Generated Agent Model Policy

* generated agents must omit the `model` field
* OpenCode subagents inherit the model of the primary agent that invokes them when no agent-specific model is configured
* Stage 5 must not select, infer, or record a model for generated agents

Permission rules:

* review-only agents must use `edit: deny` and `bash: deny`
* implementation agents may use `edit: allow` only when Stage 6 execution requires code changes
* validation agents may use `bash: allow` only when tests, builds, or checks must run
* high-risk or security-review agents should default to deny permissions unless explicitly approved

Example review agent:

```markdown
---
description: Reviews code for quality and best practices
mode: subagent
temperature: 0.1
permission:
  edit: deny
  bash: deny
---

You are in code review mode. Focus on:

- Code quality and best practices
- Potential bugs and edge cases
- Performance implications
- Security considerations

Provide constructive feedback without making direct changes.
```

Example frontend implementation agent:

```markdown
---
description: Builds and validates assigned frontend tickets using selected frontend, testing, UX, debugging, and security skills
mode: subagent
temperature: 0.1
permission:
  edit: allow
  bash: allow
---

You are a frontend developer agent assigned to Stage 6 implementation tickets.

Your assigned tickets are:
- TICKET-004: Build login screen
- TICKET-005: Add login form validation
- TICKET-006: Validate login UX states

Use these required skills:
- frontend-design
- test-driven-development
- ux-enforcement
- systematic-debugger

Skill usage order:
1. Use `frontend-design` to implement the UI, layout, responsive behavior, and component structure.
2. Use `test-driven-development` for form validation and testable interaction behavior.
3. Use `ux-enforcement` to verify the implemented flow against Stage 4 UX requirements.
4. Use `systematic-debugger` if tests, build checks, or interaction validation fail.

You may edit only:
- `src/components/**`
- `src/app/**`
- `src/styles/**`
- `tests/frontend/**`

Do not edit:
- `server/**`
- `db/**`
- `infra/**`
- `scripts/deploy/**`

Use these handoff inputs:
- `Build-Plans/Stage-5/05-build-tickets.json`
- `Build-Plans/Stage-4/03-screen-system.json`
- `Build-Plans/Stage-4/04-feature-behaviors.json`
- `Build-Plans/Stage-4/05-state-transition-map.json`
- `Build-Plans/Stage-4/06-accessibility-framework.json`
- `Build-Plans/Stage-4/07-ui-blueprint-specification.json`

Use UI blueprints as the implementation source for page structure, layout type, sections, components, shared components, routes, actions, data requirements, validation needs, and required UI states.

Validation requirements:
- Login screen renders successfully.
- Default, loading, error, and success states are implemented.
- Form validation prevents invalid submission.
- UX flow matches Stage 4 interaction architecture.
- Frontend tests pass.
- Accessibility issues are recorded or fixed.

Rules:
- Do not modify files outside your allowed scope.
- Do not invent UX behavior that conflicts with Stage 4.
- Do not change API contracts unless the ticket explicitly allows it.
- If a backend dependency is missing, mark the ticket blocked and record the dependency.
- If validation fails, use `systematic-debugger` before applying fixes.
- Record every skill used and why.

When finished, report:
- completed tickets
- files changed
- skills used
- validation results
- blockers
- handoff notes
```

Recommended `agent_type` values:

```text
frontend-builder
backend-builder
fullstack-builder
data-builder
integration-builder
test-validation
security-review
devops
documentation
```

## Assignment Risk Detection

Identify:

* missing agent registry
* tickets without suitable agents
* agents that cannot use ticket-required skills
* agents assigned too much work
* generated agents missing ticket-required skills or skill instructions
* generated agents with unsafe permissions for their role
* unclear file or domain ownership
* cross-agent dependency conflicts
* high-risk tickets without validation ownership

---

# Interactive Guidance Responsibilities

This skill should guide the user only when agent ownership cannot be inferred safely.

Ask targeted questions when any of these are unclear:

* where available agents should be loaded from
* whether work should be split by domain, slice, or workflow
* whether one agent can own full-stack slices
* whether specialized agents are required for security, testing, or integrations
* whether file ownership boundaries should be strict or flexible
* whether high-risk tickets require a reviewer agent
* whether unavailable skills require a new agent type
* whether generated implementation agents may edit files or run commands

Infer domain-based assignment when ticket skills and file scopes are clear, but record the assumption in:

```text
interactive_guidance.assumptions_made
```

Pause for user input when ownership ambiguity could cause implementation conflict in Stage 6.

---

# Inputs

```json
{
  "implementation_sequence": {},
  "build_tickets": {},
  "engineering_dependencies": {},
  "testing_strategy": {},
  "available_agents": {},
  "agent_registry": {},
  "agent_generation_policy": {},
  "skill_registry": {},
  "existing_state": {}
}
```

---

# Outputs

```json
{
  "agent_assignment_plan": {},
  "available_agents": [],
  "agents": [],
  "ticket_assignments": [],
  "slice_assignments": [],
  "unassigned_tickets": [],
  "generated_agents": [],
  "generated_agent_files": [],
  "agent_handoff_packages": [],
  "assignment_risks": []
}
```

---

# Shared State Updates

```text
agent_assignment_plan
build_tickets
engineering_dependencies
execution_risks
coordination_notes
stage_6_handoff
interactive_guidance
```

---

# Skill — parallel-execution-planning

# Purpose

The `parallel-execution-planning` skill groups assigned tickets into dependency-safe parallel execution batches.

It determines:

* which agents can run at the same time
* batch order
* blocking dependencies
* file ownership conflicts
* merge and validation gates
* worktree or workspace isolation needs
* Stage 6 parallel execution readiness

This skill is the concurrency planning layer for multi-agent Stage 6 execution.

---

# Core Responsibilities

## Parallel Batch Planning

Create parallel batches from:

* ticket dependency graph
* agent assignment plan
* engineering dependencies
* file ownership boundaries
* integration risks
* testing strategy
* release gates

## Parallel Batch Contract

Each parallel batch must include:

```json
{
  "batch_id": "",
  "execution_order": 0,
  "can_run_in_parallel": true,
  "assigned_agents": [],
  "tickets": [],
  "blocked_by_batches": [],
  "file_ownership_boundaries": [],
  "file_locks": [],
  "shared_contracts": [],
  "merge_strategy": "",
  "merge_owner": "",
  "conflict_policy": "",
  "batch_validation": [],
  "failure_policy": "",
  "risk_level": "",
  "coordination_notes": []
}
```

Recommended `merge_strategy` values:

```text
validate_each_then_merge_batch
serial_merge_by_dependency
contract_review_before_merge
manual_review_required
```

Recommended `failure_policy` values:

```text
block_dependent_batches
continue_unrelated_batches
stop_all_parallel_work
manual_decision_required
```

## Conflict Control

Block parallel execution when tickets have:

* dependency conflicts
* file ownership conflicts
* shared API or schema conflicts
* unresolved architecture or UX decisions
* incompatible validation requirements
* high-risk integration overlap

Parallel batches must identify file locks for shared files, schema files, API contracts, routing files, configuration files, and migration files.

If a parallel batch fails, the parallel execution plan must state whether dependent batches stop, unrelated batches continue, or a manual decision is required.

## Workspace Isolation Guidance

When parallel work is approved, recommend isolated workspaces such as:

```text
worktrees/backend-agent
worktrees/frontend-agent
worktrees/testing-agent
```

Each agent should receive:

* assigned tickets
* allowed file scopes
* handoff inputs
* validation requirements
* merge expectations

---

# Interactive Guidance Responsibilities

This skill should guide the user only when parallel execution risk cannot be inferred safely.

Ask targeted questions when any of these are unclear:

* whether agents may work in separate git worktrees
* whether shared API or schema changes require serial execution
* whether file ownership boundaries are strict
* whether batch merges require manual approval
* whether high-risk integrations should run serially
* whether validation should happen per ticket, per agent, or per batch

Infer conservative serial execution for risky conflicts, but record the assumption in:

```text
interactive_guidance.assumptions_made
```

Pause for user input when parallel execution could create merge conflicts, data contract conflicts, or validation uncertainty.

---

# Inputs

```json
{
  "build_tickets": {},
  "agent_assignment_plan": {},
  "engineering_dependencies": {},
  "testing_strategy": {},
  "release_plan": {},
  "existing_state": {}
}
```

---

# Outputs

```json
{
  "parallel_execution_plan": {},
  "parallel_batches": [],
  "serial_batches": [],
  "conflict_controls": [],
  "workspace_plan": {},
  "merge_plan": {},
  "batch_validation_gates": [],
  "parallel_execution_risks": []
}
```

---

# Shared State Updates

```text
parallel_execution_plan
agent_assignment_plan
engineering_dependencies
execution_risks
coordination_notes
stage_6_handoff
interactive_guidance
```

---

# Skill — release-plan-orchestration

# Purpose

The `release-plan-orchestration` skill defines rollout sequencing and release readiness.

It determines:

* release phases
* launch scope
* rollout gates
* release readiness criteria
* deployment preparation needs
* rollback and recovery planning
* Stage 7 handoff implications

---

# Core Responsibilities

## Release Planning

Define:

* release phases
* MVP launch package
* launch gates
* release checklist
* rollout sequencing
* rollback requirements
* operational readiness needs

## Release Risk Detection

Identify:

* launch-blocking dependencies
* missing readiness criteria
* unsupported rollback
* fragile integrations
* unclear support expectations
* monitoring gaps

## Stage 7 Handoff Awareness

Prepare:

* deployment preparation notes
* monitoring needs
* analytics needs
* support needs
* operational tooling needs

---

# Interactive Guidance Responsibilities

This skill should guide the user through release decisions that affect launch readiness and Stage 7 operationalization.

Ask targeted questions when any of these are unclear:

* whether release should be private, beta, staged, or public
* what must be included in MVP launch
* what can be released after launch
* what conditions block release
* whether rollback or manual recovery is required
* what monitoring or support is needed at launch

Infer a conservative staged rollout when risk is moderate and launch constraints are unclear, but record the assumption in:

```text
interactive_guidance.assumptions_made
```

Pause for user input when release strategy changes implementation scope, testing scope, or operational readiness.

---

# Inputs

```json
{
  "development_roadmap": {},
  "implementation_sequence": {},
  "engineering_dependencies": {},
  "testing_strategy": {},
  "build_tickets": {},
  "agent_assignment_plan": {},
  "parallel_execution_plan": {},
  "mvp_scope": {},
  "existing_state": {}
}
```

---

# Outputs

```json
{
  "release_plan": {},
  "release_phases": [],
  "release_gates": [],
  "rollback_requirements": [],
  "stage_7_handoff_notes": {},
  "release_risks": []
}
```

---

# Shared State Updates

```text
release_plan
execution_risks
coordination_notes
stage_6_handoff
interactive_guidance
```

---

# Skill — development-orchestration-synthesis

# Purpose

The `development-orchestration-synthesis` skill combines all Stage 5 engineering planning intelligence into final outputs.

It produces:

* development roadmap
* implementation sequence
* engineering dependencies
* testing strategy
* build tickets
* agent assignment plan
* parallel execution plan
* release plan
* handoff guidance for Stage 6

---

# Core Responsibilities

## Execution Coherence

Validate:

* roadmap aligns with MVP scope
* implementation sequence respects dependencies
* engineering dependencies are explicit
* testing strategy covers launch-critical workflows
* build tickets cover implementation slices
* build tickets include required skill assignments and validation steps
* agent assignment plan maps tickets to capable agents
* parallel execution plan avoids dependency, file ownership, and shared contract conflicts
* release plan aligns with build sequence
* Stage 6 handoff is actionable

## Tradeoff Documentation

Record:

* sequencing decisions
* accepted execution risks
* deferred work
* coordination notes
* testing tradeoffs
* release tradeoffs

## Completion Determination

Determine whether Stage 5 is:

```text
ready_for_stage_6
needs_orchestration_revision
needs_earlier_stage_revision
blocked
```

---

# Interactive Guidance Responsibilities

This skill should not finalize Stage 5 if execution-blocking questions remain unresolved.

Before writing final outputs, inspect:

```text
interactive_guidance.open_questions
interactive_guidance.blocked_decisions
interactive_guidance.execution_confidence_gaps
execution_risks
open_questions
coordination_notes
```

Classify unresolved guidance items as:

```text
safe_to_assume
needs_user_confirmation
blocks_stage_5_completion
```

Ask the minimum number of final questions needed to complete Stage 5.

Do not ask broad implementation preference questions at this stage. Only ask questions tied directly to:

* missing final orchestration output fields
* unresolved sequencing decisions
* unresolved dependency blockers
* unresolved testing strategy decisions
* unresolved ticket decomposition, primary skill, recommended skill-chain, or agent skill-instruction decisions
* unresolved agent ownership decisions
* unresolved parallel execution conflicts
* unresolved release planning decisions
* execution risks that block Stage 6 handoff

If proceeding with assumptions, record them in:

```text
interactive_guidance.assumptions_made
```

If Stage 5 cannot complete, set `completion_status` to one of:

```text
needs_orchestration_revision
needs_earlier_stage_revision
blocked
```

and return the specific questions or decisions required.

---

# Inputs

```json
{
  "development_roadmap": {},
  "implementation_sequence": {},
  "engineering_dependencies": {},
  "testing_strategy": {},
  "build_tickets": {},
  "agent_assignment_plan": {},
  "parallel_execution_plan": {},
  "release_plan": {},
  "existing_state": {}
}
```

---

# Outputs

```json
{
  "orchestration_outputs": {},
  "build_tickets": {},
  "agent_assignment_plan": {},
  "parallel_execution_plan": {},
  "execution_risks": [],
  "coordination_notes": [],
  "stage_6_handoff": {},
  "completion_status": {}
}
```

---

# Final Stage 5 Outputs

Write or update:

```text
Build-Plans/Stage-5/00-stage-context.json
Build-Plans/Stage-5/01-development-roadmap.json
Build-Plans/Stage-5/02-implementation-sequence.json
Build-Plans/Stage-5/03-engineering-dependencies.json
Build-Plans/Stage-5/04-testing-strategy.json
Build-Plans/Stage-5/05-build-tickets.json
Build-Plans/Stage-5/06-agent-assignment-plan.json
Build-Plans/Stage-5/07-parallel-execution-plan.json
Build-Plans/Stage-5/08-release-plan.json
Build-Plans/Stage-5/09-stage-manifest.json
Build-Plans/Stage-5/10-stage-5-summary.md
```

`10-stage-5-summary.md` is a local human-readable review artifact for every Stage 5 finalization attempt, including ready, revision, and blocked outcomes. It must summarize the actions taken, roadmap, implementation sequence, ticket plan, agent assignments, parallel execution plan, release plan, validation and reference-integrity evidence, blockers, major risks, next actions, Stage 6 handoff readiness, and a clear user assessment. It must not contain canonical data that is absent from the JSON outputs.

Do not add `10-stage-5-summary.md` to `stage_6_handoff`, required Stage 6 inputs, artifact indexes, or downstream readiness requirements. Stage 6 must continue to consume the canonical Stage 5 JSON outputs and manifest.

## Final Output Schemas

`01-development-roadmap.json` must follow this structure:

```json
{
  "stage": "Stage 5",
  "status": "",
  "roadmap_phases": [],
  "workstreams": [],
  "milestones": [],
  "launch_critical_deliverables": [],
  "deferred_work": [],
  "roadmap_risks": [],
  "stage_6_handoff_notes": []
}
```

`02-implementation-sequence.json` must follow this structure:

```json
{
  "stage": "Stage 5",
  "status": "",
  "implementation_sequence": {},
  "implementation_slices": [],
  "validation_checkpoints": [],
  "sequence_dependencies": [],
  "execution_queue": [],
  "sequence_risks": []
}
```

`03-engineering-dependencies.json` must follow this structure:

```json
{
  "stage": "Stage 5",
  "status": "",
  "dependency_graph": [],
  "blocked_work": [],
  "parallel_workstreams": [],
  "shared_contracts": [],
  "file_ownership_boundaries": [],
  "coordination_notes": [],
  "dependency_risks": []
}
```

`04-testing-strategy.json` must follow this structure:

```json
{
  "stage": "Stage 5",
  "status": "",
  "testing_strategy": {},
  "test_levels": [],
  "acceptance_criteria": [],
  "regression_strategy": {},
  "validation_command_plan": {},
  "dev_server_validation_needs": {},
  "artifact_expectations": {},
  "testing_risks": [],
  "release_test_gates": []
}
```

`05-build-tickets.json` must follow this structure:

```json
{
  "stage": "Stage 5",
  "status": "",
  "tickets": [],
  "ticket_groups": [],
  "ticket_dependency_graph": [],
  "ticket_skill_assignments": [],
  "ticket_ui_blueprint_assignments": [],
  "ticket_visual_spec_assignments": [],
  "ticket_visual_reference_assignments": [],
  "ticket_design_system_assignments": [],
  "visual_acceptance_criteria_ticket_map": [],
  "ticket_artifact_expectations": [],
  "frontend_task_groups": [],
  "component_ticket_map": [],
  "stage_6_execution_queue": [],
  "retry_policy": {},
  "ticket_risks": []
}
```

`06-agent-assignment-plan.json` must follow this structure:

```json
{
  "stage": "Stage 5",
  "status": "",
  "available_agents": [],
  "agents": [],
  "ticket_assignments": [],
  "slice_assignments": [],
  "unassigned_tickets": [],
  "generated_agents": [],
  "generated_agent_files": [],
  "agent_handoff_packages": [],
  "agent_report_contract": {},
  "assignment_risks": []
}
```

`07-parallel-execution-plan.json` must follow this structure:

```json
{
  "stage": "Stage 5",
  "status": "",
  "parallel_batches": [],
  "serial_batches": [],
  "conflict_controls": [],
  "file_locks": [],
  "workspace_plan": {},
  "merge_plan": {},
  "batch_validation_gates": [],
  "failure_policies": [],
  "parallel_execution_risks": []
}
```

`08-release-plan.json` must follow this structure:

```json
{
  "stage": "Stage 5",
  "status": "",
  "release_plan": {},
  "release_phases": [],
  "release_gates": [],
  "rollback_requirements": [],
  "environment_execution_plan": {},
  "dev_server_plan": {},
  "stage_6_handoff": {},
  "stage_7_handoff_notes": {},
  "release_risks": []
}
```

Each output must include:

* related Stage 1 scope or feature inputs
* related Stage 3 architecture dependencies
* related Stage 4 UX dependencies
* related Stage 4 UI blueprint dependencies where applicable
* related Stage 4 visual spec dependencies where applicable
* related Stage 4 design system dependencies where applicable
* execution decisions
* risks and constraints
* unresolved questions
* Stage 6 handoff notes when relevant
* local human-readable assessment summary at `Build-Plans/Stage-5/10-stage-5-summary.md`

The build ticket output must include:

* ticket IDs
* slice IDs
* ticket dependencies
* UI blueprint references for frontend tickets
* UI architecture template, extension, page archetype, layout pattern, component family, and template deviation references for frontend tickets when applicable
* visual spec references and visual requirements for frontend tickets
* design system references for frontend tickets
* expected artifacts for tickets requiring validation, preview, visual QA, deployment proof, or launch-readiness evidence
* page, component, shared component, route, state, action, and interactive element references when applicable
* layout requirements and component-family requirements for frontend tickets when applicable
* frontend task hints from the Stage 4 frontend build package
* primary skill from the skill registry
* recommended skill chain from the skill registry
* required skills the assigned agent must use
* skill usage instructions for the assigned agent
* skill suitability score and selection rationale
* skill coverage gaps when no suitable skill exists
* acceptance criteria
* validation steps
* validation layers and executable validation commands when known
* dev server requirements for UI or browser-validated tickets
* `expected_artifacts`
* `completion_definition` for launch-critical workflow tickets
* `workflow_smoke_tests` with expected user outcomes for launch-critical workflow tickets
* retry and repair policy
* risk level
* Stage 6 execution queue position

The agent assignment output must include:

* available agent inventory source
* agent IDs
* agent types
* generated agent file paths when new agents are created
* generated agent files under `.opencode/agents/`
* generated agent frontmatter including description, mode, temperature, and permissions
* generated agent prompt body using the required prompt template
* assigned slices
* assigned tickets
* ticket-required skills consumed from build tickets
* ticket skill usage instructions consumed from build tickets
* matched and missing skills
* suitability scores
* assignment reasons
* handoff inputs
* owned domains
* allowed and restricted file scopes
* validation requirements
* required Stage 6 report structure
* unassigned tickets with manual-assignment or new-agent-profile reasons
* permission rationale for any generated agent with edit or bash access

The parallel execution output must include:

* parallel batch IDs
* assigned agents per batch
* tickets per batch
* blocked-by relationships
* file ownership boundaries
* file locks
* shared contracts
* merge strategy
* merge owner
* failure policy
* batch validation gates

The release output must include:

* environment execution plan
* dev server plan
* validation command plan
* Stage 6 handoff object
* setup, build, test, and start command assumptions
* known execution blockers
* accepted execution risks

---

# Completion Gate

Before Stage 5 may use `ready_for_stage_6`, it must run `global-stage-readiness-audit` and write:

```text
Build-Plans/Build-status/Stage-5-readiness-audit.json
```

The audit must pass according to:

```text
System-References/Docs/Global-Stage-Workflow-Contract.md
```

Stage 5 may complete only when:

* all eight development orchestration outputs exist
* development roadmap is defined
* implementation sequence is dependency-aware
* engineering dependencies are mapped
* testing strategy covers launch-critical workflows
* testing strategy includes executable validation commands or explicit manual validation fallback
* build tickets cover every MVP implementation slice
* build tickets include a best-suited primary skill or record why no matching skill exists
* build tickets include an ordered recommended skill chain
* build tickets include required skills for the assigned agent
* build tickets include skill usage instructions for the assigned agent
* build tickets include skill suitability scores and selection rationale
* build tickets include acceptance criteria and validation steps
* frontend build tickets reference applicable UI blueprint IDs or explicitly record why no UI blueprint applies
* frontend build tickets preserve Stage 4 UI architecture template context, page archetype, layout pattern decisions, component-family decisions, template deviations, and responsive transformations when applicable
* frontend build tickets reference applicable visual spec IDs or explicitly record why no visual spec applies
* frontend build tickets reference selected visual style references or explicitly record why no visual reference applies
* frontend build tickets reference applicable design system IDs or explicitly record why no design system applies
* frontend build tickets preserve page, component, route, action, state, validation, accessibility, responsive, visual, and design system requirements from Stage 4
* frontend build tickets preserve layout pattern requirements, including selected pattern, decision factors, rationale, rejected alternatives, source refs, and responsive transformation
* frontend build tickets reference applicable interaction contracts and stable `UI-ELEMENT-`, `ROUTE-`, and `ACTION-` IDs
* frontend build tickets preserve route types, action outcomes, confirmation, permission-denied, recovery, design-system component, mobile, and accessibility behavior where applicable
* frontend build tickets map visual acceptance criteria to validation steps
* build tickets include validation layers, `expected_artifacts`, and retry policy
* launch-critical workflow tickets include outcome-based `completion_definition`
* launch-critical workflow tickets include smoke tests with expected user outcomes
* UI/browser-validated tickets include dev server requirements
* agent assignment plan scans available agents before assignment
* agent assignment plan assigns every MVP ticket to the most suitable available agent that can use the ticket-required skills, or records why it requires manual ownership
* agent assignment plan records suitability scores and assignment reasons
* generated agents are written under `.opencode/agents/`
* generated agents include valid subagent frontmatter and prompt body based on ticket-required skills
* generated agent prompt bodies include assigned tickets, required skills, skill usage order, file scopes, handoff inputs, validation requirements, rules, and reporting requirements
* generated agents include the Stage 6 report contract
* generated agent permissions match the assigned role and risk level
* parallel execution plan separates safe parallel work from serial work
* parallel execution plan blocks unresolved dependency, file ownership, API, schema, architecture, or UX conflicts
* parallel execution plan defines file locks, merge owner, and failure policy
* Stage 6 handoff includes execution queue, validation commands, dev server plan, environment requirements, file scope controls, retry policy, `expected_artifacts`, launch-critical workflow IDs, workflow smoke tests, and workflow evidence obligations
* Stage 6 handoff includes the approved Stage 3 `selected_stack`
* Stage 6 handoff includes the Stage 4 complete app blueprint markdown path
* Stage 6 handoff includes Stage 4 `UI-COMPONENTS.md` when generated and referenced by frontend tickets
* Stage 5 local human-readable assessment summary exists, matches canonical JSON outputs, identifies whether the stage is ready, needs revision, or is blocked, and does not become a Stage 6 input
* release plan exists
* high and critical execution risks have mitigation paths
* critical interactive guidance questions are answered or converted into recorded assumptions
* no execution-blocking Stage 3 or Stage 4 unknowns remain unresolved

---

# Validation Checklist

Before completing Stage 5, confirm:

* Stage 5 did not redefine product strategy
* Stage 5 did not redesign architecture or UX
* Stage 5 did not implement code
* every MVP feature appears in the roadmap or deferred work
* every launch-critical workflow has an implementation sequence
* every major engineering dependency is mapped
* approved Stage 3 `selected_stack` is present and unchanged
* testing strategy includes validation checkpoints
* build tickets exist for every MVP implementation slice
* build tickets include primary skill, recommended skill chain, agent-required skills, skill usage instructions, acceptance criteria, and validation steps
* frontend build tickets include UI blueprint, interaction contract, visual spec, `visual_reference_refs`, design system, component, route, state, action, interactive element, visual requirement, and frontend task hint references
* frontend build tickets include UI architecture refs, page archetype, layout pattern refs, component family refs, template deviation refs, layout requirements, and component-family requirements when applicable
* frontend build tickets reference `09-complete-app-blueprint.md` when page structure, component structure, route structure, or state structure matters
* frontend build tickets reference `UI-COMPONENTS.md` when structural UI architecture template, extension, page archetype, layout pattern, component-family, or template-deviation context matters
* agent assignment plan gives each agent clear ownership and handoff inputs
* agent assignment plan records available-agent scan results, suitability scores, and unassigned ticket reasons
* generated agents have valid markdown definitions in `.opencode/agents/`, safe permission settings, and complete prompt bodies
* parallel execution plan defines batches, merge strategy, and validation gates
* release plan includes readiness gates
* critical interactive guidance questions are answered or converted into recorded assumptions
* Stage 6 handoff is usable for implementation and validation

---

# A-Grade Workflow Compliance

Stage 5 must consume `stage_contract_profile` and `guidance_policy`.

Stage 5 must consume the approved Stage 3 `selected_stack`.

If the selected stack is missing or ambiguous, Stage 5 must not create build tickets. It must write a revision loop targeting Stage 3 and stop with:

```text
completion_status.status = blocked
completion_status.reason = "missing_or_unresolved_selected_stack"
```

Stage 5 output validation should reference:

```text
System-References/Schemas/stage-5-output.schema.json
```

Build tickets must define `expected_artifacts` when validation, preview, visual QA, deployment proof, or launch readiness evidence will be required later.

Build tickets that represent launch-critical user workflows must define:

```json
{
  "completion_definition": {
    "contract_only_allowed": false,
    "requires_ui_wiring": true,
    "requires_runtime_persistence": true,
    "requires_worker_or_service_execution": false,
    "requires_end_to_end_smoke": true,
    "done_means_user_can_complete_workflow": true
  },
  "workflow_smoke_tests": []
}
```

The smoke tests must identify the expected user outcome and required evidence
chain:

```text
UI action -> route/API/action -> database/queue/storage -> worker/service -> result visible in UI -> evidence
```

Expected artifacts must be carried into:

```text
Build-Plans/Build-status/Artifact-evidence-registry.json
```

Stage 5 readiness must also record:

```json
{
  "schema_validation": {},
  "reference_integrity": {},
  "risk_acceptance_ledger": {},
  "revision_loops": []
}
```

Stage 5 may not use `ready_for_stage_6` until required schema validation passes, slice, ticket, skill, agent, UI blueprint, visual spec, design system, route, component, validation, and artifact references resolve to upstream sources, accepted high and critical execution risks are written to `Build-Plans/Build-status/Risk-acceptance-ledger.json`, and failed readiness checks are converted into revision-loop actions.
