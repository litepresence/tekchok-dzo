#!/usr/bin/env python3
"""
Content Extraction Script v2 - Phase 2 (FIXED)
Preserves line numbers and inserts FOLIO markers at TOP of every page (Tibetan layer only)
"""

import json
import os
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

def parse_line(line):
    match = re.match(r'\[(\d+)\]\s*(.*)', line.strip())
    if match:
        return int(match.group(1)), match.group(2)
    return None, line.strip()

def extract_section_content(volume, layer, start_page, start_line, end_page, end_line):
    """
    Extract content with line numbers preserved.
    For Tibetan layer: Insert FOLIO_ marker at TOP of EVERY page (with blank lines around).
    """
    content_lines = []
    current_page = start_page
    
    while current_page <= end_page:
        page_lines = read_page_file(volume, layer, current_page)
        
        # Skip if page doesn't exist (for commentary layers that may not have content yet)
        if page_lines is None:
            current_page += 1
            continue
        
        if not page_lines:
            current_page += 1
            continue
        
        # Determine line range for this page
        if current_page == start_page:
            extract_from = start_line
        else:
            extract_from = 1
        
        if current_page == end_page:
            extract_to = end_line
        else:
            extract_to = float('inf')
        
        # Extract lines from this page
        page_content = []
        for line in page_lines:
            line_num, line_content = parse_line(line)
            
            if line_num is None:
                continue
            
            if line_num < extract_from:
                continue
            if line_num > extract_to:
                break
            
            formatted_line = f"[{line_num}] {line_content}"
            page_content.append(formatted_line)
        
        # Add FOLIO marker for Tibetan layer at the TOP of each page's content
        if layer == 'tibetan' and page_content:
            # Add blank line before FOLIO (except at very beginning)
            if content_lines:
                content_lines.append("")
            content_lines.append(f"FOLIO_{current_page:03d}")
            content_lines.append("")  # Blank line after FOLIO
        
        # Add the page content
        content_lines.extend(page_content)
        
        current_page += 1
    
    return '\n'.join(content_lines)

def process_section(volume_data, chapter_data, section_data, layer):
    """Process a single section for a given layer."""
    volume_num = volume_data['volume_number']
    chapter_num = chapter_data['chapter_number']
    section_id = section_data['section_id']
    
    start_page = section_data['boundary_start']['page']
    start_line = section_data['boundary_start']['line']
    
    # Find end boundary
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
        # Find last line of the page
        page_lines = read_page_file(volume_num, layer, end_page)
        if page_lines:
            last_line_num = None
            for line in reversed(page_lines):
                line_num, _ = parse_line(line)
                if line_num is not None:
                    last_line_num = line_num
                    break
            end_line = last_line_num if last_line_num else 99999
        else:
            end_line = 99999
    
    content = extract_section_content(
        volume_num, layer, 
        start_page, start_line, 
        end_page, end_line
    )
    
    return content

def main():
    print("=" * 60)
    print("CONTENT EXTRACTION v2 - Phase 2 (FIXED)")
    print("Preserves line numbers and FOLIO markers at top of every page")
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
    print()
    print("Next step: Run ./03_verify_migration_v2.py")

if __name__ == "__main__":
    main()
