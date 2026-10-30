# Stage 3 — System Architecture Command & Skill Draft

# Core Philosophy

Stage 3 is centered around:

```text
technical systems cognition
```

NOT:

* product discovery
* market validation
* UX interaction design
* implementation scheduling

Those responsibilities belong to other stages.

Stage 3 is responsible for transforming validated product intelligence into a coherent technical architecture model.

The stage focuses on:

* system topology
* service boundaries
* data architecture
* API architecture
* integration architecture
* infrastructure model
* security foundations
* scalability framework

---

# Stage 3 Core Purpose

Transform:

* Stage 1 product structures
* Stage 2 validation intelligence
* architecture readiness findings
* validated assumptions
* known risks and constraints

into:

* technical system topology
* service architecture
* data architecture
* API architecture
* integration model
* security foundations
* infrastructure model
* scalability framework

---

# Recommended Stage 3 Architecture

```text
stage-3-system-architecture (command)
│
├── system-topology-design
├── service-boundary-architecture
├── data-and-api-architecture
├── integration-and-infrastructure-architecture
├── security-and-scalability-architecture
└── architecture-synthesis
```

---

# Stage 3 Command

# Command — stage-3-system-architecture

# Purpose

The `stage-3-system-architecture` command orchestrates Stage 3.

It transforms validated product and research intelligence into a technical architecture package that is ready for Stage 4 UX architecture and Stage 5 development orchestration.

This is the Stage 3 command skill. It is not a single architecture subskill.

---

# Cognitive Boundary

Stage 3 asks:

```text
How should the validated product be technically structured?
```

Stage 3 must not:

* redefine the product concept
* perform market validation
* design detailed user interfaces
* write implementation tickets
* produce production deployment scripts

Stage 3 may recommend product or validation revisions only when architecture analysis exposes a blocking contradiction.

---

# Output Directory

All final Stage 3 outputs must be recorded in:

```text
Build-Plans/Stage-3/
```

The command must create this folder if it does not exist.

---

# Shared Architecture State

The command maintains a shared Stage 3 architecture state object.

The shared architecture state must be written to:

```text
Build-Plans/Build-status/Architecture-state.json
```

The command must load this file at the beginning of Stage 3, update it after each architecture skill runs, and preserve it as the durable architecture state for the build.

```json
{
  "stage": "Stage 3",
  "command": "stage-3-system-architecture",
  "status": "not_started",
  "stage_1_inputs": {},
  "stage_2_inputs": {},
  "preflight": {},
  "architecture_drivers": [],
  "architecture_decisions": [],
  "system_topology": {},
  "service_architecture": {},
  "data_architecture": {},
  "api_architecture": {},
  "integration_architecture": {},
  "security_foundations": {},
  "infrastructure_model": {},
  "scalability_framework": {},
  "architecture_risks": [],
  "tradeoffs": [],
  "open_questions": [],
  "interactive_guidance": {
    "open_questions": [],
    "answered_questions": [],
    "assumptions_made": [],
    "blocked_decisions": [],
    "user_confirmations": [],
    "architecture_confidence_gaps": []
  },
  "stage_4_handoff": {},
  "stage_5_handoff": {},
  "completion_status": {}
}
```

Each subskill reads the current architecture state and writes its updates back into the shared state before the next skill runs.

After each subskill completes, the command must persist the updated shared state to:

```text
Build-Plans/Build-status/Architecture-state.json
```

---

# Interactive Guidance Rules

The Stage 3 command should behave like a guided architecture decision interview.

Use this decision rule:

```text
Ask only for architecture decisions that materially affect system design.
Infer standard technical defaults when risk is low and the product model supports the inference.
Record assumptions when proceeding without user confirmation.
Block only when a missing decision prevents coherent architecture.
```

When asking the user questions:

* ask 1-3 questions at a time
* prioritize architecture-blocking decisions first
* avoid asking questions already answered by Stage 1 or Stage 2 outputs
* explain the architectural consequence of each question
* prefer concrete options over open-ended questions when the tradeoff is known
* update `interactive_guidance.open_questions`
* move answered questions into `interactive_guidance.answered_questions`
* record inferred defaults in `interactive_guidance.assumptions_made`
* record unresolved blockers in `interactive_guidance.blocked_decisions`

