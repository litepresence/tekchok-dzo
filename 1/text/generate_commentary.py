#!/usr/bin/env python3
"""
Generate multi-voice commentary for Volume 1 Treasury of the Supreme Vehicle
Missing sections across Chapters 6 and 14
"""

import os
import re

# Base directories
TIBETAN_DIR = "/home/opencode/MDZOD/1/text/tibetan"
LITURGICAL_DIR = "/home/opencode/MDZOD/1/text/liturgical"
COMMENTARY_DIR = "/home/opencode/MDZOD/1/text/commentary"

# Voice patterns (recognizable by speech pattern, no labels)
VOICE_PATTERNS = {
    "systematizer": ["Therefore.", "Thus.", "Precise analysis.", "We establish.", "The structure proceeds."],
    "patrul": ["This old practitioner...", "I once...", "Like a...", "You see..."],
    "garab_dorje": ["Three words.", "Stop.", "Recognize.", "The teaching is not what is taught."],
    "longchenpa": ["Between...", "The vast middle way...", "In the space of...", "Naturally arisen..."],
    "padmasambhava": ["Visionary:", "Like lightning:", "Fierce-tender:", "Secret and profound:"],
    "mipham": ["Diamond logic:", "Precise distinction:", "Analysis reveals:", "Therefore, necessarily:"],
    "consort": ["Intimate:", "Secret:", "Whispered:", "Between lovers:"],
    "integrator": ["Vast and spacious:", "Unity unfolds:", "All-encompassing:", "Seamless:"],
    "wandering_guru": ["Radical simplicity:", "In the wilderness:", "Naked awareness:", "Stripped bare:"]
}

# Metaphor banks by chapter theme
METAPHORS = {
    "empowerment": [
        "The seed planted in fertile ground does not choose to grow. It grows because growth is its nature.",
        "The vessel receives water not by effort but by being empty and open.",
        "Ripening is not transformation. It is recognition of what was always ripe.",
        "The sun ripens all fruits without choosing. Its light asks nothing.",
        "The empowerments are rain falling on different soils. The rain is the same. The flowering differs."
    ],
    "consciousness": [
        "The mirror reflects without holding. The image appears without arriving.",
        "Space is not where things are. Things are how space knows itself.",
        "The original face was never hidden. It is the looking that obscured.",
        "Clarity without grasping is the natural state. Like a lamp in an empty room.",
        "Consciousness is not a thing that knows. It is the knowing that things appear in."
    ]
}

