---
name: global-stage-readiness-audit
description: Audit stage handoffs, schemas, references, evidence, and revision-loop readiness.
compatibility: opencode
---

# Skill — global-stage-readiness-audit

# Purpose

The `global-stage-readiness-audit` skill validates whether a stage is ready to hand off, close out, or route feedback.

It enforces:

```text
System-References/Docs/Global-Stage-Workflow-Contract.md
```

and writes a stage-specific audit result to:

```text
Build-Plans/Build-status/Stage-X-readiness-audit.json
```

---

# When To Use

Use this skill as the finalization audit for every stage completion attempt.

The calling stage must run the audit after final outputs are assembled and before it writes the final completion status. This includes failed, blocked, and revision outcomes, not only successful ready outcomes.

Use it for:

* Stage 1 before `ready_for_stage_2`
* Stage 2 before `ready_for_stage_3`
* Stage 3 before `ready_for_stage_4`
* Stage 4 before `ready_for_stage_5`
* Stage 5 before `ready_for_stage_6`
* Stage 6 before `ready_for_stage_7`
* Stage 7 before `ready_for_stage_8`
* Stage 8 before `evolution_plan_ready`

---

# Inputs

```json
{
  "stage": "",
  "stage_number": 0,
  "stage_output_directory": "",
  "required_output_files": [],
  "stage_state_file": "",
  "expected_handoff_key": "",
  "expected_next_stage": "",
  "proposed_completion_status": "",
  "finalization_attempt": true,
  "handoff_mode": "next_stage | feedback_routes | terminal",
  "existing_state": {}
}
```

---

# Executable Runner

Run the audit after final outputs are assembled:

```sh
python3 .opencode/Skills/global-stage-readiness-audit/scripts/run_readiness_audit.py \
  --stage 6 \
  --proposed-status ready_for_stage_7
```

The runner uses `workflow_validation.py` to execute the repository's JSON Schema subset and resolve stable IDs plus file-and-JSON-Pointer references. It writes the stage audit and updates global workflow state. A non-ready result exits nonzero after preserving the failed audit and revision loops.

---

# Audit Checks

For Stage 5 format `2.0`, audit `00-stage-context.json`, all eight manifest
entries and their declared data paths, and `09-stage-manifest.json`. Completion
and handoff checks read only the manifest. Reject partial v2 packages, duplicate
artifact IDs, inconsistent manifest entries, copied canonical collections, or
`schemas_valid: true` without evidence that validation executed. Resolve legacy
self-contained Stage 5 files through the read-only compatibility resolver.

Reference-integrity checks must resolve ticket stable IDs against the actual
Stage 1-4 inputs and fully navigate file-plus-JSON-Pointer references. Also
validate shared-context `risk_refs`, assigned-agent scope coverage, and batch
execution-wave dependency order.

Validate:

* required output directory exists
* required output files exist
* Stage 5-8 local assessment summary exists for every finalization attempt
* Stage 5-8 local assessment summary matches canonical JSON outputs and does not add downstream handoff requirements
* Stage 5 declares workflow proof obligations for launch-critical user workflows
* Stage 6 provides workflow outcome evidence for launch-critical user workflows
* Stage 6 records no unresolved dead controls on launch-critical visible actions
* Stage 6 records no unresolved fixture-backed runtime data dependencies on launch-critical screens
* Stage 7 rejects Stage 6 handoffs that lack launch-critical workflow evidence
* output files are parseable JSON when applicable
* output files contain `stage` and `status`
* completion status exists
* proposed completion status exists for the finalization attempt
* completion status maps to the global completion status model
* expected handoff or feedback-route object exists for the active handoff mode
* next-stage handoffs contain source stage, target stage, required files, readiness, blockers, accepted risks, traceability refs, and completion status
* Stage 8 feedback routes contain source signal refs, recommended target stage, evidence refs, owner or next action for critical findings, and whether a new stage cycle is created
* risks are present or explicitly marked not applicable
* assumptions are present or explicitly marked not applicable
* traceability IDs are present or missing traceability is justified
* stage contract profile requirements are checked when a profile is present
* referenced schema files exist and required outputs are checked against them
* artifact references are present when evidence-backed claims, previews, builds, validation results, or deployment proofs are required
* `Build-Plans/Build-status/Artifact-evidence-registry.json` exists when artifact evidence is required
* `Build-Plans/Build-status/Risk-acceptance-ledger.json` exists when progression depends on accepted risk
* cross-stage references are present, unique, and resolvable when used by required outputs
* frontend-facing work preserves UI blueprint, UI architecture template, page archetype, layout pattern, component-family, template-deviation, visual spec, visual style reference, and design system continuity when applicable
* blockers have next actions and failed checks produce revision-loop records

---

# Output

Write:

```text
Build-Plans/Build-status/Stage-X-readiness-audit.json
```

using this structure:

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

Allowed `audit_status` values:

```text
passed
passed_with_warnings
failed
blocked
```

---

# Global Workflow State Update

After writing the stage audit, update:

```text
Build-Plans/Build-status/Global-workflow-state.json
```

Record:

* stage audit status
* global status
* current stage
* blockers
* revision loops
* next recommended action

---

# Completion Rule

The audit file must be written for every finalization attempt, including attempts that resolve to `needs_current_stage_revision`, `needs_prior_stage_revision`, or `blocked`.

If `ready_for_next_stage` is false, the calling stage command must not use its ready completion status.

For Stage 7, the ready completion status is `ready_for_stage_8`.

For Stage 8, `ready_for_next_stage` means the evolution package is ready to close the current cycle or create routed prior-stage feedback. Stage 8 does not hand off to Stage 9. Its audit must evaluate `prior_stage_feedback` and feedback routes when live findings route work back to earlier stages.

The audit must fail or block when required schema validation, stage profile requirements, artifact evidence, risk acceptance entries, reference integrity, revision-loop ownership, or visual continuity proof is missing for a stage that depends on those contracts.

When the audit fails, write revision-loop records that identify:

* owning stage
* owning output
* owning skill or command
* blocking issue
* required change
* recommended action
* whether accepted risk is allowed

The calling stage must instead set one of:

```text
needs_current_stage_revision
needs_prior_stage_revision
blocked
```
