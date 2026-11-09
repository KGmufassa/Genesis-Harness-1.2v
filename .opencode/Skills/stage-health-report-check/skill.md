---
name: stage-health-report-check
description: Run a health check across all eight Genesis stages and synchronize the health report, Markdown improvement plan, and HTML reading edition.
compatibility: opencode
---

# Stage Health Report Check

## When To Use

- Use when the user requests `stage health report check`, an all-stage harness health assessment, or refreshed health and improvement-plan documents.
- Assess workflow correctness and executable enforcement. A real application finalization or security audit is a separate task.

## Scope And Source Of Truth

- Read the repository `AGENTS.md`, the current health report, improvement plan, implementation record, pilot runbook, global workflow/readiness contracts, and applicable enforcement/pre-code contracts.
- Inspect all eight live command skills, relevant synthesis/completion guidance, schemas, canonical state templates, executable controls, and tests; resolve discoverable facts from current source.
- Preserve existing work, IDs, historical implementation status, and user decisions, including deployment selection in Stage 3 and the waitlist opening Stage 4.
- Limit durable updates to the three reporting outputs below. Collect evidence in a temporary directory; do not implement fixes, launch an app, change approvals, or advance `Build-Plans` state during a health check.
- Do not invoke the readiness CLI against the actual workspace: it writes audits/global state. Use `build_audit()` or the CLI in isolated temporary fixtures for behavioral probes.

## Evidence Collection

- Run the collector from the repository root, using an absolute temporary output path. It discovers test suites/counts and checks stage-specific seeds/registries, syntax, JSON, metadata, whitespace, and baseline preservation without hardcoded inventory totals.
- Treat a nonzero collector exit as evidence to report, not permission to fix code or stop without documenting failed checks. `--skip-tests` is partial collection and cannot support a claim that tests passed.
- Read the complete results, including per-suite output and timeouts; the JSON is evidence, not a finished assessment or automatic grade.

```sh
python3 .opencode/Skills/stage-health-report-check/scripts/collect_health_evidence.py \
  --workspace-root . --output /absolute/temporary/path/stage-health-evidence.json
```

## Behavioral Review

- Follow `references/assessment-guide.md` for stage coverage, scoring, findings, and plan reconciliation.
- Compare each stage's substantive completion obligations with the actual audit paths, not only schema shape or helper existence.
- Reproduce every currently open finding using fresh temporary fixtures and include a passing baseline/control. Adapt probes if fixture interfaces have changed; record unavailable probes instead of assuming their result.
- Investigate additional plausible false-ready paths exposed by source changes. Record the owning stage, expected/actual result, affected source, reproducible setup, and practical impact.
- Keep stable `RISK-HEALTH-` finding IDs. Mark findings resolved only after fresh contrary evidence; use unverified/not rechecked for incomplete reviews. Preserve the original closure history and do not equate a broader new gap with reopening an old specific probe.
- Separate simulated harness behavior, real application outputs, and external capabilities. Empty application stage folders are normal for an unused harness and are not by themselves broken code.

## Required Reporting Outputs

- Update `System-References/Docs/Stage-1-8 Health Report.mdx`: preserve valid frontmatter and provide current evidence counts/date, all eight stage assessments, explained score/rubric, findings with statuses and evidence, remaining operational limits, and next work.
- Update `System-References/Docs/Stage-1-8-A-Grade-Improvement-Patch-Plan.md` from that same assessment: reconcile baseline/results and map each open finding to an actionable existing or new patch with owner, priority, changes, acceptance criteria, and dependencies.
- Preserve existing patch numbers and history; allocate new numbers after the current maximum. Never mark planned fixes implemented, or mark the real-app pilot complete, from reporting work or fixture success.
- Give every new/current patch a `## Implementation Status` with a clear status such as `Planned`, `Implemented and verified`, or `Prepared; live pilot pending`. Put the current assessment/date/test evidence in the health report; the renderer reads it rather than inventing metrics.
- Regenerate `System-References/Docs/Stage-1-8-A-Grade-Improvement-Patch-Plan.html` only after both reviewed Markdown documents are consistent. Use the bundled renderer, which handles new patch numbers and embeds local styles/scripts for offline viewing.

```sh
python3 .opencode/Skills/stage-health-report-check/scripts/render_patch_plan.py --workspace-root .
```

## Verification And Completion

- Check all three documents agree on current findings, scores, counts, date, patch status, and pending real-app work; historical metrics must be labeled historical.
- Verify HTML patch count/anchors, local links, source code examples, escaped content, filtering/navigation/print script syntax, and responsive/print styles. Use a browser preview when available and disclose when visual preview cannot be performed.
- Run the skill's tests and package metadata validation after creating/changing its scripts. Inspect the reporting diff and confirm `Build-Plans` files remained unchanged during the check.
- Summarize the current assessment, executed/failed/skipped checks, key remaining gaps, and links to the updated files. Do not promise an A+ grade or production readiness without evidence.
- Update this skill in place when verified usage reveals a workflow lesson; preserve the reporting-only scope.
