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

INPUT_DIR = Path("../text/layer/delusion")
OUTPUT_FILE = Path("html/delusion.html")
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

CSS_FILE = Path("css/delusion.css")
HTML_CSS = Path(CSS_FILE).read_text(encoding='utf-8')

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
            # First convert valid <...> patterns to spans (they're error tags in cascade context)
            line_stripped = re.sub(
                r'<([a-zA-Z][a-zA-Z0-9_\s-]*)>',
                r'<span class="error-tag cascade">\1</span>',
                line_stripped
            )
            # Then escape any remaining unescaped < characters that aren't part of tags
            line_stripped = re.sub(r'<(?!/?span)', '&lt;', line_stripped)
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

function goToLine(lineNum, volume) {{
    volume = volume || 1;
    const volPrefix = volume === 1 ? '01-' : '02-';
    
    let lineEl = document.getElementById('line-' + lineNum);
    
    if (!lineEl) {{
        // Only search within chapters of the correct volume
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
    // Format: #line-VOL-LINENUM or just #line-LINENUM
    const match = hash.match(/line-(\d+)(?:-(\d+))?/);
    if (match) {{
        let lineNum, volume;
        if (match[2]) {{
            // Format: #line-VOL-LINENUM
            volume = parseInt(match[1]);
            lineNum = parseInt(match[2]);
        }} else {{
            // Format: #line-LINENUM (backward compat)
            lineNum = parseInt(match[1]);
            volume = 1;
        }}
        goToLine(lineNum, volume);
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
            const chapter = closest.closest('[data-chapter-key]');
            const chapterKey = chapter ? chapter.dataset.chapterKey : '01-01';
            const volume = chapterKey.startsWith('02-') ? 2 : 1;
            window.parent.postMessage({{ type: 'linePosition', line: lineNum, volume: volume }}, '*');
        }}
    }}
}}

document.addEventListener('DOMContentLoaded', () => {{
    console.log('Delusion page loaded, initializing navigation...');
    updateNavButtons();
    updateIndicator();
    handleHashNavigation();
    
    // Verify elements exist
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const indicator = document.getElementById('chapterIndicator');
    console.log('Navigation elements:', {{ prevBtn, nextBtn, indicator }});
    
    window.addEventListener('scroll', reportCurrentLine);
    setTimeout(reportCurrentLine, 500);
}});

window.addEventListener('hashchange', handleHashNavigation);

// Dark mode handling - sync with parent
(function() {{
    const isDark = localStorage.getItem('darkMode') !== 'false';
    if (!isDark) document.body.classList.add('light-mode');
    
    window.addEventListener('message', function(e) {{
        if (e.data && e.data.type === 'darkModeChange') {{
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
    <title>Delusion Analysis Collection</title>
    <meta name="generator" content="Delusion Parser">
    <meta name="created" content="{datetime.now().isoformat()}">
    <link rel="stylesheet" href="../css/delusion.css">
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
