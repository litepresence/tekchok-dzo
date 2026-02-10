#!/usr/bin/env python3
"""
Verify markers.md against boundary_v3.json and repair if needed.
Ensures markers.md accurately reflects all section markers in boundary_v3.json.
"""

import json
import re
from pathlib import Path

def parse_markers_md(filepath):
    """Parse markers.md and extract marker data."""
    markers = []
    current_chapter = None
    
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for line in lines:
        line = line.strip()
        
        # Check for chapter headers
        if line.startswith('## Chapter '):
            match = re.search(r'Chapter (\d+)', line)
            if match:
                current_chapter = int(match.group(1))
        
        # Check for table rows with marker data
        # Format: | # | Vol | Page | Line | Marker |
        if line.startswith('|') and not line.startswith('|---'):
            parts = [p.strip() for p in line.split('|')]
            # Filter out empty strings from split
            parts = [p for p in parts if p]
            
            if len(parts) >= 5 and parts[0].isdigit():
                try:
                    marker_num = int(parts[0])
                    vol = int(parts[1])
                    page = int(parts[2])
                    line_num = int(parts[3])
                    marker_text = parts[4]
                    
                    markers.append({
                        'num': marker_num,
                        'vol': vol,
                        'page': page,
                        'line': line_num,
                        'chapter': current_chapter,
                        'marker': marker_text
                    })
                except (ValueError, IndexError):
                    continue
    
    return markers