The command should continue automatically when a decision has a low-risk default.

The command should pause for user input when:

* data ownership is unclear
* user roles or permissions materially affect service boundaries
* an external integration is required but unspecified
* AI processing requires a major architecture choice
* synchronous vs asynchronous workflow behavior changes the topology
* sensitive data handling is unclear
* scalability expectations materially affect infrastructure choices
* a Stage 2 risk cannot be mitigated through architecture

The command should not ask the user to choose implementation details that can be deferred to Stage 5 unless the decision changes Stage 3 architecture.

---

# Stage 3 Input Contract

Load Stage 1 outputs from:

```text
Build-Plans/Stage-1/
```

Load Stage 2 outputs from:

```text
Build-Plans/Stage-2/
```

Required Stage 1 files:

```text
01-product-foundation.json
02-user-system-map.json
03-workflow-architecture.json
04-product-capabilities.json
05-feature-structure.json
06-product-boundaries.json
07-dependency-map.json
08-mvp-operational-model.json
09-risk-and-constraints.json
10-success-framework.json
```

Required Stage 2 files:

```text
01-market-analysis.json
02-competitive-landscape.json
03-technical-feasibility.json
04-business-viability.json
05-risk-validation.json
06-strategic-positioning.json
```

Minimum viable input set:

```text
Stage 1:
01-product-foundation.json
03-workflow-architecture.json
04-product-capabilities.json
05-feature-structure.json
07-dependency-map.json
08-mvp-operational-model.json
09-risk-and-constraints.json

Stage 2:
03-technical-feasibility.json
05-risk-validation.json
06-strategic-positioning.json
```

If the minimum viable input set is missing, stop and set:

```text
completion_status.status = "blocked"
completion_status.reason = "missing_architecture_inputs"
```

If Stage 2 completion status is not `ready_for_stage_3`, continue only if the unresolved issues are not architecture-blocking. Record all carry-forward risks in `architecture_risks`.

---

# Preflight Validation

Before architecture design, validate:

* Stage 1 outputs exist and are readable
* Stage 2 outputs exist and are readable
* architecture readiness status is acceptable
* critical unknowns from Stage 2 are resolved or mitigated
* validated assumptions are available
* high and critical risks have mitigation paths
* MVP scope is clear enough to architecture

Record preflight results in:

```text
preflight
architecture_risks
open_questions
interactive_guidance
completion_status
```

---

# Stage 4 And Stage 5 Handoff Contracts

Stage 3 must produce concrete handoffs for both UX architecture and development orchestration.

The `stage_4_handoff` object must include:

```json
{
  "stage_3_output_directory": "Build-Plans/Stage-3/",
  "selected_stack": {
    "frontend": {},
    "backend": {},
    "hosting_and_deployment": {},
    "testing_stack": {},
    "package_manager": "",
    "stage_4_implications": []
  },
  "system_topology_refs": [],
  "service_refs": [],
  "data_entity_refs": [],
  "api_surface_refs": [],
  "integration_refs": [],
  "security_constraints": [],
  "role_permission_model": {},
  "workflow_architecture_constraints": [],
  "ux_relevant_latency_or_async_constraints": [],
  "interaction_blockers": [],
  "completion_status": {}
}
```

The `stage_5_handoff` object must include:

```json
{
  "stage_3_output_directory": "Build-Plans/Stage-3/",
  "architecture_decision_records": [],
  "selected_stack": {
    "frontend": {},
    "backend": {},
    "database": {},
    "storage": {},
    "authentication": {},
    "hosting_and_deployment": {},
    "testing_stack": {},
    "package_manager": "",
    "ai_and_external_services": [],
    "rationale": "",
    "rejected_alternatives": [],
    "risks": []
  },
  "service_implementation_units": [],
  "data_implementation_units": [],
  "api_implementation_units": [],
  "integration_implementation_units": [],
  "infrastructure_requirements": [],
  "security_requirements": [],
  "scalability_requirements": [],
  "implementation_constraints": [],
  "architecture_risks": [],
  "completion_status": {}
}
```

