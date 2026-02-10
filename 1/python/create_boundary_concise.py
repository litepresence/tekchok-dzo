#!/usr/bin/env python3
"""
Create boundary_concise.json from boundary.json with minimal required fields.

Only keeps: section_id, start_page, start_line, start_phrase
Sections are ordered by (volume, start_page, start_line).
"""

import json
from pathlib import Path


def parse_section_id(section_id):
    """Parse section_id like '01-01-01-01' into volume and sort key."""
    parts = section_id.split('-')
    return tuple(int(p) for p in parts)


def main():
    base_dir = Path("/home/opencode/MDZOD/1")
    boundary_path = base_dir / "boundary.json"
    concise_path = base_dir / "boundary_concise.json"
    
    # Load full boundary data
    with open(boundary_path, 'r', encoding='utf-8') as f:
        boundary_data = json.load(f)
    
    sections = boundary_data['sections']
    print(f"Loaded {len(sections)} sections from boundary.json")
    
    # Create concise version
    concise_sections = []
    
    for section_id, section_data in sections.items():
        volume, chapter, section, subsection = parse_section_id(section_id)
        
        concise_entry = {
            "id": section_id,
            "start_page": section_data['start_page'],
            "start_line": section_data['start_line'],
            "start_phrase": section_data['start_phrase']
        }
        
        concise_sections.append(concise_entry)
    
    # Sort by (volume, start_page, start_line)
    concise_sections.sort(key=lambda x: (
        parse_section_id(x['id'])[0],  # volume
        x['start_page'],
        x['start_line']
    ))
    
    # Write concise file
    concise_data = {
        "metadata": {
            "source": "boundary.json",
            "fields": ["id", "start_page", "start_line", "start_phrase"],
            "total_sections": len(concise_sections),
            "note": "Sections end at the start of the next section's phrase"
        },
        "sections": concise_sections
    }
    
    with open(concise_path, 'w', encoding='utf-8') as f:
        json.dump(concise_data, f, indent=2, ensure_ascii=False)
    
    print(f"\nCreated boundary_concise.json with {len(concise_sections)} sections")
    print(f"Output: {concise_path}")
    
    # Show first few entries
    print(f"\nFirst 3 sections:")
    for section in concise_sections[:3]:
        print(f"  {section['id']}: p.{section['start_page']} L{section['start_line']} \"{section['start_phrase'][:40]}...\"")
    
    print(f"\nLast 3 sections:")
    for section in concise_sections[-3:]:
        print(f"  {section['id']}: p.{section['start_page']} L{section['start_line']} \"{section['start_phrase'][:40]}...\"")


if __name__ == "__main__":
    main()
