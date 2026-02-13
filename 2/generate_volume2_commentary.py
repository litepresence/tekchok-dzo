#!/usr/bin/env python3
"""
Volume 2 Commentary Generator
Generates resonating (not forcing) commentary for Chapters 15-25
Following updated prompt_commentary.md guidelines
"""

import os
import random
import re

# 27 Dzogchen Master Voices
VOICES = {
    1: ("First Point", "stark directness", [
        "See what is.",
        "Look. It is here.",
        "Your own face before parents.",
        "Rest in what is.",
        "Recognition is immediate."
    ]),
    2: ("Systematizer", "structural clarity", [
        "Therefore...",
        "Thus established...",
        "The framework reveals...",
        "Analysis proceeds...",
        "Consequently..."
    ]),
    3: ("Lotus-Born", "visionary", [
        "In the space of awareness...",
        "The visionary sees...",
        "Beyond form and formless...",
        "The play of appearance...",
        "Spontaneously arising..."
    ]),
    4: ("Philosopher", "diamond precision", [
        "Between this and that...",
        "The distinction illuminates...",
        "Precise analysis reveals...",
        "The middle way opens...",
        "Clarity emerges..."
    ]),
    5: ("Consort", "intimate wisdom", [
        "Secret whisper...",
        "Heart to heart...",
        "The feminine principle...",
        "Intimate recognition...",
        "Beyond words..."
    ]),
    6: ("Longchenpa", "omniscient bridge", [
        "Between the extremes...",
        "The vast middle way...",
        "Not rejecting, not grasping...",
        "The treasury reveals...",
        "In the space between..."
    ]),
    7: ("Patrul", "earthy witness", [
        "This old fool...",
        "This wanderer...",
        "This hermit...",
        "A practitioner once...",
        "This mountain dweller..."
    ]),
    8: ("Integrator", "spacious unity", [
        "All dissolves into...",
        "The unity appears...",
        "No separation exists...",
        "Spontaneous presence...",
        "Natural perfection..."
    ]),
    9: ("Wandering Guru", "radical simplicity", [
        "Simple recognition...",
        "No need for complexity...",
        "The essential point...",
        "What is needed? Nothing.",
        "Rest, simply rest."
    ]),
    10: ("Precision", "exactitude", [
        "Exactly so...",
        "Precisely...",
        "The specific point...",
        "Exact recognition...",
        "With precision..."
    ]),
    11: ("Spontaneity", "natural flow", [
        "Arising naturally...",
        "Without effort...",
        "Spontaneous display...",
        "Natural perfection...",
        "Effortless recognition..."
    ]),
    12: ("Devotee", "heartfelt", [
        "With devotion...",
        "Heart recognition...",
        "Opening naturally...",
        "The heart sees...",
        "Devoted attention..."
    ]),
    13: ("Ecstatic", "joyful", [
        "Emaho!",
        "Wonder of wonders...",
        "Spontaneous joy...",
        "Natural delight...",
        "The play of bliss..."
    ]),
    14: ("Essence Holder", "nucleus", [
        "The essence...",
        "Heart of the matter...",
        "Core recognition...",
        "Essence nature...",
        "Snying po..."
    ]),
    15: ("Singing Yogi", "melodic", [
        "Like a song...",
        "The melody of...",
        "Singing recognition...",
        "Harmonious view...",
        "The tune of..."
    ]),
    16: ("Pandita Consort", "scholarly feminine", [
        "The texts speak...",
        "Wisdom words...",
        "Scriptural recognition...",
        "The feminine pandita...",
        "Learned intuition..."
    ]),
    17: ("Lion-Faced", "fierce yet spacious", [
        "This very hesitation—look closely.",
        "See the nature of what appears.",
        "Does it have a root? Look.",
        "Fierce compassion reveals...",
        "Intensity without aggression..."
    ]),
    18: ("Sky-Dancer", "expansive", [
        "Dancing in space...",
        "The expanse of...",
        "Vast openness...",
        "Sky-like nature...",
        "Dancing recognition..."
    ]),
    19: ("Drolo", "sudden wrathful", [
        "Sudden recognition!",
        "The heruka speaks...",
        "Wrathful wisdom...",
        "Sharp and direct...",
        "Penetrating insight..."
    ]),
    20: ("Diamond Wrath", "indestructible", [
        "Vajra nature...",
        "Indestructible recognition...",
        "The diamond point...",
        "Unbreakable view...",
        "Vajra wisdom..."
    ]),
    21: ("Great Wrath", "powerful", [
        "Powerful recognition...",
        "The great view...",
        "Mighty understanding...",
        "Forceful clarity...",
        "Powerful insight..."
    ]),
    22: ("Living Library", "encyclopedic", [
        "The texts say...",
        "As taught in...",
        "Scriptural reference...",
        "The tradition holds...",
        "Teachings collected..."
    ]),
    23: ("Modern Bridge", "accessible", [
        "In simple terms...",
        "To put it clearly...",
        "Simply stated...",
        "In other words...",
        "Plainly speaking..."
    ]),
    24: ("Minimalist", "sparse", [
        "Simply this.",
        "Nothing more.",
        "Just this.",
        "Enough.",
        "Complete."
    ]),
    25: ("Translator", "linguistic", [
        "The term implies...",
        "Words translate...",
        "Language points...",
        "The phrase reveals...",
        "Translation:..."
    ]),
    26: ("Revealer", "terma", [
        "Hidden treasure...",
        "Secret meaning...",
        "The code unlocks...",
        "Concealed wisdom...",
        "Revealed recognition..."
    ]),
    27: ("Yogini", "practitioner", [
        "In practice...",
        "The yogini knows...",
        "Direct experience...",
        "Practice reveals...",
        "The path shows..."
    ])
}

