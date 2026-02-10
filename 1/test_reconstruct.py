#!/usr/bin/env python3
"""
Verify by reconstructing PAGE files from sections.
"""

from pathlib import Path
import re


def reconstruct_pages(section_dir, prefix):
    """Build a map of page_number -> content from sections."""
    pages = {}  # page_num -> list of lines
    
    for section_file in sorted(section_dir.glob(f"{prefix}*.txt")):
        with open(section_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Split by page markers: content, marker, content, marker, ...
        # Pattern: \n\n### PAGE <number>\n\n
        parts = re.split(r'\n\n### PAGE (\d+)\n\n', content)
        
        # First part is always page 1 of this section
        if parts[0].strip():
            # Parse the first line to get the page number
            first_line = parts[0].strip().split('\n')[0]
            match = re.match(r'\[(\d+)\]', first_line)
            if match:
                line_num = int(match.group(1))
                # Estimate page from line number (rough approximation)
                # Volume 1: ~43 lines per page average
                # We'll use the section filename to determine starting page
                page_num = 1  # Default
                
                # Get page from first [line_num]
                if line_num <= 35:
                    page_num = 1
                else:
                    page_num = (line_num // 43) + 1
                
                if page_num not in pages:
                    pages[page_num] = []
                pages[page_num].append(parts[0])
        
        # Process remaining parts (marker + content pairs)
        for i in range(1, len(parts), 2):
            if i < len(parts):
                page_num = int(parts[i])
                if page_num not in pages:
                    pages[page_num] = []
                if i + 1 < len(parts):
                    pages[page_num].append(parts[i + 1])
    
    return pages


def main():
    base_dir = Path("/home/opencode/MDZOD/1")
    section_dir = base_dir / "text" / "tibetan"
    volume1_dir = base_dir / "volume_1" / "tibetan"
    
    print("Reconstructing Volume 1...")
    pages = reconstruct_pages(section_dir, "01-")
    print(f"Found {len(pages)} pages in sections")
    
    # Check a few pages
    for page_num in [1, 100, 479]:
        if page_num in pages:
            print(f"\nPage {page_num}:")
            content = '\n'.join(pages[page_num])
            lines = content.strip().split('\n')
            print(f"  {len(lines)} lines")
            print(f"  First: {lines[0][:60]}...")
            print(f"  Last: {lines[-1][:60]}...")


if __name__ == "__main__":
    main()
