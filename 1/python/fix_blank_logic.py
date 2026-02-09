with open('02_extract_content_v4.py', 'r') as f:
    content = f.read()

# Remove the blank line before FOLIO - we only need after
old_code = '''            else:
                # Subsequent pages - add blank line, FOLIO, blank line
                content_parts.append("")  # Blank line before FOLIO
                content_parts.append(f"FOLIO_{current_page:03d}")
                content_parts.append("")  # Blank line after FOLIO'''

new_code = '''            else:
                # Subsequent pages - add FOLIO with blank line after
                content_parts.append(f"FOLIO_{current_page:03d}")
                content_parts.append("")  # Blank line after FOLIO'''

if old_code in content:
    content = content.replace(old_code, new_code)
    with open('02_extract_content_v4.py', 'w') as f:
        f.write(content)
    print("✓ Removed blank line before FOLIO")
else:
    print("✗ Pattern not found")
