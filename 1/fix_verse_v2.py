#!/usr/bin/env python3
"""
Fix misclassified VERSE entries in meter layer.
"""

import re
from pathlib import Path


def count_syllables(tibetan_text):
    """Count syllables in Tibetan text."""
    syllables = tibetan_text.replace('།', '་').split('་')
    return len([s for s in syllables if s.strip()])


def analyze_lines(lines_data):
    """Analyze lines to determine if they're really verse."""
    if not lines_data:
        return None
    
    counts = [count for _, count in lines_data]
    avg = sum(counts) / len(counts) if counts else 0
    min_c = min(counts) if counts else 0
    max_c = max(counts) if counts else 0
    variance = max_c - min_c
    
    # VERSE criteria: avg >= 5, variance <= 5, more than 1 line
    if avg >= 5 and variance <= 5 and len(counts) > 1:
        return 'VERSE'
    elif avg < 4:
        return 'ORNAMENTAL'
    else:
        return 'PROSE'


def main():
    base_dir = Path("/home/opencode/MDZOD/1")
    meter_dir = base_dir / "text" / "meter"
    tibetan_dir = base_dir / "text" / "tibetan"
    
    print("Checking and fixing VERSE entries...")
    print("="*70)
    
    total_fixed = 0
    
    for meter_file in sorted(meter_dir.glob("*.txt")):
        section_id = meter_file.stem
        
        # Read meter file
        with open(meter_file, 'r', encoding='utf-8') as f:
            meter_content = f.read()
        
        # Read Tibetan
        tibetan_file = tibetan_dir / f"{section_id}.txt"
        if not tibetan_file.exists():
            continue
        
        with open(tibetan_file, 'r', encoding='utf-8') as f:
            tibetan_content = f.read()
        
        # Build Tibetan lookup
        tibetan_lines = {}
        for line in tibetan_content.split('\n'):
            match = re.match(r'\[(\d+)\]\s*(.*)', line)
            if match:
                tibetan_lines[int(match.group(1))] = match.group(2)
        
        # Find VERSE entries
        verse_entries = list(re.finditer(r'\[(\d+)-(\d+)\]\s*\[VERSE\]\n(-.*?)(?=\n---|\Z)', meter_content, re.DOTALL))
        
        if not verse_entries:
            continue
        
        file_changes = 0
        new_content = meter_content
        
        for match in verse_entries:
            start = int(match.group(1))
            end = int(match.group(2))
            old_notes = match.group(3).strip()
            
            # Get actual Tibetan lines
            lines_data = []
            for line_num in range(start, end + 1):
                if line_num in tibetan_lines:
                    text = tibetan_lines[line_num]
                    count = count_syllables(text)
                    lines_data.append((line_num, count, text))
            
            if not lines_data:
                continue
            
            # Analyze
            counts = [c for _, c, _ in lines_data]
            avg = sum(counts) / len(counts)
            variance = max(counts) - min(counts) if len(counts) > 1 else 0
            
            # Check if it's really verse
            is_valid_verse = (avg >= 5 and variance <= 5 and len(counts) > 1)
            
            if not is_valid_verse:
                # Need to reclassify
                if avg < 4:
                    new_type = 'ORNAMENTAL'
                    new_notes = "- Type: Structural marker\n- Elements: Section enumeration or brief notation"
                else:
                    new_type = 'PROSE'
                    # Sample text for prose analysis
                    sample = ' '.join([t for _, _, t in lines_data[:3]])
                    if any(x in sample for x in ['དང་པོ', 'གཉིས་པ', 'གསུམ་པ']):
                        new_notes = "- Type: Transitional/structural\n- Style: Section enumeration\n- Structure: Organizational marker"
                    else:
                        new_notes = "- Type: Doctrinal exposition\n- Style: Expository prose\n- Structure: Extended discussion"
                
                # Replace in content
                old_text = match.group(0)
                new_text = f"[{start:03d}-{end:03d}] [{new_type}]\n{new_notes}\n\n---"
                
                new_content = new_content.replace(old_text, new_text)
                file_changes += 1
                total_fixed += 1
                
                if file_changes <= 2:  # Show first 2 changes per file
                    print(f"\n{section_id}: [{start}-{end}]")
                    print(f"  Reclassified: VERSE -> {new_type}")
                    print(f"  Syllables: {counts} (avg: {avg:.1f}, variance: {variance})")
        
        if file_changes > 0:
            # Write updated content
            with open(meter_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
    
    print()
    print("="*70)
    print(f"Total VERSE entries reclassified: {total_fixed}")
    
    # Show final stats
    print("\nFinal VERSE statistics:")
    verse_count = 0
    for meter_file in meter_dir.glob("*.txt"):
        with open(meter_file, 'r') as f:
            verse_count += f.read().count('[VERSE]')
    print(f"  Valid VERSE entries remaining: {verse_count}")


if __name__ == "__main__":
    main()
