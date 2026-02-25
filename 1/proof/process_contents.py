#!/usr/bin/env python3
"""
Contents Parser
Parses contents.md and outputs a single combined HTML file optimized for PDF rendering.
"""

import os
import re
import html
import sys
import json
from pathlib import Path
from datetime import datetime

INPUT_FILE = Path("../contents/contents.md")
OUTPUT_FILE = Path("html/contents_proof.html")
LITERAL_DIR = Path("../text/dynamic/literal")

LINE_MAP = {}

def build_line_map():
    """Build a mapping from file IDs to starting line numbers by scanning literal files."""
    global LINE_MAP
    current_line = 1
    
    files = sorted([f for f in os.listdir(LITERAL_DIR) if f.endswith('.txt')])
    
    for filename in files:
        file_id = filename.replace('.txt', '')
        LINE_MAP[file_id] = current_line
        
        filepath = LITERAL_DIR / filename
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                if re.match(r'^\[\d+\]', line.strip()):
                    current_line += 1

def file_id_to_literal_key(volume, chapter, file_id):
    """Convert a contents file_id like '1-1' or '2-1-2' to literal file key like '01-01-01-01'."""
    parts = file_id.split('-')
    vol = volume.zfill(2)
    ch = chapter.zfill(2)
    
    if len(parts) == 2:
        sec = parts[1].zfill(2)
        return f"{vol}-{ch}-{sec}-01"
    elif len(parts) == 3:
        sec = parts[1].zfill(2)
        sub = parts[2].zfill(2)
        return f"{vol}-{ch}-{sec}-{sub}"
    
    return None

# -----------------------------------------------------------------------------
# CSS STYLES (PDF-OPTIMIZED)
# -----------------------------------------------------------------------------

