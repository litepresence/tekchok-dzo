#!/usr/bin/env python3
"""
Verify section files by attempting to reconstruct original PAGE files.
Reports exact byte differences.
"""

from pathlib import Path
import re


def get_page_lines(page_path):
    """Get all lines from a page file."""
    if not page_path.exists():
        return []
    with open(page_path, 'r', encoding='utf-8') as f:
        return f.readlines()


def reconstruct_volume(volume_num, section_dir, volume_dir):
    """Reconstruct a volume from its section files."""
    prefix = f"{volume_num:02d}-"
    sections = sorted(section_dir.glob(f"{prefix}*.txt"))
    
    print(f"\nReconstructing Volume {volume_num}:")
    print(f"  Found {len(sections)} section files")
    
    # Build expected content per page
    page_contents = {}
    
    for section_file in sections:
        with open(section_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Split by page markers
        parts = re.split(r'\n\n### PAGE (\d+)\n\n', content)
        
        # First part is page 1 of the section
        if parts[0].strip():
            # Find which page this is
            # Get it from filename or track sequentially
            first_page_match = re.search(r'PAGE_(\d+)', str(section_file))
            if first_page_match:
                page_num = int(first_page_match.group(1))
            else:
                continue
            
            if page_num not in page_contents:
                page_contents[page_num] = []
            page_contents[page_num].append(parts[0])
        
        # Remaining parts are page markers and content
        for i in range(1, len(parts), 2):
            if i < len(parts):
                page_num = int(parts[i])
                if page_num not in page_contents:
                    page_contents[page_num] = []
                if i + 1 < len(parts):
                    page_contents[page_num].append(parts[i + 1])
    
    # Now verify each page
    total_original = 0
    total_reconstructed = 0
    mismatches = 0
    
    for page_file in sorted(volume_dir.glob("PAGE_*.txt")):
        page_num = int(page_file.stem.split('_')[1])
        
        with open(page_file, 'rb') as f:
            original = f.read()
        
        total_original += len(original)
        
        if page_num in page_contents:
            # Reconstruct
            reconstructed = ''.join(page_contents[page_num]).encode('utf-8')
            total_reconstructed += len(reconstructed)
            
            if original != reconstructed:
                mismatches += 1
                if mismatches <= 3:  # Show first 3 mismatches
                    print(f"\n  Mismatch in PAGE_{page_num:03d}:")
                    print(f"    Original: {len(original)} bytes")
                    print(f"    Reconstructed: {len(reconstructed)} bytes")
                    # Find difference
                    min_len = min(len(original), len(reconstructed))
                    for i in range(min_len):
                        if original[i] != reconstructed[i]:
                            print(f"    First diff at byte {i}")
                            print(f"    Original: {original[max(0,i-20):i+20]}")
                            print(f"    Recon:    {reconstructed[max(0,i-20):i+20]}")
                            break
        else:
            print(f"  Warning: No sections found for PAGE_{page_num:03d}")
    
    print(f"\n  Total original: {total_original:,} bytes")
    print(f"  Total reconstructed: {total_reconstructed:,} bytes")
    print(f"  Difference: {total_original - total_reconstructed:,} bytes")
    print(f"  Mismatched pages: {mismatches}")
    
    return total_original, total_reconstructed


def main():
    base_dir = Path("/home/opencode/MDZOD/1")
    section_dir = base_dir / "text" / "tibetan"
    volume1_dir = base_dir / "volume_1" / "tibetan"
    volume2_dir = base_dir / "volume_2" / "tibetan"
    
    orig1, recon1 = reconstruct_volume(1, section_dir, volume1_dir)
    orig2, recon2 = reconstruct_volume(2, section_dir, volume2_dir)
    
    print(f"\n{'='*60}")
    print(f"TOTAL VERIFICATION")
    print(f"{'='*60}")
    print(f"Original: {orig1 + orig2:,} bytes")
    print(f"Reconstructed: {recon1 + recon2:,} bytes")
    print(f"Difference: {(orig1 + orig2) - (recon1 + recon2):,} bytes")


if __name__ == "__main__":
    main()
