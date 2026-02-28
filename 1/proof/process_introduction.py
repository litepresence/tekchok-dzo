#!/usr/bin/env python3
"""
Introduction Parser
Parses main introduction, volume introductions, and chapter introductions
and outputs a single combined HTML file optimized for PDF rendering and iframe navigation.
"""

import html
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

# -----------------------------------------------------------------------------
# CONFIGURATION
# -----------------------------------------------------------------------------
# Adjust these paths based on where this script runs relative to the text folder
BASE_DIR = Path("../text/preface")
INTRO_DIR = BASE_DIR / "introduction"
VOLUME_DIR = BASE_DIR / "volume"
CHAPTER_DIR = BASE_DIR / "chapter"
OUTPUT_FILE = Path("html/introduction.html")
ALN_MAP_FILE = Path("ALN_map.json")


# Load ALN map for data-aln attributes
def load_aln_map():
    if ALN_MAP_FILE.exists():
        with open(ALN_MAP_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return None


ALN_MAP = load_aln_map()


# Map introduction section IDs to ALN section keys
def get_aln_range_for_section(section_id):
    """Map introduction section ID to ALN range."""
    if not ALN_MAP:
        return None, None

    # Direct mapping from intro ID to ALN section key
    mapping = {
        "intro-main": "01-01-01-01",
        "vol-01": "01-01-01-01",
        "vol-02": "02-15-01-01",
    }

    # For chapters, construct the section key
    if section_id.startswith("chap-"):
        parts = section_id.replace("chap-", "").split("-")
        if len(parts) >= 2:
            vol = parts[0].zfill(2)
            ch = parts[1].zfill(2)
            mapping[section_id] = f"{vol}-{ch}-01-01"

    section_key = mapping.get(section_id)
    if section_key and section_key in ALN_MAP:
        return ALN_MAP[section_key][0], ALN_MAP[section_key][1]

    return None, None


# Define the exact sequence of files to ensure correct navigation order
FILE_SEQUENCE = [
    # Main Introduction
    {
        "type": "main",
        "path": INTRO_DIR / "intro.md",
        "id": "intro-main",
        "title": "General Introduction",
    },
    # Volume 1
    {
        "type": "volume",
        "path": VOLUME_DIR / "01-00-00-00.txt",
        "id": "vol-01",
        "title": "Volume 1 Introduction",
    },
    # Volume 1 Chapters
    {
        "type": "chapter",
        "path": CHAPTER_DIR / "01-01-00-00.txt",
        "id": "chap-01-01",
        "title": "Chapter 1: The Perfect Teacher",
    },
    {
        "type": "chapter",
        "path": CHAPTER_DIR / "01-02-00-00.txt",
        "id": "chap-01-02",
        "title": "Chapter 2: The Container and Contents",
    },
    {
        "type": "chapter",
        "path": CHAPTER_DIR / "01-03-00-00.txt",
        "id": "chap-01-03",
        "title": "Chapter 3: Aggregates, Elements, and Sense Sources",
    },
    {
        "type": "chapter",
        "path": CHAPTER_DIR / "01-04-00-00.txt",
        "id": "chap-01-04",
        "title": "Chapter 4: Vehicle Enumeration",
    },
    {
        "type": "chapter",
        "path": CHAPTER_DIR / "01-05-00-00.txt",
        "id": "chap-01-05",
        "title": "Chapter 5: Empowerment and Samaya",
    },
    {
        "type": "chapter",
        "path": CHAPTER_DIR / "01-06-00-00.txt",
        "id": "chap-01-06",
        "title": "Chapter 6: Samaya Discipline",
    },
    {
        "type": "chapter",
        "path": CHAPTER_DIR / "01-07-00-00.txt",
        "id": "chap-01-07",
        "title": "Chapter 7: Samaya Restoration",
    },
    {
        "type": "chapter",
        "path": CHAPTER_DIR / "01-08-00-00.txt",
        "id": "chap-01-08",
        "title": "Chapter 8: Ground, Path, and Fruit",
    },
    {
        "type": "chapter",
        "path": CHAPTER_DIR / "01-09-00-00.txt",
        "id": "chap-01-09",
        "title": "Chapter 9: Delusion and Liberation",
    },
    {
        "type": "chapter",
        "path": CHAPTER_DIR / "01-10-00-00.txt",
        "id": "chap-01-10",
        "title": "Chapter 10: Arising of Elements",
    },
    {
        "type": "chapter",
        "path": CHAPTER_DIR / "01-11-00-00.txt",
        "id": "chap-01-11",
        "title": "Chapter 11: Body Formation",
    },
    {
        "type": "chapter",
        "path": CHAPTER_DIR / "01-12-00-00.txt",
        "id": "chap-01-12",
        "title": "Chapter 12: Channels, Winds, and Bindu",
    },
    {
        "type": "chapter",
        "path": CHAPTER_DIR / "01-13-00-00.txt",
        "id": "chap-01-13",
        "title": "Chapter 13: Luminosity",
    },
    {
        "type": "chapter",
        "path": CHAPTER_DIR / "01-14-00-00.txt",
        "id": "chap-01-14",
        "title": "Chapter 14: Mind and Pristine Awareness",
    },
    # Volume 2
    {
        "type": "volume",
        "path": VOLUME_DIR / "02-00-00-00.txt",
        "id": "vol-02",
        "title": "Volume 2 Introduction",
    },
    # Volume 2 Chapters
    {
        "type": "chapter",
        "path": CHAPTER_DIR / "02-15-00-00.txt",
        "id": "chap-02-15",
        "title": "Chapter 15: Elements Place",
    },
    {
        "type": "chapter",
        "path": CHAPTER_DIR / "02-16-00-00.txt",
        "id": "chap-02-16",
        "title": "Chapter 16: Kaya and Wisdom",
    },
    {
        "type": "chapter",
        "path": CHAPTER_DIR / "02-17-00-00.txt",
        "id": "chap-02-17",
        "title": "Chapter 17: Path and Signs",
    },
    {
        "type": "chapter",
        "path": CHAPTER_DIR / "02-18-00-00.txt",
        "id": "chap-02-18",
        "title": "Chapter 18: Luminosity Path",
    },
    {
        "type": "chapter",
        "path": CHAPTER_DIR / "02-19-00-00.txt",
        "id": "chap-02-19",
        "title": "Chapter 19: Cutting Through",
    },
    {
        "type": "chapter",
        "path": CHAPTER_DIR / "02-20-00-00.txt",
        "id": "chap-02-20",
        "title": "Chapter 20: Leap-Over",
    },
    {
        "type": "chapter",
        "path": CHAPTER_DIR / "02-21-00-00.txt",
        "id": "chap-02-21",
        "title": "Chapter 21: Introduction",
    },
    {
        "type": "chapter",
        "path": CHAPTER_DIR / "02-22-00-00.txt",
        "id": "chap-02-22",
        "title": "Chapter 22: Signs of Liberation",
    },
    {
        "type": "chapter",
        "path": CHAPTER_DIR / "02-23-00-00.txt",
        "id": "chap-02-23",
        "title": "Chapter 23: Intermediate State",
    },
    {
        "type": "chapter",
        "path": CHAPTER_DIR / "02-24-00-00.txt",
        "id": "chap-02-24",
        "title": "Chapter 24: Emanation Field",
    },
    {
        "type": "chapter",
        "path": CHAPTER_DIR / "02-25-00-00.txt",
        "id": "chap-02-25",
        "title": "Chapter 25: Fruition",
    },
]

# -----------------------------------------------------------------------------
# CSS STYLES (PDF-OPTIMIZED)
# -----------------------------------------------------------------------------
CSS_FILE = Path("css/introduction.css")
HTML_CSS = Path(CSS_FILE).read_text(encoding="utf-8")


# -----------------------------------------------------------------------------
# PARSER LOGIC
# -----------------------------------------------------------------------------
def parse_markdown_text(text):
    """
    Converts simple Markdown syntax to HTML.
    Handles headers, bold, lists, and paragraphs.
    """
    # Escape HTML first
    text = html.escape(text)

    # Headers
    text = re.sub(r"^### (.+)$", r"<h3>\1</h3>", text, flags=re.MULTILINE)
    text = re.sub(r"^## (.+)$", r"<h2>\1</h2>", text, flags=re.MULTILINE)
    text = re.sub(r"^# (.+)$", r"<h1>\1</h1>", text, flags=re.MULTILINE)

    # Bold
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)

    # Lists (simple bullet points)
    text = re.sub(r"^- (.+)$", r"<li>\1</li>", text, flags=re.MULTILINE)
    text = re.sub(r"(<li>.*?</li>\n?)+", lambda m: "<ul>" + m.group(0) + "</ul>", text)

    # Paragraphs (split by double newline)
    paragraphs = text.split("\n\n")
    html_parts = []
    for p in paragraphs:
        p = p.strip()
        if p and not p.startswith("<h") and not p.startswith("<ul") and not p.startswith("<li"):
            html_parts.append(f"<p>{p}</p>")
        else:
            html_parts.append(p)

    return "\n".join(html_parts)