---

# Architecture Decision Record Contract

Every major architecture decision must use this structure:

```json
{
  "decision_id": "",
  "title": "",
  "context": "",
  "decision": "",
  "alternatives_considered": [],
  "rationale": "",
  "affected_services": [],
  "affected_data_entities": [],
  "affected_api_surfaces": [],
  "affected_workflows": [],
  "assumption_ids": [],
  "risks": [],
  "stage_4_implications": [],
  "stage_5_implications": []
}
```

---

# Concrete Stack Decision Contract

Stage 3 must select one concrete implementation stack before it can complete.

Stage 3 may compare alternatives, but it may not leave unresolved stack choices for Stage 5, implementation agents, or frontend/backend builders to decide later.

The selected stack must include:

```json
{
  "stack_decision_id": "",
  "frontend": {
    "framework": "",
    "language": "",
    "styling": "",
    "ui_library": "",
    "state_management": "",
    "routing": ""
  },
  "backend": {
    "framework": "",
    "language": "",
    "runtime": "",
    "api_style": ""
  },
  "database": {
    "primary_database": "",
    "orm_or_query_layer": "",
    "migration_tool": ""
  },
  "storage": {
    "provider": "",
    "usage": []
  },
  "authentication": {
    "provider": "",
    "session_strategy": "",
    "authorization_model": ""
  },
  "hosting_and_deployment": {
    "frontend_host": "",
    "backend_host": "",
    "database_host": "",
    "deployment_flow": ""
  },
  "testing_stack": {
    "unit": "",
    "integration": "",
    "e2e": "",
    "visual": ""
  },
  "package_manager": "",
  "ai_and_external_services": [],
  "rationale": "",
  "rejected_alternatives": [],
  "risks": [],
  "stage_4_implications": [],
  "stage_5_implications": []
}
```

Selection rules:

* choose one best-fit stack based on Stage 2 feasibility, product complexity, skill availability, implementation speed, scalability, security, cost, and operational burden
* record rejected alternatives with rationale
* use `none_for_mvp` for stack areas that are intentionally unnecessary instead of leaving them blank
* do not use unresolved phrases such as `or`, `TBD`, `to decide later`, `optional`, or `depends` in the selected stack
* if the user rejects the stack in the Stage 3 decision brief, revise the selected stack and regenerate affected architecture outputs before completing Stage 3

---

# Architecture Contract Formats

Service entries must include:

```json
{
  "service_id": "",
  "name": "",
  "purpose": "",
  "responsibilities": [],
  "owned_data_entities": [],
  "upstream_dependencies": [],
  "downstream_dependencies": [],
  "api_surfaces": [],
  "failure_modes": [],
  "implementation_constraints": []
}
```

Data entity entries must include:

```json
{
  "entity_id": "",
  "name": "",
  "owner_service_id": "",
  "description": "",
  "relationships": [],
  "sensitive_fields": [],
  "lifecycle_rules": [],
  "audit_requirements": [],
  "schema_risks": []
}
```

API surface entries must include:

```json
{
  "api_id": "",
  "name": "",
  "consumer": "",
  "provider_service_id": "",
  "operations": [],
  "auth_required": true,
  "permission_requirements": [],
  "request_response_concepts": [],
  "error_concepts": [],
  "stage_4_behavior_dependencies": []
}
```

Role and permission entries must include:

```json
{
  "role_id": "",
  "role_name": "",
  "permissions": [],
  "restricted_actions": [],
  "affected_workflows": [],
  "affected_screens": []
}
```

---

# Orchestrated Skills

Run Stage 3 skills in this order:

```text
1. system-topology-design
2. service-boundary-architecture
3. data-and-api-architecture
4. integration-and-infrastructure-architecture
5. security-and-scalability-architecture
6. architecture-synthesis
```

