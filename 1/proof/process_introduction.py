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

CHAPTER_MAP = {
    '01-01-00-00': 1, '01-02-00-00': 584, '01-03-00-00': 1247, '01-04-00-00': 1931,
    '01-05-00-00': 3282, '01-06-00-00': 4021, '01-07-00-00': 4728, '01-08-00-00': 5368,
    '01-09-00-00': 6103, '01-10-00-00': 6987, '01-11-00-00': 7724, '01-12-00-00': 8442,
    '01-13-00-00': 9250, '01-14-00-00': 10001, '02-15-00-00': 10702, '02-16-00-00': 11397,
    '02-17-00-00': 12025, '02-18-00-00': 12604, '02-19-00-00': 13247, '02-20-00-00': 13921,
    '02-21-00-00': 14615, '02-22-00-00': 14985, '02-23-00-00': 15320, '02-24-00-00': 15635,
    '02-25-00-00': 16272
}

def md_to_html(content):
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
                        chapter_id = cf.replace('.txt', '')
                        sections.append((f'<section class="chapter" id="chapter-{chapter_id}">', md_to_html(ccontent), '</section>'))
    
    html_content = '\n'.join([f'{start}\n{content}\n{end}' for start, content, end in sections])
    chapter_keys = list(CHAPTER_MAP.keys())
    
    js_script = f"""
<script>
const CHAPTER_MAP = {CHAPTER_MAP};
const chapters = {chapter_keys};
let currentChapter = 0;
let lastReportedChapter = null;

function showChapter(index) {{
    if (index < 0 || index >= chapters.length) return;
    currentChapter = index;
    const el = document.getElementById('chapter-' + chapters[index]);
    if (el) el.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
    updateButtons();
}}

function nextChapter() {{ showChapter(currentChapter + 1); }}
function prevChapter() {{ showChapter(currentChapter - 1); }}

function updateButtons() {{
    document.getElementById('prevBtn').disabled = currentChapter === 0;
    document.getElementById('nextBtn').disabled = currentChapter === chapters.length - 1;
}}

function handleHash() {{
    const hash = window.location.hash;
    const match = hash.match(/chapter-([\\d-]+)/);
    if (match) {{
        const idx = chapters.indexOf(match[1]);
        if (idx >= 0) showChapter(idx);
    }}
}}

function reportChapter() {{
    const chaptersEls = document.querySelectorAll('[id^="chapter-"]');
    let found = null;
    for (const el of chaptersEls) {{
        const rect = el.getBoundingClientRect();
        if (rect.top < 300 && rect.bottom > 50) {{
            found = el.id.replace('chapter-', '');
            break;
        }}
    }}
    if (found && found !== lastReportedChapter && CHAPTER_MAP[found]) {{
        lastReportedChapter = found;
        window.parent.postMessage({{ type: 'chapterPosition', chapter: found, line: CHAPTER_MAP[found] }}, '*');
    }}
}}

// Throttled scroll reporting
let scrollTimeout;
function onScroll() {{
    clearTimeout(scrollTimeout);
    scrollTimeout = setTimeout(reportChapter, 100);
}}

document.addEventListener('DOMContentLoaded', () => {{
    updateButtons();
    handleHash();
    window.addEventListener('scroll', onScroll);
    // Initial report after a short delay
    setTimeout(reportChapter, 200);
}});
window.addEventListener('hashchange', handleHash);
</script>
"""
    
    nav_html = """
<div class="nav-controls">
    <button class="nav-btn" id="prevBtn" onclick="prevChapter()">Previous</button>
    <button class="nav-btn" id="nextBtn" onclick="nextChapter()">Next Chapter</button>
</div>
"""
    
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
            --font-sans: 'Helvetica', 'Arial', sans-serif;
            --color-bg: #1e1e1e;
            --color-text: #e0e0e0;
            --color-muted: #a0a0a0;
            --color-accent: #bcaaa4;
            --color-header: #d7ccc8;
            --color-border: #3a3a3a;
            --color-btn: #2d5a7b;
            --color-btn-hover: #3d7a9b;
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
        .nav-controls {{
            position: fixed;
            bottom: 20px;
            right: 20px;
            display: flex;
            gap: 10px;
            z-index: 1000;
        }}
        .nav-btn {{
            background-color: var(--color-btn);
            color: var(--color-text);
            border: none;
            padding: 12px 20px;
            font-size: 14px;
            cursor: pointer;
            border-radius: 5px;
            font-family: var(--font-sans);
            transition: background-color 0.2s;
        }}
        .nav-btn:hover {{ background-color: var(--color-btn-hover); }}
        .nav-btn:disabled {{ background-color: #444; color: #666; cursor: not-allowed; }}
        @media print {{ .nav-controls {{ display: none; }} }}
    </style>
    {js_script}
</head>
<body>
    <div class="document">
        {html_content}
    </div>
    {nav_html}
</body>
</html>
"""
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    print(f"Created: {OUTPUT_FILE}")

if __name__ == "__main__":
    process_introduction()
