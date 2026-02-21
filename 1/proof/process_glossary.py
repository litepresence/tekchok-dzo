#!/usr/bin/env python3
"""
Glossary Parser
Parses glossary.md and outputs a single combined HTML file optimized for PDF rendering.
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

INPUT_FILE = Path("../text/glossary.md")
OUTPUT_FILE = Path("html/glossary_proof.html")

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
        --color-accent: #5d4037;
        --color-header: #3e2723;
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

    /* Title */
    .title-section {
        text-align: center;
        margin-bottom: 3em;
        padding-bottom: 2em;
        border-bottom: 2px solid var(--color-accent);
    }

    .title-section h1 {
        font-size: 1.5em;
        color: var(--color-header);
        margin-bottom: 0.5em;
        font-variant: small-caps;
        letter-spacing: 2px;
    }

    .title-section .subtitle {
        font-style: italic;
        color: var(--color-muted);
        font-size: 1.1em;
    }

    .title-section .description {
        margin-top: 1.5em;
        font-size: 0.9em;
        text-align: left;
        text-indent: 2em;
        color: var(--color-text);
    }

    /* Glossary intro */
    .glossary-intro {
        margin-bottom: 2em;
        font-size: 0.9em;
        color: var(--color-muted);
        font-style: italic;
    }

    /* Glossary entries */
    .glossary-letter {
        margin-top: 2em;
        margin-bottom: 1em;
        padding-bottom: 0.5em;
        border-bottom: 1px solid var(--color-accent);
    }

    .glossary-letter h2 {
        font-size: 1.2em;
        color: var(--color-header);
        font-variant: small-caps;
        letter-spacing: 3px;
        margin: 0;
    }

    .glossary-entry {
        margin-bottom: 1.5em;
        padding: 0.75em;
        page-break-inside: avoid;
    }

    .term {
        font-weight: 700;
        color: var(--color-header);
        font-size: 1.05em;
    }

    .tibetan {
        font-family: 'Jomolhari', 'Noto Sans Tibetan', serif;
        color: var(--color-muted);
        font-style: italic;
    }

    .sanskrit {
        font-style: italic;
        color: var(--color-muted);
    }

    .definition {
        margin-top: 0.5em;
        text-align: justify;
        hyphens: auto;
        -webkit-hyphens: auto;
        line-height: 1.6;
    }

    .first-appearance {
        margin-top: 0.5em;
        font-size: 0.8em;
        color: var(--color-muted);
        font-family: var(--font-sans);
    }

    .first-appearance .location {
        font-family: var(--font-mono);
        color: var(--color-accent);
    }

    /* Two-column layout for definitions */
    @media screen {
        .glossary-entry {
            display: inline-block;
            width: 45%;
            margin-right: 4%;
            vertical-align: top;
        }
    }

    /* Print-specific adjustments */
    @media print {
        body {
            font-size: 9pt;
        }
        .document {
            max-width: none;
        }
        .glossary-entry {
            display: block;
            width: 100%;
            margin-right: 0;
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

def parse_glossary(content):
    """
    Parses the glossary markdown content.
    Extracts title, description, and glossary entries from table.
    """
    entries = []
    
    # Extract title and subtitle
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else "Glossary"
    
    subtitle_match = re.search(r'^##\s+(.+)$', content, re.MULTILINE)
    subtitle = subtitle_match.group(1) if subtitle_match else ""
    
    # Find all table data rows (lines starting with | **)
    # Format: | **term** (tibetan) | definition | location |
    rows = re.findall(
        r'^\|\s*\*\*([^*]+)\*\*\s*(?:\(([^)]+)\))?\s*(?:"([^"]+)")?\s*\|\s*(.+?)\s*\|\s*(\d{2}-\d{2}-\d{2}-\d{2}:\d+)\s*\|$',
        content, 
        re.MULTILINE
    )
    
    for row in rows:
        term_raw = row[0].strip()
        tibetan = row[1].strip() if row[1] else ""
        alt_form = row[2].strip() if row[2] else ""
        definition = row[3].strip()
        first_appearance = row[4].strip()
        
        # Format term with Tibetan/Sanskrit
        term_html = format_term(term_raw, tibetan, alt_form)
        
        # Clean up definition
        definition = process_definition(definition)
        
        # Get first letter for grouping
        first_letter = term_raw.strip()[0].upper()
        
        entries.append({
            'term': term_html,
            'tibetan': tibetan,
            'definition': definition,
            'first_appearance': first_appearance,
            'letter': first_letter
        })
    
    return {
        'title': title,
        'subtitle': subtitle,
        'entries': entries
    }

def format_term(term_raw, tibetan="", alt_form=""):
    """Format the term with Tibetan/Sanskrit highlighting."""
    term = html.escape(term_raw.strip())
    
    # Add Tibetan if present
    if tibetan:
        term = f'{term} <span class="tibetan">({tibetan})</span>'
    
    # Add alternate form if present
    if alt_form:
        term = f'{term} "{alt_form}"'
    
    return term

def process_definition(definition):
    """Process definition text with formatting."""
    definition = html.escape(definition)
    
    # Convert bold markers
    definition = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', definition)
    
    # Format Tibetan in definition
    definition = re.sub(r'([\u0F00-\u0FFF][\s\u0F00-\u0FFF]*)', 
                       r'<span class="tibetan">\1</span>', definition)
    
    # Format Sanskrit/Iast
    definition = re.sub(r'([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)', 
                       r'<span class="sanskrit">\1</span>', definition)
    
    return definition

def generate_html(glossary_data):
    """Generates the complete HTML document."""
    html_parts = []
    
    # Title section
    html_parts.append(f'''
    <div class="title-section">
        <h1>{html.escape(glossary_data['title'])}</h1>
        <div class="subtitle">{html.escape(glossary_data['subtitle'])}</div>
        <div class="description">
            ACQUAINTANCE: This glossary functions like a traditional glossary in the back of a translated religious work. 
            It provides definitions, context, and first appearances for lineage-specific terms, proper names, and technical vocabulary. 
            Readers should consult this glossary to understand specialized terminology encountered throughout the text.
            <br><br>
            Terms are listed alphabetically by their English rendering. Tibetan and Sanskrit equivalents are provided in parentheses.
        </div>
    </div>
    ''')
    
    # Group entries by letter
    entries_by_letter = {}
    for entry in glossary_data['entries']:
        letter = entry['letter']
        if letter not in entries_by_letter:
            entries_by_letter[letter] = []
        entries_by_letter[letter].append(entry)
    
    # Output entries grouped by letter
    for letter in sorted(entries_by_letter.keys()):
        html_parts.append(f'<div class="glossary-letter"><h2>{letter}</h2></div>')
        
        for entry in entries_by_letter[letter]:
            html_parts.append(f'''
            <div class="glossary-entry">
                <div class="term">{entry['term']}</div>
                <div class="definition">{entry['definition']}</div>
                <div class="first-appearance">
                    First Appearance: <span class="location">{html.escape(entry['first_appearance'])}</span>
                </div>
            </div>
            ''')
    
    return "\n".join(html_parts)

def build_full_document(glossary_data):
    """Wraps everything in HTML5 boilerplate."""
    
    content = generate_html(glossary_data)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html.escape(glossary_data['title'])}</title>
    <meta name="generator" content="Glossary Parser">
    <meta name="created" content="{datetime.now().isoformat()}">
    {HTML_CSS}
</head>
<body>
    <div class="document">
        {content}
    </div>
</body>
</html>
"""

# -----------------------------------------------------------------------------
# MAIN PROCESSING
# -----------------------------------------------------------------------------

def process_glossary():
    # Check Input File
    if not INPUT_FILE.exists():
        print(f"Error: Input file '{INPUT_FILE}' not found.")
        sys.exit(1)

    try:
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            content = f.read()

        print("Parsing glossary...")
        
        # Parse the glossary
        glossary_data = parse_glossary(content)
        
        print(f"  Found {len(glossary_data['entries'])} glossary entries")
        
        # Build HTML
        full_html = build_full_document(glossary_data)

        # Write Output
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write(full_html)

        print(f"\n✓ Complete! Output saved to '{OUTPUT_FILE}'")
        print(f"\nTo create PDF:")
        print(f"  1. Open '{OUTPUT_FILE}' in Chrome or Edge")
        print(f"  2. Press Ctrl+P (Print)")
        print(f"  3. Select 'Save as PDF'")
        print(f"  4. Ensure 'Background graphics' is checked")
        print(f"  5. Set margins to 'Default' or 'Minimum'")
        print(f"  6. Click Save")

    except Exception as e:
        print(f"Error processing glossary: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    process_glossary()
