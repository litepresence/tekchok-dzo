import re

with open('02_extract_content_v4.py', 'r') as f:
    content = f.read()

# Fix the blank line issue - should be single blank lines, not double
old_code = '''            else:
                # Subsequent pages - add FOLIO with blank line separator
                content_parts.append(f"\\n\\nFOLIO_{current_page:03d}\\n\\n")'''

new_code = '''            else:
                # Subsequent pages - add FOLIO with blank line separator
                content_parts.append(f"\\nFOLIO_{current_page:03d}\\n")'''

if old_code in content:
    content = content.replace(old_code, new_code)
    with open('02_extract_content_v4.py', 'w') as f:
        f.write(content)
    print("✓ Fixed blank line issue (\\n\\n -> \\n)")
else:
    print("✗ Could not find pattern")
    # Try to find it
    import re
    match = re.search(r'else:.*?content_parts\.append\(f"\\n\\nFOLIO_', content, re.DOTALL)
    if match:
        print("Found near:", match.group()[:100])
