#!/usr/bin/env python3
"""
Verify all start phrases in boundary_v3.json against source Tibetan text.
Generates verified.json with True/False for each section.
"""

import json
import os
import re
from pathlib import Path

def get_source_file(page_num, chapter=None):
    """Get the source file path for a given page number.
    
    Page numbers in boundary_v3.json are relative to each volume:
    - Volume 1: Chapters 1-14, pages 1-479
    - Volume 2: Chapters 15-25, pages 1-415
    """
    if chapter is not None and chapter >= 15:
        vol = 2
    elif page_num > 479:
        # Absolute page number (shouldn't happen with current data)
        vol = 2
        page_num = page_num - 479
    else:
        vol = 1
    
    return f"/home/opencode/MDZOD/1/volume_{vol}/tibetan/PAGE_{page_num:03d}.txt"

def read_page(page_num, chapter=None):
    """Read a page file and return list of (line_num, text) tuples."""
    filepath = get_source_file(page_num, chapter)
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        result = []
        for line in lines:
            line = line.strip()
            if not line:
                continue
            # Parse [NNN] format
            match = re.match(r'\[(\d+)\]\s*(.*)', line)
            if match:
                line_num = int(match.group(1))
                text = match.group(2)
                result.append((line_num, text))
        return result
    except FileNotFoundError:
        print(f"ERROR: File not found: {filepath}")
        return []

def find_phrase(page_num, line_num, phrase, chapter=None):
    """Look for a phrase starting at a specific line in a page."""
    lines = read_page(page_num, chapter)
    
    # Create a dictionary for quick lookup
    line_dict = {ln: text for ln, text in lines}
    
    # Check if the line exists
    if line_num not in line_dict:
        vol = 2 if chapter and chapter >= 15 else 1
        return False, f"Line {line_num} not found in page {page_num} (vol {vol})"
    
    # Get the text at that line
    text = line_dict[line_num]
    
    # Clean both phrase and text for comparison
    # Remove leading punctuation from phrase for matching
    clean_phrase = phrase.lstrip('།')
    clean_text = text.lstrip('།')
    
    # Check if phrase is at the start of the text
    if clean_text.startswith(clean_phrase):
        return True, "Found at line start"
    
    # Also try with full phrase
    if text.startswith(phrase):
        return True, "Found at line start (exact)"
    
    # Try searching within the line
    if clean_phrase in clean_text:
        return True, "Found within line"
    
    # Try without tsek (་) at end
    if clean_phrase.rstrip('་') in clean_text:
        return True, "Found (without final tsek)"
    
    vol = 2 if chapter and chapter >= 15 else 1
    return False, f"Not found. Text at line {line_num} (vol {vol}): {text[:100]}"

def main():
    print("=" * 80)
    print("BOUNDARY VERIFICATION SCRIPT")
    print("=" * 80)
    
    # Load boundary file
    with open('/home/opencode/MDZOD/1/boundary_v3.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    results = {}
    failures = []
    
    total = len(data['sections'])
    print(f"\nVerifying {total} sections...\n")
    
    for idx, (key, section) in enumerate(sorted(data['sections'].items()), 1):
        page = section['start_page']
        line = section['start_line']
        phrase = section['start_phrase']
        chapter = section['chapter']
        
        found, message = find_phrase(page, line, phrase, chapter)
        results[key] = found
        
        if not found:
            failures.append({
                'key': key,
                'page': page,
                'line': line,
                'phrase': phrase[:100],
                'message': message
            })
            print(f"✗ {key}: {message}")
        elif idx % 50 == 0:
            print(f"  Progress: {idx}/{total} sections checked...")
    
    # Save results
    with open('/home/opencode/MDZOD/1/verified.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print("\n" + "=" * 80)
    print("VERIFICATION SUMMARY")
    print("=" * 80)
    print(f"\nTotal sections: {total}")
    print(f"Found: {sum(results.values())}")
    print(f"Failed: {len(failures)}")
    
    if failures:
        print(f"\nFailed sections ({len(failures)}):")
        for f in failures[:10]:
            print(f"  - {f['key']}: Page {f['page']}, Line {f['line']}")
            print(f"    Phrase: {f['phrase'][:60]}...")
            print(f"    Reason: {f['message'][:80]}")
        if len(failures) > 10:
            print(f"    ... and {len(failures) - 10} more")
    
    print(f"\nResults saved to verified.json")
    
    return len(failures) == 0

if __name__ == '__main__':
    success = main()
    exit(0 if success else 1)
