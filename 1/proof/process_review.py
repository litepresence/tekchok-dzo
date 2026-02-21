#!/usr/bin/env python3
"""
Review Prompt Generator
Generates chapter-by-chapter review prompts for AI bots.
Each output file contains the Tibetan, literal, and liturgical layers for review.
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

TIBETAN_DIR = Path("../text/frozen/tibetan")
LITERAL_DIR = Path("../text/frozen/literal")
LITURGICAL_DIR = Path("../text/frozen/liturgical")
OUTPUT_DIR = Path("review")
CONTENTS_FILE = Path("../contents/contents.md")

# File pattern: VV-CC-SS-ss.txt
FILE_PATTERN = re.compile(r'^(\d\d)-(\d\d)-(\d\d)-(\d\d)\.txt$')

# -----------------------------------------------------------------------------
# MISSION STATEMENTS
# -----------------------------------------------------------------------------

LITERAL_MISSION = """# LITERAL MISSION STATEMENT

## Expected Output: Dense, Concise Literal Translation

The literal layer should provide:
- Word-by-word or phrase-by-phrase translation closest to Tibetan syntax
- Technical term consistency (same English term for same Tibetan term)
- Minimal elaboration - translate what is there, no more
- Serve as "truth" reference for checking interpretive translations
- Use compound structures that mirror Tibetan word compounds
- Preserve Tibetan word order where possible
- Include Sanskrit loanwords in IAST transliteration when original is Sanskrit
- Mark Tibetan technical terms in italics or parentheses
- No theological interpretation or doctrinal elaboration
- Cadence should feel slightly "awkward" in English - this is a feature, not a bug"""

LITURGICAL_MISSION = """# LITURGICAL MISSION STATEMENT

## Expected Output: Poetic, Devotional, Oral-Performance Ready

The liturgical layer should provide:
- Flowing, elegant English that sounds good when chanted or read aloud
- Proper English grammar and syntax (readable, not literally awkward)
- Traditional Buddhist terminology in standard English translations
- Verse/prose formatting with clear break markers
- Tags indicating vocal performance:
  - <ornament> - Title markers, colophons, auspicious openings
  - <break> - Major section transitions
  - <verse> - Metric lines meant for chanting
  - <prose> - Explanatory passages for oral delivery
  - <prayer> - Devotional requests or aspirations
  - <citation> - Scriptural references or quotations
