#!/usr/bin/env python3
"""
Commentary Layer Parser
Parses all matching files in 'commentary/' folder and outputs a single 
combined HTML file optimized for PDF rendering.

This layer contains poetic philosophical prose with line ranges only.
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

INPUT_DIR = Path("../text/dynamic/commentary")
OUTPUT_FILE = Path("html/commentary_proof.html")
FILE_PATTERN = re.compile(r"^\d\d-\d\d-\d\d-\d\d\.txt$")

LINE_RANGE_PATTERN = re.compile(r'^\[(\d+-\d+)\]')

def get_chapter_key(filename):
    parts = filename.replace('.txt', '').split('-')
    if len(parts) >= 2:
        return f"{parts[0]}-{parts[1]}"
    return filename.replace('.txt', '')

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
        --font-mono: 'Consolas', 'Courier New', monospace;
        
        --color-bg: #1e1e1e;
        --color-text: #e0e0e0;
        --color-muted: #a0a0a0;
        --color-accent: #9c6ade;
        --color-line-range: #757575;
        --color-border: #3a3a3a;
        --color-btn: #2d5a7b;
        --color-btn-hover: #3d7a9b;
        
        --line-height: 1.6;
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
        font-family: var(--font-sans);
    }
    .file-separator:first-child {
        margin-top: 0;
    }

    .entry-block {
        margin: 1.5em 0;
        padding: 0.5em 0;
        page-break-inside: avoid;
    }

    .line-range {
        font-family: var(--font-sans);
        font-size: 0.7em;
        color: var(--color-line-range);
        margin-bottom: 0.5em;
        font-weight: bold;
        letter-spacing: 1px;
    }

    .commentary-content {
        font-size: 1em;
        text-align: left;
        line-height: 1.7;
        color: var(--color-text);
        font-style: italic;
    }

    .emphasis {
        font-weight: 600;
        color: var(--color-accent);
    }

    .term {
        font-style: italic;
        color: var(--color-muted);
    }

    .key-term {
        font-style: italic;
        border-bottom: 1px dotted var(--color-accent);
    }

    .tibetan-inline {
        font-family: 'Jomolhari', 'Noto Sans Tibetan', serif;
        font-size: 0.9em;
        color: var(--color-muted);
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

    .highlighted-line {
        background-color: rgba(156, 106, 222, 0.4) !important;
        border-radius: 3px;
        animation: highlightFade 3s ease-out forwards;
    }

    @keyframes highlightFade {
        0% { background-color: rgba(156, 106, 222, 0.4); }
        80% { background-color: rgba(156, 106, 222, 0.3); }
        100% { background-color: transparent; }
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

def parse_entry(lines):
    """
    Parses a single commentary entry (line range + prose content).
    """
    entry = {
        "line_range": None,
        "content": []
    }

    in_content = False

    for line in lines:
        line_stripped = line.strip()
        if not line_stripped:
            continue

        # Check for line range (starts new entry)
        range_match = LINE_RANGE_PATTERN.match(line_stripped)
        if range_match:
            entry["line_range"] = range_match.group(1)
            in_content = True
            continue

        # Content line
        if in_content:
            entry["content"].append(line_stripped)

    # Join and process content
    entry["content_text"] = " ".join(entry["content"])
    
    # Highlight Tibetan text
    entry["content_text"] = highlight_tibetan(entry["content_text"])
    
    # Process key terms (italicize words in parentheses)
    entry["content_text"] = re.sub(r'\(([^)]+)\)', r'<span class="term">(\1)</span>', entry["content_text"])
    
    return entry

def highlight_tibetan(text):
    """Wraps Tibetan text segments in span for styling."""
    tibetan_pattern = re.compile(r'([\u0F00-\u0FFF]+)')
    return tibetan_pattern.sub(r'<span class="tibetan-inline">\1</span>', text)

def split_into_entries(content):
    """
    Splits file content into individual entries.
    """
    entries = []
    current_entry = []
    in_entry = False

    for line in content.splitlines():
        line_stripped = line.strip()

        # Check if this line starts a new entry (has line range)
        if LINE_RANGE_PATTERN.match(line_stripped):
            # Save previous entry if exists
            if current_entry:
                entries.append("\n".join(current_entry))
            # Start new entry
            current_entry = [line_stripped]
            in_entry = True
        elif in_entry:
            # Continue current entry
            current_entry.append(line_stripped)

    # Don't forget the last entry
    if current_entry:
        entries.append("\n".join(current_entry))

    return entries

def generate_file_html(entries, filename):
    """Generates HTML content for a single file."""
    html_parts = []
    
    file_title = filename.replace('.txt', '').replace('-', ' ')
    file_id = filename.replace('.txt', '')
    html_parts.append(f'<div class="file-separator" id="file-{file_id}">{file_title}</div>')

    for entry in entries:
        if not entry["line_range"]:
            continue

        # Get first line number from range for ID
        range_parts = entry["line_range"].split('-')
        first_line = range_parts[0] if range_parts else "1"

        html_parts.append(f'<div class="entry-block" id="line-{first_line}" data-line="{first_line}">')

        # Line range
        html_parts.append(f'  <div class="line-range">[{entry["line_range"]}]</div>')

        # Content
        if entry["content_text"]:
            html_parts.append(f'  <div class="commentary-content">{html.escape(entry["content_text"])}</div>')

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

function goToLine(lineNum) {{
    let lineEl = document.getElementById('line-' + lineNum);
    
    if (!lineEl) {{
        const allLines = document.querySelectorAll('[id^="line-"]');
        let bestMatch = null;
        let bestDiff = Infinity;
        
        for (const el of allLines) {{
            const elLine = parseInt(el.id.replace('line-', ''));
            const diff = Math.abs(elLine - lineNum);
            if (diff < bestDiff) {{
                bestDiff = diff;
                bestMatch = el;
            }}
        }}
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
    
    window.addEventListener('scroll', reportCurrentLine);
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
    <title>Commentary Collection</title>
    <meta name="generator" content="Commentary Parser">
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
        print("Please create a folder named 'commentary' and place your .txt files there.")
        sys.exit(1)

    all_files = os.listdir(INPUT_DIR)
    matching_files = sorted([f for f in all_files if FILE_PATTERN.match(f)])

    if not matching_files:
        print(f"No files matching pattern '{FILE_PATTERN.pattern}' found in '{INPUT_DIR}'.")
        sys.exit(0)

    print(f"Found {len(matching_files)} file(s) to process.")

    chapters = {}
    total_entries = 0

    for filename in matching_files:
        input_path = INPUT_DIR / filename

        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                content = f.read()

            raw_entries = split_into_entries(content)
            entries = [parse_entry(e.splitlines()) for e in raw_entries]
            entries = [e for e in entries if e["line_range"]]

            file_html = generate_file_html(entries, filename)
            
            chapter_key = get_chapter_key(filename)
            if chapter_key not in chapters:
                chapters[chapter_key] = []
            chapters[chapter_key].append(file_html)

            file_entry_count = len(entries)
            total_entries += file_entry_count

            print(f"  ✓ Processed: {filename} ({file_entry_count} entries)")

        except Exception as e:
            print(f"  ✗ Error processing {filename}: {e}")
            import traceback
            traceback.print_exc()

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
    print(f"  Total entries processed: {total_entries}")

if __name__ == "__main__":
    process_folder()
