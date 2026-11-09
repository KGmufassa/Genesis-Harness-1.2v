# Stage Health Assessment Guide

## Stage Coverage

| Stage | Review Beyond File Presence |
| --- | --- |
| 1 | Approved product/MVP substance, intended platforms, assumptions/risks, feature scope, and usable research handoff |
| 2 | Realistic evidence quality, confidence ceilings/thresholds, architecture-critical assumptions, contradictions, and permitted exceptions |
| 3 | Complete concrete stack, evaluations/rationales, deployment alternatives, original platform coverage, compatibility, approvals, and fingerprints |
| 4 | Early waitlist after approvals, publication/signup proof, complete page set, written/hash approvals, UX/visual/a11y contracts, and design continuity |
| 5 | Full normalized package/index, substantive feature/workflow-to-ticket coverage, scopes/assignments/waves, acceptance/tests, and handoff freshness |
| 6 | All planned work accounted for, terminal execution/validation/regression results, general blockers/failures, workflow outcomes, visual proof, and upstream freshness |
| 7 | Actual launch-proof obligations, result/artifact verification, unresolved release blockers, rollback/monitoring, authorized exceptions, and approved build/scope continuity |
| 8 | Real signal inputs and limits, valid destinations, owned/evidenced actions, cycle flags, and an actual review trigger or schedule |

## Reproducible Probes

- Use the current integration test fixtures as starting points, reading their implementation before mutating a temporary copy. Never copy fake evidence into real stage folders.
- Confirm the baseline passes before applying a mutation. Distinguish a domain check rejecting a bad result from an unrelated reference/schema error masking the behavior under examination.
- Record the precise mutation, target stage/ready status, expected behavior, actual return/exception, source paths, and whether evidence is synthetic.
- Recheck the report's existing open probes first. Then inspect gaps not covered by tests, particularly empty collections, unrelated earlier successes, missing complete-stack fields, and stale upstream approvals.
- Failing tests, unavailable tools, incomplete reviews, and false-ready probes are different findings; report each accurately.

## Scoring

- Retain the report's established rubric unless the user changes it: workflow/contract design 30%, executable enforcement 50%, verification maturity 20%; round the weighted result to the nearest integer and explain the inputs.
- A = 90–100, B = 80–89, C = 70–79, D = 60–69, F = below 60. Per-stage scores are separate explained judgments. Do not invent an A+ subdivision or promote a grade based solely on patch completion/test counts.
- Scores must reflect reviewed code and reproduced behavior; no script automatically awards them. If evidence is insufficient, label the assessment provisional or retain the previous score as historical rather than declare fresh verification.
- Explicitly justify changes from the prior assessment and identify the supervised/real-app evidence ceiling. A passing harness fixture does not establish live deployment or business success.

## Document Synchronization

- Treat the health report as the assessment and the Markdown plan as the editable backlog. Generate HTML from those two sources; do not maintain independent hardcoded HTML counts or completion labels.
- Keep report sections `Diagnostic Scope`, `Per-Stage Health`, and `Open Findings` (or `Newly Confirmed Gaps`) for reviewability. Put stable finding IDs in open-finding headings; keep resolved finding history separate.
- Preserve plan foundation patches and previously reviewed completion history. Add new defects to a relevant open patch or append a new numbered patch; never reuse a number for another concept.
- For every open finding, specify concrete behavior changes and passing/negative acceptance cases. State dependencies and order, and retain pending pilot/access work as pending.
- Synchronize current assessment, date, executed checks, findings, and next work. Historical implementation records retain their original run counts and dates rather than being rewritten as current results.
- The renderer supports headings, paragraphs, strong text, inline code, flat lists, fenced code, and pipe tables used in this plan. It escapes raw HTML and is intentionally not a general Markdown engine. Extend it or adopt a Markdown library if future document syntax exceeds that ceiling.
- Do not launch a server automatically. If a localhost preview already exists, the regenerated file is served at the same URL; only start a server when requested.