---

# Skill — system-topology-design

# Purpose

The `system-topology-design` skill defines the high-level technical system shape.

It determines:

* primary systems
* subsystems
* runtime boundaries
* user-facing vs backend systems
* internal operational systems
* AI or automation systems
* external system touchpoints

---

# Core Responsibilities

## Topology Design

Identify:

* frontend applications
* backend services
* databases
* queues
* workers
* AI services
* storage systems
* notification systems
* admin or operational tooling
* external integrations

## Architecture Drivers

Extract architecture drivers from:

* validated assumptions
* workflows
* capabilities
* MVP scope
* dependency map
* risk validation
* scalability needs

## Boundary Mapping

Define:

* system boundaries
* data flow boundaries
* trust boundaries
* ownership boundaries
* external dependency boundaries

---

# Interactive Guidance Responsibilities

This skill should guide the user only when the high-level system shape cannot be inferred safely.

Ask targeted questions when any of these are unclear:

* whether the product needs one app or multiple apps
* whether admin or operator tooling is required
* whether AI processing is synchronous or asynchronous
* whether collaboration requires real-time architecture
* which external systems are mandatory for MVP
* whether user-facing and internal systems need separate boundaries

Infer standard topology defaults when the product category and MVP scope make them obvious, but record the assumption in:

```text
interactive_guidance.assumptions_made
```

Pause for user input when the topology choice changes service boundaries, infrastructure, or Stage 4 handoff.

---

# Inputs

```json
{
  "stage_1_inputs": {},
  "stage_2_inputs": {},
  "existing_state": {}
}
```

---

# Outputs

```json
{
  "system_topology": {},
  "architecture_drivers": [],
  "system_boundaries": [],
  "topology_risks": [],
  "open_questions": []
}
```

---

# Shared State Updates

```text
system_topology
architecture_drivers
architecture_risks
open_questions
```

---

# Skill — service-boundary-architecture

# Purpose

The `service-boundary-architecture` skill converts system topology into service-level architecture.

It determines:

* service boundaries
* service responsibilities
* ownership domains
* communication patterns
* synchronous vs asynchronous interactions
* shared service risks

---

# Core Responsibilities

## Service Modeling

Define:

* service names
* service purpose
* responsibilities
* owned data
* upstream dependencies
* downstream dependencies
* failure modes

## Boundary Validation

Validate:

* services map to product capabilities
* service boundaries are not over-fragmented
* shared dependencies are explicit
* MVP architecture remains implementable
* future scaling needs are not blocked

## Communication Patterns

Determine:

* request-response flows
* event-driven flows
* queue usage
* background jobs
* retry and failure handling needs

---

# Interactive Guidance Responsibilities

This skill should guide the user through service boundary tradeoffs without forcing premature implementation detail.

Ask targeted questions when any of these are unclear:

* whether a capability should be isolated or kept inside a shared service
* whether a workflow requires synchronous or asynchronous processing
* whether user roles require separate permission boundaries
* whether AI, billing, notifications, or integrations require dedicated service ownership
* whether MVP simplicity should override future service separation

Infer simpler MVP-oriented boundaries when risk is low, but record the assumption in:

```text
interactive_guidance.assumptions_made
```

Pause for user input when a service boundary affects security, data ownership, scaling, or operational responsibility.

---

# Inputs

```json
{
  "system_topology": {},
  "capabilities": {},
  "dependencies": {},
  "mvp_scope": {},
  "existing_state": {}
}
```

---

# Outputs

```json
{
  "service_architecture": {},
  "service_boundaries": [],
  "communication_patterns": [],
  "service_risks": [],
  "tradeoffs": []
}
```

---

# Shared State Updates

```text
service_architecture
architecture_decisions
architecture_risks
tradeoffs
```

---

# Skill — data-and-api-architecture

# Purpose

The `data-and-api-architecture` skill designs the data model and API architecture.

It determines:

* core entities
* data ownership
* persistence needs
* read/write patterns
* API surfaces
* API contracts
* data lifecycle

---

# Core Responsibilities

