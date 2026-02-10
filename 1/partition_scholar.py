#!/usr/bin/env python3
"""
Partition scholar layer using Tibetan boundaries.
Handles cumulative line numbers and splits entries at section boundaries.
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


def read_scholar_entries(page_path):
    """Read scholar PAGE file and return list of (start_line, end_line, marker, content) tuples."""
    entries = []
    if not page_path.exists():
        return entries
    
    with open(page_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all [N-M] patterns and their associated content
    for match in re.finditer(r'\[(\d+)-(\d+)\](?:\s*\[([A-Z]+)\])?\s*\n?(.*?)(?=\[\d+-\d+\]|\Z)', content, re.DOTALL):
        start_line = int(match.group(1))
        end_line = int(match.group(2))
        marker = match.group(3) if match.group(3) else ""
        text = match.group(4).strip()
        if text:
            entries.append((start_line, end_line, marker, text))
    
    return entries


def build_section_boundaries(sections):
    """Build lookup of section boundaries by volume."""
    boundaries = {}  # volume -> list of (start, end, section_id)
    
    for i, section in enumerate(sections):
        section_id = section['id']
        start_line = section['start_line']
        volume = int(section_id.split('-')[0])
        
        # Calculate end line
        if i + 1 < len(sections):
            next_section = sections[i + 1]
            next_vol = int(next_section['id'].split('-')[0])
            if next_vol == volume:
                end_line = next_section['start_line'] - 1
            else:
                end_line = 999999
        else:
            end_line = 999999
        
        if volume not in boundaries:
            boundaries[volume] = []
        boundaries[volume].append((start_line, end_line, section_id))
    
    return boundaries


def get_section_for_line(line_num, volume_boundaries):
    """Get the section that contains this line number."""
    for start, end, section_id in volume_boundaries:
        if start <= line_num <= end:
            return section_id
    return None


def split_entry(start_line, end_line, marker, text, volume_boundaries):
    """Split a scholar entry that spans multiple sections."""
    parts = []
    
    # Find which section(s) this entry belongs to
    start_section = get_section_for_line(start_line, volume_boundaries)
    end_section = get_section_for_line(end_line, volume_boundaries)
    
    if not start_section or not end_section:
        return [(start_line, end_line, marker, text)]
    
    if start_section == end_section:
        # Fits entirely in one section
        return [(start_line, end_line, marker, text)]
    
    # Spans multiple sections - need to split
    # For simplicity, assign entire entry to first section
    # (scholar entries often reference multiple lines as a unit)
    return [(start_line, end_line, marker, text)]


def extract_scholar_sections(sections, scholar1_dir, scholar2_dir):
    """Extract scholar entries organized by Tibetan section boundaries."""
    boundaries = build_section_boundaries(sections)
    
    # Initialize sections dict
    section_scholar = {}  # section_id -> list of (start, end, marker, text)
    for section in sections:
        section_scholar[section['id']] = []
    
    # Process both volumes
    for volume in [1, 2]:
        scholar_dir = scholar1_dir if volume == 1 else scholar2_dir
        volume_boundaries = boundaries.get(volume, [])
        
        if not volume_boundaries:
            continue
        
        # Read all scholar entries
        for page_file in sorted(scholar_dir.glob('PAGE_*.txt')):
            entries = read_scholar_entries(page_file)
            
            for start_line, end_line, marker, text in entries:
                # Check which section(s) this entry spans
                start_section = get_section_for_line(start_line, volume_boundaries)
                end_section = get_section_for_line(end_line, volume_boundaries)
                
                if not start_section:
                    continue
                
                if start_section == end_section or not end_section:
                    # Fits entirely in one section
                    section_scholar[start_section].append((start_line, end_line, marker, text))
                else:
                    # Spans multiple sections - split the entry
                    # Find the boundary
                    boundary_line = None
                    for sec_start, sec_end, sec_id in volume_boundaries:
                        if sec_id == start_section:
                            boundary_line = sec_end
                            break
                    
                    if boundary_line:
                        # Split into two parts at the boundary
                        # First part: start_line to boundary_line
                        section_scholar[start_section].append((start_line, boundary_line, marker, text))
                        # Second part: boundary_line+1 to end_line
                        section_scholar[end_section].append((boundary_line + 1, end_line, marker, text))
                    else:
                        # Can't find boundary, assign to start section
                        section_scholar[start_section].append((start_line, end_line, marker, text))
    
    return section_scholar


def main():
    base_dir = Path("/home/opencode/MDZOD/1")
    concise_path = base_dir / "boundary_concise.json"
    scholar1_dir = base_dir / "volume_1" / "scholar"
    scholar2_dir = base_dir / "volume_2" / "scholar"
    output_dir = base_dir / "text" / "scholar"
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Clear existing files
    for f in output_dir.glob("*.txt"):
        f.unlink()
    
    # Load boundary data
    with open(concise_path, 'r', encoding='utf-8') as f:
        concise_data = json.load(f)
    
    sections = concise_data['sections']
    print(f"Loaded {len(sections)} sections")
    
    # Calculate input size
    v1_input = sum(f.stat().st_size for f in scholar1_dir.glob("PAGE_*.txt"))
    v2_input = sum(f.stat().st_size for f in scholar2_dir.glob("PAGE_*.txt"))
    total_input = v1_input + v2_input
    
    print(f"\nInput sizes:")
    print(f"  Volume 1: {v1_input:,} bytes")
    print(f"  Volume 2: {v2_input:,} bytes")
    print(f"  Total: {total_input:,} bytes")
    
    # Extract scholar sections
    section_scholar = extract_scholar_sections(sections, scholar1_dir, scholar2_dir)
    
    # Write section files
    total_output = 0
    total_entries = 0
    sections_with_content = 0
    
    for section in sections:
        section_id = section['id']
        scholar_list = section_scholar.get(section_id, [])
        
        if not scholar_list:
            continue
        
        sections_with_content += 1
        
        # Format output
        output_lines = []
        for start, end, marker, text in sorted(scholar_list, key=lambda x: x[0]):
            if marker:
                output_lines.append(f"[{start:03d}-{end:03d}] [{marker}]\n")
            else:
                output_lines.append(f"[{start:03d}-{end:03d}]\n")
            output_lines.append(text + "\n\n")
            total_entries += 1
        
        # Write file
        output_path = output_dir / f"{section_id}.txt"
        content = ''.join(output_lines)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        total_output += len(content)
    
    print(f"\n{'='*60}")
    print("SCHOLAR PARTITION COMPLETE")
    print(f"{'='*60}")
    
    print(f"\nStatistics:")
    print(f"  Sections with content: {sections_with_content}/{len(sections)}")
    print(f"  Total entries: {total_entries}")
    print(f"  Input: {total_input:,} bytes")
    print(f"  Output: {total_output:,} bytes")
    print(f"  Difference: {total_output - total_input:,} bytes")
    
    # Show samples
    print(f"\nSample files:")
    for sample_name in ["01-01-01-01.txt", "01-01-02-01.txt"]:
        sample_path = output_dir / sample_name
        if sample_path.exists():
            with open(sample_path, 'r', encoding='utf-8') as f:
                content = f.read()
                entries = content.count('[') // 2
                lines = content.split('\n')[:6]
                print(f"\n  {sample_name} ({len(content):,} chars, ~{entries} entries):")
                for line in lines:
                    if line.strip():
                        print(f"    {line[:90]}")


if __name__ == "__main__":
    main()
