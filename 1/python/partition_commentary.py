#!/usr/bin/env python3
"""
Partition commentary layer using Tibetan boundaries.
Splits commentary paragraphs at logical breaks when they span sections.
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
    """Read commentary PAGE file and return list of (start_line, end_line, text) tuples."""
    paragraphs = []
    if not page_path.exists():
        return paragraphs
    
    with open(page_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all [N-M] patterns with their text
    pattern = r'\[(\d+)-(\d+)\](.*?)(?=\[\d+-\d+\]|\Z)'
    for match in re.finditer(pattern, content, re.DOTALL):
        start_line = int(match.group(1))
        end_line = int(match.group(2))
        text = match.group(3).strip()
        if text:
            paragraphs.append((start_line, end_line, text))
    
    return paragraphs


def split_at_logical_break(text, target_char_count):
    """
    Split text at a logical break (sentence end) close to target character count.
    Returns (first_part, second_part).
    """
    if len(text) <= target_char_count:
        return text, ""
    
    # Look for sentence endings (. ! ?) near the target
    sentences = re.split(r'(?<=[.!?])\s+', text)
    
    first_part = ""
    second_part = text
    current_len = 0
    
    for i, sentence in enumerate(sentences):
        if current_len + len(sentence) <= target_char_count or not first_part:
            first_part += sentence + " "
            current_len += len(sentence) + 1
        else:
            # Found the split point
            second_part = " ".join(sentences[i:]).strip()
            break
    
    first_part = first_part.strip()
    
    return first_part, second_part


def build_section_boundaries(sections):
    """Build lookup of which section each line belongs to."""
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
                # Last section of volume
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


def extract_commentary_sections(sections, commentary1_dir, commentary2_dir):
    """Extract commentary organized by Tibetan section boundaries."""
    boundaries = build_section_boundaries(sections)
    
    # Initialize sections dict
    section_commentary = {}  # section_id -> list of (start, end, text)
    for section in sections:
        section_commentary[section['id']] = []
    
    # Process both volumes
    for volume in [1, 2]:
        commentary_dir = commentary1_dir if volume == 1 else commentary2_dir
        volume_boundaries = boundaries.get(volume, [])
        
        if not volume_boundaries:
            continue
        
        # Read all commentary paragraphs
        for page_file in sorted(commentary_dir.glob('PAGE_*.txt')):
            paragraphs = read_page_lines(page_file)
            
            for start_line, end_line, text in paragraphs:
                # Check which section(s) this paragraph belongs to
                start_section = get_section_for_line(start_line, volume_boundaries)
                end_section = get_section_for_line(end_line, volume_boundaries)
                
                if start_section is None or end_section is None:
                    continue
                
                if start_section == end_section:
                    # Fits entirely in one section
                    section_commentary[start_section].append((start_line, end_line, text))
                else:
                    # Spans multiple sections - need to split
                    # Find the boundary line between start_section and end_section
                    boundary_line = None
                    for sec_start, sec_end, sec_id in volume_boundaries:
                        if sec_id == start_section:
                            boundary_line = sec_end
                            break
                    
                    if boundary_line:
                        # Calculate proportional split
                        total_lines = end_line - start_line + 1
                        lines_in_first = boundary_line - start_line + 1
                        
                        # Split text proportionally at logical break
                        target_chars = int(len(text) * (lines_in_first / total_lines))
                        first_text, second_text = split_at_logical_break(text, target_chars)
                        
                        # Add to first section
                        if first_text:
                            section_commentary[start_section].append((start_line, boundary_line, first_text))
                        
                        # Add remaining to subsequent sections
                        remaining_text = second_text
                        remaining_start = boundary_line + 1
                        
                        for sec_start, sec_end, sec_id in volume_boundaries:
                            if sec_start >= remaining_start and remaining_text:
                                if sec_id == end_section:
                                    # Last section gets remainder
                                    section_commentary[sec_id].append((sec_start, end_line, remaining_text))
                                    break
                                elif sec_start <= end_line:
                                    # Middle section
                                    section_commentary[sec_id].append((sec_start, sec_end, remaining_text))
                                    remaining_text = ""
                                    remaining_start = sec_end + 1
    
    return section_commentary


def main():
    base_dir = Path("/home/opencode/MDZOD/1")
    concise_path = base_dir / "boundary_concise.json"
    commentary1_dir = base_dir / "volume_1" / "commentary"
    commentary2_dir = base_dir / "volume_2" / "commentary"
    output_dir = base_dir / "text" / "commentary"
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Clear existing files
    for f in output_dir.glob("*.txt"):
        f.unlink()
    
    # Load boundary data
    with open(concise_path, 'r', encoding='utf-8') as f:
        concise_data = json.load(f)
    
    sections = concise_data['sections']
    print(f"Loaded {len(sections)} sections")
    
    # Extract commentary
    section_commentary = extract_commentary_sections(sections, commentary1_dir, commentary2_dir)
    
    # Write section files
    total_input = 0
    total_output = 0
    total_paragraphs = 0
    
    for section in sections:
        section_id = section['id']
        commentary_list = section_commentary.get(section_id, [])
        
        if not commentary_list:
            continue
        
        # Format output
        output_lines = []
        for start, end, text in sorted(commentary_list, key=lambda x: x[0]):
            output_lines.append(f"[{start}-{end}]\n")
            output_lines.append(text + "\n\n")
            total_paragraphs += 1
        
        # Write file
        output_path = output_dir / f"{section_id}.txt"
        content = ''.join(output_lines)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        total_output += len(content)
    
    # Calculate input size
    for page_file in list(commentary1_dir.glob('PAGE_*.txt')) + list(commentary2_dir.glob('PAGE_*.txt')):
        with open(page_file, 'r') as f:
            total_input += len(f.read())
    
    print(f"\n{'='*60}")
    print("COMMENTARY PARTITION COMPLETE")
    print(f"{'='*60}")
    
    print(f"\nStatistics:")
    print(f"  Input: {total_input:,} chars")
    print(f"  Output: {total_output:,} chars")
    print(f"  Paragraphs: {total_paragraphs}")
    
    # Show samples
    print(f"\nSample files:")
    for sample_name in ["01-01-01-01.txt", "01-01-02-01.txt"]:
        sample_path = output_dir / sample_name
        if sample_path.exists():
            with open(sample_path, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')[:10]
                print(f"\n  {sample_name} ({len(content):,} chars):")
                for line in lines:
                    if line.strip():
                        print(f"    {line[:80]}")


if __name__ == "__main__":
    main()