## Data Architecture

Define:

* domain entities
* entity relationships
* data ownership by service
* persistence model
* data lifecycle
* audit and history needs
* privacy-sensitive data

## API Architecture

Define:

* API boundaries
* primary endpoints or operations
* request/response concepts
* authentication and authorization requirements
* external API exposure
* internal API usage

## Data Risk Detection

Identify:

* unclear data ownership
* excessive coupling
* sensitive data exposure
* missing auditability
* reporting or analytics data needs
* schema evolution risks

---

# Interactive Guidance Responsibilities

This skill should guide the user through data ownership, sensitive data, and API exposure decisions.

Ask targeted questions when any of these are unclear:

* which entities are core business objects
* who owns or can modify critical data
* whether sensitive or regulated data is present
* whether audit history is required
* whether APIs are internal only or externally exposed
* whether users need exports, imports, or reporting access
* whether data must support real-time collaboration

Infer standard CRUD-style data and API structures only when the workflow is simple and low-risk.

Record assumptions in:

```text
interactive_guidance.assumptions_made
```

Pause for user input when data ownership, privacy, auditability, or external API exposure is unclear.

---

# Inputs

```json
{
  "system_topology": {},
  "service_architecture": {},
  "workflows": {},
  "feature_structure": {},
  "security_requirements": {},
  "existing_state": {}
}
```

---

# Outputs

```json
{
  "data_architecture": {},
  "api_architecture": {},
  "data_entities": [],
  "api_surfaces": [],
  "data_risks": [],
  "open_questions": []
}
```

---

# Shared State Updates

```text
data_architecture
api_architecture
architecture_decisions
architecture_risks
open_questions
```

---

# Skill — integration-and-infrastructure-architecture

# Purpose

The `integration-and-infrastructure-architecture` skill designs the external integration model and infrastructure foundation.

It determines:

* integration points
* external service dependencies
* hosting model
* runtime infrastructure
* storage infrastructure
* queue and worker infrastructure
* observability foundations

---

# Core Responsibilities

## Integration Architecture

Define:

* external APIs
* third-party services
* integration ownership
* authentication method per integration
* failure handling
* rate-limit considerations
* fallback behavior

## Infrastructure Model

Define:

* hosting approach
* compute model
* database model
* object storage needs
* queueing needs
* background worker needs
* environment strategy
* observability requirements

## Infrastructure Risk Detection

Identify:

* fragile external dependencies
* unclear deployment assumptions
* cost-sensitive infrastructure choices
* scaling bottlenecks
* operational blind spots

---

# Interactive Guidance Responsibilities

This skill should guide the user through integration and infrastructure decisions that affect feasibility, cost, or reliability.

Ask targeted questions when any of these are unclear:

* required third-party integrations
* payment, email, notification, storage, analytics, or AI providers
* whether integrations are MVP-critical or deferrable
* expected file, media, or data volume
* whether background jobs or queues are required
* whether the system needs staging, production, or multi-environment support
* whether observability is required at launch

Infer standard infrastructure defaults when they are low-risk and aligned with MVP scope.

Record assumptions in:

```text
interactive_guidance.assumptions_made
```

Pause for user input when a provider, integration, or infrastructure choice changes architecture risk or cost.

---

# Inputs

```json
{
  "service_architecture": {},
  "data_architecture": {},
  "api_architecture": {},
  "dependency_map": {},
  "technical_feasibility": {},
  "existing_state": {}
}
```

---

# Outputs

```json
{
  "integration_architecture": {},
  "infrastructure_model": {},
  "integration_risks": [],
  "infrastructure_risks": [],
  "observability_requirements": []
}
```

---

# Shared State Updates

```text
integration_architecture
infrastructure_model
architecture_decisions
architecture_risks
tradeoffs
```

---

# Skill — security-and-scalability-architecture

# Purpose

The `security-and-scalability-architecture` skill defines security foundations and scalability strategy.

It determines:

* authentication foundations
* authorization model
* data protection needs
* trust boundaries
* compliance-sensitive controls
* scalability bottlenecks
* performance strategy
* resilience strategy

