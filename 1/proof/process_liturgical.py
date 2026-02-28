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

import html
import os
import re
import sys
from datetime import datetime
from pathlib import Path

# -----------------------------------------------------------------------------
# CONFIGURATION
# -----------------------------------------------------------------------------

INPUT_DIR = Path("../text/layer/liturgical")
OUTPUT_FILE = Path("html/liturgical.html")
FILE_PATTERN = re.compile(r"^\d\d-\d\d-\d\d-\d\d\.txt$")

# Regex to parse lines: [LineNum] [<break>] <Tag> Content
LINE_PATTERN = re.compile(r"^\[(\d+)\]\s*(?:(<break>)\s*)?<(\w+)>\s*(.*)$")

# -----------------------------------------------------------------------------
# CSS STYLES (PDF-OPTIMIZED)
# -----------------------------------------------------------------------------

CSS_FILE = Path("css/liturgical.css")
HTML_CSS = Path(CSS_FILE).read_text(encoding="utf-8")

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
        "content": html.escape(content),
    }


def get_chapter_key(filename):
    parts = filename.replace(".txt", "").split("-")
    if len(parts) >= 2:
        return f"{parts[0]}-{parts[1]}"
    return filename.replace(".txt", "")


def generate_file_html(parsed_lines, filename):
    """Generates HTML content for a single file.

    Updates: Groups consecutive lines with the same tag and no break
    into single HTML elements. Prose joins with spaces; others join with <br>.
    """
    html_parts = []

    file_title = filename.replace(".txt", "").replace("-", " ")
    file_id = filename.replace(".txt", "")
    html_parts.append(f'<div class="file-separator" id="file-{file_id}">{file_title}</div>')

    groups = []
    current_group = None

    for item in parsed_lines:
        if not item:
            continue

        can_merge = False
        if current_group:
            if (
                item["tag"] == current_group["tag"]
                and not current_group["is_break"]
                and not item["is_break"]
            ):
                can_merge = True

        if can_merge:
            if item["tag"] == "prose":
                current_group["content"] += " " + item["content"]
            else:
                current_group["content"] += "<br>" + item["content"]
        else:
            if current_group:
                groups.append(current_group)
            current_group = item.copy()

    if current_group:
        groups.append(current_group)

    for item in groups:
        tag = item["tag"]
        content = item["content"]
        is_break = item["is_break"]

        classes = [tag]
        if is_break:
            classes.append("break-before")

        class_str = " ".join(classes)

        if tag == "mantra":
            content_html = f'<span class="mantra">{content}</span>'
        else:
            content_html = content

        content_html = re.sub(
            r"\|\|\s*(\d+)\s*\|\|", r'<span class="verse-marker">|| \1 ||</span>', content_html
        )

        html_parts.append(
            f'<div class="{class_str}" id="line-{item["line_num"]}" data-line="{item["line_num"]}">{content_html}</div>'
        )

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

    js_script = f"""
<script>
let currentChapter = 0;
const totalChapters = {total_chapters};
const chapterKeys = {chapter_keys};
</script>
<script src="../js/liturgical.js"></script>
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
    <link rel="stylesheet" href="../css/liturgical.css">
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
            with open(input_path, "r", encoding="utf-8") as f:
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

    full_html = build_full_document(
        all_chapter_content, sorted_chapter_keys, len(sorted_chapter_keys)
    )

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
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
