import os
import re
import glob
import markdown

# CONFIGURATION
INPUT_FOLDER = "chapter"
OUTPUT_FOLDER = "html_output"

def get_css():
    """Returns minimal CSS styling - let PDF engine handle margins."""
    return """
    <style>
        body {
            font-family: 'Georgia', 'Merriweather', serif;
            line-height: 1.7;
            color: #333;
            margin: 0;
            padding: 0;
        }
        h2 {
            color: #8b0000;
            border-bottom: 2px solid #8b0000;
            padding-bottom: 8px;
            margin-top: 2em;
            margin-bottom: 1em;
            text-transform: uppercase;
            letter-spacing: 1px;
            page-break-after: avoid;
        }
        h3 {
            color: #555;
            margin-top: 1.5em;
            margin-bottom: 0.8em;
            font-style: italic;
            page-break-after: avoid;
        }
        h4 {
            color: #666;
            margin-top: 1.2em;
            margin-bottom: 0.6em;
            page-break-after: avoid;
        }
        strong {
            font-weight: 700;
        }
        blockquote.tantra {
            background-color: #f9f9f9;
            border-left: 4px solid #8b0000;
            margin: 1.5em 0;
            padding: 1em 1.2em;
            font-style: italic;
            color: #555;
            page-break-inside: avoid;
        }
        ul, ol {
            margin: 1em 0;
            padding-left: 1.5em;
        }
        li {
            margin-bottom: 0.5em;
        }
        hr {
            border: 0;
            border-top: 1px solid #ccc;
            margin: 2em 0;
        }
        .ornament {
            text-align: center;
            font-size: 1.3em;
            color: #8b0000;
            margin: 2em 0;
            font-family: 'Times New Roman', serif;
        }
        .metadata {
            font-size: 0.85em;
            color: #666;
            background: #f5f5f5;
            padding: 0.8em 1em;
            margin: 1em 0;
            border-left: 3px solid #8b0000;
            page-break-inside: avoid;
        }
        p {
            margin: 1em 0;
            text-align: justify;
        }
        /* Print/PDF specific */
        @media print {
            body {
                font-size: 11pt;
            }
            h2 {
                page-break-before: always;
            }
            blockquote.tantra, .metadata {
                page-break-inside: avoid;
            }
        }
    </style>
    """

def protect_custom_tags(content):
    """Protect custom tags from Markdown parser."""
    placeholders = {}
    counter = [0]
    
    def replace_tag(match):
        tag_type = match.group(1)
        tag_content = match.group(2)
        placeholder = f"__CUSTOM_TAG_{counter[0]}__"
        placeholders[placeholder] = (tag_type, tag_content)
        counter[0] += 1
        return placeholder
    
    content = re.sub(r'<tantra>(.*?)</tantra>', replace_tag, content, flags=re.DOTALL)
    content = re.sub(r'<list>(.*?)</list>', replace_tag, content, flags=re.DOTALL)
    content = re.sub(r'<ornament>(.*?)</ornament>', replace_tag, content, flags=re.DOTALL)
    
    return content, placeholders

def restore_custom_tags(html_content, placeholders):
    """Restore custom tags after Markdown processing."""
    for placeholder, (tag_type, tag_content) in placeholders.items():
        if tag_type == 'tantra':
            tag_content_html = markdown.markdown(tag_content, extensions=['extra'])
            tag_content_html = re.sub(r'^<p>|</p>$', '', tag_content_html)
            replacement = f'<blockquote class="tantra">{tag_content_html}</blockquote>'
        elif tag_type == 'list':
            tag_content_html = markdown.markdown(tag_content, extensions=['extra'])
            tag_content_html = re.sub(r'^<p>|</p>$', '', tag_content_html)
            replacement = f'<li>{tag_content_html}</li>'
        elif tag_type == 'ornament':
            tag_content_html = markdown.markdown(tag_content, extensions=['extra'])
            replacement = f'<div class="ornament">{tag_content_html}</div>'
        else:
            replacement = f'<{tag_type}>{tag_content}</{tag_type}>'
        
        html_content = html_content.replace(placeholder, replacement)
    
    return html_content

def process_line_prefixes(content):
    """Handle line-level custom tags."""
    lines = content.split('\n')
    processed_lines = []
    
    for line in lines:
        if line.strip().startswith('<list>'):
            line = re.sub(r'^(\s*)<list>\s*', r'\1- ', line)
        processed_lines.append(line)
    
    return '\n'.join(processed_lines)

def post_process_html(html_content):
    """Additional post-processing."""
    metadata_patterns = [
        r'(<p><strong>Tibetan:</strong>.*?</p>)',
        r'(<p><strong>Location:</strong>.*?</p>)',
        r'(<p><strong>Tibetan Lines:</strong>.*?</p>)',
        r'(<p><strong>Total Liturgical Lines:</strong>.*?</p>)',
    ]
    
    for pattern in metadata_patterns:
        html_content = re.sub(
            pattern,
            lambda m: f'<div class="metadata">{m.group(1)}</div>',
            html_content
        )
    
    return html_content

def convert_file(input_path, output_path):
    """Convert a single file from markdown to HTML."""
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    protected_content, placeholders = protect_custom_tags(content)
    protected_content = process_line_prefixes(protected_content)
    
    md = markdown.Markdown(extensions=['extra', 'tables', 'fenced_code'])
    html_body = md.convert(protected_content)
    
    html_body = restore_custom_tags(html_body, placeholders)
    html_body = post_process_html(html_body)
    
    # Extract title from first h2 if present
    title_match = re.search(r'<h2>(.*?)</h2>', html_body)
    title = title_match.group(1) if title_match else "Chapter"
    
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    {get_css()}
</head>
<body>
{html_body}
</body>
</html>
"""
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    print(f"✓ Converted: {os.path.basename(input_path)}")
    os.system(f"pypy -m md2pdf {output_path} {output_path+'.pdf'}")

def main():
    try:
        import markdown
    except ImportError:
        print("ERROR: The 'markdown' library is not installed.")
        print("Please install it with: pip install markdown")
        return
    
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
    
    files = glob.glob(os.path.join(INPUT_FOLDER, "*.txt"))
    
    if not files:
        print(f"⚠ No .txt files found in '{INPUT_FOLDER}' folder.")
        return
    
    print(f"📚 Found {len(files)} files. Converting...\n")
    
    for file_path in sorted(files):
        filename = os.path.basename(file_path)
        output_filename = filename.replace(".txt", ".html")
        output_path = os.path.join(OUTPUT_FOLDER, output_filename)
        
        try:
            convert_file(file_path, output_path)
        except Exception as e:
            print(f"✗ Error processing {filename}: {e}")
    
    print(f"\n✅ Done! Files saved to '{OUTPUT_FOLDER}' folder.")

if __name__ == "__main__":
    main()
