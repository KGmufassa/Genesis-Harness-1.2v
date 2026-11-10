# Readiness Enforcement Contract

## Ownership And Adoption

- Apply this contract alongside the global workflow contract. Keep the eight stages and the Stage 4 opening waitlist checkpoint.
- Patches 13–19 strengthen the existing readiness runner. New active finalizations must provide the fields below; do not fabricate approvals or backfill successful results into archived work.
- The read-only Stage 5 resolver still accepts archived self-contained input. Active Stage 5 readiness requires a complete normalized v2 package.
- The audit evaluates recorded evidence. The owning skills perform live research, signup, runtime, visual, deployment, and monitoring checks.

---

## Schema And Input Failures

- Validate current-stage outputs and canonical state against their stage-specific schemas, and registries against their own schemas.
- Support the repository's declared schema vocabulary, including `uniqueItems` and `$ref` sibling constraints. Unknown validation keywords are errors; vocabulary regression tests cover all repository schemas.
- Treat malformed JSON, wrong root shapes, unavailable schema references, and unreadable summaries as blockers. Save failed audits and revision actions with a nonzero CLI exit.
- Preserve damaged source files. If global state is unreadable, save the standalone failed audit, report the failed global update, and leave the damaged global file untouched.

---

## Profiles And Current-Stage Decisions

- Read `stage_contract_profile` from the current canonical state; Stage 5 reads it from shared context.
- `required_outputs` is a list of existing paths. Bare filenames resolve relative to the active stage directory; `Build-Plans/` paths resolve relative to the workspace.
- `required_validation_layers` accepts `schema_validation`, `reference_integrity`, `research_evidence`, `deployment_strategy`, `waitlist_validation`, `page_specifications`, `normalized_handoff`, `workflow_outcomes`, `deployment_proof`, `visual_qa`, or `feedback_routes`, only in applicable stages.
- `approval_gates` contains JSON pointers to approved objects in the current canonical state. Unsupported layers/control fields block rather than report an assumed successful standard profile.
- `required_stage_depth` uses `stage_1` through `stage_8` with `minimal`, `standard`, `detailed`, or `exhaustive`; detailed/exhaustive depth needs explicit executable layers.
- `optional_outputs` and `skip_allowed_outputs` identify optional profile additions; they do not waive baseline required files or safety/evidence gates.
- Require current-stage assumptions and risks or explicit `*_not_applicable: true`; previous-stage records and false flags do not substitute.
- Stage 1–4 approval must be on the canonical decision brief with `approval_status: approved`, `approved_by`, and `approved_at`; nested unrelated approval records do not authorize progression.

---

## Stage 2 Research

- Require a nonempty `assumption_registry` and `confidence_scores` for market, technical, business, operational, and architecture readiness.
- Apply existing minimums: 0.70, 0.75, 0.65, 0.70, and 0.75 respectively. Respect evidence-quality confidence ceilings.
- Validated or architecture-critical assumptions need medium/high evidence with source type, summary, source date, freshness, inference flag, and an HTTP(S) source or verified artifact references. Validated assumption confidence is at least 0.75.
- An assumption-specific `accepted_risk_ref` may authorize an existing policy-permitted evidence exception. `research_accepted_risk_ref` may authorize a threshold exception. Neither replaces the assumption registry, nor silently resolves critical contradictions/unknowns.
- Keep waitlist launch out of Stage 2; it occurs after stack/deployment approval in Stage 4.

---

## Approved Scope And Deployment Bindings

- Record `target_platforms` in `Build-Plans/Stage-1/05-feature-structure.json` using `web`, `ios`, and/or `android`. Stage 3 must cover exactly that approved target set; omissions require an approved Stage 1 scope revision.
- Use `decision_bindings.decision_hashes(root, architecture, strategy)` to compute `core_features_hash`, `stack_hash`, and `strategy_hash`. Hashes use canonical JSON and exclude the documented control envelope from feature/strategy payloads.
- Before presenting Stage 1 scope for approval, compute its hash and include it in `Planning-state.json.stage_decision_brief.core_features_hash`.
- Present the selected stack/strategy and their hashes for Stage 3 review; store all three hashes in the deployment strategy's `approval` object after actual approval.
- Store those same reviewed hashes in the Stage 4 waitlist artifact's `approved_decisions`. Do not recompute approval hashes automatically after a material decision changes; route the affected decision for review and re-verify affected evidence.
- Status/schema-check envelope updates do not alter the scope hash. Feature, target, selected-stack, or deployment-decision changes invalidate affected bindings while preserving stable IDs and history.

