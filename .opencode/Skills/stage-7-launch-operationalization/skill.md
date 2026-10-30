---
name: stage-7-launch-operationalization
description: The stage-7-launch-operationalization command orchestrates Stage 7.
compatibility: opencode
---

# Command — stage-7-launch-operationalization

# Purpose

The `stage-7-launch-operationalization` command orchestrates Stage 7.

It transforms:

* Stage 6 implementation outputs
* Stage 6 system health
* Stage 6 repair and validation evidence
* Stage 6 visual QA and design system compliance evidence
* Stage 6 interaction contract conformance and approved deviation evidence
* deployment prerequisites
* operational requirements

into:

* launch readiness model
* deployment framework
* monitoring systems
* analytics framework
* operational tooling model
* Stage 8 handoff

This is the Stage 7 command skill. It is not a single operationalization subskill.

---

# Output Directory

All final Stage 7 outputs must be recorded in:

```text
Build-Plans/Stage-7/
```

The command must create this folder if it does not exist.

---

# Shared Operationalization State

The shared Stage 7 state must be written to:

```text
Build-Plans/Build-status/Operationalization-state.json
```

The command must load this file at the beginning of Stage 7, update it after each operationalization skill runs, and preserve it as durable operationalization state.

---

# Input Contract

Load Stage 6 outputs from:

```text
Build-Plans/Stage-6/
```

Required Stage 6 files:

```text
01-implementation-status.json
02-validation-results.json
03-regression-analysis.json
04-system-health.json
05-repair-log.json
```

Minimum viable input set:

```text
01-implementation-status.json
02-validation-results.json
04-system-health.json
```

---

# Orchestrated Skills

Run Stage 7 skills in this order:

```text
1. launch-readiness-validation
2. deployment-framework-planning
3. monitoring-systems-planning
4. analytics-framework-planning
5. operational-tooling-planning
6. launch-operationalization-synthesis
```

---

# Final Outputs

Generate:

```text
Build-Plans/Stage-7/01-launch-readiness.json
Build-Plans/Stage-7/02-deployment-framework.json
Build-Plans/Stage-7/03-monitoring-systems.json
Build-Plans/Stage-7/04-analytics-framework.json
Build-Plans/Stage-7/05-operational-tooling.json
Build-Plans/Stage-7/06-stage-7-summary.md
```

`06-stage-7-summary.md` is a local human-readable review artifact for every Stage 7 finalization attempt, including ready, revision, and blocked outcomes. It must summarize actions taken, launch readiness, deployment framework, monitoring, analytics, operational tooling, accepted launch risks, blockers, next actions, Stage 8 handoff readiness, and a clear user assessment. It must not contain canonical data that is absent from the JSON outputs.

Do not add `06-stage-7-summary.md` to `stage_8_handoff`, required Stage 8 inputs, or downstream readiness requirements. Stage 8 must continue to consume the Stage 7 JSON outputs.

---

# Final Readiness Audit

At the end of every Stage 7 finalization attempt, run `global-stage-readiness-audit`.

Run the audit after the five Stage 7 outputs are assembled and after Stage 7 derives a proposed completion status, but before writing the final completion status to shared state.

The audit must write:

```text
Build-Plans/Build-status/Stage-7-readiness-audit.json
```

The audit must pass according to:

```text
System-References/Docs/Global-Stage-Workflow-Contract.md
```

If the audit does not pass, do not use `ready_for_stage_8`.

The audit must still be written when Stage 7 resolves to `needs_launch_readiness_work`, `needs_operational_revision`, or `blocked`. Failed or blocked audits must preserve their findings in `blocking_gaps`, `revision_loops`, and `next_actions`.

Stage 7 audit input must include:

```json
{
  "stage": "Stage 7",
  "stage_number": 7,
  "stage_output_directory": "Build-Plans/Stage-7/",
  "required_output_files": [
    "01-launch-readiness.json",
    "02-deployment-framework.json",
    "03-monitoring-systems.json",
    "04-analytics-framework.json",
    "05-operational-tooling.json"
  ],
  "stage_state_file": "Build-Plans/Build-status/Operationalization-state.json",
  "expected_handoff_key": "stage_8_handoff",
  "expected_next_stage": "Stage 8",
  "proposed_completion_status": "",
  "finalization_attempt": true,
  "handoff_mode": "next_stage"
}
```

---

# Completion Status Values

```text
ready_for_stage_8
needs_launch_readiness_work
needs_operational_revision
blocked
```

Use `ready_for_stage_8` only when Stage 8 can safely consume launch, monitoring, analytics, support, incident, and operational signal sources.

The final Stage 7 status may be `ready_for_stage_8` only when `Build-Plans/Build-status/Stage-7-readiness-audit.json` has `audit_status` of `passed` or `passed_with_warnings` and `ready_for_next_stage` is `true`.

Stage 7 may use `ready_for_stage_8` only when the local human-readable assessment summary exists at `Build-Plans/Stage-7/06-stage-7-summary.md`, matches the canonical Stage 7 JSON outputs, identifies whether the stage is ready, needs revision, or is blocked, and does not add downstream requirements.

Stage 7 must not use `ready_for_stage_8` when launch-critical frontend work has unresolved visual QA failures, unresolved UI architecture/layout pattern/component-family/template-deviation compliance failures, unresolved visual reference compliance failures, unresolved design system compliance failures, missing required preview evidence, or `major_visual_drift`, unless each item is explicitly accepted as a known launch risk.

Stage 7 must also block `ready_for_stage_8` when a launch-critical `UI-ELEMENT-`, `ROUTE-`, or `ACTION-` has unresolved interaction conformance failures; missing required route, outcome, confirmation, permission, recovery, mobile, accessibility, layout pattern, or design-system behavior; or an unapproved material deviation. Record accepted exceptions as launch risks tied to the affected stable IDs or affected layout/template refs.

Stage 7 must reject the Stage 6 handoff when launch-critical workflow evidence
is missing or insufficient. Every launch-critical workflow must be
`local_e2e_passed`, `staging_e2e_passed`, explicitly deferred with approval, or
accepted as a launch risk with owner, severity, mitigation, and rollback/support
path. Missing workflow evidence, unresolved dead controls, and unresolved
fixture-backed runtime data are launch blockers, not documentation gaps.

---

# A-Grade Workflow Compliance

Stage 7 must consume `stage_contract_profile` and `guidance_policy`.

Stage 7 must reference:

```text
System-References/Schemas/stage-7-output.schema.json
```

Stage 7 must record production build proof, deployment dry-run evidence, workflow evidence review, smoke test results, rollback verification, environment verification, monitoring alert proof, and accepted launch risk evidence in:

```text
Build-Plans/Build-status/Artifact-evidence-registry.json
```

Before using `ready_for_stage_8`, Stage 7 must provide `schema_validation`, `reference_integrity`, `risk_acceptance_ledger`, and `revision_loops` in the readiness audit or stage state.

Accepted high and critical launch, deployment, monitoring, analytics, support, or operational risks must be recorded in:

```text
Build-Plans/Build-status/Risk-acceptance-ledger.json
```

Failed readiness checks must become revision-loop actions with owning output, owning skill, required change, and next action.
