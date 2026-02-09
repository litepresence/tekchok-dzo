import re

# Read the extraction script
with open('02_extract_content_v3.py', 'r') as f:
    content = f.read()

# Find the liturgical mapping section and add blank line filtering
old_code = '''            if parsed is None:
                # No line number in source - handle specially
                if layer == 'liturgical' and tibetan_line_nums and tibetan_idx < len(tibetan_line_nums):
                    # Map to Tibetan line number
                    line_num = tibetan_line_nums[tibetan_idx]
                    line_content = line.strip()
                    tibetan_idx += 1
                else:
                    continue'''

new_code = '''            if parsed is None:
                # No line number in source - handle specially
                if layer == 'liturgical' and tibetan_line_nums and tibetan_idx < len(tibetan_line_nums):
                    # Map to Tibetan line number
                    line_content = line.strip()
                    # Skip blank lines in liturgical source
                    if not line_content:
                        tibetan_idx += 1
                        continue
                    line_num = tibetan_line_nums[tibetan_idx]
                    tibetan_idx += 1
                else:
                    continue'''

if old_code in content:
    content = content.replace(old_code, new_code)
    with open('02_extract_content_v3.py', 'w') as f:
        f.write(content)
    print("✓ Added liturgical blank line filtering")
else:
    print("✗ Could not find insertion point")
