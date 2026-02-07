#!/usr/bin/env python3
"""
Script to generate commentary for missing pages in Volume 2
"""
import os
import glob
from pathlib import Path

def get_missing_pages():
    """Get list of pages missing commentary"""
    base_path = Path("/home/oracle/extinction-event/EV/theg pa'i mchog rin po che'i mdzod/1/volume_2")
    
    # Get all Tibetan pages
    tibetan_pages = set()
    for f in (base_path / "tibetan").glob("PAGE *.txt"):
        try:
            page_num = int(f.stem.replace("PAGE ", ""))
            tibetan_pages.add(page_num)
        except:
            pass
    
    # Get all Commentary pages
    commentary_pages = set()
    for f in (base_path / "commentary").glob("PAGE *.txt"):
        try:
            page_num = int(f.stem.replace("PAGE ", ""))
            commentary_pages.add(page_num)
        except:
            pass
    
    missing = sorted(tibetan_pages - commentary_pages)
    return missing

if __name__ == "__main__":
    missing = get_missing_pages()
    print(f"Total missing commentary pages: {len(missing)}")
    print(f"Range: {missing[0]} - {missing[-1]}")
    print(f"\nFirst 20 missing: {missing[:20]}")
