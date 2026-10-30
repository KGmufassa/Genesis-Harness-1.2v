# Global Stage Readiness Audit

# Purpose

The global stage readiness audit verifies that a stage is ready to hand off to the next stage according to:

```text
System-References/Docs/Global-Stage-Workflow-Contract.md
```

This audit is required at the end of every stage finalization attempt, before the stage writes its final completion status to shared state.

The audit must run for ready, revision-needed, prior-stage-revision, and blocked outcomes.

---

# Audit Skill

Use:

```text
global-stage-readiness-audit
```

Executable command:

```sh
python3 .opencode/Skills/global-stage-readiness-audit/scripts/run_readiness_audit.py \
  --stage <1-8> \
  --proposed-status <stage-status>
```

The audit validates:

* required output files exist
* output files follow the expected stage schemas
* completion status exists
* global completion status is mapped
* handoff object exists
* handoff contains enough structured data for the next stage
* risks are recorded
* assumptions are recorded
* blockers are explicit
* traceability IDs exist or missing traceability is justified
* artifact references are recorded when evidence exists
* structural UI architecture, visual, and design continuity checks pass when the stage contains frontend-facing work
* stage contract profile requirements are satisfied
* schema validation results are recorded for required outputs
* accepted risks are recorded in the risk acceptance ledger when progression depends on accepted risk
* cross-stage references are valid, not duplicated, and not stale
* failed readiness conditions produce revision-loop records with owning stage, output, skill, and next action
* Stage 8 feedback routes are owned, evidence-backed, and routed to earlier stages when live findings create a new cycle

---

# Required Audit Output

Each stage must write:

```text
Build-Plans/Build-status/Stage-X-readiness-audit.json
```

Where `X` is the stage number.

Example:

```text
Build-Plans/Build-status/Stage-5-readiness-audit.json
```

---

# Audit Output Schema

```json
{
  "stage": "",
  "command": "global-stage-readiness-audit",
  "audit_status": "pending",
  "finalization_attempt": true,
  "proposed_completion_status": "",
  "evaluated_completion_status": "",
  "handoff_mode": "next_stage | feedback_routes | terminal",
  "global_workflow_contract": "System-References/Docs/Global-Stage-Workflow-Contract.md",
  "required_files_present": false,
  "local_assessment_summary": {
    "required": false,
    "path": "",
    "present": false,
    "matches_canonical_outputs": false,
    "assessment": "",
    "blocking_gaps": []
  },
  "workflow_outcome_evidence": {
    "required": false,
    "workflow_evidence_present": false,
    "launch_critical_workflows_checked": [],
    "launch_critical_workflows_passed": false,
    "dead_controls_detected": [],
    "fixture_runtime_dependencies": [],
    "blocking_workflow_gaps": []
  },
  "schemas_valid": false,
  "completion_status_present": false,
  "global_status_mapped": false,
  "handoff_present": false,
  "handoff_usable": false,
  "feedback_routes_present": false,
  "feedback_routes_usable": false,
  "risks_recorded": false,
  "assumptions_recorded": false,
  "traceability_present": false,
  "artifacts_recorded": false,
  "stage_contract_profile": {
    "profile_id": "",
    "profile_requirements_checked": false,
    "missing_profile_requirements": []
  },
  "schema_validation": {
    "schema_refs": [],
    "validated_files": [],
    "schema_errors": [],
    "schemas_valid": false,
    "validated_at": "",
    "validator": "",
    "blocking": true
  },
  "reference_integrity": {
    "checked_refs": [],
    "missing_refs": [],
    "orphaned_refs": [],
    "stale_refs": [],
    "duplicate_ids": [],
    "integrity_status": "passed | passed_with_warnings | failed",
    "blocking_ref_errors": []
  },
  "artifact_evidence_registry": {
    "registry_path": "Build-Plans/Build-status/Artifact-evidence-registry.json",
    "required": false,
    "required_artifacts_present": false,
    "missing_artifacts": []
  },
  "risk_acceptance_ledger": {
    "ledger_path": "Build-Plans/Build-status/Risk-acceptance-ledger.json",
    "required": false,
    "accepted_risks_present": false,
    "missing_risk_acceptance_entries": [],
    "expired_or_unowned_risks": []
  },
  "revision_loops": [],
  "feedback_route_audit": {
    "required": false,
    "routes_checked": [],
    "missing_route_owners": [],
    "missing_route_actions": [],
    "missing_route_evidence": [],
    "critical_routes_blocking": [],
    "creates_new_stage_cycle": false
  },
  "visual_design_continuity": {
    "required": false,
    "ui_blueprint_refs_present": false,
    "visual_spec_refs_present": false,
    "visual_reference_refs_present": false,
    "design_system_refs_present": false,
    "visual_acceptance_criteria_mapped": false,
    "visual_reference_compliance_recorded": false,
    "preview_or_visual_qa_evidence_present": false,
    "design_system_compliance_recorded": false,
    "visual_drift_status_recorded": false,
    "blocking_visual_gaps": []
  },
  "blocking_gaps": [],
  "warnings": [],
  "next_actions": [],
  "ready_for_next_stage": false
}
```

Allowed audit statuses:

```text
passed
passed_with_warnings
failed
blocked
```

---

# Readiness Rule

A stage may use a stage-specific ready status only when:

```text
ready_for_next_stage = true
```

Stage 8 is terminal and cyclical. For Stage 8, `ready_for_next_stage = true` means the evolution package is ready to close the current cycle or create routed work for earlier stages through `prior_stage_feedback`; it does not imply a Stage 9 handoff.

For frontend-facing work, the audit must also enforce the structural UI architecture, visual, and design continuity rules in:

```text
System-References/Docs/Global-Stage-Workflow-Contract.md
```

For launch-critical user workflows, the audit must verify workflow outcome
evidence. Contract-only work, API-only work, static UI, fixture-backed runtime
pages, successful builds, and unresolved dead controls do not satisfy readiness.

For evidence-backed readiness claims, the audit must verify related evidence exists in:

```text
Build-Plans/Build-status/Artifact-evidence-registry.json
```

For accepted-risk readiness claims, the audit must verify risk acceptance entries exist in:

```text
Build-Plans/Build-status/Risk-acceptance-ledger.json
```

For every failed or blocked readiness condition, the audit must create a revision-loop object with the owning stage, output, skill, required change, and whether accepted risk is allowed.

If the audit fails, the stage must set completion status to one of:

```text
needs_current_stage_revision
needs_prior_stage_revision
blocked
```

The failed or blocked audit file must still be written and must include `blocking_gaps`, `revision_loops`, and `next_actions`.

---

# Global Workflow State Update

After each audit, update:

```text
Build-Plans/Build-status/Global-workflow-state.json
```

The workflow state must record:

* stage status
* audit result
* current stage
* blockers
* revision loops
* next recommended action
