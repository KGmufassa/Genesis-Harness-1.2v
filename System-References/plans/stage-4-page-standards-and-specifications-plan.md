# Stage 4 Page Standards and Specification Improvements

## Summary

Strengthen the existing Stage 4 workflow so every in-scope screen has a complete Markdown specification, follows a shared page standard, and can be edited with traceable revisions. Preserve existing page folders, canonical JSON outputs, stable IDs, and approval gates.

---

## Implementation Changes

### Generate Shared Page Standards

- Require `Build-Plans/Stage-4/PAGE-STANDARDS.md` as a Stage 4 output.
- Derive it from the existing design-system foundation, accessibility framework, and interaction architecture; canonical JSON remains authoritative.
- Cover typography, colors, spacing, layout widths, breakpoints, assets/icons, shared components, navigation, controls, accessibility, and loading/empty/error states.
- Include exact font families, fallbacks, weights, sizes, and line heights or resolvable design-token references.
- Generate the initial standard before written page approval. Reconcile prototype-driven changes into canonical outputs and affected page specifications before renewed approval.

### Expand Individual Page Specifications

- Retain `Pages/<screen_id>/page-spec.md` and `Pages/README.md`.
- Add a required Assets table: reference, type, owning component, usage, source/planned location, availability, and accessibility treatment.
- Add a required Typography table: usage, token reference or concrete font properties, and page-specific overrides.
- Require a shared-standard link and a deviations section; explicitly record when no deviations or assets apply.
- Strengthen existing component and interaction tables with canonical IDs, ownership, control labels, route IDs and destinations, or action IDs and outcomes.
- Retain existing permissions, states, data, validation, responsive, and accessibility requirements.
- Reconcile the active screen inventory against approved workflows and journeys. Record excluded/deferred screens through existing UX decisions.

### Generate and Maintain Page Revisions

- Generate `Build-Plans/Stage-4/Page-Revisions/README.md` alongside the page specifications. Index baseline and subsequent revision records stored as `Page-Revisions/<change_id>.md`, using stable `CHANGE-` IDs.
- Establish each page's initial baseline with its screen ID, document path, content hash, creation attribution, and timestamp. Record subsequent edits without moving the page specification from its stable path.
- Each revision records requester/editor attribution when known, reason, timestamp, affected screen/component/control/route/design-system IDs, previous and new content hashes, and an exact diff or resolvable Git revision references. Mark unknown attribution explicitly rather than inventing it.
- Preserve the previous content through Git or a retained snapshot before agent edits. For direct user edits, compare against the last recorded baseline; if prior bytes cannot be recovered, record the history gap and require reconciliation rather than claiming a complete diff.
- Link records from the page index and revision index. A single change affecting multiple pages uses one record with separate before/after hashes and impact entries per page. Reuse an existing change-intake `CHANGE-` ID when applicable rather than creating a competing change record.
- Record affected canonical outputs, other pages, Stage 5 tickets, Stage 6 implementation/validation, and later-stage work where applicable. Give each impact a resolution, owner, and status, or an explicit not-applicable explanation.
- Follow `edit -> detect change -> record revision -> reconcile affected artifacts -> validate -> reapprove -> propagate downstream`. Preserve direct user edits; never regenerate over them from stale state.
- Invalidate affected written approvals using existing rules, including complete-set approval when screens are added or removed. Shared-standard changes must identify affected pages and reopen review where necessary.
- Record validation evidence, approval attribution and approved hashes, downstream propagation evidence, and revision status. Retain history when a change is superseded or reverted; record reversions as new linked revisions.
- Extend Stage 4 UX state and its schema with revision references and current baseline hashes. Keep detailed history in the revision records and existing approval metadata authoritative; use Git for exact file history where available.

### Strengthen Validation

- Extend the existing read-only page-specification validator rather than introducing a separate validation system.
- Require populated standard/page sections and reject empty tables and template placeholders. Accept explicit “not applicable” explanations where appropriate.
- Check page-standard links, documented component/control IDs, and route/action references against applicable canonical inventories.
- Separate draft and final checks: before prototype generation, validate written requirements and references already established; at final readiness, also reconcile against completed UI blueprints.
- Preserve hash validation, explicit per-page and complete-set approval, and user-edit protection.
- Check revision/index links, unique change IDs, baseline-to-revision hash continuity, and current specification hashes. Block prototype updates or readiness when changed pages lack a reconciled revision or current approval; report unresolved history gaps explicitly.
- At final readiness, require downstream impacts to be resolved or routed through the existing revision process with owners and evidence. Validators report gaps without generating records, changing files, or granting approval.
- Keep semantic completeness and workflow coverage subject to human review; structural checks cannot prove those independently.

### Update Workflow and Downstream Guidance

- Update the Stage 4 orchestrator, page template/review instructions, design-system skill, UI-blueprint skill, Stage 4 draft, and applicable readiness documentation together.
- Link the standard, individual specifications, and revision index from `09-complete-app-blueprint.md`.
- Update Stage 5/6 guidance to consume these links for planning, implementation, and visual QA.
- Preserve the Stage 5 handoff interface and Stage-4-local approval metadata. No new runtime dependencies or application implementation are required.

---

## Tests and Acceptance Criteria

- Add cases for missing standards, missing sections, placeholder content, incomplete asset/typography tables, omitted controls, unresolved destinations, invalid shared references, and stale approvals.
- Add passing cases for shared typography tokens, pages with no assets, action-only controls, responsive variants, and documented approved deviations.
- Verify draft checks work before final blueprints exist and final checks detect blueprint/specification mismatches.
- Test baseline creation, direct user edits, multi-page changes, shared-standard impact review, missing revision records, broken hash chains, unknown attribution, missing historical content, reapproval, downstream propagation, and superseded/reverted changes.
- Verify record creation preserves page content, and repeated reconciliation does not create duplicate records for an unchanged revision. Verify validators remain read-only.
- Run the page-specification tests and full readiness-audit suite:

```sh
python3 -m unittest discover -s .opencode/Skills/global-stage-readiness-audit/tests -p test_page_specifications.py
python3 -m unittest discover .opencode/Skills/global-stage-readiness-audit/tests
```

- Acceptance requires complete screen/file coverage, populated required content, consistent canonical references, traceable revision history from the recorded baseline, resolved or properly routed downstream impacts, and current approvals. Validators must remain read-only.

---

## Assumptions and Rollout

- Standards apply to all in-scope screens while permitting documented page-specific layouts.
- Agents author the Markdown using prescribed templates; a standalone document generator is unnecessary.
- Existing runs must meet the strengthened requirements before their next prototype mutation or final Stage 4 readiness approval.
- For existing pages, establish a baseline from current content without fabricating earlier history. Preserve prior approval evidence, but require reconciliation and reapproval where the strengthened requirements change the specification.
- Do not populate this repository’s empty Stage 4 with fictional application pages.
- Follow repository Python conventions and lazy-mode guidance during implementation.
