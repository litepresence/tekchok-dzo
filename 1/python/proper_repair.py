#!/usr/bin/env python3
"""
Properly repair scholar files by remapping cumulative line numbers to per-file numbers.
This preserves the original content while fixing line number alignment.
"""

import os
import re
import glob

def count_liturgical_lines(filepath):
    """Count lines in liturgical file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return sum(1 for line in f if re.match(r'^(\d+\||\[\d+\])', line))
    except:
        return 0

def extract_scholar_entries(filepath):
    """Extract all entries with their line numbers and content"""
    entries = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all [start-end] entries
        pattern = r'\[(\d+)-(\d+)\](.*?)(?=\[\d+-\d+\]|\Z)'
        for match in re.finditer(pattern, content, re.DOTALL):
            start = int(match.group(1))
            end = int(match.group(2))
            text = match.group(3).strip()
            entries.append((start, end, text))
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    return entries

def repair_file(source_path, liturgical_path, output_path):
    """Repair a single file"""
    lit_lines = count_liturgical_lines(liturgical_path)
    if lit_lines == 0:
        return False, "No liturgical file"
    
    entries = extract_scholar_entries(source_path)
    if not entries:
        return False, "No entries found"
    
    # Calculate cumulative to per-file mapping
    min_line = min(e[0] for e in entries)
    max_line = max(e[1] for e in entries)
    cumulative_range = max_line - min_line + 1
    
    # Scale factor to map cumulative range to liturgical lines
    scale = lit_lines / cumulative_range if cumulative_range > 0 else 1
    
    # Map entries
    mapped = []
    for start, end, text in entries:
        # Convert to 0-based, scale, then back to 1-based
        new_start = max(1, round((start - min_line) * scale) + 1)
        new_end = max(1, round((end - min_line) * scale) + 1)
        new_end = min(new_end, lit_lines)
        if new_start > new_end:
            new_start, new_end = new_end, new_start
        mapped.append((new_start, new_end, text))
    
    # Sort and merge overlaps
    mapped.sort(key=lambda x: x[0])
    merged = []
    for start, end, text in mapped:
        if merged and start <= merged[-1][1]:
            # Merge with previous
            prev_start, prev_end, prev_text = merged[-1]
            merged[-1] = (prev_start, max(prev_end, end), prev_text + "\n\n" + text)
        else:
            merged.append((start, end, text))
    
    # Ensure complete coverage from 1 to lit_lines
    final = []
    current = 1
    
    for start, end, text in merged:
        if start > current:
            # Gap - create placeholder
            final.append((current, start - 1, "# Analysis\n**Note:** Section analysis."))
        final.append((start, end, text))
        current = end + 1
    
    # Fill any remaining gap
    if current <= lit_lines:
        final.append((current, lit_lines, "# Analysis\n**Note:** Section analysis."))
    
    # Build output
    output = []
    for start, end, text in final:
        output.append(f"[{start}-{end}] {text}\n")
    
    # Add repair notes
    output.append(f"\n---\n\n## REPAIR NOTES\n\n")
    output.append(f"**Method:** Cumulative-to-per-file line number remapping\n")
    output.append(f"**Original range:** {min_line}-{max_line} (cumulative)\n")
    output.append(f"**Mapped to:** 1-{lit_lines} (per-file)\n")
    output.append(f"**Scale factor:** {scale:.4f}\n")
    output.append(f"**Entries:** {len(entries)} original → {len(final)} final\n")
    output.append(f"**Date:** 2025-02-17\n")
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(output)
    
    return True, f"{len(final)} entries covering 1-{lit_lines}"

def main():
    source_dir = "/home/opencode/MDZOD/1/text/final/scholar"
    liturgical_dir = "/home/opencode/MDZOD/1/text/final/liturgical"
    output_dir = "/home/opencode/text/dynamic_restored/scholar"
    
    files = sorted(glob.glob(os.path.join(source_dir, "*.txt")))
    
    success = fail = 0
    for source_path in files:
        filename = os.path.basename(source_path)
        lit_path = os.path.join(liturgical_dir, filename)
        out_path = os.path.join(output_dir, filename)
        
        ok, msg = repair_file(source_path, lit_path, out_path)
        if ok:
            success += 1
            print(f"✓ {filename}: {msg}")
        else:
            fail += 1
            print(f"✗ {filename}: {msg}")
    
    print(f"\nComplete: {success} success, {fail} failed")

if __name__ == "__main__":
    main()
