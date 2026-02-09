#!/usr/bin/env python3
"""
Content Extraction Script v4 - PERFECT PRESERVATION
- Preserves exact content
- Adds FOLIO markers to Tibetan only
- Maps liturgical to Tibetan line numbers 1:1
- Preserves range format [1-4] for commentary layers
- Removes blank lines
- Filters Patrul Rinpoche signatures
"""

import json
import re
from pathlib import Path

LAYERS = ['tibetan', 'wylie', 'literal', 'liturgical', 
          'commentary', 'scholar', 'epistemic', 'delusion', 'cognitive']

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

def read_page_file_raw(volume, layer, page_num):
    """Read entire file as raw string."""
    if volume == 1:
        page_dir = 'volume_1'
    else:
        page_dir = 'volume_2'
    page_file = Path(page_dir) / layer / f"PAGE_{page_num:03d}.txt"
    if not page_file.exists():
        return None
    with open(page_file, 'r', encoding='utf-8') as f:
        return f.read()

def get_line_number(line):
    """Extract line number from a line if present. Returns (num, is_range, range_start, range_end)."""
    stripped = line.strip()
    # Single number: [4417]
    match = re.match(r'\[(\d+)\]\s*(.*)', stripped)
    if match:
        return (int(match.group(1)), False, None, None, match.group(2))
    # Range: [1-4]
    match = re.match(r'\[(\d+)-(\d+)\]\s*(.*)', stripped)
    if match:
        start = int(match.group(1))
        end = int(match.group(2))
        return (end, True, start, end, match.group(3))
    return (None, False, None, None, stripped)

def is_patrul_signature(line):
    """Check if line is a Patrul Rinpoche signature."""
    stripped = line.strip()
    return (stripped.startswith('—Patrul') or 
            stripped.startswith('--Patrul') or
            stripped.startswith('COMMENTARY ON PAGE'))

def extract_section_content(volume, layer, start_page, start_line, end_page, end_line):
    """
    Extract section content with perfect preservation.
    """
    content_lines = []  # Will store tuples of (line_num, content, is_range, range_start, range_end)
    current_page = start_page
    first_page = True
    
    # For liturgical, get Tibetan line numbers as reference
    tibetan_line_nums = []
    if layer == 'liturgical':
        page = start_page
        while page <= end_page:
            tibetan_content = read_page_file_raw(volume, 'tibetan', page)
            if tibetan_content:
                for line in tibetan_content.split('\n'):
                    num, _, _, _, _ = get_line_number(line)
                    if num:
                        tibetan_line_nums.append(num)
            page += 1
    
    tibetan_idx = 0
    
    while current_page <= end_page:
        page_content = read_page_file_raw(volume, layer, current_page)
        
        if page_content is None:
            current_page += 1
            continue
        
        lines = page_content.split('\n')
        
        for line in lines:
            stripped = line.strip()
            
            # Skip blank lines
            if not stripped:
                continue
            
            # Skip Patrul signatures for commentary layers
            if layer in ['commentary', 'scholar', 'epistemic', 'delusion', 'cognitive']:
                if is_patrul_signature(line):
                    continue
            
            line_num, is_range, range_start, range_end, content = get_line_number(line)
            
            # For liturgical without line numbers, map to Tibetan
            if layer == 'liturgical' and line_num is None:
                if tibetan_idx < len(tibetan_line_nums):
                    line_num = tibetan_line_nums[tibetan_idx]
                    content = stripped
                    tibetan_idx += 1
                else:
                    continue
            elif layer == 'liturgical':
                tibetan_idx += 1
            
            # Determine if this line should be included based on boundaries
            if line_num is not None:
                if current_page == start_page and current_page == end_page:
                    # Single page
                    if not (start_line <= line_num <= end_line):
                        continue
                elif current_page == start_page:
                    # First page
                    if line_num < start_line:
                        continue
                elif current_page == end_page:
                    # Last page
                    if line_num > end_line:
                        continue
            
            # Add to content
            content_lines.append((line_num, content, is_range, range_start, range_end))
        
        current_page += 1
    
    # Format output
    output_lines = []
    first_output = True
    prev_page = None
    
    for line_num, content, is_range, range_start, range_end in content_lines:
        # Add FOLIO marker for Tibetan layer at page transitions
        if layer == 'tibetan' and line_num is not None:
            # Determine which page this line belongs to
            # This is an approximation - FOLIO markers go at start of each new page
            pass  # We'll handle FOLIO differently below
        
        # Format the line
        if is_range and range_start is not None:
            formatted = f"[{range_start}-{range_end}] {content}"
        elif line_num is not None:
            formatted = f"[{line_num}] {content}"
        else:
            formatted = content
        
        output_lines.append(formatted)
    
    return '\n'.join(output_lines)