---

# Core Responsibilities

## Security Foundations

Define:

* authentication model
* authorization model
* roles and permissions
* sensitive data handling
* audit logging needs
* trust boundaries
* abuse and moderation controls
* compliance considerations

## Scalability Framework

Define:

* expected load assumptions
* scaling bottlenecks
* performance-sensitive workflows
* caching needs
* async processing needs
* AI or compute cost scaling
* resilience and failure handling

## Security and Scalability Risks

Identify:

* missing access controls
* unclear privacy requirements
* expensive scaling paths
* single points of failure
* data exposure risks
* unbounded AI usage

---

# Interactive Guidance Responsibilities

This skill should guide the user through security and scale decisions that materially affect architecture.

Ask targeted questions when any of these are unclear:

* authentication requirements
* user roles and permissions
* sensitive data handling
* audit logging needs
* abuse, moderation, or rate-limit needs
* expected user or request volume
* AI usage limits
* performance-sensitive workflows
* resilience expectations

Infer standard security foundations only when the product has simple user roles and no sensitive data exposure.

Record assumptions in:

```text
interactive_guidance.assumptions_made
```

Pause for user input when access control, privacy, compliance, scale, or abuse prevention is unclear.

---

# Inputs

```json
{
  "system_topology": {},
  "service_architecture": {},
  "data_architecture": {},
  "api_architecture": {},
  "infrastructure_model": {},
  "risk_validation": {},
  "existing_state": {}
}
```

---

# Outputs

```json
{
  "security_foundations": {},
  "scalability_framework": {},
  "security_risks": [],
  "scalability_risks": [],
  "architecture_warnings": []
}
```

---

# Shared State Updates

```text
security_foundations
scalability_framework
architecture_risks
architecture_decisions
tradeoffs
```

---

# Skill — architecture-synthesis

# Purpose

The `architecture-synthesis` skill combines all Stage 3 architecture intelligence into final architecture outputs.

It produces:

* coherent system topology
* service architecture
* data architecture
* API architecture
* integration architecture
* security foundations
* infrastructure model
* scalability framework
* handoff guidance for Stage 4 and Stage 5

---

# Core Responsibilities

## Architecture Coherence

Validate:

* service boundaries align with capabilities
* data ownership is clear
* APIs support workflows
* integrations are mapped to dependencies
* infrastructure supports technical feasibility findings
* security controls map to risk validation
* scalability framework supports MVP and future growth

## Tradeoff Documentation

Record:

* major architecture decisions
* alternatives considered
* accepted risks
* deferred architecture concerns
* Stage 4 handoff implications
* Stage 5 execution implications

## Completion Determination

Determine whether Stage 3 is:

```text
ready_for_stage_4
needs_architecture_revision
needs_stage_2_revalidation
blocked
```

---

# Interactive Guidance Responsibilities

This skill should not finalize Stage 3 if architecture-blocking questions remain unresolved.

Before writing final outputs, inspect:

```text
interactive_guidance.open_questions
interactive_guidance.blocked_decisions
interactive_guidance.architecture_confidence_gaps
architecture_risks
open_questions
tradeoffs
```

Classify unresolved guidance items as:

```text
safe_to_assume
needs_user_confirmation
blocks_stage_3_completion
```

Ask the minimum number of final questions needed to complete Stage 3.

Do not ask broad technical preference questions at this stage. Only ask questions tied directly to:

* missing final architecture output fields
* unresolved service boundary decisions
* unresolved data ownership decisions
* unresolved security decisions
* unresolved infrastructure or integration decisions
* architecture risks that block Stage 4 or Stage 5 handoff

If proceeding with assumptions, record them in:

```text
interactive_guidance.assumptions_made
```

If Stage 3 cannot complete, set `completion_status` to one of:

```text
needs_architecture_revision
needs_stage_2_revalidation
blocked
```

and return the specific questions or decisions required.

---

# Inputs

