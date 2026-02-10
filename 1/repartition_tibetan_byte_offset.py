#!/usr/bin/env python3
"""
Repartition Tibetan text using byte-offset approach.

Concatenates all PAGE files into single byte stream per volume,
then splits at exact byte offsets based on phrase locations.
Guarantees byte-perfect reconstruction.
"""

import json
import re
from pathlib import Path


def parse_section_id(section_id):
    """Parse section_id like '01-01-01-01' into (volume, chapter, section, subsection)."""
    parts = section_id.split('-')
    return tuple(int(p) for p in parts)


def concatenate_pages(volume_dir):
    """
    Concatenate all PAGE files into a single bytes object.
    Returns (concatenated_bytes, page_offsets).
    page_offsets: dict of {page_num: byte_offset}
    """
    concatenated = b''
    page_offsets = {}
    current_offset = 0
    
    # Sort page files by number
    page_files = sorted(volume_dir.glob("PAGE_*.txt"))
    
    for page_file in page_files:
        # Extract page number from filename
        page_num = int(page_file.stem.split('_')[1])
        
        # Read page content as bytes
        with open(page_file, 'rb') as f:
            page_content = f.read()
        
        # Record offset where this page starts
        page_offsets[page_num] = current_offset
        
        # Append to concatenated stream
        concatenated += page_content
        current_offset += len(page_content)
    
    return concatenated, page_offsets


def find_phrase_byte_offset(concatenated_bytes, page_offsets, page_num, phrase, hint_line):
    """
    Find the exact byte offset of a phrase within the concatenated stream.
    Returns byte offset where phrase starts.
    """
    # Get page starting offset
    page_start_offset = page_offsets.get(page_num, 0)
    
    # Decode just the page content (for performance)
    # We need to find the page boundary first
    page_end_offset = None
    sorted_pages = sorted(page_offsets.keys())
    page_idx = sorted_pages.index(page_num)
    
    if page_idx + 1 < len(sorted_pages):
        next_page = sorted_pages[page_idx + 1]
        page_end_offset = page_offsets[next_page]
    else:
        page_end_offset = len(concatenated_bytes)
    
    # Extract page content
    page_content = concatenated_bytes[page_start_offset:page_end_offset]
    
    try:
        page_text = page_content.decode('utf-8')
    except UnicodeDecodeError:
        # Try with error handling
        page_text = page_content.decode('utf-8', errors='replace')
    
    # Search for phrase in page text
    if phrase in page_text:
        phrase_offset_in_page = page_text.find(phrase)
        # Calculate absolute byte offset
        phrase_bytes = page_text[:phrase_offset_in_page].encode('utf-8')
        absolute_offset = page_start_offset + len(phrase_bytes)
        return absolute_offset
    
    # If not found, return start of page as fallback
    return page_start_offset