def get_expected_markers_from_boundary():
    """Extract expected markers from boundary_v3.json."""
    with open('/home/opencode/MDZOD/1/boundary_v3.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    markers = []
    marker_num = 0
    
    # Sort by key to maintain order
    for key in sorted(data['sections'].keys()):
        section = data['sections'][key]
        
        # Only include subsection 1 (main section markers)
        if section['subsection'] == 1:
            marker_num += 1
            ch = section['chapter']
            page = section['start_page']
            line = section['start_line']
            
            # Determine volume by chapter
            vol = 1 if ch <= 14 else 2
            
            # Get marker text (first 50 chars of start_phrase)
            marker_text = section['start_phrase'][:50]
            if len(section['start_phrase']) > 50:
                marker_text += '...'
            
            markers.append({
                'num': marker_num,
                'vol': vol,
                'page': page,
                'line': line,
                'chapter': ch,
                'marker': marker_text,
                'key': key  # Keep for debugging
            })
    
    return markers

def compare_markers(expected, actual):
    """Compare expected vs actual markers and return discrepancies."""
    issues = []
    
    # Check count
    if len(expected) != len(actual):
        issues.append({
            'type': 'count_mismatch',
            'expected_count': len(expected),
            'actual_count': len(actual)
        })
    
    # Compare each marker
    min_len = min(len(expected), len(actual))
    for i in range(min_len):
        exp = expected[i]
        act = actual[i]
        
        if exp['vol'] != act['vol']:
            issues.append({
                'type': 'volume_mismatch',
                'marker_num': exp['num'],
                'expected_vol': exp['vol'],
                'actual_vol': act['vol']
            })
        
        if exp['page'] != act['page']:
            issues.append({
                'type': 'page_mismatch',
                'marker_num': exp['num'],
                'chapter': exp['chapter'],
                'expected_page': exp['page'],
                'actual_page': act['page']
            })
        
        if exp['line'] != act['line']:
            issues.append({
                'type': 'line_mismatch',
                'marker_num': exp['num'],
                'chapter': exp['chapter'],
                'expected_line': exp['line'],
                'actual_line': act['line']
            })
    
    # Check for extra markers in actual
    if len(actual) > len(expected):
        for i in range(len(expected), len(actual)):
            issues.append({
                'type': 'extra_marker',
                'marker_num': actual[i]['num'],
                'marker': actual[i]
            })
    
    # Check for missing markers
    if len(expected) > len(actual):
        for i in range(len(actual), len(expected)):
            issues.append({
                'type': 'missing_marker',
                'marker_num': expected[i]['num'],
                'marker': expected[i]
            })
    
    return issues

def generate_markers_md(markers):
    """Generate fresh markers.md content from marker data."""
    lines = []
    lines.append("# Treasury of the Supreme Vehicle: Section Markers")
    lines.append("")
    lines.append("Complete list of all section markers (དང་པོ་, གཉིས་པ་, etc.) found in the root Tibetan text.")
    lines.append("")
    lines.append(f"**Total Markers**: {len(markers)}")
    lines.append(f"**Generated**: 2026-02-10")
    lines.append(f"**Source**: boundary_v3.json")
    lines.append("")
    
    # Group by chapter
    current_chapter = 0
    for m in markers:
        if m['chapter'] != current_chapter:
            if current_chapter > 0:
                lines.append("")
            lines.append(f"## Chapter {m['chapter']}")
            lines.append("")
            lines.append("| # | Vol | Page | Line | Marker |")
            lines.append("|---|-----|------|------|--------|")
            current_chapter = m['chapter']
        
        lines.append(f"| {m['num']} | {m['vol']} | {m['page']} | {m['line']} | {m['marker']} |")
    
    # Add summary
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    
    vol1_count = len([m for m in markers if m['vol'] == 1])
    vol2_count = len([m for m in markers if m['vol'] == 2])
    
    lines.append(f"- **Volume 1**: {vol1_count} markers")
    lines.append(f"- **Volume 2**: {vol2_count} markers")
    lines.append(f"- **Total**: {len(markers)} markers")
    lines.append("")
    
    return '\n'.join(lines)

def main():
    print("=" * 80)
    print("MARKERS.MD VERIFICATION SCRIPT")
    print("=" * 80)
    
    markers_path = '/home/opencode/MDZOD/1/markers.md'
    
    # Get expected markers from boundary_v3.json
    print("\nLoading expected markers from boundary_v3.json...")
    expected_markers = get_expected_markers_from_boundary()
    print(f"Expected: {len(expected_markers)} markers")
    
    # Parse actual markers.md
    print(f"\nParsing {markers_path}...")
    try:
        actual_markers = parse_markers_md(markers_path)
        print(f"Found: {len(actual_markers)} markers")
    except FileNotFoundError:
        print(f"ERROR: {markers_path} not found!")
        actual_markers = []
    
    # Compare
    print("\nComparing markers...")
    issues = compare_markers(expected_markers, actual_markers)
    
    if not issues:
        print("\n" + "=" * 80)
        print("✅ VERIFICATION PASSED")
        print("=" * 80)
        print(f"\nAll {len(expected_markers)} markers verified correctly!")
        print("markers.md is up to date with boundary_v3.json")
        return True
    
    # Report issues
    print("\n" + "=" * 80)
    print("⚠️  DISCREPANCIES FOUND")
    print("=" * 80)
    
    for issue in issues:
        if issue['type'] == 'count_mismatch':
            print(f"\n❌ Count mismatch:")
            print(f"   Expected: {issue['expected_count']} markers")
            print(f"   Actual: {issue['actual_count']} markers")
        
        elif issue['type'] == 'volume_mismatch':
            print(f"\n❌ Marker {issue['marker_num']}: Volume mismatch")
            print(f"   Expected: Volume {issue['expected_vol']}")
            print(f"   Actual: Volume {issue['actual_vol']}")
        
        elif issue['type'] == 'page_mismatch':
            print(f"\n❌ Marker {issue['marker_num']} (Chapter {issue.get('chapter', '?')}): Page mismatch")
            print(f"   Expected: Page {issue['expected_page']}")
            print(f"   Actual: Page {issue['actual_page']}")
        
        elif issue['type'] == 'line_mismatch':
            print(f"\n❌ Marker {issue['marker_num']} (Chapter {issue.get('chapter', '?')}): Line mismatch")
            print(f"   Expected: Line {issue['expected_line']}")
            print(f"   Actual: Line {issue['actual_line']}")
        
        elif issue['type'] == 'extra_marker':
            print(f"\n❌ Extra marker #{issue['marker_num']} found in markers.md")
        
        elif issue['type'] == 'missing_marker':
            m = issue['marker']
            print(f"\n❌ Missing marker #{issue['marker_num']} (Chapter {m['chapter']}, Page {m['page']}, Line {m['line']})")
    
    # Repair markers.md
    print("\n" + "=" * 80)
    print("🔧 REPAIRING MARKERS.MD")
    print("=" * 80)
    
    new_content = generate_markers_md(expected_markers)
    
    with open(markers_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"\n✅ Repaired {markers_path}")
    print(f"   - Total markers: {len(expected_markers)}")
    print(f"   - Volume 1: {len([m for m in expected_markers if m['vol'] == 1])}")
    print(f"   - Volume 2: {len([m for m in expected_markers if m['vol'] == 2])}")
    print(f"   - Chapters: {len(set(m['chapter'] for m in expected_markers))}")
    
    return True

if __name__ == '__main__':
    success = main()
    exit(0 if success else 1)
