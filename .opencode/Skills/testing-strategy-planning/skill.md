---
name: testing-strategy-planning
description: Define the canonical Stage 5 testing strategy for Stage 6 execution.
compatibility: opencode
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

This skill is the testing orchestration layer for Stage 5.

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

Read and update shared development state from:

```text
Build-Plans/Build-status/Development-state.json
```

---

# Core Responsibilities

## Testing Strategy

Define:

* unit testing scope
* integration testing scope
* end-to-end testing scope
* launch-critical workflow smoke tests
* workflow outcome evidence requirements
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
* Stage 5 ticket `completion_definition`
* Stage 6 `workflow_evidence`

For every launch-critical user workflow, define a smoke test that proves:

```text
UI action -> route/API/action -> database/queue/storage -> worker/service -> result visible in UI -> evidence
```

Do not treat a contract, generated API route, static page, fixture-backed page,
or successful build as enough workflow evidence.

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

Guide the user through test planning decisions that materially affect release confidence.

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

# Outputs

```json
{
  "testing_strategy": {},
  "test_levels": [],
  "acceptance_criteria": [],
  "workflow_smoke_tests": [],
  "workflow_evidence_requirements": [],
  "regression_strategy": {},
  "testing_risks": [],
  "release_test_gates": []
}
```

---

# Shared State Updates

Update:

```text
testing_strategy
execution_risks
coordination_notes
interactive_guidance
```

Persist updates to:

```text
Build-Plans/Build-status/Development-state.json
```

---

# Validation Responsibilities

Validate:

* every launch-critical workflow has acceptance criteria
* every implementation slice has a validation checkpoint
* API, integration, accessibility, and security risks are reflected in test scope
* release gates include regression checks
* any manual validation assumptions are recorded

---

# Normalized Stage 5 v2 Output

Keep all testing collections inside
`04-testing-strategy.json.data.testing_strategy`. Testing views reference
ticket, slice, workflow, risk, and validation IDs and never duplicate their
complete objects.
