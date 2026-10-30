---
name: stage-8-post-launch-evolution
description: The stage-8-post-launch-evolution command orchestrates Stage 8.
compatibility: opencode
---

# Command — stage-8-post-launch-evolution

# Purpose

The `stage-8-post-launch-evolution` command orchestrates Stage 8.

It transforms:

* Stage 7 launch and operationalization outputs
* live telemetry
* analytics signals
* support signals
* incident signals
* AI performance signals
* scalability and cost signals

into:

* telemetry analysis
* operational optimization
* AI improvement plan
* roadmap evolution
* scalability evolution

This is the Stage 8 command skill. It is not a single optimization subskill.

---

# Output Directory

All final Stage 8 outputs must be recorded in:

```text
Build-Plans/Stage-8/
```

The command must create this folder if it does not exist.

---

# Shared Evolution State

The shared Stage 8 state must be written to:

```text
Build-Plans/Build-status/Evolution-state.json
```

The command must load this file at the beginning of Stage 8, update it after each evolution skill runs, and preserve it as durable evolution state.

---

# Input Contract

Load Stage 7 outputs from:

```text
Build-Plans/Stage-7/
```

Required Stage 7 files:

```text
01-launch-readiness.json
03-monitoring-systems.json
04-analytics-framework.json
05-operational-tooling.json
```

Live-product inputs may include telemetry data, analytics data, support logs, incident logs, AI quality reports, user feedback, cost metrics, and scalability metrics.

When interaction telemetry exists, normalize events to stable Stage 4 `UI-ELEMENT-`, `ROUTE-`, and `ACTION-` IDs and preserve related Stage 4 UI architecture, page archetype, layout pattern, component-family, Stage 5 ticket, and Stage 6 validation references when present. Record unmapped events as telemetry gaps.

---

# Orchestrated Skills

Run Stage 8 skills in this order:

```text
1. telemetry-analysis
2. operational-optimization
3. ai-improvement-planning
4. roadmap-evolution-planning
5. scalability-evolution-planning
6. post-launch-evolution-synthesis
```

---

# Final Outputs

Generate:

```text
Build-Plans/Stage-8/01-telemetry-analysis.json
Build-Plans/Stage-8/02-operational-optimization.json
Build-Plans/Stage-8/03-ai-improvement-plan.json
Build-Plans/Stage-8/04-roadmap-evolution.json
Build-Plans/Stage-8/05-scalability-evolution.json
Build-Plans/Stage-8/06-stage-8-summary.md
```

`06-stage-8-summary.md` is a local human-readable review artifact for every Stage 8 finalization attempt, including evolution-ready, operational-review, telemetry-gap, and blocked outcomes. It must summarize actions taken, telemetry findings, operational optimization, AI improvement needs, roadmap evolution, scalability evolution, feedback routes, evidence gaps, risks, next actions, evolution readiness, and a clear user assessment. It must not contain canonical data that is absent from the JSON outputs.

Do not add `06-stage-8-summary.md` to `prior_stage_feedback`, required routed-stage inputs, or downstream readiness requirements. Earlier-stage revision routes must continue to consume the canonical Stage 8 JSON outputs.

---

# Final Readiness Audit

At the end of every Stage 8 finalization attempt, run `global-stage-readiness-audit`.

Run the audit after the five Stage 8 outputs are assembled and after Stage 8 derives a proposed completion status, but before writing the final completion status to shared state.

The audit must write:

```text
Build-Plans/Build-status/Stage-8-readiness-audit.json
```

The audit must pass according to:

```text
System-References/Docs/Global-Stage-Workflow-Contract.md
```

If the audit does not pass, do not use `evolution_plan_ready`.

The audit must still be written when Stage 8 resolves to `needs_more_telemetry`, `needs_operational_review`, or `blocked`. Failed or blocked audits must preserve their findings in `blocking_gaps`, `revision_loops`, and `next_actions`.

Stage 8 audit input must include:

```json
{
  "stage": "Stage 8",
  "stage_number": 8,
  "stage_output_directory": "Build-Plans/Stage-8/",
  "required_output_files": [
    "01-telemetry-analysis.json",
    "02-operational-optimization.json",
    "03-ai-improvement-plan.json",
    "04-roadmap-evolution.json",
    "05-scalability-evolution.json"
  ],
  "stage_state_file": "Build-Plans/Build-status/Evolution-state.json",
  "expected_handoff_key": "prior_stage_feedback",
  "expected_next_stage": "Earlier stages",
  "proposed_completion_status": "",
  "finalization_attempt": true,
  "handoff_mode": "feedback_routes"
}
```

---

# Completion Status Values

```text
evolution_plan_ready
needs_more_telemetry
needs_operational_review
blocked
```

Use `evolution_plan_ready` only when findings are evidence-backed, recommendations are traceable, and revision loops are routed to the correct earlier stages.

The final Stage 8 status may be `evolution_plan_ready` only when `Build-Plans/Build-status/Stage-8-readiness-audit.json` has `audit_status` of `passed` or `passed_with_warnings` and `ready_for_next_stage` is `true`.

Stage 8 may use `evolution_plan_ready` only when the local human-readable assessment summary exists at `Build-Plans/Stage-8/06-stage-8-summary.md`, matches the canonical Stage 8 JSON outputs, identifies whether the stage is ready, needs revision, or is blocked, and does not add routed-stage requirements.

---

# Prior Stage Feedback Routing

Stage 8 must classify live findings and route them to the correct stage when they expose a flaw in product strategy, validation, architecture, UX, implementation, launch operations, or roadmap direction.

Feedback route object:

```json
{
  "feedback_route_id": "",
  "source_signal_ids": [],
  "ui_element_refs": [],
  "route_refs": [],
  "action_refs": [],
  "stage_5_ticket_refs": [],
  "stage_6_validation_refs": [],
  "finding": "",
  "recommended_target_stage": "",
  "owner": "",
  "severity": "",
  "evidence_refs": [],
  "recommended_action": "",
  "blocks_current_evolution": false,
  "creates_new_stage_cycle": false
}
```

Unresolved critical feedback routes must have owners or explicit next actions before `evolution_plan_ready`.

When feedback routes create a new cycle, the readiness audit must record `handoff_mode: "feedback_routes"` and preserve the target stages, owners, evidence refs, actions, and `creates_new_stage_cycle` flags. Missing ownership, evidence, or next action on unresolved critical routes blocks `evolution_plan_ready`.

---

# A-Grade Workflow Compliance

Stage 8 must consume `stage_contract_profile` and `guidance_policy`.

Stage 8 must reference:

```text
System-References/Schemas/stage-8-output.schema.json
```

Stage 8 telemetry, analytics, support, incident, user feedback, and cost/scalability evidence should be referenced in:

```text
Build-Plans/Build-status/Artifact-evidence-registry.json
```

Before using `evolution_plan_ready`, Stage 8 must provide `schema_validation`, `reference_integrity`, `risk_acceptance_ledger`, and `revision_loops` in the readiness audit or stage state.

Accepted high and critical evolution, feedback routing, telemetry, scalability, AI, or operational risks must be recorded in:

```text
Build-Plans/Build-status/Risk-acceptance-ledger.json
```

Failed readiness checks must become revision-loop actions with owning output, owning skill, required change, and next action.
