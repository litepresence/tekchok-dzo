#!/usr/bin/env python3
"""
Partition epistemic, delusion, and cognitive layers.
For delusion: adds line number ranges based on PAGE boundaries before partitioning.
"""

import json
import re
from pathlib import Path


def parse_section_id(section_id):
    """Parse section_id like '01-01-01-01' into (volume, chapter, section, subsection)."""
    parts = section_id.split('-')
    return tuple(int(p) for p in parts)


def get_volume_dir(volume, v1_dir, v2_dir):
    """Return the appropriate volume directory."""
    return v1_dir if volume == 1 else v2_dir


def build_section_boundaries(sections):
    """Build lookup of section boundaries by volume."""
    boundaries = {}
    for i, section in enumerate(sections):
        section_id = section['id']
        start_line = section['start_line']
        volume = int(section_id.split('-')[0])
        
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


def read_page_line_ranges(volume_dir):
    """Build mapping of PAGE file -> (first_line, last_line) from Tibetan."""
    page_ranges = {}
    tibetan_dir = volume_dir.parent / "tibetan"
    
    for page_file in sorted(tibetan_dir.glob("PAGE_*.txt")):
        page_num = int(page_file.stem.split('_')[1])
        with open(page_file, 'r', encoding='utf-8') as f:
            lines = [l for l in f.read().split('\n') if re.match(r'^\[\d+\]', l)]
            if lines:
                first_match = re.match(r'\[(\d+)\]', lines[0])
                last_match = re.match(r'\[(\d+)\]', lines[-1])
                if first_match and last_match:
                    page_ranges[page_num] = (int(first_match.group(1)), int(last_match.group(1)))
    return page_ranges


