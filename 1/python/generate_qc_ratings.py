#!/usr/bin/env python3
"""
Generate a qualitative QC rating for liturgical files based on the
category from liturgical_ratios.csv.

Rating scale (F- to A+):
- a -> F-
- b -> E
- c -> C
- d -> D
- e -> A
- f -> F

This is a first-pass heuristic that should be refined with: content-length,
presence of Tibetan content, deduplication flags, and human review notes.
"""
import csv
from pathlib import Path

BASE = Path("/home/opencode/MDZOD/1")
RATIOS = BASE / "liturgical_ratios.csv"
OUTPUT = BASE / "text" / "liturgical" / "qc_ratings.csv"

SCORE_MAP = {
    'a': 'F-',
    'b': 'E',
    'c': 'C',
    'd': 'D',
    'e': 'A',
    'f': 'F',
}

def main():
    if not RATIOS.exists():
        print(f"Ratios file not found: {RATIOS}")
        return
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with RATIOS.open('r', encoding='utf-8') as f_in, OUTPUT.open('w', encoding='utf-8', newline='') as f_out:
        writer = csv.writer(f_out)
        writer.writerow(["id", "file_code", "ratio", "category", "rating", "notes"])
        for line in f_in:
            line = line.strip()
            if not line or line.startswith('(End of file'):
                break
            # Expect format like: 00001| 01-05-04-03,104,1820,0.057..., a
            if '|' not in line:
                continue
            left, rest = line.split('|', 1)
            fid = left.strip()
            parts = rest.strip().split(',')
            if len(parts) < 5:
                # malformed line
                continue
            file_code = parts[0].strip()
            ratio = parts[3].strip() if len(parts) > 3 else ''
            cat = parts[-1].strip().lower()
            rating = SCORE_MAP.get(cat, 'E')
            notes = f"derived from category '{cat}'"
            writer.writerow([fid, file_code, ratio, cat, rating, notes])

if __name__ == '__main__':
    main()
