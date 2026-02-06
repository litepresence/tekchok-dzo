#!/usr/bin/env python3
"""Check translation status for Volume 2"""
import os
import re

def get_page_numbers(directory):
    """Extract page numbers from filenames like 'PAGE 123.txt'"""
    pages = set()
    if not os.path.exists(directory):
        return pages
    for filename in os.listdir(directory):
        match = re.match(r'PAGE (\d+)\.txt', filename)
        if match:
            pages.add(int(match.group(1)))
    return pages

# Get all pages
v2_path = '/home/oracle/extinction-event/EV/theg pa\'i mchog rin po che\'i mdzod/1/volume_2'
tibetan_pages = get_page_numbers(os.path.join(v2_path, 'tibetan'))
wylie_pages = get_page_numbers(os.path.join(v2_path, 'wylie'))
literal_pages = get_page_numbers(os.path.join(v2_path, 'literal'))
liturgical_pages = get_page_numbers(os.path.join(v2_path, 'liturgical'))

print("=" * 60)
print("VOLUME 2 TRANSLATION STATUS")
print("=" * 60)
print(f"\nTibetan source: {len(tibetan_pages)}/415 pages")
print(f"Wylie layer: {len(wylie_pages)}/415 pages")
print(f"Literal layer: {len(literal_pages)}/415 pages")
print(f"Liturgical layer: {len(liturgical_pages)}/415 pages")

# Find missing pages
all_pages = set(range(1, 416))
missing_literal = sorted(all_pages - literal_pages)
missing_liturgical = sorted(all_pages - liturgical_pages)

print(f"\nMissing from Literal: {len(missing_literal)} pages")
if missing_literal:
    print(f"  Ranges: {missing_literal[:20]}..." if len(missing_literal) > 20 else f"  {missing_literal}")

print(f"\nMissing from Liturgical: {len(missing_liturgical)} pages")
if missing_liturgical:
    print(f"  Ranges: {missing_liturgical[:20]}..." if len(missing_liturgical) > 20 else f"  {missing_liturgical}")

# Check which pages need both
need_both = sorted((all_pages - literal_pages) & (all_pages - liturgical_pages))
need_literal_only = sorted((all_pages - literal_pages) - (all_pages - liturgical_pages))
need_liturgical_only = sorted((all_pages - liturgical_pages) - (all_pages - literal_pages))

print(f"\nNeed BOTH layers: {len(need_both)} pages")
print(f"Need Literal only: {len(need_literal_only)} pages")
print(f"Need Liturgical only: {len(need_liturgical_only)} pages")