- Appropriate honorifics and devotional language
- Should "come alive" when performed orally
- Preserves meaning while prioritizing beauty and usability"""

# -----------------------------------------------------------------------------
# PARSER LOGIC
# -----------------------------------------------------------------------------

def parse_contents():
    """Parse contents.md to get chapter information."""
    if not CONTENTS_FILE.exists():
        print(f"Warning: Contents file not found at {CONTENTS_FILE}")
        return []
    
    with open(CONTENTS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    chapters = []
    
    # Find all chapters
    chapter_pattern = re.compile(r'^##\s+Chapter\s+(\d+):\s+(.+)$', re.MULTILINE)
    chapter_matches = list(chapter_pattern.finditer(content))
    
    for i, match in enumerate(chapter_matches):
        chapter_num = match.group(1).zfill(2)
        chapter_title = match.group(2).strip()
        
        # Find chapter header info
        start_pos = match.end()
        end_pos = chapter_matches[i+1].start() if i + 1 < len(chapter_matches) else len(content)
        chapter_content = content[start_pos:end_pos]
        
        # Get volume
        vol_match = re.search(r'\*\*Volume\*\*:\s*(\d+)', chapter_content)
        volume = vol_match.group(1) if vol_match else "01"
        
        # Extract file names for this chapter
        files = re.findall(r'\|\s*([\w_]+\.md)\s*\|', chapter_content)
        
        # Convert .md to .txt with VV-CC-SS-ss pattern
        txt_files = []
        for f in files:
            # ch1_sec1.md -> need to find matching txt
            # The txt files are like 01-01-01-01.txt
            pass
        
        chapters.append({
            'number': chapter_num,
            'title': chapter_title,
            'volume': volume,
            'files': files
        })
    
    return chapters

def get_chapter_files(chapter_num):
    """Get all files belonging to a chapter."""
    chapter_int = int(chapter_num)
    
    # Chapters 1-14 are in volume 01, chapters 15-25 are in volume 02
    if chapter_int <= 14:
        vol = "01"
        ch = chapter_num.zfill(2)  # 1 -> 01, 2 -> 02, etc.
    else:
        vol = "02"
        ch = chapter_num.zfill(2)  # 15 -> 15, 16 -> 16, etc. (not reset!)
    
    files = []
    
    # Scan literal directory for matching files
    if LITERAL_DIR.exists():
        for f in os.listdir(LITERAL_DIR):
            if f.endswith('.txt') and not f.endswith('.backup'):
                match = FILE_PATTERN.match(f)
                if match:
                    file_vol = match.group(1)
                    file_ch = match.group(2)
                    
                    if file_ch == ch and file_vol == vol:
                        files.append(f)
    
    return sorted(files)

def parse_line_content(line):
    """Parse a single line to extract line number and content."""
    # Pattern: [line_num] content or [line_num] <tag> content
    match = re.match(r'\[(\d+)\]\s*(.*)$', line.strip())
    if not match:
        return None
    
    line_num = match.group(1)
    content = match.group(2)
    
    # Extract tag if present
    tag_match = re.match(r'<(\w+)>\s*(.*)$', content)
    if tag_match:
        tag = tag_match.group(1)
        text = tag_match.group(2)
    else:
        tag = None
        text = content
    
    return {
        'line': line_num,
        'tag': tag,
        'text': text
    }

def read_layer_file(filepath):
    """Read a layer file and return parsed lines."""
    if not filepath.exists():
        return []
    
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    parsed = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        result = parse_line_content(line)
        if result:
            parsed.append(result)
    
    return parsed

def merge_layers(tibetan_files, literal_files, liturgical_files):
    """Merge all three layers by line number."""
    # Read all files
    tibetan_data = {}
    for f in tibetan_files:
        data = read_layer_file(TIBETAN_DIR / f)
        for item in data:
            tibetan_data[item['line']] = item['text']
    
    literal_data = {}
    for f in literal_files:
        data = read_layer_file(LITERAL_DIR / f)
        for item in data:
            literal_data[item['line']] = item['text']
    
    liturgical_data = {}
    for f in liturgical_files:
        data = read_layer_file(LITURGICAL_DIR / f)
        for item in data:
            liturgical_data[item['line']] = {'tag': item['tag'], 'text': item['text']}
    
    # Merge by line number
    all_lines = sorted(set(list(tibetan_data.keys()) + 
                          list(literal_data.keys()) + 
                          list(liturgical_data.keys())), 
                     key=lambda x: int(x))
    
    merged = []
    for line_num in all_lines:
        tibetan = tibetan_data.get(line_num, "")
        literal = literal_data.get(line_num, "")
        
        lit_data = liturgical_data.get(line_num, {'tag': None, 'text': ""})
        liturgical_tag = lit_data['tag']
        liturgical_text = lit_data['text']
        
        merged.append({
            'line': line_num,
            'tibetan': tibetan,
            'literal': literal,
            'liturgical_tag': liturgical_tag,
            'liturgical': liturgical_text
        })
    
    return merged

def generate_review_prompt(chapter_num, chapter_title, merged_data):
    """Generate the review prompt for a chapter."""
    
    lines = []
    
    # Header
    lines.append("Conduct deep scan and critical honest review of the attached Tibetan Dzogchen translation in light of the literal and liturgical mission statements.")
    lines.append("")
    lines.append("If you have suggestions for specific lines return them in code block in the strict line format:")
    lines.append("")
    lines.append("[line number]<literal or liturgical><<liturgical tags if any>>replacement text")
    lines.append("")
    lines.append("(double line break)")
    lines.append("")
    lines.append("For each entry, eg.")
    lines.append("")
    lines.append("[684]<literal>buddhas-by-means-of dharma teach-and")
    lines.append("[725]<liturgical><prose>The antidote for the three poisons of desire, anger, and delusion is the realization of emptiness.")
    lines.append("")
    lines.append("=" * 60)
    lines.append("")
    
    # Mission statements
    lines.append(LITERAL_MISSION)
    lines.append("")
    lines.append("=" * 60)
    lines.append("")
    lines.append(LITURGICAL_MISSION)
    lines.append("")
    lines.append("=" * 60)
    lines.append("")
    
    # Draft to review
    lines.append("The draft in need of review is:")
    lines.append("")
    lines.append("# Treasury of the Supreme Vehicle: Autocommentary")
    lines.append("# Longchen Rabjampa (1308-1364)")
    lines.append(f"## Volume 01 - Chapter {int(chapter_num)} - Section 01")
    lines.append(f"## Chapter {int(chapter_num)}: {chapter_title}")
    lines.append("")
    
    # Output merged lines
    for item in merged_data:
        line_num = item['line']
        tibetan = item['tibetan']
        literal = item['literal']
        liturgical_tag = item['liturgical_tag']
        liturgical = item['liturgical']
        
        lines.append(f"[{line_num}]")
        lines.append(f"<tibetan>{tibetan}")
        
        if literal:
            lines.append(f"<literal>{literal}")
        
        if liturgical:
            if liturgical_tag:
                lines.append(f"<liturgical><{liturgical_tag}>{liturgical}")
            else:
                lines.append(f"<liturgical>{liturgical}")
        
        lines.append("")
    
    return "\n".join(lines)

# -----------------------------------------------------------------------------
# MAIN
# -----------------------------------------------------------------------------

def main():
    # Create output directory
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    print("Parsing contents...")
    chapters = parse_contents()
    
    if not chapters:
        print("Could not parse contents.md, using file-based chapter detection")
        # Fall back to detecting chapters from files
        chapters = []
        for i in range(1, 26):
            files = get_chapter_files(f"{i:02d}")
            if files:
                chapters.append({
                    'number': f"{i:02d}",
                    'title': f"Chapter {i}",
                    'volume': "01" if i <= 14 else "02",
                    'files': files
                })
    
    print(f"Found {len(chapters)} chapters")
    
    # Process each chapter
    for chapter in chapters:
        chapter_num = chapter['number']
        chapter_title = chapter['title']
        
        print(f"Processing Chapter {chapter_num}: {chapter_title}...")
        
        # Get files for this chapter
        files = get_chapter_files(chapter_num)
        
        if not files:
            print(f"  Warning: No files found for chapter {chapter_num}")
            continue
        
        # Get corresponding files in each layer
        tibetan_files = [f.replace('.txt', '.txt') for f in files]
        
        # Merge layers
        merged = merge_layers(files, files, files)
        
        if not merged:
            print(f"  Warning: No content merged for chapter {chapter_num}")
            continue
        
        # Generate prompt
        prompt = generate_review_prompt(chapter_num, chapter_title, merged)
        
        # Write output
        output_file = OUTPUT_DIR / f"chapter_{chapter_num}_review.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(prompt)
        
        print(f"  ✓ Wrote {output_file} ({len(merged)} lines)")
    
    print(f"\n✓ Complete! Generated {len(chapters)} review files in {OUTPUT_DIR}/")

if __name__ == "__main__":
    main()
