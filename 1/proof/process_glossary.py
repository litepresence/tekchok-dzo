#!/usr/bin/env python3
"""
Glossary Markdown to HTML Converter (Scholarly Dark Theme)
Converts glossary.md to glossary.html format with print-friendly dark theme styling.
"""

import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

# Try to import markdown library, fall back to basic parsing if not available
try:
    import markdown
    HAS_MARKDOWN = True
except ImportError:
    HAS_MARKDOWN = False
    print("Warning: markdown library not installed. Using basic parsing.")
    print("Install with: pip install markdown")


class GlossaryConverter:
    """Converts markdown glossary to HTML format with scholarly dark theme."""
    
    def __init__(self, input_file: str, output_file: str):
        self.input_file = Path(input_file)
        self.output_file = Path(output_file)
        self.content = ""
        self.html_content = ""
        
    def read_markdown(self) -> str:
        """Read the markdown file content."""
        with open(self.input_file, 'r', encoding='utf-8') as f:
            self.content = f.read()
        return self.content
    
    def parse_horizontal_rules(self, content: str) -> str:
        """Convert markdown horizontal rules (---) to HTML <hr> tags."""
        lines = content.split('\n')
        result_lines = []
        
        for line in lines:
            stripped = line.strip()
            # Check for horizontal rule (---, ***, ___)
            if re.match(r'^(-{3,}|\*{3,}|_{3,})$', stripped):
                result_lines.append('<hr>')
            else:
                result_lines.append(line)
        
        return '\n'.join(result_lines)
    
    def parse_tables(self, content: str) -> str:
        """
        Parse markdown tables and convert to HTML tables.
        Handles the glossary table format specifically.
        """
        lines = content.split('\n')
        result_lines = []
        in_table = False
        table_rows = []
        table_headers = []
        
        i = 0
        while i < len(lines):
            line = lines[i]
            
            # Detect table start (line with | characters)
            if line.strip().startswith('|') and '|' in line:
                if not in_table:
                    in_table = True
                    table_rows = []
                    table_headers = []
                
                # Split by | and clean
                cells = [cell.strip() for cell in line.split('|')]
                cells = [cell for cell in cells if cell]  # Remove empty cells
                
                # Check if this is separator line (---|---|---)
                if all(re.match(r'^-+:?-*$', cell) for cell in cells):
                    # This is the separator line, skip it
                    i += 1
                    continue
                
                if not table_headers:
                    table_headers = cells
                else:
                    table_rows.append(cells)
                
                # Check if table ends (next line doesn't start with |)
                if i + 1 < len(lines):
                    next_line = lines[i + 1]
                    if not next_line.strip().startswith('|'):
                        # End of table, convert to HTML
                        html_table = self._convert_table_to_html(table_headers, table_rows)
                        result_lines.append(html_table)
                        in_table = False
                        table_rows = []
                        table_headers = []
            else:
                if in_table:
                    # Table ended without proper detection, convert anyway
                    html_table = self._convert_table_to_html(table_headers, table_rows)
                    result_lines.append(html_table)
                    in_table = False
                    table_rows = []
                    table_headers = []
                result_lines.append(line)
            
            i += 1
        
        # Handle any remaining table
        if in_table and table_headers:
            html_table = self._convert_table_to_html(table_headers, table_rows)
            result_lines.append(html_table)
        
        return '\n'.join(result_lines)
    
    def _convert_table_to_html(self, headers: List[str], rows: List[List[str]]) -> str:
        """Convert table data to HTML table with letter section headers."""
        if not headers:
            return ""
        
        html = ['<table class="glossary-table">']
        
        # Header row
        html.append('  <thead>')
        html.append('    <tr>')
        for header in headers:
            # Clean header text
            header = self._clean_cell_content(header)
            html.append(f'      <th>{header}</th>')
        html.append('    </tr>')
        html.append('  </thead>')
        
        # Body rows
        html.append('  <tbody>')
        
        last_letter = None
        for row in rows:
            # Extract first letter from first column (from bold text)
            first_letter = ''
            if row and row[0]:
                # Look for bold text pattern **(letter)**
                bold_match = re.search(r'\*\*([A-Za-z])', row[0])
                if bold_match:
                    first_letter = bold_match.group(1).upper()
            
            # Add letter section header if letter changed
            if first_letter and first_letter != last_letter:
                if last_letter is not None:
                    html.append('  </tbody>')
                    html.append('</table>')
                    html.append(f'<table class="glossary-table">')
                    html.append('  <tbody>')
                html.append(f'    <tr class="letter-section">')
                html.append(f'      <td colspan="{len(headers)}"><h3 id="letter-{first_letter}">{first_letter}</h3></td>')
                html.append('    </tr>')
                last_letter = first_letter
            
            html.append('    <tr>')
            # Pad row if needed
            while len(row) < len(headers):
                row.append('')
            for cell in row:
                cell = self._clean_cell_content(cell)
                html.append(f'      <td>{cell}</td>')
            html.append('    </tr>')
        html.append('  </tbody>')
        html.append('</table>')
        
        return '\n'.join(html)
    
    def _clean_cell_content(self, content: str) -> str:
        """Clean and process cell content for HTML."""
        # Remove extra whitespace
        content = ' '.join(content.split())
        
        # Convert bold markdown to HTML
        content = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', content)
        content = re.sub(r'__(.+?)__', r'<strong>\1</strong>', content)
        
        # Convert italic markdown to HTML
        content = re.sub(r'\*(.+?)\*', r'<em>\1</em>', content)
        content = re.sub(r'_(.+?)_', r'<em>\1</em>', content)
        
        # Convert inline code to HTML
        content = re.sub(r'`(.+?)`', r'<code>\1</code>', content)
        
        # Convert links
        content = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', content)
        
        return content
    
    def parse_headers(self, content: str) -> str:
        """Convert markdown headers to HTML headers."""
        lines = content.split('\n')
        result_lines = []
        
        for line in lines:
            # Check for ATX-style headers (# ## ### etc.)
            match = re.match(r'^(#{1,6})\s+(.+)$', line)
            if match:
                level = len(match.group(1))
                text = match.group(2).strip()
                text = self._clean_cell_content(text)
                html_header = f'<h{level} class="section-header">{text}</h{level}>'
                result_lines.append(html_header)
            else:
                result_lines.append(line)
        
        return '\n'.join(result_lines)
    
    def parse_code_blocks(self, content: str) -> str:
        """Convert markdown code blocks to HTML pre/code blocks."""
        # Handle fenced code blocks (```)
        content = re.sub(
            r'```(\w*)\n(.*?)```',
            lambda m: f'<pre class="code-block"><code class="language-{m.group(1)}">{m.group(2)}</code></pre>',
            content,
            flags=re.DOTALL
        )
        
        return content
    
    def parse_paragraphs(self, content: str) -> str:
        """Wrap text paragraphs in <p> tags."""
        lines = content.split('\n')
        result_lines = []
        paragraph_lines = []
        
        def flush_paragraph():
            if paragraph_lines:
                text = ' '.join(paragraph_lines)
                text = self._clean_cell_content(text)
                if text.strip() and not text.strip().startswith('<'):
                    result_lines.append(f'<p class="text-paragraph">{text}</p>')
                else:
                    result_lines.append(text)
            paragraph_lines.clear()
        
        for line in lines:
            stripped = line.strip()
            
            # Check if this is HTML or special content
            if stripped.startswith('<') or stripped.startswith('ACQUAINTANCE:'):
                flush_paragraph()
                if stripped.startswith('ACQUAINTANCE:'):
                    stripped = stripped.replace('ACQUAINTANCE:', '<p class="acquaintance-note"><strong>ACQUAINTANCE:</strong>')
                    result_lines.append(stripped + '</p>')
                else:
                    result_lines.append(line)
            elif stripped == '':
                flush_paragraph()
                result_lines.append('')
            elif stripped.startswith('|') or stripped.startswith('#'):
                flush_paragraph()
                result_lines.append(line)
            else:
                paragraph_lines.append(stripped)
        
        flush_paragraph()
        return '\n'.join(result_lines)
    
    def add_html_structure(self, content: str) -> str:
        """Wrap content in full HTML document structure with SCHOLARLY DARK THEME."""
        # NOTE: All CSS curly braces must be doubled {{ }} for .format() to work
        html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Glossary of Lineage-Specific Terms</title>
    <link rel="stylesheet" href="../css/glossary.css">
    <script src="../js/glossary.js"></script>
