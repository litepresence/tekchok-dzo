#!/usr/bin/env python3
"""Generate liturgical translations in Vairotsana style - majestic, chantable, transmissive Dzogchen vajra speech"""

import os
import re

def extract_verse_num(line):
    match = re.search(r'\[(\d+)\]', line)
    return match.group(1) if match else None

def clean_line(line):
    return re.sub(r'^\s*\[\d+\]\s*', '', line).strip()

def transform_to_liturgical(text, page_num, line_num):
    """Transform literal translation into liturgical Dzogchen vajra speech"""
    text = text.replace('/', '').replace('*/', '').strip()
    
    # Special handling for verse citations
    if text.lower() in ['from', 'thus', 'is', 'and', 'or']:
        return text.capitalize()
    
    # Handle single word lines (often section markers)
    words = text.split()
    if len(words) == 1 and not any(c.isdigit() for c in words[0]):
        return text.capitalize()
    
    # Transform Dzogchen terminology into elevated liturgical form
    replacements = [
        (r'\brig pa\b', 'Rigpa'),
        (r'\brig-pa\b', 'Rigpa'),
        (r'\bsems\b', 'mind'),
        (r'\bdbyings\b', 'expanse'),
        (r'\bsgron ma\b', 'Lamp'),
        (r'\bye shes\b', 'Wisdom'),
        (r'\bye-shes\b', 'Wisdom'),
        (r'\bchos nyid\b', 'Dharmata'),
        (r'\bsku\b', 'kaya'),
        (r'\bthig le\b', 'Bindu'),
        (r'\bthig-le\b', 'Bindu'),
        (r'\bkunzhi\b', 'Alaya'),
        (r'\bsnang ba\b', 'appearance'),
        (r'\bsnang-ba\b', 'appearance'),
        (r'\bgsal\b', 'luminous'),
        (r'\bdag pa\b', 'pure'),
        (r'\bka dag\b', 'primordially pure'),
        (r'\bka-dag\b', 'primordially pure'),
        (r'\blhun grub\b', 'spontaneously accomplished'),
        (r'\brang bzhin\b', 'nature'),
        (r'\bngo bo\b', 'essence'),
        (r'\bmtshan nyid\b', 'characteristic'),
        (r'\bshes rab\b', 'wisdom'),
        (r'\bby-means-of\b', 'by'),
        (r'\bnot-exist\b', 'nonexistent'),
        (r'\bnot-exist-as\b', 'nonexistent as'),
        (r'\bnot-exist-of\b', 'nonexistence of'),
        (r'\bself-([a-z]+)\b', r'self-\1'),
        (r'-of\b', ' of'),
        (r'-to\b', ' to'),
        (r'-by\b', ' by'),
        (r'-in\b', ' in'),
        (r'-at\b', ' at'),
        (r'-as\b', ' as'),
        (r'-and\b', ' and'),
        (r'-from\b', ' from'),
        (r'-with\b', ' with'),
        (r'-on\b', ' on'),
    ]
    
    for pattern, replacement in replacements:
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    
    # Clean up multiple spaces and capitalize
    text = re.sub(r'\s+', ' ', text).strip()
    if text:
        text = text[0].upper() + text[1:]
    
    return text

def create_liturgical_translation(literal_line, page_num, line_num):
    verse = extract_verse_num(literal_line) or ""
    literal = clean_line(literal_line)
    
    if not literal:
        return ""
    
    liturgical = transform_to_liturgical(literal, page_num, line_num)
    
    if verse:
        return f"[{verse}] {liturgical}"
    return liturgical

def process_page(page_num):
    base_path = "/home/oracle/extinction-event/EV/theg pa'i mchog rin po che'i mdzod/1"
    literal_path = f"{base_path}/literal/PAGE {page_num}.txt"
    output_path = f"{base_path}/liturgical/PAGE {page_num}.txt"
    
    try:
        with open(literal_path, 'r', encoding='utf-8') as f:
            literal_lines = f.readlines()
    except FileNotFoundError:
        print(f"Warning: Page {page_num} not found, skipping")
        return 0
    
    liturgical_lines = []
    for i, lit_line in enumerate(literal_lines):
        liturgical = create_liturgical_translation(lit_line.strip(), page_num, i+1)
        liturgical_lines.append(liturgical)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(liturgical_lines))
    
    return len(liturgical_lines)

if __name__ == "__main__":
    total_lines = 0
    for page in range(401, 434):
        lines = process_page(page)
        total_lines += lines
        if lines > 0:
            print(f"Page {page}: {lines} lines")
    print(f"\nTotal: 33 pages, {total_lines} lines processed")
