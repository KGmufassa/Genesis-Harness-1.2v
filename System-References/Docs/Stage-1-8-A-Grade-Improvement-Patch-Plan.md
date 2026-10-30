# Stage 1-8 A-Grade Improvement Patch Plan

# Purpose

This review document defines the planned patches needed to raise the full Stage 1-8 workflow from a strong B+/A- system to an A-grade workflow across planning, implementation, launch, and post-launch evolution.

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

Original overall workflow grade before patches 1-7:

```text
88 / 100
```

Diagnostic result after applying patches 1-7:

```text
94 / 100
```

Diagnostic result after applying patches 8-12:

```text
97 / 100
```

Target workflow grade:

```text
96-98 / 100
```

Target result:

```text
All stages grade A-range.
```

---

# Latest Diagnostic Run

Diagnostic date:

```text
2026-06-16
```

Review scope:

```text
System-References/Docs/Stage-1-product-initialization-draft.md
System-References/Docs/Stage-2-architect.md
System-References/Docs/Stage-3-system-architecture-draft.md
System-References/Docs/Stage-4-ux-interaction-architecture-draft.md
System-References/Docs/Stage-5-development-orchestration-draft.md
System-References/Docs/Stage-6-implementation-validation-draft.md
System-References/Docs/Stage-7-launch-operationalization-draft.md
System-References/Docs/Stage-8-post-launch-evolution-draft.md
```

Diagnostic summary:

| Area | Status | Notes |
| --- | --- | --- |
| Stage contract profiles | Present | All Stage 1-8 review docs consume `stage_contract_profile`. |
| Guidance policy | Present | All Stage 1-8 review docs consume `guidance_policy`. |
| Schema references | Present | All Stage 1-8 review docs reference their stage schema file. |
| Artifact evidence registry | Implemented | Stages 1-8 now reference artifact evidence where relevant, and Stage 3 explicitly names the registry path. |
| Stage 2 evidence quality | Present | Evidence metadata and quality rules are documented. |
| Stage 5 expected artifacts | Implemented | Stage 5 now standardizes on the exact `expected_artifacts` field name. |
| Stage 6 implementation proof | Strong | Stage 6 requires terminal ticket status, artifact evidence, validation proof, visual QA, and regression mapping. |
| Stage 7 deployment proof | Present | Launch readiness now includes deployment proof fields and completion requirements. |
| Stage 8 feedback routing | Present | Stage 8 includes prior-stage feedback routing and critical route ownership rules. |
| Schema validation result object | Implemented | Stage review docs, command skills, common schema, and readiness audit now require `schema_validation`. |
| Risk acceptance durability | Implemented | `Build-Plans/Build-status/Risk-acceptance-ledger.json` and schema now exist. |
| Cross-stage reference integrity | Implemented | Stage review docs, command skills, global contract, and readiness audit now require `reference_integrity`. |
| Revision loop behavior | Implemented | Failed readiness checks now require `revision_loops` with owning stage, output, skill, required change, and next action. |

Stage diagnostic grade:

| Stage | Grade | Diagnostic |
| --- | --- | --- |
| Stage 1 | A | Strong product initialization, schema controls, risk ledger visibility, and Stage 2 handoff. |
| Stage 2 | A | Evidence-quality upgrade is strong and now includes readiness control objects. |
| Stage 3 | A | Architecture scope is coherent and now explicitly references artifacts, risk ledger, and reference integrity. |
| Stage 4 | A | UX, UI blueprint, visual spec, design system, schema validation, and reference controls are strong. |
| Stage 5 | A | Ticket, agent, skill, visual, and artifact planning now standardizes `expected_artifacts`. |
| Stage 6 | A | Implementation loop, validation, repair, artifact proof, visual QA, and terminal status controls are strong. |
| Stage 7 | A | Deployment proof, launch gates, risk ledger linkage, and readiness controls are strong. |
| Stage 8 | A | Feedback routing, evolution controls, risk ledger linkage, and revision-loop rules are strong. |

Most important remaining gaps after patches 8-12:

```text
1. Actual schema validation tooling can be made stricter later if the harness adds a concrete validator command.
2. Reference integrity checks are now specified, but future implementation can add a dedicated automated resolver.
3. Risk acceptance entries are durable, but future runs should decide who counts as `accepted_by` for automated agent execution.
```

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

