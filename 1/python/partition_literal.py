#!/usr/bin/env python3
"""
Partition literal layer using Tibetan boundaries.
Creates section files with placeholders for missing lines.
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
            match = re.match(r'^\[(\d+)\]\s*(.*)', line)
            if match:
                line_num = int(match.group(1))
                content = match.group(2)
                lines[line_num] = content
    
    return lines


def extract_section_content(section_data, next_section_data, literal_dir, tibetan_dir):
    """
    Extract content for a section from literal layer.
    Returns (content_lines, page_markers_added_bytes, placeholder_count).
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
    placeholder_count = 0
    current_page = start_page
    
    while True:
        literal_page_path = literal_dir / f"PAGE_{current_page:03d}.txt"
        tibetan_page_path = tibetan_dir / f"PAGE_{current_page:03d}.txt"
        
        literal_lines = read_page_lines(literal_page_path)
        tibetan_lines = read_page_lines(tibetan_page_path)
        
        if not literal_lines and not tibetan_lines:
            print(f"Warning: Could not read page {current_page}")
            break
        
        # Add page marker if not first page
        if current_page > start_page:
            marker = f"\n\n### PAGE {current_page}\n\n"
            content_lines.append(marker)
            page_markers_bytes += len(marker.encode('utf-8'))
        
        # Determine line range for this page
        if current_page == start_page:
            page_start_line = start_line
        else:
            page_start_line = min(tibetan_lines.keys()) if tibetan_lines else min(literal_lines.keys())
        
        if end_page and current_page == end_page:
            page_end_line = end_line - 1  # Stop before the next section's start line
        else:
            page_end_line = max(tibetan_lines.keys()) if tibetan_lines else max(literal_lines.keys())
        
        # Collect lines in order
        all_line_nums = sorted(set(list(tibetan_lines.keys()) + list(literal_lines.keys())))
        for line_num in all_line_nums:
            if page_start_line <= line_num <= page_end_line:
                if line_num in literal_lines:
                    # Line exists in literal
                    content_lines.append(f"[{line_num}] {literal_lines[line_num]}\n")
                elif line_num in tibetan_lines:
                    # Line missing in literal, add placeholder
                    content_lines.append(f"[{line_num}] [PLACEHOLDER]\n")
                    placeholder_count += 1
        
        # Check if we've reached the end
        if end_page and current_page >= end_page:
            break
        
        if not end_page:
            # Last section - check if more pages exist
            next_page_path = literal_dir / f"PAGE_{current_page + 1:03d}.txt"
            if not next_page_path.exists():
                break
        
        current_page += 1
    
    return content_lines, page_markers_bytes, placeholder_count


def main():
    # Paths
    base_dir = Path("/home/opencode/MDZOD/1")
    concise_path = base_dir / "boundary_concise.json"
    literal1_dir = base_dir / "volume_1" / "literal"
    literal2_dir = base_dir / "volume_2" / "literal"
    tibetan1_dir = base_dir / "volume_1" / "tibetan"
    tibetan2_dir = base_dir / "volume_2" / "tibetan"
    output_dir = base_dir / "text" / "literal"
    
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
    v1_input = sum(f.stat().st_size for f in literal1_dir.glob("PAGE_*.txt"))
    v2_input = sum(f.stat().st_size for f in literal2_dir.glob("PAGE_*.txt"))
    total_input = v1_input + v2_input
    
    print(f"\nInput sizes:")
    print(f"  Volume 1: {v1_input:,} bytes")
    print(f"  Volume 2: {v2_input:,} bytes")
    print(f"  Total: {total_input:,} bytes")
    
    # Process sections
    total_page_markers = 0
    total_placeholders = 0
    total_output = 0
    
    for i, section in enumerate(sections):
        section_id = section['id']
        volume, _, _, _ = parse_section_id(section_id)
        literal_dir = literal1_dir if volume == 1 else literal2_dir
        tibetan_dir = tibetan1_dir if volume == 1 else tibetan2_dir
        
        # Get next section for end boundary
        next_section = sections[i + 1] if i < len(sections) - 1 else None
        
        # Verify volumes match for end boundary
        if next_section:
            next_vol, _, _, _ = parse_section_id(next_section['id'])
            if next_vol != volume:
                next_section = None
        
        # Extract content
        content_lines, markers_bytes, placeholder_count = extract_section_content(
            section, next_section, literal_dir, tibetan_dir
        )
        total_page_markers += markers_bytes
        total_placeholders += placeholder_count
        
        # Write section file
        output_path = output_dir / f"{section_id}.txt"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.writelines(content_lines)
        
        total_output += output_path.stat().st_size
        
        if (i + 1) % 50 == 0:
            print(f"Processed {i + 1}/{len(sections)} sections...")
    
    print(f"\n{'='*60}")
    print("PARTITION COMPLETE")
    print(f"{'='*60}")
    
    print(f"\nStatistics:")
    print(f"  Input: {total_input:,} bytes")
    print(f"  Page markers added: {total_page_markers:,} bytes")
    print(f"  Placeholders: {total_placeholders}")
    print(f"  Output: {total_output:,} bytes")
    print(f"  Difference: {total_output - total_input - total_page_markers:,} bytes")
    
    print(f"\nSample files:")
    for sample_name in ["01-01-01-01.txt", "01-01-02-01.txt"]:
        sample_path = output_dir / sample_name
        if sample_path.exists():
            with open(sample_path, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')[:5]
                placeholders = content.count('[PLACEHOLDER]')
                print(f"\n  {sample_name} ({len(content):,} chars, {placeholders} placeholders):")
                for line in lines:
                    if line.strip():
                        print(f"    {line[:80]}")


if __name__ == "__main__":
    main()
