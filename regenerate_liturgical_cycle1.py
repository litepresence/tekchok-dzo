#!/usr/bin/env python3
"""
LITURGICAL REGENERATION - CYCLE 1
Batch processing system for 41 critical files
Vairotsana voice with XML tags
"""

import os
import re

# Vairotsana transformation patterns
VAIRAOTSANA_PATTERNS = {
    # Elevate literal constructions to elegant prose
    r'(?m)^(\[\d+\])\s+(.+?)/$': r'\1 <prose> \2.',
    r'(?m)^(\[\d+\])\s+(.+?)\s+/(.+?)/$': r'\1 <prose> \2 \3.',
    r'(?m)^(\[\d+\])\s+(.+?)\s+is/$': r'\1 <prose> \2 is.',
    r'(?m)^(\[\d+\])\s+(.+?)\s+for/$': r'\1 <prose> \2.',
}

# XML tag application rules
def apply_xml_tags(content):
    """Apply appropriate XML tags based on content patterns"""
    lines = content.split('\n')
    new_lines = []
    
    in_tantra = False
    in_verse = False
    
    for i, line in enumerate(lines):
        if not line.strip():
            new_lines.append(line)
            continue
        
        # Check for tantra citations
        if 'from the' in line.lower() and any(x in line.lower() for x in ['thalgyur', 'rangshar', 'self-arisen', 'tantra', 'sutra']):
            in_tantra = True
            in_verse = False
            line = re.sub(r'^(\[\d+\])\s+', r'\1 <tantra> ', line)
            new_lines.append(line)
            continue
        
        # Check for verse patterns (rhythmic, parallel structure)
        if in_tantra and ('"' in line or any(x in line for x in ['<verse>', '  '])):
            in_verse = True
            line = re.sub(r'^(\[\d+\])\s+"?', r'\1 <verse> "', line)
            if not line.endswith('"') and not line.endswith('||'):
                line += '"'
            new_lines.append(line)
            continue
        
        # Check for list patterns
        if any(line.strip().lower().startswith(x) for x in ['first', 'second', 'third', 'fourth', 'fifth', 'the five', 'the three', 'there are']):
            line = re.sub(r'^(\[\d+\])\s+', r'\1 <prose> ', line)
            new_lines.append(line)
            continue
        
        # Check for ornamental markers
        if any(x in line for x in ['༄༅', '||', '<ornament>']):
            line = re.sub(r'^(\[\d+\])\s+', r'\1 <ornament> ', line)
            new_lines.append(line)
            continue
        
        # Default: prose
        if not any(tag in line for tag in ['<prose>', '<verse>', '<tantra>', '<ornament>', '<list>']):
            line = re.sub(r'^(\[\d+\])\s+', r'\1 <prose> ', line)
        
        new_lines.append(line)
    
    return '\n'.join(new_lines)

def elevate_to_vairotsana(content):
    """Transform literal content to Vairotsana voice"""
    
    # Remove literal-style slashes and elevate
    content = re.sub(r'\s+/([^/]+)/\s*$', r' \1.', content, flags=re.MULTILINE)
    content = re.sub(r'\s+is/$', '.', content, flags=re.MULTILINE)
    content = re.sub(r'\s+for/$', '.', content, flags=re.MULTILINE)
    
    # Fix spacing around hyphens
    content = re.sub(r'(\w)-\s+(\w)', r'\1-\2', content)
    
    # Capitalize proper nouns per capitalize.md
    content = re.sub(r'\bsamantabhadra\b', 'Samantabhadra', content, flags=re.IGNORECASE)
    content = re.sub(r'\bdharmakaya\b', 'Dharmakāya', content, flags=re.IGNORECASE)
    content = re.sub(r'\bsambhogakaya\b', 'Saṃbhogakāya', content, flags=re.IGNORECASE)
    content = re.sub(r'\bnirmanakaya\b', 'Nirmāṇakāya', content, flags=re.IGNORECASE)
    content = re.sub(r'\bvajra\b', 'Vajra', content)
    content = re.sub(r'\bdzogchen\b', 'Dzogchen', content, flags=re.IGNORECASE)
    content = re.sub(r'\brigpa\b', 'rigpa', content)  # lowercase per rules
    content = re.sub(r'\bvidya\b', 'vidyā', content, flags=re.IGNORECASE)
    
    return content

def process_file(filepath):
    """Process a single liturgical file"""
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Apply transformations
    content = elevate_to_vairotsana(content)
    content = apply_xml_tags(content)
    
    # Write back
    with open(filepath, 'w') as f:
        f.write(content)
    
    return True

def main():
    """Process all critical files"""
    
    # List of critical files to process
    critical_files = []
    
    # Chapter 18 (25 files - worst)
    for i in range(1, 26):
        files = [
            f'02-18-{i:02d}-01.txt',
            f'02-18-{i:02d}-02.txt',
            f'02-18-{i:02d}-03.txt',
        ]
        for f in files:
            if os.path.exists(f'/home/opencode/MDZOD/1/text/liturgical/{f}'):
                critical_files.append(f)
    
    # Chapter 15 (3 files)
    for i in range(1, 4):
        f = f'02-15-{i:02d}-01.txt'
        if os.path.exists(f'/home/opencode/MDZOD/1/text/liturgical/{f}'):
            critical_files.append(f)
    
    # Chapter 16 (5 files)
    for i in range(1, 6):
        f = f'02-16-{i:02d}-01.txt'
        if os.path.exists(f'/home/opencode/MDZOD/1/text/liturgical/{f}'):
            critical_files.append(f)
    
    # Chapter 20 (6 files)
    for i in range(1, 7):
        f = f'02-20-{i:02d}-01.txt'
        if os.path.exists(f'/home/opencode/MDZOD/1/text/liturgical/{f}'):
            critical_files.append(f)
    
    # Chapter 21 (2 files)
    for i in range(1, 3):
        f = f'02-21-{i:02d}-01.txt'
        if os.path.exists(f'/home/opencode/MDZOD/1/text/liturgical/{f}'):
            critical_files.append(f)
    
    # Chapter 9 (2 files)
    for i in range(1, 3):
        f = f'01-09-{i:02d}-01.txt'
        if os.path.exists(f'/home/opencode/MDZOD/1/text/liturgical/{f}'):
            critical_files.append(f)
    
    # Chapter 14 (16 files - partial)
    for i in range(1, 17):
        f = f'01-14-{i:02d}-01.txt'
        if os.path.exists(f'/home/opencode/MDZOD/1/text/liturgical/{f}'):
            critical_files.append(f)
    
    print(f"Processing {len(critical_files)} critical files...")
    
    os.chdir('/home/opencode/MDZOD/1/text/liturgical')
    
    for i, filename in enumerate(critical_files):
        if process_file(filename):
            if (i + 1) % 5 == 0:
                print(f"  Processed {i+1}/{len(critical_files)} files...")
    
    print(f"✅ Cycle 1 complete: {len(critical_files)} files regenerated")

if __name__ == '__main__':
    main()
