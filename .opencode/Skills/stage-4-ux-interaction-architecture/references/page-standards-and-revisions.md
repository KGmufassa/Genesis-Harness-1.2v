# Page Standards, Content and Revision Contract

## Generation and Canonical Sources

- Generate `Build-Plans/Stage-4/PAGE-STANDARDS.md` after design-system foundation and template selection, before written page approval, using `page-standards-template.md`.
- Derive rules from UX state's `design_system_foundation`, `accessibility_framework`, and `interaction_architecture`. Populate all ten template sections; canonical JSON remains authoritative. Do not introduce a new Stage 5 handoff interface.
- Set `page_standards.content_hash` to SHA-256 of exact standard bytes. Set `source_hashes` for each of the three source keys to SHA-256 of `json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(',', ':')).encode()`.
- Set each `page_specifications` record's `standards_hash` after reconciling its content with the current standard. Updating hashes is not approval. A changed standard reopens review of affected pages; assess every active page before recording unchanged applicability.
- Reconcile screen coverage against approved workflows/journeys, including supporting screens; retain explicit exclusion/defer decisions. Automation checks the listed set; human review establishes its completeness.

## Required Page Content

- Use all headings and exact table headers from `page-spec-template.md`. Populate every cell; replace placeholders and empty field prompts before approval.
- List each canonical component in Components, and each individual control in Interactive Elements, using `element_id / label` in the first cell. Preserve owning section/component IDs. Targets contain `ROUTE-ID /actual/path`, `ACTION-ID` with outcome/recovery, or `no_navigation` with behavior.
- Assets require a reference, type, owning component, usage, source/planned location, availability and accessibility treatment. Planned assets are allowed; describe the intended location and status without claiming files exist.
- Assets or Interactive Elements may instead contain `Not applicable: <specific reason>` when none exist. Canonical controls still cannot be omitted.
- Typography requires one row per usage. Use `token:/typography_tokens/body` (a JSON pointer into `design_system_foundation`) or `none` plus concrete family/fallback, weight, size and line height. A token must resolve to an object with `font_family`, `fallback`, `weight`, `size` and `line_height`. A token row may use `inherited` for properties supplied by a populated shared token; overrides must be explicit or `none`.
- Shared Standard and Deviations must link `[Page standards](../../PAGE-STANDARDS.md)` and list approved deviations or explicitly none. Ordinary page-specific layouts are permitted.
- Keep platform differences, permissions, states, validation and review notes meaningful. Use explicit not-applicable explanations instead of blank cells.

## Revision Lifecycle

- Generate `Page-Revisions/README.md` alongside `Pages/README.md`; do not create fictional app pages in this harness repository. Use `page-revision-template.md` for records under `Page-Revisions/<change_id>.md`.
- Establish a baseline for each new or existing screen: retain its exact content snapshot, empty `before_hash`, calculated `after_hash`, attribution and timestamp. Do not fabricate pre-baseline history or approvals.
- Store chronological references in UX state `page_revisions`: objects with `change_id` and workspace-relative `document_path`. Store initial hashes in `page_baselines`, mapping screen IDs to baseline SHA-256 strings. Preserve removed-screen history even after the active set changes.
- Reserve globally unique `CHANGE-` IDs; reuse the authoritative change-intake ID and link its record when applicable. A record may include multiple pages, with separate hashes and immutable snapshot paths under `Page-Revisions/Snapshots/<change_id>/`.
- Before agent edits, retain previous bytes. For user edits compare against the last snapshot, preserve current user bytes and reconcile canonical state. Unknown requester/editor attribution must be `unknown`; never infer approval or invent historical content.
- For revisions, `before_hash` must match the previous snapshot hash and `after_hash` the new snapshot hash. Store the reviewed `standards_hash` in each page entry, including baselines. When standards change without page-byte changes, create a new standards-review revision with the new standards hash and empty page diff; document affected-page assessment and renewed approval. Store the exact diff computed by `''.join(difflib.unified_diff(before.decode('utf-8').splitlines(keepends=True), after.decode('utf-8').splitlines(keepends=True), fromfile='before', tofile='after'))`. Baselines have empty diff.
- If historical bytes are missing, set `history_gap: true`, explain the gap and stop generation/readiness until recovered or a transparently reviewed baseline is established; never claim an exact historical diff without bytes.
- Link `[CHANGE-ID](CHANGE-ID.md)` from the revision index and `[CHANGE-ID](../Page-Revisions/CHANGE-ID.md)` from the page index. Link revision records, affected IDs and related standards changes in human review notes.
- Record reason, ISO timestamp, requester/editor, affected IDs, validation evidence paths, status and per-page history in the single JSON block. Evidence paths must resolve inside the workspace. Keep approval attribution/hashes in authoritative page approval state; copy its `approval_status`, `approved_hash`, `approved_by`, and `approved_at` into each latest revision page entry's `approval` object after explicit approval, and link that evidence in the human review section. This is an audit copy, not an alternative approval authority.
- Assess canonical outputs, other pages, Stage 5 tickets, Stage 6 implementation/validation and later-stage work. Each impact uses `ref`, `owner`, `status`, `resolution`, and `evidence` (workspace-relative paths). If no impacts exist, give a specific `impacts_not_applicable` explanation.
- Follow edit -> record -> reconcile -> validate -> reapprove -> propagate. Set status `needs_reconciliation` while incomplete, `reconciled` when ready for written review, and `closed` after completion. Retain `superseded` records and create a new linked revision for reversions.
- Invalidate edited pages' approvals and reset complete-set approval on screen additions/removals using existing rules. Never automatically grant approval, including when user edits appear minor.
- Agent authorship must be idempotent: if current bytes and reviewed standard hash match the latest record, reuse that revision rather than creating a duplicate. Validators never create records or write documents.

## Gates and Handoff

- Before every prototype mutation run `page_specifications.py --workspace-root . --phase draft`. It checks populated content, current standards/source hashes, available canonical references, revision history and current approvals without requiring future blueprints.
- Final Stage 4 audit calls the same validator with final checks: every active screen has a blueprint, component/control and route/action references resolve, and downstream impacts are resolved or routed with owner, resolution and local evidence.
- Reconcile prototype changes into standards, page files, snapshots, canonical outputs and approvals before further generation or readiness.
- Link standards, pages and the revision index from `09-complete-app-blueprint.md`. Stage 5/6 consume these links and record impacted work against the same IDs without new downstream Stitch dependencies.
