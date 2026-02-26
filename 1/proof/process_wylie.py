#!/usr/bin/env python3
"""
Wylie Transliteration Parser
Parses all matching files in 'wylie/' folder and outputs a single 
combined HTML file optimized for PDF rendering.

This layer contains Tibetan text in Wylie transliteration.
"""

import html
import os
import re
import sys
from datetime import datetime
from pathlib import Path

INPUT_DIR = Path("../text/layer/wylie")
OUTPUT_FILE = Path("html/wylie.html")
FILE_PATTERN = re.compile(r"^\d\d-\d\d-\d\d-\d\d\.txt$")

LINE_PATTERN = re.compile(r'^\[(\d+)\]\s*(.*)$')
PAGE_MARKER = re.compile(r'^@#/$')
TERMINATOR = re.compile(r'\*/$')

def get_chapter_key(filename):
    parts = filename.replace('.txt', '').split('-')
    if len(parts) >= 2:
        return f"{parts[0]}-{parts[1]}"
    return filename.replace('.txt', '')

# -----------------------------------------------------------------------------
# CSS STYLES (PDF-OPTIMIZED FOR WYLIE)
# -----------------------------------------------------------------------------

CSS_FILE = Path("css/wylie.css")
HTML_CSS = Path(CSS_FILE).read_text(encoding='utf-8')

# -----------------------------------------------------------------------------
# PARSER LOGIC
# -----------------------------------------------------------------------------

def parse_line(raw_line):
    """Parses a single line of the Wylie text."""
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
    Processes Wylie text content for HTML styling.
    """
    # Escape HTML first
    content = html.escape(content)
    
    # Strip leading/trailing slashes from content
    content = content.strip('/')
    
    # Mark terminator markers (ending with */)
    content = re.sub(r'(.+)\*/$', r'<span class="terminator">\1*/</span>', content)
    
    # Highlight Sanskrit terms (capitalized words with +)
    content = re.sub(r'\+([A-Z][a-zA-Z]+)\+', r'<span class="sanskrit">+\1+</span>', content)
    
    # Mark Tibetan punctuation (common marks in Tibetan text rendered in Wylie)
    # Common: shad (//), tsheg (/)
    # These are part of the transliteration
    
    return content

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
        html_parts.append(f'  <div class="line-content" id="line-{line_num}"><span class="wylie-line" data-line="{line_num}">{content}</span></div>')

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
<script src="../js/wylie.js"></script>
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
    <title>Wylie Transliteration Collection</title>
    <meta name="generator" content="Wylie Parser">
    <meta name="created" content="{datetime.now().isoformat()}">
    <link rel="stylesheet" href="../css/wylie.css">
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
        print("Please create a folder named 'wylie' and place your .txt files there.")
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
    print(f"  Total lines processed: {total_lines}")

if __name__ == "__main__":
    process_folder()
