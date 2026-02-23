```python
#!/usr/bin/env python3
"""
Introduction Parser
Parses main introduction, volume introductions, and chapter introductions
and outputs a single combined HTML file optimized for PDF rendering and iframe navigation.
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
# Adjust these paths based on where this script runs relative to the text folder
BASE_DIR = Path("../text/preface")
INTRO_DIR = BASE_DIR / "introduction"
VOLUME_DIR = BASE_DIR / "volume"
CHAPTER_DIR = BASE_DIR / "chapter"
OUTPUT_FILE = Path("html/introduction_proof.html")

# Define the exact sequence of files to ensure correct navigation order
FILE_SEQUENCE = [
    # Main Introduction
    {"type": "main", "path": INTRO_DIR / "intro.md", "id": "intro-main", "title": "General Introduction"},
    
    # Volume 1
    {"type": "volume", "path": VOLUME_DIR / "01-00-00-00.txt", "id": "vol-01", "title": "Volume 1 Introduction"},
    
    # Volume 1 Chapters
    {"type": "chapter", "path": CHAPTER_DIR / "01-01-00-00.txt", "id": "chap-01-01", "title": "Chapter 1: The Perfect Teacher"},
    {"type": "chapter", "path": CHAPTER_DIR / "01-02-00-00.txt", "id": "chap-01-02", "title": "Chapter 2: The Container and Contents"},
    {"type": "chapter", "path": CHAPTER_DIR / "01-03-00-00.txt", "id": "chap-01-03", "title": "Chapter 3: Aggregates, Elements, and Sense Sources"},
    {"type": "chapter", "path": CHAPTER_DIR / "01-04-00-00.txt", "id": "chap-01-04", "title": "Chapter 4: Vehicle Enumeration"},
    {"type": "chapter", "path": CHAPTER_DIR / "01-05-00-00.txt", "id": "chap-01-05", "title": "Chapter 5: Empowerment and Samaya"},
    {"type": "chapter", "path": CHAPTER_DIR / "01-06-00-00.txt", "id": "chap-01-06", "title": "Chapter 6: Samaya Discipline"},
    {"type": "chapter", "path": CHAPTER_DIR / "01-07-00-00.txt", "id": "chap-01-07", "title": "Chapter 7: Samaya Restoration"},
    {"type": "chapter", "path": CHAPTER_DIR / "01-08-00-00.txt", "id": "chap-01-08", "title": "Chapter 8: Ground, Path, and Fruit"},
    {"type": "chapter", "path": CHAPTER_DIR / "01-09-00-00.txt", "id": "chap-01-09", "title": "Chapter 9: Delusion and Liberation"},
    {"type": "chapter", "path": CHAPTER_DIR / "01-10-00-00.txt", "id": "chap-01-10", "title": "Chapter 10: Arising of Elements"},
    {"type": "chapter", "path": CHAPTER_DIR / "01-11-00-00.txt", "id": "chap-01-11", "title": "Chapter 11: Body Formation"},
    {"type": "chapter", "path": CHAPTER_DIR / "01-12-00-00.txt", "id": "chap-01-12", "title": "Chapter 12: Channels, Winds, and Bindu"},
    {"type": "chapter", "path": CHAPTER_DIR / "01-13-00-00.txt", "id": "chap-01-13", "title": "Chapter 13: Luminosity"},
    {"type": "chapter", "path": CHAPTER_DIR / "01-14-00-00.txt", "id": "chap-01-14", "title": "Chapter 14: Mind and Pristine Awareness"},
    
    # Volume 2
    {"type": "volume", "path": VOLUME_DIR / "02-00-00-00.txt", "id": "vol-02", "title": "Volume 2 Introduction"},
    
    # Volume 2 Chapters
    {"type": "chapter", "path": CHAPTER_DIR / "02-15-00-00.txt", "id": "chap-02-15", "title": "Chapter 15: Elements Place"},
    {"type": "chapter", "path": CHAPTER_DIR / "02-16-00-00.txt", "id": "chap-02-16", "title": "Chapter 16: Kaya and Wisdom"},
    {"type": "chapter", "path": CHAPTER_DIR / "02-17-00-00.txt", "id": "chap-02-17", "title": "Chapter 17: Path and Signs"},
    {"type": "chapter", "path": CHAPTER_DIR / "02-18-00-00.txt", "id": "chap-02-18", "title": "Chapter 18: Luminosity Path"},
    {"type": "chapter", "path": CHAPTER_DIR / "02-19-00-00.txt", "id": "chap-02-19", "title": "Chapter 19: Cutting Through"},
    {"type": "chapter", "path": CHAPTER_DIR / "02-20-00-00.txt", "id": "chap-02-20", "title": "Chapter 20: Leap-Over"},
    {"type": "chapter", "path": CHAPTER_DIR / "02-21-00-00.txt", "id": "chap-02-21", "title": "Chapter 21: Introduction"},
    {"type": "chapter", "path": CHAPTER_DIR / "02-22-00-00.txt", "id": "chap-02-22", "title": "Chapter 22: Signs of Liberation"},
    {"type": "chapter", "path": CHAPTER_DIR / "02-23-00-00.txt", "id": "chap-02-23", "title": "Chapter 23: Intermediate State"},
    {"type": "chapter", "path": CHAPTER_DIR / "02-24-00-00.txt", "id": "chap-02-24", "title": "Chapter 24: Emanation Field"},
    {"type": "chapter", "path": CHAPTER_DIR / "02-25-00-00.txt", "id": "chap-02-25", "title": "Chapter 25: Fruition"},
]

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
        color: #888;
    }
}
:root {
    --font-main: 'Georgia', 'Times New Roman', serif;
    --font-sans: 'Helvetica', 'Arial', sans-serif;
    --font-mono: 'Consolas', 'Courier New', monospace;
    --color-bg: #1e1e1e;
    --color-text: #e0e0e0;
    --color-muted: #a0a0a0;
    --color-accent: #8b7355;
    --color-chapter: #d4a574;
    --color-border: #3a3a3a;
    --color-btn: #2d5a7b;
    --color-btn-hover: #3d7a9b;
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
    background-color: var(--color-bg);
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
}
.document {
    max-width: 5.5in;
    margin: 0 auto;
    padding: 0;
}
.intro-section {
    display: none;
    padding: 2em 0;
    border-bottom: 1px solid var(--color-border);
}
.intro-section.active {
    display: block;
}
.intro-section:first-child {
    padding-top: 0;
}
.intro-header {
    font-family: var(--font-sans);
    font-size: 1.2em;
    font-weight: 600;
    margin-top: 0;
    margin-bottom: 0.5em;
    color: var(--color-chapter);
    border-left: 4px solid var(--color-accent);
    padding-left: 0.5em;
}
.intro-content {
    font-size: 0.95em;
    text-align: justify;
    hyphens: auto;
    -webkit-hyphens: auto;
}
.intro-content h1, .intro-content h2, .intro-content h3 {
    color: var(--color-chapter);
    font-family: var(--font-sans);
    margin-top: 1.5em;
}
.intro-content strong {
    color: var(--color-accent);
}
.nav-controls {
    position: fixed;
    bottom: 20px;
    right: 20px;
    display: flex;
    gap: 10px;
    z-index: 1000;
}
.nav-btn {
    background-color: var(--color-btn);
    color: var(--color-text);
    border: none;
    padding: 12px 20px;
    font-size: 14px;
    cursor: pointer;
    border-radius: 5px;
    font-family: var(--font-sans);
    transition: background-color 0.2s;
}
.nav-btn:hover {
    background-color: var(--color-btn-hover);
}
.nav-btn:disabled {
    background-color: #444;
    color: #666;
    cursor: not-allowed;
}
.chapter-indicator {
    position: fixed;
    bottom: 20px;
    left: 20px;
    background-color: rgba(30, 30, 30, 0.9);
    color: var(--color-chapter);
    padding: 10px 15px;
    border-radius: 5px;
    font-family: var(--font-sans);
    font-size: 12px;
    z-index: 1000;
}
.highlighted-section {
    background-color: rgba(139, 115, 85, 0.2) !important;
    border-radius: 3px;
    animation: highlightFade 3s ease-out forwards;
}
@keyframes highlightFade {
    0% { background-color: rgba(139, 115, 85, 0.4); }
    80% { background-color: rgba(139, 115, 85, 0.2); }
    100% { background-color: transparent; }
}
@media print {
    body {
        font-size: 9.5pt;
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
    }
    .document {
        max-width: none;
    }
    .nav-controls,
    .chapter-indicator {
        display: none;
    }
    .intro-section {
        display: block !important;
        page-break-after: always;
    }
}
</style>
"""

# -----------------------------------------------------------------------------
# PARSER LOGIC
# -----------------------------------------------------------------------------
def parse_markdown_text(text):
    """
    Converts simple Markdown syntax to HTML.
    Handles headers, bold, lists, and paragraphs.
    """
    # Escape HTML first
    text = html.escape(text)
    
    # Headers
    text = re.sub(r'^### (.+)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    text = re.sub(r'^## (.+)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    text = re.sub(r'^# (.+)$', r'<h1>\1</h1>', text, flags=re.MULTILINE)
    
    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    
    # Lists (simple bullet points)
    text = re.sub(r'^- (.+)$', r'<li>\1</li>', text, flags=re.MULTILINE)
    text = re.sub(r'(<li>.*?</li>\n?)+', lambda m: '<ul>' + m.group(0) + '</ul>', text)
    
    # Paragraphs (split by double newline)
    paragraphs = text.split('\n\n')
    html_parts = []
    for p in paragraphs:
        p = p.strip()
        if p and not p.startswith('<h') and not p.startswith('<ul') and not p.startswith('<li'):
            html_parts.append(f'<p>{p}</p>')
        else:
            html_parts.append(p)
    
    return "\n".join(html_parts)

def generate_section_html(file_data, content):
    """Generates HTML content for a single introduction section."""
    html_parts = []
    html_parts.append(f'<div class="intro-section" id="{file_data["id"]}">')
    html_parts.append(f'<h2 class="intro-header">{file_data["title"]}</h2>')
    html_parts.append('<div class="intro-content">')
    html_parts.append(parse_markdown_text(content))
    html_parts.append('</div>')
    html_parts.append('</div>')
    return "\n".join(html_parts)

def build_full_document(sections_html, total_sections):
    """Wraps everything in HTML5 boilerplate with navigation."""
    # Create JS array of section IDs for navigation
    section_ids = [s["id"] for s in FILE_SEQUENCE]
    section_titles = [s["title"] for s in FILE_SEQUENCE]
    
    js_script = f"""
<script>
let currentSection = 0;
const totalSections = {total_sections};
const sectionIds = {section_ids};
const sectionTitles = {section_titles};

function showSection(index) {{
    const sections = document.querySelectorAll('.intro-section');
    sections.forEach((sec, i) => {{
        sec.classList.toggle('active', i === index);
    }});
    currentSection = index;
    updateNavButtons();
    updateIndicator();
    window.scrollTo({{ top: 0, behavior: 'instant' }});
}}

function nextSection() {{
    if (currentSection < totalSections - 1) {{
        showSection(currentSection + 1);
    }}
}}

function prevSection() {{
    if (currentSection > 0) {{
        showSection(currentSection - 1);
    }}
}}

function updateNavButtons() {{
    document.getElementById('prevBtn').disabled = currentSection === 0;
    document.getElementById('nextBtn').disabled = currentSection === totalSections - 1;
}}

function updateIndicator() {{
    document.getElementById('sectionIndicator').textContent = sectionTitles[currentSection];
}}

function scrollToSection(id) {{
    const index = sectionIds.indexOf(id);
    if (index !== -1) {{
        showSection(index);
        setTimeout(() => {{
            const el = document.getElementById(id);
            if (el) {{
                el.classList.add('highlighted-section');
                el.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
            }}
        }}, 100);
        return true;
    }}
    return false;
}}

function handleUrlParams() {{
    const params = new URLSearchParams(window.location.search);
    const chapter = params.get('chapter');
    const volume = params.get('volume');
    
    // Try to match chapter/volume to section ID
    if (chapter) {{
        const targetId = 'chap-' + chapter.replace(/-/g, '-');
        if (scrollToSection(targetId)) return;
    }}
    if (volume) {{
        const targetId = 'vol-' + volume;
        if (scrollToSection(targetId)) return;
    }}
    
    // Default to main intro
    showSection(0);
}}

document.addEventListener('DOMContentLoaded', () => {{
    updateNavButtons();
    updateIndicator();
    handleUrlParams();
    
    // Listen for messages from parent frame (for radio button sync)
    window.addEventListener('message', (event) => {{
        if (event.data && event.data.type === 'navigateIntroduction') {{
            if (event.data.chapter) {{
                const targetId = 'chap-' + event.data.chapter.replace(/-/g, '-');
                scrollToSection(targetId);
            }} else if (event.data.volume) {{
                const targetId = 'vol-' + event.data.volume;
                scrollToSection(targetId);
            }} else if (event.data.main) {{
                showSection(0);
            }}
        }}
    }});
}});
</script>
"""
    nav_html = """
<div class="nav-controls">
    <button class="nav-btn" id="prevBtn" onclick="prevSection()">Previous</button>
    <button class="nav-btn" id="nextBtn" onclick="nextSection()">Next</button>
</div>
<div class="chapter-indicator" id="sectionIndicator">Introduction</div>
"""
    combined_content = "\n".join(sections_html)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Treasury Introductions</title>
    <meta name="generator" content="Introduction Parser">
    <meta name="created" content="{datetime.now().isoformat()}">
    {HTML_CSS}
    {js_script}
</head>
<body>
    <div class="document">
        {combined_content}
    </div>
    {nav_html}
</body>
</html>
"""

# -----------------------------------------------------------------------------
# BATCH PROCESSING
# -----------------------------------------------------------------------------
def process_introductions():
    sections_html = []
    valid_sections = 0
    
    print(f"Processing introductions...")
    
    for file_data in FILE_SEQUENCE:
        path = file_data["path"]
        if not path.exists():
            print(f"  ⚠ Warning: File not found: {path}")
            # Create a placeholder if file is missing to maintain navigation structure
            content = f"*Introduction file not found: {path.name}*"
        else:
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception as e:
                print(f"  ✗ Error reading {path}: {e}")
                content = f"*Error reading file: {e}*"
        
        section_html = generate_section_html(file_data, content)
        sections_html.append(section_html)
        valid_sections += 1
        print(f"  ✓ Processed: {file_data['title']}")
    
    full_html = build_full_document(sections_html, valid_sections)
    
    # Ensure output directory exists
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    print(f"\n✓ Complete! Output saved to '{OUTPUT_FILE}'")
    print(f"  Total sections: {valid_sections}")
    print(f"\nIntegration Note:")
    print(f"  Add a radio button to index.html with value='introduction'")
    print(f"  Target iframe should load '{OUTPUT_FILE.name}'")
    print(f"  Pass chapter/volume params via URL or postMessage for sync.")

if __name__ == "__main__":
    process_introductions()
```