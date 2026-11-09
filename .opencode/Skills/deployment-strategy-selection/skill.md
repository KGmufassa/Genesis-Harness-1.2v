---
name: deployment-strategy-selection
description: Compare and approve web and mobile deployment methods alongside the Stage 3 tech stack before app implementation.
compatibility: opencode
---

# Deployment Strategy Selection

## Purpose And Inputs

- Select deployment together with the Stage 3 stack, before architecture synthesis and application coding.
- Read Stage 1 target platforms and capabilities, Stage 2 feasibility/constraints, and the proposed architecture and stack.
- Use `System-References/Docs/Pre-Code-Validation-and-Deployment.md` and `deployment-strategy.schema.json` as the output contract.

## App-Specific Comparison

- Identify every required target: `web`, `ios`, and/or `android`; do not silently drop a requested platform.
- Compare viable web hosting/runtime approaches against rendering, backend APIs, database connectivity, background jobs, storage, security, cost, scaling, skill availability, and operational burden.
- Evaluate Cloudflare when relevant; explain exclusion when its execution model or capabilities do not fit. Never default to it solely because it was mentioned.
- For mobile, compare browser/PWA, native, and cross-platform delivery where applicable. Distinguish hosting APIs from distributing mobile binaries; a web host does not replace mobile distribution.
- For each mobile target, specify build service/toolchain, signing, test distribution, intended store or other eligible channel, developer accounts, release review, and update process. Mark inapplicable requirements explicitly with reasons.
- Research current provider capabilities, pricing assumptions, and platform/distribution rules using official sources; record URLs, access dates, and findings. If research is unavailable, record uncertainty and block decisions whose feasibility cannot be established.
- Present at least two app-specific alternatives, rejection reasons, and one concrete selected method for each required target. Alternatives may be rejected as infeasible with evidence.

## Decision And Approval

- Write `Build-Plans/Stage-3/09-deployment-strategy.json` and mirror its `required_targets` into `Architecture-state.json.deployment_targets`.
- Give the strategy an `INFRA-` ID and source references. Record shared backend hosting, per-target deployment methods, alternatives, sources, prerequisites, risks, and stack-compatibility findings.
- Copy the selected per-target choices into `selected_stack.hosting_and_deployment.target_methods`; do not leave unresolved alternatives or placeholders in selected choices.
- Make missing accounts actionable prerequisites with owner and next action. Missing accounts alone need not block architecture; unresolved runtime or distribution feasibility does.
- Include strategy and tradeoffs in the Stage 3 decision brief. After user approval, record approval authority, time, and brief reference in the strategy; never infer approval from a recommendation.
- Set `deployment_strategy_ref` in architecture state, `selected_stack.hosting_and_deployment`, and `stage_4_handoff` to the output file plus `#`.
- Require `stack_compatibility.status = compatible`, no unresolved blockers, and approval before Stage 3 readiness or app implementation.
- Update this skill in place when verified workflow lessons change its requirements.

---

# Executable Enforcement Upgrade

- Bind approved target methods to the Stage 1 platform set and record core_features_hash, stack_hash, and strategy_hash with actual user approval. Missing or stale hashes require reconciliation.
- Read `System-References/Docs/Readiness-Enforcement-Contract.md` for exact fields, compatibility boundaries, and risk/evidence rules.
- Update this skill in place when verified workflow lessons change its requirements.