HTML_CSS = """
<style>
    @page {
        size: 6in 9in;
        margin: 0.75in;
        @bottom-center {
            content: counter(page);
        }
    }

    :root {
        --font-main: 'Georgia', 'Times New Roman', serif;
        --font-sans: 'Helvetica', 'Arial', sans-serif;
        --font-mono: 'Consolas', 'Courier New', monospace;
        
        --color-bg: #1e1e1e;
        --color-text: #e0e0e0;
        --color-muted: #a0a0a0;
        --color-accent: #bcaaa4;
        --color-header: #d7ccc8;
        --color-chapter: #81d4fa;
        --color-prologue: #ce93d8;
        --color-main: #a5d6a7;
        --color-subsection: #ffcc80;
        --color-list: #80deea;
        --color-fragment: #b0bec5;
        --color-border: #3a3a3a;
        --color-table-header: #2d2d2d;
        --color-table-row: #252525;
        --color-table-hover: #3a3a3a;
        
        --line-height: 1.5;
    }

    body.light-mode {
        --color-bg: #fafafa;
        --color-text: #1a1a1a;
        --color-muted: #666;
        --color-accent: #6a1b9a;
        --color-header: #4a148c;
        --color-chapter: #0277bd;
        --color-prologue: #7b1fa2;
        --color-main: #2e7d32;
        --color-subsection: #e65100;
        --color-list: #00838f;
        --color-fragment: #455a64;
        --color-border: #ddd;
        --color-table-header: #eee;
        --color-table-row: #f5f5f5;
        --color-table-hover: #e0e0e0;
    }

    * {
        box-sizing: border-box;
    }

    body {
        font-family: var(--font-main);
        color: var(--color-text);
        line-height: var(--line-height);
        font-size: 10pt;
        margin: 0;
        padding: 0;
        background-color: var(--color-bg);
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
    }

    .document {
        max-width: 5.5in;
        margin: 0 auto;
        padding: 0;
    }

    /* Title */
    .title-section {
        text-align: center;
        margin-bottom: 3em;
        padding-bottom: 2em;
        border-bottom: 2px solid var(--color-border);
    }

    .title-section h1 {
        font-size: 1.4em;
        color: var(--color-header);
        margin-bottom: 0.5em;
        font-variant: small-caps;
        letter-spacing: 1px;
    }

    .title-section .work-title {
        font-size: 1.1em;
        color: var(--color-accent);
        margin-bottom: 0.25em;
    }

    .title-section .meta {
        font-size: 0.85em;
        color: var(--color-muted);
        margin-top: 1em;
    }

    /* Overview section */
    .overview {
        margin-bottom: 2em;
        padding: 1em;
        background-color: rgba(60, 60, 60, 0.5);
        border-left: 3px solid var(--color-accent);
        page-break-after: always;
    }

    .overview h2 {
        font-size: 1.1em;
        color: var(--color-header);
        margin-top: 0;
        margin-bottom: 0.75em;
    }

    .overview ul {
        margin: 0;
        padding-left: 1.5em;
    }

    .overview li {
        margin-bottom: 0.5em;
        font-size: 0.9em;
    }

    /* Chapter */
    .chapter {
        margin-top: 2em;
        margin-bottom: 1.5em;
    }

    .chapter-header {
        border-bottom: 1px solid var(--color-border);
        padding-bottom: 0.5em;
        margin-bottom: 1em;
    }

    .chapter-title {
        font-size: 1.2em;
        color: var(--color-chapter);
        font-weight: 700;
        margin: 0;
    }

    .chapter-meta {
        font-size: 0.8em;
        color: var(--color-muted);
        margin-top: 0.25em;
        font-family: var(--font-sans);
    }

    /* Section table */
    .section-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 0.85em;
    }

    .section-table th {
        text-align: left;
        font-family: var(--font-sans);
        font-size: 0.7em;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        color: var(--color-muted);
        border-bottom: 1px solid var(--color-border);
        padding: 0.25em 0.5em;
    }

    .section-table td {
        padding: 0.35em 0.5em;
        vertical-align: top;
        border-bottom: 1px solid var(--color-border);
    }

    .section-table .col-file {
        font-family: var(--font-mono);
        font-size: 0.8em;
        color: var(--color-muted);
        width: 22%;
    }

    .section-table .col-lines {
        font-family: var(--font-mono);
        font-size: 0.8em;
        color: var(--color-muted);
        width: 8%;
        text-align: right;
    }

    .section-table .col-type {
        font-family: var(--font-sans);
        font-size: 0.75em;
        width: 12%;
    }

    .section-table .col-title {
        width: 58%;
    }

    /* Type badges */
    .type-badge {
        display: inline-block;
        padding: 1px 6px;
        border-radius: 3px;
        font-size: 0.7em;
        font-weight: 600;
        text-transform: uppercase;
    }

    .type-prologue {
        background-color: rgba(206, 147, 216, 0.25);
        color: var(--color-prologue);
    }

    .type-main {
        background-color: rgba(165, 214, 167, 0.25);
        color: var(--color-main);
    }

    .type-subsection {
        background-color: rgba(255, 204, 128, 0.25);
        color: var(--color-subsection);
    }

    .type-list {
        background-color: rgba(128, 222, 234, 0.25);
        color: var(--color-list);
    }

    .type-fragment {
        background-color: rgba(176, 190, 197, 0.25);
        color: var(--color-fragment);
    }

    /* Separator */
    .chapter-separator {
        margin: 2em 0;
        border: none;
        border-top: 1px dashed var(--color-border);
    }

    /* Clickable rows */
    .section-table tbody tr {
        cursor: pointer;
        transition: background-color 0.2s ease;
    }
    
    .section-table tbody tr:hover {
        background-color: var(--color-table-hover);
    }
    
    .section-table tbody tr:active {
        background-color: rgba(129, 212, 250, 0.2);
    }

    /* Print-specific adjustments */
    @media print {
        body {
            font-size: 9pt;
        }
        .document {
            max-width: none;
        }
        a {
            text-decoration: none;
            color: inherit;
        }
        .overview {
            background-color: #f5f5f5;
        }
    }
</style>
"""

# -----------------------------------------------------------------------------
# PARSER LOGIC
# -----------------------------------------------------------------------------