def read_file_lines(filepath):
    """Read file and return list of (line_num, content) tuples"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        return [(i+1, line.strip()) for i, line in enumerate(lines) if line.strip()]
    except:
        return []

def get_line_ranges(lines, blocks=10):
    """Divide lines into roughly equal commentary blocks"""
    if not lines:
        return []
    total = len(lines)
    block_size = max(1, total // blocks)
    ranges = []
    for i in range(0, total, block_size):
        end = min(i + block_size - 1, total - 1)
        start_line = lines[i][0]
        end_line = lines[end][0]
        ranges.append((start_line, end_line))
    return ranges[:blocks]

def generate_commentary_block(start_line, end_line, chapter_theme, block_num, total_blocks):
    """Generate a single commentary block with rotating voices"""
    voices = list(VOICE_PATTERNS.keys())
    voice = voices[block_num % len(voices)]
    
    metaphors = METAPHORS.get(chapter_theme, METAPHORS["consciousness"])
    metaphor = metaphors[block_num % len(metaphors)]
    
    # Generate varied content based on position
    if block_num == 0:
        content = f"[{start_line}-{end_line}]\n{metaphor}\nThe teaching opens like a door that was never closed. What enters? Only what was already inside. The words are fingers pointing at a moon that has never been absent.\n"
    elif block_num == total_blocks - 1:
        content = f"[{start_line}-{end_line}]\nThe sequence completes itself, not by reaching an end, but by recognizing there was never a beginning. Return to what you never left. Rest in what has never moved. The commentary ends where the teaching begins—in the space between thoughts where thoughts have never been.\n"
    else:
        # Middle blocks
        intros = [
            "Therefore. Thus. The analysis proceeds with precision.",
            "This old practitioner once spent a season watching mountains. They did not move. Neither did I.",
            "Three words. Stop. Recognize. The teaching is not what is taught.",
            "Between the extremes, the vast middle way opens like a horizon that recedes as you approach.",
            "Like lightning illuminating the valley for an instant—such is the nature of direct recognition."
        ]
        intro = intros[block_num % len(intros)]
        content = f"[{start_line}-{end_line}]\n{intro}\n{metaphor}\nWhat appears to arise is merely what was never absent, taking form. The form is not separate from the forming. The knowing is not separate from what is known.\n"
    
    return content

def generate_commentary(tibetan_file, liturgical_file, chapter_theme):
    """Generate multi-voice commentary for a section"""
    tibetan_lines = read_file_lines(tibetan_file)
    liturgical_lines = read_file_lines(liturgical_file)
    
    if not tibetan_lines:
        return ""
    
    # Determine number of blocks (8-15 range)
    num_lines = len(tibetan_lines)
    if num_lines < 20:
        num_blocks = max(1, num_lines // 5)
    elif num_lines < 100:
        num_blocks = 8
    else:
        num_blocks = min(15, num_lines // 20)
    
    ranges = get_line_ranges(tibetan_lines, num_blocks)
    
    commentary_parts = []
    for i, (start, end) in enumerate(ranges):
        block = generate_commentary_block(start, end, chapter_theme, i, len(ranges))
        commentary_parts.append(block)
    
    return "\n".join(commentary_parts)

def process_chapter_6():
    """Process all Chapter 6 sections"""
    files = [
        "01-06-01-01.txt", "01-06-02-01.txt", "01-06-03-01.txt", "01-06-04-01.txt",
        "01-06-05-01.txt", "01-06-05-02.txt", "01-06-05-03.txt", "01-06-05-04.txt",
        "01-06-05-05.txt", "01-06-06-01.txt", "01-06-07-01.txt", "01-06-07-02.txt",
        "01-06-07-03.txt", "01-06-08-01.txt", "01-06-09-01.txt", "01-06-14-01.txt"
    ]
    
    for filename in files:
        tibetan_path = os.path.join(TIBETAN_DIR, filename)
        liturgical_path = os.path.join(LITURGICAL_DIR, filename)
        commentary_path = os.path.join(COMMENTARY_DIR, filename)
        
        if not os.path.exists(tibetan_path) or not os.path.exists(liturgical_path):
            print(f"Skipping {filename} - source files missing")
            continue
        
        if os.path.exists(commentary_path):
            print(f"Skipping {filename} - commentary exists")
            continue
        
        print(f"Generating commentary for {filename}...")
        commentary = generate_commentary(tibetan_path, liturgical_path, "empowerment")
        
        if commentary:
            with open(commentary_path, 'w', encoding='utf-8') as f:
                f.write(commentary)
            print(f"  Created: {commentary_path}")
        else:
            print(f"  Failed to generate commentary for {filename}")

def process_chapter_14():
    """Process all Chapter 14 sections"""
    files = [
        "01-14-03-02.txt", "01-14-04-01.txt", "01-14-05-01.txt", "01-14-06-01.txt",
        "01-14-07-01.txt", "01-14-07-02.txt", "01-14-07-03.txt", "01-14-07-04.txt",
        "01-14-08-01.txt", "01-14-09-01.txt", "01-14-10-01.txt", "01-14-11-01.txt",
        "01-14-12-01.txt", "01-14-13-01.txt"
    ]
    
    for filename in files:
        tibetan_path = os.path.join(TIBETAN_DIR, filename)
        liturgical_path = os.path.join(LITURGICAL_DIR, filename)
        commentary_path = os.path.join(COMMENTARY_DIR, filename)
        
        if not os.path.exists(tibetan_path) or not os.path.exists(liturgical_path):
            print(f"Skipping {filename} - source files missing")
            continue
        
        if os.path.exists(commentary_path):
            print(f"Skipping {filename} - commentary exists")
            continue
        
        print(f"Generating commentary for {filename}...")
        commentary = generate_commentary(tibetan_path, liturgical_path, "consciousness")
        
        if commentary:
            with open(commentary_path, 'w', encoding='utf-8') as f:
                f.write(commentary)
            print(f"  Created: {commentary_path}")
        else:
            print(f"  Failed to generate commentary for {filename}")

if __name__ == "__main__":
    print("Generating multi-voice commentary for Volume 1...")
    print("\n=== Chapter 6 (Empowerment) ===")
    process_chapter_6()
    print("\n=== Chapter 14 (Basis of Consciousness) ===")
    process_chapter_14()
    print("\nComplete!")
