---
name: document-to-skill-package
description: Use when converting a structured markdown document plus a mapping file into a Codex skill package under .opencode/skills. Creates SKILL.md and mapped reference files by splitting the source document on top-level headings in deterministic order.
compatibility: opencode
---

# Document To Skill Package

Use this skill when a user wants to convert one large markdown document into a skill package with a `SKILL.md` router and a set of `references/*.md` files.

## When To Use

- The user has a source markdown document containing multiple top-level sections.
- The user has a mapping file that defines the target skill folder and reference file names.
- The user wants the content separated into a real skill package under `.opencode/skills/`.
- The split should be deterministic and based on document structure, not freeform rewriting.

## Required Inputs

- Source markdown document path
- Mapping file path
- Target skill root, usually `.opencode/skills`

## Expected Source Format

- The source document uses top-level markdown headings (`# `) as section boundaries.
- The first top-level section becomes the content basis for `SKILL.md`.
- Remaining top-level sections map in order to the mapped reference files.

## Expected Mapping Format

The mapping file should define a structure like:

```text
backend-development/
├── SKILL.md
└── references/
    ├── backend-api-design.md
    ├── backend-architecture.md
```

Rules:
- exactly one skill root directory
- exactly one `SKILL.md`
- one or more `references/*.md` files
- file order in the mapping controls output order

## Workflow

1. Read the mapping file and extract:
   - skill package name
   - reference file paths in order
2. Read the source document and split it on top-level headings.
3. Validate:
   - source has at least two top-level sections
   - mapped reference count matches source sections after the first section
4. Run the bundled converter script.
5. Verify all mapped files exist in the target package.
6. If counts or structure do not match, stop and ask the user instead of guessing.

## Script

Use:

```bash
python3 .opencode/skills/document-to-skill-package/scripts/convert_doc_to_skill.py \
  --source-doc <source-doc> \
  --mapping-file <mapping-file> \
  --target-root .opencode/skills
```

Optional flags:

- `--force` to overwrite an existing target package

## Output Rules

- Keep the first top-level section as `SKILL.md`.
- Write each remaining top-level section to the next mapped reference file in order.
- Preserve section headings and body content.
- Do not invent extra files.
- Do not silently drop unmatched sections.

## Stop Conditions

Stop and ask the user if:

- the mapping file does not define a valid skill structure
- the source document does not use top-level headings cleanly
- the number of mapped reference files does not match the number of source sections after the first
- the target package already exists and overwrite was not requested

## Verification

After conversion, confirm:

- `SKILL.md` exists
- every mapped reference file exists
- no unexpected files were created

