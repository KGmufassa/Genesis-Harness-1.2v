# UI Component System Maintenance

Normal Stage 4 runs must not edit this library.

Record candidate updates when:

- the same missing pattern appears across multiple products
- a template recommendation repeatedly produces poor page architecture
- an extension needs the same new page/component/state across multiple products
- two templates duplicate the same guidance
- a contradiction rule catches repeated failures
- a responsive rule repeatedly fails

Template gap record:

```json
{
  "gap": "",
  "affected_template_or_pattern": "",
  "project_context": "",
  "repeated_across_projects": false,
  "recommended_resolution": "",
  "evidence_refs": []
}
```

Maintenance workflow:

1. Review accumulated Stage 4 `template_gaps`.
2. Group repeated gaps by template, extension, pattern, or contradiction rule.
3. Update the smallest useful reference file.
4. Update `TEMPLATE-REGISTRY.md` or version notes when a template changes.
5. Keep changes structural; do not add visual design language or frontend code.

## Draft Template Graduation

Promote a template from `draft` to `stable` only when all conditions pass:

- at least three completed Stage 4 uses across at least two distinct products
- no unresolved high or critical `template_gaps`
- launch-critical desktop and mobile structures were validated
- accessibility and responsive transformations have evidence
- selector conditions and contradiction rules produced no unresolved routing conflict
- one maintainer records the evidence references and updates the template version to at least `1.0.0`

If evidence is incomplete, keep the template `draft`. A single successful project is not sufficient.