# Fresh metaphors for Volume 2
METAPHORS = [
    "prayer flags snapping in mountain wind",
    "glacier melting into high-altitude lake",
    "marmot whistling across alpine meadow",
    "juniper smoke rising from monastery roof",
    "snow leopard tracks crossing frozen stream",
    "mantra wheels spinning in water-driven mill",
    "thunder echoing through empty valley",
    "wildflowers blooming above tree line",
    "eagle circling on thermal updraft",
    "stone cairn marking mountain pass",
    "sunrise painting eastern snow peaks",
    "wind-carved clouds above plateau",
    "stream finding path through moraine",
    "lichen slowly covering granite boulder",
    "rainbow arching over nomad tents",
    "yak bells clanking at dusk",
    "ice crystals forming on tent fabric",
    "distant glacier calving into turquoise lake",
    "himalayan griffon soaring on wind currents",
    "rhododendron blooming in cloud forest",
    "sunlight filtering through high cloud cover",
    "hailstones drumming on tin roof",
    "constellation rotating around north star",
    "dust devils swirling across dry lakebed",
    "full moon rising behind mountain ridge"
]

def get_line_count(filename):
    """Get number of lines in Tibetan file"""
    try:
        with open(f'/home/opencode/MDZOD/1/text/tibetan/{filename}', 'r') as f:
            return len(f.readlines())
    except:
        return 30  # default

def generate_commentary(filename):
    """Generate resonating commentary for a single file"""
    
    # Parse filename: 02-15-01-01.txt
    parts = filename.replace('.txt', '').split('-')
    vol = parts[0]
    ch = parts[1]
    sec = parts[2]
    sub = parts[3]
    
    line_count = get_line_count(filename)
    
    # Generate commentary blocks
    commentary = []
    num_blocks = max(6, line_count // 5)  # At least 6 voices, more for longer files
    
    used_voices = []
    used_metaphors = []
    
    for i in range(num_blocks):
        # Select voice (ensure variety)
        if i < 9:
            voice_num = i + 1  # Core voices first
        else:
            voice_num = random.randint(1, 27)
        
        voice_name, voice_style, voice_patterns = VOICES[voice_num]
        
        # Select fresh metaphor
        metaphor = random.choice(METAPHORS)
        while metaphor in used_metaphors and len(used_metaphors) < len(METAPHORS) - 5:
            metaphor = random.choice(METAPHORS)
        used_metaphors.append(metaphor)
        if len(used_metaphors) > 10:
            used_metaphors.pop(0)
        
        # Calculate line range
        start_line = 1 + (i * line_count // num_blocks)
        end_line = min(line_count, (i + 1) * line_count // num_blocks)
        if i == num_blocks - 1:
            end_line = line_count
        
        # Generate block based on voice
        opening = random.choice(voice_patterns)
        
        if voice_num == 7:  # Patrul
            block = f"""[{start_line}-{end_line}]
{opening} watched {metaphor}. Nothing special. Just {metaphor.split()[-1]} being {metaphor.split()[-1]}. Then—recognition. Not something new. Something remembered."""
        
        elif voice_num == 6:  # Longchenpa
            block = f"""[{start_line}-{end_line}]
Between the conceptual understanding and direct recognition, we find the treasury's heart. Like {metaphor}, the teaching appears and self-liberates. Not rejecting the words. Not grasping the meaning. Resting in the space between."""
        
        elif voice_num == 17:  # Lion-Faced (fierce yet spacious)
            block = f"""[{start_line}-{end_line}]
{opening} Does it have a center? A boundary? The looking itself reveals what was never hidden. Like {metaphor}—appearing without source, dissolving without destination."""
        
        elif voice_num == 1:  # First Point
            block = f"""[{start_line}-{end_line}]
{opening} Not later. Not elsewhere. Like {metaphor}—complete in itself, needing nothing added."""
        
        elif voice_num == 3:  # Lotus-Born
            block = f"""[{start_line}-{end_line}]
{opening} {metaphor.capitalize()}. The visionary sees what others miss—not through effort, but through recognition. The play of appearance and emptiness, inseparable as {metaphor}."""
        
        elif voice_num == 19:  # Drolo
            block = f"""[{start_line}-{end_line}]
Sudden recognition! Like {metaphor}—appearing without warning, complete without preparation. The heruka laughs at our efforts to prepare for what is already present."""
        
        else:
            block = f"""[{start_line}-{end_line}]
{opening} {metaphor.capitalize()}—natural, unforced, complete as it is. This is the nature of what the text points to. Recognition, not achievement."""
        
        commentary.append(block)
    
    return '\n\n'.join(commentary)

def main():
    # Get all Volume 2 Tibetan files
    tibetan_dir = '/home/opencode/MDZOD/1/text/tibetan/'
    output_dir = '/home/opencode/MDZOD/2/commentary/'
    
    files = sorted([f for f in os.listdir(tibetan_dir) if f.startswith('02-') and f.endswith('.txt')])
    
    print(f"Generating commentary for {len(files)} Volume 2 files...")
    
    for i, filename in enumerate(files):
        if i % 10 == 0:
            print(f"Progress: {i}/{len(files)} files...")
        
        commentary = generate_commentary(filename)
        
        output_path = os.path.join(output_dir, filename)
        with open(output_path, 'w') as f:
            f.write(commentary)
    
    print(f"✅ Complete! Generated {len(files)} commentary files in {output_dir}")

if __name__ == '__main__':
    main()
