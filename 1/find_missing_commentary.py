#!/usr/bin/env python3
"""
Script to identify missing commentary pages in Volume 2
"""
import os
import glob
from pathlib import Path

def find_missing_commentary(volume_path):
    """Find pages with Tibetan but no Commentary"""
    tibetan_dir = Path(volume_path) / "tibetan"
    commentary_dir = Path(volume_path) / "commentary"
    
    # Get all page numbers from Tibetan files
    tibetan_pages = set()
    for f in tibetan_dir.glob("PAGE *.txt"):
        # Extract page number from filename like "PAGE 123.txt"
        try:
            page_num = int(f.stem.replace("PAGE ", ""))
            tibetan_pages.add(page_num)
        except ValueError:
            continue
    
    # Get all page numbers from Commentary files
    commentary_pages = set()
    for f in commentary_dir.glob("PAGE *.txt"):
        try:
            page_num = int(f.stem.replace("PAGE ", ""))
            commentary_pages.add(page_num)
        except ValueError:
            continue
    
    # Find missing pages
    missing = sorted(tibetan_pages - commentary_pages)
    
    print(f"Total Tibetan pages: {len(tibetan_pages)}")
    print(f"Total Commentary pages: {len(commentary_pages)}")
    print(f"Missing Commentary pages: {len(missing)}")
    print(f"\nMissing pages: {missing}")
    
    # Group consecutive pages for easier processing
    if missing:
        print("\nConsecutive ranges:")
        ranges = []
        start = missing[0]
        end = missing[0]
        
        for i in range(1, len(missing)):
            if missing[i] == end + 1:
                end = missing[i]
            else:
                if start == end:
                    ranges.append(f"{start}")
                else:
                    ranges.append(f"{start}-{end}")
                start = missing[i]
                end = missing[i]
        
        # Add the last range
        if start == end:
            ranges.append(f"{start}")
        else:
            ranges.append(f"{start}-{end}")
        
        print(", ".join(ranges))
    
    return missing

if __name__ == "__main__":
    volume2_path = "/home/oracle/extinction-event/EV/theg pa'i mchog rin po che'i mdzod/1/volume_2"
    missing = find_missing_commentary(volume2_path)
    
    # Save to file for reference
    with open("/home/oracle/extinction-event/EV/theg pa'i mchog rin po che'i mdzod/1/missing_commentary_pages.txt", "w") as f:
        f.write("Missing Commentary Pages in Volume 2:\n")
        f.write(f"Total: {len(missing)}\n\n")
        f.write("Pages: " + ", ".join(map(str, missing)) + "\n")
    
    print(f"\nSaved list to missing_commentary_pages.txt")
