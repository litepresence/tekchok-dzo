#!/usr/bin/env python3
"""
Repartition Tibetan text using line-based extraction with phrase boundary tracking.

Tracks line duplications to achieve perfect byte accounting.
Sections split mid-line will duplicate the line number in both sections.
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
    """
    Read a PAGE file and return list of (line_number, line_content) tuples.
    Line content includes the [number] prefix.
    """
    lines = []
    if not page_path.exists():
        return lines
    
    with open(page_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n\r')
            match = re.match(r'^(\[(\d+)\])(.*)', line)
            if match:
                full_prefix = match.group(1)  # e.g., "[1]"
                line_num = int(match.group(2))  # e.g., 1
                content = match.group(3)  # content after [number]
                lines.append((line_num, full_prefix, content, line))
    
    return lines


def find_phrase_location(lines, phrase, hint_line):
    """
    Find which line contains the phrase and where within the line.
    Returns (line_index, char_offset, is_at_line_start).
    """
    # Search around hint_line first (±5 lines)
    for offset in range(-5, 6):
        search_line = hint_line + offset
        for i, (line_num, prefix, content, full_line) in enumerate(lines):
            if line_num == search_line:
                if phrase in content:
                    char_offset = content.find(phrase)
                    # Check if phrase is at start of content (allowing for leading space)
                    is_at_start = (char_offset <= 1)
                    return i, char_offset, is_at_start
    
    # If not found, search all lines
    for i, (line_num, prefix, content, full_line) in enumerate(lines):
        if phrase in content:
            char_offset = content.find(phrase)
            is_at_start = (char_offset == 0)
            return i, char_offset, is_at_start
    
    return None, None, None


def extract_section_content(section_data, next_section_data, volume_dir):
    """
    Extract content for a section.
    Handles phrase-based boundaries and tracks line number duplications.
    
    Returns (content_lines, page_markers_added_bytes, duplicated_line_number_bytes).
    """
    section_id = section_data['id']
    start_page = section_data['start_page']
    start_phrase = section_data['start_phrase']
    hint_line = section_data['start_line']
    
    # Determine end boundary
    if next_section_data:
        end_page = next_section_data['start_page']
        end_phrase = next_section_data['start_phrase']
        end_hint_line = next_section_data['start_line']
    else:
        end_page = None
        end_phrase = None
        end_hint_line = None
    
    content_lines = []
    page_markers_bytes = 0
    duplicated_line_number_bytes = 0
    current_page = start_page
    started = False
    
    while True:
        page_path = volume_dir / f"PAGE_{current_page:03d}.txt"
        lines = read_page_lines(page_path)
        
        if not lines:
            print(f"Warning: Could not read page {current_page}")
            break
        
        # Add page marker if not first page
        if current_page > start_page:
            marker = f"\n\n### PAGE {current_page}\n\n"
            content_lines.append(marker)
            page_markers_bytes += len(marker.encode('utf-8'))
        
        # Handle start of section
        if not started and current_page == start_page:
            line_idx, char_offset, is_at_start = find_phrase_location(lines, start_phrase, hint_line)
            
            if line_idx is None:
                print(f"Warning: Could not find start phrase in section {section_id}")
                print(f"  Page {start_page}, hint line {hint_line}")
                print(f"  Phrase: {start_phrase[:50]}...")
                break
            
            started = True
            
            if is_at_start:
                # Phrase at start of line - include from this line onward
                for i in range(line_idx, len(lines)):
                    line_num, prefix, content, full_line = lines[i]
                    content_lines.append(full_line + '\n')
            else:
                # Phrase mid-line - split this line, include from phrase
                line_num, prefix, content, full_line = lines[line_idx]
                # Content from phrase onward (strip leading space if present)
                split_content = content[char_offset:].lstrip()
                new_line = f"{prefix} {split_content}\n"
                content_lines.append(new_line)
                # Remaining lines
                for i in range(line_idx + 1, len(lines)):
                    line_num, prefix, content, full_line = lines[i]
                    content_lines.append(full_line + '\n')
        
        # Handle end of section
        elif end_phrase and current_page == end_page:
            line_idx, char_offset, is_at_start = find_phrase_location(lines, end_phrase, end_hint_line)
            
            if line_idx is None:
                # End phrase not found on this page, include all lines
                for line_num, prefix, content, full_line in lines:
                    content_lines.append(full_line + '\n')
            else:
                if is_at_start:
                    # Phrase at start of line - section ends BEFORE this line
                    # Include lines before this one
                    for i in range(0, line_idx):
                        line_num, prefix, content, full_line = lines[i]
                        content_lines.append(full_line + '\n')
                else:
                    # Phrase mid-line - split this line, include up to phrase
                    line_num, prefix, content, full_line = lines[line_idx]
                    # Include lines before this one first
                    for i in range(0, line_idx):
                        prev_line_num, prev_prefix, prev_content, prev_full_line = lines[i]
                        content_lines.append(prev_full_line + '\n')
                    # Content before phrase (trim trailing whitespace)
                    split_content = content[:char_offset].rstrip()
                    if split_content:  # Only add if there's content before the phrase
                        new_line = f"{prefix} {split_content}\n"
                        content_lines.append(new_line)
                        # Track duplication: the line number will appear in both sections
                        duplicated_line_number_bytes += len(prefix.encode('utf-8'))
            
            # We've reached the end
            break
        
        # Middle pages - include all lines
        else:
            for line_num, prefix, content, full_line in lines:
                content_lines.append(full_line + '\n')
        
        # Move to next page
        if end_page and current_page >= end_page:
            break
        
        if not end_page:
            # Last section - check if more pages exist
            next_page_path = volume_dir / f"PAGE_{current_page + 1:03d}.txt"
            if not next_page_path.exists():
                break
        
        current_page += 1
    
    return content_lines, page_markers_bytes, duplicated_line_number_bytes


def main():
    # Paths
    base_dir = Path("/home/opencode/MDZOD/1")
    concise_path = base_dir / "boundary_concise.json"
    volume1_dir = base_dir / "volume_1" / "tibetan"
    volume2_dir = base_dir / "volume_2" / "tibetan"
    output_dir = base_dir / "text" / "tibetan"
    
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
    v1_size = sum(f.stat().st_size for f in volume1_dir.glob("*.txt"))
    v2_size = sum(f.stat().st_size for f in volume2_dir.glob("*.txt"))
    total_input = v1_size + v2_size
    
    print(f"\nInput sizes:")
    print(f"  Volume 1: {v1_size:,} bytes ({len(list(volume1_dir.glob('*.txt')))} pages)")
    print(f"  Volume 2: {v2_size:,} bytes ({len(list(volume2_dir.glob('*.txt')))} pages)")
    print(f"  Total: {total_input:,} bytes")
    
    # Process sections
    total_page_markers = 0
    total_duplicated_bytes = 0
    total_output = 0
    
    for i, section in enumerate(sections):
        section_id = section['id']
        volume, _, _, _ = parse_section_id(section_id)
        volume_dir = get_volume_dir(volume, volume1_dir, volume2_dir)
        
        # Get next section for end boundary
        next_section = sections[i + 1] if i < len(sections) - 1 else None
        
        # Verify volumes match for end boundary
        if next_section:
            next_vol, _, _, _ = parse_section_id(next_section['id'])
            if next_vol != volume:
                next_section = None  # Last section of this volume
        
        # Extract content
        content_lines, markers_bytes, dup_bytes = extract_section_content(
            section, next_section, volume_dir
        )
        
        total_page_markers += markers_bytes
        total_duplicated_bytes += dup_bytes
        
        # Write section file
        output_path = output_dir / f"{section_id}.txt"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.writelines(content_lines)
        
        output_size = output_path.stat().st_size
        total_output += output_size
        
        if (i + 1) % 50 == 0:
            print(f"Processed {i + 1}/{len(sections)} sections...")
    
    print(f"\n{'='*60}")
    print("REPARTITION COMPLETE")
    print(f"{'='*60}")
    
    print(f"\nAccounting:")
    print(f"  Input: {total_input:,} bytes")
    print(f"  + Page markers: {total_page_markers:,} bytes")
    print(f"  + Duplicated line numbers: {total_duplicated_bytes:,} bytes")
    print(f"  = Expected: {total_input + total_page_markers + total_duplicated_bytes:,} bytes")
    print(f"  Actual: {total_output:,} bytes")
    
    diff = total_output - (total_input + total_page_markers + total_duplicated_bytes)
    print(f"  Difference: {diff:,} bytes")
    
    if diff == 0:
        print("\n  ✓ PERFECT MATCH - ZERO BYTE DIFFERENCE!")
    elif abs(diff) < 10:
        print(f"\n  ✓ ACCEPTABLE: {diff} bytes")
    else:
        print(f"\n  ⚠ WARNING: {diff:,} byte difference")
    
    # Show samples
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
