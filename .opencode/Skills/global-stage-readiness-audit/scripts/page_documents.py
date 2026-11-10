"""Read-only content and revision checks for agent-authored Stage 4 documents."""
from __future__ import annotations

import difflib
import hashlib
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any, Mapping, Sequence

STAGE = Path('Build-Plans/Stage-4')
STANDARD = STAGE / 'PAGE-STANDARDS.md'
REVISIONS = STAGE / 'Page-Revisions'
SOURCES = ('design_system_foundation', 'accessibility_framework', 'interaction_architecture')
PAGE_SECTIONS = (
    'Purpose and Scope', 'Users and Permissions', 'Navigation',
    'Proposed Layout and Components', 'Components', 'Interactive Elements',
    'Assets', 'Typography', 'Shared Standard and Deviations', 'Data and Validation',
    'States and Flows', 'Accessibility and Platform Behavior',
    'Proposed Visual Direction', 'Review Notes',
)
STANDARD_SECTIONS = (
    'Sources', 'Typography', 'Colors', 'Spacing and Layout', 'Responsive Behavior',
    'Assets and Icons', 'Shared Components', 'Navigation and Controls',
    'Accessibility', 'UI States',
)
TABLES = {
    'Components': ('Component ID', 'Section', 'Purpose / shared reference'),
    'Interactive Elements': ('Element ID / label', 'Owning section / component', 'Trigger', 'Route / action / no navigation', 'Outcome / recovery', 'Permissions / confirmation'),
    'Assets': ('Asset reference', 'Type', 'Owning component', 'Usage', 'Source / planned location', 'Availability', 'Accessibility treatment'),
    'Typography': ('Usage', 'Token reference', 'Font family / fallback', 'Weight', 'Size', 'Line height', 'Overrides'),
}


def sha(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def source_hash(value: Any) -> str:
    return sha(json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(',', ':')).encode())


def read_local(root: Path, relative: str) -> bytes:
    if not isinstance(relative, str) or not relative:
        raise ValueError('reference must be a nonempty path')
    path = root / relative
    if Path(relative).is_absolute() or not path.resolve().is_relative_to(root.resolve()):
        raise ValueError('reference must stay inside workspace')
    return path.read_bytes()


def sections(text: str) -> dict[str, str]:
    # lazy: prescribed ATX headings and pipe tables only; use a Markdown parser if templates expand.
    parts = re.split(r'^## (.+?)\s*$', text, flags=re.M)
    return {parts[i]: parts[i + 1].strip() for i in range(1, len(parts), 2)}


def incomplete(value: str) -> bool:
    return not value.strip(' -\n') or bool(re.search(r'\b(TODO|TBD|PLACEHOLDER)\b|<[^>]+>', value, re.I))


def rows(body: str) -> list[list[str]]:
    result = []
    for line in body.splitlines():
        if line.strip().startswith('|'):
            cells = [cell.strip().strip('`') for cell in line.strip().strip('|').split('|')]
            if not all(re.fullmatch(r':?-+:?', cell) for cell in cells):
                result.append(cells)
    return result


def objects(value: Any) -> list[Mapping[str, Any]]:
    if isinstance(value, Mapping):
        return [value] + [item for child in value.values() for item in objects(child)]
    if isinstance(value, list):
        return [item for child in value for item in objects(child)]
    return []


def has_id(value: str, ref: str) -> bool:
    return bool(re.search(r'(?<![\w.-])' + re.escape(ref) + r'(?![\w.-])', value))


def content_errors(text: str, required: Sequence[str], label: str) -> list[str]:
    found = sections(text)
    errors = [f'{label}: missing or incomplete section {name}' for name in required if incomplete(found.get(name, ''))]
    if re.search(r'^- [^\n]+:\s*$', text, re.M):
        errors.append(f'{label}: unfilled template field')
    return errors


def token_exists(state: Mapping[str, Any], pointer: str) -> bool:
    value: Any = state.get('design_system_foundation', {})
    try:
        for key in pointer.removeprefix('token:').split('/')[1:]:
            value = value[key.replace('~1', '/').replace('~0', '~')]
        return isinstance(value, Mapping) and all(isinstance(value.get(key), (str, int, float)) and not incomplete(str(value[key])) for key in ('font_family', 'fallback', 'weight', 'size', 'line_height'))
    except (KeyError, TypeError, IndexError):
        return False