---

## Stage 5 Package And Later Handoffs

- Validate context, all eight artifacts, and manifest with pinned schemas and existing Stage 5 contract helpers.
- Match manifest paths, artifact IDs/types, schema references, and canonical data pointers to the actual files. Validate ticket references, compact risk references, agent scopes, execution waves, and launch-critical completion definitions.
- Require `waitlist_validation_ref` and `deployment_strategy_ref` in Stage 5 shared context and its Stage 6 handoff, and in Stage 6/7 canonical records and outgoing handoffs. Both references must resolve.
- Stage 5 plans runtime checks; it does not require implementation evidence before implementation begins.

---

## Runtime, Visual, And Launch Proof

- Required workflow IDs come from the accumulated stage documents. Evaluate evidence only from the active implementation/launch stage so earlier success cannot hide missing current results.
- Require covered workflows to reach `local_e2e_passed` or `staging_e2e_passed` with `verified_user_outcome` and verified artifact references. Explicit persistence failures, blocked outcomes, duplicate records, and missing coverage block.
- Require checked `dead_control_validation` and `runtime_data_source_validation` for launch-critical workflows; unresolved gaps continue to block.
- Applicable visual work requires `visual_qa` with passed status, `responsive_validation: passed`, `design_system_compliance: passed`, no `unresolved_failures`, and verified `evidence_refs`. An explicit profile visual layer requires these checks even without a blueprint marker.
- Stage 7 `deployment_proof` requires `production_build_artifact`, `deployment_dry_run_result`, `smoke_test_results`, `rollback_test_result`, `environment_verification`, and `monitoring_alert_test`. Each is an object with passed `status` and verified `evidence_refs`; unresolved `release_blockers` block readiness.
- Registry evidence uses stable `ARTIFACT-` IDs, `status: verified`, and a readable, nonempty local `path_or_url` or HTTP(S) location. A remote location is recorded evidence, not a fresh network verification by the runner.
- Allowed deferrals use `status: deferred_with_approval` plus a valid stage-scoped `accepted_risk_ref`. Visual deferral is allowed only at Stage 7. Explicit failure statuses remain blockers.
- An accepted risk must be active/accepted, scoped to the current source stage, carry user/delegated-policy authority, approver, reason, mitigation, resolvable approval evidence, and any required delegated-policy reference. Expired risk acceptance is invalid; existing ledger schema obligations still apply.

---

## Stage 8 Feedback

- Require an explicit `prior_stage_feedback` array with valid target stage, owner, and action. Targets are `Stage 1` through `Stage 8`; Stage 8 remains terminal/cyclical.
- When `issue_domain` is supplied, route product → 1, assumptions → 2, architecture → 3, UX → 4, planning → 5, implementation → 6, deployment → 7, telemetry → 8.
- High/critical feedback requires verified evidence references. Populate checked route records, missing-owner/action/evidence diagnostics, and cycle flags from actual evaluation.
- Feedback recommendations do not authorize implementation or deployment changes on their own.

---

## Stage 4 Page Standards and Revision Enforcement

- Apply [Page Standards, Content and Revision Contract](../../.opencode/Skills/stage-4-ux-interaction-architecture/references/page-standards-and-revisions.md) to all Stage 4 runs, including legacy runs before their next prototype mutation or readiness approval.
- Written review requires populated shared standards and page content, current source/standard hashes, baseline/revision snapshots, complete hash chains and explicit current approvals. Human review establishes workflow completeness and semantic correctness.
- Before prototype mutation use the read-only `page_specifications.py --workspace-root . --phase draft` gate; final readiness uses `--phase final` and additionally reconciles completed blueprints and downstream impact resolutions/routes. Missing history must be recovered or transparently rebaselined and reviewed, never fabricated.
- Keep `page_standards`, `page_baselines` and `page_revisions` in Stage 4 UX state. Preserve the existing downstream handoff interface; link generated Markdown through the complete app blueprint.
