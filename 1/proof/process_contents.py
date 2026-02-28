#!/usr/bin/env python3
"""
Contents Parser
Parses contents.md and outputs a single combined HTML file optimized for PDF rendering.
"""

import html
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

INPUT_FILE = Path("../contents/contents.md")
OUTPUT_FILE = Path("html/contents.html")
LITERAL_DIR = Path("../text/layer/literal")

LINE_MAP = {}


def build_line_map():
    """Build a mapping from file IDs to starting line numbers by scanning literal files."""
    global LINE_MAP
    current_line = 1

    files = sorted([f for f in os.listdir(LITERAL_DIR) if f.endswith(".txt")])

    for filename in files:
        file_id = filename.replace(".txt", "")
        LINE_MAP[file_id] = current_line

        filepath = LITERAL_DIR / filename
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                if re.match(r"^\[\d+\]", line.strip()):
                    current_line += 1


def file_id_to_literal_key(volume, chapter, file_id):
    """Convert a contents file_id like '1-1' or '2-1-2' to literal file key like '01-01-01-01'."""
    parts = file_id.split("-")
    vol = volume.zfill(2)
    ch = chapter.zfill(2)

    if len(parts) == 2:
        sec = parts[1].zfill(2)
        return f"{vol}-{ch}-{sec}-01"
    elif len(parts) == 3:
        sec = parts[1].zfill(2)
        sub = parts[2].zfill(2)
        return f"{vol}-{ch}-{sec}-{sub}"

    return None


# -----------------------------------------------------------------------------
# CSS STYLES (PDF-OPTIMIZED)
# -----------------------------------------------------------------------------

CSS_FILE = Path("css/contents.css")
HTML_CSS = Path(CSS_FILE).read_text(encoding="utf-8")

# -----------------------------------------------------------------------------
# PARSER LOGIC
# -----------------------------------------------------------------------------


def parse_contents(content):
    """Parse the contents.md file."""
    data = {"title": "", "work_title": "", "meta": {}, "chapters": []}

    lines = content.split("\n")

    # Extract title (first # heading)
    title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    if title_match:
        data["title"] = title_match.group(1).strip()

    # Extract work title (Tibetan line)
    tibetan_match = re.search(r"\*\*Work\*\*:\s*(.+?)\s*\n", content)
    if tibetan_match:
        data["work_title"] = tibetan_match.group(1).strip()

    # Extract metadata
    for key in ["Author", "Total Chapters", "Total Sections"]:
        match = re.search(rf"\*\*{key}\*\*:\s*(.+?)\s*\n", content)
        print(match)
        if match:
            data["meta"][key] = match.group(1).strip()

    # Find all chapters
    # Pattern: ## Chapter N: Title
    chapter_pattern = re.compile(r"^##\s+Chapter\s+(\d+):\s+(.+)$", re.MULTILINE)

    # Find chapter sections with their tables
    # Pattern: **Volume**: XX | **Pages**: XX-XX | **Sections**: XX | **Total Lines**: ~X

    chapter_matches = list(chapter_pattern.finditer(content))

    for i, match in enumerate(chapter_matches):
        chapter_num = match.group(1)
        chapter_title = match.group(2).strip()

        # Find chapter header info (Volume, Pages, Sections, Lines)
        start_pos = match.end()
        end_pos = chapter_matches[i + 1].start() if i + 1 < len(chapter_matches) else len(content)

        chapter_content = content[start_pos:end_pos]

        # Extract chapter meta
        vol_match = re.search(r"\*\*Volume\*\*:\s*(\d+)", chapter_content)
        pages_match = re.search(r"\*\*Pages\*\*:\s*([\d-]+)", chapter_content)
        sections_match = re.search(r"\*\*Sections\*\*:\s*(\d+)", chapter_content)
        lines_match = re.search(r"\*\*Total Lines\*\*:\s*~?([\d,]+)", chapter_content)

        chapter_data = {
            "number": chapter_num,
            "title": chapter_title,
            "volume": vol_match.group(1) if vol_match else "",
            "pages": pages_match.group(1) if pages_match else "",
            "sections": sections_match.group(1) if sections_match else "",
            "total_lines": lines_match.group(1) if lines_match else "",
            "entries": [],
        }

        # Extract table rows
        # Format: | file | lines | Type | Title |
        table_rows = re.findall(
            r"\|\s*([\d-]+)\s*\|\s*~?(\d+)\s*\|\s*([\w\s/-]+)\s*\|\s*(.+?)\s*\|", chapter_content
        )

        for row in table_rows:
            file_name = row[0].strip()
            lines = row[1].strip()
            content_type = row[2].strip()
            title = row[3].strip()

            chapter_data["entries"].append(
                {"file": file_name, "lines": lines, "type": content_type, "title": title}
            )

        data["chapters"].append(chapter_data)

    return data


