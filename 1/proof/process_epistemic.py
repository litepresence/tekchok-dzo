#!/usr/bin/env python3
"""
Epistemic Layer Parser
Parses all matching files in 'epistemic/' folder and outputs a single
combined HTML file optimized for PDF rendering.
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

INPUT_DIR = Path("../text/layer/epistemic")
OUTPUT_FILE = Path("html/epistemic.html")
FILE_PATTERN = re.compile(r"^\d\d-\d\d-\d\d-\d\d\.txt$")

# Regex patterns
LINE_RANGE_PATTERN = re.compile(r"^\[(\d+-\d+)\]")
TAG_PATTERN = re.compile(r"^<(\w+)>(.*)$")


def get_chapter_key(filename):
    parts = filename.replace(".txt", "").split("-")
    if len(parts) >= 2:
        return f"{parts[0]}-{parts[1]}"
    return filename.replace(".txt", "")


# -----------------------------------------------------------------------------
# CSS STYLES (PDF-OPTIMIZED)
# -----------------------------------------------------------------------------

CSS_FILE = Path("css/epistemic.css")
HTML_CSS = Path(CSS_FILE).read_text(encoding="utf-8")

# -----------------------------------------------------------------------------
# PARSER LOGIC
# -----------------------------------------------------------------------------


def parse_entry(lines):
    """
    Parses a single epistemic entry (line range + metadata + classification).
    Handles classification content on same line OR subsequent lines.
    Returns a dict with line_range, view, pedagogy, risk, classification.
    """
    entry = {"line_range": None, "view": None, "pedagogy": None, "risk": None, "classification": []}

    in_classification = False

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Check for line range (starts new entry)
        range_match = LINE_RANGE_PATTERN.match(line)
        if range_match:
            entry["line_range"] = range_match.group(1)
            in_classification = False
            continue

        # Check for tags
        tag_match = TAG_PATTERN.match(line)
        if tag_match:
            tag_type = tag_match.group(1).lower()
            tag_value = tag_match.group(2).strip()

            if tag_type == "view":
                entry["view"] = tag_value
                in_classification = False
            elif tag_type == "pedagogy":
                entry["pedagogy"] = tag_value
                in_classification = False
            elif tag_type == "risk":
                entry["risk"] = tag_value
                in_classification = False
            elif tag_type == "classification":
                in_classification = True
                # Check if there's content after the tag on the same line
                if tag_value:
                    entry["classification"].append(tag_value)
            continue

        # If we're in classification mode, add line to classification
        if in_classification and entry["line_range"]:
            entry["classification"].append(line)

    # Join classification paragraphs
    entry["classification_text"] = " ".join(entry["classification"])

    # Highlight Tibetan text in classification
    entry["classification_text"] = highlight_tibetan(entry["classification_text"])

    return entry


def highlight_tibetan(text):
    """Wraps Tibetan text segments in span for styling."""
    # Detection: if text contains Tibetan Unicode range
    tibetan_pattern = re.compile(r"([\u0F00-\u0FFF]+)")
    return tibetan_pattern.sub(r'<span class="tibetan-inline">\1</span>', text)


def split_into_entries(content):
    """
    Splits file content into individual entries.
    More robust splitting that handles various formatting.
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


def generate_file_html(parsed_lines, filename):
    """Generates HTML content for a single file."""
    html_parts = []

    file_title = filename.replace(".txt", "").replace("-", " ")
    file_id = filename.replace(".txt", "")
    html_parts.append(f'<div class="file-separator" id="file-{file_id}">{file_title}</div>')

    line_counter = {}

    for entry in parsed_lines:
        if not entry["line_range"]:
            continue

        range_parts = entry["line_range"].split("-")
        first_line = range_parts[0] if range_parts else "1"
        last_line = range_parts[1] if len(range_parts) > 1 else first_line

        if first_line not in line_counter:
            line_counter[first_line] = 0
        line_counter[first_line] += 1
        unique_id = f"{first_line}-{line_counter[first_line]}"

        html_parts.append(
            f'<div class="entry-block" id="line-{unique_id}" data-line="{first_line}" data-range-start="{first_line}" data-range-end="{last_line}">'
        )

        html_parts.append(f'  <div class="line-range">[{entry["line_range"]}]</div>')

        html_parts.append('  <div class="metadata">')

        if entry["view"]:
            html_parts.append(
                f'    <span class="tag tag-view">View: {html.escape(entry["view"])}</span>'
            )

        if entry["pedagogy"]:
            html_parts.append(
                f'    <span class="tag tag-pedagogy">Pedagogy: {html.escape(entry["pedagogy"])}</span>'
            )

        if entry["risk"]:
            html_parts.append(
                f'    <span class="tag tag-risk">Risk: {html.escape(entry["risk"])}</span>'
            )

        html_parts.append("  </div>")

        if entry["classification_text"]:
            html_parts.append(f'  <div class="classification">{entry["classification_text"]}</div>')

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

    js_script = f"""
<script>
let currentChapter = 0;
const totalChapters = {total_chapters};
const chapterKeys = {chapter_keys};
</script>
<script src="../js/epistemic.js"></script>
"""

    combined_content = "\n".join(all_chapter_content)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Epistemic Layer Collection</title>
    <meta name="generator" content="Epistemic Parser">
    <meta name="created" content="{datetime.now().isoformat()}">
    <link rel="stylesheet" href="../css/epistemic.css">
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
        print("Please create a folder named 'epistemic' and place your .txt files there.")
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
            with open(input_path, "r", encoding="utf-8") as f:
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

    full_html = build_full_document(
        all_chapter_content, sorted_chapter_keys, len(sorted_chapter_keys)
    )

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(full_html)

    print(f"\n✓ Complete! Output saved to '{OUTPUT_FILE}'")
    print(f"  Total files combined: {len(matching_files)}")
    print(f"  Total chapters: {len(sorted_chapter_keys)}")
    print(f"  Total entries processed: {total_entries}")


if __name__ == "__main__":
    process_folder()
