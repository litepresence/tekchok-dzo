#!/usr/bin/env python3
"""
Normalize PAGE files in-place - STRIP ONLY, don't add.
Removes trailing whitespace from each line.
Reports bytes before and after.
"""

from pathlib import Path


def normalize_page_file(page_path):
    """
    Read file, strip trailing whitespace from each line.
    Keep original line endings and structure.
    Returns (original_bytes, new_bytes, was_modified).
    """
    with open(page_path, 'r', encoding='utf-8') as f:
        original_content = f.read()
    
    original_bytes = len(original_content.encode('utf-8'))
    
    # Split into lines preserving original line endings
    # Handle both \n and \r\n
    if '\r\n' in original_content:
        lines = original_content.split('\r\n')
        line_ending = '\r\n'
    else:
        lines = original_content.split('\n')
        line_ending = '\n'
    
    # Strip trailing whitespace from each line
    normalized_lines = [line.rstrip() for line in lines]
    
    # Rejoin with original line endings
    new_content = line_ending.join(normalized_lines)
    
    new_bytes = len(new_content.encode('utf-8'))
    
    # Write back if changed
    if new_content != original_content:
        with open(page_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return original_bytes, new_bytes, True
    else:
        return original_bytes, new_bytes, False


def main():
    base_dir = Path("/home/opencode/MDZOD/1")
    volume1_dir = base_dir / "volume_1" / "tibetan"
    volume2_dir = base_dir / "volume_2" / "tibetan"
    
    total_original = 0
    total_new = 0
    files_modified = 0
    files_unchanged = 0
    
    # Process both volumes
    for volume_dir in [volume1_dir, volume2_dir]:
        print(f"\nProcessing {volume_dir}...")
        
        for page_file in sorted(volume_dir.glob("PAGE_*.txt")):
            orig, new, modified = normalize_page_file(page_file)
            total_original += orig
            total_new += new
            
            if modified:
                files_modified += 1
            else:
                files_unchanged += 1
    
    print(f"\n{'='*60}")
    print(f"NORMALIZATION COMPLETE")
    print(f"{'='*60}")
    print(f"Files modified: {files_modified}")
    print(f"Files unchanged: {files_unchanged}")
    print(f"Total files: {files_modified + files_unchanged}")
    print(f"\nByte comparison:")
    print(f"  Before: {total_original:,} bytes")
    print(f"  After:  {total_new:,} bytes")
    print(f"  Diff:   {total_original - total_new:,} bytes removed")


if __name__ == "__main__":
    main()
