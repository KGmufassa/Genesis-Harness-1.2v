---
name: lazy-mode-debt
description: >
  Harvest every `lazy:` or `ponytail:` comment in the codebase into a debt
  ledger, so the deliberate shortcuts and deferrals lazy-mode leaves behind get
  tracked instead of rotting into "later means never". Use when the user says
  "lazy-mode debt", "what did lazy-mode defer", "list the shortcuts",
  "lazy-mode ledger", or "what did we mark to do later". One-shot report,
  changes nothing.
compatibility: opencode
---
# Lazy Mode Debt

Every deliberate lazy-mode shortcut is marked with a `lazy:` comment naming
its ceiling and upgrade path. The legacy `ponytail:` marker is also recognized.
This collects them into one ledger so a deferral can't quietly become permanent.

## Scan

Grep the repo for comment markers, skipping `node_modules`, `.git`, and build
output:

`grep -rnE '(#|//) ?(lazy|ponytail):' .`

Each hit is one ledger row. The comment prefix keeps prose that merely mentions
the convention out of the ledger.

## Output

One row per marker, grouped by file:

`<file>:<line>, <what was simplified>. ceiling: <the limit named>. upgrade: <the trigger to revisit>.`

The convention is `lazy: <ceiling>, <upgrade path>`, so pull the ceiling
and the trigger straight from the comment. Want an owner per row too? add
`git blame -L<line>,<line>`.

Flag the rot risk: any `lazy:` or `ponytail:` comment that names no upgrade
path or trigger gets a `no-trigger` tag, those are the ones that silently rot.

End with `<N> markers, <M> with no trigger.` Nothing found: `No lazy-mode debt. Clean ledger.`

## Boundaries

Reads and reports only, changes nothing. To persist it, ask and it writes the
ledger to a file (e.g. `LAZY-DEBT.md`). One-shot.
