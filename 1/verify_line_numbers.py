#!/usr/bin/env python3
"""
Fix over-expanded liturgical files by regenerating with exact 1:1 line correspondence.
Each [XXX] line number must match exactly between Tibetan and Liturgical.
"""

from pathlib import Path
import re

def extract_line_number(line):
    """Extract line number from bracketed format [123]."""
    match = re.match(r'\[(\d+)\]', line)
    if match:
        return int(match.group(1))
    return None

def get_line_numbers(filepath):
    """Get all line numbers from a file."""
    numbers = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            num = extract_line_number(line)
            if num is not None:
                numbers.append(num)
    return numbers

# Files to fix with their line count issues
files_to_fix = [
    "01-01-03-01.txt",  # 57 Tibetan lines vs 455 liturgical - WRONG CONTENT
    "01-09-01-01.txt",  # 1143 → 1330
    "01-10-01-01.txt",  # 604 → 788
    "02-19-01-01.txt",  # 1669 → 1829
    "01-12-01-01.txt",  # 697 → 845
    "02-22-01-01.txt",  # 555 → 702
    "01-06-12-01.txt",  # 503 → 641
    "02-25-01-01.txt",  # 694 → 810
    "02-20-09-01.txt",  # 9 → 116
    "01-05-04-01.txt",  # 1572 → 1674
    "02-22-02-01.txt",  # 60 → 160
    "01-13-06-01.txt",  # 289 → 386
    "02-25-02-01.txt",  # 31 → 100
    "02-23-06-01.txt",  # 499 → 563
    "01-04-01-01.txt",  # 637 → 698
    "02-17-04-01.txt",  # 625 → 685
    "01-14-05-01.txt",  # 693 → 753
    "02-25-06-01.txt",  # 51 → 110
    "02-23-09-01.txt",  # 452 → 504
]

tibetan_dir = Path('text/tibetan')
liturgical_dir = Path('text/liturgical')
literal_dir = Path('text/literal')

print("=== VERIFYING LINE NUMBER CORRESPONDENCE ===\n")

issues_found = []

for filename in files_to_fix:
    tib_path = tibetan_dir / filename
    lit_path = liturgical_dir / filename
    
    if not tib_path.exists():
        print(f"⚠️ {filename}: Tibetan file missing")
        continue
    if not lit_path.exists():
        print(f"⚠️ {filename}: Liturgical file missing")
        continue
    
    tib_numbers = get_line_numbers(tib_path)
    lit_numbers = get_line_numbers(lit_path)
    
    # Check if line numbers match
    if tib_numbers != lit_numbers:
        print(f"🔴 {filename}: MISMATCH")
        print(f"   Tibetan lines: {tib_numbers[:3]}...{tib_numbers[-3:] if len(tib_numbers) > 3 else ''} ({len(tib_numbers)} total)")
        print(f"   Liturgical lines: {lit_numbers[:3]}...{lit_numbers[-3:] if len(lit_numbers) > 3 else ''} ({len(lit_numbers)} total)")
        issues_found.append((filename, tib_numbers, lit_numbers))
    else:
        print(f"✓ {filename}: Line numbers match ({len(tib_numbers)} lines)")

print(f"\n=== SUMMARY ===")
print(f"Files with line number mismatches: {len(issues_found)}")
if issues_found:
    print("\nThese files need regeneration with correct line numbers:")
    for filename, tib_nums, lit_nums in issues_found:
        print(f"  - {filename}: Tibetan {len(tib_nums)} lines vs Liturgical {len(lit_nums)} lines")
