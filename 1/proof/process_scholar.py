#!/usr/bin/env python3
"""
Scholarly Analysis Parser
Parses all matching files in 'scholar/' folder and outputs a single 
combined HTML file optimized for PDF rendering.
"""

import html
import os
import re
import sys
from datetime import datetime
from pathlib import Path

INPUT_DIR = Path("../text/layer/scholar")
OUTPUT_FILE = Path("html/scholar.html")
FILE_PATTERN = re.compile(r"^\d\d-\d\d-\d\d-\d\d\.txt$")

LINE_RANGE_PATTERN = re.compile(r'^\[(\d+-\d+)\]')
TAG_PATTERN = re.compile(r'^<(\w+)>(.*)$')
HEADING_PATTERN = re.compile(r'^#\s+(.+)$')
SEPARATOR_PATTERN = re.compile(r'^---+$')

def get_chapter_key(filename):
    parts = filename.replace('.txt', '').split('-')
    if len(parts) >= 2:
        return f"{parts[0]}-{parts[1]}"
    return filename.replace('.txt', '')

def preprocess_markdown(text):
    """Convert markdown formatting to HTML."""
    result = text
    
    result = re.sub(r'\*\*\*([^*]+)\*\*\*', r'<strong><em>\1</em></strong>', result)
    
    result = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', result)
    
    result = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', result)
    
    result = re.sub(r'^- (.+)$', r'<li>\1</li>', result, flags=re.MULTILINE)
    
    result = re.sub(r'(<li>.*?</li>\n?)+', lambda m: '<ul>' + m.group(0) + '</ul>', result)
    
    result = re.sub(r'</ul>\n<ul>', '', result)
    
    return result

# -----------------------------------------------------------------------------
# CSS STYLES (PDF-OPTIMIZED)
# -----------------------------------------------------------------------------

CSS_FILE = Path("css/scholar.css")
HTML_CSS = Path(CSS_FILE).read_text(encoding='utf-8')

# -----------------------------------------------------------------------------
# PARSER LOGIC
# -----------------------------------------------------------------------------

def parse_entry(lines):
    """
    Parses a single scholarly entry with tags: structure, philology, context, concept.
    Handles headings, analysis content, and section separators.
    """
    entry = {
        "line_range": None,
        "tag": None,
        "heading": None,
        "sections": []
    }

    current_section = {"heading": None, "content": []}
    in_content = False

    for line in lines:
        line_stripped = line.strip()
        if not line_stripped:
            continue

        # Check for combined line range + tag (e.g., "[1-4] <structure>")
        range_and_tag = re.match(r'^\[(\d+-\d+)\]\s*<(\w+)>(.*)$', line_stripped)
        if range_and_tag:
            entry["line_range"] = range_and_tag.group(1)
            tag_type = range_and_tag.group(2).lower()
            tag_value = range_and_tag.group(3).strip()
            entry["tag"] = tag_type
            if tag_value:
                entry["heading"] = tag_value
            in_content = True
            continue

        # Check for line range only (starts new entry)
        range_match = LINE_RANGE_PATTERN.match(line_stripped)
        if range_match:
            entry["line_range"] = range_match.group(1)
            continue

        # Check for tag only (on its own line)
        tag_match = TAG_PATTERN.match(line_stripped)
        if tag_match:
            tag_type = tag_match.group(1).lower()
            tag_value = tag_match.group(2).strip()
            entry["tag"] = tag_type
            if tag_value:
                entry["heading"] = tag_value
            in_content = True
            continue

        # Check for heading (# Title)
        heading_match = HEADING_PATTERN.match(line_stripped)
        if heading_match:
            if current_section["content"]:
                entry["sections"].append(current_section)
            current_section = {"heading": heading_match.group(1), "content": []}
            continue

        # Check for separator (---)
        if SEPARATOR_PATTERN.match(line_stripped):
            if current_section["content"]:
                entry["sections"].append(current_section)
                current_section = {"heading": None, "content": []}
            continue

        # Content line
        if in_content or current_section["content"]:
            current_section["content"].append(line_stripped)

    # Don't forget last section
    if current_section["content"]:
        entry["sections"].append(current_section)

    # Build full content text
    entry["full_content"] = build_content_text(entry)

    # Highlight Tibetan text
    entry["full_content"] = highlight_tibetan(entry["full_content"])

    return entry

