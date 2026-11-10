# Written Page Specification Review

- Follow [Page Standards, Content and Revision Contract](page-standards-and-revisions.md) for required page content, standards, snapshots, revision records and draft/final gates.

- Run this phase after `ui-architecture-template-selection` and before creating or updating any Stitch project or screen. Read-only capability discovery may run earlier.
- Maintain the complete in-scope screen list in `screen_system.screen_inventory` in UX state; each entry has a stable `screen_id`. Include supporting, authentication, settings, and administrative screens when required by the approved product scope, not only launch-critical screens.
- Use these same `SCREEN-` IDs as `page_ref` in page inventories and blueprints. Preserve existing IDs; reconcile existing page aliases explicitly before review.
- Produce `Build-Plans/Stage-4/Pages/README.md` and one `Build-Plans/Stage-4/Pages/<screen_id>/page-spec.md` per screen, using `references/page-spec-template.md` relative to this skill. Stable ID folders survive page renames.
- The index must link each file using `[Page name](SCREEN-001/page-spec.md)` and show scope, platform coverage, and current approval status. Retain deferred/rejected scope decisions in `ux_decisions`; exclude them from the active screen set and preserve their documents outside `Pages/` if previously created.
- Use one specification for equivalent web/mobile screens with explicit platform differences. Split materially different workflows into separate screens. Describe ordinary states, modals, and drawers within their owning screen unless independently defined as screens.
- Cover purpose, users, permissions, upstream IDs, navigation, proposed layout regions, components, individual interactive elements and outcomes, data, validation, states, accessibility, responsive behavior, design direction, open questions, and review notes. Components and visual choices are proposals until prototype reconciliation.
- Read every existing specification before editing it. Compare it with canonical state and the recorded content hash, incorporate user edits into the screen, behavior, state, accessibility, and design constraints, and resolve conflicting changes with the user. Never overwrite user changes by regenerating from stale JSON.
- Route product-scope or backend changes through the existing prior-stage revision process. Resolve cross-page navigation and permission conflicts before approval.
- Record each document in `page_specifications` using the schema below. Hash the exact file bytes with SHA-256 after reconciliation. Hashes detect edits; they do not establish semantic reconciliation or user approval.
- Record approval only after explicit user confirmation of the presented content. A single explicit approval may cover the entire reviewed set. Do not infer approval from edits, silence, low-risk assumptions, prototype approval, or final-stage approval.
- Record complete-set approval separately in `page_set_approval`. Every active specification AND the complete page set must be approved before any Stitch generation; there is no page-by-page bypass.
- On any specification edit, set its status to `needs_user_review`, update `content_hash` after reconciliation, and clear its approved hash, approver, and timestamp. On screen addition/removal, also reset page-set approval. Shared constraint changes must be reflected in affected specifications and reapproved.
- Keep approval metadata in UX state; show review status in the index rather than rewriting approved specification bytes solely to change a status label.
- Immediately before every Stitch generation/update, including resumed runs, run the read-only gate below. Exit 1 means stop, report the blocking gaps, and use `blocked` while waiting for approval or `needs_current_stage_revision` for corrections. Do not call a mutating Stitch tool until it passes.
- Build prompts from approved specifications and reconciled canonical constraints. Limit generated page candidates to the approved screen set; new screen proposals must return through written review. Retain the existing post-generation prototype approval and suggestion-review ledgers as separate decisions.
- If prototype review changes a written specification, reconcile and reapprove the changed document before further generation or final readiness. Pure screenshot/evidence references may be kept in the index and existing Stitch ledger without changing the approved specification.
- Retain the existing explicit user decision for a non-Stitch fallback; fallback does not bypass written specification review.
- Final synthesis must preserve reviewed page files, link them from `09-complete-app-blueprint.md`, and reconcile final canonical JSON with their approved content. Do not silently replace them with generated summaries.
- `page_specifications` and `page_set_approval` remain Stage-4-local. Do not add fields to `stage_5_handoff` or impose new downstream Stitch dependencies.

## Review State

```json
{
  "page_specifications": [
    {
      "screen_ref": "SCREEN-001",
      "document_path": "Build-Plans/Stage-4/Pages/SCREEN-001/page-spec.md",
      "standards_hash": "",
      "content_hash": "",
      "approval_status": "needs_user_review",
      "approved_hash": "",
      "approved_by": "",
      "approved_at": null
    }
  ],
  "page_set_approval": {
    "approval_status": "needs_user_review",
    "approved_screen_refs": [],
    "approved_by": "",
    "approved_at": null
  }
}
```

## Read-Only Gate

```sh
python3 .opencode/Skills/global-stage-readiness-audit/scripts/page_specifications.py --workspace-root .
```

- Exit 0 confirms file coverage, relative index links, unique records, explicit approvals, and current approved hashes. It never writes files or grants approval. The Stage 4 readiness audit uses the same validator; other stages retain their existing behavior.
- Legacy Stage 4 runs must create and review the page files before their next Stitch mutation or readiness audit. Existing prototype approvals do not automatically approve written specifications.
