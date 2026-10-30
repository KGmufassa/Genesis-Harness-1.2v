---
name: development-orchestration-synthesis
description: Validate and serialize the normalized Stage 5 v2 package and manifest.
compatibility: opencode
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

This skill is the final synthesis and completion gate for Stage 5.

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

Read and update shared development state from:

```text
Build-Plans/Build-status/Development-state.json
```

---

# Core Responsibilities

## Execution Coherence

Validate:

* roadmap aligns with MVP scope
* implementation sequence respects dependencies
* engineering dependencies are explicit
* testing strategy covers launch-critical workflows
* build tickets cover implementation slices
* build tickets include primary skill, recommended skill chain, agent-required skills, skill usage instructions, acceptance criteria, and validation steps
* agent assignment plan maps tickets to capable agents
* generated agents are written under `.opencode/agents/`
* generated agents include valid subagent frontmatter and prompt body based on ticket-required skills
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
* agent assignment tradeoffs
* parallel execution tradeoffs
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

Do not finalize Stage 5 if execution-blocking questions remain unresolved.

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
* launch-critical workflow tickets without outcome-based completion definitions
* missing workflow smoke-test obligations for launch-critical user paths

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

`stage_6_handoff` must include the launch-critical workflow IDs, smoke-test
requirements, and evidence obligations that Stage 6 must satisfy. A ticket that
represents a launch-critical user workflow is not complete when only contracts,
schemas, routes, fixtures, or static UI exist.

---

# Shared State Updates

Update:

```text
development_roadmap
implementation_sequence
engineering_dependencies
testing_strategy
build_tickets
agent_assignment_plan
parallel_execution_plan
release_plan
execution_risks
coordination_notes
stage_6_handoff
completion_status
interactive_guidance
```

`stage_6_handoff` and `completion_status` in this list are transient synthesis
values. Exclude them from shared-state persistence and serialize them only in
`09-stage-manifest.json`.

Persist updates to:

```text
Build-Plans/Build-status/Development-state.json
```

---

# Final Stage 5 Output Files

Write the normalized v2 context, numbered artifacts, and manifest:

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

The normalized contract in
`.opencode/Skills/stage-5-development-orchestration/skill.md` supersedes legacy
self-contained output examples below. Shared context is written only to file
`00`; canonical payloads are written only under `data` in files `01`-`08`; and
completion plus the Stage 6 handoff are written only to file `09`. Use
`stage5_contract.py` to construct and validate these documents.

Legacy self-contained outputs included the following shared material. Under v2,
place it in context file `00` or manifest file `09`, never in each numbered
artifact:

* related Stage 1 scope or feature inputs
* related Stage 3 architecture dependencies
* related Stage 4 UX dependencies
* execution decisions
* risks and constraints
* unresolved questions
* Stage 6 handoff notes when relevant

The build ticket output must include:

* ticket IDs
* slice IDs
* ticket dependencies
* primary skill from the skill registry
* recommended skill chain from the skill registry
* required skills the assigned agent must use
* skill usage instructions for the assigned agent
* skill suitability score and selection rationale
* skill coverage gaps when no suitable skill exists
* acceptance criteria
* validation steps
* risk level
* Stage 6 execution queue position

The agent assignment output must include:

* available agent inventory source
* agent IDs
* agent types
* generated agent file paths when new agents are created
* generated agent files under `.opencode/agents/`
* generated agent frontmatter including description, mode, model, temperature, and permissions
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
* unassigned tickets with manual-assignment or new-agent-profile reasons
* permission rationale for any generated agent with edit or bash access

The parallel execution output must include:

* parallel batch IDs
* assigned agents per batch
* tickets per batch
* blocked-by relationships
* file ownership boundaries
* shared contracts
* merge strategy
* batch validation gates

---

# Completion Gate

Stage 5 may complete only when:

* context, all eight normalized numbered artifacts, and the manifest exist
* development roadmap is defined
* implementation sequence is dependency-aware
* engineering dependencies are mapped
* testing strategy covers launch-critical workflows
* build tickets cover every MVP implementation slice
* build tickets include a best-suited primary skill or record why no matching skill exists
* build tickets include an ordered recommended skill chain
* build tickets include required skills for the assigned agent
* build tickets include skill usage instructions for the assigned agent
* build tickets include skill suitability scores and selection rationale
* build tickets include acceptance criteria and validation steps
* agent assignment plan scans available agents before assignment
* agent assignment plan assigns every MVP ticket to the most suitable available agent that can use the ticket-required skills, or records why it requires manual ownership
* agent assignment plan records suitability scores and assignment reasons
* generated agents are written under `.opencode/agents/`
* generated agents include valid subagent frontmatter and prompt body based on ticket-required skills
* generated agent prompt bodies include assigned tickets, required skills, skill usage order, file scopes, handoff inputs, validation requirements, rules, and reporting requirements
* generated agent permissions match the assigned role and risk level
* parallel execution plan separates safe parallel work from serial work
* parallel execution plan blocks unresolved dependency, file ownership, API, schema, architecture, or UX conflicts
* reference, risk-reference, agent-scope, execution-wave, manifest consistency, and schema validation have executed and passed
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
* testing strategy includes validation checkpoints
* build tickets exist for every MVP implementation slice
* build tickets include primary skill, recommended skill chain, agent-required skills, skill usage instructions, acceptance criteria, and validation steps
* agent assignment plan gives each agent clear ownership and handoff inputs
* agent assignment plan records available-agent scan results, suitability scores, and unassigned ticket reasons
* generated agents have valid markdown definitions in `.opencode/agents/`, safe permission settings, and complete prompt bodies
* parallel execution plan defines batches, merge strategy, and validation gates
* release plan includes readiness gates
* critical interactive guidance questions are answered or converted into recorded assumptions
* Stage 6 handoff is usable for implementation and validation
