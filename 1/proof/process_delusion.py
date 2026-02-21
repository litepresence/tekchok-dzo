#!/usr/bin/env python3
"""
Delusion Analysis Parser
Parses all matching files in 'delusion/' folder and outputs a single 
combined HTML file optimized for PDF rendering.

This layer analyzes common misinterpretations and their consequences.
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

INPUT_DIR = Path("../text/dynamic/delusion")
OUTPUT_FILE = Path("html/delusion_proof.html")
FILE_PATTERN = re.compile(r"^\d\d-\d\d-\d\d-\d\d\.txt$")

LINE_RANGE_PATTERN = re.compile(r'^\[(\d+-\d+)\]')
TAG_PATTERN = re.compile(r'^<([^>]+)>')

def get_chapter_key(filename):
    parts = filename.replace('.txt', '').split('-')
    if len(parts) >= 2:
        return f"{parts[0]}-{parts[1]}"
    return filename.replace('.txt', '')

SECTION_HEADERS = {
    "misreading": "Misreading",
    "why_it_arises": "Why it arises",
    "primary_consequence": "Primary consequence",
    "secondary_consequences": "Secondary consequences",
    "cascade_effects": "Cascade effects"
}

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
        --color-error: #ef5350;
        --color-warning: #ffb74d;
        --color-consequence: #ff8a65;
        --color-cascade: #ba68c8;
        --color-line-range: #757575;
        --color-border: #3a3a3a;
        --color-btn: #5d4037;
        --color-btn-hover: #795548;
        
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
        color: var(--color-muted);
        font-size: 0.95em;
        letter-spacing: 2px;
        font-family: var(--font-sans);
    }
    .file-separator:first-child {
        margin-top: 0;
    }

    .entry-block {
        margin: 1.5em 0;
        padding: 0.75em;
        background-color: rgba(60, 40, 30, 0.3);
        border-left: 4px solid var(--color-error);
        page-break-inside: avoid;
    }

    /* Line range display */
    .line-range {
        font-family: var(--font-sans);
        font-size: 0.75em;
        color: var(--color-line-range);
        margin-bottom: 0.5em;
        font-weight: bold;
    }

    /* Error tags */
    .error-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 0.4em;
        margin-bottom: 0.75em;
    }

    .error-tag {
        padding: 2px 8px;
        border-radius: 3px;
        font-weight: 600;
        font-size: 0.7em;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        font-family: var(--font-sans);
    }

    .error-tag.ontological { background-color: rgba(198, 40, 40, 0.3); color: #ef9a9a; border: 1px solid rgba(198, 40, 40, 0.5); }
    .error-tag.reification { background-color: rgba(173, 20, 87, 0.3); color: #f48fb1; border: 1px solid rgba(173, 20, 87, 0.5); }
    .error-tag.temporal { background-color: rgba(230, 81, 0, 0.3); color: #ffcc80; border: 1px solid rgba(230, 81, 0, 0.5); }
    .error-tag.primordial { background-color: rgba(191, 54, 12, 0.3); color: #ffab91; border: 1px solid rgba(191, 54, 12, 0.5); }
    .error-tag.hierarchical { background-color: rgba(40, 53, 147, 0.3); color: #9fa8da; border: 1px solid rgba(40, 53, 147, 0.5); }
    .error-tag.meditationism { background-color: rgba(0, 105, 92, 0.3); color: #80cbc4; border: 1px solid rgba(0, 105, 92, 0.5); }
    .error-tag.nostalgia { background-color: rgba(85, 139, 47, 0.3); color: #c5e1a5; border: 1px solid rgba(85, 139, 47, 0.5); }
    .error-tag.acquisition { background-color: rgba(46, 125, 50, 0.3); color: #a5d6a7; border: 1px solid rgba(46, 125, 50, 0.5); }
    .error-tag.default {
        background-color: rgba(100, 100, 100, 0.3);
        color: var(--color-error);
        border: 1px solid rgba(100, 100, 100, 0.5);
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
        color: var(--color-error);
        padding: 10px 15px;
        border-radius: 5px;
        font-family: var(--font-sans);
        font-size: 12px;
        z-index: 1000;
    }

    .highlighted-line {
        background-color: rgba(239, 83, 80, 0.4) !important;
        border-radius: 3px;
        animation: highlightFade 3s ease-out forwards;
    }

    @keyframes highlightFade {{
        0% {{ background-color: rgba(239, 83, 80, 0.4); }}
        80% {{ background-color: rgba(239, 83, 80, 0.3); }}
        100% {{ background-color: transparent; }}
    }}

    /* Section headers */
    .section-header {
        font-family: var(--font-sans);
        font-size: 0.8em;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-top: 0.75em;
        margin-bottom: 0.25em;
    }

    .section-header.misreading {
        color: var(--color-error);
    }

    .section-header.why-it-arises {
        color: var(--color-warning);
    }

    .section-header.primary-consequence {
        color: var(--color-consequence);
    }

    .section-header.secondary-consequences {
        color: #f9a825;
    }

    .section-header.cascade_effects {
        color: var(--color-cascade);
    }

    /* Section content */
    .section-content {
        font-size: 0.9em;
        line-height: 1.5;
        text-align: justify;
        hyphens: auto;
        -webkit-hyphens: auto;
    }

    /* Cascade arrow styling */
    .cascade-chain {
        font-family: var(--font-mono);
        font-size: 0.8em;
        color: var(--color-cascade);
        background-color: #f3e5f5;
        padding: 0.25em 0.5em;
        border-radius: 3px;
        display: inline-block;
        margin: 0.25em 0;
    }

    /* Cascade arrows within content */
    .cascade-arrow {
        color: var(--color-cascade);
        font-weight: bold;
        margin: 0 0.25em;
    }

    @media print {
        body {
            font-size: 9.5pt;
        }
        .document {
            max-width: none;
        }
        a {
            text-decoration: none;
            color: inherit;
        }
        .entry-block {
            border-left: 2px solid #999;
        }
    }
</style>
"""