def build_content_text(entry):
    """Builds HTML content from entry sections."""
    html_parts = []
    
    for section in entry["sections"]:
        if section["heading"]:
            html_parts.append(f'<div class="section-heading">{html.escape(section["heading"])}</div>')
        
        content_text = " ".join(section["content"])
        
        content_text = preprocess_markdown(content_text)
        
        content_text = re.sub(r'\*\*Analysis:\*\*', '<span class="analysis-header">Analysis:</span>', content_text)
        content_text = re.sub(r'\*\*Section Placement:\*\*', '<span class="analysis-header">Section Placement:</span>', content_text)
        content_text = re.sub(r'\*\*Connection to Following Sections:\*\*', '<span class="analysis-header">Connection to Following Sections:</span>', content_text)
        content_text = re.sub(r'\*\*Terminological Precision:\*\*', '<span class="analysis-header">Terminological Precision:</span>', content_text)
        content_text = re.sub(r'\*\*Key Terms:\*\*', '<span class="analysis-header">Key Terms:</span>', content_text)
        
        html_parts.append(f'<div class="analysis-content">{content_text}</div>')
    
    return "\n".join(html_parts)

def highlight_tibetan(text):
    """Wraps Tibetan text segments in span for styling."""
    tibetan_pattern = re.compile(r'([\u0F00-\u0FFF]+)')
    return tibetan_pattern.sub(r'<span class="tibetan-inline">\1</span>', text)

def split_into_entries(content):
    """
    Splits file content into individual entries.
    Each entry starts with a line range, even if same range appears multiple times.
    """
    entries = []
    current_entry = []
    in_entry = False

    for line in content.splitlines():
        line_stripped = line.strip()

        # Skip empty lines at the start
        if not line_stripped and not current_entry:
            continue

        # Check if this line starts a new entry (has line range)
        range_match = LINE_RANGE_PATTERN.match(line_stripped)
        if range_match:
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

def generate_file_html(parsed_lines, filename):
    """Generates HTML content for a single file."""
    html_parts = []
    
    file_title = filename.replace('.txt', '').replace('-', ' ')
    file_id = filename.replace('.txt', '')
    html_parts.append(f'<div class="file-separator" id="file-{file_id}">{file_title}</div>')

    line_counter = {}
    
    for entry in parsed_lines:
        if not entry["line_range"]:
            continue

        range_parts = entry["line_range"].split('-')
        first_line = range_parts[0] if range_parts else "1"
        
        if first_line not in line_counter:
            line_counter[first_line] = 0
        line_counter[first_line] += 1
        unique_id = f"{first_line}-{line_counter[first_line]}"

        tag_class = f"tag-{entry['tag']}" if entry['tag'] else ""
        html_parts.append(f'<div class="entry-block {tag_class}" id="line-{unique_id}" data-line="{first_line}">')

        html_parts.append(f'  <div class="line-range">[{entry["line_range"]}]</div>')

        if entry["tag"]:
            html_parts.append(f'  <div class="metadata">')
            html_parts.append(f'    <span class="tag tag-{entry["tag"]}">{entry["tag"].title()}</span>')
            html_parts.append(f'  </div>')

        if entry["full_content"]:
            html_parts.append(f'  {entry["full_content"]}')

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
</script>
<script src="../js/scholar.js"></script>
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
    <title>Scholarly Analysis Collection</title>
    <meta name="generator" content="Scholar Parser">
    <meta name="created" content="{datetime.now().isoformat()}">
    <link rel="stylesheet" href="../css/scholar.css">
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
        print("Please create a folder named 'scholar' and place your .txt files there.")
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