def validate_content(root: Path, state: Mapping[str, Any], ref: str, text: str, final: bool) -> list[str]:
    errors = content_errors(text, PAGE_SECTIONS, ref)
    found = sections(text)
    parsed: dict[str, list[list[str]]] = {}
    for name, header in TABLES.items():
        body = found.get(name, '')
        if name in ('Assets', 'Interactive Elements') and body.startswith('Not applicable:') and not incomplete(body.removeprefix('Not applicable:')):
            parsed[name] = []
            continue
        table = rows(body)
        if not table or table[0] != list(header) or len(table) < 2 or any(len(row) != len(header) or any(incomplete(cell) for cell in row) for row in table[1:]):
            errors.append(f'{ref}: incomplete {name} table')
        parsed[name] = table[1:]
    if '[Page standards](../../PAGE-STANDARDS.md)' not in found.get('Shared Standard and Deviations', ''):
        errors.append(f'{ref}: missing shared-standard link')
    for token in re.findall(r'token:/[\w/~.-]+', text):
        if not token_exists(state, token):
            errors.append(f'{ref}: unresolved typography token {token}')
    for row in parsed.get('Interactive Elements', []):
        if row and not re.fullmatch(r'UI-ELEMENT-[A-Za-z0-9._-]+ / .+', row[0]):
            errors.append(f'{ref}: control needs stable UI-ELEMENT-ID / label')
    component_ids = {row[0] for row in parsed.get('Components', []) if row}
    for row in parsed.get('Assets', []):
        if len(row) == 7 and row[2] not in component_ids:
            errors.append(f'{ref}: asset owner is not a documented component')
    for row in parsed.get('Typography', []):
        if len(row) == 7 and row[1] != 'none' and not re.fullmatch(r'token:/[\w/~.-]+', row[1]):
            errors.append(f'{ref}: typography requires a token reference or none')
        if len(row) == 7 and row[1] == 'none' and any(cell.lower() in ('inherited', 'none', 'n/a') for cell in row[2:6]):
            errors.append(f'{ref}: concrete typography needs family/fallback, weight, size and line height')
    blueprints = state.get('ui_blueprints', [])
    page = [p for p in blueprints if isinstance(p, Mapping) and p.get('page_ref') == ref] if isinstance(blueprints, list) else []
    if final and not page:
        errors.append(f'{ref}: final blueprint missing')
    canonical = objects(page)
    for key in ('component_inventory', 'interactive_element_inventory'):
        canonical += [p for p in objects(state.get(key, [])) if p.get('page_ref') == ref or ref in (p.get('owning_page_refs') or [])]
    for component in objects(page):
        if component.get('component_id'):
            for element in component.get('interactive_elements', []) or []:
                if isinstance(element, Mapping):
                    canonical.append({**element, 'owning_component_ref': component['component_id']})
    for key, heading in (('component_id', 'Components'), ('element_id', 'Interactive Elements')):
        identifiers = [row[0].split(' / ')[0] for row in parsed.get(heading, []) if row]
        if len(identifiers) != len(set(identifiers)):
            errors.append(f'{ref}: duplicate {key} in specification')
        for obj in canonical:
            identifier = obj.get(key)
            if isinstance(identifier, str) and identifier and identifier not in identifiers:
                errors.append(f'{ref}: omitted {key} {identifier}')
        known = {p[key] for p in objects([state.get('ui_blueprints', []), state.get('component_inventory', []), state.get('interactive_element_inventory', [])]) if isinstance(p.get(key), str) and p[key]}
        for row in parsed.get(heading, []):
            identifier = row[0].split(' / ')[0] if row else ''
            if (final or known) and identifier not in known:
                errors.append(f'{ref}: unknown {key} {identifier}')
    for prefix, inventory, key in (('ROUTE', 'route_inventory', 'route_id'), ('ACTION', 'action_inventory', 'action_id')):
        known = {p[key]: p for p in objects(state.get(inventory, [])) if isinstance(p.get(key), str)}
        for identifier in set(re.findall(r'\b' + prefix + r'-[\w.-]+', text)):
            if (final or known) and identifier not in known:
                errors.append(f'{ref}: unresolved {identifier}')
    route_map = {p.get('route_id'): p for p in objects(state.get('route_inventory', [])) if p.get('route_id')}
    for row in parsed.get('Interactive Elements', []):
        if len(row) != 6:
            continue
        target = row[3]
        if not re.search(r'\b(?:ROUTE|ACTION)-[\w.-]+|\bno_navigation\b', target):
            errors.append(f'{ref}: control lacks route/action/no_navigation')
        for identifier in re.findall(r'\bROUTE-[\w.-]+', target):
            route = route_map.get(identifier)
            if route and (not route.get('path') or not re.search(r'(?<!\S)' + re.escape(route['path']) + r'(?!\S)', target)):
                errors.append(f'{ref}: route destination mismatch for {identifier}')
        for obj in canonical:
            if obj.get('element_id') and has_id(row[0], obj['element_id']):
                for key in ('route_id', 'action_id'):
                    if obj.get(key) and not has_id(target, obj[key]):
                        errors.append(f'{ref}: control target differs from canonical {obj[key]}')
                if obj.get('behavior') == 'no_navigation' and target != 'no_navigation':
                    errors.append(f'{ref}: control no_navigation classification differs from canonical')
                owners = (obj.get('owning_component_refs') or []) + ([obj['owning_component_ref']] if obj.get('owning_component_ref') else [])
                if any(not has_id(row[1], owner) for owner in owners):
                    errors.append(f'{ref}: control owner mismatch')
    return errors


