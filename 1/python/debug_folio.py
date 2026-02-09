#!/usr/bin/env python3
import json
from pathlib import Path
import re

def read_page_file_raw(volume, layer, page_num):
    if volume == 1:
        page_dir = 'volume_1'
    else:
        page_dir = 'volume_2'
    page_file = Path(page_dir) / layer / f"PAGE_{page_num:03d}.txt"
    if not page_file.exists():
        return None
    with open(page_file, 'r', encoding='utf-8') as f:
        return f.read()

def get_line_number(line):
    stripped = line.strip()
    match = re.match(r'\[(\d+)\]\s*(.*)', stripped)
    if match:
        return (int(match.group(1)), False, None, None, match.group(2))
    match = re.match(r'\[(\d+)-(\d+)\]\s*(.*)', stripped)
    if match:
        start = int(match.group(1))
        end = int(match.group(2))
        return (end, True, start, end, match.group(3))
    return (None, False, None, None, stripped)

# Debug Ch 4 section A-i
volume = 1
layer = 'tibetan'
start_page = 119
start_line = 4417
end_page = 132
end_line = 5034  # From boundary.json next section

print(f"Section: V{volume} Ch4 A-i, pages {start_page}-{end_page}")
print(f"Lines: {start_line}-{end_line}")
print()

content_parts = []
current_page = start_page
first_page = True
pages_processed = 0

while current_page <= end_page:
    page_content = read_page_file_raw(volume, layer, current_page)
    
    if page_content is None:
        print(f"Page {current_page}: NOT FOUND")
        current_page += 1
        continue
    
    lines = page_content.split('\n')
    selected_lines = []
    
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        
        line_num, is_range, range_start, range_end, content = get_line_number(line)
        
        if line_num is not None:
            if current_page == start_page and current_page == end_page:
                if not (start_line <= line_num <= end_line):
                    continue
            elif current_page == start_page:
                if line_num < start_line:
                    continue
            elif current_page == end_page:
                if line_num > end_line:
                    break
        
        if line_num is not None:
            formatted = f"[{line_num}] {content}"
        else:
            formatted = content
        
        selected_lines.append(formatted)
    
    if selected_lines:
        pages_processed += 1
        print(f"Page {current_page}: {len(selected_lines)} lines selected")
        
        # FOLIO logic
        if first_page and volume == 1 and current_page == 1:
            print(f"  -> Adding FOLIO_{current_page:03d} (first page)")
            content_parts.append(f"FOLIO_{current_page:03d}\n")
            first_page = False
        elif not first_page:
            print(f"  -> Adding FOLIO_{current_page:03d} (subsequent page)")
            content_parts.append(f"\nFOLIO_{current_page:03d}\n")
        else:
            print(f"  -> NOT adding FOLIO (first_page={first_page}, volume={volume}, current_page={current_page})")
        
        content_parts.append('\n'.join(selected_lines))
    else:
        print(f"Page {current_page}: NO LINES SELECTED")
    
    current_page += 1

print()
print(f"Total pages processed: {pages_processed}")
print(f"Content parts: {len(content_parts)}")

# Count FOLIO markers
folio_count = sum(1 for part in content_parts if 'FOLIO_' in part)
print(f"FOLIO markers added: {folio_count}")
