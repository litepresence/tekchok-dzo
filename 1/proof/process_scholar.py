#!/usr/bin/env python3
"""
Scholarly Analysis Parser
Parses all matching files in 'scholar/' folder and outputs a single 
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

INPUT_DIR = Path("../text/dynamic/scholar")
OUTPUT_FILE = Path("html/scholar_proof.html")
FILE_PATTERN = re.compile(r"^\d\d-\d\d-\d\d-\d\d\.txt$")

LINE_RANGE_PATTERN = re.compile(r'^\[(\d+-\d+)\]')
TAG_PATTERN = re.compile(r'^<(\w+)>(.*)$')
HEADING_PATTERN = re.compile(r'^#\s+(.+)$')
SEPARATOR_PATTERN = re.compile(r'^---+$')

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
        --color-text: #1a1a1a;
        --color-muted: #666;
        --color-structure: #2c5f7f;
        --color-philology: #8b4513;
        --color-context: #2e7d32;
        --color-concept: #6a1b9a;
        --color-line-range: #888;
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
        background-color: #fff;
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
    }

    .document {
        max-width: 5.5in;
        margin: 0 auto;
        padding: 0;
    }

    /* File separators */
    .file-separator {
        margin-top: 2em;
        margin-bottom: 1em;
        padding-top: 1em;
        border-top: 1px solid #ddd;
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

    /* Entry block for each scholarly unit */
    .entry-block {
        margin: 1.5em 0;
        padding: 0.75em;
        background-color: #fafafa;
        border-left: 4px solid var(--color-muted);
        page-break-inside: avoid;
    }

    .entry-block.tag-structure {
        border-left-color: var(--color-structure);
    }

    .entry-block.tag-philology {
        border-left-color: var(--color-philology);
    }

    .entry-block.tag-context {
        border-left-color: var(--color-context);
    }

    .entry-block.tag-concept {
        border-left-color: var(--color-concept);
    }

    /* Line range display */
    .line-range {
        font-family: var(--font-sans);
        font-size: 0.75em;
        color: var(--color-line-range);
        margin-bottom: 0.5em;
        font-weight: bold;
    }

    /* Metadata tags */
    .metadata {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5em;
        margin-bottom: 0.75em;
        font-family: var(--font-sans);
        font-size: 0.7em;
    }

    .tag {
        padding: 2px 8px;
        border-radius: 3px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .tag-structure {
        background-color: #e3f2fd;
        color: var(--color-structure);
        border: 1px solid #bbdefb;
    }

    .tag-philology {
        background-color: #f5ebe0;
        color: var(--color-philology);
        border: 1px solid #e8d5c0;
    }

    .tag-context {
        background-color: #e8f5e9;
        color: var(--color-context);
        border: 1px solid #c8e6c9;
    }

    .tag-concept {
        background-color: #f3e5f5;
        color: var(--color-concept);
        border: 1px solid #e1bee7;
    }

    /* Section headings within entries */
    .section-heading {
        font-family: var(--font-sans);
        font-size: 0.85em;
        font-weight: 600;
        margin-top: 1em;
        margin-bottom: 0.25em;
        color: var(--color-text);
    }

    .section-heading:first-child {
        margin-top: 0;
    }

    /* Analysis content */
    .analysis-content {
        font-size: 0.95em;
        text-align: justify;
        hyphens: auto;
        -webkit-hyphens: auto;
        line-height: 1.6;
    }

    .analysis-header {
        font-weight: 700;
        color: var(--color-structure);
        display: block;
        margin-top: 0.75em;
        margin-bottom: 0.25em;
    }

    .analysis-content p {
        margin: 0.5em 0;
    }

    .analysis-content ul,
    .analysis-content ol {
        margin: 0.5em 0;
        padding-left: 1.5em;
    }

    .analysis-content li {
        margin: 0.25em 0;
    }

    /* Horizontal separators within entries */
    .section-separator {
        margin: 1em 0;
        border: none;
        border-top: 1px dashed #ccc;
    }

    /* Tibetan text within analysis */
    .tibetan-inline {
        font-family: 'Jomolhari', 'Noto Sans Tibetan', serif;
        font-size: 0.9em;
        color: var(--color-muted);
        font-style: italic;
    }

    /* Table of Contents */
    .toc {
        margin-bottom: 3em;
        page-break-after: always;
    }
    .toc h1 {
        text-align: center;
        font-variant: small-caps;
        margin-bottom: 1.5em;
        color: var(--color-muted);
        font-family: var(--font-sans);
    }
    .toc ul {
        list-style: none;
        padding-left: 0;
    }
    .toc li {
        margin-bottom: 0.5em;
        color: var(--color-text);
        font-family: var(--font-sans);
    }
    .toc a {
        text-decoration: none;
        color: inherit;
    }
    .toc a:hover {
        color: var(--color-structure);
    }

    /* Print-specific adjustments */
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
        
        # Process content - handle **Analysis:** and other bold markers
        content_text = " ".join(section["content"])
        
        # Convert **Analysis:** to styled headers
        content_text = re.sub(r'\*\*Analysis:\*\*', '<span class="analysis-header">Analysis:</span>', content_text)
        content_text = re.sub(r'\*\*Section Placement:\*\*', '<span class="analysis-header">Section Placement:</span>', content_text)
        content_text = re.sub(r'\*\*Connection to Following Sections:\*\*', '<span class="analysis-header">Connection to Following Sections:</span>', content_text)
        content_text = re.sub(r'\*\*Terminological Precision:\*\*', '<span class="analysis-header">Terminological Precision:</span>', content_text)
        content_text = re.sub(r'\*\*Key Terms:\*\*', '<span class="analysis-header">Key Terms:</span>', content_text)
        
        # Convert bold markers to HTML
        content_text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', content_text)
        
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

def generate_file_html(entries, filename):
    """Generates HTML content for a single file."""
    html_parts = []

    # File separator header
    file_title = filename.replace('.txt', '').replace('-', ' ')
    file_id = filename.replace('.txt', '')
    html_parts.append(f'<div class="file-separator" id="file-{file_id}">{file_title}</div>')

    for entry in entries:
        if not entry["line_range"]:
            continue

        tag_class = f"tag-{entry['tag']}" if entry['tag'] else ""
        html_parts.append(f'<div class="entry-block {tag_class}">')

        # Line range
        html_parts.append(f'  <div class="line-range">[{entry["line_range"]}]</div>')

        # Metadata tag
        if entry["tag"]:
            html_parts.append(f'  <div class="metadata">')
            html_parts.append(f'    <span class="tag tag-{entry["tag"]}">{entry["tag"].title()}</span>')
            html_parts.append(f'  </div>')

        # Content
        if entry["full_content"]:
            html_parts.append(f'  {entry["full_content"]}')

        html_parts.append('</div>')

    return "\n".join(html_parts)

def build_full_document(all_file_content, toc_entries):
    """Wraps everything in HTML5 boilerplate with Table of Contents."""

    # Build TOC
    toc_html = '<div class="toc"><h1>Scholarly Analysis Index</h1><ul>'
    for entry in toc_entries:
        toc_html += f'<li><a href="#file-{entry["id"]}">{entry["title"]}</a></li>'
    toc_html += '</ul></div>'

    combined_content = toc_html + "\n" + "\n".join(all_file_content)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Scholarly Analysis Collection</title>
    <meta name="generator" content="Scholar Parser">
    <meta name="created" content="{datetime.now().isoformat()}">
    {HTML_CSS}
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
        print("Please create a folder named 'scholar' and place your .txt files there.")
        sys.exit(1)

    # Find Matching Files
    all_files = os.listdir(INPUT_DIR)
    matching_files = sorted([f for f in all_files if FILE_PATTERN.match(f)])

    if not matching_files:
        print(f"No files matching pattern '{FILE_PATTERN.pattern}' found in '{INPUT_DIR}'.")
        sys.exit(0)

    print(f"Found {len(matching_files)} file(s) to process.")

    # Process Each File
    all_file_content = []
    toc_entries = []
    total_entries = 0

    for filename in matching_files:
        input_path = INPUT_DIR / filename

        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Split content into entries
            raw_entries = split_into_entries(content)

            # Parse each entry
            entries = [parse_entry(e.splitlines()) for e in raw_entries]
            entries = [e for e in entries if e["line_range"]]

            file_html = generate_file_html(entries, filename)
            all_file_content.append(file_html)

            # Count entries
            file_entry_count = len(entries)
            total_entries += file_entry_count

            # Add to TOC
            file_id = filename.replace('.txt', '')
            file_title = filename.replace('.txt', '').replace('-', ' ')
            toc_entries.append({"id": file_id, "title": file_title})

            print(f"  ✓ Processed: {filename} ({file_entry_count} entries)")

        except Exception as e:
            print(f"  ✗ Error processing {filename}: {e}")
            import traceback
            traceback.print_exc()

    # Build Final Document
    full_html = build_full_document(all_file_content, toc_entries)

    # Write Output
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(full_html)

    print(f"\n✓ Complete! Output saved to '{OUTPUT_FILE}'")
    print(f"  Total files combined: {len(matching_files)}")
    print(f"  Total entries processed: {total_entries}")
    print(f"\nTo create PDF:")
    print(f"  1. Open '{OUTPUT_FILE}' in Chrome or Edge")
    print(f"  2. Press Ctrl+P (Print)")
    print(f"  3. Select 'Save as PDF'")
    print(f"  4. Ensure 'Background graphics' is checked")
    print(f"  5. Set margins to 'Default' or 'Minimum'")
    print(f"  6. Click Save")

if __name__ == "__main__":
    process_folder()