def generate_section_html(file_data, content):
    """Generates HTML content for a single introduction section."""
    # Get ALN range for this section
    aln_start, aln_end = get_aln_range_for_section(file_data["id"])

    html_parts = []
    attrs = f'id="{file_data["id"]}"'
    if aln_start:
        attrs += f' data-aln-start="{aln_start}"'
    if aln_end:
        attrs += f' data-aln-end="{aln_end}"'

    html_parts.append(f'<div class="intro-section" {attrs}>')
    html_parts.append(f'<h2 class="intro-header">{file_data["title"]}</h2>')
    html_parts.append('<div class="intro-content">')
    html_parts.append(parse_markdown_text(content))
    html_parts.append("</div>")
    html_parts.append("</div>")
    return "\n".join(html_parts)


def build_full_document(sections_html, total_sections):
    """Wraps everything in HTML5 boilerplate with navigation."""
    # Create JS array of section IDs for navigation
    section_ids = [s["id"] for s in FILE_SEQUENCE]
    section_titles = [s["title"] for s in FILE_SEQUENCE]

    js_script = f"""
<script>
let currentChapter = 0;
const totalChapters = {total_sections};
const chapterKeys = {section_ids};
const chapterTitles = {section_titles};
</script>
<script src="../js/introduction.js"></script>
"""
    combined_content = "\n".join(sections_html)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Treasury Introductions</title>
    <meta name="generator" content="Introduction Parser">
    <meta name="created" content="{datetime.now().isoformat()}">
    <link rel="stylesheet" href="../css/introduction.css">
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
def process_introductions():
    sections_html = []
    valid_sections = 0

    print(f"Processing introductions...")

    for file_data in FILE_SEQUENCE:
        path = file_data["path"]
        if not path.exists():
            print(f"  ⚠ Warning: File not found: {path}")
            # Create a placeholder if file is missing to maintain navigation structure
            content = f"*Introduction file not found: {path.name}*"
        else:
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception as e:
                print(f"  ✗ Error reading {path}: {e}")
                content = f"*Error reading file: {e}*"

        section_html = generate_section_html(file_data, content)
        sections_html.append(section_html)
        valid_sections += 1
        print(f"  ✓ Processed: {file_data['title']}")

    full_html = build_full_document(sections_html, valid_sections)

    # Ensure output directory exists
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(full_html)

    print(f"\n✓ Complete! Output saved to '{OUTPUT_FILE}'")
    print(f"  Total sections: {valid_sections}")
    print(f"\nIntegration Note:")
    print(f"  Add a radio button to index.html with value='introduction'")
    print(f"  Target iframe should load '{OUTPUT_FILE.name}'")
    print(f"  Pass chapter/volume params via URL or postMessage for sync.")


if __name__ == "__main__":
    process_introductions()
