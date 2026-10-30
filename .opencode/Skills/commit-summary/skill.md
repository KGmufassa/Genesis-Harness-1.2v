---
name: commit-summary
description: Creates a concise commit title and brief 20-30 word description summarizing codebase changes from git diff, git status, changed files, or user-provided change notes.
origin: ECC
compatibility: opencode
---

# Commit Summary Skill

Use this skill when the user asks for:

* a commit title
* a commit summary
* a short commit description
* a title and 20-30 word description of codebase changes
* release-style summary from current changes

---

# Purpose

Create a concise commit-ready summary of changes.

The output must include:

```text
Title:
<short imperative or descriptive title>

Description:
<20-30 word description>
```

---

# Input Sources

Use the best available source:

1. User-provided change notes.
2. `git diff --stat`.
3. `git diff`.
4. `git status --short`.
5. Recently touched files if diff is unavailable.

Do not invent changes that are not visible in the provided context or repository state.

---

# Review Workflow

1. Identify the primary change theme.
2. Identify the affected subsystem or feature.
3. Separate core changes from incidental file churn.
4. Write a title that is specific but short.
5. Write a 20-30 word description that explains what changed and why it matters.

---

# Title Rules

The title should:

* be 5-12 words when possible
* use sentence case
* be specific to the main change
* avoid vague words like "updates" when a clearer verb exists
* avoid punctuation unless useful

Good examples:

```text
Add dynamic security review workflow
Create Stage 7 operationalization skills
Update build ticket agent assignment rules
```

---

# Description Rules

The description must:

* be 20-30 words
* summarize the concrete change
* mention the main affected area
* avoid implementation noise
* avoid exaggerated claims
* avoid listing every file

Good example:

```text
Adds dynamic security review behavior with changed-file scanning, contextual checks, severity reporting, permission-aware fixes, and updated registry routing metadata.
```

---

# Output Format

Return only:

```text
Title:
<title>

Description:
<20-30 word description>
```

If the change context is unclear, ask for the diff or change notes instead of guessing.