def parse_contents(content):
    """Parse the contents.md file."""
    data = {
        'title': '',
        'work_title': '',
        'meta': {},
        'chapters': []
    }
    
    lines = content.split('\n')
    
    # Extract title (first # heading)
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if title_match:
        data['title'] = title_match.group(1).strip()
    
    # Extract work title (Tibetan line)
    tibetan_match = re.search(r'\*\*Work\*\*:\s*(.+?)\s*\*\*', content)
    if tibetan_match:
        data['work_title'] = tibetan_match.group(1).strip()
    
    # Extract metadata
    for key in ['English Title', 'Author', 'Total Chapters', 'Total Sections', 'Version', 'Generated']:
        match = re.search(rf'\*\*{key}\*\*:\s*(.+?)\s*\*\*', content)
        if match:
            data['meta'][key] = match.group(1).strip()
    
    # Find all chapters
    # Pattern: ## Chapter N: Title
    chapter_pattern = re.compile(r'^##\s+Chapter\s+(\d+):\s+(.+)$', re.MULTILINE)
    
    # Find chapter sections with their tables
    # Pattern: **Volume**: XX | **Pages**: XX-XX | **Sections**: XX | **Total Lines**: ~X
    
    chapter_matches = list(chapter_pattern.finditer(content))
    
    for i, match in enumerate(chapter_matches):
        chapter_num = match.group(1)
        chapter_title = match.group(2).strip()
        
        # Find chapter header info (Volume, Pages, Sections, Lines)
        start_pos = match.end()
        end_pos = chapter_matches[i+1].start() if i + 1 < len(chapter_matches) else len(content)
        
        chapter_content = content[start_pos:end_pos]
        
        # Extract chapter meta
        vol_match = re.search(r'\*\*Volume\*\*:\s*(\d+)', chapter_content)
        pages_match = re.search(r'\*\*Pages\*\*:\s*([\d-]+)', chapter_content)
        sections_match = re.search(r'\*\*Sections\*\*:\s*(\d+)', chapter_content)
        lines_match = re.search(r'\*\*Total Lines\*\*:\s*~?([\d,]+)', chapter_content)
        
        chapter_data = {
            'number': chapter_num,
            'title': chapter_title,
            'volume': vol_match.group(1) if vol_match else '',
            'pages': pages_match.group(1) if pages_match else '',
            'sections': sections_match.group(1) if sections_match else '',
            'total_lines': lines_match.group(1) if lines_match else '',
            'entries': []
        }
        
        # Extract table rows
        # Format: | file | lines | Type | Title |
        table_rows = re.findall(
            r'\|\s*([\d-]+)\s*\|\s*~?(\d+)\s*\|\s*([\w\s/-]+)\s*\|\s*(.+?)\s*\|',
            chapter_content
        )
        
        for row in table_rows:
            file_name = row[0].strip()
            lines = row[1].strip()
            content_type = row[2].strip()
            title = row[3].strip()
            
            chapter_data['entries'].append({
                'file': file_name,
                'lines': lines,
                'type': content_type,
                'title': title
            })
        
        data['chapters'].append(chapter_data)
    
    return data

def get_type_class(content_type):
    """Return CSS class based on content type."""
    type_lower = content_type.lower().strip()
    
    if 'prologue' in type_lower:
        return 'prologue'
    elif 'main teaching' in type_lower:
        return 'main'
    elif 'subsection' in type_lower:
        return 'subsection'
    elif 'list' in type_lower:
        return 'list'
    elif 'fragment' in type_lower:
        return 'fragment'
    else:
        return 'list'

