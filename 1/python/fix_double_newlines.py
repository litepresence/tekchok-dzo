with open('02_extract_content_v4.py', 'r') as f:
    content = f.read()

# Remove the \n from FOLIO markers since join() will add newlines
old_code = '''                content_parts.append(f"FOLIO_{current_page:03d}\\n")'''
new_code = '''                content_parts.append(f"FOLIO_{current_page:03d}")'''

if old_code in content:
    content = content.replace(old_code, new_code)
    with open('02_extract_content_v4.py', 'w') as f:
        f.write(content)
    print("✓ Fixed double newline in FOLIO (first_page)")
else:
    print("✗ Pattern not found for first_page")

# Also fix the subsequent pages
old_code2 = '''                content_parts.append(f"\\nFOLIO_{current_page:03d}\\n")'''
new_code2 = '''                content_parts.append(f"FOLIO_{current_page:03d}")'''

if old_code2 in content:
    content = content.replace(old_code2, new_code2)
    with open('02_extract_content_v4.py', 'w') as f:
        f.write(content)
    print("✓ Fixed double newline in FOLIO (subsequent pages)")
else:
    print("✗ Pattern not found for subsequent pages")
