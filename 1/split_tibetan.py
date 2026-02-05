#!/usr/bin/env python3
import os
import re
import sys


def sanitize_filename(name):
    """
    Convert section titles to safe filenames:
    - Keep alphanumeric, Tibetan Unicode, underscores, hyphens, and dots
    - Replace problematic characters (slashes, colons, etc.) with underscores
    - Collapse multiple underscores and trim edge underscores
    """
    # Allow Tibetan Unicode (U+0F00-U+0FFF) + safe ASCII chars
    safe = re.sub(r'[^\w\-\.\/\u0F00-\u0FFF ]', '_', name)
    safe = re.sub(r'_+', '_', safe)  # Collapse multiple underscores
    safe = safe.strip('_').strip()   # Trim edge underscores/spaces
    if not safe:
        safe = 'section'
    return safe + '.txt'

def main():
    input_file = '1_numbered.txt'
    output_dir = 'tibetan'

    # Verify input file exists
    if not os.path.isfile(input_file):
        print(f"❌ Error: '{input_file}' not found in current directory.", file=sys.stderr)
        print(f"   Current directory: {os.getcwd()}", file=sys.stderr)
        sys.exit(1)

    # Read file with UTF-8 encoding (critical for Tibetan text)
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()

    # Parse sections
    sections = []
    current_title = None
    current_content = []

    idx = 1

    for line in lines:
        if line.startswith('### '):
            # Save previous section if exists
            if current_title is not None:
                sections.append((current_title, '\n'.join(current_content)))
                idx = 1
                current_content = []
            # Extract title (remove '### ' prefix and normalize whitespace)
            current_title = re.sub(r'\s+', ' ', line[4:].strip())
        elif line.strip():
            current_content.append(f"{idx}. {line.strip()}")
            idx += 1
    
    # Save last section
    if current_title is not None:
        sections.append((current_title, '\n'.join(current_content)))
    
    if not sections:
        print("❌ No sections found. File must contain '### PAGE' markers.", file=sys.stderr)
        sys.exit(1)

    # Create output directory
    os.makedirs(output_dir, exist_ok=True)

    # Write sections to files
    duplicates = {}
    for title, content in sections:
        base_name = sanitize_filename(title)
        filename = base_name
        counter = 1
        
        # Handle duplicate filenames (e.g., multiple "SECTION 1")
        while filename in duplicates:
            name, ext = os.path.splitext(base_name)
            filename = f"{name}_{counter}{ext}"
            counter += 1
        duplicates[filename] = True
        
        filepath = os.path.join(output_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Created: {filepath} (from '{title}')")

    print(f"\n✨ Successfully split {len(sections)} sections into '{output_dir}' folder")

if __name__ == '__main__':
    main()