def generate_html(data):
    """Generate HTML content."""
    html_parts = []
    
    html_parts.append('''
    <script>
    document.addEventListener('click', function(e) {
        const row = e.target.closest('tr[data-line]');
        if (row) {
            const lineNum = row.dataset.line;
            window.parent.postMessage({ type: 'navigateToLine', line: lineNum }, '*');
        }
    });
    
    // Dark mode handling - sync with parent
    (function() {
        const isDark = localStorage.getItem('darkMode') !== 'false';
        if (!isDark) document.body.classList.add('light-mode');
        
        window.addEventListener('message', function(e) {
            if (e.data && e.data.type === 'darkModeChange') {
                document.body.classList.toggle('light-mode', !e.data.enabled);
                localStorage.setItem('darkMode', e.data.enabled);
            }
        });
    })();
    </script>
    ''')
    
    html_parts.append(f'''
    <div class="title-section">
        <h1>{html.escape(data['title'])}</h1>
        <div class="work-title">{html.escape(data['work_title'])}</div>
        <div class="meta">
    ''')
    
    for key, value in data['meta'].items():
        html_parts.append(f'<div>{key}: {html.escape(value)}</div>')
    
    html_parts.append('''
        </div>
    </div>
    ''')
    
    # Overview
    html_parts.append('''
    <div class="overview">
        <h2>Overview</h2>
        <ul>
            <li><strong>Descriptive titles</strong> for all 213 sections based on content analysis</li>
            <li><strong>Line counts</strong> for each section (calculated from line markers)</li>
            <li><strong>Click any row</strong> to jump to that section in your currently selected translation layer</li>
            <li><strong>Content type</strong> classification:
                <ul>
                    <li><span class="type-badge type-prologue">Prologue</span> - Introductory/Homage sections</li>
                    <li><span class="type-badge type-main">Main Teaching</span> - Substantive doctrinal content</li>
                    <li><span class="type-badge type-subsection">Subsection</span> - Divisions within main teachings</li>
                    <li><span class="type-badge type-list">List Item</span> - Brief structural markers (often one-line)</li>
                    <li><span class="type-badge type-fragment">Structural Fragment</span> - Incomplete list items or outlines</li>
                </ul>
            </li>
        </ul>
    </div>
    ''')
    
    # Chapters
    for chapter in data['chapters']:
        html_parts.append(f'''
        <div class="chapter">
            <div class="chapter-header">
                <h2 class="chapter-title">Chapter {chapter['number']}: {html.escape(chapter['title'])}</h2>
                <div class="chapter-meta">
                    Volume: {chapter['volume']} | 
                    Pages: {chapter['pages']} | 
                    Sections: {chapter['sections']} | 
                    Total Lines: ~{chapter['total_lines']}
                </div>
            </div>
            <table class="section-table">
                <thead>
                    <tr>
                        <th class="col-file">File</th>
                        <th class="col-lines">Lines</th>
                        <th class="col-type">Type</th>
                        <th class="col-title">Title</th>
                    </tr>
                </thead>
                <tbody>
        ''')
        
        for entry in chapter['entries']:
            type_class = get_type_class(entry['type'])
            literal_key = file_id_to_literal_key(chapter['volume'], chapter['number'], entry['file'].replace('.md', ''))
            start_line = LINE_MAP.get(literal_key, 1)
            html_parts.append(f'''
                    <tr data-line="{start_line}" style="cursor: pointer;" title="Click to go to line {start_line}">
                        <td class="col-file">{html.escape(entry['file'])}</td>
                        <td class="col-lines">{html.escape(entry['lines'])}</td>
                        <td class="col-type"><span class="type-badge type-{type_class}">{html.escape(entry['type'])}</span></td>
                        <td class="col-title">{html.escape(entry['title'])}</td>
                    </tr>
            ''')
        
        html_parts.append('''
                </tbody>
            </table>
        </div>
        ''')
    
    return '\n'.join(html_parts)

def build_full_document(data):
    """Build complete HTML document."""
    content = generate_html(data)
    
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html.escape(data['title'])}</title>
    <meta name="generator" content="Contents Parser">
    <meta name="created" content="{datetime.now().isoformat()}">
    {HTML_CSS}
</head>
<body>
    <div class="document">
        {content}
    </div>
</body>
</html>
"""

# -----------------------------------------------------------------------------
# MAIN
# -----------------------------------------------------------------------------

def process_contents():
    if not INPUT_FILE.exists():
        print(f"Error: Input file '{INPUT_FILE}' not found.")
        sys.exit(1)
    
    print("Building line map from literal files...")
    build_line_map()
    print(f"  Mapped {len(LINE_MAP)} files to line numbers")
    
    try:
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print("Parsing contents...")
        data = parse_contents(content)
        
        print(f"  Found {len(data['chapters'])} chapters")
        
        total_sections = sum(len(ch['entries']) for ch in data['chapters'])
        print(f"  Found {total_sections} sections")
        
        full_html = build_full_document(data)
        
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write(full_html)
        
        print(f"\n✓ Complete! Output saved to '{OUTPUT_FILE}'")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    process_contents()
