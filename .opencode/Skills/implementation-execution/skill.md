---
name: implementation-execution
description: Execute assigned Stage 5 tickets through normalized or legacy-compatible Stage 6 inputs.
compatibility: opencode
---

# Skill — implementation-execution

# Purpose

The `implementation-execution` skill executes assigned Stage 5 build tickets.

It is responsible for:

* executing assigned build tickets
* running generated or assigned agents when applicable
* following ticket `agent_required_skills` and `agent_skill_instructions`
* respecting allowed and restricted file scopes
* tracking implemented slices and tickets
* mapping implementation back to Stage 5 sequence, tickets, and agents
* detecting implementation blockers

This skill is the execution layer for Stage 6.

---

# Inputs

Resolve Stage 5 input format with the read-only `resolve_stage5.py` helper. For
v2, read tickets, agents, and batches from their canonical `/data` paths, shared
context from file `00`, and completion/handoff from manifest file `09`. Reject
partial v2 handoffs and follow batch `execution_waves`.

```json
{
  "build_tickets": {},
  "agent_assignment_plan": {},
  "parallel_execution_plan": {},
  "testing_strategy": {},
  "ui_blueprint_inputs": {},
  "existing_state": {}
}
```

Read and update shared implementation state from:

```text
Build-Plans/Build-status/Implementation-state.json
```

---

# Execution Requirements

Before executing a ticket, verify:

* ticket has `agent_required_skills`
* ticket has `agent_skill_instructions`
* ticket has acceptance criteria
* ticket has validation steps
* launch-critical workflow tickets have `completion_definition`
* launch-critical workflow tickets have `workflow_smoke_tests`
* frontend tickets with `ui_blueprint_refs` have UI blueprint handoff inputs
* frontend tickets with `interaction_contract_refs` include interaction contract and complete app blueprint handoff inputs
* frontend tickets with `visual_spec_refs` include visual requirements and visual acceptance criteria
* frontend tickets with `visual_reference_refs` include selected visual style reference handoff inputs
* frontend tickets with `design_system_refs` include design system handoff inputs
* frontend tickets with `preview_required` include dev server or preview instructions
* frontend tickets include page, component, route, state, action, and interactive element refs when applicable
* ticket is assigned to an agent or explicitly marked for manual execution
* agent can use the ticket-required skills
* allowed and restricted file scopes are clear
* parallel execution conflicts are resolved or the ticket is in a serial batch

Do not execute blocked tickets.

Do not modify files outside assigned file scopes.

Do not change Stage 5 outputs during Stage 6 execution.

When executing a frontend ticket with `ui_blueprint_refs`, use:

```text
Build-Plans/Stage-4/07-ui-blueprint-specification.json
```

as the source for page structure, layout type, sections, components, shared components, routes, actions, states, data requirements, validation requirements, accessibility requirements, responsive requirements, visual requirements, visual reference requirements, visual acceptance criteria, design system requirements, and stable interaction contracts.

Also preserve Stage 4 structural UI architecture requirements from each referenced UI blueprint, including selected template/extensions, page archetype, layout pattern decision, rejected plausible patterns, layout rationale, component-family decisions, template deviations, and desktop/tablet/mobile transformations.

Preserve `UI-ELEMENT-`, `ROUTE-`, and `ACTION-` IDs, labels or accessible names, route types and targets, action outcomes, confirmations, permission-denied behavior, recovery behavior, responsive behavior, accessibility behavior, and design-system component mappings. Do not silently drop, rename, reroute, or change an interaction. Record a blocker or an approved deviation.

For launch-critical user workflows, do not stop at contract/API/static UI
implementation. Execute toward the declared runtime outcome:

```text
UI action -> route/API/action -> database/queue/storage -> worker/service -> result visible in UI -> evidence
```

Visible controls must be wired to working behavior or explicitly disabled with a
reason. Runtime pages must replace preview fixtures with live data sources before
Stage 6 can be ready.

---

# Outputs

```json
{
  "implemented_items": [],
  "implemented_tickets": [],
  "agent_execution_results": [],
  "parallel_batch_results": [
    {
      "batch_id": "",
      "status": "",
      "completed_at": "",
      "recorded_at": "",
      "completed_tickets": [],
      "blocked_tickets": [],
      "failed_tickets": [],
      "validation_gates_passed": [],
      "validation_gates_failed": [],
      "conflicts_detected": [],
      "blocking_failures": [],
      "batch_completion_recorded": false
    }
  ],
  "ui_blueprint_execution_refs": [],
  "interaction_contract_execution_refs": [],
  "interactive_element_execution_refs": [],
  "interaction_deviations": [],
  "visual_spec_execution_refs": [],
  "visual_reference_execution_refs": [],
  "design_system_execution_refs": [],
  "preview_urls": [],
  "artifact_evidence_updates": [],
  "workflow_evidence": [],
  "dead_control_findings": [],
  "runtime_data_source_findings": [],
  "pending_items": [],
  "blocked_items": [],
  "implementation_notes": [],
  "implementation_risks": []
}
```

---

# Shared State Updates

Update:

```text
implementation_status
execution_blockers
active_agents
parallel_batches
interactive_guidance
```

Persist updates to:

```text
Build-Plans/Build-status/Implementation-state.json
```

---

# Validation Responsibilities

Validate:

* every executed ticket maps to a Stage 5 ticket ID
* every executed ticket records the agent or manual executor
* every executed ticket records required skills used
* every executed ticket records changed files when available
* every executed frontend ticket with `ui_blueprint_refs` records the referenced UI blueprint IDs
* every executed frontend ticket with UI architecture refs records the referenced template, extensions, page archetype, layout pattern, component family, and deviation refs
* every executed frontend ticket with `interaction_contract_refs` records contract and stable interaction IDs
* every executed frontend ticket with `visual_spec_refs` records the referenced visual spec IDs
* every executed frontend ticket with `visual_reference_refs` records the referenced visual style references
* every executed frontend ticket with `design_system_refs` records the referenced design system IDs
* every executed frontend ticket with `preview_required` records a preview URL or blocker
* every visible launch-critical control is wired, explicitly disabled with reason, deferred with approval, or blocked
* every launch-critical runtime page records whether it uses live data or preview fixtures
* every launch-critical workflow records workflow evidence status separate from build status
* every executed frontend ticket preserves referenced page, component, route, action, state, interactive element (with element_type, label, route_target, and behavior), validation, accessibility, responsive, visual, visual reference, and design system requirements
* every executed frontend ticket preserves referenced layout pattern decision, layout rationale, component-family requirements, template deviations, and responsive transformations
* every dropped, renamed, rerouted, or behavior-changed interaction has an approved deviation with rationale and evidence
* every generated implementation, preview, build, or log artifact is recorded or queued for `Build-Plans/Build-status/Artifact-evidence-registry.json`
* every blocker includes a reason and next action
* every parallel batch execution records batch status
* every parallel batch result records completion status, completed_at, and recorded_at
