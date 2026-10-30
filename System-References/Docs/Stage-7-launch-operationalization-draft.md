# Stage 7 — Launch & Operationalization Command & Skill Draft

# Core Philosophy

Stage 7 is centered around:

```text
production operationalization cognition
```

Stage 7 prepares the validated system for production deployment, onboarding, monitoring, analytics, support, and operational readiness.

---

# Recommended Stage 7 Architecture

```text
stage-7-launch-operationalization (command)
│
├── launch-readiness-validation
├── deployment-framework-planning
├── monitoring-systems-planning
├── analytics-framework-planning
├── operational-tooling-planning
└── launch-operationalization-synthesis
```

---

# Command — stage-7-launch-operationalization

# Purpose

The `stage-7-launch-operationalization` command orchestrates Stage 7.

It transforms:

* validated implementation outputs
* system health results
* release plan
* operational requirements

into:

* launch readiness model
* deployment framework
* monitoring systems
* analytics framework
* operational tooling model

---

# Cognitive Boundary

Stage 7 asks:

```text
Is the system ready to operate in production?
```

Stage 7 must not:

* redesign the product
* redesign architecture
* run implementation
* perform post-launch optimization

---

# Output Directory

All final Stage 7 outputs must be recorded in:

```text
Build-Plans/Stage-7/
```

---

# Shared Operationalization State

The shared Stage 7 state must be written to:

```text
Build-Plans/Build-status/Operationalization-state.json
```

```json
{
  "stage": "Stage 7",
  "command": "stage-7-launch-operationalization",
  "status": "not_started",
  "stage_6_inputs": {},
  "stage_6_handoff": {},
  "launch_readiness": {},
  "deployment_framework": {},
  "monitoring_systems": {},
  "analytics_framework": {},
  "operational_tooling": {},
  "support_model": {},
  "onboarding_model": {},
  "operational_risks": [],
  "interactive_guidance": {
    "open_questions": [],
    "answered_questions": [],
    "assumptions_made": [],
    "blocked_decisions": [],
    "user_confirmations": [],
    "operational_confidence_gaps": []
  },
  "stage_8_handoff": {},
  "completion_status": {}
}
```

---

# Interactive Guidance Rules

Ask only for operational decisions that materially affect launch readiness, deployment, monitoring, analytics, support, or Stage 8 evolution.

Pause for user input when:

* deployment environment is unclear
* launch readiness criteria are incomplete
* monitoring or alerting expectations are unknown
* analytics events are required but undefined
* support ownership is unclear
* rollback or incident response decisions are missing

---

# Stage 6 Handoff Consumption

Stage 7 must consume the Stage 6 handoff from:

```text
Build-Plans/Stage-6/04-system-health.json
```

The Stage 6 handoff should be normalized into:

```json
{
  "deployment_blockers": [],
  "deployment_prerequisites": [],
  "setup_commands": [],
  "build_command": "",
  "start_command": "",
  "test_commands": [],
  "environment_variables_required": [],
  "secrets_required": [],
  "migration_requirements": [],
  "seed_data_requirements": [],
  "monitoring_needs": [],
  "analytics_needs": [],
  "support_needs": [],
  "known_defects": [],
  "accepted_risks": [],
  "visual_qa_results": [],
  "responsive_validation_results": [],
  "visual_reference_refs": [],
  "visual_reference_compliance": {},
  "design_system_compliance": {},
  "visual_drift_status": "",
  "visual_drift_source": "",
  "dev_server_url": "",
  "artifact_refs": []
}
```

Stage 7 must not mark launch-ready while unresolved launch-critical Stage 6 blockers remain, unless they are explicitly accepted as known launch risks.

Stage 7 must not mark launch-ready while launch-critical frontend work has unresolved visual QA failures, unresolved responsive validation failures, unresolved UI architecture/layout pattern/component-family/template-deviation compliance failures, unresolved `visual_reference_compliance`, unresolved design system compliance failures, missing required preview evidence, an unexplained `visual_drift_source`, or `major_visual_drift`, unless each item is explicitly accepted as a known launch risk.

---

