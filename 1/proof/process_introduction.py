#!/usr/bin/env python3
"""
Introduction Parser
Parses preface materials and outputs a single combined HTML file.
"""

import os
import re
import html
import sys
from pathlib import Path
from datetime import datetime
import markdown

INPUT_DIR = Path("../text/preface")
OUTPUT_FILE = Path("html/introduction_proof.html")

def md_to_html(content):
    """Convert markdown to HTML."""
    return markdown.markdown(content, extensions=['tables', 'fenced_code'])

def process_introduction():
    sections = []
    
    main_intro = INPUT_DIR / "introduction" / "main_introduction.md"
    if main_intro.exists():
        with open(main_intro, 'r', encoding='utf-8') as f:
            content = f.read()
        sections.append(('<section class="main-intro">', md_to_html(content), '</section>'))
    
    volume_dir = INPUT_DIR / "volume"
    if volume_dir.exists():
        files = sorted(os.listdir(volume_dir))
        for fname in files:
            if fname.endswith('.txt'):
                with open(volume_dir / fname, 'r', encoding='utf-8') as f:
                    content = f.read()
                vol_num = fname[:2]
                sections.append((f'<section class="volume" id="vol-{vol_num}">', md_to_html(content), '</section>'))
                
                chapter_dir = INPUT_DIR / "chapter"
                if chapter_dir.exists():
                    chapter_files = sorted([f for f in os.listdir(chapter_dir) if f.startswith(vol_num)])
                    for cf in chapter_files:
                        with open(chapter_dir / cf, 'r', encoding='utf-8') as f:
                            ccontent = f.read()
                        sections.append((f'<section class="chapter">', md_to_html(ccontent), '</section>'))
    
    html_content = '\n'.join([f'{start}\n{content}\n{end}' for start, content, end in sections])
    
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Introduction - Treasury of the Supreme Vehicle</title>
    <meta name="created" content="{datetime.now().isoformat()}">
    <style>
        @page {{ size: 6in 9in; margin: 0.75in; }}
        :root {{
            --font-main: 'Georgia', 'Times New Roman', serif;
            --color-bg: #1e1e1e;
            --color-text: #e0e0e0;
            --color-muted: #a0a0a0;
            --color-accent: #bcaaa4;
            --color-header: #d7ccc8;
            --color-border: #3a3a3a;
        }}
        * {{ box-sizing: border-box; }}
        body {{
            font-family: var(--font-main);
            color: var(--color-text);
            background: var(--color-bg);
            line-height: 1.6;
            font-size: 11pt;
            margin: 0;
            padding: 2em;
            -webkit-print-color-adjust: exact;
        }}
        .document {{ max-width: 6in; margin: 0 auto; }}
        h1 {{ font-size: 1.4em; color: var(--color-header); margin-top: 1.5em; }}
        h2 {{ font-size: 1.2em; color: var(--color-accent); margin-top: 1.5em; border-bottom: 1px solid var(--color-border); padding-bottom: 0.5em; }}
        h3 {{ font-size: 1.1em; color: var(--color-text); }}
        p {{ margin: 0.75em 0; text-align: justify; }}
        hr {{ border: none; border-top: 1px solid var(--color-border); margin: 2em 0; }}
        li {{ margin: 0.5em 0 0.5em 1.5em; }}
        strong {{ color: var(--color-accent); }}
        .main-intro h1 {{ text-align: center; font-variant: small-caps; }}
        .volume {{ margin-top: 3em; page-break-before: always; }}
        .volume h1 {{ text-align: center; }}
        .chapter {{ margin: 2em 0; padding: 1em; border-left: 3px solid var(--color-accent); background: rgba(60,60,60,0.3); }}
        .chapter h2 {{ margin-top: 0; border: none; }}
    </style>
</head>
<body>
    <div class="document">
        {html_content}
    </div>
</body>
</html>
"""
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    print(f"Created: {OUTPUT_FILE}")

if __name__ == "__main__":
    process_introduction()