def read_epistemic_entries(page_path):
    """Read epistemic PAGE file and return list of (start, end, view, declarative, text)."""
    entries = []
    if not page_path.exists():
        return entries
    
    with open(page_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Parse line by line looking for [START-END] patterns
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        # Look for [START-END] pattern (with or without "Line range " prefix)
        match = re.search(r'\[(\d+)-(\d+)\]', line)
        if match and i + 2 < len(lines):
            start = int(match.group(1))
            end = int(match.group(2))
            
            # Collect all bracketed markers until we hit non-bracketed content
            markers = []
            i += 1
            while i < len(lines):
                marker_line = lines[i].strip()
                if not marker_line.startswith('['):
                    break
                marker_match = re.match(r'\[([^\]]+)\]', marker_line)
                if not marker_match:
                    break
                markers.append(marker_match.group(1))
                i += 1
            
            # Need at least 2 markers (view and declarative)
            if len(markers) < 2:
                continue
            
            view = markers[0]
            declarative = markers[1]
            
            # Collect text until next entry or end
            text_lines = []
            while i < len(lines):
                if lines[i].strip().startswith('[---') or re.match(r'\[\d+-\d+\]', lines[i].strip()):
                    break
                text_lines.append(lines[i])
                i += 1
            
            text = ''.join(text_lines).strip()
            if text:
                entries.append((start, end, view, declarative, text))
        else:
            i += 1
    
    return entries


def read_cognitive_entries(page_path):
    """Read cognitive PAGE file and return list of (start, end, text)."""
    entries = []
    if not page_path.exists():
        return entries
    
    with open(page_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern: [START-END]\n<content>
    pattern = r'\[(\d+)-(\d+)\]\s*\n(.*?)(?=\[\d+-\d+\]|\Z)'
    for match in re.finditer(pattern, content, re.DOTALL):
        start = int(match.group(1))
        end = int(match.group(2))
        text = match.group(3).strip()
        if text:
            entries.append((start, end, text))
    
    return entries


def read_delusion_entries(page_path, page_ranges):
    """Read delusion PAGE file and add line numbers from page_ranges."""
    entries = []
    if not page_path.exists():
        return entries
    
    page_num = int(page_path.stem.split('_')[1])
    if page_num not in page_ranges:
        return entries
    
    first_line, last_line = page_ranges[page_num]
    
    with open(page_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by error type headers
    # Pattern: [ERROR TYPE] [SUBTYPE]\n\n<content>
    pattern = r'(\[[^\]]+\]\s*\[[^\]]+\])\s*\n\n(.*?)(?=\[[^\]]+\]\s*\[[^\]]+\]|\Z)'
    matches = list(re.finditer(pattern, content, re.DOTALL))
    
    for i, match in enumerate(matches):
        error_header = match.group(1).strip()
        text = match.group(2).strip()
        if text:
            # Assign range based on position within page
            if len(matches) == 1:
                # Single entry for page - use full range
                entries.append((first_line, last_line, error_header, text))
            else:
                # Multiple entries - split range proportionally
                portion_size = (last_line - first_line + 1) / len(matches)
                entry_first = int(first_line + (i * portion_size))
                entry_last = int(first_line + ((i + 1) * portion_size) - 1)
                entries.append((entry_first, entry_last, error_header, text))
    
    return entries


def extract_layer_sections(sections, v1_dir, v2_dir, read_func, is_delusion=False):
    """Extract layer entries organized by Tibetan section boundaries."""
    boundaries = build_section_boundaries(sections)
    
    section_entries = {}
    for section in sections:
        section_entries[section['id']] = []
    
    # Get page ranges for delusion layer
    page_ranges = {}
    if is_delusion:
        page_ranges = {**read_page_line_ranges(v1_dir), **read_page_line_ranges(v2_dir)}
    
    for volume in [1, 2]:
        layer_dir = get_volume_dir(volume, v1_dir, v2_dir)
        volume_boundaries = boundaries.get(volume, [])
        
        if not volume_boundaries:
            continue
        
        for page_file in sorted(layer_dir.glob('PAGE_*.txt')):
            if is_delusion:
                entries = read_delusion_entries(page_file, page_ranges)
            else:
                entries = read_func(page_file)
            
            for entry in entries:
                if is_delusion:
                    start_line, end_line, error_header, text = entry
                    marker = error_header
                else:
                    start_line, end_line = entry[0], entry[1]
                    text = entry[-1]
                    marker = entry[2] if len(entry) > 3 else ""
                
                start_section = get_section_for_line(start_line, volume_boundaries)
                end_section = get_section_for_line(end_line, volume_boundaries)
                
                if not start_section:
                    continue
                
                if start_section == end_section or not end_section:
                    section_entries[start_section].append((start_line, end_line, marker, text))
                else:
                    # Split at boundary
                    boundary_line = None
                    for sec_start, sec_end, sec_id in volume_boundaries:
                        if sec_id == start_section:
                            boundary_line = sec_end
                            break
                    
                    if boundary_line:
                        section_entries[start_section].append((start_line, boundary_line, marker, text))
                        section_entries[end_section].append((boundary_line + 1, end_line, marker, text))
                    else:
                        section_entries[start_section].append((start_line, end_line, marker, text))
    
    return section_entries


def main():
    base_dir = Path("/home/opencode/MDZOD/1")
    concise_path = base_dir / "boundary_concise.json"
    
    # Load boundary data
    with open(concise_path, 'r', encoding='utf-8') as f:
        concise_data = json.load(f)
    sections = concise_data['sections']
    
    print("="*60)
    print("PARTITIONING THREE LAYERS")
    print("="*60)
    
    # Process each layer
    layers = [
        ('epistemic', read_epistemic_entries, False),
        ('delusion', None, True),
        ('cognitive', read_cognitive_entries, False)
    ]
    
    for layer_name, read_func, is_delusion in layers:
        print(f"\n{layer_name.upper()} LAYER")
        print("-"*60)
        
        v1_dir = base_dir / "volume_1" / layer_name
        v2_dir = base_dir / "volume_2" / layer_name
        output_dir = base_dir / "text" / layer_name
        
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Clear existing
        for f in output_dir.glob("*.txt"):
            f.unlink()
        
        # Extract entries
        section_entries = extract_layer_sections(sections, v1_dir, v2_dir, read_func, is_delusion)
        
        # Write section files
        total_output = 0
        sections_with_content = 0
        total_entries = 0
        
        for section in sections:
            section_id = section['id']
            entries = section_entries.get(section_id, [])
            
            if not entries:
                continue
            
            sections_with_content += 1
            
            output_lines = []
            for start, end, marker, text in sorted(entries, key=lambda x: x[0]):
                if is_delusion:
                    output_lines.append(f"[{start:03d}-{end:03d}] {marker}\n")
                elif layer_name == 'epistemic':
                    output_lines.append(f"[{start:03d}-{end:03d}] [{marker}]\n")
                else:
                    output_lines.append(f"[{start:03d}-{end:03d}]\n")
                output_lines.append(text + "\n\n")
                total_entries += 1
            
            output_path = output_dir / f"{section_id}.txt"
            content = ''.join(output_lines)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            total_output += len(content)
        
        print(f"  Sections with content: {sections_with_content}")
        print(f"  Total entries: {total_entries}")
        print(f"  Output: {total_output:,} bytes")
    
    print("\n" + "="*60)
    print("ALL THREE LAYERS COMPLETE")
    print("="*60)


if __name__ == "__main__":
    main()
