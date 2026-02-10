#!/usr/bin/env python3
"""
Repair content summaries in boundary_v3.json by reading actual source text.
Replaces short/generic summaries with meaningful content from the Tibetan text.
"""

import json
import re
import os

def get_source_file(page_num, chapter):
    """Get the source file path for a given page and chapter."""
    vol = 1 if chapter <= 14 else 2
    return f"/home/opencode/MDZOD/1/volume_{vol}/tibetan/PAGE_{page_num:03d}.txt"

def read_page_lines(page_num, chapter):
    """Read a page and return dict of line_num -> text."""
    filepath = get_source_file(page_num, chapter)
    lines_dict = {}
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                match = re.match(r'\[(\d+)\]\s*(.*)', line)
                if match:
                    line_num = int(match.group(1))
                    text = match.group(2)
                    lines_dict[line_num] = text
    except FileNotFoundError:
        print(f"Warning: File not found: {filepath}")
    
    return lines_dict

def extract_content_from_source(page_num, line_num, chapter, max_chars=100):
    """Extract content from source file starting at given line."""
    lines = read_page_lines(page_num, chapter)
    
    if line_num not in lines:
        return None
    
    # Get the starting line
    text = lines[line_num]
    
    # If it's very short, try to get next line too
    if len(text) < 30 and (line_num + 1) in lines:
        text += " " + lines[line_num + 1]
    
    # Clean up the text
    text = text.strip()
    
    # Remove leading punctuation
    text = re.sub(r'^[།༄༅\s]+', '', text)
    
    # Truncate to max_chars but at a word boundary
    if len(text) > max_chars:
        # Find last space before max_chars
        truncated = text[:max_chars]
        last_space = truncated.rfind('་')
        if last_space > max_chars * 0.7:  # Only truncate if we found a reasonable break
            text = truncated[:last_space + 1]
        else:
            text = truncated
    
    return text

def is_generic_summary(summary):
    """Check if summary is just a generic ordinal marker."""
    generic_patterns = [
        r'^དང་པོ་\s*ནི།$',
        r'^གཉིས་པ་\s*ནི།$',
        r'^གསུམ་པ་\s*ནི།$',
        r'^བཞི་པ་\s*ནི།$',
        r'^ལྔ་པ་\s*ནི།$',
        r'^དྲུག་པ་\s*ནི།$',
        r'^བདུན་པ་\s*ནི།$',
        r'^བརྒྱད་པ་\s*ནི།$',
        r'^དགུ་པ་\s*ནི།$',
        r'^བཅུ་པ་\s*ནི།$',
        r'^དང་པོ་\s*\S+\s*ནི།$',  # e.g., "དང་པོ་ཕྱི་ནི།"
        r'^དང་པོ་\s*\S+\s*སྟེ།$',  # e.g., "དང་པོ་དགའ་བ་སྟེ།"
    ]
    
    for pattern in generic_patterns:
        if re.match(pattern, summary.strip()):
            return True
    
    # Also check if summary is just the start phrase or too short
    if len(summary) < 25:
        return True
    
    return False

def main():
    print("=" * 80)
    print("CONTENT SUMMARY REPAIR SCRIPT")
    print("=" * 80)
    
    # Load boundary
    with open('/home/opencode/MDZOD/1/boundary_v3.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Find sections needing repair
    sections_to_repair = []
    for key, section in data['sections'].items():
        cs = section.get('content_summary', '')
        if is_generic_summary(cs):
            sections_to_repair.append({
                'key': key,
                'current': cs,
                'page': section['start_page'],
                'line': section['start_line'],
                'chapter': section['chapter']
            })
    
    print(f"\nFound {len(sections_to_repair)} sections with generic/short summaries")
    
    if not sections_to_repair:
        print("✓ No repairs needed")
        return True
    
    # Repair each section
    repaired_count = 0
    failed_count = 0
    
    print("\nRepairing...")
    for item in sections_to_repair:
        key = item['key']
        section = data['sections'][key]
        
        # Extract better content from source
        new_summary = extract_content_from_source(
            item['page'], 
            item['line'], 
            item['chapter'],
            max_chars=80
        )
        
        if new_summary and len(new_summary) > len(item['current']):
            section['content_summary'] = new_summary
            repaired_count += 1
            if repaired_count <= 5:
                print(f"  ✓ {key}: '{item['current']}' -> '{new_summary[:50]}...'")
        else:
            # If extraction failed, use start_phrase
            start_phrase = section.get('start_phrase', '')
            if len(start_phrase) > len(item['current']):
                section['content_summary'] = start_phrase[:80]
                repaired_count += 1
                if repaired_count <= 5:
                    print(f"  ✓ {key}: Used start_phrase")
            else:
                failed_count += 1
    
    print(f"\n{'=' * 80}")
    print(f"Repaired: {repaired_count}")
    print(f"Failed: {failed_count}")
    
    # Update metadata date
    data['metadata']['created_date'] = '2026-02-10'
    data['metadata']['last_repaired'] = '2026-02-10'
    print(f"✓ Updated metadata dates")
    
    # Save
    with open('/home/opencode/MDZOD/1/boundary_v3.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"✓ Saved boundary_v3.json")
    
    # Verify repairs
    print(f"\n{'=' * 80}")
    print("VERIFICATION")
    print(f"{'=' * 80}")
    
    still_short = 0
    for key, section in data['sections'].items():
        cs = section.get('content_summary', '')
        if is_generic_summary(cs):
            still_short += 1
    
    if still_short == 0:
        print(f"✓ All content summaries now have meaningful content")
    else:
        print(f"⚠️  {still_short} sections still have generic summaries")
        print("  (These may be sections where source text starts with just ordinal markers)")
    
    return True

if __name__ == '__main__':
    success = main()
    exit(0 if success else 1)
