import os
import re
import glob

# CONFIGURATION
INPUT_FOLDER = "chapter"  # The folder containing your .txt files
OUTPUT_FOLDER = "html_output" # Where the HTML files will be saved

def get_css():
    """Returns the CSS styling for the book layout."""
    return """
    <style>
        body {
            font-family: 'Georgia', 'Merriweather', serif;
            line-height: 1.6;
            color: #333;
            background-color: #f4f1ea; /* Parchment color */
            margin: 0;
            padding: 20px;
        }
        .book-container {
            max-width: 800px;
            margin: 0 auto;
            background: #fff;
            padding: 40px 60px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            border-radius: 4px;
        }
        h2 {
            color: #8b0000; /* Deep red for chapter titles */
            border-bottom: 2px solid #8b0000;
            padding-bottom: 10px;
            margin-top: 40px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        h3 {
            color: #555;
            margin-top: 30px;
            font-style: italic;
        }
        strong {
            color: #000;
            font-weight: 700;
        }
        blockquote.tantra {
            background-color: #f9f9f9;
            border-left: 5px solid #8b0000;
            margin: 20px 0;
            padding: 15px 20px;
            font-style: italic;
            color: #555;
            font-size: 1.05em;
        }
        ul {
            margin-bottom: 20px;
        }
        li {
            margin-bottom: 8px;
        }
        hr {
            border: 0;
            height: 1px;
            background-image: linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0));
            margin: 40px 0;
        }
        .ornament {
            text-align: center;
            font-size: 1.5em;
            color: #8b0000;
            margin: 30px 0;
            font-family: 'Times New Roman', serif;
        }
        .metadata {
            font-size: 0.9em;
            color: #666;
            background: #eee;
            padding: 10px;
            border-radius: 4px;
            margin-bottom: 20px;
        }
    </style>
    """

def process_content(content):
    """Parses the text content and converts it to HTML."""
    lines = content.split('\n')
    html_lines = []
    in_list = False
    
    # Regex patterns
    bold_pattern = re.compile(r'\*\*(.*?)\*\*')
    header_h2_pattern = re.compile(r'^##\s+(.*)')
    header_h3_pattern = re.compile(r'^###\s+(.*)')
    hr_pattern = re.compile(r'^---\s*$')
    list_pattern = re.compile(r'^<list>\s*(.*)')
    tantra_pattern = re.compile(r'<tantra>(.*?)</tantra>', re.DOTALL)
    ornament_pattern = re.compile(r'<ornament>(.*?)</ornament>', re.DOTALL)

    for line in lines:
        stripped = line.strip()
        
        # 1. Handle Horizontal Rules
        if hr_pattern.match(stripped):
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append("<hr>")
            continue

        # 2. Handle Headers
        h2_match = header_h2_pattern.match(stripped)
        if h2_match:
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append(f"<h2>{h2_match.group(1)}</h2>")
            continue

        h3_match = header_h3_pattern.match(stripped)
        if h3_match:
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append(f"<h3>{h3_match.group(1)}</h3>")
            continue

        # 3. Handle Lists
        list_match = list_pattern.match(stripped)
        if list_match:
            if not in_list:
                html_lines.append("<ul>")
                in_list = True
            item_content = list_match.group(1)
            # Process bolding inside list items
            item_content = bold_pattern.sub(r'<strong>\1</strong>', item_content)
            html_lines.append(f"<li>{item_content}</li>")
            continue
        else:
            # If we were in a list and hit a non-list line, close the list
            if in_list:
                html_lines.append("</ul>")
                in_list = False

        # 4. Handle Custom Tags (Tantra, Ornament)
        # We do this on the whole line to catch multiline or complex structures
        processed_line = stripped
        
        # Replace Tantra tags
        processed_line = tantra_pattern.sub(r'<blockquote class="tantra">\1</blockquote>', processed_line)
        
        # Replace Ornament tags
        processed_line = ornament_pattern.sub(r'<div class="ornament">\1</div>', processed_line)

        # 5. Handle Bold Text (Global)
        processed_line = bold_pattern.sub(r'<strong>\1</strong>', processed_line)

        # 6. Handle Metadata Blocks (Optional visual tweak)
        # If line starts with **Tibetan:** or **Location:**, we might want to wrap it
        if stripped.startswith("**Tibetan:**") or stripped.startswith("**Location:**"):
             processed_line = f'<div class="metadata">{processed_line}</div>'

        if processed_line:
            html_lines.append(f"<p>{processed_line}</p>")
        else:
            # Preserve empty lines as breaks if needed, or ignore
            pass

    # Close any remaining open list
    if in_list:
        html_lines.append("</ul>")

    return "\n".join(html_lines)

def convert_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    body_html = process_content(content)
    
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chapter Conversion</title>
    {get_css()}
</head>
<body>
    <div class="book-container">
        {body_html}
    </div>
</body>
</html>
"""

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f"Converted: {os.path.basename(input_path)}")

def main():
    # Create output folder if it doesn't exist
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    # Find all txt files in the input folder
    # Adjust the pattern if your files have a different extension
    files = glob.glob(os.path.join(INPUT_FOLDER, "*.txt"))
    
    if not files:
        print(f"No .txt files found in '{INPUT_FOLDER}' folder.")
        return

    print(f"Found {len(files)} files. Converting...")
    
    for file_path in files:
        filename = os.path.basename(file_path)
        output_filename = filename.replace(".txt", ".html")
        output_path = os.path.join(OUTPUT_FOLDER, output_filename)
        
        try:
            convert_file(file_path, output_path)
        except Exception as e:
            print(f"Error processing {filename}: {e}")

    print(f"\nDone! Files saved to '{OUTPUT_FOLDER}' folder.")

if __name__ == "__main__":
    main()
