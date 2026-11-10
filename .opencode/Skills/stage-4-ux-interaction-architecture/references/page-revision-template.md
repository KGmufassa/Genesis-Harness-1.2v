# CHANGE-ID — Revision summary

- Replace the JSON placeholders below; the record must contain exactly one JSON code block.
- Use one record for a baseline or multi-page revision. Add one pages entry per affected screen.
- Retain snapshots of exact UTF-8 bytes; compute diff using the documented Python expression.
- Link human review, approvals and downstream evidence below. Approval authority remains UX state.

```json
{
  "change_id": "CHANGE-ID",
  "requester": "unknown",
  "editor": "unknown",
  "reason": "<reason>",
  "timestamp": "<ISO timestamp>",
  "status": "needs_reconciliation",
  "history_gap": false,
  "affected_ids": ["SCREEN-001"],
  "validation_evidence": ["Build-Plans/Stage-4/Page-Revisions/Evidence/CHANGE-ID.md"],
  "impacts": [],
  "impacts_not_applicable": "<explanation or empty when impacts exist>",
  "pages": [
    {
      "screen_ref": "SCREEN-001",
      "before_hash": "",
      "after_hash": "<SHA-256>",
      "standards_hash": "<reviewed standard SHA-256>",
      "snapshot_path": "Build-Plans/Stage-4/Page-Revisions/Snapshots/CHANGE-ID/SCREEN-001.md",
      "diff": "",
      "approval": {
        "approval_status": "needs_user_review",
        "approved_hash": "",
        "approved_by": "",
        "approved_at": null
      }
    }
  ]
}
```

## Review and Propagation

- Approval references and affected artifacts:
- Validation results and resolution/route evidence:
- Superseded/reverted revision references where applicable:
