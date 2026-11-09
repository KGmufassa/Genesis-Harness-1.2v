"""Render the reviewed Markdown plan as a portable HTML reading edition."""
from __future__ import annotations

import argparse
import html
import re
from pathlib import Path
from typing import Any, Sequence

DOCS = Path("System-References/Docs")
PLAN_NAME = "Stage-1-8-A-Grade-Improvement-Patch-Plan"

def inline(value: str) -> str:
    tokens = []
    def code(match: re.Match) -> str:
        tokens.append('<code>' + html.escape(match.group(1)) + '</code>')
        return f'\x00{len(tokens)-1}\x00'
    value = re.sub(r'`([^`]+)`', code, value)
    value = html.escape(value)
    value = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', value)
    for index, token in enumerate(tokens):
        value = value.replace(f'\x00{index}\x00', token)
    return value

def render(text: str) -> str:
    # lazy: render only this document's headings, paragraphs, lists, tables, and fences;
    # use a Markdown library if future source content adds other syntax.
    lines = text.strip().splitlines()
    result = []
    index = 0
    while index < len(lines):
        line = lines[index].strip()
        if not line or line == '---':
            index += 1
            continue
        if line.startswith('```'):
            language = line[3:].strip() or 'text'
            index += 1
            code = []
            while index < len(lines) and not lines[index].strip().startswith('```'):
                code.append(lines[index]); index += 1
            result.append('<div class="code-wrap"><span class="code-label">' + html.escape(language) + '</span><pre><code>' + html.escape('\n'.join(code)) + '</code></pre></div>')
            index += 1
            continue
        if line.startswith('|'):
            rows = []
            while index < len(lines) and lines[index].strip().startswith('|'):
                row = lines[index].strip().strip('|')
                # The source tables use backticks but have no pipe-containing cells.
                cells = [cell.strip() for cell in row.split('|')]
                if not all(re.fullmatch(r':?-+:?', cell) for cell in cells):
                    rows.append(cells)
                index += 1
            header = '<tr>' + ''.join('<th scope="col">' + inline(cell) + '</th>' for cell in rows[0]) + '</tr>'
            body = ''.join('<tr>' + ''.join('<td>' + inline(cell) + '</td>' for cell in row) + '</tr>' for row in rows[1:])
            result.append('<div class="table-wrap" tabindex="0" role="region" aria-label="Scrollable reference table"><table><thead>' + header + '</thead><tbody>' + body + '</tbody></table></div>')
            continue
        heading = re.match(r'^#{1,6}\s+(.+)', line)
        if heading:
            result.append('<h3>' + inline(heading.group(1)) + '</h3>')
            index += 1
            continue
        bullet = re.match(r'^(?:[-*]|\d+\.)\s+', line)
        if bullet:
            ordered = bool(re.match(r'^\d+\.', line))
            tag = 'ol' if ordered else 'ul'
            items = []
            while index < len(lines):
                item = re.match(r'^(?:\d+\.|[-*])\s+(.+)', lines[index].strip())
                if not item: break
                items.append('<li>' + inline(item.group(1)) + '</li>'); index += 1
            result.append(f'<{tag}>' + ''.join(items) + f'</{tag}>')
            continue
        paragraph = [line]; index += 1
        while index < len(lines) and lines[index].strip() and not re.match(r'^(?:#|```|\||---$|[-*]\s|\d+\.\s)', lines[index].strip()):
            paragraph.append(lines[index].strip()); index += 1
        result.append('<p>' + inline(' '.join(paragraph)) + '</p>')
    return '\n'.join(result)

def split_blocks(raw: str) -> list[dict[str, Any]]:
    major = {"Purpose", "Current Health Baseline", "Latest Diagnostic Run", "Latest Health Check", "Patch Overview", "Follow-Up Patch Overview", "Implementation Strategy", "Review Checklist For Future Hardening", "Expected Result"}
    blocks: list[dict[str, Any]] = []
    current = None
    fenced = False
    for line in raw.splitlines():
        if line.strip().startswith("```"):
            fenced = not fenced
        match = re.match(r"^# (.+)$", line) if not fenced else None
        title = match.group(1) if match else ""
        patch = re.match(r"^Patch (\d+) [—–-] (.+)", title)
        boundary = title in major or title.startswith("Current Enforcement Backlog") or patch
        if boundary:
            current = {"title": title, "number": int(patch.group(1)) if patch else 0, "lines": []}
            blocks.append(current)
        elif current is not None:
            current["lines"].append(line)
    if fenced:
        raise ValueError("Markdown has an unclosed code fence")
    numbers = [b["number"] for b in blocks if b["number"]]
    if not numbers or len(numbers) != len(set(numbers)):
        raise ValueError("Plan requires unique numbered Patch headings")
    ids: set[str] = set()
    for block in blocks:
        block["id"] = f"patch-{block['number']}" if block["number"] else re.sub(r"[^a-z0-9]+", "-", block["title"].lower()).strip("-")
        if block["id"] in ids:
            raise ValueError(f"Duplicate section anchor: {block['id']}")
        ids.add(block["id"])
        body = "\n".join(block["lines"])
        status = re.search(r"^## Implementation Status\s*\n(.*?)(?=\n## |\Z)", body, re.S | re.M)
        block["status"] = re.sub(r"^[\s*-]+|[\s*]+$", "", status.group(1)).splitlines()[0] if status and status.group(1).strip() else "Historical reference; see current coverage table"
        block["pending"] = bool(re.search(r"\b(planned|pending|open|not implemented|not executed)\b", block["status"], re.I))
        block["body"] = render(body)
    return blocks


def report_metrics(report: str) -> dict[str, str]:
    score = re.search(r"Overall harness health:\s*\*\*([^*]+)\*\*", report)
    date = re.search(r"Diagnostic date:\s*\*\*([^*]+)\*\*", report)
    tests = re.search(r"\|\s*All (?:repository Python|discovered repository test) suites\s*\|\s*\*\*([^*]+)\*\*", report)
    open_section = re.search(r"^## (?:Open Findings|Newly Confirmed Gaps|Confirmed Open Findings)\s*\n(.*?)(?=\n## |\Z)", report, re.S | re.M)
    findings = str(len(set(re.findall(r"RISK-HEALTH-\d+", open_section.group(1))))) if open_section else "Not assessed"
    return {"score": score.group(1).strip() if score else "Not assessed", "date": date.group(1).strip() if date else "Not recorded", "tests": tests.group(1).strip() if tests else "Not recorded", "findings": findings}


def render_html(plan: str, report: str) -> str:
    blocks = split_blocks(plan)
    metrics = report_metrics(report)
    patches = [b for b in blocks if b["number"]]
    pending = [b for b in patches if b["pending"]]
    reference = [b for b in patches if not b["pending"]]
    sections = [b for b in blocks if not b["number"]]
    assets = Path(__file__).resolve().parents[1] / "assets"
    css = (assets / "report.css").read_text(encoding="utf-8")
    script = (assets / "report.js").read_text(encoding="utf-8")

    def links(items: Sequence[dict[str, Any]]) -> str:
        return "".join(f'<a href="#{b["id"]}">{html.escape(b["title"])}</a>' for b in items)

    def section(block: dict[str, Any]) -> str:
        return f'<section class="section" id="{block["id"]}"><h2>{html.escape(block["title"])}</h2>{block["body"]}</section>'

    def card(block: dict[str, Any]) -> str:
        opened = " open" if block["pending"] else ""
        title = re.sub(r"^Patch \d+ [—–-] ", "", block["title"])
        return f'<details class="patch" id="{block["id"]}" data-patch="{block["number"]}"{opened}><summary><span class="patch-number">{block["number"]:02}</span><span class="patch-title">{html.escape(title)}<span class="patch-meta">{inline(block["status"])}</span></span><span class="toggle" aria-hidden="true">+</span></summary><div class="patch-body">{block["body"]}</div></details>'

    overview = [b for b in sections if b["title"] not in {"Patch Overview", "Follow-Up Patch Overview"}]
    historical = [b for b in sections if b not in overview]
    content = "".join(section(b) for b in overview)
    content += '<section aria-labelledby="open-patches"><div class="group-heading"><span class="eyebrow">REMAINING WORK</span><h2 id="open-patches">Open and pending patches</h2><p>Priorities and acceptance criteria come from the reviewed Markdown plan.</p></div>'
    content += "".join(card(b) for b in pending) or '<p>No patches are marked open or pending. Consult the health findings before inferring full readiness.</p>'
    content += '</section><section id="historical-foundation"><div class="group-heading"><span class="eyebrow">REFERENCE</span><h2>Implemented work and foundation</h2><p>Completion labels reflect the Markdown source; they do not imply completed live validation.</p></div>'
    content += "".join(section(b) for b in historical) + "".join(card(b) for b in reference) + "</section>"
    cards = (("Current health assessment", metrics["score"], "Engineering judgment from the health report"), ("Repository tests", metrics["tests"], "Recorded checks, not proof of live operation"), ("Confirmed open findings", metrics["findings"], "From the report's open-findings section"), ("Open or pending patches", str(len(pending)), "Derived from implementation status"))
    stats = "".join(f'<div class="metric"><span>{html.escape(label)}</span><strong>{html.escape(value)}</strong><small>{html.escape(note)}</small></div>' for label, value, note in cards)
    date = html.escape(metrics["date"])
    footer_links = ((PLAN_NAME + ".md", "Markdown plan"), ("Stage-1-8%20Health%20Report.mdx", "Health report"), ("Stage-1-8-Improvement-Implementation-Record.md", "Implementation record"), ("Stage-1-8-Supervised-Pilot-Runbook.md", "Pilot runbook"))
    footer = "".join(f'<a href="{path}">{label}</a>' for path, label in footer_links)
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Stage 1–8 · Improvement Patch Plan</title><style>{css}</style></head>
<body><a class="skip" href="#main">Skip to content</a><aside class="sidebar"><div class="brand">GENESIS<small>WORKFLOW HEALTH</small></div><nav aria-label="Plan navigation"><p class="nav-label">Assessment</p>{links(sections)}<p class="nav-label">Open and pending</p>{links(pending)}<details><summary>Implemented and historical</summary>{links(reference)}</details></nav><div class="nav-footer">Stage 1–8 harness<br>{date}</div></aside>
<main id="main"><header><span class="eyebrow">ENGINEERING IMPROVEMENT PLAN</span><h1>Stage 1–8<span>A-grade improvement patch plan</span></h1><p class="intro">Current findings, planned improvements, and verified implementation history in one reading edition.</p><div class="header-meta"><span class="pill">Reviewed health and patch status</span><span class="pill neutral">{date}</span></div></header><div class="metrics">{stats}</div>
<div class="toolbar"><div class="search"><label for="patch-search">Find a patch</label><input id="patch-search" type="search" placeholder="Search patches and acceptance criteria…"></div><button id="expand" type="button">Expand all</button><button id="collapse" type="button">Collapse all</button><button id="print" type="button">Print / save PDF</button></div><p id="search-status" role="status" aria-live="polite">Showing all {len(patches)} patches · Filter patches or browse the section navigation.</p>{content}<footer class="page-footer"><p>Generated from the Markdown plan and reviewed health report. No live validation is inferred.</p>{footer}</footer></main><script>{script}</script></body></html>'''


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace-root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    docs = args.workspace_root / DOCS
    try:
        page = render_html((docs / (PLAN_NAME + ".md")).read_text(encoding="utf-8"), (docs / "Stage-1-8 Health Report.mdx").read_text(encoding="utf-8"))
        (docs / (PLAN_NAME + ".html")).write_text(page, encoding="utf-8")
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Unable to render plan: {exc}\n")
    print(docs / (PLAN_NAME + ".html"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