# Stage 7 Input Contract

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

# Launch Gate Model

Stage 7 launch readiness must be evaluated through explicit gates:

```text
deployment_readiness
environment_readiness
secret_readiness
data_migration_readiness
validation_evidence_readiness
visual_qa_readiness
design_system_readiness
monitoring_readiness
analytics_readiness
rollback_readiness
support_readiness
onboarding_readiness
known_risk_acceptance
```

Every gate must include:

```json
{
  "gate_id": "",
  "name": "",
  "status": "pending",
  "owner": "",
  "evidence_refs": [],
  "blockers": [],
  "accepted_risks": [],
  "next_action": ""
}
```

Allowed gate statuses:

```text
pending
ready
blocked
accepted_risk
not_applicable
```

---

# Deployment Contract

The deployment framework must define:

```json
{
  "environments": [],
  "required_environment_variables": [],
  "required_secrets": [],
  "setup_commands": [],
  "build_command": "",
  "deployment_command": "",
  "rollback_command": "",
  "migration_plan": {},
  "seed_data_plan": {},
  "release_owner": "",
  "approval_status": "",
  "deployment_artifacts": [],
  "deployment_risks": []
}
```

Stage 7 must not invent secrets or environment values. Missing secrets must become launch blockers or explicit setup actions.

---

# Rollback And Incident Response Contract

Rollback planning must include:

```json
{
  "rollback_triggers": [],
  "rollback_steps": [],
  "rollback_owner": "",
  "recovery_verification": [],
  "data_recovery_notes": [],
  "user_communication_plan": ""
}
```

Incident response planning must include:

```json
{
  "severity_levels": [],
  "incident_triggers": [],
  "response_owners": [],
  "escalation_paths": [],
  "runbooks": [],
  "communication_channels": [],
  "post_incident_review_requirements": []
}
```

---

# Monitoring And Analytics Contracts

Monitoring must define:

```json
{
  "health_checks": [],
  "uptime_checks": [],
  "error_rate_alerts": [],
  "latency_alerts": [],
  "job_or_queue_checks": [],
  "log_requirements": [],
  "alert_owners": [],
  "slo_targets": [],
  "dashboard_refs": []
}
```

Analytics events must define:

```json
{
  "event_name": "",
  "trigger": "",
  "payload_fields": [],
  "user_identity_rules": [],
  "privacy_notes": [],
  "related_success_metric": "",
  "dashboard": "",
  "owner": ""
}
```

---

# Support, Onboarding, And Operational Tooling Contract

Operational tooling must define:

```json
{
  "onboarding_flows": [],
  "help_docs": [],
  "support_workflows": [],
  "support_ownership": [],
  "ticket_triage_rules": [],
  "admin_tools": [],
  "moderation_or_review_flows": [],
  "operational_dashboards": [],
  "runbooks": []
}
```

---

# Stage 8 Handoff Contract

Stage 7 must produce a concrete Stage 8 handoff:

```json
{
  "stage_7_output_directory": "Build-Plans/Stage-7/",
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
  "recommended_evolution_watchlist": [],
  "completion_status": {}
}
```

---

# Stage 7 Skills

## Skill — launch-readiness-validation

Purpose:

* validate production readiness
* confirm launch blockers
* assess user onboarding readiness
* verify support readiness

Outputs:

```json
{
  "launch_readiness": {},
  "launch_blockers": [],
  "readiness_gates": [],
  "onboarding_gaps": [],
  "support_gaps": []
}
```

---

## Skill — deployment-framework-planning

Purpose:

* define deployment environments
* deployment checklist
* rollback needs
* release execution process

Outputs:

```json
{
  "deployment_framework": {},
  "deployment_environments": [],
  "deployment_checklist": [],
  "rollback_plan": {},
  "deployment_risks": []
}
```

---

## Skill — monitoring-systems-planning

Purpose:

* define operational monitoring
* alerts
* logs
* uptime checks
* incident response triggers

Outputs:

```json
{
  "monitoring_systems": {},
  "alerts": [],
  "health_checks": [],
  "incident_triggers": [],
  "monitoring_risks": []
}
```

