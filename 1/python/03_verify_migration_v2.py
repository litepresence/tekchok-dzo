#!/usr/bin/env python3
"""
Migration Verification Script v2 - Phase 3
Verifies line numbers and FOLIO markers at page transitions only
"""

import json
import re
from pathlib import Path

LAYERS = ['tibetan', 'wylie', 'literal', 'liturgical', 
          'commentary', 'scholar', 'epistemic', 'delusion', 'cognitive']

INDIVIDUAL_LINE_LAYERS = ['tibetan', 'wylie', 'literal', 'liturgical']

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

def verify_section_file(filepath, layer, section_data, volume_num):
    """Verify a single section file."""
    errors = []
    
    if not filepath.exists():
        return [f"File does not exist: {filepath}"]
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if not content.strip():
        # Empty files are OK for commentary layers that don't have source content yet
        return []
    
    lines = content.split('\n')
    
    # Check line number format
    folio_markers = []
    has_line_numbers = False
    
    for i, line in enumerate(lines):
        if not line.strip():
            continue
        
        # Check for FOLIO marker
        if line.startswith('FOLIO_'):
            folio_markers.append((i, line.strip()))
            continue
        
        # Check for line number format
        if layer in INDIVIDUAL_LINE_LAYERS:
            match = re.match(r'\[(\d+)\]\s*(.+)', line)
            if match:
                has_line_numbers = True
            else:
                errors.append(f"Line {i+1}: Missing line number format in {filepath.name}")
    
    # Verify FOLIO markers for Tibetan layer
    if layer == 'tibetan':
        start_page = section_data['boundary_start']['page']
        end_page = section_data['pages']['end']
        
        # Check if page 1 of volume 1 and needs FOLIO_001
        if volume_num == 1 and start_page == 1:
            if not folio_markers or not folio_markers[0][1] == 'FOLIO_001':
                errors.append(f"Missing FOLIO_001 at start of page 1 section in {filepath.name}")
        
        # For multi-page sections, check that page transitions have FOLIO markers
        if end_page > start_page:
            # Build list of expected FOLIO pages (all pages in the section)
            expected_pages = list(range(start_page, end_page + 1))
            found_pages = []
            
            for line_num, folio_line in folio_markers:
                match = re.match(r'FOLIO_(\d{3})$', folio_line)
                if match:
                    found_pages.append(int(match.group(1)))
            
            # Check that all section pages have FOLIO markers
            for page in expected_pages:
                if page not in found_pages:
                    errors.append(f"Missing FOLIO_{page:03d} in multi-page section in {filepath.name}")
        
        # Check FOLIO format (3-digit padding)
        for line_num, folio_line in folio_markers:
            if not re.match(r'FOLIO_\d{3}$', folio_line):
                errors.append(f"Line {line_num+1}: FOLIO marker doesn't use 3-digit format in {filepath.name}")
    else:
        # Non-Tibetan layers should NOT have FOLIO markers
        if folio_markers:
            errors.append(f"FOLIO markers found in non-Tibetan layer ({layer}) in {filepath.name}")
    
    return errors

def main():
    print("=" * 60)
    print("MIGRATION VERIFICATION v2 - Phase 3")
    print("=" * 60)
    print()
    
    boundary_data = load_boundary_json()
    
    total_errors = 0
    total_passed = 0
    total_empty = 0
    
    for layer in LAYERS:
        print(f"Verifying layer: {layer}")
        print("-" * 60)
        
        layer_errors = 0
        layer_passed = 0
        layer_empty = 0
        
        for volume_data in boundary_data['volumes']:
            volume_num = volume_data['volume_number']
            
            for chapter_data in volume_data['chapters']:
                chapter_num = chapter_data['chapter_number']
                
                for section_data in chapter_data['sections']:
                    section_id = section_data['section_id']
                    filepath = get_layer_path(volume_num, layer, chapter_num, section_id)
                    
                    errors = verify_section_file(filepath, layer, section_data, volume_num)
                    
                    if errors:
                        layer_errors += 1
                        total_errors += 1
                        for error in errors[:3]:  # Show first 3 errors
                            print(f"  ✗ {error}")
                    else:
                        # Check if file is empty (acceptable for commentary layers)
                        if filepath.exists():
                            with open(filepath, 'r', encoding='utf-8') as f:
                                if not f.read().strip():
                                    layer_empty += 1
                                    total_empty += 1
                                else:
                                    layer_passed += 1
                                    total_passed += 1
        
        status = f"  ✓ Passed: {layer_passed}"
        if layer_empty > 0:
            status += f", Empty: {layer_empty}"
        if layer_errors > 0:
            status += f", ✗ Failed: {layer_errors}"
        print(status)
        print()
    
    print("=" * 60)
    print("VERIFICATION SUMMARY")
    print("=" * 60)
    print(f"Total sections checked: {total_passed + total_empty + total_errors}")
    print(f"✓ Passed: {total_passed}")
    if total_empty > 0:
        print(f"⚠ Empty (no source content): {total_empty}")
    print(f"✗ Failed: {total_errors}")
    print()
    
    if total_errors == 0:
        print("✅ MIGRATION VERIFIED SUCCESSFULLY")
        return 0
    else:
        print("❌ VERIFICATION FAILED")
        return 1

if __name__ == "__main__":
    import sys
    sys.exit(main())
