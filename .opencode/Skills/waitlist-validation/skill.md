---
name: waitlist-validation
description: Create and publish the waitlist at the opening of Stage 4 after core-feature, tech-stack, and deployment approval.
compatibility: opencode
---

# Waitlist Validation

## Purpose

- Create and publish the demand experiment at the Stage 4 opening checkpoint after input preflight and before app-wide UX work; follow `System-References/Docs/Pre-Code-Validation-and-Deployment.md` for the output contract.
- Read the approved Stage 1 core features, MVP boundaries, audience, value proposition, success framework, Stage 2 assumptions, and approved Stage 3 stack/deployment strategy before creating the page. Reconfirm scope feasibility at Stage 3 approval; route material scope changes back for approval.
- Treat signup evidence as demand validation; retain separate technical-feasibility validation.

## Experiment And Implementation

- Define an `EXPERIMENT-` ID, upstream assumption references, audience, offer, desired metrics, measurement window, and owner.
- Use the approved stack and deployment strategy for hosting and signup collection; record rationale and cost. If the minimal waitlist needs a different method, obtain a Stage 3 strategy amendment before building or publishing.
- Prepare and approve the focused waitlist design under applicable Stage 4 page/design rules, then create a responsive page with clear value proposition, signup CTA, accessible labels, success/error states, duplicate handling, basic spam protection, and a clear explanation of how signup information will be used.
- Store signups durably; collect only necessary data. Keep credentials server-side and exclude signup personal data from workflow evidence.
- Publish the page within the user's authorized scope; if access, required authorization, or provider capability is missing, return `blocked` with the exact next action. Do not report a local preview as published.
- Limit this pre-Stage-6 implementation exception to the validation site and collection/measurement plumbing; do not build app features.

## Verification And Evidence

- Verify the public URL and a signup from submission through durable storage, success/error and duplicate handling, spam protection, mobile layout, accessibility basics, and measurement collection.
- Record each check with `status`, `checked_at`, and `evidence_refs` to verified entries in the artifact evidence registry; redact test addresses and other personal data.
- Write `Build-Plans/Stage-4/10-waitlist-validation.json` using `waitlist-validation.schema.json`; register preview, test, and publication evidence.
- Use numeric metrics only for observed values. Omit unmeasured numbers and set `metrics.status = awaiting_evidence` until traffic has been observed; zero observed signups is valid.
- Record visits, completed signups, conversion rate, traffic sources, observation dates, limitations, and follow-up actions when available. Never label page publication alone as validated demand.

## Handoff And Readiness

- Set UX state `waitlist_validation_ref` and `stage_5_handoff.waitlist_validation_ref` to the output file plus `#`; retain `deployment_strategy_ref` in both. Record `core_features_ref` and `deployment_strategy_ref` in the waitlist artifact.
- Include launch status and pending demand evidence in the Stage 4 decision brief and synthesis.
- Require publication and all verification checks to pass for Stage 4 readiness; desired signup counts and elapsed measurement time do not block progression.
- Update this skill in place when verified workflow lessons change its requirements.

---

# Executable Enforcement Upgrade

- Use the approved decision hashes in approved_decisions, then verify publication after Stage 3 approval. Material upstream changes require affected decision review and re-verification; do not silently refresh hashes.
- Read `System-References/Docs/Readiness-Enforcement-Contract.md` for exact fields, compatibility boundaries, and risk/evidence rules.
- Update this skill in place when verified workflow lessons change its requirements.