---

## Skill — analytics-framework-planning

Purpose:

* define analytics events
* product metrics
* activation metrics
* retention metrics
* success measurement

Outputs:

```json
{
  "analytics_framework": {},
  "events": [],
  "metrics": [],
  "dashboards": [],
  "analytics_risks": []
}
```

---

## Skill — operational-tooling-planning

Purpose:

* define admin tools
* support workflows
* moderation or review workflows
* operational dashboards
* runbooks

Outputs:

```json
{
  "operational_tooling": {},
  "support_model": {},
  "runbooks": [],
  "admin_tools": [],
  "tooling_risks": []
}
```

---

## Skill — launch-operationalization-synthesis

Purpose:

* synthesize production readiness
* determine launch status
* produce Stage 8 handoff

Final outputs:

```text
Build-Plans/Stage-7/01-launch-readiness.json
Build-Plans/Stage-7/02-deployment-framework.json
Build-Plans/Stage-7/03-monitoring-systems.json
Build-Plans/Stage-7/04-analytics-framework.json
Build-Plans/Stage-7/05-operational-tooling.json
Build-Plans/Stage-7/06-stage-7-summary.md
```

`06-stage-7-summary.md` is a local human-readable review artifact for every Stage 7 finalization attempt, including ready, revision, and blocked outcomes. It must summarize actions taken, launch readiness, deployment framework, monitoring, analytics, operational tooling, accepted launch risks, blockers, next actions, Stage 8 handoff readiness, and a clear user assessment. It must not contain canonical data that is absent from the JSON outputs.

Do not add `06-stage-7-summary.md` to `stage_8_handoff`, required Stage 8 inputs, or downstream readiness requirements. Stage 8 must continue to consume the canonical Stage 7 JSON outputs.

Completion statuses:

```text
ready_for_stage_8
needs_launch_readiness_work
needs_operational_revision
blocked
```

---

# Final Output Schemas

`01-launch-readiness.json` must include:

```json
{
  "stage": "Stage 7",
  "status": "",
  "launch_gates": [],
  "launch_blockers": [],
  "known_defects": [],
  "accepted_risks": [],
  "visual_launch_readiness": {},
  "design_system_launch_readiness": {},
  "deployment_proof": {
    "production_build_artifact": "",
    "deployment_dry_run_result": {},
    "smoke_test_results": [],
    "rollback_test_result": {},
    "environment_verification": {},
    "monitoring_alert_test": {},
    "release_blockers": [],
    "accepted_launch_risks": []
  },
  "onboarding_readiness": {},
  "support_readiness": {},
  "evidence_refs": [],
  "completion_status": {}
}
```

`02-deployment-framework.json` must include:

```json
{
  "stage": "Stage 7",
  "status": "",
  "deployment_framework": {},
  "environments": [],
  "environment_variables": [],
  "secrets_required": [],
  "setup_commands": [],
  "build_command": "",
  "deployment_command": "",
  "rollback_plan": {},
  "incident_response": {},
  "deployment_risks": []
}
```

`03-monitoring-systems.json` must include:

```json
{
  "stage": "Stage 7",
  "status": "",
  "monitoring_systems": {},
  "health_checks": [],
  "uptime_checks": [],
  "alerts": [],
  "slo_targets": [],
  "incident_triggers": [],
  "runbooks": [],
  "monitoring_risks": []
}
```

`04-analytics-framework.json` must include:

```json
{
  "stage": "Stage 7",
  "status": "",
  "analytics_framework": {},
  "events": [],
  "metrics": [],
  "dashboards": [],
  "privacy_notes": [],
  "success_metric_map": [],
  "analytics_risks": []
}
```

`05-operational-tooling.json` must include:

```json
{
  "stage": "Stage 7",
  "status": "",
  "operational_tooling": {},
  "support_model": {},
  "onboarding_model": {},
  "admin_tools": [],
  "support_workflows": [],
  "runbooks": [],
  "stage_8_handoff": {},
  "tooling_risks": []
}
```

---

# Completion Gate