def extract_section_with_folio(volume, layer, start_page, start_line, end_page, end_line):
    """Extract with FOLIO markers for Tibetan layer."""
    if layer != 'tibetan':
        return extract_section_content(volume, layer, start_page, start_line, end_page, end_line)
    
    # For Tibetan, add FOLIO markers at page transitions
    content_parts = []
    current_page = start_page
    first_page = True
    
    while current_page <= end_page:
        page_content = read_page_file_raw(volume, layer, current_page)
        
        if page_content is None:
            current_page += 1
            continue
        
        # Get lines in range for this page
        lines = page_content.split('\n')
        selected_lines = []
        
        for line in lines:
            stripped = line.strip()
            if not stripped:
                continue
            
            line_num, is_range, range_start, range_end, content = get_line_number(line)
            
            if line_num is not None:
                if current_page == start_page and current_page == end_page:
                    if not (start_line <= line_num <= end_line):
                        continue
                elif current_page == start_page:
                    if line_num < start_line:
                        continue
                elif current_page == end_page:
                    if line_num > end_line:
                        continue
            
            # Format
            if is_range and range_start is not None:
                formatted = f"[{range_start}-{range_end}] {content}"
            elif line_num is not None:
                formatted = f"[{line_num}] {content}"
            else:
                formatted = content
            
            selected_lines.append(formatted)
        
        if selected_lines:
            # Add FOLIO marker at the start of each page's content
            if first_page:
                # First page of section - add FOLIO marker with trailing blank line
                content_parts.append(f"FOLIO_{current_page:03d}")
                content_parts.append("")  # Blank line after FOLIO
                first_page = False
            else:
                # Subsequent pages - add FOLIO with blank line after
                content_parts.append(f"FOLIO_{current_page:03d}")
                content_parts.append("")  # Blank line after FOLIO
            
            content_parts.append('\n'.join(selected_lines))
        
        current_page += 1
    
    return '\n'.join(content_parts)

def process_section(volume_data, chapter_data, section_data, layer):
    """Process a single section."""
    volume_num = volume_data['volume_number']
    chapter_num = chapter_data['chapter_number']
    section_id = section_data['section_id']
    
    start_page = section_data['boundary_start']['page']
    start_line = section_data['boundary_start']['line']
    
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
        end_page = section_data['pages']['end']
        page_content = read_page_file_raw(volume_num, layer, end_page)
        if page_content:
            lines = page_content.split('\n')
            end_line = 0
            for line in reversed(lines):
                num, _, _, _, _ = get_line_number(line)
                if num:
                    end_line = num
                    break
            if end_line == 0:
                end_line = 99999
        else:
            end_line = 99999
    
    if layer == 'tibetan':
        return extract_section_with_folio(volume_num, layer, start_page, start_line, end_page, end_line)
    else:
        return extract_section_content(volume_num, layer, start_page, start_line, end_page, end_line)

def main():
    print("=" * 60)
    print("CONTENT EXTRACTION v4 - PERFECT PRESERVATION")
    print("=" * 60)
    print()
    
    print("Loading boundary.json...")
    boundary_data = load_boundary_json()
    print(f"  Loaded {len(boundary_data['volumes'])} volumes")
    print()
    
    total_sections = 0
    
    for layer in LAYERS:
        print(f"Processing layer: {layer}")
        print("-" * 60)
        
        layer_sections = 0
        
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
                    
                    layer_sections += 1
                    
                    if layer_sections % 10 == 0:
                        print(f"  Progress: {layer_sections} sections...", end='\r')
        
        print(f"  ✓ Extracted {layer_sections} sections")
        print()
        total_sections += layer_sections
    
    print("=" * 60)
    print("EXTRACTION COMPLETE")
    print("=" * 60)
    print(f"Total sections extracted: {total_sections}")
    print(f"Layers processed: {len(LAYERS)}")

if __name__ == "__main__":
    main()
