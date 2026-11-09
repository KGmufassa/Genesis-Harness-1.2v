# Pre-Code Validation And Deployment Contract

## Stage Boundaries

- Keep the eight stages. Stage 1 defines the waitlist audience, value proposition, signup offer, target assumptions, desired metrics, and measurement window in its product boundaries and success framework.
- Stage 2 researches assumptions and feasibility without building or publishing the waitlist. Stage 3 reconfirms the approved Stage 1 core features/MVP boundaries and approves the stack and deployment strategy before page creation.
- Stage 4 opens with waitlist design, build, and publication using those approved decisions, before app-wide UX work. This narrow exception to Stage 6 covers only the page, collection, and measurement plumbing. Apply the existing relevant page/design approvals to the focused waitlist design.
- A working published page is required; waiting for traffic, elapsed measurement time, or signup targets is not required. Verified publication is required before Stage 4 completes; existing Stage 2 research and Stage 4 design approval gates still apply.
- Page publication proves the experiment works, not demand or technical feasibility. Record unobserved demand as `awaiting_evidence`.
- Stage 3 compares deployment alternatives with the tech stack and obtains approval before application code. Stage 7 executes the approved strategy.

## Waitlist Artifact

- Write `Build-Plans/Stage-4/10-waitlist-validation.json` with `$schema: System-References/Schemas/waitlist-validation.schema.json` and the common stage envelope. Do not renumber existing outputs.
- Record `core_features_ref: Build-Plans/Stage-1/05-feature-structure.json#` and `deployment_strategy_ref: Build-Plans/Stage-3/09-deployment-strategy.json#`; require approved Stage 1 scope and Stage 3 stack/deployment before publication. Publication timestamps must be on or after deployment approval.
- Define `experiment_id` (`EXPERIMENT-`), nonempty `source_refs` to upstream assumptions, `audience`, `value_proposition`, `signup_offer`, `desired_metrics`, `measurement_window`, and `owner`.
- Record `hosting` with `method`, `collection_method`, `rationale`, and `cost_assumptions`; record `publication` with `status`, `url`, and `published_at`.
- Record `verification` checks named `public_url`, `signup_persistence`, `success_error_states`, `duplicate_handling`, `spam_protection`, `mobile_layout`, `accessibility`, and `measurement`. Each has `status`, `checked_at`, and nonempty `evidence_refs` of verified `ARTIFACT-` entries.
- Evidence entries belong in `Build-Plans/Build-status/Artifact-evidence-registry.json` with `status: verified` and `path_or_url` pointing to a real local evidence file or public HTTP(S) URL. Never include signup personal data.
- Record `metrics.status` as `awaiting_evidence` or `observed`. For observed traffic include `visits`, `completed_signups`, `conversion_rate` (0–1), `traffic_sources`, `observation_start`, and `observation_end`. Omit unobserved numeric values instead of inventing zeros.
- Include `limitations` and `follow_up_actions`; UX state and its Stage 5 handoff use `waitlist_validation_ref: Build-Plans/Stage-4/10-waitlist-validation.json#`.
- Waitlist readiness requires publication, a public HTTP(S) URL, all checks passed, and resolvable verified evidence. Failed launch/access produces a blocker with a next action.

## Deployment Artifact

- Write `Build-Plans/Stage-3/09-deployment-strategy.json` with `$schema: System-References/Schemas/deployment-strategy.schema.json` and the common stage envelope.
- Define `strategy_id` (`INFRA-`), nonempty upstream `source_refs`, `required_targets` drawn from `web`, `ios`, `android`, `backend_hosting` (explicitly describe external/absent backend when applicable), `targets`, `sources`, `prerequisites`, and `risks`.
- Each target contains `platform`, `method`, `rationale`, and at least two `alternatives`. Each alternative contains `method`, `disposition` (`selected` or `rejected`), and `rationale`; exactly one selected alternative matches `method`.
- Include `runtime_fit`, `cost_assumptions`, and `operational_burden` for every target. Mobile targets additionally contain `build_toolchain`, `signing`, `test_distribution`, `distribution_channel`, `developer_accounts`, `release_process`, and `update_process`; explain any nonapplicability, including PWA delivery.
- Sources contain official `url`, `accessed_at`, and `finding`. Prerequisites contain `requirement`, `owner`, and `next_action`; account setup may remain a prerequisite without blocking architectural feasibility.
- Record `stack_compatibility.status` (`compatible`, `incompatible`, or `unresolved`), `findings`, and `unresolved_blockers`.
- Record `approval` with `approval_status`, `approved_by`, `approved_at`, and `brief_ref` pointing to `Build-Plans/Stage-3/00-stage-decision-brief.md`. Require actual user approval and compatibility before readiness.
- Set `deployment_targets` in architecture state to all required targets. Set `deployment_strategy_ref` in state, `stage_4_handoff`, and `selected_stack.hosting_and_deployment` to `Build-Plans/Stage-3/09-deployment-strategy.json#`.
- Set `selected_stack.hosting_and_deployment.target_methods` to a mapping from each required platform to its exact selected method. Reject missing targets, unresolved choices, drift from the stack, or unresolved compatibility blockers.

## Downstream Continuity

- Stage 3 hands the approved deployment strategy to Stage 4; it does not require a waitlist artifact. Stage 4 creates that artifact at its opening checkpoint and passes both references to Stage 5. Preserve the resulting waitlist design and record planned revisions; existing app-wide page specification and design approval gates still apply.
- Stage 5 places `deployment_strategy_ref` and `waitlist_validation_ref` in the normalized shared context (`00-stage-context.json` at the top level) and passes them in the manifest's Stage 6 handoff. Tickets reference the strategy for environment setup, accounts, builds, signing, distribution, release verification, and any planned waitlist changes.
- Stage 6 consumes these references through the existing normalized resolver, checks builds against the approved target methods, and carries both into the Stage 7 handoff. The early waitlist exception does not waive app implementation or visual QA gates.
- Stage 7 consumes the approved strategy, executes deployment and mobile distribution preparations, and records deployment proof. Material method/platform changes route back to Stage 3 rather than silently replacing the decision.
- Stage 8 compares observed waitlist outcomes with the original assumptions and desired metrics; pending observations remain unknown and may inform a later product revision.

## Adoption

- Apply the requirements to new workflows and the next affected Stage 3 or Stage 4 readiness attempt in existing projects. Do not backfill fabricated publication, research, or approval evidence.
- If an earlier Stage 2 waitlist artifact exists, preserve it as historical evidence and create the Stage 4 artifact with the same experiment ID after reconciling approved features/stack and re-verifying publication. Active readiness audits exclude the superseded Stage 2 filename so historical IDs and schemas cannot satisfy or conflict with the new gate. Do not auto-move, delete, or silently accept it as satisfying the Stage 4 gate.
- Preserve existing IDs, output numbering, stage statuses, and normalized Stage 5 envelopes. The two additional artifacts use dedicated schemas; stage output schemas allow their references without requiring these fields in every unrelated numbered output.
- Use the readiness audit to resolve structural/evidence references; live checks are performed by the owning skill and recorded with timestamps. The audit does not independently probe the network.

---

# Executable Enforcement Contract

- Apply `System-References/Docs/Readiness-Enforcement-Contract.md` for active profile evaluation, evidence gates, scope hashes, normalized handoff validation, and durable input-error diagnostics.
- Existing artifacts without the new binding/proof fields require real review and verification before their next affected readiness attempt; never fabricate backfilled success.
