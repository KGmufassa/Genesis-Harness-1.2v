---
name: agent-assignment-planning
description: Assign Stage 5 tickets to capable agents with validated file scopes.
compatibility: opencode
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
ui_blueprint_refs
ui_architecture_refs
page_archetype
layout_pattern_refs
component_family_refs
template_deviation_refs
ui_components_markdown_refs
visual_spec_refs
visual_reference_refs
design_system_refs
page_refs
component_refs
route_refs
state_refs
action_refs
frontend_task_hint
visual_requirements
responsive_requirements
layout_requirements
component_family_requirements
preview_required
visual_qa_required
design_system_compliance_required
```

Its job is to find, assign, or generate an agent capable of using those required skills.

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
  "ui_blueprint_inputs": {},
  "visual_reference_inputs": {},
  "design_system_inputs": {},
  "frontend_build_package": {},
  "existing_state": {}
}
```

Read and update shared development state from:

```text
Build-Plans/Build-status/Development-state.json
```

Scan available agents from:

```text
.opencode/agents/
System-References/agent-registry/agent-registry.json
System-References/agents/available-agents.json
Build-Plans/Stage-5/available-agents.json
```

Generated agents must be written to:

```text
.opencode/agents/[agent-id].md
```

Create `.opencode/agents/` if it does not exist.

---

# Core Responsibilities

## Available Agent Scan

Scan available agents before assigning work.

Extract:

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

If no formal agent registry exists, infer provisional agent profiles from:

* ticket `agent_required_skills`
* ticket `agent_skill_instructions`
* Stage 5 ticket types
* implementation domains
* validation requirements

Record inferred provisional agents in:

```text
interactive_guidance.assumptions_made
```

## Agent Assignment

Assign build tickets using:

* available agent profiles
* implementation slices
* ticket dependencies
* ticket `agent_required_skills`
* ticket `agent_skill_instructions`
* ticket `skill_match`
* ticket UI blueprint references
* ticket visual spec references and visual requirements
* ticket `visual_reference_refs`
* ticket design system references
* frontend build package hints
* architecture domains
* UX domains
* validation requirements
* risk levels

Before writing assignment data, compare every assigned ticket's `file_scopes`
or `allowed_file_scopes` with the assigned agent's `allowed_file_scopes`.
Every ticket target must be equal to, below, or matched by at least one allowed
scope. Run `validate_agent_scopes` from the Stage 5 contract helper and fail
generation if any assigned ticket falls outside the agent scope.

## Suitability Matching

For each ticket, score available agents against:

* ticket `agent_required_skills`
* ticket `agent_skill_instructions`
* required skill coverage
* ticket type
* implementation domain
* architecture references
* UX references
* UI blueprint references
* visual spec references and visual requirements
* `visual_reference_refs`
* design system references and compliance requirements
* page, component, route, state, and action references
* interaction contract and interactive element references
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

If no suitable agent exists, mark the ticket as:

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
  "ui_blueprint_refs": [],
  "ui_architecture_refs": [],
  "page_archetype": "",
  "layout_pattern_refs": [],
  "component_family_refs": [],
  "template_deviation_refs": [],
  "ui_components_markdown_refs": [],
  "interaction_contract_refs": [],
  "interactive_element_refs": [],
  "visual_spec_refs": [],
  "visual_reference_refs": [],
  "design_system_refs": [],
  "visual_requirements": {},
  "responsive_requirements": {},
  "layout_requirements": {},
  "component_family_requirements": [],
  "preview_required": false,
  "visual_qa_required": false,
  "design_system_compliance_required": false,
  "frontend_build_package_refs": [],
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

When a suitable existing agent does not exist, generate a subagent definition from the ticket-required skills and skill usage instructions.

Generated agents must use this frontmatter:

```yaml
description: ""
mode: subagent
temperature: 0.1
permission:
  edit: deny
  bash: deny
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

## Generated Agent Prompt Template

Generated agent files must include a prompt body after the frontmatter.

Generate the prompt body from:

* agent type
* assigned tickets
* assigned slices
* ticket `agent_required_skills`
* ticket `agent_skill_instructions`
* allowed file scopes
* restricted file scopes
* handoff inputs
* UI blueprint references when assigned frontend tickets
* page interaction contract and stable interactive element, route, and action references when assigned frontend tickets
* visual spec references and visual requirements when assigned frontend tickets
* `visual_reference_refs` when assigned frontend tickets
* design system references when assigned frontend tickets
* frontend build package references when assigned frontend tickets
* validation requirements
* workflow completion definition and smoke tests when assigned launch-critical workflow tickets
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
- Resolve Stage 5 format through `.opencode/Skills/stage-5-development-orchestration/scripts/resolve_stage5.py`.
- For v2, load shared context from `00-stage-context.json` and completion/handoff from `09-stage-manifest.json`.
- Read tickets from `05-build-tickets.json#/data/tickets`, agents from `06-agent-assignment-plan.json#/data/agents`, batches from `07-parallel-execution-plan.json#/data/batches`, and other payloads from `/data`.
- [handoff file]
- [UI blueprint file when assigned frontend tickets]
- [interaction contract and complete app blueprint when assigned frontend tickets]
- [visual style reference file when assigned frontend tickets]
- [design system file when assigned frontend tickets]

