#!/usr/bin/env python3
"""
Epistemic Layer Parser
Parses all matching files in 'epistemic/' folder and outputs a single 
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

INPUT_DIR = Path("../text/frozen/epistemic")
OUTPUT_FILE = Path("epistemic_proof.html")
FILE_PATTERN = re.compile(r"^\d\d-\d\d-\d\d-\d\d\.txt$")

# Regex patterns
LINE_RANGE_PATTERN = re.compile(r'^\[(\d+-\d+)\]')
TAG_PATTERN = re.compile(r'^<(\w+)>(.*)$')

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
        --color-view: #2c5f7f;
        --color-pedagogy: #8b4513;
        --color-risk: #8b0000;
        --color-classification: #333;
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

    /* Entry block for each epistemic unit */
    .entry-block {
        margin: 1.5em 0;
        padding: 0.75em;
        background-color: #fafafa;
        border-left: 3px solid var(--color-muted);
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
        padding: 2px 6px;
        border-radius: 3px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .tag-view {
        background-color: #e8f4f8;
        color: var(--color-view);
        border: 1px solid #c5dce8;
    }

    .tag-pedagogy {
        background-color: #f5ebe0;
        color: var(--color-pedagogy);
        border: 1px solid #e8d5c0;
    }

    .tag-risk {
        background-color: #f8e8e8;
        color: var(--color-risk);
        border: 1px solid #e8c5c5;
    }

    /* Classification content */
    .classification {
        font-size: 0.95em;
        text-align: justify;
        hyphens: auto;
        -webkit-hyphens: auto;
        line-height: 1.6;
    }

    /* Tibetan text within classification */
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
        color: var(--color-view);
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
    Parses a single epistemic entry (line range + metadata + classification).
    Handles classification content on same line OR subsequent lines.
    Returns a dict with line_range, view, pedagogy, risk, classification.
    """
    entry = {
        "line_range": None,
        "view": None,
        "pedagogy": None,
        "risk": None,
        "classification": []
    }

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
    tibetan_pattern = re.compile(r'([\u0F00-\u0FFF]+)')
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

        html_parts.append('<div class="entry-block">')

        # Line range
        html_parts.append(f'  <div class="line-range">[{entry["line_range"]}]</div>')

        # Metadata tags
        html_parts.append('  <div class="metadata">')

        if entry["view"]:
            html_parts.append(f'    <span class="tag tag-view">View: {html.escape(entry["view"])}</span>')

        if entry["pedagogy"]:
            html_parts.append(f'    <span class="tag tag-pedagogy">Pedagogy: {html.escape(entry["pedagogy"])}</span>')

        if entry["risk"]:
            html_parts.append(f'    <span class="tag tag-risk">Risk: {html.escape(entry["risk"])}</span>')

        html_parts.append('  </div>')

        # Classification content
        if entry["classification_text"]:
            html_parts.append(f'  <div class="classification">{entry["classification_text"]}</div>')

        html_parts.append('</div>')

    return "\n".join(html_parts)

def build_full_document(all_file_content, toc_entries):
    """Wraps everything in HTML5 boilerplate with Table of Contents."""

    # Build TOC
    toc_html = '<div class="toc"><h1>Epistemic Layer Index</h1><ul>'
    for entry in toc_entries:
        toc_html += f'<li><a href="#file-{entry["id"]}">{entry["title"]}</a></li>'
    toc_html += '</ul></div>'

    combined_content = toc_html + "\n" + "\n".join(all_file_content)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Epistemic Layer Collection</title>
    <meta name="generator" content="Epistemic Parser">
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
        print("Please create a folder named 'epistemic' and place your .txt files there.")
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

            # Split content into entries using robust splitter
            raw_entries = split_into_entries(content)

            # Parse each entry
            entries = [parse_entry(e.splitlines()) for e in raw_entries]
            entries = [e for e in entries if e["line_range"]]

            file_html = generate_file_html(entries, filename)
            all_file_content.append(file_html)

            # Count entries for this file
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
