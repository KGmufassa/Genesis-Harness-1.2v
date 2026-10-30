---
name: change-intake-router
description: Route approved-product changes to the earliest affected Genesis stage, create compact CHANGE records after approval, enforce single-writer ID locks, and audit scoped changes before merge.
compatibility: opencode
---

# Change Intake Router

## Purpose

- distinguish an active-stage refinement from a change to approved scope
- select the earliest owning stage
- keep unchanged stages and stable IDs intact
- create one compact change record only after approval
- audit approval, locks, references, validation, risks, and deferred work before merge

## Workflow

1. Run the router without `--record` to preview classification and stage routing.
1. Show material product, architecture, UX, security, migration, or release impacts to the user.
1. Record only after approval and a clean-worktree preflight.
1. Run only stages marked `required`; preserve `not_required` reasons.
1. Use the normal stage contracts for affected work.
1. Audit the change record before merge.

```sh
python3 .opencode/Skills/change-intake-router/scripts/route_change.py "Add threaded comments"
python3 .opencode/Skills/change-intake-router/scripts/route_change.py "Fix approved copy" --approval-status approved --owner user --record
python3 .opencode/Skills/change-intake-router/scripts/route_change.py --audit-record Build-Plans/Changes/CHANGE-001/change-record.json
```

## Boundaries

- do not create a change cycle while the owning stage is active and unapproved
- do not infer approval for material product, architecture, UX, security, migration, or release changes
- do not modify baseline global stage status or overwrite baseline readiness audits
- do not regenerate unaffected stage outputs
- do not allow two active changes to write the same stable ID
- do not create branches, worktrees, commits, or merges automatically
- use Git as the baseline, diff, and recovery mechanism

## Outputs

```text
Build-Plans/Changes/CHANGE-NNN/change-record.json
Build-Plans/Build-status/Change-ledger.json
```

Only a passed scoped audit may set `ready_to_merge`. Set `completed` only after merge and post-merge verification.

