#!/usr/bin/env python3
"""
Fix mislabeled PROSE entries in meter layer.
Reclassifies very short lines to ORNAMENTAL and consistent meter to VERSE.
"""

import re
from pathlib import Path


def count_syllables(tibetan_text):
    """Count syllables in Tibetan text."""
    syllables = tibetan_text.replace('།', '་').split('་')
    return len([s for s in syllables if s.strip()])


def analyze_and_reclassify(lines_data):
    """Analyze lines and determine proper classification."""
    if not lines_data:
        return None
    
    counts = [count for _, count, _ in lines_data]
    avg = sum(counts) / len(counts)
    min_c = min(counts)
    max_c = max(counts)
    variance = max_c - min_c
    
    # Check if it should be ORNAMENTAL (very short)
    if avg < 4:
        return 'ORNAMENTAL', "- Type: Structural marker\n- Elements: Brief notation or enumeration marker"
    
    # Check if it should be VERSE (consistent meter, substantial length)
    if len(counts) >= 2 and variance <= 2 and avg >= 5:
        # Determine meter type
        if 6 <= avg <= 8:
            meter = 'Sang Drel (7-syllable)'
            pattern_note = '7'
        elif 8 <= avg <= 10:
            meter = 'Nor Nang (9-syllable)'
            pattern_note = '9'
        elif 10 <= avg <= 12:
            meter = 'Chudral (11-syllable)'
            pattern_note = '11'
        else:
            meter = f'Mixed ({int(avg)}-syllable)'
            pattern_note = str(int(avg))
        
        # Build syllable pattern
        if len(counts) == 4 and variance == 0:
            syllable_pattern = f"{pattern_note}-{pattern_note}-{pattern_note}-{pattern_note} quatrains"
            stanzas = 1
        else:
            pattern_parts = [str(c) for c in counts]
            syllable_pattern = "-".join(pattern_parts)
            stanzas = max(1, len(counts) // 4)
        
        notes = f"- Primary meter: {meter}\n- Syllable pattern: {syllable_pattern}\n- Stanzas: {stanzas}\n- Rhyme: End-line assonance"
        return 'VERSE', notes
    
    # Keep as PROSE
    return None, None


def main():
    base_dir = Path("/home/opencode/MDZOD/1")
    meter_dir = base_dir / "text" / "meter"
    tibetan_dir = base_dir / "text" / "tibetan"
    
    print("Fixing mislabeled PROSE entries...")
    print("="*70)
    
    total_fixed = 0
    ornamental_count = 0
    verse_count = 0
    
    for meter_file in sorted(meter_dir.glob("*.txt")):
        section_id = meter_file.stem
        
        with open(meter_file, 'r') as f:
            meter_content = f.read()
        
        # Read Tibetan
        tibetan_file = tibetan_dir / f"{section_id}.txt"
        if not tibetan_file.exists():
            continue
        
        with open(tibetan_file, 'r') as f:
            tibetan_content = f.read()
        
        # Build lookup
        tibetan_lines = {}
        for line in tibetan_content.split('\n'):
            match = re.match(r'\[(\d+)\]\s*(.*)', line)
            if match:
                tibetan_lines[int(match.group(1))] = match.group(2)
        
        # Find PROSE entries
        changes = []
        for match in re.finditer(r'\[(\d+)-(\d+)\]\s*\[PROSE\]\n((?:-[^\n]*\n)+)', meter_content):
            start = int(match.group(1))
            end = int(match.group(2))
            old_notes = match.group(3).strip()
            
            # Get lines
            lines_data = []
            for line_num in range(start, end + 1):
                if line_num in tibetan_lines:
                    text = tibetan_lines[line_num]
                    count = count_syllables(text)
                    lines_data.append((line_num, count, text))
            
            if not lines_data:
                continue
            
            new_type, new_notes = analyze_and_reclassify(lines_data)
            
            if new_type:
                changes.append({
                    'start': start,
                    'end': end,
                    'old_type': 'PROSE',
                    'new_type': new_type,
                    'new_notes': new_notes,
                    'syllables': [c for _, c, _ in lines_data]
                })
        
        if changes:
            # Apply changes
            new_content = meter_content
            for change in changes:
                old_pattern = f"[{change['start']:03d}-{change['end']:03d}] [PROSE]"
                new_pattern = f"[{change['start']:03d}-{change['end']:03d}] [{change['new_type']}]"
                new_content = new_content.replace(old_pattern, new_pattern)
                
                # Replace notes
                old_notes_start = new_content.find(f"[{change['start']:03d}-{change['end']:03d}] [{change['new_type']}]")
                if old_notes_start >= 0:
                    # Find the notes section
                    line_start = new_content.find('\n', old_notes_start) + 1
                    line_end = new_content.find('\n\n---', line_start)
                    if line_end > line_start:
                        new_content = new_content[:line_start] + change['new_notes'] + '\n' + new_content[line_end:]
                
                total_fixed += 1
                if change['new_type'] == 'ORNAMENTAL':
                    ornamental_count += 1
                else:
                    verse_count += 1
            
            # Write updated content
            with open(meter_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            if changes:
                print(f"\n{section_id}:")
                for change in changes[:3]:  # Show first 3 changes
                    print(f"  [{change['start']}-{change['end']}]: PROSE -> {change['new_type']}")
                    print(f"    Syllables: {change['syllables']}")
    
    print()
    print("="*70)
    print(f"Total PROSE entries reclassified: {total_fixed}")
    print(f"  -> ORNAMENTAL: {ornamental_count}")
    print(f"  -> VERSE: {verse_count}")
    
    # Show final stats
    print("\nFinal meter layer statistics:")
    final_prose = 0
    final_verse = 0
    final_ornamental = 0
    final_mantra = 0
    
    for meter_file in meter_dir.glob("*.txt"):
        with open(meter_file, 'r') as f:
            content = f.read()
        final_prose += content.count('[PROSE]')
        final_verse += content.count('[VERSE]')
        final_ornamental += content.count('[ORNAMENTAL]')
        final_mantra += content.count('[MANTRA]')
    
    print(f"  PROSE: {final_prose}")
    print(f"  VERSE: {final_verse}")
    print(f"  ORNAMENTAL: {final_ornamental}")
    print(f"  MANTRA: {final_mantra}")


if __name__ == "__main__":
    main()
