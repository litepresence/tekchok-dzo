#!/usr/bin/env python3
"""
Liturgical Batch Parser
Parses all matching files in 'liturgical/' folder and outputs a single 
combined HTML file optimized for PDF rendering.

Updates:
- Consecutive tags of the same type are now joined into single blocks.
- Prose sections join with spaces; all other sections join with <br> to maintain line breaks.
- Line spacing and margins reduced for tighter PDF layout.
"""

import os
import re
import html
import sys
from pathlib import Path
from datetime import datetime

# -----------------------------------------------------------------------------
# CONFIGURATION
# -----------------------------------------------------------------------------

INPUT_DIR = Path("../text/layer/liturgical")
OUTPUT_FILE = Path("html/liturgical.html")
FILE_PATTERN = re.compile(r"^\d\d-\d\d-\d\d-\d\d\.txt$")

# Regex to parse lines: [LineNum] [<break>] <Tag> Content
LINE_PATTERN = re.compile(r'^\[(\d+)\]\s*(?:(<break>)\s*)?<(\w+)>\s*(.*)$')

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
            color: #888;
        }
    }

    :root {
        --font-main: 'Georgia', 'Times New Roman', serif;
        --font-sans: 'Helvetica', 'Arial', sans-serif;
        
        --color-bg: #1e1e1e;
        --color-text: #e0e0e0;
        --color-muted: #a0a0a0;
        --color-accent: #c9a55c;
        --color-mantra: #e07050;
        --color-border: #3a3a3a;
        --color-btn: #2d5a7b;
        --color-btn-hover: #3d7a9b;
        
        --line-height: 1.3;
    }

    body.light-mode {
        --color-bg: #fafafa;
        --color-text: #1a1a1a;
        --color-muted: #666;
        --color-accent: #6a1b9a;
        --color-mantra: #c62828;
        --color-border: #ddd;
        --color-btn: #1565c0;
        --color-btn-hover: #1976d2;
    }

    * {
        box-sizing: border-box;
    }

    body {
        font-family: var(--font-main);
        color: var(--color-text);
        line-height: var(--line-height);
        font-size: 11pt;
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

    .chapter {
        display: none;
    }
    .chapter.active {
        display: block;
    }

    .file-separator {
        margin-top: 2em;
        margin-bottom: 1em;
        padding-top: 1em;
        border-top: 1px solid var(--color-border);
        text-align: center;
        font-variant: small-caps;
        color: var(--color-accent);
        font-size: 0.9em;
        letter-spacing: 2px;
    }

    .prose {
        display: block;
        margin-top: 0;
        margin-bottom: 0.5em;
        text-align: justify;
        hyphens: auto;
        -webkit-hyphens: auto;
        color: var(--color-text);
    }
    
    .prose.break-before {
        margin-top: 1em;
        text-indent: 1.5em;
    }

    .verse {
        display: block;
        text-align: center;
        font-style: italic;
        margin: 0.4em 0;
        color: var(--color-muted);
        page-break-inside: avoid;
    }

    .tantra {
        display: block;
        margin: 0.2em 0;
        padding-left: 1.5em;
        border-left: 2px solid var(--color-accent);
        color: var(--color-accent);
        font-style: italic;
        page-break-inside: avoid;
    }

    .ornament {
        display: block;
        text-align: center;
        font-variant: small-caps;
        font-weight: bold;
        color: var(--color-accent);
        margin: 1.5em 0 0.8em 0;
        letter-spacing: 1.5px;
        font-size: 1.05em;
        page-break-after: avoid;
    }

    .mantra {
        display: inline-block;
        font-weight: bold;
        color: var(--color-mantra);
        font-family: var(--font-sans);
        letter-spacing: 0.5px;
    }

    .list {
        display: list-item;
        list-style-type: disc;
        margin-left: 1.5em;
        margin-top: 0.1em;
        margin-bottom: 0.1em;
        color: var(--color-text);
    }

    .verse-marker {
        font-size: 0.75em;
        vertical-align: super;
        color: var(--color-muted);
        margin-left: 4px;
        font-family: var(--font-sans);
    }

    .nav-controls {
        position: fixed;
        bottom: 20px;
        right: 20px;
        display: flex;
        gap: 10px;
        z-index: 1000;
    }

    .nav-btn {
        background-color: var(--color-btn);
        color: var(--color-text);
        border: none;
        padding: 12px 20px;
        font-size: 14px;
        cursor: pointer;
        border-radius: 5px;
        font-family: var(--font-sans);
        transition: background-color 0.2s;
    }
    .nav-btn:hover {
        background-color: var(--color-btn-hover);
    }
    .nav-btn:disabled {
        background-color: #444;
        color: #666;
        cursor: not-allowed;
    }

    .chapter-indicator {
        position: fixed;
        bottom: 20px;
        left: 20px;
        background-color: rgba(30, 30, 30, 0.9);
        color: var(--color-accent);
        padding: 10px 15px;
        border-radius: 5px;
        font-family: var(--font-sans);
        font-size: 12px;
        z-index: 1000;
    }

    [id^="line-"]:target {
        background-color: rgba(201, 165, 92, 0.3);
        border-radius: 3px;
    }

    .highlighted-line {
        background-color: rgba(201, 165, 92, 0.4) !important;
        border-radius: 3px;
        animation: highlightFade 3s ease-out forwards;
    }

    @keyframes highlightFade {
        0% { background-color: rgba(201, 165, 92, 0.4); }
        80% { background-color: rgba(201, 165, 92, 0.3); }
        100% { background-color: transparent; }
    }

    .toc {
        margin-bottom: 2em;
        page-break-after: always;
    }
    .toc h1 {
        text-align: center;
        font-variant: small-caps;
        margin-bottom: 1em;
        color: var(--color-accent);
    }
    .toc ul {
        list-style: none;
        padding-left: 0;
    }
    .toc li {
        margin-bottom: 0.3em;
        color: var(--color-text);
    }
    .toc a {
        text-decoration: none;
        color: inherit;
    }
    .toc a:hover {
        color: var(--color-accent);
    }

    @media print {
        body {
            font-size: 10.5pt;
            -webkit-print-color-adjust: exact;
            print-color-adjust: exact;
        }
        .document {
            max-width: none;
        }
        a {
            text-decoration: none;
            color: inherit;
        }
        .file-separator {
            border-top: 1px solid var(--color-border);
        }
        .nav-controls,
        .chapter-indicator {
            display: none;
        }
        .chapter {
            display: block !important;
            page-break-after: always;
        }
    }
</style>
"""

# -----------------------------------------------------------------------------
# PARSER LOGIC
# -----------------------------------------------------------------------------

def parse_line(raw_line):
    """Parses a single line of the input spec."""
    raw_line = raw_line.strip()
    if not raw_line:
        return None

    match = LINE_PATTERN.match(raw_line)
    if not match:
        return None

    line_num = match.group(1)
    break_tag = match.group(2)
    tag_type = match.group(3).lower()
    content = match.group(4).strip()

    return {
        "line_num": line_num,
        "is_break": break_tag is not None,
        "tag": tag_type,
        "content": html.escape(content)
    }

def get_chapter_key(filename):
    parts = filename.replace('.txt', '').split('-')
    if len(parts) >= 2:
        return f"{parts[0]}-{parts[1]}"
    return filename.replace('.txt', '')

def generate_file_html(parsed_lines, filename):
    """Generates HTML content for a single file.
    
    Updates: Groups consecutive lines with the same tag and no break 
    into single HTML elements. Prose joins with spaces; others join with <br>.
    """
    html_parts = []
    
    file_title = filename.replace('.txt', '').replace('-', ' ')
    file_id = filename.replace('.txt', '')
    html_parts.append(f'<div class="file-separator" id="file-{file_id}">{file_title}</div>')

    groups = []
    current_group = None

    for item in parsed_lines:
        if not item:
            continue

        can_merge = False
        if current_group:
            if (item['tag'] == current_group['tag'] and 
                not current_group['is_break'] and 
                not item['is_break']):
                can_merge = True

        if can_merge:
            if item['tag'] == 'prose':
                current_group['content'] += " " + item['content']
            else:
                current_group['content'] += "<br>" + item['content']
        else:
            if current_group:
                groups.append(current_group)
            current_group = item.copy()

    if current_group:
        groups.append(current_group)

    for item in groups:
        tag = item['tag']
        content = item['content']
        is_break = item['is_break']

        classes = [tag]
        if is_break:
            classes.append('break-before')
        
        class_str = " ".join(classes)

        if tag == 'mantra':
            content_html = f'<span class="mantra">{content}</span>'
        else:
            content_html = content

        content_html = re.sub(r'\|\|\s*(\d+)\s*\|\|', r'<span class="verse-marker">|| \1 ||</span>', content_html)

        html_parts.append(f'<div class="{class_str}" id="line-{item["line_num"]}" data-line="{item["line_num"]}">{content_html}</div>')

    return "\n".join(html_parts)

def build_chapter_html(file_html_list, chapter_key, chapter_index):
    """Wraps all files in a chapter into a chapter div."""
    active_class = ' active' if chapter_index == 0 else ''
    parts = [f'<div class="chapter{active_class}" data-chapter="{chapter_index}" data-chapter-key="{chapter_key}">']
    parts.extend(file_html_list)
    parts.append('</div>')
    return "\n".join(parts)

def build_full_document(all_chapter_content, chapter_keys, total_chapters):
    """Wraps everything in HTML5 boilerplate with navigation."""
    
    js_script = f"""
<script>
let currentChapter = 0;
const totalChapters = {total_chapters};
const chapterKeys = {chapter_keys};

function showChapter(index) {{
    const chapters = document.querySelectorAll('.chapter');
    chapters.forEach((ch, i) => {{
        ch.classList.toggle('active', i === index);
    }});
    currentChapter = index;
    updateNavButtons();
    updateIndicator();
    window.scrollTo({{ top: 0, behavior: 'instant' }});
}}

function nextChapter() {{
    if (currentChapter < totalChapters - 1) {{
        showChapter(currentChapter + 1);
    }}
}}

function prevChapter() {{
    if (currentChapter > 0) {{
        showChapter(currentChapter - 1);
    }}
}}

function updateNavButtons() {{
    document.getElementById('prevBtn').disabled = currentChapter === 0;
    document.getElementById('nextBtn').disabled = currentChapter === totalChapters - 1;
}}

function updateIndicator() {{
    const key = chapterKeys[currentChapter];
    const parts = key.split('-');
    const volume = parts[0];
    const chapter = parts[1];
    document.getElementById('chapterIndicator').textContent = 
        `Volume ${{volume}}, Chapter ${{chapter}}`;
}}

function goToLine(lineNum, volume) {{
    volume = volume || 1;
    const volPrefix = volume === 1 ? '01-' : '02-';
    
    let lineEl = document.getElementById('line-' + lineNum);
    
    if (!lineEl) {{
        const volChapters = document.querySelectorAll(`.chapter[data-chapter-key^="${{volPrefix}}"]`);
        let bestMatch = null;
        let bestDiff = Infinity;
        
        volChapters.forEach(ch => {{
            const lines = ch.querySelectorAll('[id^="line-"]');
            for (const el of lines) {{
                const elLine = parseInt(el.id.replace('line-', ''));
                const diff = Math.abs(elLine - lineNum);
                if (diff < bestDiff) {{
                    bestDiff = diff;
                    bestMatch = el;
                }}
            }}
        }});
        lineEl = bestMatch;
    }}
    
    if (lineEl) {{
        const chapter = lineEl.closest('.chapter');
        if (chapter) {{
            const chapterIndex = parseInt(chapter.dataset.chapter);
            showChapter(chapterIndex);
            setTimeout(() => {{
                document.querySelectorAll('.highlighted-line').forEach(el => {{
                    el.classList.remove('highlighted-line');
                    el.style.animation = '';
                }});
                lineEl.classList.add('highlighted-line');
                void lineEl.offsetWidth;
                lineEl.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
            }}, 100);
            return true;
        }}
    }}
    return false;
}}

function handleHashNavigation() {{
    const hash = window.location.hash;
    const match = hash.match(/line-(\d+)(?:-(\d+))?/);
    if (match) {{
        let lineNum, volume;
        if (match[2]) {{
            volume = parseInt(match[1]);
            lineNum = parseInt(match[2]);
        }} else {{
            lineNum = parseInt(match[1]);
            volume = 1;
        }}
        goToLine(lineNum, volume);
    }}
}}

// Report visible line to parent on scroll
let lastReportedLine = null;
function reportCurrentLine() {{
    const lines = document.querySelectorAll('[id^="line-"]');
    if (!lines.length) return;
    
    const viewportMiddle = window.innerHeight / 2;
    
    // Find the line closest to the middle of the viewport
    let closest = null;
    let closestDist = Infinity;
    
    for (const line of lines) {{
        const rect = line.getBoundingClientRect();
        const lineMiddle = (rect.top + rect.bottom) / 2;
        const dist = Math.abs(lineMiddle - viewportMiddle);
        if (dist < closestDist) {{
            closestDist = dist;
            closest = line;
        }}
    }}
    
    if (closest) {{
        const lineNum = closest.id.replace('line-', '');
        if (lineNum !== lastReportedLine) {{
            lastReportedLine = lineNum;
            const chapter = closest.closest('[data-chapter-key]');
            const chapterKey = chapter ? chapter.dataset.chapterKey : '01-01';
            const volume = chapterKey.startsWith('02-') ? 2 : 1;
            window.parent.postMessage({{ type: 'linePosition', line: lineNum, volume: volume }}, '*');
        }}
    }}
}}

document.addEventListener('DOMContentLoaded', () => {{
    updateNavButtons();
    updateIndicator();
    handleHashNavigation();
    
    // Report line position on scroll
    window.addEventListener('scroll', reportCurrentLine);
    // Initial report
    setTimeout(reportCurrentLine, 500);
}});

window.addEventListener('hashchange', handleHashNavigation);

// Dark mode handling - sync with parent
(function() {{
    const isDark = localStorage.getItem('darkMode') !== 'false';
    console.log('Liturgical page loaded, isDark:', isDark);
    if (!isDark) document.body.classList.add('light-mode');
    
    window.addEventListener('message', function(e) {{
        console.log('Received message:', e.data);
        if (e.data && e.data.type === 'darkModeChange') {{
            console.log('darkModeChange received, enabled:', e.data.enabled);
            document.body.classList.toggle('light-mode', !e.data.enabled);
            localStorage.setItem('darkMode', e.data.enabled);
        }}
    }});
}})();
</script>
"""

    nav_html = """
<div class="nav-controls">
    <button class="nav-btn" id="prevBtn" onclick="prevChapter()">Previous</button>
    <button class="nav-btn" id="nextBtn" onclick="nextChapter()">Next Chapter</button>
</div>
<div class="chapter-indicator" id="chapterIndicator">Volume 1, Chapter 1</div>
"""

    combined_content = "\n".join(all_chapter_content)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Liturgical Text Collection</title>
    <meta name="generator" content="Liturgical Parser">
    <meta name="created" content="{datetime.now().isoformat()}">
    {HTML_CSS}
    {js_script}
</head>
<body>
    <div class="document">
        {combined_content}
    </div>
    {nav_html}
</body>
</html>
"""

# -----------------------------------------------------------------------------
# BATCH PROCESSING
# -----------------------------------------------------------------------------

def process_folder():
    # Check Input Directory
    if not INPUT_DIR.exists():
        print(f"Error: Input directory '{INPUT_DIR}' not found.")
        print("Please create a folder named 'liturgical' and place your .txt files there.")
        sys.exit(1)

    # Find Matching Files
    all_files = os.listdir(INPUT_DIR)
    matching_files = sorted([f for f in all_files if FILE_PATTERN.match(f)])

    if not matching_files:
        print(f"No files matching pattern '{FILE_PATTERN.pattern}' found in '{INPUT_DIR}'.")
        sys.exit(0)

    print(f"Found {len(matching_files)} file(s) to process.")

    chapters = {}

    for filename in matching_files:
        input_path = INPUT_DIR / filename

        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            parsed_data = [parse_line(line) for line in lines]
            parsed_data = [p for p in parsed_data if p is not None]

            file_html = generate_file_html(parsed_data, filename)
            
            chapter_key = get_chapter_key(filename)
            if chapter_key not in chapters:
                chapters[chapter_key] = []
            chapters[chapter_key].append(file_html)

            print(f"  ✓ Processed: {filename}")

        except Exception as e:
            print(f"  ✗ Error processing {filename}: {e}")

    sorted_chapter_keys = sorted(chapters.keys())
    all_chapter_content = []
    for idx, chapter_key in enumerate(sorted_chapter_keys):
        chapter_html = build_chapter_html(chapters[chapter_key], chapter_key, idx)
        all_chapter_content.append(chapter_html)

    full_html = build_full_document(all_chapter_content, sorted_chapter_keys, len(sorted_chapter_keys))

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(full_html)

    print(f"\n✓ Complete! Output saved to '{OUTPUT_FILE}'")
    print(f"  Total files combined: {len(matching_files)}")
    print(f"  Total chapters: {len(sorted_chapter_keys)}")
    print(f"\nTo create PDF:")
    print(f"  1. Open '{OUTPUT_FILE}' in Chrome or Edge")
    print(f"  2. Press Ctrl+P (Print)")
    print(f"  3. Select 'Save as PDF'")
    print(f"  4. Ensure 'Background graphics' is checked")
    print(f"  5. Click Save")

if __name__ == "__main__":
    process_folder()
