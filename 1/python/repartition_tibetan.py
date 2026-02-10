#!/usr/bin/env python3
"""
Repartition Tibetan text from PAGE-based to section-based structure.

Reads boundary_concise.json and volume_1/tibetan + volume_2/tibetan PAGE files,
creates section files in text/tibetan/ with flat structure.

Uses phrase-based extraction: sections start at their start_phrase and end at
the next section's start_phrase.

Filename format: VV-CC-SS-ss.txt (Volume-Chapter-Section-Subsection)
"""

import json
import re
from pathlib import Path


def parse_section_id(section_id):
    """Parse section_id like '01-01-01-01' into (volume, chapter, section, subsection)."""
    parts = section_id.split('-')
    if len(parts) != 4:
        raise ValueError(f"Invalid section_id format: {section_id}")
    return tuple(int(p) for p in parts)


def find_phrase_in_page(page_path, phrase, hint_line, section_id):
    """
    Find phrase in page file, returning (line_number, line_content, char_offset).
    Uses hint_line as starting point but searches nearby lines.
    Returns None if not found.
    """
    if not page_path.exists():
        return None
    
    lines = []
    with open(page_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Build line lookup with line numbers
    line_lookup = {}
    for i, line in enumerate(lines):
        match = re.match(r'\[(\d+)\]', line.strip())
        if match:
            line_num = int(match.group(1))
            line_lookup[line_num] = (i, line)
    
    # Search around hint_line first (±5 lines)
    search_range = list(range(hint_line - 5, hint_line + 6))
    
    # Then search all lines if not found
    all_line_nums = sorted(line_lookup.keys())
    search_order = search_range + [ln for ln in all_line_nums if ln not in search_range]
    
    for line_num in search_order:
        if line_num in line_lookup:
            idx, line_content = line_lookup[line_num]
            # Search for phrase in this line (exact match)
            if phrase in line_content:
                char_offset = line_content.find(phrase)
                return (line_num, line_content, char_offset)
    
    return None


def get_page_lines_dict(page_path):
    """Read a PAGE file and return dict of {line_number: line_content}."""
    lines_by_number = {}
    if not page_path.exists():
        return lines_by_number
    
    with open(page_path, 'r', encoding='utf-8') as f:
        for line in f:
            line_stripped = line.rstrip('\n\r')
            match = re.match(r'\[(\d+)\]', line_stripped)
            if match:
                line_num = int(match.group(1))
                lines_by_number[line_num] = line_stripped
    
    return lines_by_number


def get_last_line_of_page(page_path):
    """Get the highest line number in a page file."""
    lines = get_page_lines_dict(page_path)
    if not lines:
        return None
    return max(lines.keys())


def extract_section_content(section, next_section, volume1_dir, volume2_dir):
    """
    Extract content for a section.
    Section starts at its phrase and ends at next_section's phrase (or end of volume).
    Returns (content_lines, page_markers_added_bytes).
    """
    section_id = section['id']
    start_page = section['start_page']
    hint_line = section['start_line']
    start_phrase = section['start_phrase']
    
    volume, _, _, _ = parse_section_id(section_id)
    source_dir = volume1_dir if volume == 1 else volume2_dir
    
    # Determine end point
    if next_section:
        end_page = next_section['start_page']
        end_phrase = next_section['start_phrase']
        # We stop BEFORE this phrase
    else:
        # Last section - go to end of volume
        end_page = None
        end_phrase = None
    
    content_lines = []
    page_markers_added = 0
    current_page = start_page
    found_start = False
    
    while True:
        page_path = source_dir / f"PAGE_{current_page:03d}.txt"
        page_lines = get_page_lines_dict(page_path)
        
        if not page_lines:
            print(f"Warning: Could not read page {current_page} for section {section_id}")
            current_page += 1
            if end_page and current_page > end_page:
                break
            continue
        
        # Add page marker if not first page of section
        if current_page > start_page:
            marker = f"\n\n### PAGE {current_page}\n\n"
            content_lines.append(marker)
            page_markers_added += len(marker.encode('utf-8'))
        
        # Sort lines by line number
        sorted_line_nums = sorted(page_lines.keys())
        
        for line_num in sorted_line_nums:
            line_content = page_lines[line_num]
            
            # Handle start of section
            if not found_start:
                if current_page == start_page and line_num >= hint_line - 10:
                    # Look for start phrase
                    if start_phrase in line_content:
                        # Found start - include from this point
                        found_start = True
                        # Include the full line (we don't truncate at phrase)
                        content_lines.append(line_content + '\n')
                    # If we haven't found it yet, keep looking
                continue
            
            # Handle end of section
            if end_page and current_page == end_page and end_phrase in line_content:
                # Found end phrase - stop BEFORE this line
                break
            
            # Regular content line
            content_lines.append(line_content + '\n')
        
        # Check if we've reached end
        if end_page and current_page >= end_page:
            break
        
        # Check if we've gone past end page (shouldn't happen)
        if end_page and current_page > end_page:
            break
        
        # Check if no end_page specified (last section of volume)
        if not end_page:
            # Check if next page exists
            next_page_path = source_dir / f"PAGE_{current_page + 1:03d}.txt"
            if not next_page_path.exists():
                break
        
        current_page += 1
    
    if not found_start:
        print(f"Warning: Could not find start phrase for section {section_id}")
        print(f"  Page {start_page}, hint line {hint_line}, phrase: {start_phrase[:50]}...")
    
    return content_lines, page_markers_added


def calculate_directory_size(directory, pattern="*.txt"):
    """Calculate total bytes of all matching files in directory."""
    total_bytes = 0
    if not directory.exists():
        return 0
    
    for txt_file in directory.glob(pattern):
        total_bytes += txt_file.stat().st_size
    
    return total_bytes


def main():
    # Paths
    base_dir = Path("/home/opencode/MDZOD/1")
    concise_path = base_dir / "boundary_concise.json"
    volume1_dir = base_dir / "volume_1" / "tibetan"
    volume2_dir = base_dir / "volume_2" / "tibetan"
    output_dir = base_dir / "text" / "tibetan"
    
    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Load concise boundary data
    with open(concise_path, 'r', encoding='utf-8') as f:
        concise_data = json.load(f)
    
    sections = concise_data['sections']
    print(f"Loaded {len(sections)} sections from boundary_concise.json")
    
    # Calculate input sizes before processing
    input_v1_size = calculate_directory_size(volume1_dir)
    input_v2_size = calculate_directory_size(volume2_dir)
    total_input_size = input_v1_size + input_v2_size
    
    print(f"\nInput sizes:")
    print(f"  Volume 1: {input_v1_size:,} bytes")
    print(f"  Volume 2: {input_v2_size:,} bytes")
    print(f"  Total: {total_input_size:,} bytes")
    
    # Process sections
    total_page_markers_added = 0
    sections_processed = 0
    v1_sections = 0
    v2_sections = 0
    
    for i, section in enumerate(sections):
        section_id = section['id']
        volume, _, _, _ = parse_section_id(section_id)
        
        # Get next section to determine end point
        next_section = sections[i + 1] if i < len(sections) - 1 else None
        
        # Verify next section is in same volume
        if next_section:
            next_vol, _, _, _ = parse_section_id(next_section['id'])
            if next_vol != volume:
                next_section = None  # Last section of this volume
        
        if volume == 1:
            v1_sections += 1
        else:
            v2_sections += 1
        
        # Extract content
        content_lines, markers_bytes = extract_section_content(
            section, next_section, volume1_dir, volume2_dir
        )
        total_page_markers_added += markers_bytes
        
        # Create output file
        output_path = output_dir / f"{section_id}.txt"
        
        # Write content
        with open(output_path, 'w', encoding='utf-8') as f:
            f.writelines(content_lines)
        
        sections_processed += 1
        
        if sections_processed % 50 == 0:
            print(f"Processed {sections_processed}/{len(sections)} sections...")
    
    print(f"\nProcessed {sections_processed} sections:")
    print(f"  Volume 1: {v1_sections} sections")
    print(f"  Volume 2: {v2_sections} sections")
    
    # Calculate output sizes
    output_v1_size = calculate_directory_size(output_dir, "01-*.txt")
    output_v2_size = calculate_directory_size(output_dir, "02-*.txt")
    total_output_size = calculate_directory_size(output_dir)
    
    print(f"\nOutput sizes:")
    print(f"  Volume 1 (01-*): {output_v1_size:,} bytes")
    print(f"  Volume 2 (02-*): {output_v2_size:,} bytes")
    print(f"  Total: {total_output_size:,} bytes")
    
    # Verify byte counts
    print(f"\nVerification:")
    print(f"  Page markers added: {total_page_markers_added:,} bytes")
    print(f"  Expected output: {total_input_size + total_page_markers_added:,} bytes")
    print(f"  Actual output: {total_output_size:,} bytes")
    
    size_difference = total_output_size - (total_input_size + total_page_markers_added)
    
    if size_difference == 0:
        print(f"  ✓ PERFECT MATCH: Output size equals input + markers")
    elif abs(size_difference) < 100:
        print(f"  ✓ ACCEPTABLE: Difference of {size_difference} bytes")
    else:
        print(f"  ✗ MISMATCH: Difference of {size_difference:,} bytes")
        print(f"    This may indicate missing or extra content")
    
    # Show sample files
    print(f"\nSample output files:")
    sample_v1 = sorted(output_dir.glob("01-*.txt"))[:1]
    sample_v2 = sorted(output_dir.glob("02-*.txt"))[:1]
    
    for sample in sample_v1 + sample_v2:
        with open(sample, 'r', encoding='utf-8') as f:
            sample_content = f.read()
            print(f"\n  {sample.name} ({len(sample_content):,} chars):")
            preview = sample_content[:500].replace('\n', ' ')
            print(f"  Preview: {preview}...")


if __name__ == "__main__":
    main()
