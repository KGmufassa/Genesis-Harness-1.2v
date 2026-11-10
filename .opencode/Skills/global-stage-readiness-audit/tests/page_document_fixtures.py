"""Complete agent-authored document fixtures for Stage 4 gate tests."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from page_documents import PAGE_SECTIONS, STANDARD_SECTIONS, TABLES, SOURCES, sha, source_hash


def seed_page_documents(root: Path, state: dict[str, Any]) -> None:
    stage = root / 'Build-Plans/Stage-4'
    for key in SOURCES:
        state[key] = state.get(key) or {'rules': 'Approved shared rules'}
    standard = '# Page Standards\n\n' + ''.join(f'## {name}\n\nApproved concrete rules for {name}.\n\n' for name in STANDARD_SECTIONS)
    (stage / 'PAGE-STANDARDS.md').write_text(standard, encoding='utf-8')
    standard_hash = sha(standard.encode())
    state['page_standards'] = {'content_hash': standard_hash, 'source_hashes': {key: source_hash(state[key]) for key in SOURCES}}
    state['page_baselines'] = {}
    state['page_revisions'] = []
    revision_index = []
    page_index = []
    state['ui_blueprints'] = []
    state['visual_spec_inventory'] = [{'visual_spec_id': 'VISUAL-SPEC-TEST', 'approval_status': 'approved'}]
    for number, record in enumerate(state['page_specifications'], 1):
        ref = record['screen_ref']
        component = f'COMP-{number}'
        content = f'# {ref}\n\n'
        for heading in PAGE_SECTIONS:
            body = f'Approved {heading.lower()} requirements, including mobile differences and recovery.'
            if heading in TABLES:
                header = TABLES[heading]
                body = '| ' + ' | '.join(header) + ' |\n|' + '---|' * len(header)
                if heading == 'Components':
                    body += f'\n| {component} | Main | Shared content component |'
                elif heading in ('Assets', 'Interactive Elements'):
                    body = 'Not applicable: This informational screen uses text only and has no controls or media.'
                else:
                    body += '\n| Body | none | Arial, sans-serif | 400 | 16px | 24px | none |'
            if heading == 'Shared Standard and Deviations':
                body = '[Page standards](../../PAGE-STANDARDS.md)\n\nDeviations: none.'
            content += f'## {heading}\n\n{body}\n\n'
        path = root / record['document_path']
        path.write_text(content, encoding='utf-8')
        digest = sha(path.read_bytes())
        record.update(content_hash=digest, approved_hash=digest, standards_hash=standard_hash)
        state['ui_blueprints'].append({'page_ref': ref, 'sections': [{'components': [{'component_id': component}]}]})
        change = f'CHANGE-BASE-{number}'
        snapshot = stage / f'Page-Revisions/Snapshots/{change}/{ref}.md'
        snapshot.parent.mkdir(parents=True, exist_ok=True)
        snapshot.write_bytes(path.read_bytes())
        evidence = stage / f'Page-Revisions/Evidence/{change}.md'
        evidence.parent.mkdir(parents=True, exist_ok=True)
        evidence.write_text('# Review\n\nCanonical content reconciled and checked.\n', encoding='utf-8')
        revision = {'change_id': change, 'requester': 'unknown', 'editor': 'agent', 'reason': 'Establish baseline', 'timestamp': '2026-11-09T12:00:00Z', 'status': 'reconciled', 'history_gap': False, 'affected_ids': [ref], 'validation_evidence': [str(evidence.relative_to(root))], 'impacts': [], 'impacts_not_applicable': 'Initial planning; no implementation exists.', 'pages': [{'screen_ref': ref, 'before_hash': '', 'after_hash': digest, 'standards_hash': standard_hash, 'snapshot_path': str(snapshot.relative_to(root)), 'diff': '', 'approval': {key: record[key] for key in ('approval_status', 'approved_hash', 'approved_by', 'approved_at')}}]}
        target = stage / f'Page-Revisions/{change}.md'
        target.write_text('# Baseline\n\n```json\n' + json.dumps(revision, indent=2) + '\n```\n', encoding='utf-8')
        state['page_revisions'].append({'change_id': change, 'document_path': str(target.relative_to(root))})
        state['page_baselines'][ref] = digest
        revision_index.append(f'[{change}]({change}.md)')
        page_index.append(f'[{ref}]({ref}/page-spec.md) [{change}](../Page-Revisions/{change}.md)')
    (stage / 'Page-Revisions/README.md').write_text('\n'.join(revision_index), encoding='utf-8')
    (stage / 'Pages/README.md').write_text('\n'.join(page_index), encoding='utf-8')
    (stage / '09-complete-app-blueprint.md').write_text('# Complete app blueprint\n\n[Standards](PAGE-STANDARDS.md)\n[Revisions](Page-Revisions/README.md)\n' + '\n'.join(f"[{record['screen_ref']}](Pages/{record['screen_ref']}/page-spec.md)" for record in state['page_specifications']), encoding='utf-8')
