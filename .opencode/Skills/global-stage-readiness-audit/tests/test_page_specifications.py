from __future__ import annotations

import hashlib
import difflib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
from page_specifications import validate_page_specifications  # noqa: E402
from workflow_validation import validate_schema  # noqa: E402
from page_document_fixtures import seed_page_documents
from page_documents import validate_content, sha, source_hash, SOURCES


class PageSpecificationTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.pages = self.root / "Build-Plans/Stage-4/Pages"
        self.state_path = self.root / "Build-Plans/Build-status/UX-state.json"
        self.state_path.parent.mkdir(parents=True)
        self.approval = {"approval_status": "approved", "approved_by": "user", "approved_at": "2026-10-30T12:00:00Z"}
        self.state: dict[str, Any] = {
            "screen_system": {"screen_inventory": []},
            "page_specifications": [],
            "page_set_approval": {"approved_screen_refs": [], **self.approval},
        }
        for number, name in enumerate(("Dashboard", "Settings"), 1):
            ref = f"SCREEN-{number:03}"
            path = self.pages / ref / "page-spec.md"
            path.parent.mkdir(parents=True)
            path.write_text(f"# {name}\n\nWeb/mobile variants, modal, loading and recovery states.\n", encoding="utf-8")
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            self.state["screen_system"]["screen_inventory"].append({"screen_id": ref})
            self.state["page_specifications"].append({"screen_ref": ref, "document_path": path.relative_to(self.root).as_posix(), "content_hash": digest, "approved_hash": digest, **self.approval})
            self.state["page_set_approval"]["approved_screen_refs"].append(ref)
        (self.pages / "README.md").write_text("[Dashboard](SCREEN-001/page-spec.md)\n[Settings](SCREEN-002/page-spec.md)\n", encoding="utf-8")
        seed_page_documents(self.root, self.state)

    def errors(self) -> str:
        return "\n".join(validate_page_specifications(self.root, self.state))

    def run_gate(self) -> subprocess.CompletedProcess[str]:
        self.state_path.write_text(json.dumps(self.state), encoding="utf-8")
        return subprocess.run([sys.executable, str(SCRIPTS / "page_specifications.py"), "--workspace-root", str(self.root)], capture_output=True, text=True)

    def test_approved_set_passes_without_mutation(self) -> None:
        self.state_path.write_text(json.dumps(self.state), encoding="utf-8")
        before = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        result = self.run_gate()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertTrue(json.loads(result.stdout)["passed"])
        after = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.assertEqual(before, after)

    def test_edit_preserved_and_requires_reapproval_even_after_hash_refresh(self) -> None:
        path = self.pages / "SCREEN-002/page-spec.md"
        content = b"# User changes\n\nDifferent mobile workflow.\n"
        path.write_bytes(content)
        self.state["page_specifications"][1]["content_hash"] = hashlib.sha256(content).hexdigest()
        result = self.run_gate()
        self.assertEqual(result.returncode, 1)
        self.assertIn("matching approved content hash", result.stdout)
        self.assertEqual(path.read_bytes(), content)
        self.state["page_specifications"][1]["approved_hash"] = hashlib.sha256(content).hexdigest()
        self.assertIn("missing reconciled revision", self.errors())

    def test_one_unapproved_page_blocks_entire_set_despite_prototype_approval(self) -> None:
        self.state["page_specifications"][1]["approval_status"] = "needs_user_review"
        self.state["stitch_prototyping"] = {"approved_page_refs": ["SCREEN-001", "SCREEN-002"]}
        self.assertIn("SCREEN-002: explicit written-specification approval", self.errors())

    def test_approval_requires_attribution_and_complete_set_confirmation(self) -> None:
        for key in ("approved_by", "approved_at"):
            with self.subTest(key=key):
                original = self.state["page_specifications"][0][key]
                self.state["page_specifications"][0][key] = " "
                self.assertIn("explicit written-specification approval", self.errors())
                self.state["page_specifications"][0][key] = original
        self.state["page_set_approval"]["approval_status"] = "needs_user_review"
        self.assertIn("approval of the complete page set is missing", self.errors())

    def test_missing_and_duplicate_records_block(self) -> None:
        self.state["page_specifications"] = [self.state["page_specifications"][0]] * 2
        errors = self.errors()
        self.assertIn("duplicate review records", errors)
        self.assertIn("SCREEN-002: missing", errors)

    def test_missing_document_and_index_link_block(self) -> None:
        (self.pages / "SCREEN-001/page-spec.md").unlink()
        (self.pages / "README.md").write_text("# Pages\n", encoding="utf-8")
        errors = self.errors()
        self.assertIn("specification is missing", errors)
        self.assertIn("lacks a relative specification link", errors)

    def test_added_and_removed_screens_invalidate_page_set(self) -> None:
        self.state["screen_system"]["screen_inventory"].append({"screen_id": "SCREEN-003"})
        self.assertIn("page-set approval does not match", self.errors())
        self.assertIn("SCREEN-003: missing", self.errors())
        self.state["screen_system"]["screen_inventory"] = [{"screen_id": "SCREEN-001"}]
        self.assertIn("page-set approval does not match", self.errors())
        self.assertIn("unexpected screen SCREEN-002", self.errors())

    def test_unlisted_blueprint_and_extra_file_block(self) -> None:
        self.state["ui_blueprints"] = [{"page_ref": "SCREEN-003"}]
        path = self.pages / "duplicate/page-spec.md"
        path.parent.mkdir()
        path.write_text("# Duplicate", encoding="utf-8")
        self.assertIn("outside the screen inventory", self.errors())
        self.assertIn("unindexed specification", self.errors())

    def test_malformed_state_and_wrong_paths_block(self) -> None:
        self.state["page_specifications"][0]["document_path"] = "../elsewhere.md"
        self.assertIn("document_path must be", self.errors())
        self.state["page_set_approval"] = []
        self.assertIn("approval of the complete page set is missing", self.errors())
        self.state["screen_system"] = []
        self.assertIn("must list every in-scope screen", self.errors())

    def test_schema_accepts_review_records_and_rejects_invalid_status(self) -> None:
        repository = SCRIPTS.parents[3]
        schema = repository / "System-References/Schemas/stage-4-output.schema.json"
        # Common stage fields are exercised by the readiness fixture; inspect review errors here.
        errors = validate_schema(self.state, schema, repository)
        self.assertFalse(any("page_specifications" in error or "page_set_approval" in error for error in errors), errors)
        self.state["page_specifications"][0]["approval_status"] = "assumed_low_risk"
        self.assertTrue(any("approval_status" in error for error in validate_schema(self.state, schema, repository)))


    def read_revision(self, index: int = 0) -> dict[str, Any]:
        path = self.root / self.state['page_revisions'][index]['document_path']
        return json.loads(path.read_text(encoding='utf-8').split('```json\n')[1].split('```')[0])

    def write_revision(self, record: dict[str, Any], index: int = 0) -> None:
        path = self.root / self.state['page_revisions'][index]['document_path']
        path.write_text('# Revision\n\n```json\n' + json.dumps(record) + '\n```\n', encoding='utf-8')

    def add_revision(self, change: str = 'CHANGE-EDIT-1', refs: tuple[str, ...] = ('SCREEN-001',), *, revert: bool = False) -> None:
        pages = []
        for ref in refs:
            record = next(r for r in self.state['page_specifications'] if r['screen_ref'] == ref)
            path = self.root / record['document_path']
            before = path.read_bytes()
            after = (self.root / self.read_revision(0)['pages'][0]['snapshot_path']).read_bytes() if revert else before + b'Additional reviewed requirements.\n'
            path.write_bytes(after)
            digest = sha(after)
            record.update(content_hash=digest, approved_hash=digest)
            snapshot = self.root / f'Build-Plans/Stage-4/Page-Revisions/Snapshots/{change}/{ref}.md'
            snapshot.parent.mkdir(parents=True, exist_ok=True)
            snapshot.write_bytes(after)
            pages.append({'screen_ref': ref, 'before_hash': sha(before), 'after_hash': digest, 'standards_hash': record['standards_hash'], 'snapshot_path': str(snapshot.relative_to(self.root)), 'diff': ''.join(difflib.unified_diff(before.decode().splitlines(keepends=True), after.decode().splitlines(keepends=True), fromfile='before', tofile='after')), 'approval': {k: record[k] for k in ('approval_status', 'approved_hash', 'approved_by', 'approved_at')}})
        revision = self.read_revision()
        revision.update(change_id=change, reason='Reviewed user edit', affected_ids=list(refs), pages=pages)
        self.state['page_revisions'].append({'change_id': change, 'document_path': f'Build-Plans/Stage-4/Page-Revisions/{change}.md'})
        self.write_revision(revision, -1)
        for relative, link in (('Page-Revisions/README.md', f'[{change}]({change}.md)'), ('Pages/README.md', f'[{change}](../Page-Revisions/{change}.md)')):
            path = self.root / 'Build-Plans/Stage-4' / relative
            path.write_text(path.read_text() + '\n' + link, encoding='utf-8')

    def test_missing_standard_and_stale_shared_sources_block(self) -> None:
        self.state['design_system_foundation']['new_rule'] = 'Different shared type'
        self.assertIn('stale source design_system_foundation', self.errors())
        (self.root / 'Build-Plans/Stage-4/PAGE-STANDARDS.md').unlink()
        self.assertIn('Page standards: missing or unreadable', self.errors())

    def test_standard_edit_requires_page_reconciliation(self) -> None:
        path = self.root / 'Build-Plans/Stage-4/PAGE-STANDARDS.md'
        path.write_bytes(path.read_bytes() + b'Changed shared rule.\n')
        self.state['page_standards']['content_hash'] = sha(path.read_bytes())
        self.assertIn('shared standard changed; reconcile and reapprove', self.errors())

    def test_required_sections_placeholders_and_tables(self) -> None:
        path = self.pages / 'SCREEN-001/page-spec.md'
        content = path.read_text()
        for before, after, expected in (
            ('## Assets', '## Removed Assets', 'section Assets'),
            ('400 | 16px', 'TBD | 16px', 'incomplete Typography'),
            ('COMP-1 | Main', 'COMP-1 | ', 'incomplete Components'),
            ('Not applicable: This informational screen uses text only and has no controls or media.', 'Not applicable:', 'incomplete Assets'),
        ):
            with self.subTest(expected=expected):
                errors = validate_content(self.root, self.state, 'SCREEN-001', content.replace(before, after), False)
                self.assertIn(expected, '\n'.join(errors))

    def test_valid_shared_typography_and_invalid_token(self) -> None:
        self.state['design_system_foundation']['typography_tokens'] = {'body': {'font_family': 'Arial', 'fallback': 'sans-serif', 'weight': 400, 'size': '16px', 'line_height': '24px'}}
        text = (self.pages / 'SCREEN-001/page-spec.md').read_text().replace('none | Arial, sans-serif | 400 | 16px | 24px', 'token:/typography_tokens/body | inherited | inherited | inherited | inherited')
        self.assertEqual(validate_content(self.root, self.state, 'SCREEN-001', text, False), [])
        self.assertIn('unresolved typography token', '\n'.join(validate_content(self.root, self.state, 'SCREEN-001', text.replace('/body', '/missing'), False)))

    def test_draft_accepts_no_blueprint_final_requires_one(self) -> None:
        self.state['ui_blueprints'] = []
        self.assertEqual(self.errors(), '')
        self.assertIn('final blueprint missing', '\n'.join(validate_page_specifications(self.root, self.state, final=True)))

    def test_omitted_control_and_wrong_destination(self) -> None:
        blueprint = self.state['ui_blueprints'][0]
        component = blueprint['sections'][0]['components'][0]
        component['interactive_elements'] = [{'element_id': 'UI-ELEMENT-001', 'route_id': 'ROUTE-001', 'owning_component_ref': 'COMP-1'}]
        self.state['route_inventory'] = [{'route_id': 'ROUTE-001', 'path': '/settings'}]
        text = (self.pages / 'SCREEN-001/page-spec.md').read_text()
        self.assertIn('omitted element_id', '\n'.join(validate_content(self.root, self.state, 'SCREEN-001', text, True)))
        table = '| ' + ' | '.join(('Element ID / label', 'Owning section / component', 'Trigger', 'Route / action / no navigation', 'Outcome / recovery', 'Permissions / confirmation')) + ' |\n|---|---|---|---|---|---|\n| UI-ELEMENT-001 / Settings | Main / COMP-1 | Click | ROUTE-001 /wrong | Opens settings | All users |'
        text = text.replace('## Interactive Elements\n\nNot applicable: This informational screen uses text only and has no controls or media.', '## Interactive Elements\n\n' + table)
        self.assertIn('route destination mismatch', '\n'.join(validate_content(self.root, self.state, 'SCREEN-001', text, True)))
        self.assertEqual(validate_content(self.root, self.state, 'SCREEN-001', text.replace('/wrong', '/settings'), True), [])
        self.assertIn('unresolved ROUTE-002', '\n'.join(validate_content(self.root, self.state, 'SCREEN-001', text.replace('ROUTE-001', 'ROUTE-002'), True)))

    def test_multi_page_revision_preserves_history_and_approvals(self) -> None:
        self.add_revision(refs=('SCREEN-001', 'SCREEN-002'))
        self.assertEqual(self.errors(), '')
        self.assertEqual(validate_page_specifications(self.root, self.state, final=True), [])
        before = {p: p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        self.assertEqual(self.errors(), '')
        self.assertEqual(before, {p: p.read_bytes() for p in self.root.rglob('*') if p.is_file()})

    def test_hash_chain_diff_snapshot_and_history_gap(self) -> None:
        self.add_revision()
        valid = self.read_revision(-1)
        for field, value, expected in (('before_hash', '0' * 64, 'broken hash chain'), ('diff', 'invented diff', 'exact diff mismatch'), ('snapshot_path', '../missing.md', 'snapshot must be retained')):
            record = json.loads(json.dumps(valid))
            record['pages'][0][field] = value
            self.write_revision(record, -1)
            self.assertIn(expected, self.errors())
        valid['history_gap'] = True
        self.write_revision(valid, -1)
        self.assertIn('unresolved history gap', self.errors())

    def test_revision_indices_duplicate_ids_and_missing_approval_evidence(self) -> None:
        self.state['page_revisions'].append(self.state['page_revisions'][0])
        self.assertIn('duplicate change ID', self.errors())
        self.state['page_revisions'].pop()
        record = self.read_revision()
        record['pages'][0]['approval'] = {}
        self.write_revision(record)
        self.assertIn('matching approval evidence', self.errors())
        (self.root / 'Build-Plans/Stage-4/Page-Revisions/README.md').write_text('# Empty')
        self.assertIn('missing revision index link', self.errors())

    def test_final_downstream_impacts_need_owned_resolution_and_evidence(self) -> None:
        record = self.read_revision()
        record['impacts'] = [{'ref': 'TICKET-001', 'owner': 'agent', 'status': 'pending', 'resolution': 'Awaiting reconciliation', 'evidence': []}]
        self.write_revision(record)
        self.assertEqual(self.errors(), '')
        self.assertIn('downstream impact needs resolution', '\n'.join(validate_page_specifications(self.root, self.state, final=True)))
        record['impacts'][0].update(status='routed', resolution='Owned Stage 5 revision', evidence=record['validation_evidence'])
        self.write_revision(record)
        self.assertEqual(validate_page_specifications(self.root, self.state, final=True), [])

    def test_superseded_revision_and_reversion_remain_in_chain(self) -> None:
        self.add_revision()
        record = self.read_revision(-1)
        record['status'] = 'superseded'
        self.write_revision(record, -1)
        self.add_revision('CHANGE-REVERT-1', revert=True)
        self.assertEqual(self.errors(), '')

    def test_unrecoverable_snapshot_blocks_and_unknown_attribution_is_allowed(self) -> None:
        self.assertEqual(self.errors(), '')
        record = self.read_revision()
        (self.root / record['pages'][0]['snapshot_path']).unlink()
        self.assertIn('Page revisions:', self.errors())



    def test_action_only_and_non_navigation_controls(self) -> None:
        text = (self.pages / 'SCREEN-001/page-spec.md').read_text()
        component = self.state['ui_blueprints'][0]['sections'][0]['components'][0]
        control = {'element_id': 'UI-ELEMENT-001', 'action_id': 'ACTION-SAVE', 'owning_component_ref': 'COMP-1'}
        component['interactive_elements'] = [control]
        self.state['action_inventory'] = [{'action_id': 'ACTION-SAVE', 'name': 'Save'}]
        table = '| ' + ' | '.join(('Element ID / label', 'Owning section / component', 'Trigger', 'Route / action / no navigation', 'Outcome / recovery', 'Permissions / confirmation')) + ' |\n|---|---|---|---|---|---|\n| UI-ELEMENT-001 / Save | Main / COMP-1 | Click | ACTION-SAVE | Saves data; retry on failure | Editor |'
        text = text.replace('## Interactive Elements\n\nNot applicable: This informational screen uses text only and has no controls or media.', '## Interactive Elements\n\n' + table)
        self.assertEqual(validate_content(self.root, self.state, 'SCREEN-001', text, True), [])
        control.pop('action_id')
        control['behavior'] = 'no_navigation'
        self.assertEqual(validate_content(self.root, self.state, 'SCREEN-001', text.replace('ACTION-SAVE', 'no_navigation'), True), [])
        self.assertIn('control owner mismatch', '\n'.join(validate_content(self.root, self.state, 'SCREEN-001', text.replace('Main / COMP-1', 'Main / wrong'), True)))

    def test_assets_require_a_documented_component(self) -> None:
        text = (self.pages / 'SCREEN-001/page-spec.md').read_text()
        table = '| ' + ' | '.join(('Asset reference', 'Type', 'Owning component', 'Usage', 'Source / planned location', 'Availability', 'Accessibility treatment')) + ' |\n|---|---|---|---|---|---|---|\n| Hero | Image | COMP-1 | Header | assets/hero.png | Planned | Decorative, empty alt |'
        text = text.replace('## Assets\n\nNot applicable: This informational screen uses text only and has no controls or media.', '## Assets\n\n' + table)
        self.assertEqual(validate_content(self.root, self.state, 'SCREEN-001', text, False), [])
        self.assertIn('asset owner', '\n'.join(validate_content(self.root, self.state, 'SCREEN-001', text.replace('Image | COMP-1', 'Image | wrong'), False)))

    def test_unchanged_duplicate_revision_rejected(self) -> None:
        self.add_revision()
        record = self.read_revision(-1)
        record['change_id'] = 'CHANGE-NOOP'
        record['pages'][0]['before_hash'] = record['pages'][0]['after_hash']
        record['pages'][0]['diff'] = ''
        self.state['page_revisions'].append({'change_id': 'CHANGE-NOOP', 'document_path': 'Build-Plans/Stage-4/Page-Revisions/CHANGE-NOOP.md'})
        self.write_revision(record, -1)
        for relative, link in (('Page-Revisions/README.md', '[No-op](CHANGE-NOOP.md)'), ('Pages/README.md', '[No-op](../Page-Revisions/CHANGE-NOOP.md)')):
            path = self.root / 'Build-Plans/Stage-4' / relative
            path.write_text(path.read_text() + '\n' + link, encoding='utf-8')
        self.assertIn('unchanged page must reuse', self.errors())

    def test_standard_only_revision_requires_recorded_review(self) -> None:
        path = self.root / 'Build-Plans/Stage-4/PAGE-STANDARDS.md'
        path.write_bytes(path.read_bytes() + b'Updated shared spacing rule.\n')
        digest = sha(path.read_bytes())
        self.state['page_standards']['content_hash'] = digest
        for page in self.state['page_specifications']:
            page['standards_hash'] = digest
        self.assertIn('latest revision lacks current shared-standard review', self.errors())
        for number, page in enumerate(self.state['page_specifications'], 1):
            change = f'CHANGE-STANDARD-{number}'
            record = self.read_revision(number - 1)
            record.update(change_id=change, reason='Reviewed shared rule; page content remains valid')
            record['pages'][0].update(before_hash=page['content_hash'], standards_hash=digest)
            self.state['page_revisions'].append({'change_id': change, 'document_path': f'Build-Plans/Stage-4/Page-Revisions/{change}.md'})
            self.write_revision(record, -1)
            for relative, link in (('Page-Revisions/README.md', f'[{change}]({change}.md)'), ('Pages/README.md', f'[{change}](../Page-Revisions/{change}.md)')):
                index = self.root / 'Build-Plans/Stage-4' / relative
                index.write_text(index.read_text() + '\n' + link, encoding='utf-8')
        self.assertEqual(self.errors(), '')

    def test_complete_app_blueprint_links_required_at_final_gate(self) -> None:
        path = self.root / 'Build-Plans/Stage-4/09-complete-app-blueprint.md'
        path.write_text('# Summary only', encoding='utf-8')
        self.assertEqual(self.errors(), '')
        errors = '\n'.join(validate_page_specifications(self.root, self.state, final=True))
        self.assertIn('missing link PAGE-STANDARDS.md', errors)
        self.assertIn('missing link Page-Revisions/README.md', errors)


if __name__ == "__main__":
    unittest.main()
