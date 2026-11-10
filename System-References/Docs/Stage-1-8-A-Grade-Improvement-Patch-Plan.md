# Stage 1-8 A-Grade Improvement Patch Plan

# Purpose

This review document defines the planned patches needed to raise the full Stage 1-8 workflow from the current B-grade assessment to an A-grade workflow across planning, implementation, launch, and post-launch evolution.

The goal is not to restructure the stage architecture. The current architecture is sound.

The goal is to improve:

* evidence quality
* verification rigor
* workflow adaptability
* readiness audit reliability
* launch proof
* post-launch feedback routing
* implementation traceability

---

# Current Health Baseline

Assessment update: **2026-11-09**. Patches 13–19 retain their historical 2026-11-08 implementation record.

| Measure | Verified Status |
| --- | --- |
| Original diagnostic assessment | 84 / 100 — B, retained as the pre-patch baseline |
| Current health assessment | **87 / 100 — B**; four readiness gaps and one contract-test regression remain |
| Patches 13–19 | **Implemented and regression-tested** |
| Patch 20 | **Runbook prepared; real-app execution pending application selection/access** |
| Repository tests, latest health check | **132 executed: 131 passed; 1 error; 0 assertion failures** |
| Seed/registry schema checks | **6 passed; 0 failed** |
| Original confirmed findings | **8 addressed by executable controls and regression tests** |
| Skill packages | **90 compliant packages** |
| Actual application stages | Baseline remains `not_started`; no live pilot or production evidence claimed |

See `Stage-1-8-Improvement-Implementation-Record.md` for the change inventory, exact contract additions, test evidence, and remaining work. The HTML edition mirrors this implementation status.

The current health check assesses the harness at 87/B (workflow design 94 at 30%, enforcement 84 at 50%, verification 85 at 20%; weighted 87.2). The prior 88/B grade is historical. The original eight findings remain addressed; four readiness gaps map to planned patches 21–24, and a new contract-test regression maps to Patch 25. Stronger enforcement, a green regression run and supervised real-app evidence are still required; counts alone do not award a grade.

---

# Latest Diagnostic Run

- Reporting-only check on 2026-11-09: all eight stage contracts and live controls reviewed; all four prior open findings re-confirmed with passing synthetic baselines.
- The complete collector ran 132 tests (131 passed, one error), six passing seed/registry checks, 90 compliant skill packages, 17 syntax checks and 37 JSON checks. No timeouts or skipped suites.
- New Stage 4 standards/page/revision controls were present before the check. No fixes or stage advancement occurred during this reporting run.

## Historical Implementation Work — Patches 13–19

- Preserved unrelated in-progress edits, the eight-stage architecture, and the approved Stage 4 waitlist placement.
- Added regression coverage for the confirmed gaps and successful controls, then implemented the missing checks.
- Replaced the generic Stage 5 integration fixture with an actual normalized v2 package and recorded runtime/launch evidence fixtures.
- Verified all repository tests, schema vocabulary coverage, stage-specific seeds, metadata, script syntax, and patch whitespace.
- Saved implementation details in `Stage-1-8-Improvement-Implementation-Record.md`; the original health report retains the pre-patch diagnostic as historical evidence.

## Verified Improvements

- Active profiles, current-stage decisions, Stage 2 research confidence/evidence, and supported approval gates are evaluated.
- The global audit invokes normalized package, reference, scope, wave, and completion-definition validators.
- Failed persistence, missing current-stage outcomes, incomplete visual checks, missing launch proof, and unverified artifacts block readiness.
- Malformed canonical/registry/ledger/schema inputs produce failed audit diagnostics; damaged global state is preserved.
- Feedback routes have valid destinations, owned actions, verified high/critical evidence, and accurate cycle reporting.
- Feature/platform, selected-stack, and deployment fingerprints detect stale approvals and waitlist decisions.
- Patch 20 has a separate supervised runbook; it has not been represented as a completed real-app run.

## Confirmed Findings Addressed

| Finding | Implemented Resolution | Patch | Status |
| --- | --- | --- | --- |
| RISK-HEALTH-001 | UX blueprint seed is an array; stage-specific seed regression checks pass. | 13 | Verified |
| RISK-HEALTH-002 | Shared validator enforces JSON-aware uniqueness and used vocabulary, including reference siblings. | 13 | Verified |
| RISK-HEALTH-003 | Actual profile requirements and Stage 2 evidence/confidence are checked. | 14 | Verified |
| RISK-HEALTH-004 | Normalized manifest paths, IDs, schemas, pointers, package contracts, and handoffs are checked. | 15 | Verified |
| RISK-HEALTH-005 | Failed persistence and missing required current-stage workflow evidence block. | 16 | Verified |
| RISK-HEALTH-006 | All six launch-proof categories require passed, verified evidence or an expressly allowed scoped exception. | 16 | Verified |
| RISK-HEALTH-007 | Malformed input produces durable failed audit/revision output; damaged source/global state is preserved. | 17 | Verified |
| RISK-HEALTH-008 | Invalid feedback destinations and missing high/critical proof block; route audit fields reflect actual evaluation. | 18 | Verified |

---

# Latest Health Check

- Assessment date: **2026-11-09**; result **87/100 — B**. The full test run recorded **132 executed: 131 passed; 1 error**; all six seed/registry schemas pass, all 90 skills pass metadata checks, and baseline stage status is unchanged.
- The collector exits 1 because the Stage 4 phase-heading assertion raises `ValueError`; no code is fixed during this reporting check. Verification maturity is reduced from 88 to 85; other dimension scores are unchanged.
- Reproduced all four current readiness gaps and added a page-edit variant to RISK-HEALTH-012. The new test regression is RISK-HEALTH-013. Preserve original closure and implementation history.
- Stage 4 now has 27 page-specification tests within 87 passing readiness tests; the separate Stitch contract suite has three passes and one error. The real-app pilot remains pending.
- The HTML edition is regenerated from reviewed sources: 25 patches, six pending (20–25), valid anchors/local links and JavaScript syntax. Browser visual preview was unavailable because browser host/native permissions were unavailable; responsive/print checks are static only.

