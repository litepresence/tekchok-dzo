import os

# Directory to process
directory = 'volume_2/commentary'

# Make sure the directory exists
if not os.path.isdir(directory):
    print(f"Error: Directory '{directory}' not found.")
    exit(1)

# Get all PAGE_*.txt files
files = [f for f in os.listdir(directory) 
         if f.startswith('PAGE_') and f.endswith('.txt')]

if not files:
    print(f"No PAGE_*.txt files found in '{directory}'.")
    exit(0)

processed_count = 0

for filename in files:
    filepath = os.path.join(directory, filename)
    
    try:
        # Read original content
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Filter out lines containing "Rinpoche"
        cleaned_lines = [line for line in lines if 'Rinpoche' not in line]
        
        # Write back only if something was removed (or always, to be safe)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(cleaned_lines)
        
        removed = len(lines) - len(cleaned_lines)
        print(f"Processed {filename}: removed {removed} line(s) containing 'Rinpoche'")
        processed_count += 1
    
    except Exception as e:
        print(f"Error processing {filename}: {e}")

print(f"\nDone. Processed {processed_count} file(s) in '{directory}'.")
