#!/usr/bin/env python3
"""
Add <break> tags to liturgical files at section transitions.
Reads meter files to determine where sections change.
"""

import os
import re
import sys

def parse_meter_file(meter_path):
    """Parse meter file to find section transitions."""
    transitions = []
    
    with open(meter_path, 'r') as f:
        content = f.read()
    
    # Find all section declarations [XXX-YYY] [TYPE]
    pattern = r'\[(\d+)-(\d+)\]\s*\[(\w+)\]'
    matches = re.findall(pattern, content)
    
    for match in matches:
        start = int(match[0])
        end = int(match[1])
        section_type = match[2]
        transitions.append((start, end, section_type))
    
    return transitions

def add_breaks_to_liturgical(lit_path, transitions):
    """Add <break> tags at section starts."""
    
    with open(lit_path, 'r') as f:
        lines = f.readlines()
    
    # Get line numbers where sections start (skip first section)
    break_lines = set()
    for i, (start, end, section_type) in enumerate(transitions):
        if i > 0:  # Skip first section
            break_lines.add(start)
    
    # Process lines
    modified = []
    for line in lines:
        # Extract line number
        match = re.match(r'\[(\d+)\]', line)
        if match:
            line_num = int(match.group(1))
            
            # Check if this line needs a break
            if line_num in break_lines and '<break>' not in line:
                # Add <break> after the line number
                line = re.sub(r'(\[\d+\])\s*', r'\1 <break> ', line, count=1)
        
        modified.append(line)
    
    return modified

def process_file(filename):
    """Process a single liturgical file."""
    lit_path = f'/home/opencode/MDZOD/1/text/dynamic/liturgical/{filename}'
    meter_path = f'/home/opencode/MDZOD/1/text/frozen/meter/{filename}'
    
    if not os.path.exists(lit_path):
        print(f'Liturgical file not found: {filename}')
        return False
    
    if not os.path.exists(meter_path):
        print(f'Meter file not found: {filename}')
        return False
    
    # Parse meter file
    transitions = parse_meter_file(meter_path)
    
    if len(transitions) <= 1:
        print(f'{filename}: Only {len(transitions)} section, no breaks needed')
        return True
    
    # Add breaks
    modified_lines = add_breaks_to_liturgical(lit_path, transitions)
    
    # Write back
    with open(lit_path, 'w') as f:
        f.writelines(modified_lines)
    
    breaks_added = len(transitions) - 1
    print(f'{filename}: Added {breaks_added} <break> tag(s)')
    return True

if __name__ == '__main__':
    # Process files from command line or process all
    if len(sys.argv) > 1:
        # Process specific files
        for filename in sys.argv[1:]:
            process_file(filename)
    else:
        # Process all files without <break> tags
        lit_dir = '/home/opencode/MDZOD/1/text/dynamic/liturgical'
        count = 0
        for filename in sorted(os.listdir(lit_dir)):
            if filename.endswith('.txt'):
                lit_path = os.path.join(lit_dir, filename)
                # Check if file already has breaks
                with open(lit_path, 'r') as f:
                    content = f.read()
                if '<break>' not in content:
                    process_file(filename)
                    count += 1
                    if count % 50 == 0:
                        print(f'Processed {count} files...')
        print(f'Total files processed: {count}')
