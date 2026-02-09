#!/usr/bin/env python3
"""
Content Extraction Script v3 - FIXED
- Handles line ranges [1-4] for commentary layers
- Maps liturgical to Tibetan line numbers dynamically
- Fixes boundary overlap bug
- No zero padding on line numbers
"""

import json
import os
import re
from pathlib import Path

LAYERS = ['tibetan', 'wylie', 'literal', 'liturgical', 
          'commentary', 'scholar', 'epistemic', 'delusion', 'cognitive']

# Layers that use individual line numbers
INDIVIDUAL_LINE_LAYERS = ['tibetan', 'wylie', 'literal', 'liturgical']

# Layers that use range notation
RANGE_LAYERS = ['commentary', 'scholar', 'epistemic', 'delusion', 'cognitive']

def load_boundary_json():
    with open('boundary.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def get_layer_path(volume, layer, chapter, section_id):
    if volume == 1:
        base_dir = 'partitioned_v1'
    else:
        base_dir = 'partitioned_v2'
    chapter_str = f"chapter_{chapter:02d}"
    filename = f"section_{section_id}.txt"
    return Path(base_dir) / layer / chapter_str / filename

def read_page_file(volume, layer, page_num):
    if volume == 1:
        page_dir = 'volume_1'
    else:
        page_dir = 'volume_2'
    page_file = Path(page_dir) / layer / f"PAGE_{page_num:03d}.txt"
    if not page_file.exists():
        return None
    with open(page_file, 'r', encoding='utf-8') as f:
        return f.readlines()

def parse_line_number(line):
    """Parse line number in various formats. Returns dict with all info."""
    line = line.strip()
    
    # Try single number: [4417]
    match = re.match(r'\[(\d+)\]\s*(.*)', line)
    if match:
        return {
            'line_num': int(match.group(1)),
            'content': match.group(2),
            'format': 'single',
            'range_start': None,
            'range_end': None
        }
    
    # Try range: [1-4] or [001-004]
    match = re.match(r'\[(\d+)-(\d+)\]\s*(.*)', line)
    if match:
        start = int(match.group(1))
        end = int(match.group(2))
        return {
            'line_num': end,  # Use END of range for positioning
            'content': match.group(3),
            'format': 'range',
            'range_start': start,
            'range_end': end
        }
    
    return None

def get_last_line_on_page(page_lines):
    """Get the last line number on a page."""
    for line in reversed(page_lines):
        parsed = parse_line_number(line)
        if parsed and parsed['line_num'] is not None:
            return parsed['line_num']
    return None

def extract_section_content_fixed(volume, layer, start_page, start_line, end_page, end_line, tibetan_ref=None):
    """
    Extract content with proper boundary handling.
    
    Fixes:
    1. Respects end_line even on pages before end_page (fixes overlap bug)
    2. Handles liturgical line mapping using tibetan_ref
    3. Handles range notation for commentary layers
    """
    content_lines = []
    current_page = start_page
    
    # For liturgical layer, read corresponding Tibetan page for line numbers
    if layer == 'liturgical' and tibetan_ref:
        tibetan_lines = read_page_file(volume, 'tibetan', current_page)
        tibetan_line_nums = []
        if tibetan_lines:
            for line in tibetan_lines:
                parsed = parse_line_number(line)
                if parsed and parsed['line_num'] is not None:
                    tibetan_line_nums.append(parsed['line_num'])
    else:
        tibetan_line_nums = None
    
    while current_page <= end_page:
        page_lines = read_page_file(volume, layer, current_page)
        
        if page_lines is None or not page_lines:
            current_page += 1
            # Refresh Tibetan reference for next page
            if layer == 'liturgical' and tibetan_ref:
                tibetan_lines = read_page_file(volume, 'tibetan', current_page)
                if tibetan_lines:
                    tibetan_line_nums = []
                    for line in tibetan_lines:
                        parsed = parse_line_number(line)
                        if parsed and parsed['line_num'] is not None:
                            tibetan_line_nums.append(parsed['line_num'])
                else:
                    tibetan_line_nums = []
            continue
        
        # Determine extraction boundaries for this page
        if current_page == start_page:
            extract_from = start_line
        else:
            extract_from = 1
        
        # FIX: Check if this page has lines beyond end_line (even if not end_page)
        if current_page == end_page:
            extract_to = end_line
        else:
            # Check if this page extends beyond end_line
            page_last_line = get_last_line_on_page(page_lines)
            if page_last_line is not None and page_last_line >= end_line:
                # This page contains lines that belong to next section
                extract_to = end_line
            else:
                extract_to = float('inf')
        
        # Process lines from this page
        page_content = []
        tibetan_idx = 0
        
        for line in page_lines:
            # Skip Patrul Rinpoche signature lines in commentary layers
            if layer in RANGE_LAYERS:
                stripped = line.strip()
                if stripped.startswith('—Patrul') or stripped.startswith('--Patrul') or stripped.startswith('COMMENTARY ON PAGE'):
                    continue
            
            parsed = parse_line_number(line)
            
            if parsed is None:
                # No line number in source - handle specially
                if layer == 'liturgical' and tibetan_line_nums and tibetan_idx < len(tibetan_line_nums):
                    # Map to Tibetan line number
                    line_content = line.strip()
                    # Skip blank lines in liturgical source
                    if not line_content:
                        tibetan_idx += 1
                        continue
                    line_num = tibetan_line_nums[tibetan_idx]
                    tibetan_idx += 1
                else:
                    continue
            else:
                # Use the line number from source
                line_num = parsed['line_num']
                line_content = parsed['content']
                
                # Skip lines with empty content (like [433] with nothing after)
                if not line_content.strip():
                    continue
                if layer == 'liturgical' and tibetan_line_nums:
                    tibetan_idx += 1
            
            # Check if this line should be included
            if line_num < extract_from:
                continue
            if line_num > extract_to:
                break
            
            # Format output based on layer type
            if layer in INDIVIDUAL_LINE_LAYERS:
                formatted_line = f"[{line_num}] {line_content}"
                page_content.append(formatted_line)
            elif layer in RANGE_LAYERS and parsed and parsed['format'] == 'range':
                # Preserve range format, no zero padding
                range_start = parsed['range_start'] if parsed['range_start'] else line_num
                range_end = parsed['range_end'] if parsed['range_end'] else line_num
                formatted_line = f"[{range_start}-{range_end}] {line_content}"
                page_content.append(formatted_line)
            else:
                # Default to single format
                formatted_line = f"[{line_num}] {line_content}"
                page_content.append(formatted_line)
        
        # Add FOLIO marker for Tibetan layer at top of each page's content
        if layer == 'tibetan' and page_content:
            # Special case: FOLIO_001 at very beginning
            if volume == 1 and current_page == 1 and not content_lines:
                content_lines.append(f"FOLIO_{current_page:03d}")
                content_lines.append("")
            elif current_page > start_page:
                # Page transition within section
                content_lines.append("")
                content_lines.append(f"FOLIO_{current_page:03d}")
                content_lines.append("")
        
        content_lines.extend(page_content)
        current_page += 1
        
        # Refresh Tibetan reference for next page
        if layer == 'liturgical' and tibetan_ref:
            tibetan_lines = read_page_file(volume, 'tibetan', current_page)
            if tibetan_lines:
                tibetan_line_nums = []
                for line in tibetan_lines:
                    parsed = parse_line_number(line)
                    if parsed and parsed['line_num'] is not None:
                        tibetan_line_nums.append(parsed['line_num'])
            else:
                tibetan_line_nums = []
    
    return '\n'.join(content_lines)

def process_section(volume_data, chapter_data, section_data, layer):
    """Process a single section for a given layer."""
    volume_num = volume_data['volume_number']
    chapter_num = chapter_data['chapter_number']
    section_id = section_data['section_id']
    
    start_page = section_data['boundary_start']['page']
    start_line = section_data['boundary_start']['line']
    
    # Calculate end boundary from next section
    sections = chapter_data['sections']
    section_idx = None
    for idx, sec in enumerate(sections):
        if sec['section_id'] == section_id:
            section_idx = idx
            break
    
    if section_idx is not None and section_idx < len(sections) - 1:
        next_section = sections[section_idx + 1]
        end_page = next_section['boundary_start']['page']
        end_line = next_section['boundary_start']['line'] - 1
    else:
        # Last section in chapter
        end_page = section_data['pages']['end']
        # Find actual last line
        page_lines = read_page_file(volume_num, layer, end_page)
        if page_lines:
            end_line = get_last_line_on_page(page_lines)
            if end_line is None:
                end_line = 99999
        else:
            end_line = 99999
    
    # For liturgical, use Tibetan as reference for line numbers
    tibetan_ref = (layer == 'liturgical')
    
    content = extract_section_content_fixed(
        volume_num, layer, 
        start_page, start_line, 
        end_page, end_line,
        tibetan_ref=tibetan_ref
    )
    
    return content

def main():
    print("=" * 60)
    print("CONTENT EXTRACTION v3 - FIXED")
    print("Handles ranges, liturgical mapping, boundary overlaps")
    print("=" * 60)
    print()
    
    print("Loading boundary.json...")
    boundary_data = load_boundary_json()
    print(f"  Loaded {len(boundary_data['volumes'])} volumes")
    print()
    
    total_sections = 0
    skipped_empty = 0
    
    for layer in LAYERS:
        print(f"Processing layer: {layer}")
        print("-" * 60)
        
        layer_sections = 0
        layer_skipped = 0
        
        for volume_data in boundary_data['volumes']:
            volume_num = volume_data['volume_number']
            
            for chapter_data in volume_data['chapters']:
                chapter_num = chapter_data['chapter_number']
                
                for section_data in chapter_data['sections']:
                    section_id = section_data['section_id']
                    
                    content = process_section(volume_data, chapter_data, section_data, layer)
                    
                    output_path = get_layer_path(volume_num, layer, chapter_num, section_id)
                    output_path.parent.mkdir(parents=True, exist_ok=True)
                    
                    with open(output_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    if not content.strip():
                        layer_skipped += 1
                    
                    layer_sections += 1
                    
                    if layer_sections % 10 == 0:
                        print(f"  Progress: {layer_sections} sections...", end='\r')
        
        if layer_skipped > 0:
            print(f"  ✓ Extracted {layer_sections} sections ({layer_skipped} empty)")
        else:
            print(f"  ✓ Extracted {layer_sections} sections")
        print()
        total_sections += layer_sections
        skipped_empty += layer_skipped
    
    print("=" * 60)
    print("EXTRACTION COMPLETE")
    print("=" * 60)
    print(f"Total sections extracted: {total_sections}")
    if skipped_empty > 0:
        print(f"Empty sections (no source content): {skipped_empty}")
    print(f"Layers processed: {len(LAYERS)}")

if __name__ == "__main__":
    main()
