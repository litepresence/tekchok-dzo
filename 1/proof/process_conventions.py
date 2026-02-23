#!/usr/bin/env python3
"""
Editorial Conventions Page Generator
Parses convention markdown files and outputs a static HTML page.
"""

import os
from pathlib import Path
from datetime import datetime
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
    <style>
        @page {{ size: 6in 9in; margin: 0.75in; }}
        :root {{
            --font-main: 'Georgia', 'Times New Roman', serif;
            --font-sans: 'Helvetica', 'Arial', sans-serif;
            --color-bg: #1e1e1e;
            --color-text: #e0e0e0;
            --color-muted: #a0a0a0;
            --color-accent: #bcaaa4;
            --color-header: #d7ccc8;
            --color-border: #3a3a3a;
            --color-link: #7eb8c9;
        }}
        * {{ box-sizing: border-box; }}
        body {{
            font-family: var(--font-main);
            color: var(--color-text);
            background: var(--color-bg);
            line-height: 1.6;
            font-size: 11pt;
            margin: 0;
            padding: 0;
            -webkit-print-color-adjust: exact;
        }}
        .container {{
            max-width: 800px;
            margin: 0 auto;
            padding: 2em;
        }}
        header {{
            text-align: center;
            padding: 2em 0;
            border-bottom: 1px solid var(--color-border);
            margin-bottom: 2em;
        }}
        header h1 {{
            font-size: 1.8em;
            color: var(--color-header);
            margin: 0 0 0.5em 0;
            font-variant: small-caps;
        }}
        header .subtitle {{
            color: var(--color-muted);
            font-size: 0.9em;
        }}
        .back-link {{
            display: inline-block;
            color: var(--color-link);
            text-decoration: none;
            font-family: var(--font-sans);
            font-size: 0.9em;
            margin-bottom: 1em;
        }}
        .back-link:hover {{
            text-decoration: underline;
        }}
        .toc {{
            background: rgba(60, 60, 60, 0.3);
            border: 1px solid var(--color-border);
            border-radius: 8px;
            padding: 1.5em 2em;
            margin-bottom: 2em;
        }}
        .toc h2 {{
            margin: 0 0 1em 0;
            font-size: 1.1em;
            color: var(--color-accent);
        }}
        .toc ul {{
            list-style: none;
            padding: 0;
            margin: 0;
            display: flex;
            flex-wrap: wrap;
            gap: 0.5em 1.5em;
        }}
        .toc li {{
            margin: 0;
        }}
        .toc a {{
            color: var(--color-link);
            text-decoration: none;
            font-family: var(--font-sans);
            font-size: 0.9em;
        }}
        .toc a:hover {{
            text-decoration: underline;
        }}
        .convention-section {{
            margin-bottom: 3em;
            padding-bottom: 2em;
            border-bottom: 1px solid var(--color-border);
        }}
        .convention-section:last-child {{
            border-bottom: none;
        }}
        .convention-section h2 {{
            font-size: 1.4em;
            color: var(--color-header);
            margin: 0 0 1em 0;
            padding-bottom: 0.5em;
            border-bottom: 2px solid var(--color-accent);
        }}
        h3 {{
            font-size: 1.2em;
            color: var(--color-accent);
            margin: 1.5em 0 0.75em 0;
        }}
        h4 {{
            font-size: 1.1em;
            color: var(--color-text);
            margin: 1.25em 0 0.5em 0;
        }}
        p {{
            margin: 0.75em 0;
            text-align: justify;
        }}
        ul, ol {{
            margin: 0.75em 0;
            padding-left: 1.5em;
        }}
        li {{
            margin: 0.4em 0;
        }}
        strong {{
            color: var(--color-accent);
        }}
        em {{
            color: var(--color-muted);
        }}
        code {{
            background: rgba(100, 100, 100, 0.3);
            padding: 0.15em 0.4em;
            border-radius: 3px;
            font-family: 'Consolas', 'Monaco', monospace;
            font-size: 0.9em;
        }}
        pre {{
            background: rgba(60, 60, 60, 0.5);
            padding: 1em;
            border-radius: 5px;
            overflow-x: auto;
            border: 1px solid var(--color-border);
        }}
        pre code {{
            background: none;
            padding: 0;
        }}
        a {{
            color: var(--color-link);
        }}
        footer {{
            text-align: center;
            padding: 2em 0;
            margin-top: 2em;
            border-top: 1px solid var(--color-border);
        }}
        footer a {{
            color: var(--color-link);
            text-decoration: none;
            font-family: var(--font-sans);
        }}
        footer a:hover {{
            text-decoration: underline;
        }}
        @media print {{
            .back-link, footer {{ display: none; }}
            .container {{ max-width: none; padding: 0; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <a href="index.html" class="back-link">← Back to Treasury</a>
        <header>
            <h1>Editorial Conventions</h1>
            <div class="subtitle">Translation Layer Methodologies</div>
        </header>
        {toc_html}
        <main>
            {content_html}
        </main>
        <footer>
            <a href="index.html">← Return to Treasury of the Supreme Vehicle</a>
        </footer>
    </div>
</body>
</html>
"""
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    print(f"\n✓ Created: {OUTPUT_FILE}")

if __name__ == "__main__":
    process_conventions()
