---
name: distill-conversation-context
description: Converts archived AI conversations into structured distilled reports with duplicate prevention via content hashing, then synthesizes project state using a reusable prompt template.
compatibility: opencode
---

# Distill Conversation Context

Use this skill when you have a folder of conversation markdown files that need to be converted into reusable operational memory for future agents.

## When To Use

- You have raw conversation files in `Memory/Context Thread archive/`
- You want deduplicated, structured summaries of each conversation
- You need a synthesized project state for agent onboarding
- You want to prevent re-processing unchanged files

## Scope

This skill processes only:
```
Memory/Context Thread archive/*.md
```

Outputs:
```
Memory/Distilled Context threads/<stem>-distilled.md
Memory/processed-files.json
Memory/processing-log.md
Memory/project-state.md
```

The reusable synthesis instructions live at
`.opencode/Skills/distill-conversation-context/references/synthesis-prompt.md`.

## Required Inputs

- Workspace root containing `Memory/` folder

## Output Contract

For each new/changed conversation file:
- One distilled markdown report in `Memory/Distilled Context threads/`
- Registry entry in `Memory/processed-files.json` with SHA256 hash
- Log entry in `Memory/processing-log.md`

Plus one project-state synthesis:
- `Memory/project-state.md` — generated from the reusable synthesis prompt template and distilled reports

## Workflow (7 Stages)

1. **Inventory** — Find all `*.md` files in source folder
2. **Duplicate Prevention** — SHA256 each file; skip if hash exists in registry
3. **Conversation Analysis** — Extract 9 categories via heuristic patterns (no LLM)
4. **Report Generation** — Render fixed template to `Distilled Context threads/`
5. **Registry Update** — Atomic upsert to `processed-files.json`
6. **Log Append** — Write timestamped line to `processing-log.md`
7. **Project-State Synthesis** — Load the reference prompt template and generate `project-state.md`

## Heuristic Extraction Categories (Stage 3)

| Category | Trigger Patterns |
|----------|------------------|
| Summary | First 3 non-empty paragraphs |
| State Changes | `changed\|updated\|migrated\|switched\|replaced` |
| Locked Decisions | `decided\|final\|locked\|approved` (exclude `maybe\|draft\|consider`) |
| New Knowledge | `learned\|discovered\|found that\|realized` |
| Resolved Problems | Nearby `error\|failed\|issue` plus `fixed\|resolved\|solved` |
| Unresolved Problems | Problem indicators without a nearby resolution |
| Repeated Mistakes | Duplicate error substrings (count ≥2) |
| User Preferences | `prefer\|always\|never\|standard\|convention` |
| Entities | Capitalized + suffixes (`Project\|Service\|Model\|Lib\|API\|SDK`) |
| Files | `[\w/-]+\.(md\|py\|json\|yaml\|toml\|txt)` |

## Determinism Rules

- Files processed in sorted path order
- Registry keyed by content hash, while retaining the source filename for traceability
- Template headings and section order fixed
- No LLM calls in skill — pure stdlib heuristics

## Stop Conditions

Stop and surface error if:
- Source folder missing
- Registry JSON malformed
- File read/write fails

## Verification

Before completion, confirm:
- Only new/changed files produced distilled reports
- Registry contains hash for every processed file
- Log has one line per file processed
- `references/synthesis-prompt.md` exists and `Memory/project-state.md` is generated when reports exist

## Script

```bash
python3 .opencode/Skills/distill-conversation-context/scripts/distill.py \
  [--force] [--dry-run] [--no-synthesize]
```

Flags:
- `--force` — Reprocess all files (ignore registry)
- `--dry-run` — Show what would be done, write nothing
- `--no-synthesize` — Skip Stage 7 project-state synthesis