| Open Finding | Owner | Planned Patch | Priority |
| --- | --- | --- | --- |
| RISK-HEALTH-009 — General implementation failures | Stage 6 | 21 | High |
| RISK-HEALTH-010 — Feature-to-ticket coverage | Stage 5 | 22 | High |
| RISK-HEALTH-011 — Complete concrete stack | Stage 3 | 23 | High |
| RISK-HEALTH-012 — Downstream scope/page approval freshness | Stages 5–7 | 24 | High |
| RISK-HEALTH-013 — Stage 4 contract-test heading drift | Stage 4 tests/documentation | 25 | Medium |

---

# Patch Overview

| Patch | Name | Primary Impact | Priority |
| --- | --- | --- | --- |
| 1 | Artifact Evidence Registry | Stages 5-7 verification proof | Critical |
| 2 | Stage Contract Profiles | Adaptive workflow depth | Critical |
| 3 | Machine-Checkable Schema Validation | Readiness audit reliability | High |
| 4 | Stage 2 Evidence Quality Upgrade | Validation confidence | High |
| 5 | Stage 7 Deployment Proof Upgrade | Launch readiness rigor | High |
| 6 | Stage 8 Feedback Routing Upgrade | Continuous evolution quality | High |
| 7 | Complexity-Based Interactive Guidance | Reduces workflow friction | Medium |

Patch foundation status after the implementation update:

| Patch | Status | Current Coverage |
| --- | --- | --- |
| 1 | Implemented with evidence integration | Registry IDs, verified status, and usable proof locations are checked. |
| 2 | Implemented with profile evaluation | Active outputs, supported layers, and explicit approval pointers are evaluated. |
| 3 | Implemented for used vocabulary | Stage-specific schema/seed checks, uniqueness, references, and unsupported-keyword regressions pass. |
| 4 | Implemented with Stage 2 gates | Assumption evidence, confidence ceilings/thresholds, and unresolved critical issues are checked. |
| 5 | Implemented with launch gates | Required result objects and verified references block incomplete launch readiness. |
| 6 | Implemented with destination validation | Feedback ownership, targets, optional domain routing, high/critical evidence, and cycle reporting execute. |
| 7 | Contract and shape implemented | Interview behavior remains agent-driven; unsupported executable requirements block. |
| 8 | Implemented with stage-specific results | Outputs, canonical state, registries, and normalized package schemas are evaluated. |
| 9 | Implemented with scoped exception checks | Authority, approval evidence, current-stage scope, and expiry govern allowed exceptions. |
| 10 | Implemented with package integration | Stable IDs, JSON pointers, manifest paths, and required pre-code handoffs are checked. |
| 11 | Implemented with malformed-input recovery | Failed audit and revision output survive supported input failures; damaged global state is preserved. |
| 12 | Implemented | Existing canonical names and normalized ownership remain intact. |

Patches 1–12 below retain their original design descriptions. Patches 13–19 implement the enforcement corrections; Patch 20 still needs real application evidence. These labels do not imply general Draft 2020-12 compliance, fresh network validation, or completed production validation.

Original foundation implementation order (historical):

```text
1. Artifact Evidence Registry
2. Stage Contract Profiles
3. Machine-Checkable Schema Validation
4. Stage 2 Evidence Quality Upgrade
5. Stage 7 Deployment Proof Upgrade
6. Stage 8 Feedback Routing Upgrade
7. Complexity-Based Interactive Guidance
```

---

# Follow-Up Patch Overview

Patches 8–12 describe the original follow-up design. Their current status is qualified above; the earlier projected `96-98 / 100` result is not a verified current grade.

| Patch | Name | Primary Impact | Priority |
| --- | --- | --- | --- |
| 8 | Stage-Level Schema Validation Results | Makes schema validation visible in every stage handoff | High |
| 9 | Risk Acceptance Ledger | Prevents accepted risks from becoming invisible downstream | High |
| 10 | Cross-Stage Reference Integrity Audit | Prevents broken IDs and weak traceability across handoffs | High |
| 11 | Readiness Failure Revision Loop | Makes failed readiness audits actionable and stage-routable | High |
| 12 | Artifact Field Standardization | Removes ambiguity around `expected_artifacts` and registry references | Medium |

Original follow-up implementation order (historical):

```text
8. Stage-Level Schema Validation Results
9. Risk Acceptance Ledger
10. Cross-Stage Reference Integrity Audit
11. Readiness Failure Revision Loop
12. Artifact Field Standardization
```

---

# Patch 1 — Artifact Evidence Registry

# Objective

Create a shared evidence registry that records proof generated during planning, implementation, validation, preview, launch readiness, and deployment checks.

This improves Stage 6 validation, Stage 7 launch readiness, and global readiness audits.

---

# New Output

```text
Build-Plans/Build-status/Artifact-evidence-registry.json
```

---

# Proposed Schema

```json
{
  "registry_version": "1.0.0",
  "artifacts": [
    {
      "artifact_id": "",
      "type": "test_output | screenshot | preview_url | build_log | validation_report | deployment_evidence | launch_check | telemetry_source",
      "related_stage": "",
      "related_stage_output": "",
      "related_ticket_ids": [],
      "related_validation_ids": [],
      "related_agent_ids": [],
      "path_or_url": "",
      "status": "pending | passed | failed | blocked | accepted_risk",
      "confidence": "low | medium | high",
      "created_by": "",
      "created_at": "",
      "notes": ""
    }
  ]
}
```

---

# Files To Update

Review docs:

```text
System-References/Docs/Global-Stage-Workflow-Contract.md
System-References/Docs/Global-Stage-Readiness-Audit.md
System-References/Docs/Stage-5-development-orchestration-draft.md
System-References/Docs/Stage-6-implementation-validation-draft.md
System-References/Docs/Stage-7-launch-operationalization-draft.md
```

Skills:

```text
.opencode/Skills/stage-5-development-orchestration/skill.md
.opencode/Skills/build-ticket-generation/skill.md
.opencode/Skills/stage-6-implementation-validation/skill.md
.opencode/Skills/implementation-execution/skill.md
.opencode/Skills/validation-execution/skill.md
.opencode/Skills/system-health-synthesis/skill.md
.opencode/Skills/stage-7-launch-operationalization/skill.md
.opencode/Skills/launch-readiness-validation/skill.md
```