Preserve these visual requirements when assigned frontend tickets:
- [visual style, density, color direction, typography feel, component style, primary visual focus, visual do and don't rules, visual acceptance criteria, user approval status]

Preserve these design system requirements when assigned frontend tickets:
- [design tokens, component rules, responsive breakpoints, accessibility constraints]

Preserve these interaction requirements when assigned frontend tickets:
- [UI-ELEMENT, ROUTE, and ACTION IDs, labels, route types, outcomes, confirmations, permission-denied behavior, recovery behavior, mobile behavior, and accessibility behavior]

Preview and visual QA:
- [whether local preview is required]
- [whether visual QA is required]
- [whether design system compliance must be reported]

Validation requirements:
- [validation requirement]
- For launch-critical workflow tickets, prove the declared user outcome through the full runtime chain.
- Record workflow evidence separately from build success.
- Verify visible controls are wired or explicitly disabled with a reason.
- Verify runtime pages use live data sources instead of preview fixtures before ready status.

Rules:
- Do not modify files outside your allowed scope.
- Do not invent behavior that conflicts with earlier-stage outputs.
- Do not change shared contracts unless the ticket explicitly allows it.
- If a dependency is missing, mark the ticket blocked and record the dependency.
- If validation fails, use the assigned debugging skill before applying fixes.
- If any numbered Stage 5 artifact declares v2, stop when context or manifest is missing.
- Follow `execution_waves`; do not start a dependent ticket before its prerequisite.
- Do not report a user-facing workflow complete when only contracts, APIs, static UI, or fixture data exist.
- Record every skill used and why.

When finished, report:
- completed tickets
- files changed
- skills used
- validation results
- workflow evidence and any dead-control or fixture-runtime findings
- blockers
- handoff notes
```

Review-only agents must include:

```text
Provide constructive feedback without making direct changes.
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
  "ui_blueprint_handoff_packages": [],
  "interaction_contract_handoff_packages": [],
  "interactive_element_handoff_packages": [],
  "visual_spec_handoff_packages": [],
  "visual_reference_handoff_packages": [],
  "design_system_handoff_packages": [],
  "assignment_risks": []
}
```

---

# Shared State Updates

Update:

```text
agent_assignment_plan
build_tickets
engineering_dependencies
execution_risks
coordination_notes
stage_6_handoff
interactive_guidance
```

Persist updates to:

```text
Build-Plans/Build-status/Development-state.json
```

---

# Validation Responsibilities

Validate:

* every MVP ticket is assigned to a suitable available agent or recorded for manual ownership
* assigned agents can use ticket-required skills
* frontend agents receive `Build-Plans/Stage-4/07-ui-blueprint-specification.json` when assigned frontend tickets with UI blueprint references
* frontend agents receive Stage 4 UI architecture template, page archetype, layout pattern, component-family, template-deviation, and `UI-COMPONENTS.md` references when assigned tickets include them
* frontend agents receive visual spec references and visual requirements when assigned frontend tickets with visual spec references
* frontend agents receive selected visual style reference files when assigned frontend tickets with `visual_reference_refs`
* frontend agents receive `Build-Plans/Stage-4/08-design-system-foundation.json` when assigned frontend tickets with design system references
* agent handoff packages preserve ticket UI blueprint, visual spec, visual style reference, design system, page, component, route, state, action, interactive element (element_type, label, route_target, behavior), visual requirements, responsive requirements, preview requirements, visual QA requirements, and frontend task hint references
* agent handoff packages preserve layout requirements, selected layout pattern, layout decision rationale, responsive transformations, component-family requirements, and template deviations from Stage 4
* agent handoff packages preserve stable `UI-ELEMENT-`, `ROUTE-`, and `ACTION-` IDs, interaction contract status, route types, action outcomes, confirmation, permission-denied, recovery, design-system component, mobile, and accessibility behavior
* generated agents are written under `.opencode/agents/`
* generated agents include valid frontmatter and complete prompt bodies
* generated agent permissions match assigned role and risk level
* file scopes are explicit
* every assigned ticket's required file scopes are covered by its agent's allowed scopes
* high-risk tickets include validation ownership
