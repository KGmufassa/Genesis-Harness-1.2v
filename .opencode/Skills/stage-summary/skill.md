---
name: stage-summary
description: Generate local Stage 5-8 markdown assessment summaries from canonical stage JSON outputs.
compatibility: opencode
---

# Stage Summary

Use this skill when Stage 5, Stage 6, Stage 7, or Stage 8 needs a concise
human-readable assessment summary for a finalization attempt.

## When To Use

- A Stage 5-8 command is assembling final outputs for ready, blocked, or
  revision status.
- The user needs a clear local markdown artifact to assess what the stage did
  and whether the stage can proceed.
- The summary must be deterministic and grounded only in the canonical JSON
  outputs and the matching readiness audit when present.

## Scope

This skill scans only:

```text
Build-Plans/Stage-5
Build-Plans/Stage-6
Build-Plans/Stage-7
Build-Plans/Stage-8
```

Rules:

- scan only top-level `*.json` files in the selected stage folder
- ignore `.gitkeep`, non-JSON files, generated agents, registries, and workflow
  state files
- read only the matching `Build-Plans/Build-status/Stage-N-readiness-audit.json`
  when it exists
- skip stages that have no JSON artifacts
- write exactly one local summary markdown file per populated Stage 5-8 folder

## Required Inputs

- Workspace root containing `Build-Plans/`

## Output Contract

For each populated stage, write:

```text
Build-Plans/Stage-5/10-stage-5-summary.md
Build-Plans/Stage-6/06-stage-6-summary.md
Build-Plans/Stage-7/06-stage-7-summary.md
Build-Plans/Stage-8/06-stage-8-summary.md
```

Each summary must include:

- stage objective and final status
- user assessment: `Ready`, `Needs Revision`, `Blocked`, or `Needs Assessment`
- actions performed by the stage
- generated or updated canonical outputs
- key result counts for the stage domain
- schema, reference-integrity, handoff, readiness-audit, and evidence signals
- blockers, risks, unresolved questions, revision loops, and next actions
- confirmation that the summary is a local review artifact and not a canonical
  downstream handoff

## Workflow

- Verify `Build-Plans/` exists.
- Check Stage 5 through Stage 8, or the stages provided by `--stages`.
- Collect top-level JSON files in deterministic filename order.
- Load the matching readiness audit if it exists.
- Render the assessment from canonical stage JSON and readiness-audit evidence.
- Write the stage-local markdown summary into the same stage folder.
- Report generated summaries and skipped stages.

## Script

Use:

```bash
python3 .opencode/Skills/stage-summary/scripts/generate_stage_summaries.py --workspace-root <repo-root>
```

If the current working directory is the repository root, `<repo-root>` can be `.`.

To target one stage:

```bash
python3 .opencode/Skills/stage-summary/scripts/generate_stage_summaries.py --workspace-root . --stages 6
```

## Determinism Rules

- sort JSON files by relative path before rendering
- preserve exact stage naming from the folder name
- do not invent requirements, status, or interpretations not supported by the JSON
- treat missing required canonical outputs as blockers in the summary
- keep headings and bullet order stable across runs

## Stop Conditions

Stop and surface an error if:

- `Build-Plans/` is missing
- a targeted JSON file is malformed
- a stage path cannot be read
- the requested stage number is outside Stage 5-8

## Verification

Before completion, confirm:

- only populated Stage 5-8 folders produced markdown files
- each generated markdown file matches the stage-specific summary filename
- every top-level JSON file in a summarized stage appears in the markdown
- no Build-status file was read except the matching readiness audit
- summaries do not introduce canonical data that is absent from JSON outputs
