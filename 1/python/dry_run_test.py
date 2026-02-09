#!/usr/bin/env python3
"""
Dry run test - extracts just a few sections to verify logic
"""

import sys
sys.path.insert(0, '.')
from extract_content_v3 import (
    load_boundary_json, get_layer_path, extract_section_content_fixed,
    read_page_file, parse_line_number
)

def test_ch10_overlap():
    """Test Ch 10 section B boundary handling."""
    print("Test: Ch 10 Section B Boundary (Overlap Fix)")
    print("-" * 60)
    
    # Should extract from page 441 line 18727 to page 454 line 19353
    content = extract_section_content_fixed(
        volume=1, layer='literal',
        start_page=441, start_line=18727,
        end_page=454, end_line=19353
    )
    
    lines = content.split('\n')
    
    # Find last line number
    import re
    last_num = None
    for line in reversed(lines):
        match = re.match(r'\[(\d+)\]', line.strip())
        if match:
            last_num = int(match.group(1))
            break
    
    if last_num:
        print(f"  Expected last line: ≤ 19353")
        print(f"  Actual last line: {last_num}")
        if last_num <= 19353:
            print("  ✓ PASS: No overlap")
        else:
            print(f"  ✗ FAIL: Overlap of {last_num - 19353} lines")
    else:
        print("  Could not determine last line")
    print()

def test_liturgical_mapping():
    """Test liturgical gets line numbers from Tibetan."""
    print("Test: Liturgical Line Number Mapping")
    print("-" * 60)
    
    content = extract_section_content_fixed(
        volume=1, layer='liturgical',
        start_page=1, start_line=1,
        end_page=1, end_line=35,
        tibetan_ref=True
    )
    
    lines = content.split('\n')
    import re
    numbered = [l for l in lines if re.match(r'\[\d+\]', l.strip())]
    
    print(f"  Lines extracted: {len(lines)}")
    print(f"  Lines with numbers: {len(numbered)}")
    
    if numbered:
        print("  Sample lines:")
        for line in numbered[:3]:
            print(f"    {line.strip()[:50]}...")
        print("  ✓ PASS: Line numbers assigned")
    else:
        print("  ✗ FAIL: No line numbers found")
    print()

def test_range_format():
    """Test commentary preserves range format."""
    print("Test: Commentary Range Format")
    print("-" * 60)
    
    content = extract_section_content_fixed(
        volume=1, layer='commentary',
        start_page=1, start_line=1,
        end_page=6, end_line=1000  # Approximate
    )
    
    import re
    ranges = re.findall(r'\[\d+-\d+\]', content)
    singles = re.findall(r'\[\d+\]\s', content)
    
    print(f"  Range formats found: {len(ranges)}")
    print(f"  Single formats found: {len(singles)}")
    
    if ranges:
        print("  Sample ranges:")
        for r in ranges[:3]:
            print(f"    {r}")
        print("  ✓ PASS: Range format preserved")
    else:
        print("  ✗ FAIL: No range formats found")
    print()

if __name__ == '__main__':
    print("=" * 60)
    print("DRY RUN TESTS")
    print("=" * 60)
    print()
    
    test_ch10_overlap()
    test_liturgical_mapping()
    test_range_format()
    
    print("=" * 60)
    print("Dry run complete")
    print("=" * 60)
