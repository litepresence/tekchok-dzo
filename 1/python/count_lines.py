#!/usr/bin/env python3
"""
Count total lines in source vs sections to find missing content.
"""

from pathlib import Path
import re


def count_lines_in_volume(volume_dir):
    """Count total lines in all PAGE files of a volume."""
    total_lines = 0
    for page_file in sorted(volume_dir.glob("PAGE_*.txt")):
        with open(page_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            # Only count lines that start with [number]
            content_lines = [l for l in lines if re.match(r'^\[\d+\]', l.strip())]
            total_lines += len(content_lines)
    return total_lines


def count_lines_in_sections(section_dir, prefix):
    """Count total lines in section files for a volume."""
    total_lines = 0
    for section_file in sorted(section_dir.glob(f"{prefix}*.txt")):
        with open(section_file, 'r', encoding='utf-8') as f:
            content = f.read()
            # Remove page markers
            content_no_markers = re.sub(r'\n\n### PAGE \d+\n\n', '\n', content)
            lines = content_no_markers.split('\n')
            # Only count lines that start with [number]
            content_lines = [l for l in lines if re.match(r'^\[\d+\]', l.strip())]
            total_lines += len(content_lines)
    return total_lines


def main():
    base_dir = Path("/home/opencode/MDZOD/1")
    section_dir = base_dir / "text" / "tibetan"
    volume1_dir = base_dir / "volume_1" / "tibetan"
    volume2_dir = base_dir / "volume_2" / "tibetan"
    
    print("LINE COUNT COMPARISON")
    print("="*60)
    
    # Volume 1
    v1_source = count_lines_in_volume(volume1_dir)
    v1_sections = count_lines_in_sections(section_dir, "01-")
    print(f"\nVolume 1:")
    print(f"  Source PAGE files: {v1_source} lines")
    print(f"  Section files:     {v1_sections} lines")
    print(f"  Difference:        {v1_source - v1_sections} lines")
    
    # Volume 2
    v2_source = count_lines_in_volume(volume2_dir)
    v2_sections = count_lines_in_sections(section_dir, "02-")
    print(f"\nVolume 2:")
    print(f"  Source PAGE files: {v2_source} lines")
    print(f"  Section files:     {v2_sections} lines")
    print(f"  Difference:        {v2_source - v2_sections} lines")
    
    print(f"\n{'='*60}")
    total_source = v1_source + v2_source
    total_sections = v1_sections + v2_sections
    print(f"Total:")
    print(f"  Source:   {total_source} lines")
    print(f"  Sections: {total_sections} lines")
    print(f"  Missing:  {total_source - total_sections} lines")


if __name__ == "__main__":
    main()
