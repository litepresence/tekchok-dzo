import re

# Read the extraction script
with open('02_extract_content_v3.py', 'r') as f:
    content = f.read()

# Find the section where we process lines and add signature filtering
# We need to add a check to skip signature lines

old_code = '''        for line in page_lines:
            parsed = parse_line_number(line)
            
            if parsed is None:'''

new_code = '''        for line in page_lines:
            # Skip Patrul Rinpoche signature lines in commentary layers
            if layer in RANGE_LAYERS:
                stripped = line.strip()
                if stripped.startswith('—Patrul') or stripped.startswith('--Patrul') or stripped.startswith('COMMENTARY ON PAGE'):
                    continue
            
            parsed = parse_line_number(line)
            
            if parsed is None:'''

if old_code in content:
    content = content.replace(old_code, new_code)
    with open('02_extract_content_v3.py', 'w') as f:
        f.write(content)
    print("✓ Added signature line filtering")
else:
    print("✗ Could not find insertion point")
