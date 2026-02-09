#!/usr/bin/env python3
"""
Migration Verification Script v3
- Verifies line number continuity
- Verifies FOLIO markers (Tibetan only)
- Checks for overlaps/gaps
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

def get_line_numbers_from_file(filepath):
    """Extract all line numbers from a file."""
    if not filepath.exists():
        return []
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    line_nums = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith('FOLIO_'):
            continue
        # Single number: [4417]
        match = re.match(r'\[(\d+)\]', line)
        if match:
            line_nums.append(int(match.group(1)))
            continue
        # Range: [1-4] - use both start and end
        match = re.match(r'\[(\d+)-(\d+)\]', line)
        if match:
            line_nums.append(int(match.group(1)))  # Start
            line_nums.append(int(match.group(2)))  # End
    return line_nums

def get_last_line(filepath):
    """Get the last line number in a file."""
    nums = get_line_numbers_from_file(filepath)
    return nums[-1] if nums else None

def get_first_line(filepath):
    """Get the first line number in a file."""
    nums = get_line_numbers_from_file(filepath)
    return nums[0] if nums else None

def verify_file_format(filepath, layer, section_data, volume_num):
    """Verify a single section file format."""
    errors = []
    
    if not filepath.exists():
        return [f"File does not exist: {filepath}"]
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if not content.strip():
        return []  # Empty is OK for some layers
    
    lines = content.split('\n')
    folio_markers = []
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        if line.startswith('FOLIO_'):
            folio_markers.append((i, line))
            continue
        
        # Check format based on layer
        if layer in INDIVIDUAL_LINE_LAYERS:
            # Should be [number] format, no zero padding
            if not re.match(r'\[\d+\]\s+', line):
                errors.append(f"Line {i+1}: Invalid format (expected [N] content)")
        else:
            # Commentary - can be [number] or [start-end]
            if not re.match(r'\[\d+(?:-\d+)?\]\s+', line):
                errors.append(f"Line {i+1}: Invalid range format")
    
    # Check FOLIO markers for Tibetan
    if layer == 'tibetan':
        start_page = section_data['boundary_start']['page']
        
        # Check for FOLIO_001 at start of Volume 1
        if volume_num == 1 and start_page == 1:
            if not folio_markers or folio_markers[0][1] != 'FOLIO_001':
                errors.append("Missing FOLIO_001 at Volume 1 start")
        
        # Check 3-digit padding on FOLIO markers
        for line_num, folio in folio_markers:
            if not re.match(r'FOLIO_\d{3}$', folio):
                errors.append(f"Line {line_num+1}: FOLIO marker must use 3-digit format (FOLIO_001)")
    else:
        # Non-Tibetan should not have FOLIO
        if folio_markers:
            errors.append(f"FOLIO markers found in {layer} layer (should be Tibetan only)")
    
    return errors

def main():
    print("=" * 60)
    print("MIGRATION VERIFICATION v3")
    print("=" * 60)
    print()
    
    boundary_data = load_boundary_json()
    
    total_passed = 0
    total_empty = 0
    total_errors = 0
    
    # Track gaps and overlaps
    all_gaps = []
    all_overlaps = []
    
    for layer in LAYERS:
        print(f"Verifying layer: {layer}")
        print("-" * 60)
        
        layer_passed = 0
        layer_empty = 0
        layer_errors = 0
        layer_gaps = []
        layer_overlaps = []
        
        for volume_data in boundary_data['volumes']:
            volume_num = volume_data['volume_number']
            
            for chapter_data in volume_data['chapters']:
                chapter_num = chapter_data['chapter_number']
                sections = chapter_data['sections']
                
                for i in range(len(sections)):
                    section = sections[i]
                    section_id = section['section_id']
                    filepath = get_layer_path(volume_num, layer, chapter_num, section_id)
                    
                    # Check format
                    errors = verify_file_format(filepath, layer, section, volume_num)
                    if errors:
                        layer_errors += 1
                        for err in errors[:3]:
                            print(f"  ✗ {err}")
                    else:
                        if filepath.exists():
                            with open(filepath, 'r', encoding='utf-8') as f:
                                if not f.read().strip():
                                    layer_empty += 1
                                else:
                                    layer_passed += 1
                    
                    # Check continuity with next section
                    if i < len(sections) - 1:
                        next_section = sections[i + 1]
                        next_filepath = get_layer_path(volume_num, layer, chapter_num, next_section['section_id'])
                        
                        last_line = get_last_line(filepath)
                        first_line_next = get_first_line(next_filepath)
                        
                        if last_line and first_line_next:
                            expected = last_line + 1
                            if first_line_next > expected:
                                gap_size = first_line_next - expected
                                layer_gaps.append(f"Ch{chapter_num} {section_id}→{next_section['section_id']}: gap {gap_size}")
                            elif first_line_next < expected:
                                overlap_size = expected - first_line_next
                                layer_overlaps.append(f"Ch{chapter_num} {section_id}→{next_section['section_id']}: overlap {overlap_size}")
        
        status = f"  ✓ Passed: {layer_passed}"
        if layer_empty > 0:
            status += f", Empty: {layer_empty}"
        if layer_errors > 0:
            status += f", ✗ Errors: {layer_errors}"
        print(status)
        
        if layer_gaps:
            print(f"  ⚠ Gaps: {len(layer_gaps)}")
            for g in layer_gaps[:3]:
                print(f"    {g}")
        if layer_overlaps:
            print(f"  ⚠ Overlaps: {len(layer_overlaps)}")
            for o in layer_overlaps[:3]:
                print(f"    {o}")
        
        all_gaps.extend(layer_gaps)
        all_overlaps.extend(layer_overlaps)
        total_passed += layer_passed
        total_empty += layer_empty
        total_errors += layer_errors
        print()
    
    print("=" * 60)
    print("VERIFICATION SUMMARY")
    print("=" * 60)
    print(f"Total: {total_passed} passed, {total_empty} empty, {total_errors} errors")
    print(f"Continuity: {len(all_gaps)} gaps, {len(all_overlaps)} overlaps")
    print()
    
    if total_errors == 0 and len(all_overlaps) == 0:
        print("✅ MIGRATION VERIFIED SUCCESSFULLY")
        return 0
    else:
        print("❌ VERIFICATION FAILED")
        return 1

if __name__ == "__main__":
    import sys
    sys.exit(main())
