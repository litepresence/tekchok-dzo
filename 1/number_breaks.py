def number_double_line_breaks(input_file, output_file):
    with open(input_file, 'r') as file:
        content = file.read()
    
    # Split the content by double line breaks
    sections = content.split('\n\n')
    
    # Create numbered output
    numbered_sections = []
    for i, section in enumerate(sections):
        # Strip leading/trailing white space and add the number
        numbered_sections.append(f"### SECTION {i + 1}\n\n{section.strip()}")
    
    # Join the sections back with double line breaks
    output_content = '\n\n'.join(numbered_sections)
    
    # Write to the output file
    with open(output_file, 'w') as file:
        file.write(output_content)

# Usage example
input_filename = '2.txt'  # Specify your input file name
output_filename = '2_numbered.txt'  # Specify your output file name
number_double_line_breaks(input_filename, output_filename)
