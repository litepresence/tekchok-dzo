#!/usr/bin/env python3
"""
Tibetan Text Parser
Parses all matching files in 'tibetan/' folder and outputs a single 
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

INPUT_DIR = Path("../text/frozen/tibetan")
OUTPUT_FILE = Path("tibetan_proof.html")
FILE_PATTERN = re.compile(r"^\d\d-\d\d-\d\d-\d\d\.txt$")

# Regex to parse lines: [LineNum] Content
LINE_PATTERN = re.compile(r'^\[(\d+)\]\s*(.*)$')

# -----------------------------------------------------------------------------
# CSS STYLES (PDF-OPTIMIZED FOR TIBETAN)
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
        --font-tibetan: 'Jomolhari', 'Tibetan Machine Uni', 'Noto Sans Tibetan', 'Microsoft Himalaya', serif;
        --font-sans: 'Helvetica', 'Arial', sans-serif;
        --color-text: #1a1a1a;
        --color-muted: #666;
        --color-accent: #8b4513;
        --color-line-num: #888;
        --line-height: 1.6;
    }

    * {
        box-sizing: border-box;
    }

    body {
        font-family: var(--font-tibetan);
        color: var(--color-text);
        line-height: var(--line-height);
        font-size: 8pt;
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

    /* Line grid for Tibetan text */
    .line-grid {
        display: grid;
        grid-template-columns: 45px 1fr;
        column-gap: 12px;
        margin: 0;
        padding: 0;
    }

    .line-num {
        grid-column: 1;
        text-align: right;
        font-family: var(--font-sans);
        font-size: 0.7em;
        color: var(--color-line-num);
        padding-top: 3px;
        user-select: none;
        border-right: 1px solid #eee;
        padding-right: 8px;
    }

    .line-content {
        grid-column: 2;
        margin: 0;
        padding: 2px 0;
    }

    /* Tibetan text styling */
    .tibetan-line {
        display: block;
        margin: 0;
        padding: 0;
        font-size: 1em;
        white-space: normal;
        word-wrap: break-word;
        text-align: left;
        direction: ltr;
    }

    /* Tibetan punctuation - subtle highlighting */
    .tibetan-punct {
        color: var(--color-accent);
        font-weight: normal;
    }

    /* Shad marks (། ༎) */
    .shad {
        color: var(--color-accent);
        margin-left: 2px;
    }

    /* Tsheg (་) - keep attached to preceding syllable */
    .tsheg {
        white-space: nowrap;
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
            font-size: 7pt;
        }
        .document {
            max-width: none;
        }
        a {
            text-decoration: none;
            color: inherit;
        }
        .line-num {
            border-right: 1px solid #ccc;
        }
    }
</style>
"""

# -----------------------------------------------------------------------------
# PARSER LOGIC
# -----------------------------------------------------------------------------

def parse_line(raw_line):
    """Parses a single line of the Tibetan text spec."""
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
    Processes Tibetan text content for HTML styling.
    - Escapes HTML
    - Highlights Tibetan punctuation (shad, tsheg, etc.)
    - Preserves all Tibetan Unicode characters
    """
    # Escape HTML first (safe for Tibetan Unicode)
    content = html.escape(content)
    
    # Highlight shad marks (། ༎ ༏) - sentence/verse endings
    content = re.sub(r'([།༎༏])', r'<span class="shad">\1</span>', content)
    
    # Highlight other Tibetan punctuation (྅ ༈ ་ ༌ ། ༎ ༏ ༐ ༑ ༒ ༓ ༔ ༕ ༖ ༗ ༘ ༙ ༚ ༛ ༜ ༝ ༞ ༟)
    # But not tsheg (་) which should stay attached
    tibetan_punct = '྅༌༎༏༐༑༒༓༔༕༖༗༘༙༚༛༜༝༞༟'
    for punct in tibetan_punct:
        content = content.replace(punct, f'<span class="tibetan-punct">{punct}</span>')
    
    return content

def generate_file_html(parsed_lines, filename):
    """Generates HTML content for a single file."""
    html_parts = []
    
    # File separator header
    file_title = filename.replace('.txt', '').replace('-', ' ')
    file_id = filename.replace('.txt', '')
    html_parts.append(f'<div class="file-separator" id="file-{file_id}">{file_title}</div>')
    
    # Open line grid for this file
    html_parts.append('<div class="line-grid">')

    for item in parsed_lines:
        if not item:
            continue

        line_num = item['line_num']
        content = item['content']

        html_parts.append(f'  <div class="line-num">{line_num}</div>')
        html_parts.append(f'  <div class="line-content"><span class="tibetan-line" data-line="{line_num}">{content}</span></div>')

    # Close line grid
    html_parts.append('</div>')

    return "\n".join(html_parts)

def build_full_document(all_file_content, toc_entries):
    """Wraps everything in HTML5 boilerplate with Table of Contents."""
    
    # Build TOC
    toc_html = '<div class="toc"><h1>Tibetan Text Index</h1><ul>'
    for entry in toc_entries:
        toc_html += f'<li><a href="#file-{entry["id"]}">{entry["title"]}</a></li>'
    toc_html += '</ul></div>'

    combined_content = toc_html + "\n" + "\n".join(all_file_content)

    return f"""<!DOCTYPE html>
<html lang="bo">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tibetan Text Collection</title>
    <meta name="generator" content="Tibetan Parser">
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
        print("Please create a folder named 'tibetan' and place your .txt files there.")
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
    total_lines = 0

    for filename in matching_files:
        input_path = INPUT_DIR / filename

        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            parsed_data = [parse_line(line) for line in lines]
            parsed_data = [p for p in parsed_data if p is not None]

            file_html = generate_file_html(parsed_data, filename)
            all_file_content.append(file_html)

            # Count lines for this file
            file_line_count = len(parsed_data)
            total_lines += file_line_count

            # Add to TOC
            file_id = filename.replace('.txt', '')
            file_title = filename.replace('.txt', '').replace('-', ' ')
            toc_entries.append({"id": file_id, "title": file_title})

            print(f"  ✓ Processed: {filename} ({file_line_count} lines)")

        except Exception as e:
            print(f"  ✗ Error processing {filename}: {e}")

    # Build Final Document
    full_html = build_full_document(all_file_content, toc_entries)

    # Write Output
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(full_html)

    print(f"\n✓ Complete! Output saved to '{OUTPUT_FILE}'")
    print(f"  Total files combined: {len(matching_files)}")
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
