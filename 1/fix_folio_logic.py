import re

with open('02_extract_content_v4.py', 'r') as f:
    content = f.read()

# Fix the FOLIO logic
old_code = '''        if selected_lines:
            # Add FOLIO marker
            if first_page and volume == 1 and current_page == 1:
                content_parts.append(f"FOLIO_{current_page:03d}\\n")
                first_page = False
            elif not first_page:
                content_parts.append(f"\\nFOLIO_{current_page:03d}\\n")'''

new_code = '''        if selected_lines:
            # Add FOLIO marker at the start of each page's content
            if first_page:
                # First page of section - always add FOLIO marker
                content_parts.append(f"FOLIO_{current_page:03d}\\n")
                first_page = False
            else:
                # Subsequent pages - add FOLIO with blank line separator
                content_parts.append(f"\\n\\nFOLIO_{current_page:03d}\\n\\n")'''

if old_code in content:
    content = content.replace(old_code, new_code)
    with open('02_extract_content_v4.py', 'w') as f:
        f.write(content)
    print("✓ Fixed FOLIO logic")
else:
    print("✗ Could not find code to fix")
    print("Searching for pattern...")
    # Show what's actually there
    import re
    match = re.search(r'if selected_lines:.*?elif not first_page:', content, re.DOTALL)
    if match:
        print("Found:")
        print(match.group()[:200])