---

# Required Behavior

Stage 5 should define expected artifacts per ticket.

Stage 6 should record actual artifacts generated by implementation, validation, repair, preview, visual QA, and regression checks.

Stage 7 should consume artifact evidence before launch readiness is accepted.

Global readiness audits should verify artifact evidence exists when a stage claims validation, preview, build, deployment, or launch readiness.

---

# Acceptance Criteria

* Artifact registry schema exists in the docs.
* Stage 5 tickets can declare expected artifacts.
* Stage 6 outputs reference generated artifacts.
* Stage 7 launch readiness checks artifact evidence.
* Global readiness audit includes artifact evidence checks.

---

# Patch 2 — Stage Contract Profiles

# Objective

Make the stage workflow adaptive based on product type and complexity so simple apps are not over-planned and complex apps still receive deep planning.

---

# Proposed Profiles

```text
simple-crud-app
frontend-heavy-app
ai-heavy-app
marketplace-app
internal-tool
enterprise-saas
mobile-first-app
compliance-sensitive-app
integration-heavy-app
data-heavy-app
```

---

# Proposed Shared Object

```json
{
  "stage_contract_profile": {
    "profile_id": "",
    "profile_name": "",
    "app_type": "",
    "complexity_level": "low | medium | high | critical",
    "guidance_depth": "minimal | standard | detailed | exhaustive",
    "required_stage_depth": {
      "stage_1": "",
      "stage_2": "",
      "stage_3": "",
      "stage_4": "",
      "stage_5": "",
      "stage_6": "",
      "stage_7": "",
      "stage_8": ""
    },
    "required_validation_layers": [],
    "optional_outputs": [],
    "required_outputs": [],
    "skip_allowed_outputs": [],
    "approval_gates": []
  }
}
```

---

# Files To Update

Review docs:

```text
System-References/Docs/Global-Stage-Workflow-Contract.md
System-References/Docs/Stage-1-product-initialization-draft.md
System-References/Docs/Stage-2-architect.md
System-References/Docs/Stage-3-system-architecture-draft.md
System-References/Docs/Stage-4-ux-interaction-architecture-draft.md
System-References/Docs/Stage-5-development-orchestration-draft.md
System-References/Docs/Stage-6-implementation-validation-draft.md
System-References/Docs/Stage-7-launch-operationalization-draft.md
System-References/Docs/Stage-8-post-launch-evolution-draft.md
```

Skills:

```text
.opencode/Skills/Stage-1-product-initialization/skill.md
.opencode/Skills/stage-2-research-and-validation/skill.md
.opencode/Skills/stage-3-system-architecture/skill.md
.opencode/Skills/stage-4-ux-interaction-architecture/skill.md
.opencode/Skills/stage-5-development-orchestration/skill.md
.opencode/Skills/stage-6-implementation-validation/skill.md
.opencode/Skills/stage-7-launch-operationalization/skill.md
.opencode/Skills/stage-8-post-launch-evolution/skill.md
```

---

# Required Behavior

Stage 1 should identify or infer the initial contract profile.

Each stage should adjust required depth based on the profile.

The global readiness audit should verify that the stage completed the requirements for the selected profile, not a one-size-fits-all checklist.

---

# Acceptance Criteria

* Contract profile object exists in global workflow docs.
* Stage 1 can initialize the profile.
* Stages 2-8 consume the profile.
* Readiness audits account for profile-specific requirements.
* Low-complexity apps can move faster without losing required safety gates.

---

# Patch 3 — Machine-Checkable Schema Validation

# Objective

Turn documented JSON output expectations into machine-checkable schema expectations.

This improves readiness audit reliability and prevents malformed handoffs.

---

# New Folder

```text
System-References/Schemas/
```

---

# Proposed Schema Files

```text
stage-1-output.schema.json
stage-2-output.schema.json
stage-3-output.schema.json
stage-4-output.schema.json
stage-5-output.schema.json
stage-6-output.schema.json
stage-7-output.schema.json
stage-8-output.schema.json
artifact-evidence-registry.schema.json
global-readiness-audit.schema.json
```

---

# Files To Update

Review docs:

```text
System-References/Docs/Global-Stage-Readiness-Audit.md
System-References/Docs/Global-Stage-Workflow-Contract.md
```

All stage review docs should reference their schema expectations.

Skills:

```text
All stage command skills
global-stage-readiness-audit skill, if present or later created
```

---

# Required Behavior

Each stage should declare which schema validates its outputs.

The readiness audit should record:

```json
{
  "schema_validation": {
    "schema_refs": [],
    "validated_files": [],
    "schema_errors": [],
    "schemas_valid": false
  }
}
```

---

# Acceptance Criteria

* Schema folder is documented.
* Stage outputs reference schema files.
* Readiness audit includes schema validation results.
* Missing or invalid schema results can block readiness.

---

# Patch 4 — Stage 2 Evidence Quality Upgrade

# Objective

Improve validation reliability by making evidence quality, freshness, source type, confidence rationale, and inference boundaries explicit.

---

# Proposed Evidence Object

```json
{
  "evidence_id": "",
  "claim_or_assumption_id": "",
  "source_type": "primary | secondary | user_provided | inferred | unavailable",
  "source_url": "",
  "source_date": "",
  "freshness": "current | recent | stale | unknown",
  "evidence_quality": "none | low | medium | high",
  "confidence_effect": "increase | decrease | neutral",
  "confidence_delta": 0.0,
  "summary": "",
  "is_inference": false,
  "limitations": [],
  "requires_external_research": false
}
```

---

# Files To Update

Review docs:

```text
System-References/Docs/Stage-2-architect.md
System-References/Docs/Global-Stage-Workflow-Contract.md
```

Skills:

```text
.opencode/Skills/stage-2-research-and-validation/skill.md
.opencode/Skills/assumption-analysis/skill.md
.opencode/Skills/market-and-competitive-validation/skill.md
.opencode/Skills/technical-and-operational-validation/skill.md
.opencode/Skills/business-and-scalability-validation/skill.md
.opencode/Skills/validation-synthesis/skill.md
```

---

# Required Behavior

Every validated assumption should include evidence metadata.

Unsupported claims should remain assumptions.

Architecture-critical assumptions should require at least medium evidence quality or an explicit accepted risk.

Stage 2 should distinguish:

```text
evidence-backed finding
inference
unsupported assumption
critical unknown
```

---

# Acceptance Criteria

* Evidence quality rules are documented.
* Stage 2 outputs include evidence metadata.
* Critical assumptions cannot be marked validated without evidence or accepted risk.
* Stage 3 handoff receives evidence quality and confidence rationale.

---

# Patch 5 — Stage 7 Deployment Proof Upgrade

# Objective

Strengthen launch readiness by requiring deployment and production-readiness proof instead of only readiness descriptions.

---

# Proposed Deployment Proof Fields

```json
{
  "deployment_proof": {
    "production_build_artifact": "",
    "deployment_dry_run_result": {},
    "smoke_test_results": [],
    "rollback_test_result": {},
    "environment_verification": {},
    "monitoring_alert_test": {},
    "release_blockers": [],
    "accepted_launch_risks": []
  }
}
```

---

# Files To Update

Review docs:

```text
System-References/Docs/Stage-7-launch-operationalization-draft.md
System-References/Docs/Global-Stage-Workflow-Contract.md
System-References/Docs/Global-Stage-Readiness-Audit.md
```

Skills:

```text
.opencode/Skills/stage-7-launch-operationalization/skill.md
.opencode/Skills/launch-readiness-validation/skill.md
.opencode/Skills/deployment-framework-planning/skill.md
.opencode/Skills/launch-operationalization-synthesis/skill.md
```

---

# Required Behavior

Stage 7 should require production build proof, deployment dry-run evidence, smoke test results, rollback proof, and environment verification when launch readiness claims depend on them.

Missing proof should become a launch blocker unless accepted as a known risk.

---

# Acceptance Criteria

* Launch readiness output includes deployment proof.
* Stage 7 completion gate checks deployment proof.
* Global readiness audit checks launch proof for Stage 7.
* Stage 8 receives launch proof references in the handoff.

---

# Patch 6 — Stage 8 Feedback Routing Upgrade

# Objective

Make Stage 8 a true evolution engine by routing live-product findings back to the correct earlier stage.

---

# Proposed Routing Rules

| Signal | Route |
| --- | --- |
| Retention, positioning, or product-market issue | Stage 1 or Stage 2 |
| Invalid validated assumption | Stage 2 |
| Performance, API, infrastructure, security, or scalability issue | Stage 3 |
| UX confusion, navigation friction, accessibility issue | Stage 4 |
| Ticket sequencing, agent, or test coverage issue | Stage 5 |
| Bug, regression, repair, or validation failure | Stage 6 |
| Support, monitoring, onboarding, or operational issue | Stage 7 |
| Roadmap expansion or optimization opportunity | Stage 8 |

---

# Proposed Feedback Object

