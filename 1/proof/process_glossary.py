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
        """Convert table data to HTML table."""
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
        for row in rows:
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
    <style>
        @page {{
            size: 6in 9in;
            margin: 0.75in;
            @bottom-center {{
                content: counter(page);
                color: #888;
            }}
        }}

        :root {{
            --font-main: 'Georgia', 'Times New Roman', serif;
            --font-mono: 'Courier New', 'Consolas', monospace;
            --font-sans: 'Helvetica', 'Arial', sans-serif;
            
            --color-bg: #1e1e1e;
            --color-text: #e0e0e0;
            --color-muted: #a0a0a0;
            --color-accent: #64b5f6;
            --color-line-num: #757575;
            --color-border: #3a3a3a;
            --color-btn: #2d5a7b;
            --color-btn-hover: #3d7a9b;
            --color-table-header: #2d3a4a;
            --color-table-row-alt: #252525;
            --color-table-row-hover: #2d3a4a;
            
            --line-height: 1.5;
        }}

        body.light-mode {{
            --color-bg: #fafafa;
            --color-text: #1a1a1a;
            --color-muted: #666;
            --color-accent: #1565c0;
            --color-line-num: #999;
            --color-border: #ddd;
            --color-btn: #1565c0;
            --color-btn-hover: #1976d2;
            --color-table-header: #e3f2fd;
            --color-table-row-alt: #f5f5f5;
            --color-table-row-hover: #e3f2fd;
        }}

        * {{
            box-sizing: border-box;
        }}

        body {{
            font-family: var(--font-main);
            color: var(--color-text);
            line-height: var(--line-height);
            font-size: 10pt;
            margin: 0;
            padding: 0;
            background-color: var(--color-bg);
            -webkit-print-color-adjust: exact;
            print-color-adjust: exact;
        }}

        .document {{
            max-width: 5.5in;
            margin: 0 auto;
            padding: 40px 20px;
        }}

        h1 {{
            font-size: 1.8em;
            color: var(--color-accent);
            border-bottom: 2px solid var(--color-border);
            padding-bottom: 0.5em;
            margin-top: 0;
            margin-bottom: 1.5em;
            font-variant: small-caps;
            letter-spacing: 1px;
        }}

        h2 {{
            font-size: 1.4em;
            color: var(--color-accent);
            border-bottom: 1px solid var(--color-border);
            padding-bottom: 0.3em;
            margin-top: 2em;
            margin-bottom: 1em;
            font-variant: small-caps;
        }}

        h3 {{
            font-size: 1.2em;
            color: var(--color-muted);
            margin-top: 1.5em;
            margin-bottom: 0.8em;
            font-variant: small-caps;
        }}

        h4 {{
            font-size: 1em;
            color: var(--color-muted);
            margin-top: 1.2em;
            margin-bottom: 0.5em;
        }}

        hr {{
            border: none;
            border-top: 1px solid var(--color-border);
            margin: 2em 0;
        }}

        .glossary-table {{
            width: 100%;
            border-collapse: collapse;
            margin: 1.5em 0;
            background-color: transparent;
            font-size: 0.95em;
        }}

        .glossary-table th,
        .glossary-table td {{
            border: 1px solid var(--color-border);
            padding: 10px 12px;
            text-align: left;
            vertical-align: top;
        }}

        .glossary-table th {{
            background-color: var(--color-table-header);
            font-weight: bold;
            color: var(--color-accent);
            font-variant: small-caps;
            letter-spacing: 0.5px;
            font-size: 0.9em;
        }}

        .glossary-table tr:nth-child(even) {{
            background-color: var(--color-table-row-alt);
        }}

        .glossary-table tr:nth-child(odd) {{
            background-color: transparent;
        }}

        .glossary-table tr:hover {{
            background-color: var(--color-table-row-hover);
        }}

        .glossary-table td:first-child {{
            font-weight: bold;
            color: var(--color-accent);
            width: 30%;
        }}

        .glossary-table td:last-child {{
            font-family: var(--font-mono);
            font-size: 0.85em;
            color: var(--color-line-num);
            width: 15%;
        }}

        code {{
            background-color: var(--color-table-header);
            padding: 2px 6px;
            border-radius: 3px;
            font-family: var(--font-mono);
            font-size: 0.9em;
            color: var(--color-accent);
        }}

        pre {{
            background-color: var(--color-table-header);
            padding: 15px;
            border-radius: 4px;
            overflow-x: auto;
            border: 1px solid var(--color-border);
            margin: 1.5em 0;
        }}

        pre code {{
            background-color: transparent;
            padding: 0;
            color: var(--color-text);
        }}

        a {{
            color: var(--color-accent);
            text-decoration: none;
            border-bottom: 1px dotted var(--color-accent);
        }}

        a:hover {{
            color: var(--color-btn-hover);
            border-bottom: 1px solid var(--color-btn-hover);
        }}

        .acquaintance-note {{
            background-color: var(--color-table-header);
            padding: 15px 20px;
            border-left: 3px solid var(--color-accent);
            margin: 1.5em 0;
            border-radius: 0 4px 4px 0;
            font-size: 0.95em;
        }}

        p {{
            margin: 1em 0;
            text-align: justify;
        }}

        strong {{
            color: var(--color-accent);
        }}

        em {{
            color: var(--color-muted);
            font-style: italic;
        }}

        .section-header {{
            color: var(--color-accent);
        }}

        .text-paragraph {{
            margin: 1em 0;
        }}

        .file-separator {{
            margin-top: 2em;
            margin-bottom: 1em;
            padding-top: 1em;
            border-top: 1px solid var(--color-border);
            text-align: center;
            font-variant: small-caps;
            color: var(--color-accent);
            font-size: 0.95em;
            letter-spacing: 2px;
        }}

        .file-separator:first-child {{
            margin-top: 0;
        }}

        /* Scrollbar styling */
        ::-webkit-scrollbar {{
            width: 10px;
            height: 10px;
        }}

        ::-webkit-scrollbar-track {{
            background: var(--color-bg);
        }}

        ::-webkit-scrollbar-thumb {{
            background: var(--color-border);
            border-radius: 5px;
        }}

        ::-webkit-scrollbar-thumb:hover {{
            background: var(--color-btn);
        }}

        /* Selection styling */
        ::selection {{
            background: var(--color-btn);
            color: var(--color-text);
        }}

        @media print {{
            body {{
                font-size: 9.5pt;
                -webkit-print-color-adjust: exact;
                print-color-adjust: exact;
            }}

            .document {{
                max-width: none;
                padding: 0;
            }}

            a {{
                text-decoration: none;
                color: inherit;
            }}

            .glossary-table {{
                page-break-inside: avoid;
            }}

            .glossary-table tr {{
                page-break-inside: avoid;
            }}
        }}
    </style>
    <script>
    // Dark mode handling - sync with parent
    (function() {{
        document.addEventListener('DOMContentLoaded', function() {{
            const isDark = localStorage.getItem('darkMode') !== 'false';
            if (!isDark) document.body.classList.add('light-mode');
        }});
        
        window.addEventListener('message', function(e) {{
            if (e.data && e.data.type === 'darkModeChange') {{
                document.body.classList.toggle('light-mode', !e.data.enabled);
                localStorage.setItem('darkMode', e.data.enabled);
            }}
        }});
    }})();
    </script>
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
    <style>
        @page {{
            size: 6in 9in;
            margin: 0.75in;
            @bottom-center {{
                content: counter(page);
                color: #888;
            }}
        }}

        :root {{
            --font-main: 'Georgia', 'Times New Roman', serif;
            --font-mono: 'Courier New', 'Consolas', monospace;
            --font-sans: 'Helvetica', 'Arial', sans-serif;
            
            --color-bg: #1e1e1e;
            --color-text: #e0e0e0;
            --color-muted: #a0a0a0;
            --color-accent: #64b5f6;
            --color-line-num: #757575;
            --color-border: #3a3a3a;
            --color-btn: #2d5a7b;
            --color-btn-hover: #3d7a9b;
            --color-table-header: #2d3a4a;
            --color-table-row-alt: #252525;
            --color-table-row-hover: #2d3a4a;
            
            --line-height: 1.5;
        }}

        body.light-mode {{
            --color-bg: #fafafa;
            --color-text: #1a1a1a;
            --color-muted: #666;
            --color-accent: #1565c0;
            --color-line-num: #999;
            --color-border: #ddd;
            --color-btn: #1565c0;
            --color-btn-hover: #1976d2;
            --color-table-header: #e3f2fd;
            --color-table-row-alt: #f5f5f5;
            --color-table-row-hover: #e3f2fd;
        }}

        * {{ box-sizing: border-box; }}

        body {{
            font-family: var(--font-main);
            color: var(--color-text);
            line-height: var(--line-height);
            font-size: 10pt;
            margin: 0;
            padding: 0;
            background-color: var(--color-bg);
            -webkit-print-color-adjust: exact;
            print-color-adjust: exact;
        }}

        .document {{
            max-width: 5.5in;
            margin: 0 auto;
            padding: 40px 20px;
        }}

        h1 {{
            font-size: 1.8em;
            color: var(--color-accent);
            border-bottom: 2px solid var(--color-border);
            padding-bottom: 0.5em;
            margin-top: 0;
            margin-bottom: 1.5em;
            font-variant: small-caps;
            letter-spacing: 1px;
        }}

        h2 {{
            font-size: 1.4em;
            color: var(--color-accent);
            border-bottom: 1px solid var(--color-border);
            padding-bottom: 0.3em;
            margin-top: 2em;
            margin-bottom: 1em;
            font-variant: small-caps;
        }}

        h3 {{
            font-size: 1.2em;
            color: var(--color-muted);
            margin-top: 1.5em;
            margin-bottom: 0.8em;
            font-variant: small-caps;
        }}

        hr {{
            border: none;
            border-top: 1px solid var(--color-border);
            margin: 2em 0;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 1.5em 0;
            background-color: transparent;
            font-size: 0.95em;
        }}

        th, td {{
            border: 1px solid var(--color-border);
            padding: 10px 12px;
            text-align: left;
            vertical-align: top;
        }}

        th {{
            background-color: var(--color-table-header);
            font-weight: bold;
            color: var(--color-accent);
            font-variant: small-caps;
            letter-spacing: 0.5px;
            font-size: 0.9em;
        }}

        tr:nth-child(even) {{ background-color: var(--color-table-row-alt); }}
        tr:nth-child(odd) {{ background-color: transparent; }}
        tr:hover {{ background-color: var(--color-table-row-hover); }}

        code {{
            background-color: var(--color-table-header);
            padding: 2px 6px;
            border-radius: 3px;
            font-family: var(--font-mono);
            font-size: 0.9em;
            color: var(--color-accent);
        }}

        pre {{
            background-color: var(--color-table-header);
            padding: 15px;
            border-radius: 4px;
            overflow-x: auto;
            border: 1px solid var(--color-border);
            margin: 1.5em 0;
        }}

        pre code {{ background-color: transparent; padding: 0; color: var(--color-text); }}

        a {{
            color: var(--color-accent);
            text-decoration: none;
            border-bottom: 1px dotted var(--color-accent);
        }}

        a:hover {{
            color: var(--color-btn-hover);
            border-bottom: 1px solid var(--color-btn-hover);
        }}

        p {{ margin: 1em 0; text-align: justify; }}
        strong {{ color: var(--color-accent); }}
        em {{ color: var(--color-muted); font-style: italic; }}

        ::-webkit-scrollbar {{ width: 10px; height: 10px; }}
        ::-webkit-scrollbar-track {{ background: var(--color-bg); }}
        ::-webkit-scrollbar-thumb {{ background: var(--color-border); border-radius: 5px; }}
        ::-webkit-scrollbar-thumb:hover {{ background: var(--color-btn); }}
        ::selection {{ background: var(--color-btn); color: var(--color-text); }}

        @media print {{
            body {{ font-size: 9.5pt; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
            .document {{ max-width: none; padding: 0; }}
            a {{ text-decoration: none; color: inherit; }}
            table {{ page-break-inside: avoid; }}
            tr {{ page-break-inside: avoid; }}
        }}
    </style>
    <script>
    // Dark mode handling - sync with parent
    (function() {{
        document.addEventListener('DOMContentLoaded', function() {{
            const isDark = localStorage.getItem('darkMode') !== 'false';
            if (!isDark) document.body.classList.add('light-mode');
        }});
        
        window.addEventListener('message', function(e) {{
            if (e.data && e.data.type === 'darkModeChange') {{
                document.body.classList.toggle('light-mode', !e.data.enabled);
                localStorage.setItem('darkMode', e.data.enabled);
            }}
        }});
    }})();
    </script>
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


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Convert glossary markdown to HTML format'
    )
    parser.add_argument(
        'input',
        nargs='?',
        default='../text/glossary.md',
        help='Input markdown file (default: glossary.md)'
    )
    parser.add_argument(
        'output',
        nargs='?',
        default='./html/glossary.html',
        help='Output HTML file (default: glossary.html)'
    )
    parser.add_argument(
        '--use-library',
        action='store_true',
        help='Use markdown library if available (recommended)'
    )
    
    args = parser.parse_args()
    
    # Check if input file exists
    if not Path(args.input).exists():
        print(f"Error: Input file '{args.input}' not found.")
        sys.exit(1)
    
    # Try library conversion first if requested
    if args.use_library:
        if convert_with_markdown_library(args.input, args.output):
            return
        else:
            print("Markdown library not available, falling back to basic parser...")
    
    # Use basic converter
    converter = GlossaryConverter(args.input, args.output)
    converter.convert()
    converter.write_html()


if __name__ == '__main__':
    main()