def validate_documents(root: Path, state: Mapping[str, Any], documents: Mapping[str, str], final: bool) -> list[str]:
    errors: list[str] = []
    try:
        standard = read_local(root, str(STANDARD))
        errors += content_errors(standard.decode('utf-8'), STANDARD_SECTIONS, 'Page standards')
        meta = state.get('page_standards', {})
        if not isinstance(meta, Mapping) or meta.get('content_hash') != sha(standard):
            errors.append('Page standards: missing or stale content hash')
        sources = meta.get('source_hashes', {}) if isinstance(meta, Mapping) else {}
        for key in SOURCES:
            if not isinstance(sources, Mapping) or sources.get(key) != source_hash(state.get(key, {})) or not state.get(key):
                errors.append(f'Page standards: missing or stale source {key}')
        for record in state.get('page_specifications', []):
            if isinstance(record, Mapping) and record.get('standards_hash') != sha(standard):
                errors.append(f"{record.get('screen_ref')}: shared standard changed; reconcile and reapprove")
    except (OSError, UnicodeError, ValueError) as exc:
        errors.append(f'Page standards: missing or unreadable ({exc})')
    for ref, text in documents.items():
        errors += validate_content(root, state, ref, text, final)
    if final:
        try:
            blueprint = read_local(root, str(STAGE / '09-complete-app-blueprint.md')).decode('utf-8')
            links = set(re.findall(r'\[[^\]\n]+\]\(([^)]+)\)', blueprint))
            required_links = {'PAGE-STANDARDS.md', 'Page-Revisions/README.md'} | {f'Pages/{ref}/page-spec.md' for ref in documents}
            for target in sorted(required_links - links):
                errors.append(f'Complete app blueprint: missing link {target}')
        except (OSError, UnicodeError, ValueError):
            errors.append('Complete app blueprint: missing or unreadable')
    errors += validate_revisions(root, state, documents, final)
    return errors