```json
{
  "feedback_route_id": "",
  "source_signal_ids": [],
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

# Files To Update

Review docs:

```text
System-References/Docs/Stage-8-post-launch-evolution-draft.md
System-References/Docs/Global-Stage-Workflow-Contract.md
```

Skills:

```text
.opencode/Skills/stage-8-post-launch-evolution/skill.md
.opencode/Skills/telemetry-analysis/skill.md
.opencode/Skills/operational-optimization/skill.md
.opencode/Skills/ai-improvement-planning/skill.md
.opencode/Skills/roadmap-evolution-planning/skill.md
.opencode/Skills/scalability-evolution-planning/skill.md
.opencode/Skills/post-launch-evolution-synthesis/skill.md
```

---

# Required Behavior

Stage 8 should not only produce evolution plans. It should classify findings and decide whether to:

* optimize within Stage 8
* create a new roadmap item
* route the issue to an earlier stage
* open a new validation cycle
* mark a live-product risk

---

# Acceptance Criteria

* Stage 8 outputs include feedback routes.
* Stage 8 synthesis can create prior-stage feedback objects.
* Global workflow contract documents live feedback loops.
* Stage 8 completion gate requires unresolved critical feedback routes to have owners.

---

# Patch 7 — Complexity-Based Interactive Guidance

# Objective

Reduce user friction by scaling question depth to app complexity and stage risk.

---

# Proposed Shared Guidance Object

```json
{
  "guidance_policy": {
    "complexity_level": "low | medium | high | critical",
    "guidance_depth": "minimal | standard | detailed | exhaustive",
    "ask_threshold": "only_blockers | material_decisions | important_tradeoffs | all_uncertainties",
    "default_inference_allowed": true,
    "approval_required_for": [],
    "max_questions_per_turn": 3
  }
}
```

---

# Files To Update

Review docs:

```text
System-References/Docs/Global-Stage-Workflow-Contract.md
All Stage 1-8 review docs
```

Skills:

```text
All Stage 1-8 command skills
```

---

# Required Behavior

Each stage should use the guidance policy before asking the user questions.

Low-complexity apps should use fewer pauses and more recorded assumptions.

High-risk apps should ask more confirmation questions and block more often.

---

# Acceptance Criteria

* Global guidance policy is documented.
* Each stage command consumes guidance policy.
* Interactive guidance rules reference complexity level and guidance depth.
* Readiness audits can identify unresolved guidance blockers.

---

# Patch 8 — Stage-Level Schema Validation Results

# Objective

Require every stage to write schema validation results into its readiness/audit output so schema checks are visible at the stage level, not only in the global audit contract.

This closes the gap where stages reference schema files but do not explicitly require a machine-readable validation result in the stage review doc.

---

# Proposed Shared Object

```json
{
  "schema_validation": {
    "schema_refs": [],
    "validated_files": [],
    "schema_errors": [],
    "schemas_valid": false,
    "validated_at": "",
    "validator": "",
    "blocking": true
  }
}
```

---

# Files To Update

Review docs:

```text
System-References/Docs/Stage-1-product-initialization-draft.md
System-References/Docs/Stage-2-architect.md
System-References/Docs/Stage-3-system-architecture-draft.md
System-References/Docs/Stage-4-ux-interaction-architecture-draft.md
System-References/Docs/Stage-5-development-orchestration-draft.md
System-References/Docs/Stage-6-implementation-validation-draft.md
System-References/Docs/Stage-7-launch-operationalization-draft.md
System-References/Docs/Stage-8-post-launch-evolution-draft.md
System-References/Docs/Global-Stage-Readiness-Audit.md
```

Skills:

```text
All Stage 1-8 command skills
.opencode/Skills/global-stage-readiness-audit/skill.md
```

---

# Required Behavior

Each stage must include schema validation results before using a ready completion status.

The readiness audit must block progression when:

* required schema refs are missing
* required stage output files were not validated
* schema errors exist for launch-critical or handoff-critical outputs
* `schemas_valid` is false and no accepted exception exists

---

# Acceptance Criteria

* Every stage review doc includes the `schema_validation` object.
* Every stage completion gate requires schema validation before ready status.
* Global readiness audit checks stage-level schema validation results.
* Schema failures produce concrete next actions.

---

# Patch 9 — Risk Acceptance Ledger

# Objective

Create a durable ledger for accepted risks so risks that are allowed to pass a stage remain visible to downstream stages.

This prevents accepted risk from becoming hidden once a stage completes.

---

# New Output

```text
Build-Plans/Build-status/Risk-acceptance-ledger.json
```

---

# Proposed Schema

```json
{
  "ledger_version": "1.0.0",
  "accepted_risks": [
    {
      "risk_id": "",
      "source_stage": "",
      "source_output": "",
      "risk": "",
      "severity": "low | medium | high | critical",
      "accepted_by": "",
      "accepted_at": "",
      "acceptance_reason": "",
      "mitigation": "",
      "owner_stage": "",
      "downstream_visibility": [],
      "revisit_trigger": "",
      "expires_or_recheck_at": "",
      "status": "active | mitigated | expired | superseded"
    }
  ]
}
```

---

# Files To Update

Review docs:

```text
System-References/Docs/Global-Stage-Workflow-Contract.md
System-References/Docs/Global-Stage-Readiness-Audit.md
System-References/Docs/Stage-2-architect.md
System-References/Docs/Stage-3-system-architecture-draft.md
System-References/Docs/Stage-5-development-orchestration-draft.md
System-References/Docs/Stage-6-implementation-validation-draft.md
System-References/Docs/Stage-7-launch-operationalization-draft.md
System-References/Docs/Stage-8-post-launch-evolution-draft.md
```

Skills:

```text
All stage command skills that can accept risk
.opencode/Skills/global-stage-readiness-audit/skill.md
```

---

# Required Behavior

Any stage that allows progression with an accepted risk must create or update a risk ledger entry.

The entry must include:

* severity
* accepting owner
* rationale
* mitigation
* downstream stages that must see the risk
* revisit trigger
* expiry or recheck condition

Critical accepted risks must always appear in the next stage handoff.

---

# Acceptance Criteria

* Risk acceptance ledger output is documented.
* Accepted risks cannot be silent completion exceptions.
* Downstream handoffs include active high and critical accepted risks.
* Readiness audit checks whether accepted risks have owners and revisit triggers.

---

# Patch 10 — Cross-Stage Reference Integrity Audit

# Objective

Add a reference integrity check that validates IDs passed between stages.

This ensures downstream stages do not depend on broken references, missing IDs, stale ticket links, or orphaned artifacts.

---

# Proposed Reference Integrity Object

```json
{
  "reference_integrity": {
    "checked_refs": [],
    "missing_refs": [],
    "orphaned_refs": [],
    "stale_refs": [],
    "duplicate_ids": [],
    "integrity_status": "passed | passed_with_warnings | failed",
    "blocking_ref_errors": []
  }
}
```

---

# Files To Update

Review docs:

```text
System-References/Docs/Global-Stage-Workflow-Contract.md
System-References/Docs/Global-Stage-Readiness-Audit.md
All Stage 1-8 review docs
```

Skills:

```text
.opencode/Skills/global-stage-readiness-audit/skill.md
All Stage 1-8 command skills
```

---

# Required Behavior

The readiness audit should validate references such as:

```text
USER-*
WORKFLOW-*
CAP-*
FEATURE-*
BOUNDARY-*
DEP-*
RISK-*
ASSUMPTION-*
SERVICE-*
ENTITY-*
API-*
SCREEN-*
PAGE-*
COMPONENT-*
TICKET-*
AGENT-*
ARTIFACT-*
```

The audit should fail when launch-critical downstream outputs reference missing or duplicated upstream IDs.

---

# Acceptance Criteria

* Global workflow contract defines reference integrity rules.
* Readiness audit emits `reference_integrity`.
* Each stage completion gate requires blocking reference errors to be resolved or explicitly accepted.
* Stage 5 tickets and Stage 6 validation results preserve traceability to Stage 1-4 source IDs.

---

# Patch 11 — Readiness Failure Revision Loop

# Objective

Define what happens when a readiness audit intentionally fails or blocks, including how findings route back to the owning stage, output file, and skill.

This makes failed audits actionable instead of only preventing progression.

---

# Proposed Revision Object

```json
{
  "revision_loop": {
    "revision_id": "",
    "triggering_audit": "",
    "owning_stage": "",
    "owning_output": "",
    "owning_skill": "",
    "blocking_issue": "",
    "required_change": "",
    "recommended_action": "",
    "can_continue_with_accepted_risk": false,
    "target_status_after_revision": "",
    "status": "open | in_progress | resolved | accepted_risk"
  }
}
```

---

# Files To Update

Review docs:

```text
System-References/Docs/Global-Stage-Readiness-Audit.md
System-References/Docs/Global-Stage-Workflow-Contract.md
All Stage 1-8 review docs
```

Skills:

```text
.opencode/Skills/global-stage-readiness-audit/skill.md
All Stage 1-8 command skills
```

---

# Required Behavior

When readiness fails, the audit must produce revision-loop records that identify:

* exact blocking condition
* owning stage
* owning output
* owning skill or command
* required change
* whether accepted risk is allowed
* next target status

Stage commands must not use a ready status until revision-loop blockers are resolved or explicitly accepted according to profile rules.

---

# Acceptance Criteria

* Failed readiness audits produce actionable revision-loop objects.
* Revision loops distinguish current-stage revision from prior-stage revision.
* Critical unresolved blockers cannot be hidden as warnings.
* Accepted-risk revision loops link to the risk acceptance ledger.

---

# Patch 12 — Artifact Field Standardization

# Objective

Standardize artifact field names across Stage 5, Stage 6, Stage 7, and global audit docs.

The diagnostic found that Stage 5 often says "artifact expectations" while Stage 6 and skills use `expected_artifacts`.

---

# Standard Terms

Use:

```text
expected_artifacts
artifact_evidence_updates
artifact_refs
Artifact-evidence-registry.json
```

Avoid ambiguous variants such as:

```text
artifact expectations
proof notes
evidence notes
artifact list
```

unless they are explanatory prose around the canonical fields.

---

# Files To Update

Review docs:

```text
System-References/Docs/Stage-5-development-orchestration-draft.md
System-References/Docs/Stage-6-implementation-validation-draft.md
System-References/Docs/Stage-7-launch-operationalization-draft.md
System-References/Docs/Global-Stage-Workflow-Contract.md
System-References/Docs/Global-Stage-Readiness-Audit.md
```

Skills:

```text
.opencode/Skills/build-ticket-generation/skill.md
.opencode/Skills/implementation-execution/skill.md
.opencode/Skills/validation-execution/skill.md
.opencode/Skills/system-health-synthesis/skill.md
.opencode/Skills/launch-readiness-validation/skill.md
.opencode/Skills/global-stage-readiness-audit/skill.md
```

---

# Required Behavior

Stage 5 build tickets must use the exact field:

```text
expected_artifacts
```

Stage 6 must produce:

```text
artifact_evidence_updates
artifact_refs
```

Stage 7 must consume:

```text
artifact_refs
deployment_proof
```

Global readiness audits must validate that required expected artifacts have matching registry entries or accepted blockers.

---

# Acceptance Criteria

* Stage 5 review doc uses `expected_artifacts` in build ticket schema and completion checklist.
* Stage 6 review doc maps `expected_artifacts` to `artifact_evidence_updates`.
* Stage 7 review doc maps deployment proof to `artifact_refs`.
* Global readiness audit uses canonical artifact field names.

---

# Current Enforcement Backlog

- Patches 13–19: **implemented and regression-tested**. Patch 20: **prepared; live pilot pending**. Patches 21–24: **planned; not implemented**.
- See `Readiness-Enforcement-Contract.md` for exact fields and adoption behavior, and `Stage-1-8-Improvement-Implementation-Record.md` for the change record.
- Existing outputs need genuine review/verification before the next affected finalization; approvals and successful results are never fabricated or refreshed automatically.
- Preserve the eight stages, Stage 4 opening waitlist, normalized Stage 5 envelopes, stable IDs, and unrelated work.

---

# Patch 13 — Schema Coverage And Seed Parity

## Implementation Status

- Implemented and regression-tested.

## Objective

- Close RISK-HEALTH-001 and RISK-HEALTH-002 without overstating Draft 2020-12 coverage.

## Changes

- Align the UX `ui_blueprints` seed with the Stage 4 array contract, retaining the documented legacy-empty-object compatibility only where needed for existing inputs.
- Add `uniqueItems` support to the shared validator, or remove its use only if the same invariant is guaranteed at every intended entry point. Prefer implementing this small used keyword.
- Check every seed against its specific stage schema and registries against their own schemas.
- Inventory schema vocabulary and fail tests when a newly used validation keyword has no implementation; account for known subset behavior such as `$ref` siblings before claiming general standards compliance.

## Acceptance

- All six current seed/registry checks pass.
- Duplicate `required_targets` fail standalone deployment schema validation as well as the dedicated deployment gate.
- Unique arrays pass, and existing conditional/reference/normalized schema behavior remains correct.

---

# Patch 14 — Active Profiles And Research Evidence Gates

## Implementation Status

- Implemented and regression-tested.

## Objective

- Close RISK-HEALTH-003 by evaluating policy and Stage 2 substantive evidence rather than reporting successful policy evaluation from shape alone.

## Changes

- Read the canonical active profile and evaluate declared required outputs, validation layers, and approval gates. Unknown or unsupported requirements produce an explicit blocker instead of a hardcoded `standard` success.
- Add focused Stage 2 checks for architecture-critical assumptions, evidence quality, confidence thresholds, contradictions, and explicitly authorized risk exceptions under existing rules.
- Require current-stage assumption/risk decisions where applicable; earlier-stage records must not substitute for missing current-stage assessments.
- Preserve Stage 2 research ownership: no waitlist artifact, launch, signup threshold, or measurement delay is required there.

## Acceptance

- The custom-profile missing-output probe fails with the actual missing path and active profile ID.
- Empty research envelopes cannot become ready without required evidence or a documented policy-authorized exception.
- Passing evidence, explicitly accepted risks, low confidence, unavailable research, and unresolved critical contradictions have distinct tests.

---

# Patch 15 — Normalized Stage 5 Audit And Handoff Integration

## Implementation Status

- Implemented and regression-tested.

## Objective

- Close RISK-HEALTH-004 and make the global runner enforce the same package invariants as the dedicated Stage 5 contract.

## Changes

- Use the existing contract helpers and resolver to validate the complete context, eight artifact envelopes, manifest index, canonical collections, and Stage 6 handoff during global readiness.
- Check indexed paths, IDs, types, and data pointers against actual artifacts; reject mixed/partial v2 packages. Preserve archived self-contained input through the existing read-only compatibility path.
- Require the Stage 4 waitlist and approved Stage 3 deployment references at the applicable new-workflow handoffs through Stages 5–7; merely adding optional constructor fields is insufficient.
- Add a genuinely normalized package to the global Stage 1–8 integration fixture. Keep archived/common-envelope compatibility tests separate and clearly labeled.

## Acceptance

- The missing indexed path probe blocks Stage 5 readiness and identifies the broken entry.
- Mismatched context, artifact identity, data path, missing handoff references, and partial packages fail.
- A full normalized package passes, the resolver returns both pre-code references, and applicable archived fixtures retain compatibility.

---

# Patch 16 — Runtime Outcomes And Launch Proof Enforcement

## Implementation Status

- Implemented and regression-tested.

## Objective

- Close RISK-HEALTH-005 and RISK-HEALTH-006 before relying on automatic release readiness.

## Changes

- Evaluate every required launch-critical workflow by stable ID, status, outcome, and resolvable proof. Do not accept a nonempty workflow array as success.
- Block failed persistence, blocked/unvalidated required workflows, missing workflow coverage, and unresolved dead controls or fixture runtime dependencies. Use existing approval/risk rules for any allowed deferral.
- Require applicable Stage 7 production-build, deployment, smoke-test, rollback, environment, and monitoring-alert evidence; check artifact identity, verification status, and readable location.
- Evaluate required visual QA/compliance outcomes and unresolved failures, rather than only reporting field presence. Explicit accepted launch risks must resolve to valid authority.
- Keep provider-specific live tests in the owning workflow; the global gate validates the recorded results and references.

## Acceptance

- Both confirmed false-readiness probes fail with actionable blockers.
- Missing proof, unverified artifacts, missing required workflows, failed visual QA, and invalid deferrals block.
- Complete successful evidence passes; accepted-risk exceptions pass only where the contract permits them.
- Tests prove each applicable proof category is independently required, not satisfied by an unrelated earlier-stage record.

---

# Patch 17 — Durable Diagnostics For Malformed Inputs

## Implementation Status

- Implemented and regression-tested.

## Objective

- Close RISK-HEALTH-007 and preserve the promise of an audit for every finalization attempt.

## Changes

- Convert canonical state, ledger, registry, schema, and document parse/shape failures into owned blocking diagnostics before finalization can crash.
- Make the CLI persist a failed audit and revision actions with nonzero exit when inputs are unreadable or malformed. Preserve damaged source files for repair.
- Avoid overwriting an unreadable global-state file with a fabricated baseline; write the standalone failed audit and report the global-state update failure explicitly.

## Acceptance

- Malformed JSON, unexpected root types, missing schema targets, and malformed ledgers produce deterministic failed audits without uncontrolled exceptions.
- Valid global state records the failed attempt. Invalid global state is preserved with a visible recovery action.
- No invalid input can advance readiness or be silently replaced by success defaults.

---

# Patch 18 — Feedback Destination And Audit Accuracy

## Implementation Status

- Implemented and regression-tested.

## Objective

- Close RISK-HEALTH-008 while preserving Stage 8's terminal, cyclical role.

## Changes

- Validate feedback items against allowed owning stages and existing issue-routing rules, not merely owner/action presence.
- Require evidence and resolution/ownership data for high/critical routes according to the contract; resolve evidence references.
- Populate `routes_checked`, missing-field diagnostics, and cycle flags from actual evaluation instead of returning default empty arrays and `creates_new_stage_cycle: false` unconditionally.

## Acceptance

- `Stage 99`, missing/invalid target stages, unresolved required evidence, and incomplete critical routes block evolution readiness.
- Valid routes to earlier stages pass and preserve target, owner, action, evidence, and cycle information.
- Audit fields match the evaluated routes, including the valid no-new-cycle case.

---

# Patch 19 — Bind Pre-Code Decisions To Approved Scope

## Implementation Status

- Implemented and regression-tested.

## Objective

- Reduce stale-approval and platform-omission risk identified through static inspection of the new Stage 3/4 controls.

## Changes

- Reconcile required deployment targets with the approved Stage 1 platform requirements, with explicit scope-change approval for omissions.
- Record the feature/stack/deployment revision used for waitlist creation using the smallest existing revision or content-hash mechanism available; reuse the written-page approval pattern where appropriate.
- Invalidate only affected approvals and downstream evidence when those decisions materially change; preserve stable IDs and historical artifacts.
- Keep the waitlist at the Stage 4 opening checkpoint, with a verified launch required before completion and no signup-count gate.

## Acceptance

- Omitting an approved target from both architecture state and the strategy does not evade validation.
- A material approved-scope or stack change is detected and requires reconciliation; unrelated edits do not restart the workflow.
- The unchanged approved scope/stack plus verified waitlist passes without waiting for demand metrics.

---

# Patch 20 — Supervised Real-App Evidence Pilot

## Implementation Status

- Runbook prepared; actual application pilot pending selection and access. See `Stage-1-8-Supervised-Pilot-Runbook.md`.

## Objective

- Establish practical confidence beyond synthetic fixtures after the false-readiness gaps are closed.

## Changes

- Run one approved application through Stages 1–8, retaining actual research, feature/stack approval, Stage 4 waitlist publication, design approvals, normalized tickets, runtime/visual tests, deployment proof, and telemetry-driven feedback.
- Review required evidence manually during the pilot and record limitations and provider access failures honestly.
- Update scores from observed results and document any genuine workflow lessons in the owning skills.

## Acceptance

- All eight stage audits reflect real outputs and reviewable evidence, with no invented demand, deployment, or telemetry claims.
- Failed checks produce actionable repair routes and are resolved or explicitly accepted where allowed.
- Unattended operation is considered only after the complete evidence set and residual limitations are reviewed; passing fixture tests alone is insufficient.

---

# Patch 21 — General Execution And Regression Completion

## Implementation Status

- Planned; not implemented. Priority: high. Owner: Stage 6 / global readiness. Finding: `RISK-HEALTH-009`.

## Required Changes

- Evaluate canonical execution blockers, required test failures, regression outcomes, and planned-ticket completion before Stage 6 readiness.
- Map results to required Stage 5 work; successful critical workflow proof cannot hide an incomplete migration or unrelated required test failure.
- Retain explicitly authorized deferral handling and the existing one-ticket scoped-change entry path.

## Acceptance Criteria

- Nonempty unresolved `execution_blockers` or required `test_failures` block, even when workflow evidence passes.
- Missing or nonterminal required ticket results block; complete valid results pass.
- Existing normalized and scoped-change successful controls remain passing.

---

# Patch 22 — Substantive Feature And Workflow Planning Coverage

## Implementation Status

- Planned; not implemented. Priority: high. Owner: Stage 5. Finding: `RISK-HEALTH-010`.

## Required Changes

- Reconcile approved in-scope feature/workflow IDs with slices, build tickets, assignments, acceptance criteria, and planned validation.
- Block empty planning collections when approved buildable features require work; account for exclusions only through explicit approved scope decisions.
- Reuse the normalized package and existing contract validators; add coverage checks rather than replace them.

## Acceptance Criteria

- The current one-feature/zero-ticket probe blocks for missing coverage.
- Missing feature/workflow coverage, unassigned required tickets, or absent validation obligations produce actionable diagnostics.
- A complete traceable plan passes; approved exclusions remain explicit and reviewable.

---

# Patch 23 — Complete Selected Stack Readiness

## Implementation Status

- Planned; not implemented. Priority: high. Owner: Stage 3. Finding: `RISK-HEALTH-011`.

## Required Changes

- Validate every required selected-stack component defined by the Stage 3 command, not only hosting/deployment.
- Require concrete choices or explicit allowed `none_for_mvp` decisions, component rationales, and the existing stack evaluation/compatibility decisions.
- Bind complete reviewed decisions to the existing fingerprints; preserve original platform coverage and deployment comparisons.

## Acceptance Criteria

- A hosting-only stack blocks with named missing components.
- Unresolved alternatives, missing required rationales, and unacceptable evaluation decisions block.
- Complete approved web/mobile stack scenarios and deliberate exclusions pass.

---

# Patch 24 — Downstream Approval And Evidence Freshness

## Implementation Status

- Planned; not implemented. Priority: high. Owners: Stages 5–7 / shared handoff validation. Finding: `RISK-HEALTH-012`.

## Required Changes

- Recheck approved scope/stack/strategy fingerprints at affected downstream finalizations, or consume a versioned explicitly approved decision snapshot with equivalent freshness checks.
- Require affected upstream review and evidence reconciliation when substantive scope changes; reference existence alone must not establish readiness.
- Carry reviewed Stage 4 page content, shared-standard hashes and revision approval references through the existing blueprint-linked handoff. Recheck freshness when affected Stage 5–7 work finalizes.
- Preserve stable IDs, historical artifacts, unrelated work, and the existing rule against automatically refreshing approvals.

## Acceptance Criteria

- The changed-feature probe blocks affected Stage 5, 6, and 7 readiness as it already does in Stages 3–4.
- The unapproved page-edit probe also blocks affected Stage 5, 6 and 7 readiness; shared-standard changes and stale revision approvals are covered.
- Stack/strategy drift and stale publication/build evidence are identified with the owning decision and next action.
- Unchanged approved decisions and unrelated control-envelope edits continue to pass.

---

# Patch 25 — Stage 4 Contract-Test And Workflow Wording Synchronization

## Implementation Status

- Planned; not implemented. Priority: medium. Owner: Stage 4 tests/documentation. Finding: `RISK-HEALTH-013`. Dependencies: existing Stage 4 standards/specification/revision implementation; independent of Patches 21–24.

## Required Changes

- Reconcile the Stage 4 command and draft phase-8 wording to include shared standards, written page specifications, revision baselines and complete-set approval.
- Replace the brittle exact old-heading assertion with an ordering check that tolerates descriptive text but verifies all written-review obligations precede Stitch generation/update.
- Retain separate prototype approval, read-only draft/final gates, and fallback approval requirements. Do not weaken checks just to make the wording test pass.

## Acceptance Criteria

- The dedicated Stage 4 suite passes all four tests, including its command and draft subtests, with no `ValueError`.
- A negative control that moves written approval after prototype mutation is rejected; harmless heading elaboration passes.
- The complete repository run passes, including the 27 page-specification tests and all 87 readiness tests in the current baseline. Additions may increase counts; never hardcode them as the acceptance mechanism.
- Stage ordering and new standards/revision obligations remain intact; no application state or approvals are changed by the repair.

---

# Implementation Strategy

- Retain patches 13–19 as implemented history; their original specific probes remain covered.
- Repair contract-test drift with **25**, then implement readiness fixes in order **21 → 24 → 23 → 22**, keeping each independently reviewable with a reproduced failing probe and successful control.
- Coordinate patches 21/22 for complete planned-work accounting and patches 23/24 for complete approved-stack continuity.
- Then execute Patch 20 with an actual application and its live evidence sources. Reporting and fixtures cannot complete that pilot.
- Run `stage-health-report-check` after substantive changes to refresh the assessment and both plan editions; do not implement a planned patch merely as part of a health check.

---

# Review Checklist For Future Hardening

- Keep `System-References/Docs` as the canonical review-document location.
- Reuse the global audit and existing stage-specific helpers rather than add a second readiness authority.
- Preserve the existing user/delegated-policy authority requirement for accepted high and critical risks.
- Evaluate policy-specific exceptions explicitly; never turn missing validation into an implicit approval.
- Keep standalone per-stage audit records and update global state only when safely readable.
- Preserve `expected_artifacts`, artifact-registry references, normalized Stage 5 ownership, and Stage 4 waitlist placement.
- Confirm the regression probes fail for the intended reason before calling a patch complete.

---

# Expected Result

- Seven enforcement patches implemented; all eight original findings addressed with regression coverage. Four readiness gaps remain planned under patches 21–24; the additional Stage 4 test regression is planned under Patch 25.
- The implementation record documents exact changes, interfaces, compatibility behavior, and verification results.
- The original 84 / 100 diagnostic remains historical; the current health assessment is 87/B. No A+ claim has been made.
- Patch 20 requires real product, publication, runtime, deployment, monitoring, and feedback evidence before it can be completed.
