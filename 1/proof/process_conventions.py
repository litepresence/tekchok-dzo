#!/usr/bin/env python3
"""
Editorial Conventions Page Generator
Parses convention markdown files and outputs a static HTML page.
"""

import os
from datetime import datetime
from pathlib import Path

import markdown

INPUT_DIR = Path("../text/preface/conventions")
OUTPUT_FILE = Path("html/conventions.html")

SECTION_ORDER = [
    ('exposition_tibetan.md', 'Tibetan', 'tibetan'),
    ('exposition_wylie.md', 'Wylie', 'wylie'),
    ('exposition_literal.md', 'Literal', 'literal'),
    ('exposition_liturgical.md', 'Liturgical', 'liturgical'),
    ('exposition_commentary.md', 'Commentary', 'commentary'),
    ('exposition_scholar.md', 'Scholar', 'scholar'),
    ('exposition_epistemic.md', 'Epistemic', 'epistemic'),
    ('exposition_delusion.md', 'Delusion', 'delusion'),
    ('exposition_cognitive.md', 'Cognitive', 'cognitive'),
]

def process_conventions():
    sections = []
    toc_items = []
    
    for filename, title, anchor in SECTION_ORDER:
        filepath = INPUT_DIR / filename
        if filepath.exists():
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            html_content = markdown.markdown(content, extensions=['tables', 'fenced_code'])
            sections.append(f'<section id="{anchor}" class="convention-section">\n<h2>{title}</h2>\n{html_content}\n</section>')
            toc_items.append(f'<li><a href="#{anchor}">{title}</a></li>')
            print(f"  ✓ Processed: {filename}")
        else:
            print(f"  ✗ Not found: {filename}")
    
    toc_html = '<nav class="toc"><h2>Layers</h2><ul>' + '\n'.join(toc_items) + '</ul></nav>'
    content_html = '\n'.join(sections)
    
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Editorial Conventions - Treasury of the Supreme Vehicle</title>
    <meta name="created" content="{datetime.now().isoformat()}">
    <link rel="stylesheet" href="../css/conventions.css">
    <script src="../js/conventions.js"></script>
</head>
<body>
    <div class="container">
        <header>
            <h1>Editorial Conventions</h1>
            <div class="subtitle">Translation Layer Methodologies</div>
        </header>
        {toc_html}
        <main>
            {content_html}
        </main>
    </div>
</body>
</html>
"""
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    print(f"\n✓ Created: {OUTPUT_FILE}")

if __name__ == "__main__":
    process_conventions()
