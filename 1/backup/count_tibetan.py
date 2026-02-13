#!/usr/bin/env python3
"""Count Tibetan Unicode characters in files across directories."""

import os
import re
from pathlib import Path

def count_tibetan_chars(text):
    """Count characters in Tibetan Unicode block (U+0F00-U+0FFF)."""
    # Tibetan Unicode range: U+0F00 to U+0FFF
    tibetan_pattern = re.compile(r'[\u0F00-\u0FFF]')
    return len(tibetan_pattern.findall(text))

def analyze_directory(dir_path, label):
    """Analyze all .txt files in directory."""
    dir_path = Path(dir_path)
    if not dir_path.exists():
        print(f"{label}: Directory does not exist")
        return {}
    
    results = {}
    txt_files = sorted([f for f in dir_path.glob('*.txt')])
    
    for filepath in txt_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            tibetan_count = count_tibetan_chars(content)
            results[filepath.name] = tibetan_count
        except Exception as e:
            print(f"Error reading {filepath}: {e}")
            results[filepath.name] = -1
    
    return results

def main():
    base_path = Path('/home/opencode/MDZOD/1/text')
    
    # Analyze each directory
    print("Analyzing Tibetan character counts...\n")
    
    artifacts = analyze_directory(base_path / 'artifacts', 'artifacts')
    tibetan = analyze_directory(base_path / 'tibetan', 'tibetan')
    raw = analyze_directory(base_path / 'raw', 'raw')
    
    print(f"artifacts: {len(artifacts)} files")
    print(f"tibetan: {len(tibetan)} files")
    print(f"raw: {len(raw)} files")
    
    # Compare artifacts and tibetan (they should have matching filenames)
    print("\n" + "="*60)
    print("COMPARING: artifacts vs tibetan")
    print("="*60)
    
    if set(artifacts.keys()) != set(tibetan.keys()):
        print("WARNING: File names don't match!")
        print(f"  Only in artifacts: {set(artifacts.keys()) - set(tibetan.keys())}")
        print(f"  Only in tibetan: {set(tibetan.keys()) - set(artifacts.keys())}")
    
    total_artifacts = 0
    total_tibetan = 0
    mismatches = []
    
    for filename in sorted(artifacts.keys()):
        art_count = artifacts[filename]
        tib_count = tibetan.get(filename, 0)
        total_artifacts += art_count
        total_tibetan += tib_count
        
        if art_count != tib_count:
            mismatches.append((filename, art_count, tib_count))
    
    print(f"\nTotal Tibetan characters in artifacts: {total_artifacts:,}")
    print(f"Total Tibetan characters in tibetan: {total_tibetan:,}")
    
    if mismatches:
        print(f"\nMISMATCHES FOUND: {len(mismatches)} files")
        for filename, art, tib in mismatches[:10]:  # Show first 10
            print(f"  {filename}: artifacts={art}, tibetan={tib}")
        if len(mismatches) > 10:
            print(f"  ... and {len(mismatches) - 10} more")
    else:
        print("\n✓ PERFECT MATCH: All files have identical Tibetan character counts")
    
    # Check raw directory (different filenames)
    print("\n" + "="*60)
    print("RAW DIRECTORY (different source files)")
    print("="*60)
    if raw:
        total_raw = sum(raw.values())
        print(f"Files: {list(raw.keys())}")
        print(f"Total Tibetan characters: {total_raw:,}")
        print(f"Note: raw/ contains source files with different naming convention")

if __name__ == '__main__':
    main()
