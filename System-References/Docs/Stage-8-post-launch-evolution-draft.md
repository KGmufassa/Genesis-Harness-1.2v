# Stage 8 — Post Launch Evolution Command & Skill Draft

# Core Philosophy

Stage 8 is centered around:

```text
continuous product evolution cognition
```

Stage 8 uses telemetry, operations, AI improvement, scalability data, and roadmap learning to evolve the product after launch.

---

# Recommended Stage 8 Architecture

```text
stage-8-post-launch-evolution (command)
│
├── telemetry-analysis
├── operational-optimization
├── ai-improvement-planning
├── roadmap-evolution-planning
├── scalability-evolution-planning
└── post-launch-evolution-synthesis
```

---

# Command — stage-8-post-launch-evolution

# Purpose

The `stage-8-post-launch-evolution` command orchestrates Stage 8.

It transforms:

* telemetry
* operational signals
* analytics
* support signals
* scalability signals
* AI performance signals

into:

* telemetry analysis
* operational optimization
* AI improvement plan
* roadmap evolution
* scalability evolution

---

# Cognitive Boundary

Stage 8 asks:

```text
How should the live product evolve based on real-world signals?
```

Stage 8 must not:

* perform launch readiness work
* replace incident response
* rewrite previous planning without evidence
* optimize without telemetry or operational rationale

---

# Output Directory

All final Stage 8 outputs must be recorded in:

```text
Build-Plans/Stage-8/
```

---

# Shared Evolution State

The shared Stage 8 state must be written to:

```text
Build-Plans/Build-status/Evolution-state.json
```

```json
{
  "stage": "Stage 8",
  "command": "stage-8-post-launch-evolution",
  "status": "not_started",
  "stage_7_inputs": {},
  "stage_7_handoff": {},
  "live_signal_inputs": {},
  "telemetry_analysis": {},
  "operational_optimization": {},
  "ai_improvement_plan": {},
  "roadmap_evolution": {},
  "scalability_evolution": {},
  "experiment_plan": {},
  "evidence_registry": [],
  "evolution_risks": [],
  "learning_log": [],
  "interactive_guidance": {
    "open_questions": [],
    "answered_questions": [],
    "assumptions_made": [],
    "blocked_decisions": [],
    "user_confirmations": [],
    "evolution_confidence_gaps": []
  },
  "completion_status": {}
}
```

---

# Interactive Guidance Rules

Ask only for evolution decisions that materially affect optimization, roadmap direction, AI improvement, operational changes, or scaling priorities.

Pause for user input when:

* telemetry is incomplete or contradictory
* optimization priority is unclear
* AI improvement path has multiple valid directions
* roadmap changes affect strategic direction
* scalability work requires investment tradeoffs
* operational changes affect support or user experience

---

# Stage 7 Handoff Consumption

Stage 8 must consume the Stage 8 handoff produced by Stage 7:

```text
Build-Plans/Stage-7/05-operational-tooling.json
```

Normalize the handoff into:

```json
{
  "launch_status": "",
  "launch_gates": [],
  "monitoring_sources": [],
  "analytics_events": [],
  "success_metrics": [],
  "support_signal_sources": [],
  "incident_signal_sources": [],
  "operational_runbooks": [],
  "known_defects": [],
  "accepted_risks": [],
  "telemetry_gaps": [],
  "recommended_evolution_watchlist": []
}
```

---

# Prior Stage Feedback Routing

Stage 8 must classify live findings and route them to the correct stage when they cannot be solved only through post-launch optimization.

Routing rules:

