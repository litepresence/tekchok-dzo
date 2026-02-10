import os
import re

# Directories
commentary_dir = 'volume_1/commentary'
tibetan_dir = 'volume_1/tibetan'

# Make sure both directories exist
if not os.path.isdir(commentary_dir):
    print(f"Error: Directory '{commentary_dir}' not found.")
    exit(1)

if not os.path.isdir(tibetan_dir):
    print(f"Error: Directory '{tibetan_dir}' not found.")
    exit(1)

# Find all PAGE_*.txt files in commentary
commentary_files = [
    f for f in os.listdir(commentary_dir)
    if f.startswith('PAGE_') and f.endswith('.txt')
]

if not commentary_files:
    print(f"No PAGE_*.txt files found in '{commentary_dir}'.")
    exit(0)

processed = 0
modified = 0

for filename in sorted(commentary_files):
    comm_path = os.path.join(commentary_dir, filename)
    tib_path = os.path.join(tibetan_dir, filename)

    if not os.path.exists(tib_path):
        print(f"  Skipping {filename} — no matching file in tibetan/")
        continue

    # ───────────────────────────────────────────────
    # Read commentary file
    # ───────────────────────────────────────────────
    try:
        with open(comm_path, 'r', encoding='utf-8') as f:
            comm_lines = f.readlines()
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        continue

    # Check if commentary already has any line starting with [number]
    has_number = False
    for line in comm_lines:
        if re.match(r'^.*\[\s*[\d\s\-]+\s*\].*', line):
            has_number = True
            break

    if has_number:
        # Already has numbers → skip
        continue

    # ───────────────────────────────────────────────
    # Read tibetan file and find first number
    # ───────────────────────────────────────────────
    try:
        with open(tib_path, 'r', encoding='utf-8') as f:
            tib_lines = f.readlines()
    except Exception as e:
        print(f"Error reading tibetan file for {filename}: {e}")
        continue

    first_number = None
    for line in tib_lines:
        match = re.match(r'^\s*\[\s*(\d+)\s*\]', line)
        if match:
            first_number = int(match.group(1))
            break

    if first_number is None:
        print(f"  No number found in tibetan file for {filename} → skipping")
        continue

    # ───────────────────────────────────────────────
    # Modify commentary file: insert number at the top
    # ───────────────────────────────────────────────
    new_lines = [f"[{first_number}]\n"] + comm_lines

    try:
        with open(comm_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        
        modified += 1
        print(f"  Modified {filename}: added [{first_number}] at top (no numbers were present)")
    
    except Exception as e:
        print(f"Error writing to {filename}: {e}")
        continue

    processed += 1

print(f"\nDone.")
print(f"Processed {processed} files total.")
print(f"Modified {modified} commentary files by adding a top number.")