Patch implementation status:

| Patch | Status | Diagnostic Result |
| --- | --- | --- |
| 1 | Implemented | Registry file, schema, Stage 5 expectations, Stage 6 evidence, Stage 7 launch proof, and audit checks exist. |
| 2 | Implemented | All stage review docs and command skills consume stage contract profiles. |
| 3 | Implemented | Schema folder and schema refs exist. Stage-level schema validation result recording remains a follow-up. |
| 4 | Implemented | Stage 2 evidence metadata and quality rules are documented. |
| 5 | Implemented | Stage 7 deployment proof exists in readiness output and completion gate. |
| 6 | Implemented | Stage 8 prior-stage feedback routing exists. |
| 7 | Implemented | All stage review docs and command skills consume guidance policy. |
| 8 | Implemented | Stage review docs, command skills, readiness audit, and common schema include schema validation results. |
| 9 | Implemented | Risk acceptance ledger output and schema exist, and stages require accepted high/critical risks to be recorded. |
| 10 | Implemented | Global contract, readiness audit, stage review docs, and command skills require reference integrity checks. |
| 11 | Implemented | Global contract, readiness audit, stage review docs, and command skills require revision-loop actions for failed readiness checks. |
| 12 | Implemented | Stage 5, Stage 6, skills, and global contract use canonical artifact field names. |

Recommended implementation order:

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

These patches are recommended after the diagnostic run to move the workflow from approximately `94 / 100` to `96-98 / 100`.

| Patch | Name | Primary Impact | Priority |
| --- | --- | --- | --- |
| 8 | Stage-Level Schema Validation Results | Makes schema validation visible in every stage handoff | High |
| 9 | Risk Acceptance Ledger | Prevents accepted risks from becoming invisible downstream | High |
| 10 | Cross-Stage Reference Integrity Audit | Prevents broken IDs and weak traceability across handoffs | High |
| 11 | Readiness Failure Revision Loop | Makes failed readiness audits actionable and stage-routable | High |
| 12 | Artifact Field Standardization | Removes ambiguity around `expected_artifacts` and registry references | Medium |

Recommended follow-up implementation order:

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

# Implementation Strategy

Implement patches in dependency order:

1. Add Artifact Evidence Registry because it supports later proof and audit improvements.
2. Add Stage Contract Profiles because they influence stage depth and required outputs.
3. Add Schema Validation because it strengthens readiness checks after outputs are stabilized.
4. Upgrade Stage 2 evidence quality because validated assumptions drive architecture.
5. Upgrade Stage 7 deployment proof because launch readiness depends on artifacts and evidence.
6. Upgrade Stage 8 feedback routing because live signals need stronger loopback behavior.
7. Add Complexity-Based Interactive Guidance across all stages after profile rules exist.

Then apply follow-up patches:

8. Add stage-level schema validation results.
9. Add durable risk acceptance ledger.
10. Add cross-stage reference integrity audit.
11. Add readiness failure revision-loop routing.
12. Standardize artifact field names across Stage 5-7 and global audit docs.

---

# Review Checklist For Future Hardening

Before adding stricter automation around these patches, confirm:

* Whether `System-References/Docs` remains the canonical docs folder.
* Whether schema validation should be run by the readiness audit only or also by each stage command.
* Whether accepted risks should require explicit user approval for high and critical severity.
* Whether reference integrity failures should always block readiness or allow profile-specific exceptions.
* Whether revision-loop records should be written into one global file or each stage readiness audit.
* Whether `expected_artifacts` should be required for all build tickets or only validation/preview/deployment-sensitive tickets.

---

# Expected Result

After patches 1-7, the stage workflow improved from:

```text
88 / 100
```

to approximately:

```text
94 / 100
```

After follow-up patches 8-12, the current workflow grade is approximately:

```text
97 / 100
```

The biggest expected gains:

* Stage-level schema validation becomes visible and enforceable.
* Accepted risks remain durable across downstream stages.
* Broken cross-stage references become auditable before handoff.
* Failed readiness audits produce precise revision-loop actions.
* Artifact proof fields become consistent across Stage 5 planning, Stage 6 validation, Stage 7 launch readiness, and global audits.
* Global readiness improves through schema, profile, artifact, reference, risk, and revision-loop-aware audits.
