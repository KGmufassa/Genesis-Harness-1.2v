---
name: parallel-execution-planning
description: Create dependency-safe Stage 5 batches and execution waves.
compatibility: opencode
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

Read and update shared development state from:

```text
Build-Plans/Build-status/Development-state.json
```

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
  "execution_waves": [
    {
      "wave": 1,
      "ticket_ids": []
    }
  ],
  "blocked_by_batches": [],
  "file_ownership_boundaries": [],
  "shared_contracts": [],
  "merge_strategy": "",
  "batch_validation": [],
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

## Execution Wave Validation

When tickets in one batch depend on one another:

* put every prerequisite in an earlier `execution_waves` entry
* put each dependent ticket in a later wave
* include only independently executable tickets in the same wave
* include every batch ticket in exactly one wave
* fail generation when a dependency is absent, duplicated, or ordered in the same or a later wave

Run `validate_execution_waves` from the Stage 5 contract helper before writing
the parallel execution artifact.

## Conflict Control

Block parallel execution when tickets have:

* dependency conflicts
* file ownership conflicts
* shared API or schema conflicts
* unresolved architecture or UX decisions
* incompatible validation requirements
* high-risk integration overlap

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

Update:

```text
parallel_execution_plan
agent_assignment_plan
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

* safe parallel work is separated from serial work
* every batch has a merge strategy
* every batch has validation gates
* every batch has valid `execution_waves`
* file ownership boundaries are explicit
* shared contract conflicts block parallel execution
* high-risk integration work is serialized unless explicitly approved
