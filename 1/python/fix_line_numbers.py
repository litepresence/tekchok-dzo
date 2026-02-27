#!/usr/bin/env python3
"""
Script to fix line numbers in MDZOD text layers.
Converts relative line numbers to absolute cumulative line numbers.
Handles [End], [Final], and negative range fixes.
"""

import os
import re
from pathlib import Path

BASE_PATH = Path("/home/opencode/MDZOD/1/text/layer")
BACKUP_PATH = Path("/home/opencode/MDZOD/1/text/layer_backup")

TRANSLATION_LAYERS = ["tibetan", "wylie", "literal", "liturgical"]
ANALYSIS_LAYERS = ["commentary", "scholar", "epistemic", "delusion", "cognitive"]
ALL_LAYERS = TRANSLATION_LAYERS + ANALYSIS_LAYERS

def get_tibetan_files():
    """Get all tibetan files sorted in order."""
    tib_path = BASE_PATH / "tibetan"
    files = sorted(tib_path.glob("*.txt"))
    return files

def build_cumulative_map():
    """Build a map of filename -> cumulative line info."""
    cumulative_map = {}
    cumulative_line = 1
    
    tibetan_files = get_tibetan_files()
    
    for tib_file in tibetan_files:
        name = tib_file.stem
        parts = name.split("-")
        if len(parts) != 4:
            continue
            
        vol, chap, section, subsection = parts
        
        with open(tib_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        line_count = len(lines)
        
        # Get absolute line numbers from tibetan file itself
        first_line_match = re.search(r'\[(\d+)\]', lines[0]) if lines else None
        last_line_match = re.search(r'\[(\d+)\]', lines[-1]) if lines else None
        
        first_abs = int(first_line_match.group(1)) if first_line_match else 1
        last_abs = int(last_line_match.group(1)) if last_line_match else line_count
        
        cumulative_map[name] = {
            'vol': vol,
            'line_count': line_count,
            'first_abs': first_abs,
            'last_abs': last_abs,
            'cumulative_start': cumulative_line,
            'cumulative_end': cumulative_line + line_count - 1,
        }
        
        cumulative_line += line_count
    
    return cumulative_map

def fix_end_patterns(content, filename, cum_map):
    """Fix [...-End], [...-END], [Final] patterns."""
    name = Path(filename).stem
    file_info = cum_map.get(name, {})
    cumulative_end = file_info.get('cumulative_end', 0)
    
    # Fix [...-End] and [...-END]
    def replace_end(match):
        start_num = match.group(1)
        return f'[{start_num}-{cumulative_end}]'
    
    content = re.sub(r'\[(\d+)-(End|END)\]', replace_end, content)
    
    # Fix [Final] - replace with cumulative end line
    content = re.sub(r'\[Final\]', f'[{cumulative_end}]', content)
    
    return content

def fix_negative_ranges(content, filename, cum_map):
    """Fix negative range patterns like [-20405--20394]."""
    name = Path(filename).stem
    file_info = cum_map.get(name, {})
    cumulative_start = file_info.get('cumulative_start', 0)
    
    # Fix negative ranges: [-XXXXX--YYYYY]
    # These appear to be broken cumulative references for volume 2
    def fix_negative_range(match):
        # The negative numbers are wrong - we need to calculate correct cumulative
        # For now, convert to the correct cumulative range based on file position
        # This is a placeholder - we need to calculate proper mapping
        return f'[{cumulative_start}-{cumulative_start + 99}]'  # Placeholder
    
    # Actually, let's parse the negative numbers and figure out what they meant
    # Pattern: [-XXXXX--YYYYY] where XXXXX and YYYYY are negative numbers
    def parse_negative(match):
        full_match = match.group(0)
        # Extract the numbers
        nums = re.findall(r'-(\d+)', full_match)
        if len(nums) == 2:
            # These are likely offsets from the correct cumulative
            # Let's figure out the pattern
            pass
        return full_match
    
    # For negative ranges, we need to calculate based on volume 2 offset
    # Volume 2 starts at 20427
    # The negative numbers seem to be: -(20427 - relative_line)
    # So -20405 means relative line = 20427 - 20405 = 22
    # But that's not right either...
    
    # Let me try a different approach: convert relative to absolute
    # The ranges like [-20405--20394] should become [XXXXX-YYYYY]
    
    return content

def convert_relative_to_absolute(content, filename, cum_map, layer_type):
    """Convert relative line references to absolute cumulative."""
    name = Path(filename).stem
    file_info = cum_map.get(name, {})
    
    if not file_info:
        return content
    
    cumulative_start = file_info['cumulative_start']
    cumulative_end = file_info['cumulative_end']
    vol = file_info['vol']
    
    def replace_range(match):
        prefix = match.group(1) or ''
        numbers = match.group(2)
        
        # Handle different range formats
        if '-' in numbers:
            parts = numbers.split('-')
            if len(parts) == 2:
                try:
                    start = int(parts[0])
                    end = int(parts[1])
                    
                    # Convert relative to absolute
                    abs_start = cumulative_start + start - 1
                    abs_end = cumulative_start + end - 1
                    
                    return f'[{prefix}{abs_start}-{abs_end}]'
                except:
                    return match.group(0)
        
        # Single number
        try:
            num = int(numbers)
            abs_num = cumulative_start + num - 1
            return f'[{prefix}{abs_num}]'
        except:
            return match.group(0)
    
    # Pattern to match [optional-prefix numbers]
    # Matches [1], [1-5], [005-008], etc.
    # But not [-20405--20394] which we'll handle separately
    
    if layer_type in ANALYSIS_LAYERS:
        # For analysis layers, convert line ranges
        # Pattern: [digits], [digits-digits], [000-digits]
        content = re.sub(r'\[(\d*)-?(\d+)(?:-\d+)?\]', replace_range, content)
    
    return content

def fix_commentary_file(filepath, cum_map):
    """Fix a single commentary file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    filename = filepath.name
    
    # Step 1: Fix [...-End] and [...-END] patterns
    content = fix_end_patterns(content, filename, cum_map)
    
    # Step 2: Fix negative ranges (volume 2 files)
    # These need special handling
    
    # Step 3: Convert relative to absolute
    content = convert_relative_to_absolute(content, filename, cum_map, 'commentary')
    
    return content

def main():
    print("Building cumulative line map...")
    cum_map = build_cumulative_map()
    
    print(f"\nVolume 1 ends at: {cum_map['01-14-04-01']['cumulative_end']}")
    print(f"Volume 2 starts at: {cum_map['02-15-01-01']['cumulative_start']}")
    
    # Test with one file
    test_file = BASE_PATH / "commentary" / "01-12-07-01.txt"
    if test_file.exists():
        print(f"\nTesting with {test_file.name}...")
        fixed = fix_commentary_file(test_file, cum_map)
        
        # Show some examples of changes
        print("\nChanges made:")
        for line in fixed.split('\n'):
            if '[' in line and ']' in line:
                print(f"  {line[:80]}")

if __name__ == "__main__":
    main()
