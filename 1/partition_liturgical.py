#!/usr/bin/env python3
"""
Partition liturgical layer using Tibetan boundaries.
Preserves numbered empty lines, strips only trailing unnumbered blanks.
"""

import json
import re
from pathlib import Path


def parse_section_id(section_id):
    """Parse section_id like '01-01-01-01' into (volume, chapter, section, subsection)."""
    parts = section_id.split('-')
    return tuple(int(p) for p in parts)


def get_volume_dir(volume, volume1_dir, volume2_dir):
    """Return the appropriate volume directory."""
    return volume1_dir if volume == 1 else volume2_dir


def read_page_lines(page_path):
    """Read a PAGE file and return dict of {line_number: line_content}."""
    lines = {}
    if not page_path.exists():
        return lines
    
    with open(page_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n\r')
            match = re.match(r'^(\[(\d+)\])\s*(.*)', line)
            if match:
                line_num = int(match.group(2))
                content = match.group(3)  # May be empty
                lines[line_num] = content
    
    return lines


def extract_section_content(section_data, next_section_data, liturgical_dir):
    """
    Extract content for a section from liturgical layer.
    Returns (content_lines, page_markers_added_bytes).
    """
    section_id = section_data['id']
    start_page = section_data['start_page']
    start_line = section_data['start_line']
    
    # Determine end boundary
    if next_section_data:
        end_page = next_section_data['start_page']
        end_line = next_section_data['start_line']
    else:
        end_page = None
        end_line = None
    
    content_lines = []
    page_markers_bytes = 0
    current_page = start_page
    
    while True:
        page_path = liturgical_dir / f"PAGE_{current_page:03d}.txt"
        page_lines = read_page_lines(page_path)
        
        if not page_lines:
            print(f"Warning: Could not read page {current_page}")
            break
        
        # Add page marker if not first page
        if current_page > start_page:
            marker = f"\n\n### PAGE {current_page}\n\n"
            content_lines.append(marker)
            page_markers_bytes += len(marker.encode('utf-8'))
        
        # Determine line range
        if current_page == start_page:
            page_start_line = start_line
        else:
            page_start_line = min(page_lines.keys())
        
        if end_page and current_page == end_page:
            page_end_line = end_line - 1
        else:
            page_end_line = max(page_lines.keys())
        
        # Collect lines in order (include empty content lines)
        for line_num in sorted(page_lines.keys()):
            if page_start_line <= line_num <= page_end_line:
                content = page_lines[line_num]
                if content.strip():
                    content_lines.append(f"[{line_num}] {content}\n")
                else:
                    # Preserve numbered empty line
                    content_lines.append(f"[{line_num}] \n")
        
        # Check if we've reached the end
        if end_page and current_page >= end_page:
            break
        
        if not end_page:
            next_page_path = liturgical_dir / f"PAGE_{current_page + 1:03d}.txt"
            if not next_page_path.exists():
                break
        
        current_page += 1
    
    return content_lines, page_markers_bytes


def main():
    # Paths
    base_dir = Path("/home/opencode/MDZOD/1")
    concise_path = base_dir / "boundary_concise.json"
    liturgical1_dir = base_dir / "volume_1" / "liturgical"
    liturgical2_dir = base_dir / "volume_2" / "liturgical"
    output_dir = base_dir / "text" / "liturgical"
    
    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Clear existing section files
    for f in output_dir.glob("*.txt"):
        f.unlink()
    
    # Load boundary data
    with open(concise_path, 'r', encoding='utf-8') as f:
        concise_data = json.load(f)
    
    sections = concise_data['sections']
    print(f"Loaded {len(sections)} sections")
    
    # Calculate input sizes
    v1_input = sum(f.stat().st_size for f in liturgical1_dir.glob("PAGE_*.txt"))
    v2_input = sum(f.stat().st_size for f in liturgical2_dir.glob("PAGE_*.txt"))
    total_input = v1_input + v2_input
    
    print(f"\nInput sizes:")
    print(f"  Volume 1: {v1_input:,} bytes")
    print(f"  Volume 2: {v2_input:,} bytes")
    print(f"  Total: {total_input:,} bytes")
    
    # Process sections
    total_page_markers = 0
    total_output = 0
    
    for i, section in enumerate(sections):
        section_id = section['id']
        volume, _, _, _ = parse_section_id(section_id)
        liturgical_dir = get_volume_dir(volume, liturgical1_dir, liturgical2_dir)
        
        # Get next section for end boundary
        next_section = sections[i + 1] if i < len(sections) - 1 else None
        
        # Verify volumes match
        if next_section:
            next_vol, _, _, _ = parse_section_id(next_section['id'])
            if next_vol != volume:
                next_section = None
        
        # Extract content
        content_lines, markers_bytes = extract_section_content(
            section, next_section, liturgical_dir
        )
        total_page_markers += markers_bytes
        
        # Write section file
        output_path = output_dir / f"{section_id}.txt"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.writelines(content_lines)
        
        total_output += output_path.stat().st_size
        
        if (i + 1) % 50 == 0:
            print(f"Processed {i + 1}/{len(sections)} sections...")
    
    print(f"\n{'='*60}")
    print("LITURGICAL PARTITION COMPLETE")
    print(f"{'='*60}")
    
    print(f"\nStatistics:")
    print(f"  Input: {total_input:,} bytes")
    print(f"  Page markers added: {total_page_markers:,} bytes")
    print(f"  Output: {total_output:,} bytes")
    diff = total_output - total_input - total_page_markers
    print(f"  Difference: {diff:,} bytes ({diff/total_input*100:.3f}%)")
    
    print(f"\nSample files:")
    for sample_name in ["01-01-01-01.txt", "01-01-02-01.txt"]:
        sample_path = output_dir / sample_name
        if sample_path.exists():
            with open(sample_path, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')[:5]
                print(f"\n  {sample_name} ({len(content):,} chars):")
                for line in lines:
                    if line.strip():
                        print(f"    {line[:80]}")


if __name__ == "__main__":
    main()
