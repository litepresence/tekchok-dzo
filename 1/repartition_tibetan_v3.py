#!/usr/bin/env python3
"""
Repartition Tibetan text using line-based extraction with phrase boundary tracking.
Tracks line duplications to achieve perfect byte accounting.
Uses Tibetan-only character counting for verification.
Adds a/b suffixes for split lines.
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
    Read a PAGE file and return list of (line_number, prefix, content, full_line) tuples.
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


def find_phrase_in_lines(lines, phrase, hint_line):
    """
    Find which line contains the phrase.
    Returns (line_index, is_at_line_start) or (None, None) if not found.
    """
    # Search around hint_line first (±5 lines)
    for offset in range(-5, 6):
        search_line = hint_line + offset
        for i, (line_num, prefix, content, full_line) in enumerate(lines):
            if line_num == search_line:
                # Strip leading space for comparison
                stripped_content = content.lstrip()
                if phrase in stripped_content:
                    # Check if phrase is at very start (after optional space)
                    is_at_start = stripped_content.startswith(phrase)
                    return i, is_at_start
    
    # If not found, search all lines
    for i, (line_num, prefix, content, full_line) in enumerate(lines):
        stripped_content = content.lstrip()
        if phrase in stripped_content:
            is_at_start = stripped_content.startswith(phrase)
            return i, is_at_start
    
    return None, None


def extract_section_content(section_data, next_section_data, volume_dir, prev_section_end_line=None):
    """
    Extract content for a section.
    Returns (content_lines, page_markers_added_bytes, end_line_info).
    end_line_info: (line_number, is_split) for the last line to pass to next section
    """
    section_id = section_data['id']
    start_page = section_data['start_page']
    start_phrase = section_data['start_phrase']
    start_hint = section_data['start_line']
    
    # Determine end boundary
    if next_section_data:
        end_page = next_section_data['start_page']
        end_phrase = next_section_data['start_phrase']
        end_hint = next_section_data['start_line']
    else:
        end_page = None
        end_phrase = None
        end_hint = None
    
    content_lines = []
    page_markers_bytes = 0
    current_page = start_page
    end_line_info = None
    
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
        
        # Determine which lines to include from this page
        if current_page == start_page:
            # First page - find where to start
            start_idx, start_at_beginning = find_phrase_in_lines(lines, start_phrase, start_hint)
            
            if start_idx is None:
                print(f"Warning: Could not find start phrase in section {section_id}")
                print(f"  Page {start_page}, line {start_hint}")
                break
            
            # Check if previous section ended with a split line
            if prev_section_end_line is not None:
                # This section starts with the 'b' part of a split line
                line_num, prefix, content, full_line = lines[start_idx]
                stripped = content.lstrip()
                start_pos = stripped.find(start_phrase)
                segment = stripped[start_pos:]
                if segment:
                    # Use 'b' suffix for the continuation
                    new_line = f"[{line_num}b] {segment}\n"
                    content_lines.append(new_line)
                # Continue with remaining lines
                start_idx += 1
            
            if end_page and current_page == end_page:
                # Both start and end on same page
                end_idx, end_at_beginning = find_phrase_in_lines(lines, end_phrase, end_hint)
                
                if end_idx is None:
                    # End phrase not found, include from start to end of page
                    for i in range(start_idx, len(lines)):
                        line_num, prefix, content, full_line = lines[i]
                        content_lines.append(full_line + '\n')
                elif end_idx == start_idx:
                    # Start and end on same line - unusual but possible
                    line_num, prefix, content, full_line = lines[start_idx]
                    stripped = content.lstrip()
                    start_pos = stripped.find(start_phrase)
                    end_pos = stripped.find(end_phrase)
                    
                    if start_pos < end_pos:
                        # Include from start phrase to end phrase
                        segment = stripped[start_pos:end_pos]
                        new_line = f"[{line_num}a] {segment}\n"
                        content_lines.append(new_line)
                        end_line_info = (line_num, True)  # Split line
                elif end_at_beginning:
                    # End phrase at start of line - include lines from start to line before end
                    for i in range(start_idx, end_idx):
                        line_num, prefix, content, full_line = lines[i]
                        content_lines.append(full_line + '\n')
                    end_line_info = (lines[end_idx][0], False)  # Not split
                else:
                    # End phrase mid-line - include up to the end phrase
                    for i in range(start_idx, end_idx):
                        line_num, prefix, content, full_line = lines[i]
                        content_lines.append(full_line + '\n')
                    
                    # Add partial last line up to end phrase with 'a' suffix
                    line_num, prefix, content, full_line = lines[end_idx]
                    stripped = content.lstrip()
                    end_pos = stripped.find(end_phrase)
                    segment = stripped[:end_pos]
                    if segment:
                        new_line = f"[{line_num}a] {segment}\n"
                        content_lines.append(new_line)
                    end_line_info = (line_num, True)  # Split line
            else:
                # Start on this page, continue to next pages
                for i in range(start_idx, len(lines)):
                    line_num, prefix, content, full_line = lines[i]
                    content_lines.append(full_line + '\n')
        
        elif end_page and current_page == end_page:
            # End page - find where to stop
            end_idx, end_at_beginning = find_phrase_in_lines(lines, end_phrase, end_hint)
            
            if end_idx is None:
                # End phrase not found, include all lines
                for line_num, prefix, content, full_line in lines:
                    content_lines.append(full_line + '\n')
            elif end_at_beginning:
                # End phrase at start of line - include lines before this one
                for i in range(0, end_idx):
                    line_num, prefix, content, full_line = lines[i]
                    content_lines.append(full_line + '\n')
                end_line_info = (lines[end_idx][0], False)  # Not split
            else:
                # End phrase mid-line - include lines before and partial
                for i in range(0, end_idx):
                    line_num, prefix, content, full_line = lines[i]
                    content_lines.append(full_line + '\n')
                
                # Add partial line up to end phrase with 'a' suffix
                line_num, prefix, content, full_line = lines[end_idx]
                stripped = content.lstrip()
                end_pos = stripped.find(end_phrase)
                segment = stripped[:end_pos]
                if segment:
                    new_line = f"[{line_num}a] {segment}\n"
                    content_lines.append(new_line)
                end_line_info = (line_num, True)  # Split line
            
            break
        
        else:
            # Middle page - include all lines
            for line_num, prefix, content, full_line in lines:
                content_lines.append(full_line + '\n')
        
        # Check if we've reached the end
        if end_page and current_page >= end_page:
            break
        
        if not end_page:
            # Last section - check if more pages exist
            next_page_path = volume_dir / f"PAGE_{current_page + 1:03d}.txt"
            if not next_page_path.exists():
                break
        
        current_page += 1
    
    return content_lines, page_markers_bytes, end_line_info


def count_tibetan_chars(text):
    """Count only Tibetan Unicode characters (U+0F00 to U+0FFF)."""
    return len(re.findall(r'[\u0F00-\u0FFF]', text))


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
    
    # Calculate input Tibetan character counts
    v1_tibetan = 0
    for page_file in volume1_dir.glob("PAGE_*.txt"):
        with open(page_file, 'r', encoding='utf-8') as f:
            v1_tibetan += count_tibetan_chars(f.read())
    
    v2_tibetan = 0
    for page_file in volume2_dir.glob("PAGE_*.txt"):
        with open(page_file, 'r', encoding='utf-8') as f:
            v2_tibetan += count_tibetan_chars(f.read())
    
    total_input_tibetan = v1_tibetan + v2_tibetan
    
    print(f"\nInput Tibetan characters:")
    print(f"  Volume 1: {v1_tibetan:,}")
    print(f"  Volume 2: {v2_tibetan:,}")
    print(f"  Total: {total_input_tibetan:,}")
    
    # Process sections
    total_page_markers = 0
    total_output_tibetan = 0
    prev_end_line = None
    
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
                next_section = None
        
        # Extract content
        content_lines, markers_bytes, end_line_info = extract_section_content(
            section, next_section, volume_dir, prev_end_line
        )
        total_page_markers += markers_bytes
        
        # Store end line info for next section
        prev_end_line = end_line_info
        
        # Write section file
        output_path = output_dir / f"{section_id}.txt"
        content = ''.join(content_lines)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Count Tibetan characters
        total_output_tibetan += count_tibetan_chars(content)
        
        if (i + 1) % 50 == 0:
            print(f"Processed {i + 1}/{len(sections)} sections...")
    
    print(f"\n{'='*60}")
    print("REPARTITION COMPLETE")
    print(f"{'='*60}")
    
    print(f"\nTibetan Character Accounting:")
    print(f"  Input: {total_input_tibetan:,} Tibetan chars")
    print(f"  Output: {total_output_tibetan:,} Tibetan chars")
    diff = total_output_tibetan - total_input_tibetan
    print(f"  Difference: {diff:,} chars ({diff/total_input_tibetan*100:.4f}%)")
    
    if diff == 0:
        print("\n  ✓ PERFECT MATCH - ZERO DIFFERENCE!")
    elif abs(diff) < 10:
        print(f"\n  ✓ ACCEPTABLE: {diff} chars")
    else:
        print(f"\n  ⚠ WARNING: {diff:,} char difference")
    
    # Show samples
    print(f"\nSample files:")
    for sample_name in ["01-01-01-01.txt", "01-01-02-01.txt", "01-02-01-03.txt", "01-02-01-04.txt", "01-02-01-05.txt"]:
        sample_path = output_dir / sample_name
        if sample_path.exists():
            with open(sample_path, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')[:3]
                print(f"\n  {sample_name} ({len(content):,} chars, {count_tibetan_chars(content):,} Tibetan chars):")
                for line in lines:
                    if line.strip():
                        print(f"    {line[:80]}")


if __name__ == "__main__":
    main()
