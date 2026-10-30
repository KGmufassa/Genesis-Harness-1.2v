---
name: worktree-merge-manager
description: |
  Safely merges or discards a git worktree back into the main codebase.
  Requires explicit human confirmation before executing merge or discard actions.
compatibility: opencode
---

Use when:
  - Finishing feature development in a worktree
  - Merging completed work into main branch
  - Discarding failed or unwanted worktrees
  - Cleaning up isolated environments
---

# Worktree Merge Manager (With Confirmation)

Manages merging or discarding worktrees safely with explicit human approval.

---

# Execution Rules (MANDATORY)

- NEVER execute merge or delete without confirmation  
- ALWAYS show summary BEFORE action  
- ALWAYS validate clean state BEFORE asking  
- ALWAYS stop if user does not confirm  
- ALWAYS clean up after execution  

---

# Step 1 — Validate Worktree State

```bash
cd <worktree_path>
git status --porcelain
```
If dirty:
`STOP`

Output:
`"Worktree has uncommitted changes. Commit or stash before proceeding."`

# Step 2 — Prepare Summary

Collect:

- Branch name
- Base branch
- Action (merge or discard)
- Changed files
```
git log --oneline <base_branch>..<branch_name>
git diff --stat <base_branch>..<branch_name>
```
# Step 3 — Confirmation Prompt

Output:

### ACTION CONFIRMATION REQUIRED

Action: `<merge | discard>`
Branch:`<branch_name>`
Base:`<base_branch>`

**Changes:**

[List commit summary + diff stats]

**What will happen:**

If merge:

- Branch will be merged into `<base_branch>`

If discard:

- Branch will be permanently deleted

#### Confirm to proceed:

Type one of:
- `confirm merge`
- `confirm discard`
- `cancel`

# Step 4 — Await User Decision
If `cancel`:
- STOP
- Output: "Operation cancelled"

If confirmation does NOT match action:
- STOP
- Output: "Invalid confirmation"

If `confirmed`:
- Proceed

# Step 5 — Execute Action
### Merge
```
cd $(git rev-parse --show-toplevel)
git checkout <base_branch>
git pull origin <base_branch>
git merge <branch_name>
```
**If conflict:**
- STOP
- Output conflict files
- Require manual resolution

**Discard**
```
git branch -D <branch_name>
```
# Step 6 — Remove Worktree
```
git worktree remove <worktree_path>
git worktree prune
```
# Step 7 — Final Validation
```
git status
```
Ensure clean state.

## Final Output
#### WORKTREE OPERATION COMPLETE

**Action:**
`<merge | discard>`

**Branch:**
`<branch_name>`

**Base Branch:**
`<base_branch>`


**Result:**

- Completed successfully

**Cleanup:**

- Worktree removed
- Branch handled appropriately

**Status:**

- Repository clean
- Ready for next task
  
## Error Handling
### Dirty Worktree
- Block execution
### Merge Conflict
- Stop and report
### Invalid Confirmation
- Reject and stop

## Behavior Summary
- Human-in-the-loop safety
- Prevents accidental data loss
- Explicit confirmation required
- Clean and deterministic workflow
