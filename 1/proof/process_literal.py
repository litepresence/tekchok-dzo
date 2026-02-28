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

INPUT_DIR = Path("../text/layer/literal")
OUTPUT_FILE = Path("html/literal.html")
FILE_PATTERN = re.compile(r"^\d\d-\d\d-\d\d-\d\d\.txt$")

# Regex to parse lines: [LineNum] Content
LINE_PATTERN = re.compile(r"^\[(\d+)\]\s*(.*)$")

# -----------------------------------------------------------------------------
# CSS STYLES (PDF-OPTIMIZED)
# -----------------------------------------------------------------------------

CSS_FILE = Path("css/literal.css")
HTML_CSS = Path(CSS_FILE).read_text(encoding="utf-8")

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

    return {"line_num": line_num, "content": processed_content}


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
    content = content.replace("/", "")

    # Strip any resulting extra whitespace
    content = " ".join(content.split())

    # Highlight grammatical markers (common patterns in literal translations)
    # Must be done BEFORE compound wrapping to avoid conflicts
    grammar_markers = [
        "genitive",
        "locative",
        "instrumental",
        "dative",
        "ablative",
        "nominative",
        "accusative",
        "vocative",
        "ergative",
    ]

    for marker in grammar_markers:
        # Match hyphenated grammar markers and keep them attached to previous word
        pattern = rf"(-{marker})(\s|$)"
        replacement = r'<span class="grammar_marker">\1</span>\2'
        content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)

    # Wrap hyphenated compounds for potential styling (keep together with nowrap)
    content = re.sub(r"([a-zA-Z]+)-([a-zA-Z]+)", r'<span class="compound">\1-\2</span>', content)

    return content


def get_chapter_key(filename):
    parts = filename.replace(".txt", "").split("-")
    if len(parts) >= 2:
        return f"{parts[0]}-{parts[1]}"
    return filename.replace(".txt", "")


def generate_file_html(parsed_lines, filename):
    """Generates HTML content for a single file."""
    html_parts = []

    file_title = filename.replace(".txt", "").replace("-", " ")
    file_id = filename.replace(".txt", "")
    html_parts.append(f'<div class="file-separator" id="file-{file_id}">{file_title}</div>')
    html_parts.append('<div class="line-grid">')

    for item in parsed_lines:
        if not item:
            continue

        line_num = item["line_num"]
        content = item["content"]

        html_parts.append(f'  <div class="line-num">{line_num}</div>')
        html_parts.append(
            f'  <div class="line-content" id="line-{line_num}"><span class="literal-line" data-line="{line_num}">{content}</span></div>'
        )

    html_parts.append("</div>")

    return "\n".join(html_parts)


def build_chapter_html(file_html_list, chapter_key, chapter_index):
    """Wraps all files in a chapter into a chapter div."""
    active_class = " active" if chapter_index == 0 else ""
    parts = [
        f'<div class="chapter{active_class}" data-chapter="{chapter_index}" data-chapter-key="{chapter_key}">'
    ]
    parts.extend(file_html_list)
    parts.append("</div>")
    return "\n".join(parts)


def build_full_document(all_chapter_content, chapter_keys, total_chapters):
    """Wraps everything in HTML5 boilerplate with navigation."""

    js_script = f"""<script>
let currentChapter = 0;
const totalChapters = {total_chapters};
const chapterKeys = {chapter_keys};
</script>
<script src="../js/literal.js"></script>
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
    <link rel="stylesheet" href="../css/literal.css">
    {js_script}
</head>
<body>
    <div class="document">
        {combined_content}
    </div>
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
            with open(input_path, "r", encoding="utf-8") as f:
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

    full_html = build_full_document(
        all_chapter_content, sorted_chapter_keys, len(sorted_chapter_keys)
    )

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
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