At the end of every Stage 7 finalization attempt, Stage 7 must run `global-stage-readiness-audit` and write:

```text
Build-Plans/Build-status/Stage-7-readiness-audit.json
```

Run the audit after the Stage 7 outputs are assembled and after Stage 7 derives a proposed completion status, but before the final status is committed to `Build-Plans/Build-status/Operationalization-state.json` or `Build-Plans/Build-status/Global-workflow-state.json`.

The audit must be written for `ready_for_stage_8`, `needs_launch_readiness_work`, `needs_operational_revision`, and `blocked` outcomes.

The audit must pass according to:

```text
System-References/Docs/Global-Stage-Workflow-Contract.md
```

Stage 7 may complete as `ready_for_stage_8` only when:

* `Build-Plans/Build-status/Stage-7-readiness-audit.json` exists
* audit status is `passed` or `passed_with_warnings`
* audit `ready_for_next_stage` is `true`
* all five Stage 7 output files exist
* all launch gates are `ready`, `accepted_risk`, or `not_applicable`
* deployment environment, setup, build, deployment, and rollback details are defined or explicitly blocked
* production build proof, deployment dry-run evidence, smoke test evidence, rollback verification, and environment verification are recorded or explicitly accepted as known risks
* Stage 6 workflow evidence exists for every launch-critical user workflow
* every launch-critical workflow is `local_e2e_passed`, `staging_e2e_passed`, explicitly deferred with approval, or accepted as a launch risk with owner, severity, mitigation, and rollback/support path
* no unresolved launch-critical dead controls or fixture-backed runtime dependencies remain
* visual QA, responsive validation, UI architecture/layout pattern/component-family/template-deviation compliance, design system compliance, preview evidence, and visual drift status are launch-ready or explicitly accepted as known risks
* launch-critical interaction contracts and stable `UI-ELEMENT-`, `ROUTE-`, and `ACTION-` references pass Stage 6 conformance validation or have accepted launch risks
* critical route, outcome, confirmation, permission-denied, recovery, mobile, accessibility, and design-system interaction behavior is launch-ready
* dropped, renamed, rerouted, or behavior-changed interactions have approved deviations or accepted launch risks tied to affected stable IDs
* monitoring checks and alert ownership are defined
* analytics events and success metrics are defined
* support, onboarding, and operational runbooks are defined
* local human-readable assessment summary exists at `Build-Plans/Stage-7/06-stage-7-summary.md`
* the summary matches canonical Stage 7 JSON outputs and identifies whether the stage is ready, needs revision, or is blocked
* critical launch blockers are resolved or explicitly accepted as known risks
* Stage 8 handoff includes telemetry, analytics, monitoring, support, incident, and watchlist sources

---

# A-Grade Workflow Compliance

Stage 7 must consume `stage_contract_profile` and `guidance_policy`.

Stage 7 output validation should reference:

```text
System-References/Schemas/stage-7-output.schema.json
```

Stage 7 must record production build proof, deployment dry-run evidence, workflow evidence review, smoke test results, rollback verification, environment verification, monitoring alert proof, and accepted launch risk evidence in:

```text
Build-Plans/Build-status/Artifact-evidence-registry.json
```

Stage 7 readiness must also record:

```json
{
  "finalization_attempt": true,
  "proposed_completion_status": "",
  "evaluated_completion_status": "",
  "handoff_mode": "next_stage",
  "schema_validation": {},
  "reference_integrity": {},
  "risk_acceptance_ledger": {},
  "revision_loops": []
}
```

Stage 7 may not use `ready_for_stage_8` until required schema validation passes, launch gate, deployment proof, workflow evidence, monitoring, analytics, support, onboarding, artifact, and accepted-risk references resolve to upstream sources, accepted high and critical launch risks are written to `Build-Plans/Build-status/Risk-acceptance-ledger.json`, and failed readiness checks are converted into revision-loop actions.

Stage 7 must reject Stage 6 handoffs that lack launch-critical workflow evidence.
Missing workflow evidence, unresolved dead controls, and unresolved fixture-backed
runtime data are launch blockers, not documentation gaps.
