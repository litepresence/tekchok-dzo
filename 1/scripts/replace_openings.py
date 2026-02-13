#!/usr/bin/env python3
"""
SURGICAL OPENING REPLACEMENT
Replace overused openings with alternatives
Track per-chapter quotas
"""

import os
import re
from collections import defaultdict

commentary_dir = "/home/opencode/MDZOD/1/text/commentary"

# Quotas per chapter
QUOTAS = {
    "therefore_thus": 2,  # 2 per chapter
    "three_words": 2,     # 2 per chapter max
    "cut_through": 1,     # 1 per chapter  
    "this_old": 2,        # 2 per chapter with variety
}

# Alternatives pools
ALTERNATIVES = {
    "therefore_thus": [
        "Thus. We proceed...",
        "Accordingly. The analysis...",
        "In this manner...",
        "Hence. The structure...",
        "Consequently...",
        "Thus established...",
        "The framework reveals...",
        "Analysis proceeds...",
    ],
    "three_words": [
        "See what is.",
        "Look. It is here.",
        "Recognize immediately.",
        "See your own face.",
        "Stop searching. Start seeing.",
        "Recognition is immediate.",
        "What knows these words?",
        "Wake up. Now.",
    ],
    "cut_through": [
        "Cut through.",
        "Liberate NOW.",
        "Sever immediately.",
        "Slash through hesitation.",
        "Break through.",
        "Cut!",
        "Liberate!",
        "Sever!",
    ],
    "this_old": [
        "This old man once...",
        "This wanderer...",
        "This hermit...",
        "This yogi...",
        "A practitioner...",
        "An old vagabond...",
        "This mountain dweller...",
        "This fool...",
        "A simple monk...",
        "This old yogi...",
        "A wandering fool...",
        "This mountain hermit...",
        "An old traveler...",
        "This cave dweller...",
        "A humble practitioner...",
    ],
}

def get_chapter(filename):
    """Extract chapter number from filename"""
    match = re.match(r'01-(\d+)-', filename)
    if match:
        return match.group(1)
    return "00"

def replace_overused_openings():
    """Replace overused openings with alternatives"""
    chapter_counts = defaultdict(lambda: defaultdict(int))
    replacements_made = defaultdict(int)
    
    print("SURGICAL OPENING REPLACEMENT")
    print("=" * 60)
    
    for filename in sorted(os.listdir(commentary_dir)):
        if not (filename.startswith("01-") and filename.endswith(".txt")):
            continue
            
        chapter = get_chapter(filename)
        filepath = os.path.join(commentary_dir, filename)
        
        with open(filepath, 'r') as f:
            content = f.read()
        
        lines = content.split('\n')
        new_lines = []
        
        for line in lines:
            line_stripped = line.strip()
            replaced = False
            
            # Check each pattern
            for pattern_name, quota in QUOTAS.items():
                # Define regex for this pattern
                if pattern_name == "therefore_thus":
                    match = re.match(r"^(Therefore\. Thus[^\n]*)", line_stripped, re.IGNORECASE)
                elif pattern_name == "three_words":
                    match = re.match(r"^(Three words[^\n]*)", line_stripped, re.IGNORECASE)
                elif pattern_name == "cut_through":
                    match = re.match(r"^(CUT THROUGH[^\n]*)", line_stripped, re.IGNORECASE)
                elif pattern_name == "this_old":
                    match = re.match(r"^(This old (practitioner|fool)[^\n]*)", line_stripped, re.IGNORECASE)
                else:
                    match = None
                
                if match:
                    chapter_counts[chapter][pattern_name] += 1
                    
                    if chapter_counts[chapter][pattern_name] > quota:
                        # Over quota - replace with alternative
                        alt_pool = ALTERNATIVES.get(pattern_name, [])
                        if alt_pool:
                            # Use deterministic selection based on count
                            alt_index = (chapter_counts[chapter][pattern_name] - quota - 1) % len(alt_pool)
                            replacement = alt_pool[alt_index]
                            
                            # Preserve the rest of the line after the pattern
                            full_match = match.group(1)
                            remainder = line_stripped[len(full_match):]
                            new_line = replacement + remainder
                            
                            new_lines.append(new_line)
                            replacements_made[f"{filename}:{pattern_name}"] += 1
                            replaced = True
                            break
            
            if not replaced:
                new_lines.append(line)
        
        # Write back
        with open(filepath, 'w') as f:
            f.write('\n'.join(new_lines))
    
    # Report
    print("Replacements made:")
    for key, count in sorted(replacements_made.items()):
        print(f"  {key}: {count}")
    
    print("=" * 60)
    print(f"Total replacements: {sum(replacements_made.values())}")

if __name__ == "__main__":
    replace_overused_openings()
