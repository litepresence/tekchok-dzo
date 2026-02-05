#!/usr/bin/env python3
"""
Tibetan Text Structural Marker Injector
Adds RIM_KHANG, SA_BCAD, DIMENSION, PRACTICE, VERSE, and /VERSE markers
based on line-number mappings defined in external JSON configuration.
"""
import argparse
import json
import re
from pathlib import Path


def parse_line_number(line: str) -> int | None:
    """Extract line number from bracketed prefix like '[11]' at start of line."""
    match = re.match(r'^\[(\d+)\]', line)
    return int(match.group(1)) if match else None


def inject_markers(input_path: Path, output_path: Path, json_path: Path) -> None:
    """Inject structural markers into Tibetan text based on JSON configuration."""
    
    # Load marker configuration
    with open(json_path, 'r', encoding='utf-8') as f:
        marker_configs = json.load(f)
    
    # Build efficient lookup: {line_number: [marker_strings]}
    markers_by_line = {}
    for line_num, marker_text in marker_configs:
        markers_by_line.setdefault(line_num, []).append(marker_text)
    
    # Process input file
    output_lines = []
    with open(input_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n')
            current_line_num = parse_line_number(line)
            
            # Inject markers BEFORE the line if it has a bracketed number
            if current_line_num is not None and current_line_num in markers_by_line:
                for marker in markers_by_line[current_line_num]:
                    output_lines.append(marker)
            
            output_lines.append(line)
    
    # Write output file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output_lines) + '\n')
    
    print(f"Processed {len(output_lines)} lines")
    print(f"Injected markers at {len(markers_by_line)} line positions")
    print(f"Output written to: {output_path}")


def main():
    parser = argparse.ArgumentParser(description='Inject structural markers into Tibetan text')
    parser.add_argument('--input', required=True, help='Input Tibetan text file')
    parser.add_argument('--output', required=True, help='Output file with markers injected')
    parser.add_argument('--json', required=True, help='JSON configuration file with marker mappings')
    args = parser.parse_args()
    
    input_path = Path(args.input)
    output_path = Path(args.output)
    json_path = Path(args.json)
    
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    if not json_path.exists():
        raise FileNotFoundError(f"JSON config not found: {json_path}")
    
    inject_markers(input_path, output_path, json_path)


if __name__ == '__main__':
    main()
