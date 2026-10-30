---
name: skill-registry-builder
description: Scans non-stage skills in .opencode/Skills, extracts structured metadata, infers missing capability data, and generates a standardized JSON registry optimized for agent-task-builder and rule-engine compatibility.
compatibility: opencode
---

# Skill Registry Builder

## Purpose

This skill builds a normalized registry from the local skills folder.

It scans only:

```text
.opencode/Skills
```

It excludes skills associated with Stage 1 through Stage 8 command or subskill execution.

The output is a clean structured JSON registry for agent-task-builder compatibility.

## Core Responsibilities

- scan all non-stage skills in `.opencode/Skills`
- read each skill instruction file deeply
- extract explicit metadata from frontmatter and body content
- infer missing metadata from workflow rules, triggers, inputs, outputs, and constraints
- normalize capabilities into rule-engine friendly fields
- record excluded stage-associated skills
- generate a standardized JSON registry
- validate that every included skill has actionable matching metadata

## Exclusion Rules

Exclude any skill that is:

- a Stage 1 through Stage 8 command skill
- a Stage 1 through Stage 8 subskill
- primarily responsible for stage orchestration, stage output generation, or stage-gated product planning

The skill must not exclude general-purpose engineering, design, debugging, worktree, security, or documentation packaging skills unless they are explicitly tied to a stage.

## Required Scan Behavior

1. List all folders under `.opencode/Skills`.
2. Identify the primary instruction file for each folder:
   - `SKILL.md`
   - `skill.md`
   - another markdown file if no canonical filename exists
   - known nonstandard skill files when present
3. Skip non-skill filesystem artifacts such as `.DS_Store`.
4. Classify each skill as stage-associated or non-stage.
5. Process every non-stage skill.
6. Record every excluded stage-associated skill with an exclusion reason.

## Metadata Extraction Contract

Each included skill must produce:

```json
{
  "skill_id": "",
  "name": "",
  "folder": "",
  "source_path": "",
  "stage_associated": false,
  "description": "",
  "domains": [],
  "capabilities": [],
  "task_triggers": [],
  "input_requirements": [],
  "outputs": [],
  "tools_or_scripts": [],
  "references": [],
  "constraints": [],
  "rule_engine_tags": [],
  "selection_priority": "normal",
  "risk_flags": [],
  "inferred_metadata": false
}
```

## Inference Rules

Infer metadata when frontmatter is incomplete.

Use:

- headings to infer domains
- workflow steps to infer capabilities
- "When to use" sections to infer task triggers
- "Required inputs" and examples to infer input requirements
- "Outputs" sections to infer output types
- constraints and prohibited actions to infer risk flags
- references and scripts to infer dependencies

Mark `inferred_metadata` as `true` when any important field required inference.

## Agent Task Builder Compatibility

The registry must include top-level rule-engine metadata:

```json
{
  "generated_for": "agent-task-builder",
  "rule_engine": {
    "matching_fields": [],
    "selection_strategy": "",
    "compatibility_notes": []
  }
}
```

The matching fields must support routing by:

- skill ID
- name
- aliases
- description
- domains
- capabilities
- task triggers
- input requirements
- output types
- risk flags
- rule-engine tags

## Output Location

Write the registry to:

```text
System-References/skill-regisry/skill-registry.json
```

Use the folder name exactly as written.

## Validation Checklist

Before completion, confirm:

- all folders in `.opencode/Skills` were considered
- all Stage 1 through Stage 8 skills were excluded
- all non-stage skills were included
- every included skill has capabilities
- every included skill has task triggers
- every included skill has rule-engine tags
- registry JSON is valid
- output path exists

## Completion Output

Return:

- number of skills scanned
- number of skills included
- number of skills excluded
- output file path
- validation status
