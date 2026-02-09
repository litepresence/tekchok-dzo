#!/usr/bin/env python3
"""
Test script to validate extraction fixes
Tests specific problematic cases before full repartition
"""

import sys
from pathlib import Path

# Test cases:
# 1. Ch 10 B→C overlap (should not extract lines 19354-19356 for section B)
# 2. Liturgical line mapping (should map to Tibetan line numbers)
# 3. Range format preservation (commentary should keep [1-4] format)
# 4. FOLIO markers in Tibetan only

def test_overlap_fix():
    """Test that Ch 10 B doesn't overlap into C."""
    print("Test 1: Ch 10 B→C Overlap Fix")
    print("-" * 60)
    
    filepath = Path('partitioned_v1/literal/chapter_10/section_B.txt')
    if not filepath.exists():
        print("  File not found (need to run extraction first)")
        return False
    
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    # Get last line number
    import re
    last_num = None
    for line in reversed(lines):
        match = re.match(r'\[(\d+)\]', line.strip())
        if match:
            last_num = int(match.group(1))
            break
    
    if last_num:
        if last_num <= 19353:
            print(f"  ✓ PASS: Last line is {last_num} (should be ≤ 19353)")
            return True
        else:
            print(f"  ✗ FAIL: Last line is {last_num} (should be ≤ 19353)")
            print(f"    Overlap of {last_num - 19353} lines detected")
            return False
    else:
        print("  Could not determine last line number")
        return False

def test_liturgical_mapping():
    """Test that liturgical has line numbers mapped from Tibetan."""
    print("\nTest 2: Liturgical Line Number Mapping")
    print("-" * 60)
    
    filepath = Path('partitioned_v1/liturgical/chapter_01/section_01.txt')
    if not filepath.exists():
        print("  File not found (need to run extraction first)")
        return False
    
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    # Count lines with [number] format
    import re
    numbered_lines = [l for l in lines if re.match(r'\[\d+\]', l.strip())]
    
    if len(numbered_lines) > 0:
        print(f"  ✓ PASS: {len(numbered_lines)} lines with line numbers")
        # Show first few
        for line in numbered_lines[:3]:
            print(f"    {line.strip()[:60]}...")
        return True
    else:
        print("  ✗ FAIL: No lines with line numbers found")
        return False

def test_range_format():
    """Test that commentary preserves range format."""
    print("\nTest 3: Commentary Range Format Preservation")
    print("-" * 60)
    
    filepath = Path('partitioned_v1/commentary/chapter_01/section_01.txt')
    if not filepath.exists():
        print("  File not found (need to run extraction first)")
        return False
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    if not content.strip():
        print("  File is empty (extraction may have failed)")
        return False
    
    import re
    # Check for range format
    range_matches = re.findall(r'\[\d+-\d+\]', content)
    
    if range_matches:
        print(f"  ✓ PASS: Found {len(range_matches)} range markers")
        print(f"    Examples: {', '.join(range_matches[:3])}")
        return True
    else:
        print("  ✗ FAIL: No range format found")
        return False

def test_folio_format():
    """Test FOLIO markers use correct format."""
    print("\nTest 4: FOLIO Marker Format")
    print("-" * 60)
    
    filepath = Path('partitioned_v1/tibetan/chapter_01/section_01.txt')
    if not filepath.exists():
        print("  File not found (need to run extraction first)")
        return False
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    import re
    folio_matches = re.findall(r'FOLIO_\d+', content)
    
    if not folio_matches:
        print("  ✗ FAIL: No FOLIO markers found")
        return False
    
    # Check for 3-digit format
    valid_format = all(re.match(r'FOLIO_\d{3}$', f) for f in folio_matches)
    
    if valid_format:
        print(f"  ✓ PASS: {len(folio_matches)} FOLIO markers with 3-digit format")
        print(f"    Examples: {', '.join(folio_matches[:3])}")
        return True
    else:
        print("  ✗ FAIL: FOLIO markers don't use 3-digit format")
        print(f"    Found: {folio_matches[:3]}")
        return False

def main():
    print("=" * 60)
    print("EXTRACTION FIXES VALIDATION")
    print("=" * 60)
    print()
    print("NOTE: Run extraction first: ./02_extract_content_v3.py")
    print()
    
    tests = [
        test_overlap_fix,
        test_liturgical_mapping,
        test_range_format,
        test_folio_format
    ]
    
    results = []
    for test in tests:
        try:
            results.append(test())
        except Exception as e:
            print(f"  ERROR: {e}")
            results.append(False)
    
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    passed = sum(results)
    total = len(results)
    print(f"Passed: {passed}/{total}")
    
    if passed == total:
        print("\n✅ ALL TESTS PASSED - Ready for full repartition")
        return 0
    else:
        print("\n❌ SOME TESTS FAILED - Review extraction logic")
        return 1

if __name__ == "__main__":
    sys.exit(main())