def get_type_class(content_type):
    """Return CSS class based on content type."""
    type_lower = content_type.lower().strip()

    if "prologue" in type_lower:
        return "prologue"
    elif "main teaching" in type_lower:
        return "main"
    elif "subsection" in type_lower:
        return "subsection"
    elif "list" in type_lower:
        return "list"
    elif "fragment" in type_lower:
        return "fragment"
    else:
        return "list"


def generate_html(data):
    """Generate HTML content."""
    html_parts = []

    html_parts.append(
        """
    <script src="../js/contents.js"></script>
    """
    )

    html_parts.append(
        f"""
    <div class="title-section">
        <h1>{html.escape(data['title'])}</h1>
        <div class="work-title">{html.escape(data['work_title'])}</div>
        <div class="meta">
    """
    )

    print(data["meta"])

    for key, value in data["meta"].items():
        html_parts.append(f"<div>{key}: {html.escape(value)}</div>")

    html_parts.append(
        """
        </div>
    </div>
    """
    )

    # Overview
    html_parts.append(
        """
    <div class="overview">
        <h2>Overview</h2>
        <ul>
            <li><strong>Descriptive titles</strong> for all 213 sections based on content analysis</li>
            <li><strong>Line counts</strong> for each section (calculated from line markers)</li>
            <li><strong>Click any row</strong> to jump to that section in your currently selected translation layer</li>
            <li><strong>Content type</strong> classification:
                <ul>
                    <li><span class="type-badge type-prologue">Prologue</span> - Introductory/Homage sections</li>
                    <li><span class="type-badge type-main">Main Teaching</span> - Substantive doctrinal content</li>
                    <li><span class="type-badge type-subsection">Subsection</span> - Divisions within main teachings</li>
                    <li><span class="type-badge type-list">List Item</span> - Brief structural markers (often one-line)</li>
                    <li><span class="type-badge type-fragment">Structural Fragment</span> - Incomplete list items or outlines</li>
                </ul>
            </li>
        </ul>
    </div>
    """
    )

    # Chapters
    for chapter in data["chapters"]:
        html_parts.append(
            f"""
        <div class="chapter">
            <div class="chapter-header">
                <h2 class="chapter-title">Chapter {chapter['number']}: {html.escape(chapter['title'])}</h2>
                <div class="chapter-meta">
                    Volume: {chapter['volume']} | 
                    Pages: {chapter['pages']} | 
                    Sections: {chapter['sections']} | 
                    Total Lines: ~{chapter['total_lines']}
                </div>
            </div>
            <table class="section-table">
                <thead>
                    <tr>
                        <th class="col-file">File</th>
                        <th class="col-lines">Lines</th>
                        <th class="col-type">Type</th>
                        <th class="col-title">Title</th>
                    </tr>
                </thead>
                <tbody>
        """
        )

        for entry in chapter["entries"]:
            type_class = get_type_class(entry["type"])
            literal_key = file_id_to_literal_key(
                chapter["volume"], chapter["number"], entry["file"].replace(".md", "")
            )
            start_line = LINE_MAP.get(literal_key, 1)
            html_parts.append(
                f"""
                    <tr data-line="{start_line}" style="cursor: pointer;" title="Click to go to line {start_line}">
                        <td class="col-file">{html.escape(entry['file'])}</td>
                        <td class="col-lines">{html.escape(entry['lines'])}</td>
                        <td class="col-type"><span class="type-badge type-{type_class}">{html.escape(entry['type'])}</span></td>
                        <td class="col-title">{html.escape(entry['title'])}</td>
                    </tr>
            """
            )

        html_parts.append(
            """
                </tbody>
            </table>
        </div>
        """
        )

    return "\n".join(html_parts)


def build_full_document(data):
    """Build complete HTML document."""
    content = generate_html(data)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html.escape(data['title'])}</title>
    <meta name="generator" content="Contents Parser">
    <meta name="created" content="{datetime.now().isoformat()}">
    <link rel="stylesheet" href="../css/contents.css">
</head>
<body>
    <div class="document">
        {content}
    </div>
</body>
</html>
"""


# -----------------------------------------------------------------------------
# MAIN
# -----------------------------------------------------------------------------


def process_contents():
    if not INPUT_FILE.exists():
        print(f"Error: Input file '{INPUT_FILE}' not found.")
        sys.exit(1)

    print("Building line map from literal files...")
    build_line_map()
    print(f"  Mapped {len(LINE_MAP)} files to line numbers")

    try:
        with open(INPUT_FILE, "r", encoding="utf-8") as f:
            content = f.read()

        print("Parsing contents...")
        data = parse_contents(content)

        print(f"  Found {len(data['chapters'])} chapters")

        total_sections = sum(len(ch["entries"]) for ch in data["chapters"])
        print(f"  Found {total_sections} sections")

        full_html = build_full_document(data)

        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(full_html)

        print(f"\n✓ Complete! Output saved to '{OUTPUT_FILE}'")

    except Exception as e:
        print(f"Error: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    process_contents()
