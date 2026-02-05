#!/usr/bin/env python3
import argparse
import sys


def number_tibetan_lines(text):
    lines = text.splitlines()
    output = []
    counter = 1  # Numbering starts at 1 for first eligible line after line 8
    
    for idx, line in enumerate(lines):
        # Preserve first 8 lines exactly (indices 0-7 = lines 1-8)
        #if idx < 8:
        #    output.append(line)
        #    continue
        
        # Skip numbering for blank lines (empty or whitespace-only)
        if not line.strip():
            output.append(line)
            continue
        
        # Skip numbering for section headers
        if line.startswith("###"):
            output.append(line)
            continue
        
        # Number all other lines
        output.append(f"[{counter}] {line}")
        counter += 1
    
    return "\n".join(output)

def main():
    parser = argparse.ArgumentParser(description="Number Tibetan text lines (skipping first 8 lines, blanks, and SECTION headers)")
    parser.add_argument("-i", "--input", help="Input file (default: stdin)")
    parser.add_argument("-o", "--output", help="Output file (default: stdout)")
    args = parser.parse_args()
    
    # Read input
    if args.input:
        with open(args.input, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        text = sys.stdin.read()
    
    # Process
    result = number_tibetan_lines(text)
    
    # Write output
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(result)
            if result and not result.endswith("\n"):
                f.write("\n")
    else:
        sys.stdout.write(result)
        if result and not result.endswith("\n"):
            sys.stdout.write("\n")

if __name__ == "__main__":
    main()