| Signal | Route |
| --- | --- |
| Retention, positioning, or product-market issue | Stage 1 or Stage 2 |
| Invalid validated assumption | Stage 2 |
| Performance, API, infrastructure, security, or scalability issue | Stage 3 |
| UX confusion, navigation friction, layout pattern mismatch, component-family mismatch, accessibility issue | Stage 4 |
| Ticket sequencing, agent, or test coverage issue | Stage 5 |
| Bug, regression, repair, or validation failure | Stage 6 |
| Support, monitoring, onboarding, or operational issue | Stage 7 |
| Roadmap expansion or optimization opportunity | Stage 8 |

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
  "severity": "",
  "evidence_refs": [],
  "recommended_action": "",
  "blocks_current_evolution": false,
  "creates_new_stage_cycle": false
}
```

---

# Stage 8 Input Contract

Normalize interaction telemetry to stable `UI-ELEMENT-`, `ROUTE-`, and `ACTION-` IDs and preserve related Stage 4 UI architecture, page archetype, layout pattern, component-family, Stage 5 ticket, and Stage 6 validation references when present. Record unmapped interaction events as telemetry gaps.

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

External live-product inputs may include:

```text
telemetry data
analytics data
support logs
incident logs
AI quality reports
user feedback
cost and scalability metrics
```

---

# Live Signal Input Schemas

Telemetry input entries should include:

```json
{
  "signal_id": "",
  "source": "",
  "metric_name": "",
  "time_window": "",
  "value": null,
  "segment": "",
  "confidence": "",
  "notes": ""
}
```

User feedback entries should include:

```json
{
  "feedback_id": "",
  "source": "",
  "user_segment": "",
  "theme": "",
  "severity": "",
  "evidence": "",
  "related_feature_ids": [],
  "frequency": ""
}
```

Incident entries should include:

```json
{
  "incident_id": "",
  "severity": "",
  "started_at": "",
  "resolved_at": "",
  "affected_features": [],
  "root_cause": "",
  "user_impact": "",
  "follow_up_actions": []
}
```

AI quality entries should include:

```json
{
  "ai_signal_id": "",
  "model_or_prompt_version": "",
  "task": "",
  "failure_category": "",
  "quality_score": null,
  "human_review_signal": "",
  "safety_concern": "",
  "regression_risk": ""
}
```

Minimum viable Stage 8 input:

```text
Stage 7 monitoring sources
Stage 7 analytics framework
at least one live signal source or an explicit telemetry gap record
```

If live signals are missing, Stage 8 must set `completion_status.status = "needs_more_telemetry"` unless the task is specifically to define the telemetry collection plan.

---

# Evidence Quality Rules

Stage 8 findings must distinguish:

```text
telemetry_evidence
analytics_evidence
support_evidence
incident_evidence
ai_evaluation_evidence
user_feedback
inference
recommendation
```

Every recommendation must include:

```json
{
  "recommendation_id": "",
  "recommendation": "",
  "evidence_refs": [],
  "evidence_quality": "low",
  "confidence": 0.0,
  "expected_impact": "",
  "risk": "",
  "next_action": ""
}
```

Low-evidence recommendations must be marked provisional.

---

# Decision Thresholds

Stage 8 may recommend roadmap, AI, operational, or scalability changes only when one of these is true:

* multiple independent evidence sources support the same finding
* a launch-critical metric misses its threshold
* repeated support or incident signals show recurring user impact
* AI quality or safety signals cross an accepted risk threshold
* cost, latency, error rate, or capacity trends threaten operational sustainability
* user feedback identifies a high-severity product gap

When evidence is weak, Stage 8 should recommend an experiment or measurement improvement before recommending a major change.

---

# Experiment And Iteration Model

Evolution work should be framed as experiments or evidence-backed changes.

Experiment entries must include:

```json
{
  "experiment_id": "",
  "hypothesis": "",
  "target_segment": "",
  "change": "",
  "success_metric": "",
  "guardrail_metrics": [],
  "rollout_scope": "",
  "start_criteria": [],
  "stop_criteria": [],
  "review_date": "",
  "owner": ""
}
```

---

# AI Improvement Rules

AI improvement planning must track:

* model or prompt version
* task category
* failure categories
* quality metrics
* human review signals
* safety concerns
* dataset or example needs
* prompt/model change recommendations
* regression checks required before rollout

---

# Roadmap And Prior-Stage Feedback Rules

Roadmap evolution must classify each proposed change as:

```text
new_roadmap_item
backlog_candidate
deprecation_candidate
simplification
needs_stage_1_revision
needs_stage_2_revalidation
needs_stage_3_architecture_revision
needs_stage_4_ux_revision
needs_stage_5_orchestration
needs_stage_6_implementation
```

Major product direction changes must route back to the appropriate earlier stage instead of being silently absorbed in Stage 8.

---

# Operational And Scalability Measures

Operational optimization should track:

```text
support_volume
time_to_resolution
incident_frequency
runbook_coverage
manual_workload
operational_cost
```

Scalability evolution should track:

```text
latency
throughput
error_rate
queue_depth
database_pressure
infrastructure_cost
AI_cost
capacity_trends
```

---

# Stage 8 Skills

## Skill — telemetry-analysis

Purpose:

* analyze usage data
* identify product behavior signals
* detect activation, retention, and friction patterns

Outputs:

```json
{
  "telemetry_analysis": {},
  "usage_patterns": [],
  "friction_points": [],
  "success_signals": [],
  "telemetry_gaps": []
}
```

---

## Skill — operational-optimization

Purpose:

* analyze operational burden
* improve support workflows
* optimize monitoring and tooling
* reduce operational friction

Outputs:

```json
{
  "operational_optimization": {},
  "support_improvements": [],
  "tooling_improvements": [],
  "operational_risks": []
}
```

---

## Skill — ai-improvement-planning

Purpose:

* evaluate AI quality signals
* detect model, prompt, data, or workflow improvement needs
* plan AI iteration

Outputs:

```json
{
  "ai_improvement_plan": {},
  "quality_gaps": [],
  "training_or_prompt_needs": [],
  "evaluation_needs": [],
  "ai_risks": []
}
```

---

## Skill — roadmap-evolution-planning

Purpose:

* evolve roadmap based on evidence
* prioritize improvements
* decide expansion, simplification, or refinement

Outputs:

```json
{
  "roadmap_evolution": {},
  "new_opportunities": [],
  "deferred_items_to_revisit": [],
  "roadmap_risks": []
}
```

---

## Skill — scalability-evolution-planning

Purpose:

* analyze scaling signals
* plan infrastructure and operational scalability improvements
* identify cost and performance optimization needs

Outputs:

```json
{
  "scalability_evolution": {},
  "performance_findings": [],
  "cost_findings": [],
  "scaling_recommendations": [],
  "scalability_risks": []
}
```

---

## Skill — post-launch-evolution-synthesis

Purpose:

* synthesize telemetry, operations, AI improvement, roadmap, and scalability findings
* produce a coherent evolution plan

Final outputs:

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

Completion statuses:

```text
evolution_plan_ready
needs_more_telemetry
needs_operational_review
blocked
```

---

# Final Output Schemas

`01-telemetry-analysis.json` must include:

```json
{
  "stage": "Stage 8",
  "status": "",
  "telemetry_analysis": {},
  "usage_patterns": [],
  "activation_findings": [],
  "retention_findings": [],
  "friction_points": [],
  "success_signals": [],
  "telemetry_gaps": [],
  "evidence_refs": []
}
```

`02-operational-optimization.json` must include:

```json
{
  "stage": "Stage 8",
  "status": "",
  "operational_optimization": {},
  "support_improvements": [],
  "runbook_improvements": [],
  "tooling_improvements": [],
  "incident_findings": [],
  "cost_or_workload_findings": [],
  "operational_risks": [],
  "evidence_refs": []
}
```

`03-ai-improvement-plan.json` must include:

```json
{
  "stage": "Stage 8",
  "status": "",
  "ai_improvement_plan": {},
  "model_or_prompt_versions": [],
  "quality_gaps": [],
  "failure_categories": [],
  "training_or_prompt_needs": [],
  "evaluation_needs": [],
  "safety_concerns": [],
  "regression_checks": [],
  "ai_risks": []
}
```

`04-roadmap-evolution.json` must include:

```json
{
  "stage": "Stage 8",
  "status": "",
  "roadmap_evolution": {},
  "new_opportunities": [],
  "backlog_candidates": [],
  "deprecation_candidates": [],
  "simplification_candidates": [],
  "experiments": [],
  "prior_stage_feedback": [],
  "roadmap_risks": []
}
```

`05-scalability-evolution.json` must include:

```json
{
  "stage": "Stage 8",
  "status": "",
  "scalability_evolution": {},
  "performance_findings": [],
  "cost_findings": [],
  "capacity_trends": [],
  "scaling_recommendations": [],
  "infrastructure_recommendations": [],
  "ai_cost_recommendations": [],
  "scalability_risks": []
}
```

---

# Completion Gate

At the end of every Stage 8 finalization attempt, Stage 8 must run `global-stage-readiness-audit` and write:

```text
Build-Plans/Build-status/Stage-8-readiness-audit.json
```

Run the audit after the Stage 8 outputs are assembled and after Stage 8 derives a proposed completion status, but before the final status is committed to `Build-Plans/Build-status/Evolution-state.json` or `Build-Plans/Build-status/Global-workflow-state.json`.

The audit must be written for `evolution_plan_ready`, `needs_more_telemetry`, `needs_operational_review`, and `blocked` outcomes.

The audit must pass according to:

```text
System-References/Docs/Global-Stage-Workflow-Contract.md
```

Stage 8 may complete as `evolution_plan_ready` only when:

* `Build-Plans/Build-status/Stage-8-readiness-audit.json` exists
* audit status is `passed` or `passed_with_warnings`
* audit `ready_for_next_stage` is `true`
* required Stage 7 outputs are present
* live signal inputs or telemetry gaps are recorded
* interaction findings map to stable interaction IDs and downstream ticket or validation references when available
* recommendations distinguish evidence from inference
* low-evidence recommendations are marked provisional
* roadmap changes are routed to the correct stage when needed
* AI improvements include evaluation and regression requirements
* operational and scalability recommendations include measurable signals
* experiments include hypotheses, metrics, rollout scope, and review dates
* local human-readable assessment summary exists at `Build-Plans/Stage-8/06-stage-8-summary.md`
* the summary matches canonical Stage 8 JSON outputs and identifies whether the stage is ready, needs revision, or is blocked
* unresolved critical feedback routes have owners or explicit next actions

Stage 8 is terminal and cyclical. Its readiness audit must evaluate `prior_stage_feedback` and feedback routes to earlier stages instead of a Stage 9 handoff.

---

# A-Grade Workflow Compliance

Stage 8 must consume `stage_contract_profile` and `guidance_policy`.

Stage 8 output validation should reference:

```text
System-References/Schemas/stage-8-output.schema.json
```

Stage 8 telemetry, analytics, support, incident, user feedback, and cost/scalability evidence should be referenced in:

```text
Build-Plans/Build-status/Artifact-evidence-registry.json
```

Stage 8 readiness must also record:

```json
{
  "finalization_attempt": true,
  "proposed_completion_status": "",
  "evaluated_completion_status": "",
  "handoff_mode": "feedback_routes",
  "schema_validation": {},
  "reference_integrity": {},
  "risk_acceptance_ledger": {},
  "feedback_route_audit": {},
  "revision_loops": []
}
```

Stage 8 may not use `evolution_plan_ready` until required schema validation passes, telemetry, support, incident, cost, feedback route, experiment, roadmap, artifact, and accepted-risk references resolve to upstream sources, accepted high and critical evolution risks are written to `Build-Plans/Build-status/Risk-acceptance-ledger.json`, and failed readiness checks are converted into revision-loop actions.
