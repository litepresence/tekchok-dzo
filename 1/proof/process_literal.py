#!/usr/bin/env python3
"""
Literal Translation Parser
Parses all matching files in 'literal/' folder and outputs a single 
combined HTML file optimized for PDF rendering.
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

INPUT_DIR = Path("../text/frozen/literal")
OUTPUT_FILE = Path("html/literal_proof.html")
FILE_PATTERN = re.compile(r"^\d\d-\d\d-\d\d-\d\d\.txt$")

# Regex to parse lines: [LineNum] Content
LINE_PATTERN = re.compile(r'^\[(\d+)\]\s*(.*)$')

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
        --font-mono: 'Courier New', 'Consolas', monospace;
        --font-sans: 'Helvetica', 'Arial', sans-serif;
        
        --color-bg: #1e1e1e;
        --color-text: #e0e0e0;
        --color-muted: #a0a0a0;
        --color-accent: #64b5f6;
        --color-line-num: #757575;
        --color-border: #3a3a3a;
        --color-btn: #2d5a7b;
        --color-btn-hover: #3d7a9b;
        
        --line-height: 1.5;
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
        font-size: 0.95em;
        letter-spacing: 2px;
    }
    .file-separator:first-child {
        margin-top: 0;
    }

    .line-grid {
        display: grid;
        grid-template-columns: 45px 1fr;
        column-gap: 12px;
        margin: 0;
        padding: 0;
    }

    .line-num {
        grid-column: 1;
        text-align: right;
        font-family: var(--font-sans);
        font-size: 0.7em;
        color: var(--color-line-num);
        padding-top: 2px;
        user-select: none;
        border-right: 1px solid var(--color-border);
        padding-right: 8px;
    }

    .line-content {
        grid-column: 2;
        margin: 0;
        padding: 1px 0;
    }

    .literal-line {
        display: block;
        margin: 0;
        padding: 0;
        font-size: 0.95em;
        white-space: normal;
        word-wrap: break-word;
    }

    .compound {
        color: var(--color-muted);
        white-space: nowrap;
    }

    .grammar_marker {
        font-variant: small-caps;
        font-size: 0.85em;
        color: var(--color-accent);
        white-space: nowrap;
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

    .line-content:target,
    .literal-line:target {
        background-color: rgba(100, 181, 246, 0.3);
        border-radius: 3px;
    }

    .highlighted-line {
        background-color: rgba(100, 181, 246, 0.3) !important;
        border-radius: 3px;
        animation: highlightFade 3s ease-out forwards;
    }

    @keyframes highlightFade {{
        0% {{ background-color: rgba(100, 181, 246, 0.4); }}
        70% {{ background-color: rgba(100, 181, 246, 0.3); }}
        100% {{ background-color: transparent; }}
    }}

    .toc {
        margin-bottom: 3em;
        page-break-after: always;
    }
    .toc h1 {
        text-align: center;
        font-variant: small-caps;
        margin-bottom: 1.5em;
        color: var(--color-accent);
    }
    .toc ul {
        list-style: none;
        padding-left: 0;
    }
    .toc li {
        margin-bottom: 0.5em;
        color: var(--color-text);
    }
    .toc a {
        text-decoration: none;
        color: inherit;
    }
    .toc a:hover {
        color: var(--color-accent);
        text-decoration: underline;
    }

    @media print {
        body {
            font-size: 9.5pt;
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
        .line-num {
            border-right: 1px solid var(--color-border);
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
    """Parses a single line of the literal translation spec."""
    raw_line = raw_line.strip()
    if not raw_line:
        return None

    match = LINE_PATTERN.match(raw_line)
    if not match:
        return None

    line_num = match.group(1)
    content = match.group(2).strip()

    # Process content for styling
    processed_content = process_content(content)

    return {
        "line_num": line_num,
        "content": processed_content
    }

def process_content(content):
    """
    Processes literal translation content for HTML styling.
    - Escapes HTML
    - Strips all forward slashes
    - Wraps hyphenated compounds
    - Highlights grammatical markers
    """
    # Escape HTML first
    content = html.escape(content)
    
    # Strip all forward slashes (line end markers not needed)
    content = content.replace('/', '')
    
    # Strip any resulting extra whitespace
    content = ' '.join(content.split())
    
    # Highlight grammatical markers (common patterns in literal translations)
    # Must be done BEFORE compound wrapping to avoid conflicts
    grammar_markers = [
        'genitive', 'locative', 'instrumental', 'dative', 'ablative',
        'nominative', 'accusative', 'vocative', 'ergative'
    ]
    
    for marker in grammar_markers:
        # Match hyphenated grammar markers and keep them attached to previous word
        pattern = rf'(-{marker})(\s|$)'
        replacement = r'<span class="grammar_marker">\1</span>\2'
        content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
    
    # Wrap hyphenated compounds for potential styling (keep together with nowrap)
    content = re.sub(r'([a-zA-Z]+)-([a-zA-Z]+)', r'<span class="compound">\1-\2</span>', content)
    
    return content

def get_chapter_key(filename):
    parts = filename.replace('.txt', '').split('-')
    if len(parts) >= 2:
        return f"{parts[0]}-{parts[1]}"
    return filename.replace('.txt', '')

def generate_file_html(parsed_lines, filename):
    """Generates HTML content for a single file."""
    html_parts = []
    
    file_title = filename.replace('.txt', '').replace('-', ' ')
    file_id = filename.replace('.txt', '')
    html_parts.append(f'<div class="file-separator" id="file-{file_id}">{file_title}</div>')
    html_parts.append('<div class="line-grid">')

    for item in parsed_lines:
        if not item:
            continue

        line_num = item['line_num']
        content = item['content']

        html_parts.append(f'  <div class="line-num">{line_num}</div>')
        html_parts.append(f'  <div class="line-content" id="line-{line_num}"><span class="literal-line" data-line="{line_num}">{content}</span></div>')

    html_parts.append('</div>')

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

function findChapterForLine(lineNum) {{
    const lineEl = document.getElementById('line-' + lineNum);
    if (lineEl) {{
        const chapter = lineEl.closest('.chapter');
        if (chapter) {{
            return parseInt(chapter.dataset.chapter);
        }}
    }}
    return null;
}}

function goToLine(lineNum) {{
    const chapterIndex = findChapterForLine(lineNum);
    if (chapterIndex !== null) {{
        showChapter(chapterIndex);
        setTimeout(() => {{
            const lineEl = document.getElementById('line-' + lineNum);
            if (lineEl) {{
                document.querySelectorAll('.highlighted-line').forEach(el => el.classList.remove('highlighted-line'));
                lineEl.classList.add('highlighted-line');
                lineEl.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
            }}
        }}, 100);
        return true;
    }}
    return false;
}}

function handleHashNavigation() {{
    const hash = window.location.hash;
    const match = hash.match(/line-(\\d+)/);
    if (match) {{
        const lineNum = parseInt(match[1]);
        goToLine(lineNum);
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
            window.parent.postMessage({{ type: 'linePosition', line: lineNum }}, '*');
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
    <title>Literal Translation Collection</title>
    <meta name="generator" content="Literal Parser">
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
    if not INPUT_DIR.exists():
        print(f"Error: Input directory '{INPUT_DIR}' not found.")
        print("Please create a folder named 'literal' and place your .txt files there.")
        sys.exit(1)

    all_files = os.listdir(INPUT_DIR)
    matching_files = sorted([f for f in all_files if FILE_PATTERN.match(f)])

    if not matching_files:
        print(f"No files matching pattern '{FILE_PATTERN.pattern}' found in '{INPUT_DIR}'.")
        sys.exit(0)

    print(f"Found {len(matching_files)} file(s) to process.")

    chapters = {}
    total_lines = 0

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

            file_line_count = len(parsed_data)
            total_lines += file_line_count

            print(f"  ✓ Processed: {filename} ({file_line_count} lines)")

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
    print(f"  Total lines processed: {total_lines}")
    print(f"\nTo create PDF:")
    print(f"  1. Open '{OUTPUT_FILE}' in Chrome or Edge")
    print(f"  2. Press Ctrl+P (Print)")
    print(f"  3. Select 'Save as PDF'")
    print(f"  4. Ensure 'Background graphics' is checked")
    print(f"  5. Set margins to 'Default' or 'Minimum'")
    print(f"  6. Click Save")

if __name__ == "__main__":
    process_folder()
