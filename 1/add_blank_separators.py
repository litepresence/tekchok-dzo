with open('02_extract_content_v4.py', 'r') as f:
    content = f.read()

# Fix first page - add blank line after FOLIO
old_first = '''            if first_page:
                # First page of section - always add FOLIO marker
                content_parts.append(f"FOLIO_{current_page:03d}")
                first_page = False
            else:
                # Subsequent pages - add FOLIO with blank line separator
                content_parts.append(f"FOLIO_{current_page:03d}")'''

new_first = '''            if first_page:
                # First page of section - add FOLIO marker with trailing blank line
                content_parts.append(f"FOLIO_{current_page:03d}")
                content_parts.append("")  # Blank line after FOLIO
                first_page = False
            else:
                # Subsequent pages - add blank line, FOLIO, blank line
                content_parts.append("")  # Blank line before FOLIO
                content_parts.append(f"FOLIO_{current_page:03d}")
                content_parts.append("")  # Blank line after FOLIO'''

if old_first in content:
    content = content.replace(old_first, new_first)
    with open('02_extract_content_v4.py', 'w') as f:
        f.write(content)
    print("✓ Added blank line separators")
else:
    print("✗ Pattern not found")
    # Show what's there
    import re
    match = re.search(r'if first_page:.*?else:.*?content_parts\.append\(f"FOLIO_', content, re.DOTALL)
    if match:
        print("Found:")
        print(match.group()[:200])
