#!/usr/bin/env python3
"""
Content Extractor - Phase 2 of Migration
Extracts content from page-based to section-based using boundary.json
"""

import json
import os
import re
from pathlib import Path

def load_boundary_json():
    """Load and return boundary.json data"""
    with open('boundary.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def get_page_content(volume, page_num):
    """Read content from a page file"""
    filepath = f"volume_{volume}/tibetan/PAGE_{page_num:03d}.txt"
    if not os.path.exists(filepath):
        return None
    
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def extract_lines_from_content(content, start_line, end_line=None):
    """Extract specific lines from page content"""
    lines = content.split('\n')
    extracted = []
    
    for line in lines:
        match = re.match(r'\[(\d+)\]\s*(.+)', line)
        if match:
            line_num = int(match.group(1))
            line_content = match.group(2)
            
            if line_num >= start_line:
                if end_line is None or line_num <= end_line:
                    extracted.append(line_content)
                elif end_line and line_num > end_line:
                    break
    
    return '\n'.join(extracted)

def extract_section_content(volume, start_page, start_line, end_page, end_line):
    """Extract content from start to end boundaries"""
    all_content = []
    
    current_page = start_page
    current_line = start_line
    
    while current_page <= end_page:
        page_content = get_page_content(volume, current_page)
        if not page_content:
            current_page += 1
            continue
        
        # Determine line range for this page
        page_start_line = current_line if current_page == start_page else 1
        page_end_line = end_line if current_page == end_page else None
        
        # Extract lines
        lines = extract_lines_from_content(page_content, page_start_line, page_end_line)
        if lines:
            all_content.append(lines)
        
        current_page += 1
        current_line = 1  # Reset for next page
    
    return '\n'.join(all_content)

def process_layer(layer_name, data):
    """Process extraction for one layer"""
    print(f"\nProcessing layer: {layer_name}")
    print("-" * 60)
    
    total_sections = 0
    extracted_sections = 0
    
    for vol in data['volumes']:
        vol_num = vol['volume_number']
        vol_sections = []
        
        for ch in vol['chapters']:
            ch_num = ch['chapter_number']
            
            for i, sec in enumerate(ch['sections']):
                total_sections += 1
                sec_id = sec.get('section_id', sec.get('section_number', '?'))
                
                # Get boundaries
                bs = sec['boundary_start']
                start_page = bs['page']
                start_line = bs['line']
                
                # Get end boundary (next section or chapter end)
                if i + 1 < len(ch['sections']):
                    next_sec = ch['sections'][i + 1]
                    end_page = next_sec['boundary_start']['page']
                    end_line = next_sec['boundary_start']['line'] - 1
                else:
                    # Last section in chapter
                    end_page = sec['pages']['end']
                    # Get last line of final page
                    last_page = get_page_content(vol_num, end_page)
                    if last_page:
                        lines = last_page.split('\n')
                        last_line_match = None
                        for line in reversed(lines):
                            match = re.match(r'\[(\d+)\]', line)
                            if match:
                                last_line_match = int(match.group(1))
                                break
                        end_line = last_line_match if last_line_match else 99999
                    else:
                        end_line = 99999
                
                # Extract content
                content = extract_section_content(
                    vol_num, start_page, start_line, 
                    end_page, end_line
                )
                
                # Write to destination
                vol_name = f"partitioned_v{vol_num}"
                dest_path = f"{vol_name}/{layer_name}/chapter_{ch_num:02d}/section_{sec_id}.txt"
                
                with open(dest_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                extracted_sections += 1
                
                if extracted_sections % 10 == 0:
                    print(f"  Progress: {extracted_sections} sections...")
    
    print(f"  ✓ Extracted {extracted_sections} sections")
    return extracted_sections

def main():
    print("="*60)
    print("CONTENT EXTRACTION - Phase 2")
    print("="*60)
    
    # Load boundaries
    print("\nLoading boundary.json...")
    data = load_boundary_json()
    print(f"  ✓ Loaded {data['mapping_status']['total_sections']} sections")
    
    # Process all 9 layers
    layers = ['tibetan', 'wylie', 'literal', 'liturgical', 'commentary', 
              'scholar', 'epistemic', 'delusion', 'cognitive']
    
    total_extracted = 0
    for layer in layers:
        count = process_layer(layer, data)
        total_extracted += count
    
    print("\n" + "="*60)
    print("EXTRACTION COMPLETE")
    print("="*60)
    print(f"Total sections extracted: {total_extracted}")
    print(f"Layers processed: {len(layers)}")
    print("\nNext step: Run ./03_verify_migration.py")

if __name__ == '__main__':
    main()
