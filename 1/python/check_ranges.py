#!/usr/bin/env python3
"""Check if commentary line ranges match Tibetan source line numbers."""

import os
import re
import glob

COMMENTARY_DIR = "/home/opencode/MDZOD/1/text/dynamic/commentary"
TIBETAN_DIR = "/home/opencode/MDZOD/1/text/frozen/tibetan"

def get_tibetan_lines(filepath):
    """Extract all line numbers from a Tibetan source file."""
    line_numbers = set()
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            match = re.search(r'\[(\d+)\]', line)
            if match:
                line_numbers.add(int(match.group(1)))
    return line_numbers

def get_commentary_line_refs(filepath):
    """Extract all line references (ranges and single lines) from a commentary file."""
    refs = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            # Match ranges like [1-4]
            range_match = re.search(r'\[(\d+)-(\d+)\]', line)
            if range_match:
                start = int(range_match.group(1))
                end = int(range_match.group(2))
                refs.append(('range', start, end))
                continue
            
            # Match single lines like [57]
            single_match = re.search(r'\[(\d+)\](?![-\d])', line)
            if single_match:
                num = int(single_match.group(1))
                refs.append(('single', num, num))
    return refs

def check_file(filename):
    """Check if commentary file ranges match Tibetan source lines."""
    commentary_path = os.path.join(COMMENTARY_DIR, filename)
    tibetan_path = os.path.join(TIBETAN_DIR, filename)
    
    if not os.path.exists(tibetan_path):
        return None, ["No corresponding Tibetan file found"]
    
    tib_lines = get_tibetan_lines(tibetan_path)
    if not tib_lines:
        return None, ["Tibetan file has no line numbers"]
    
    refs = get_commentary_line_refs(commentary_path)
    if not refs:
        return None, ["No line references found in commentary"]
    
    tib_min = min(tib_lines)
    tib_max = max(tib_lines)
    
    errors = []
    all_valid = True
    
    for ref_type, start, end in refs:
        for num in range(start, end + 1):
            if num not in tib_lines:
                if ref_type == 'single':
                    errors.append(f"Line [{num}] not in Tibetan [{tib_min}-{tib_max}]")
                else:
                    errors.append(f"Line {num} in range [{start}-{end}] not in Tibetan [{tib_min}-{tib_max}]")
                all_valid = False
    
    if all_valid:
        return True, []
    return False, errors

# Get all commentary files
commentary_files = sorted(glob.glob(os.path.join(COMMENTARY_DIR, "*.txt")))

violations = []
valid_count = 0

for com_path in commentary_files:
    filename = os.path.basename(com_path)
    is_valid, errors = check_file(filename)
    
    if is_valid is None:
        print(f"SKIP {filename}: {errors[0]}")
    elif is_valid:
        valid_count += 1
    else:
        violations.append((filename, errors))

print(f"\n{'='*60}")
print(f"Total files checked: {len(commentary_files)}")
print(f"Valid files: {valid_count}")
print(f"Files with violations: {len(violations)}")
print(f"{'='*60}\n")

if violations:
    print("FILES WITH VIOLATIONS:\n")
    for filename, errors in violations:
        print(f"--- {filename} ---")
        for err in errors:
            print(f"  {err}")
        print()
