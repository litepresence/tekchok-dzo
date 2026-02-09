import re

# Read the extraction script
with open('02_extract_content_v3.py', 'r') as f:
    content = f.read()

# Find where we parse lines and add check for empty content
old_code = '''            if parsed is None:
                # No line number in source - handle specially
                if layer == 'liturgical' and tibetan_line_nums and tibetan_idx < len(tibetan_line_nums):
                    # Map to Tibetan line number
                    line_num = tibetan_line_nums[tibetan_idx]
                    line_content = line.strip()
                    tibetan_idx += 1
                else:
                    continue
            else:
                # Use the line number from source
                line_num = parsed['line_num']
                line_content = parsed['content']'''

new_code = '''            if parsed is None:
                # No line number in source - handle specially
                if layer == 'liturgical' and tibetan_line_nums and tibetan_idx < len(tibetan_line_nums):
                    # Map to Tibetan line number
                    line_num = tibetan_line_nums[tibetan_idx]
                    line_content = line.strip()
                    tibetan_idx += 1
                else:
                    continue
            else:
                # Use the line number from source
                line_num = parsed['line_num']
                line_content = parsed['content']
                
                # Skip lines with empty content (like [433] with nothing after)
                if not line_content.strip():
                    continue'''

if old_code in content:
    content = content.replace(old_code, new_code)
    with open('02_extract_content_v3.py', 'w') as f:
        f.write(content)
    print("✓ Added empty content filtering")
else:
    print("✗ Could not find insertion point")
