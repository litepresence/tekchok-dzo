import os
import re

# Define directories
lit_dir = 'volume_2/liturgical'
tib_dir = 'volume_2/tibetan'
out_dir = 'volume_2/numbered_liturgical'

# Create output directory if it doesn't exist
os.makedirs(out_dir, exist_ok=True)

# Get list of PAGE_*.txt files from liturgical directory
files = [f for f in os.listdir(lit_dir) if f.startswith('PAGE_') and f.endswith('.txt')]

for file in files:
    lit_path = os.path.join(lit_dir, file)
    tib_path = os.path.join(tib_dir, file)
    
    # Skip if corresponding Tibetan file doesn't exist
    if not os.path.exists(tib_path):
        print(f"Warning: Corresponding Tibetan file {tib_path} not found. Skipping {file}.")
        continue
    
    # Read liturgical file
    with open(lit_path, 'r', encoding='utf-8') as f:
        lit_text = f.read()
    
    # Remove double newlines (collapse multiple \n to single \n)
    while '\n\n' in lit_text:
        lit_text = lit_text.replace('\n\n', '\n')
    
    # Split into lines and strip trailing/leading whitespace per line
    lit_lines = [line.strip() for line in lit_text.splitlines() if line.strip()]
    
    # If first line begins with "Page", remove it
    if lit_lines and lit_lines[0].startswith('Page'):
        lit_lines = lit_lines[1:]
    
    # Read Tibetan file
    with open(tib_path, 'r', encoding='utf-8') as f:
        tib_lines = f.readlines()
    
    # Extract first and last number
    def extract_num(line):
        match = re.match(r'\[\s*(\d+)\s*\]', line.strip())
        if match:
            return int(match.group(1))
        return None
    
    first_num = None
    last_num = None
    for line in tib_lines:
        num = extract_num(line)
        if num is not None:
            if first_num is None:
                first_num = num
            last_num = num
    
    if first_num is None or last_num is None:
        print(f"Error in {file}: No numbers found in Tibetan file.")
        continue
    
    # Generate number range
    num_range = list(range(first_num, last_num + 1))
    num_count = len(num_range)
    lit_count = len(lit_lines)
    
    # Build output lines
    output_lines = []
    current_line = ""
    last_numbered_index = -1
    
    for i in range(max(num_count, lit_count)):
        if i < num_count:
            # We have a number → start a new numbered line
            if current_line:
                output_lines.append(current_line)
            num_str = f"[{num_range[i]}]"
            current_line = num_str + " " + (lit_lines[i] if i < lit_count else "")
            last_numbered_index = i
        else:
            # Extra liturgical lines → append to the last numbered line
            if i < lit_count and current_line:
                current_line += "  " + lit_lines[i]
    
    # Don't forget to add the very last line
    if current_line:
        output_lines.append(current_line)
    
    # Write to output file
    out_path = os.path.join(out_dir, file)
    with open(out_path, 'w', encoding='utf-8') as f:
        for line in output_lines:
            f.write(line + '\n')
    
    print(f"Processed {file} → wrote to {out_path}  "
          f"({num_count} numbers, {lit_count} lit lines)")