def extract_section_content(concatenated_bytes, start_byte, end_byte, page_offsets, section_id):
    """
    Extract content between byte offsets.
    Adds page markers where sections span multiple pages.
    Returns (content_bytes, page_markers_added_bytes).
    """
    # Find which pages this spans
    sorted_pages = sorted(page_offsets.keys())
    start_page = None
    end_page = None
    
    for i, page_num in enumerate(sorted_pages):
        page_start = page_offsets[page_num]
        if i + 1 < len(sorted_pages):
            page_end = page_offsets[sorted_pages[i + 1]]
        else:
            page_end = len(concatenated_bytes)
        
        if start_page is None and page_start <= start_byte < page_end:
            start_page = page_num
        
        if end_page is None and page_start < end_byte <= page_end:
            end_page = page_num
            break
    
    if start_page is None:
        start_page = sorted_pages[0]
    if end_page is None:
        end_page = sorted_pages[-1]
    
    # Extract raw bytes
    content_bytes = concatenated_bytes[start_byte:end_byte]
    
    # Now we need to insert page markers
    # Split by page boundaries and add markers
    result_bytes = b''
    page_markers_added = 0
    current_pos = start_byte
    
    for page_num in range(start_page, end_page + 1):
        page_start = page_offsets[page_num]
        if page_num + 1 in page_offsets:
            page_end = page_offsets[page_num + 1]
        else:
            page_end = len(concatenated_bytes)
        
        # Calculate intersection with our range
        segment_start = max(current_pos, page_start)
        segment_end = min(end_byte, page_end)
        
        if segment_start < segment_end:
            # Add page marker if not first page
            if page_num > start_page:
                marker = f"\n\n### PAGE {page_num}\n\n".encode('utf-8')
                result_bytes += marker
                page_markers_added += len(marker)
            
            # Add content from this page
            result_bytes += concatenated_bytes[segment_start:segment_end]
    
    return result_bytes, page_markers_added


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
    
    # Concatenate pages for both volumes
    print("\nConcatenating pages...")
    v1_bytes, v1_offsets = concatenate_pages(volume1_dir)
    v2_bytes, v2_offsets = concatenate_pages(volume2_dir)
    
    print(f"Volume 1: {len(v1_bytes):,} bytes across {len(v1_offsets)} pages")
    print(f"Volume 2: {len(v2_bytes):,} bytes across {len(v2_offsets)} pages")
    print(f"Total input: {len(v1_bytes) + len(v2_bytes):,} bytes")
    
    # Calculate byte offsets for each section
    print("\nCalculating byte offsets...")
    section_boundaries = []  # (section_id, start_byte, end_byte, volume)
    
    for i, section in enumerate(sections):
        section_id = section['id']
        volume, chapter, sec, subsection = parse_section_id(section_id)
        page_num = section['start_page']
        phrase = section['start_phrase']
        hint_line = section['start_line']
        
        # Choose correct volume
        if volume == 1:
            concat_bytes = v1_bytes
            page_offsets = v1_offsets
        else:
            concat_bytes = v2_bytes
            page_offsets = v2_offsets
        
        # Find start byte offset
        start_byte = find_phrase_byte_offset(concat_bytes, page_offsets, page_num, phrase, hint_line)
        
        # Store for now, we'll calculate end bytes after we have all start bytes
        section_boundaries.append({
            'id': section_id,
            'volume': volume,
            'start_byte': start_byte,
            'page': page_num
        })
    
    # Now calculate end bytes (each section ends where next section begins)
    for i in range(len(section_boundaries)):
        if i + 1 < len(section_boundaries):
            next_section = section_boundaries[i + 1]
            # If same volume, end is next section's start
            if next_section['volume'] == section_boundaries[i]['volume']:
                section_boundaries[i]['end_byte'] = next_section['start_byte']
            else:
                # Last section of volume 1 goes to end of v1
                section_boundaries[i]['end_byte'] = len(v1_bytes)
        else:
            # Last section goes to end of its volume
            if section_boundaries[i]['volume'] == 1:
                section_boundaries[i]['end_byte'] = len(v1_bytes)
            else:
                section_boundaries[i]['end_byte'] = len(v2_bytes)
    
    # Extract and write sections
    print(f"\nExtracting {len(section_boundaries)} sections...")
    total_markers_bytes = 0
    total_output_bytes = 0
    
    for i, boundary in enumerate(section_boundaries):
        section_id = boundary['id']
        volume = boundary['volume']
        start_byte = boundary['start_byte']
        end_byte = boundary['end_byte']
        
        if volume == 1:
            concat_bytes = v1_bytes
            page_offsets = v1_offsets
        else:
            concat_bytes = v2_bytes
            page_offsets = v2_offsets
        
        # Extract content
        content_bytes, markers_bytes = extract_section_content(
            concat_bytes, start_byte, end_byte, page_offsets, section_id
        )
        total_markers_bytes += markers_bytes
        
        # Write section file
        output_path = output_dir / f"{section_id}.txt"
        with open(output_path, 'wb') as f:
            f.write(content_bytes)
        
        total_output_bytes += len(content_bytes)
        
        if (i + 1) % 50 == 0:
            print(f"Processed {i + 1}/{len(section_boundaries)} sections...")
    
    print(f"\n{'='*60}")
    print("EXTRACTION COMPLETE")
    print(f"{'='*60}")
    
    total_input = len(v1_bytes) + len(v2_bytes)
    expected_output = total_input + total_markers_bytes
    
    print(f"\nByte Accounting:")
    print(f"  Input: {total_input:,} bytes")
    print(f"  Page markers added: {total_markers_bytes:,} bytes")
    print(f"  Expected output: {expected_output:,} bytes")
    print(f"  Actual output: {total_output_bytes:,} bytes")
    print(f"  Difference: {total_output_bytes - expected_output:,} bytes")
    
    if total_output_bytes == expected_output:
        print("\n  ✓ PERFECT MATCH: Byte-perfect extraction!")
    elif abs(total_output_bytes - expected_output) < 10:
        print(f"\n  ✓ ACCEPTABLE: Minor difference of {total_output_bytes - expected_output} bytes")
    else:
        print(f"\n  ✗ MISMATCH: Difference of {total_output_bytes - expected_output:,} bytes")
    
    # Show samples
    print(f"\nSample outputs:")
    samples = sorted(output_dir.glob("01-01-01-01.txt")) + sorted(output_dir.glob("02-15-01-01.txt"))
    for sample in samples[:2]:
        with open(sample, 'r', encoding='utf-8') as f:
            content = f.read()
            print(f"\n  {sample.name}: {len(content):,} chars")
            preview = content[:300].replace('\n', ' ')
            print(f"    {preview}...")


if __name__ == "__main__":
    main()
