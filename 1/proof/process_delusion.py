#!/usr/bin/env python3
"""
Delusion Analysis Parser
Parses all matching files in 'delusion/' folder and outputs a single 
combined HTML file optimized for PDF rendering.

This layer analyzes common misinterpretations and their consequences.
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

INPUT_DIR = Path("../text/dynamic/delusion")
OUTPUT_FILE = Path("html/delusion_proof.html")
FILE_PATTERN = re.compile(r"^\d\d-\d\d-\d\d-\d\d\.txt$")

LINE_RANGE_PATTERN = re.compile(r'^\[(\d+-\d+)\]')
TAG_PATTERN = re.compile(r'^<([^>]+)>')

SECTION_HEADERS = {
    "misreading": "Misreading",
    "why_it_arises": "Why it arises",
    "primary_consequence": "Primary consequence",
    "secondary_consequences": "Secondary consequences",
    "cascade_effects": "Cascade effects"
}

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
        --color-error: #c62828;
        --color-warning: #f57c00;
        --color-consequence: #ef6c00;
        --color-cascade: #8e24aa;
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

    /* Entry block for each delusion analysis */
    .entry-block {
        margin: 1.5em 0;
        padding: 0.75em;
        background-color: #fffbf0;
        border-left: 4px solid var(--color-error);
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

    /* Error tags */
    .error-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 0.4em;
        margin-bottom: 0.75em;
    }

    .error-tag {
        padding: 2px 8px;
        border-radius: 3px;
        font-weight: 600;
        font-size: 0.7em;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        font-family: var(--font-sans);
    }

    /* Error tag color variations */
    .error-tag.ontological { background-color: #ffebee; color: #c62828; border: 1px solid #ffcdd2; }
    .error-tag.reification { background-color: #fce4ec; color: #ad1457; border: 1px solid #f8bbd0; }
    .error-tag.temporal { background-color: #fff3e0; color: #e65100; border: 1px solid #ffe0b2; }
    .error-tag.primordial { background-color: #fbe9e7; color: #bf360c; border: 1px solid #ffccbc; }
    .error-tag.hierarchical { background-color: #e8eaf6; color: #283593; border: 1px solid #c5cae9; }
    .error-tag.meditationism { background-color: #e0f2f1; color: #00695c; border: 1px solid #b2dfdb; }
    .error-tag.nostalgia { background-color: #f1f8e9; color: #558b2f; border: 1px solid #dcedc8; }
    .error-tag.acquisition { background-color: #e8f5e9; color: #2e7d32; border: 1px solid #c8e6c9; }
    .error-tag.default {
        background-color: #f5f5f5;
        color: var(--color-error);
        border: 1px solid #e0e0e0;
    }

    /* Section headers */
    .section-header {
        font-family: var(--font-sans);
        font-size: 0.8em;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-top: 0.75em;
        margin-bottom: 0.25em;
    }

    .section-header.misreading {
        color: var(--color-error);
    }

    .section-header.why-it-arises {
        color: var(--color-warning);
    }

    .section-header.primary-consequence {
        color: var(--color-consequence);
    }

    .section-header.secondary-consequences {
        color: #f9a825;
    }

    .section-header.cascade_effects {
        color: var(--color-cascade);
    }

    /* Section content */
    .section-content {
        font-size: 0.9em;
        line-height: 1.5;
        text-align: justify;
        hyphens: auto;
        -webkit-hyphens: auto;
    }

    /* Cascade arrow styling */
    .cascade-chain {
        font-family: var(--font-mono);
        font-size: 0.8em;
        color: var(--color-cascade);
        background-color: #f3e5f5;
        padding: 0.25em 0.5em;
        border-radius: 3px;
        display: inline-block;
        margin: 0.25em 0;
    }

    /* Cascade arrows within content */
    .cascade-arrow {
        color: var(--color-cascade);
        font-weight: bold;
        margin: 0 0.25em;
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
        color: var(--color-error);
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
        color: var(--color-error);
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

def get_error_tag_class(tag):
    """Returns CSS class based on error tag type."""
    tag_lower = tag.lower()
    
    if "ontological" in tag_lower:
        return "ontological"
    elif "reification" in tag_lower:
        return "reification"
    elif "temporal" in tag_lower:
        return "temporal"
    elif "primordial" in tag_lower:
        return "primordial"
    elif "hierarchical" in tag_lower:
        return "hierarchical"
    elif "meditationism" in tag_lower:
        return "meditationism"
    elif "nostalgia" in tag_lower:
        return "nostalgia"
    elif "acquisition" in tag_lower:
        return "acquisition"
    else:
        return "default"

def parse_entry(lines):
    """
    Parses a single delusion entry with error tags and consequence sections.
    """
    entry = {
        "line_range": None,
        "error_tags": [],
        "sections": {}
    }

    current_section = None
    current_content = []

    for line in lines:
        line_stripped = line.strip()
        if not line_stripped:
            continue

        # Check for line range (starts new entry)
        range_match = LINE_RANGE_PATTERN.match(line_stripped)
        if range_match:
            entry["line_range"] = range_match.group(1)
            current_section = None
            current_content = []
            continue

        # Check for error tags
        tag_match = TAG_PATTERN.match(line_stripped)
        if tag_match:
            # Save previous section
            if current_section and current_content:
                entry["sections"][current_section] = " ".join(current_content)
            
            tag = tag_match.group(1)
            entry["error_tags"].append(tag)
            current_section = None
            current_content = []
            continue

        # Check for section headers (**Section:**) - use exact match to avoid partial matches
        section_key = None
        for key, title in SECTION_HEADERS.items():
            # Match exactly **Title:** with nothing else after
            if line_stripped == f"**{title}:**":
                section_key = key
                break
        
        if section_key:
            # Save previous section
            if current_section and current_content:
                entry["sections"][current_section] = " ".join(current_content)
            
            current_section = section_key
            current_content = []  # Start fresh
            continue

        # Check for cascade arrow patterns (within cascade section)
        if current_section == "cascade_effects":
            # Handle arrow chains - transform all <tag> → patterns
            # Match tags with or without spaces, hyphens
            line_stripped = re.sub(
                r'<([^>]+)>\s*→',
                r'<span class="cascade-arrow">→</span><span class="error-tag cascade">\1</span>',
                line_stripped
            )
            current_content.append(line_stripped)
        elif current_section:
            current_content.append(line_stripped)
        elif not entry["error_tags"]:
            # Content without section header goes to "content"
            if current_content or line_stripped:
                current_content.append(line_stripped)

    # Don't forget last section
    if current_section and current_content:
        entry["sections"][current_section] = " ".join(current_content)
    elif current_content:
        entry["sections"]["content"] = " ".join(current_content)

    # Build HTML for sections
    entry["sections_html"] = build_sections_html(entry)

    return entry

def build_sections_html(entry):
    """Builds HTML for entry sections."""
    html_parts = []
    
    for section_key, title in SECTION_HEADERS.items():
        if section_key in entry["sections"]:
            content = entry["sections"][section_key]
            
            # Skip empty sections
            if not content.strip():
                continue
            
            # Process cascade arrows for cascade effects
            if section_key == "cascade_effects":
                # Don't escape - already contains HTML spans from parsing
                html_parts.append(f'<div class="section-header {section_key}">{title}</div>')
                html_parts.append(f'<div class="section-content">{content}</div>')
            else:
                html_parts.append(f'<div class="section-header {section_key}">{title}</div>')
                html_parts.append(f'<div class="section-content">{html.escape(content)}</div>')
    
    # Add any untagged content
    if "content" in entry["sections"] and "misreading" not in entry["sections"]:
        html_parts.append(f'<div class="section-content">{html.escape(entry["sections"]["content"])}</div>')
    
    return "\n".join(html_parts)

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

        # Error tags
        if entry["error_tags"]:
            html_parts.append('  <div class="error-tags">')
            for tag in entry["error_tags"]:
                tag_class = get_error_tag_class(tag)
                html_parts.append(f'    <span class="error-tag {tag_class}">{tag}</span>')
            html_parts.append('  </div>')

        # Sections
        if entry["sections_html"]:
            html_parts.append(f'  {entry["sections_html"]}')

        html_parts.append('</div>')

    return "\n".join(html_parts)

def build_full_document(all_file_content, toc_entries):
    """Wraps everything in HTML5 boilerplate with Table of Contents."""

    # Build TOC
    toc_html = '<div class="toc"><h1>Delusion Analysis Index</h1><ul>'
    for entry in toc_entries:
        toc_html += f'<li><a href="#file-{entry["id"]}">{entry["title"]}</a></li>'
    toc_html += '</ul></div>'

    combined_content = toc_html + "\n" + "\n".join(all_file_content)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Delusion Analysis Collection</title>
    <meta name="generator" content="Delusion Parser">
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
        print("Please create a folder named 'delusion' and place your .txt files there.")
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