def validate_revisions(root: Path, state: Mapping[str, Any], documents: Mapping[str, str], final: bool) -> list[str]:
    errors: list[str] = []
    try:
        index = read_local(root, str(REVISIONS / 'README.md')).decode('utf-8')
        page_index = read_local(root, str(STAGE / 'Pages/README.md')).decode('utf-8')
    except (OSError, UnicodeError, ValueError):
        return ['Page revisions: missing revision or page index']
    refs = state.get('page_revisions', [])
    if not isinstance(refs, list):
        return ['Page revisions: page_revisions must be a list']
    seen: set[str] = set()
    latest: dict[str, bytes] = {}
    baselines: dict[str, str] = {}
    approvals: dict[str, Any] = {}
    standards: dict[str, str] = {}
    for entry in refs:
        try:
            if not isinstance(entry, Mapping) or not re.fullmatch(r'CHANGE-[\w.-]+', str(entry.get('change_id', ''))):
                raise ValueError('invalid change reference')
            change = entry['change_id']
            if change in seen:
                raise ValueError('duplicate change ID')
            seen.add(change)
            relative = REVISIONS / f'{change}.md'
            if entry.get('document_path') != str(relative):
                raise ValueError('incorrect record path')
            text = read_local(root, str(relative)).decode('utf-8')
            blocks = re.findall(r'^```json\s*\n(.*?)^```\s*$', text, re.M | re.S)
            if len(blocks) != 1:
                raise ValueError('record must contain one JSON block')
            record = json.loads(blocks[0])
            if not isinstance(record, dict) or record.get('change_id') != change:
                raise ValueError('record ID mismatch')
            for field in ('requester', 'editor', 'reason', 'timestamp'):
                if not isinstance(record.get(field), str) or incomplete(record[field]):
                    raise ValueError(f'missing {field}; use unknown for unavailable attribution')
            datetime.fromisoformat(record['timestamp'].replace('Z', '+00:00'))
            if record.get('status') not in ('reconciled', 'closed', 'superseded'):
                raise ValueError('revision not reconciled')
            if record.get('history_gap') is not False:
                raise ValueError('unresolved history gap')
            if not isinstance(record.get('affected_ids'), list) or not record['affected_ids']:
                raise ValueError('missing affected IDs')
            evidence = record.get('validation_evidence', [])
            if not isinstance(evidence, list) or not evidence:
                raise ValueError('missing validation evidence')
            for path in evidence:
                read_local(root, path)
            if f']({change}.md)' not in index or f'](../Page-Revisions/{change}.md)' not in page_index:
                raise ValueError('missing revision index link')
            impacts = record.get('impacts', [])
            if not isinstance(impacts, list) or (not impacts and incomplete(record.get('impacts_not_applicable', ''))):
                raise ValueError('missing impact assessment')
            for impact in impacts:
                if not isinstance(impact, Mapping) or any(not isinstance(impact.get(k), str) or incomplete(impact[k]) for k in ('ref', 'owner', 'status', 'resolution')):
                    raise ValueError('incomplete downstream impact')
                if not isinstance(impact.get('evidence', []), list):
                    raise ValueError('impact evidence must be a list')
                if final:
                    if impact['status'] not in ('resolved', 'routed') or not impact.get('evidence'):
                        raise ValueError('downstream impact needs resolution or owned revision route and evidence')
                    for path in impact['evidence']:
                        read_local(root, path)
            pages = record.get('pages', [])
            if not isinstance(pages, list) or not pages:
                raise ValueError('missing changed pages')
            changed: set[str] = set()
            for page in pages:
                ref = page['screen_ref']
                if ref in changed or ref not in record['affected_ids']:
                    raise ValueError('duplicate page or missing affected screen ID')
                changed.add(ref)
                snapshot_path = page['snapshot_path']
                if not snapshot_path.startswith(str(REVISIONS / 'Snapshots') + '/'):
                    raise ValueError('snapshot must be retained under Page-Revisions/Snapshots')
                if not (root / snapshot_path).resolve().is_relative_to((root / REVISIONS / 'Snapshots').resolve()):
                    raise ValueError('snapshot resolves outside retained history')
                content = read_local(root, snapshot_path)
                previous = latest.get(ref, b'')
                if page['before_hash'] != (sha(previous) if ref in latest else '') or page['after_hash'] != sha(content):
                    raise ValueError(f'{ref}: broken hash chain or snapshot mismatch')
                standard_hash = page.get('standards_hash', '')
                if not isinstance(standard_hash, str) or not re.fullmatch(r'[a-f0-9]{64}', standard_hash):
                    raise ValueError(f'{ref}: missing standards hash in revision')
                if ref in latest:
                    if content == previous and standards.get(ref) == standard_hash:
                        raise ValueError('unchanged page must reuse its latest revision')
                    diff = ''.join(difflib.unified_diff(previous.decode('utf-8').splitlines(keepends=True), content.decode('utf-8').splitlines(keepends=True), fromfile='before', tofile='after'))
                    if page.get('diff') != diff:
                        raise ValueError(f'{ref}: exact diff mismatch')
                else:
                    if page.get('diff', ''):
                        raise ValueError('baseline cannot claim a prior diff')
                    baselines[ref] = sha(content)
                latest[ref] = content
                approvals[ref] = page.get('approval', {})
                standards[ref] = standard_hash
        except (OSError, UnicodeError, ValueError, TypeError, KeyError, AttributeError) as exc:
            errors.append(f'Page revisions: {entry!s}: {exc}')
    if state.get('page_baselines') != baselines:
        errors.append('Page revisions: baseline hashes do not match history')
    for ref, text in documents.items():
        if latest.get(ref) != text.encode('utf-8'):
            errors.append(f'{ref}: missing reconciled revision for current content')
    for record in state.get('page_specifications', []):
        if isinstance(record, Mapping) and record.get('screen_ref') in documents:
            if standards.get(record['screen_ref']) != record.get('standards_hash'):
                errors.append(f"{record['screen_ref']}: latest revision lacks current shared-standard review")
            approval = approvals.get(record['screen_ref'], {})
            if not isinstance(approval, Mapping) or any(approval.get(key) != record.get(key) for key in ('approval_status', 'approved_hash', 'approved_by', 'approved_at')):
                errors.append(f"{record['screen_ref']}: latest revision lacks matching approval evidence")
    for path in (root / REVISIONS).glob('CHANGE-*.md'):
        if path.stem not in seen:
            errors.append(f'Page revisions: unindexed record {path.name}')
    return errors