```json
{
  "system_topology": {},
  "service_architecture": {},
  "data_architecture": {},
  "api_architecture": {},
  "integration_architecture": {},
  "security_foundations": {},
  "infrastructure_model": {},
  "scalability_framework": {},
  "existing_state": {}
}
```

---

# Outputs

```json
{
  "architecture_outputs": {},
  "architecture_decisions": [],
  "architecture_risks": [],
  "tradeoffs": [],
  "stage_4_handoff": {},
  "stage_5_handoff": {},
  "completion_status": {}
}
```

---

# Final Stage 3 Outputs

Write or update:

```text
Build-Plans/Stage-3/01-system-topology.json
Build-Plans/Stage-3/02-service-architecture.json
Build-Plans/Stage-3/03-data-architecture.json
Build-Plans/Stage-3/04-api-architecture.json
Build-Plans/Stage-3/05-integration-architecture.json
Build-Plans/Stage-3/06-security-foundations.json
Build-Plans/Stage-3/07-infrastructure-model.json
Build-Plans/Stage-3/08-scalability-framework.json
```

Each output must include:

* related Stage 1 source files
* related Stage 2 assumption IDs where applicable
* architecture decisions
* risks and constraints
* unresolved questions
* Stage 4 or Stage 5 handoff notes when relevant

---

# Final Output Schemas

`01-system-topology.json` must include:

```json
{
  "stage": "Stage 3",
  "status": "",
  "system_topology": {},
  "system_boundaries": [],
  "trust_boundaries": [],
  "runtime_boundaries": [],
  "architecture_drivers": [],
  "architecture_decision_ids": [],
  "risks": []
}
```

`02-service-architecture.json` must include:

```json
{
  "stage": "Stage 3",
  "status": "",
  "services": [],
  "service_boundaries": [],
  "communication_patterns": [],
  "ownership_domains": [],
  "architecture_decision_ids": [],
  "risks": []
}
```

`03-data-architecture.json` must include:

```json
{
  "stage": "Stage 3",
  "status": "",
  "data_entities": [],
  "entity_relationships": [],
  "data_ownership": [],
  "sensitive_data": [],
  "audit_requirements": [],
  "schema_evolution_risks": []
}
```

`04-api-architecture.json` must include:

```json
{
  "stage": "Stage 3",
  "status": "",
  "api_surfaces": [],
  "operations": [],
  "auth_requirements": [],
  "permission_requirements": [],
  "error_concepts": [],
  "consumer_provider_map": []
}
```

`05-integration-architecture.json` must include:

```json
{
  "stage": "Stage 3",
  "status": "",
  "integrations": [],
  "external_dependencies": [],
  "integration_auth": [],
  "fallback_behaviors": [],
  "rate_limit_considerations": [],
  "risks": []
}
```

`06-security-foundations.json` must include:

```json
{
  "stage": "Stage 3",
  "status": "",
  "authentication_model": {},
  "authorization_model": {},
  "role_permission_matrix": [],
  "trust_boundaries": [],
  "sensitive_data_controls": [],
  "audit_logging_needs": [],
  "security_risks": []
}
```

`07-infrastructure-model.json` must include:

```json
{
  "stage": "Stage 3",
  "status": "",
  "hosting_model": {},
  "compute_model": {},
  "database_model": {},
  "storage_model": {},
  "queue_or_worker_needs": [],
  "environment_strategy": [],
  "observability_requirements": [],
  "infrastructure_risks": []
}
```

`08-scalability-framework.json` must include:

```json
{
  "stage": "Stage 3",
  "status": "",
  "load_assumptions": [],
  "scaling_bottlenecks": [],
  "performance_sensitive_workflows": [],
  "caching_needs": [],
  "async_processing_needs": [],
  "resilience_strategy": [],
  "stage_4_handoff": {},
  "stage_5_handoff": {}
}
```

---

# Stage Decision Brief

Before Stage 3 may run final synthesis, use `ready_for_stage_4`, or send a Stage 5 handoff, it must generate:

```text
Build-Plans/Stage-3/00-stage-decision-brief.md
```

Purpose:

```text
Confirm the selected concrete architecture stack before UX/UI planning and build orchestration.
```

The brief must include:

* selected architecture approach
* selected frontend stack
* selected backend stack
* selected runtime
* selected database and storage
* selected authentication model
* selected hosting and deployment model
* selected testing stack
* selected package manager
* integrations
* AI, model, or provider choices if relevant
* rejected alternatives with rationale
* tradeoffs
* risks
* downstream impact on Stage 4 and Stage 5

Approval question:

```text
Do you approve this selected concrete stack for the build?
```

Approval options:

```text
Approve tech stack
Change frontend stack
Change backend stack
Change database/auth/deployment
Choose simpler architecture
Choose more scalable architecture
```

Stage 3 shared state must include:

```json
{
  "stage_decision_brief": {
    "brief_id": "",
    "stage": "Stage 3",
    "brief_path": "Build-Plans/Stage-3/00-stage-decision-brief.md",
    "recommended_direction": "",
    "alternatives_considered": [],
    "key_decisions": [],
    "assumptions": [],
    "risks": [],
    "downstream_impact": [],
    "user_decision_required": true,
    "approval_status": "pending | approved | revision_requested | blocked",
    "approved_by": "",
    "approved_at": "",
    "revision_notes": []
  }
}
```

Stage 3 may not lock architecture direction, use `ready_for_stage_4`, or send Stage 5 architecture handoff unless:

```text
selected_stack is complete
selected_stack contains no unresolved alternatives
stage_decision_brief.approval_status = approved
```

---

# Completion Gate

Before Stage 3 may use `ready_for_stage_4`, it must run `global-stage-readiness-audit` and write:

```text
Build-Plans/Build-status/Stage-3-readiness-audit.json
```

The audit must pass according to:

```text
System-References/Docs/Global-Stage-Workflow-Contract.md
```

Stage 3 may complete only when:

* all eight architecture outputs exist
* system topology is defined
* service boundaries are clear enough for implementation planning
* data ownership is defined
* API surfaces are mapped to workflows
* integrations and infrastructure are defined
* selected concrete stack is complete and approved
* security foundations are present
* scalability framework exists
* high and critical architecture risks have mitigation paths
* no architecture-blocking Stage 2 unknowns remain unresolved
* Stage 3 decision brief exists and is approved

---

# Validation Checklist

Before completing Stage 3, confirm:

* Stage 3 did not redefine product strategy
* Stage 3 did not perform UX screen design
* Stage 3 did not write implementation tickets
* every major capability maps to a system or service
* every core workflow is supported by the architecture
* every data entity has an owner
* every external dependency has an integration strategy
* selected stack has exactly one concrete choice for frontend, backend, database, auth, deployment, testing, and package manager
* rejected stack alternatives are recorded with rationale
* security and scalability risks are recorded
* critical interactive guidance questions are answered or converted into recorded assumptions
* Stage 4 handoff is usable for UX architecture
* Stage 5 handoff is usable for development orchestration
* Stage 3 decision brief approval is recorded before Stage 4 or Stage 5 handoff is used

---

# A-Grade Workflow Compliance

Stage 3 must consume `stage_contract_profile` and `guidance_policy`.

Stage 3 output validation should reference:

```text
System-References/Schemas/stage-3-output.schema.json
```

Architecture decisions should reference Stage 2 evidence quality and create artifacts when architecture proof, diagrams, or decision records are produced.

Those artifacts should be recorded or referenced in:

```text
Build-Plans/Build-status/Artifact-evidence-registry.json
```

Stage 3 readiness must also record:

```json
{
  "schema_validation": {},
  "reference_integrity": {},
  "risk_acceptance_ledger": {},
  "revision_loops": []
}
```

Stage 3 may not use `ready_for_stage_4` until required schema validation passes, architecture IDs resolve to validated assumptions and Stage 1-2 source IDs, accepted high and critical architecture risks are written to `Build-Plans/Build-status/Risk-acceptance-ledger.json`, and failed readiness checks are converted into revision-loop actions.
