#!/usr/bin/env python3
"""
Commentary Layer Parser
Parses all matching files in 'commentary/' folder and outputs a single 
combined HTML file optimized for PDF rendering.

This layer contains poetic philosophical prose with line ranges only.
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

INPUT_DIR = Path("../text/dynamic/commentary")
OUTPUT_FILE = Path("html/commentary_proof.html")
FILE_PATTERN = re.compile(r"^\d\d-\d\d-\d\d-\d\d\.txt$")

LINE_RANGE_PATTERN = re.compile(r'^\[(\d+-\d+)\]')

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
        --color-accent: #6a4c93;
        --color-line-range: #888;
        --line-height: 1.6;
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
        color: var(--color-accent);
        font-size: 0.95em;
        letter-spacing: 2px;
        font-family: var(--font-sans);
    }
    .file-separator:first-child {
        margin-top: 0;
    }

    /* Entry block for each commentary unit */
    .entry-block {
        margin: 1.5em 0;
        padding: 0.5em 0;
        page-break-inside: avoid;
    }

    /* Line range display */
    .line-range {
        font-family: var(--font-sans);
        font-size: 0.7em;
        color: var(--color-line-range);
        margin-bottom: 0.5em;
        font-weight: bold;
        letter-spacing: 1px;
    }

    /* Commentary prose content */
    .commentary-content {
        font-size: 1em;
        text-align: left;
        line-height: 1.7;
        color: var(--color-text);
        font-style: italic;
    }

    /* Emphasized phrases */
    .emphasis {
        font-weight: 600;
        color: var(--color-accent);
    }

    /* Technical terms */
    .term {
        font-style: italic;
        color: var(--color-muted);
    }

    /* Key philosophical terms */
    .key-term {
        font-style: italic;
        border-bottom: 1px dotted var(--color-accent);
    }

    /* Tibetan text */
    .tibetan-inline {
        font-family: 'Jomolhari', 'Noto Sans Tibetan', serif;
        font-size: 0.9em;
        color: var(--color-muted);
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
        color: var(--color-accent);
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
        color: var(--color-accent);
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
    }
</style>
"""

# -----------------------------------------------------------------------------
# PARSER LOGIC
# -----------------------------------------------------------------------------

def parse_entry(lines):
    """
    Parses a single commentary entry (line range + prose content).
    """
    entry = {
        "line_range": None,
        "content": []
    }

    in_content = False

    for line in lines:
        line_stripped = line.strip()
        if not line_stripped:
            continue

        # Check for line range (starts new entry)
        range_match = LINE_RANGE_PATTERN.match(line_stripped)
        if range_match:
            entry["line_range"] = range_match.group(1)
            in_content = True
            continue

        # Content line
        if in_content:
            entry["content"].append(line_stripped)

    # Join and process content
    entry["content_text"] = " ".join(entry["content"])
    
    # Highlight Tibetan text
    entry["content_text"] = highlight_tibetan(entry["content_text"])
    
    # Process key terms (italicize words in parentheses)
    entry["content_text"] = re.sub(r'\(([^)]+)\)', r'<span class="term">(\1)</span>', entry["content_text"])
    
    return entry

def highlight_tibetan(text):
    """Wraps Tibetan text segments in span for styling."""
    tibetan_pattern = re.compile(r'([\u0F00-\u0FFF]+)')
    return tibetan_pattern.sub(r'<span class="tibetan-inline">\1</span>', text)

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

        # Content
        if entry["content_text"]:
            html_parts.append(f'  <div class="commentary-content">{html.escape(entry["content_text"])}</div>')

        html_parts.append('</div>')

    return "\n".join(html_parts)

def build_full_document(all_file_content, toc_entries):
    """Wraps everything in HTML5 boilerplate with Table of Contents."""

    # Build TOC
    toc_html = '<div class="toc"><h1>Commentary Index</h1><ul>'
    for entry in toc_entries:
        toc_html += f'<li><a href="#file-{entry["id"]}">{entry["title"]}</a></li>'
    toc_html += '</ul></div>'

    combined_content = toc_html + "\n" + "\n".join(all_file_content)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Commentary Collection</title>
    <meta name="generator" content="Commentary Parser">
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
        print("Please create a folder named 'commentary' and place your .txt files there.")
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
