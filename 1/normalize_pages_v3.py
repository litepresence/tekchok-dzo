#!/usr/bin/env python3
"""
Normalize PAGE files in-place - ensure each line ends with exactly one \n.
This is the format the repartition script expects.
Reports bytes before and after.
"""

from pathlib import Path


def normalize_page_file(page_path):
    """
    Read file, ensure each line ends with exactly one \n.
    Returns (original_bytes, new_bytes, was_modified).
    """
    with open(page_path, 'rb') as f:
        original_bytes_data = f.read()
    
    original_bytes = len(original_bytes_data)
    
    # Decode as UTF-8
    try:
        content = original_bytes_data.decode('utf-8')
    except UnicodeDecodeError:
        print(f"Warning: UTF-8 decode error in {page_path}")
        return original_bytes, original_bytes, False
    
    # Split into lines
    lines = content.split('\n')
    
    # Remove any empty trailing elements caused by trailing newlines
    while lines and lines[-1] == '':
        lines.pop()
    
    # Ensure each line ends with \n
    normalized_lines = []
    for line in lines:
        # Strip any existing trailing whitespace/newlines
        stripped = line.rstrip()
        if stripped:  # Only add non-empty lines
            normalized_lines.append(stripped)
    
    # Join with \n and add final \n
    if normalized_lines:
        new_content = '\n'.join(normalized_lines) + '\n'
    else:
        new_content = '\n'  # At least one newline for empty file
    
    new_bytes = len(new_content.encode('utf-8'))
    
    # Write back if changed
    if new_content != content:
        with open(page_path, 'wb') as f:
            f.write(new_content.encode('utf-8'))
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
    print(f"  Diff:   {total_original - total_new:,} bytes")


if __name__ == "__main__":
    main()
