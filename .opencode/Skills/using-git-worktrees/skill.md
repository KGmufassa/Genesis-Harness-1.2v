---
name: git-worktree-orchestrator
description: |
  Creates an isolated git worktree for feature development with automatic
  directory selection, safety verification, environment setup, and baseline validation.
compatibility: opencode
---
  Use when:
  - Starting new feature development
  - Running implementation plans
  - Executing tasks in isolation
  - Avoiding branch switching conflicts
  ---

# Git Worktree Orchestrator

Creates a clean, isolated development workspace using git worktrees.

---

# Execution Rules (MANDATORY)

- ALWAYS create worktree before implementation tasks
- ALWAYS verify directory is gitignored (for local directories)
- NEVER proceed if baseline tests fail without explicit confirmation
- NEVER assume directory location
- ALWAYS follow directory selection priority
- ALWAYS auto-detect project setup
- ALWAYS validate clean baseline

---

# Step 1 — Determine Worktree Directory

## Priority Order

### 1. Existing Directories

Check:

```bash
ls -d .worktrees 2>/dev/null
ls -d worktrees 2>/dev/null
```
Rules:

If .worktrees exists → use it
Else if worktrees exists → use it
If both → prefer .worktrees

### 2. Check Project Config (CLAUDE.md)

```
grep -i "worktree.*director" CLAUDE.md 2>/dev/null
```
If directory defined → use it

### 3. Fallback

If no directory exists:

Default to:
```
.worktrees/
```

# Step 2 — Safety Verification

If using project-local directory:
```
git check-ignore -q .worktrees || git check-ignore -q worktrees
```
**If NOT ignored:**
 **1.** Add to .gitignore
 **2.** Commit immediately
```
echo ".worktrees/" >> .gitignore
git add .gitignore
git commit -m "chore: add worktrees directory to gitignore"
```
# Step 3 — Detect Project Name
```
project=$(basename "$(git rev-parse --show-toplevel)")
```
# Step 4 — Create Worktree
```
git worktree add .worktrees/<branch-name> -b <branch-name>
cd .worktrees/<branch-name>
```
# Step 5 — Auto Setup Environment

Detect and run setup:
```
# Node.js
if [ -f package.json ]; then npm install; fi

# Python
if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
if [ -f pyproject.toml ]; then poetry install; fi

# Rust
if [ -f Cargo.toml ]; then cargo build; fi

# Go
if [ -f go.mod ]; then go mod download; fi
```
# Step 6 — Baseline Test Verification

Run appropriate test command:
```
npm test || \
pytest || \
cargo test || \
go test ./...
```
**If tests FAIL:**

- STOP execution
- Report failure
- Require explicit user confirmation to continue

**If tests PASS:**
- Proceed

# Step 7 — Output Result

Return:

### WORKTREE READY
```
Path:
<absolute-path>

Branch:
<branch-name>

Setup:
Dependencies installed

Tests:
Passing

Status:
Ready for development
```
## Error Handling
- Directory Not Ignored
- Fix .gitignore
- Commit immediately
- Retry

## Tests Failing
- Stop execution
- Report failures
- Await instruction

## Missing Setup Files
Skip setup
Continue safely
---
## Behavior Summary
- Deterministic directory selection
- Safe git isolation
- Automatic environment setup
- Clean baseline enforcement
- Fully compatible with:
  - task orchestrators
  - MVP analyzers
  - implementation agents