# -----------------------------------------------------------------------------
# PARSER LOGIC
# -----------------------------------------------------------------------------

def get_error_tag_class(tag):
    """Returns CSS class based on error tag type."""
    tag_lower = tag.lower()
    
    if "ontological" in tag_lower:
        return "ontological"
    elif "reification" in tag_lower:
        return "reification"
    elif "temporal" in tag_lower:
        return "temporal"
    elif "primordial" in tag_lower:
        return "primordial"
    elif "hierarchical" in tag_lower:
        return "hierarchical"
    elif "meditationism" in tag_lower:
        return "meditationism"
    elif "nostalgia" in tag_lower:
        return "nostalgia"
    elif "acquisition" in tag_lower:
        return "acquisition"
    else:
        return "default"

def parse_entry(lines):
    """
    Parses a single delusion entry with error tags and consequence sections.
    """
    entry = {
        "line_range": None,
        "error_tags": [],
        "sections": {}
    }

    current_section = None
    current_content = []

    for line in lines:
        line_stripped = line.strip()
        if not line_stripped:
            continue

        # Check for line range (starts new entry)
        range_match = LINE_RANGE_PATTERN.match(line_stripped)
        if range_match:
            entry["line_range"] = range_match.group(1)
            current_section = None
            current_content = []
            continue

        # Check for error tags
        tag_match = TAG_PATTERN.match(line_stripped)
        if tag_match:
            # Save previous section
            if current_section and current_content:
                entry["sections"][current_section] = " ".join(current_content)
            
            tag = tag_match.group(1)
            entry["error_tags"].append(tag)
            current_section = None
            current_content = []
            continue

        # Check for section headers (**Section:**) - use exact match to avoid partial matches
        section_key = None
        for key, title in SECTION_HEADERS.items():
            # Match exactly **Title:** with nothing else after
            if line_stripped == f"**{title}:**":
                section_key = key
                break
        
        if section_key:
            # Save previous section
            if current_section and current_content:
                entry["sections"][current_section] = " ".join(current_content)
            
            current_section = section_key
            current_content = []  # Start fresh
            continue

        # Check for cascade arrow patterns (within cascade section)
        if current_section == "cascade_effects":
            # Handle arrow chains - transform all <tag> → patterns
            # Match tags with or without spaces, hyphens
            line_stripped = re.sub(
                r'<([^>]+)>\s*→',
                r'<span class="cascade-arrow">→</span><span class="error-tag cascade">\1</span>',
                line_stripped
            )
            current_content.append(line_stripped)
        elif current_section:
            current_content.append(line_stripped)
        elif not entry["error_tags"]:
            # Content without section header goes to "content"
            if current_content or line_stripped:
                current_content.append(line_stripped)

    # Don't forget last section
    if current_section and current_content:
        entry["sections"][current_section] = " ".join(current_content)
    elif current_content:
        entry["sections"]["content"] = " ".join(current_content)

    # Build HTML for sections
    entry["sections_html"] = build_sections_html(entry)

    return entry

def build_sections_html(entry):
    """Builds HTML for entry sections."""
    html_parts = []
    
    for section_key, title in SECTION_HEADERS.items():
        if section_key in entry["sections"]:
            content = entry["sections"][section_key]
            
            # Skip empty sections
            if not content.strip():
                continue
            
            # Process cascade arrows for cascade effects
            if section_key == "cascade_effects":
                # Don't escape - already contains HTML spans from parsing
                html_parts.append(f'<div class="section-header {section_key}">{title}</div>')
                html_parts.append(f'<div class="section-content">{content}</div>')
            else:
                html_parts.append(f'<div class="section-header {section_key}">{title}</div>')
                html_parts.append(f'<div class="section-content">{html.escape(content)}</div>')
    
    # Add any untagged content
    if "content" in entry["sections"] and "misreading" not in entry["sections"]:
        html_parts.append(f'<div class="section-content">{html.escape(entry["sections"]["content"])}</div>')
    
    return "\n".join(html_parts)

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

    line_counter = {}
    
    for entry in entries:
        if not entry["line_range"]:
            continue

        range_parts = entry["line_range"].split('-')
        first_line = range_parts[0] if range_parts else "1"
        
        if first_line not in line_counter:
            line_counter[first_line] = 0
        line_counter[first_line] += 1
        unique_id = f"{first_line}-{line_counter[first_line]}"

        html_parts.append(f'<div class="entry-block" id="line-{unique_id}" data-line="{first_line}">')

        html_parts.append(f'  <div class="line-range">[{entry["line_range"]}]</div>')

        if entry["error_tags"]:
            html_parts.append('  <div class="error-tags">')
            for tag in entry["error_tags"]:
                tag_class = get_error_tag_class(tag)
                html_parts.append(f'    <span class="error-tag {tag_class}">{tag}</span>')
            html_parts.append('  </div>')

        if entry["sections_html"]:
            html_parts.append(f'  {entry["sections_html"]}')

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
    <title>Delusion Analysis Collection</title>
    <meta name="generator" content="Delusion Parser">
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
        print("Please create a folder named 'delusion' and place your .txt files there.")
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