</head>
<body>
    <div class="document">
{content}
    </div>
</body>
</html>"""
        
        return html_template.format(content=content)
    
    def convert(self) -> str:
        """Main conversion method."""
        # Read markdown content
        self.read_markdown()
        
        # Process content through various parsers
        content = self.content
        
        # Parse horizontal rules first
        content = self.parse_horizontal_rules(content)
        
        # Parse tables (before other transformations)
        content = self.parse_tables(content)
        
        # Parse headers
        content = self.parse_headers(content)
        
        # Parse code blocks
        content = self.parse_code_blocks(content)
        
        # Parse paragraphs
        content = self.parse_paragraphs(content)
        
        # Add HTML structure
        self.html_content = self.add_html_structure(content)
        
        return self.html_content
    
    def write_html(self):
        """Write the HTML content to output file."""
        with open(self.output_file, 'w', encoding='utf-8') as f:
            f.write(self.html_content)
        print(f"Successfully converted {self.input_file} to {self.output_file}")


def convert_with_markdown_library(input_file: str, output_file: str):
    """
    Alternative conversion using the markdown library.
    Provides better markdown parsing if library is available.
    """
    if not HAS_MARKDOWN:
        return False
    
    with open(input_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Configure markdown with extensions
    md = markdown.Markdown(extensions=[
        'tables',
        'fenced_code',
        'toc',
        'codehilite'
    ])
    
    html_body = md.convert(md_content)
    
    # Wrap in full HTML document with SCHOLARLY DARK THEME
    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Glossary of Lineage-Specific Terms</title>
    <link rel="stylesheet" href="../css/glossary.css">
    <script src="../js/glossary.js"></script>
</head>
<body>
    <div class="document">
{content}
    </div>
</body>
</html>"""
    
    html_content = html_template.format(content=html_body)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Successfully converted {input_file} to {output_file} (using markdown library)")
    return True


if __name__ == "__main__":
    input_file = Path("../text/glossary.md")
    output_file = Path("html/glossary.html")
    
    if not input_file.exists():
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)
    
    converter = GlossaryConverter(str(input_file), str(output_file))
    converter.convert()
    converter.write_html()
