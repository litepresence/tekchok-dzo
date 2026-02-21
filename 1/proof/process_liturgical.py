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

import os
import re
import html
import sys
from pathlib import Path
from datetime import datetime

# -----------------------------------------------------------------------------
# CONFIGURATION
# -----------------------------------------------------------------------------

INPUT_DIR = Path("../text/frozen/liturgical")
OUTPUT_FILE = Path("html/liturgical_proof.html")
FILE_PATTERN = re.compile(r"^\d\d-\d\d-\d\d-\d\d\.txt$")

# Regex to parse lines: [LineNum] [<break>] <Tag> Content
LINE_PATTERN = re.compile(r'^\[(\d+)\]\s*(?:(<break>)\s*)?<(\w+)>\s*(.*)$')

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
        --color-text: #1a1a1a;
        --color-muted: #666;
        --color-accent: #8b4513;
        --color-mantra: #8b0000;
        --line-height: 1.3; /* Reduced from 1.5 */
    }

    * {
        box-sizing: border-box;
    }

    body {
        font-family: var(--font-main);
        color: var(--color-text);
        line-height: var(--line-height);
        font-size: 11pt;
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

    /* File separators for organization */
    .file-separator {
        margin-top: 2em; /* Reduced from 3em */
        margin-bottom: 1em; /* Reduced from 1.5em */
        padding-top: 1em;
        border-top: 1px solid #ddd;
        text-align: center;
        font-variant: small-caps;
        color: var(--color-muted);
        font-size: 0.9em;
        letter-spacing: 2px;
    }

    /* --- TAG SPECIFIC STYLING --- */

    .prose {
        display: block;
        margin-top: 0;
        margin-bottom: 0.5em; /* Added space between paragraphs */
        text-align: justify;
        hyphens: auto;
        -webkit-hyphens: auto;
    }
    
    .prose.break-before {
        margin-top: 1em;
        text-indent: 1.5em;
    }

    .verse {
        display: block;
        text-align: center;
        font-style: italic;
        margin: 0.4em 0; /* Reduced from 1em */
        color: #333;
        page-break-inside: avoid;
    }

    .tantra {
        display: block;
        margin: 0.2em 0; /* Reduced from 0.5em */
        padding-left: 1.5em;
        border-left: 2px solid var(--color-accent);
        color: #4a3728;
        font-style: italic;
        page-break-inside: avoid;
    }

    .ornament {
        display: block;
        text-align: center;
        font-variant: small-caps;
        font-weight: bold;
        color: var(--color-accent);
        margin: 1.5em 0 0.8em 0; /* Reduced */
        letter-spacing: 1.5px;
        font-size: 1.05em;
        page-break-after: avoid;
    }

    .mantra {
        display: inline-block;
        font-weight: bold;
        color: var(--color-mantra);
        font-family: var(--font-sans);
        letter-spacing: 0.5px;
    }

    .list {
        display: list-item;
        list-style-type: disc;
        margin-left: 1.5em;
        margin-top: 0.1em; /* Reduced */
        margin-bottom: 0.1em; /* Reduced */
    }

    .verse-marker {
        font-size: 0.75em;
        vertical-align: super;
        color: var(--color-muted);
        margin-left: 4px;
        font-family: var(--font-sans);
    }

    /* Table of Contents */
    .toc {
        margin-bottom: 2em; /* Reduced */
        page-break-after: always;
    }
    .toc h1 {
        text-align: center;
        font-variant: small-caps;
        margin-bottom: 1em; /* Reduced */
    }
    .toc ul {
        list-style: none;
        padding-left: 0;
    }
    .toc li {
        margin-bottom: 0.3em; /* Reduced */
        color: var(--color-accent);
    }
    .toc a {
        text-decoration: none;
        color: inherit;
    }

    /* Print-specific adjustments */
    @media print {
        body {
            font-size: 10.5pt;
        }
        .document {
            max-width: none;
        }
        a {
            text-decoration: none;
            color: inherit;
        }
        .file-separator {
            border-top: 1px solid #999;
        }
    }
</style>
"""

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
        "content": html.escape(content)
    }

def generate_file_html(parsed_lines, filename):
    """Generates HTML content for a single file.
    
    Updates: Groups consecutive lines with the same tag and no break 
    into single HTML elements. Prose joins with spaces; others join with <br>.
    """
    html_parts = []
    
    # File separator header
    file_title = filename.replace('.txt', '').replace('-', ' ')
    html_parts.append(f'<div class="file-separator" id="file-{filename.replace(".txt", "")}">{file_title}</div>')

    # --- Grouping Logic for Consecutive Tags ---
    groups = []
    current_group = None

    for item in parsed_lines:
        if not item:
            continue

        can_merge = False
        if current_group:
            # Merge if same tag, and neither the existing group nor the new item 
            # forces a break (paragraph start)
            if (item['tag'] == current_group['tag'] and 
                not current_group['is_break'] and 
                not item['is_break']):
                can_merge = True

        if can_merge:
            # Append content based on tag type
            if item['tag'] == 'prose':
                # Prose flows naturally with spaces
                current_group['content'] += " " + item['content']
            else:
                # Other tags (verse, tantra, etc.) maintain visual line breaks
                current_group['content'] += "<br>" + item['content']
        else:
            # Save previous group and start new one
            if current_group:
                groups.append(current_group)
            current_group = item.copy()

    # Don't forget the last group
    if current_group:
        groups.append(current_group)
    # -------------------------------------------

    for item in groups:
        tag = item['tag']
        content = item['content']
        is_break = item['is_break']

        classes = [tag]
        if is_break:
            classes.append('break-before')
        
        class_str = " ".join(classes)

        if tag == 'mantra':
            content_html = f'<span class="mantra">{content}</span>'
        else:
            content_html = content

        # Highlight verse markers
        content_html = re.sub(r'\|\|\s*(\d+)\s*\|\|', r'<span class="verse-marker">|| \1 ||</span>', content_html)

        html_parts.append(f'<div class="{class_str}" data-line="{item["line_num"]}">{content_html}</div>')

    return "\n".join(html_parts)

def build_full_document(all_file_content, toc_entries):
    """Wraps everything in HTML5 boilerplate with Table of Contents."""
    
    # Build TOC
    toc_html = '<div class="toc"><h1>Table of Contents</h1><ul>'
    for entry in toc_entries:
        toc_html += f'<li><a href="#file-{entry["id"]}">{entry["title"]}</a></li>'
    toc_html += '</ul></div>'

    combined_content = toc_html + "\n".join(all_file_content)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Liturgical Text Collection</title>
    <meta name="generator" content="Liturgical Parser">
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
        print("Please create a folder named 'liturgical' and place your .txt files there.")
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

    for filename in matching_files:
        input_path = INPUT_DIR / filename

        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            parsed_data = [parse_line(line) for line in lines]
            parsed_data = [p for p in parsed_data if p is not None]

            file_html = generate_file_html(parsed_data, filename)
            all_file_content.append(file_html)

            # Add to TOC
            file_id = filename.replace('.txt', '')
            file_title = filename.replace('.txt', '').replace('-', ' ')
            toc_entries.append({"id": file_id, "title": file_title})

            print(f"  ✓ Processed: {filename}")

        except Exception as e:
            print(f"  ✗ Error processing {filename}: {e}")

    # Build Final Document
    full_html = build_full_document(all_file_content, toc_entries)

    # Write Output
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(full_html)

    print(f"\n✓ Complete! Output saved to '{OUTPUT_FILE}'")
    print(f"  Total files combined: {len(matching_files)}")
    print(f"\nTo create PDF:")
    print(f"  1. Open '{OUTPUT_FILE}' in Chrome or Edge")
    print(f"  2. Press Ctrl+P (Print)")
    print(f"  3. Select 'Save as PDF'")
    print(f"  4. Ensure 'Background graphics' is checked")
    print(f"  5. Click Save")

if __name__ == "__main__":
    process_folder()
