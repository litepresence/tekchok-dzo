#!/usr/bin/env python3
"""
Fix misclassified VERSE entries in meter layer.
Reclassifies entries with inconsistent or very short syllable counts.
"""

import re
from pathlib import Path


def count_syllables(tibetan_text):
    """Count syllables in Tibetan text."""
    syllables = tibetan_text.replace('།', '་').split('་')
    return len([s for s in syllables if s.strip()])


def analyze_segment(lines_data):
    """Analyze a segment and determine if it's really verse."""
    if not lines_data:
        return None, []
    
    # Get syllable counts
    syllable_counts = []
    for line_num, text in lines_data:
        count = count_syllables(text)
        syllable_counts.append((line_num, count, text))
    
    if not syllable_counts:
        return None, []
    
    # Check if it's verse-worthy
    counts = [c for _, c, _ in syllable_counts]
    avg_count = sum(counts) / len(counts)
    min_count = min(counts)
    max_count = max(counts)
    count_variance = max_count - min_count
    
    # Criteria for VERSE:
    # 1. Average syllables >= 5
    # 2. Variance <= 5 (consistent meter)
    # 3. More than 1 line
    is_verse = (
        avg_count >= 5 and
        count_variance <= 5 and
        len(counts) > 1
    )
    
    if is_verse:
        return 'VERSE', syllable_counts
    
    # Determine what it actually is
    if avg_count < 5:
        # Very short - likely transitional or definitional
        # Check content for clues
        sample_text = ' '.join([text for _, _, text in syllable_counts[:3]])
        
        if any(marker in sample_text for marker in ['དང་པོ', 'གཉིས་པ', 'གསུམ་པ']):
            return 'PROSE_TRANSITIONAL', syllable_counts
        elif len(counts) == 1 and counts[0] <= 3:
            return 'ORNAMENTAL', syllable_counts
        else:
            return 'PROSE', syllable_counts
    else:
        # Inconsistent meter but substantial content
        return 'PROSE', syllable_counts


def fix_meter_file(meter_file, tibetan_dir):
    """Fix misclassifications in a meter file."""
    section_id = meter_file.stem
    
    # Read meter file
    with open(meter_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Read corresponding Tibetan
    tibetan_file = tibetan_dir / f"{section_id}.txt"
    if not tibetan_file.exists():
        return None, 0
    
    with open(tibetan_file, 'r', encoding='utf-8') as f:
        tibetan_content = f.read()
    
    # Build Tibetan lookup
    tibetan_lines = {}
    for line in tibetan_content.split('\n'):
        match = re.match(r'\[(\d+)\]\s*(.*)', line)
        if match:
            line_num = int(match.group(1))
            text = match.group(2)
            tibetan_lines[line_num] = text
    
    # Parse current meter entries
    entries = re.findall(
        r'\[(\d+)-(\d+)\]\s*\[(\w+)\]\n([^-][^\n]*(?:\n-[^\n]+)*)',
        content
    )
    
    fixed_entries = []
    changes_made = 0
    
    for start_str, end_str, seg_type, notes in entries:
        start = int(start_str)
        end = int(end_str)
        
        # If it's VERSE, verify it
        if seg_type == 'VERSE':
            # Get the actual lines
            lines_data = []
            for line_num in range(start, end + 1):
                if line_num in tibetan_lines:
                    lines_data.append((line_num, tibetan_lines[line_num]))
            
            actual_type, syllable_data = analyze_segment(lines_data)
            
            if actual_type and actual_type != 'VERSE':
                # Reclassify
                changes_made += 1
                
                # Generate new notes based on actual type
                if actual_type == 'ORNAMENTAL':
                    new_notes = "- Type: Section marker\n- Elements: Structural enumeration"
                elif actual_type == 'PROSE_TRANSITIONAL':
                    new_notes = "- Type: Transitional/structural\n- Style: Section enumeration\n- Structure: Brief marker"
                else:  # PROSE
                    # Analyze prose style
                    sample = ' '.join([text for _, text in lines_data[:3]])
                    if any(term in sample for term in ['བསྒོམ', 'སྒྲུབ']):
                        new_notes = "- Type: Instructional/methodological\n- Style: Practice guidance\n- Structure: Expository"
                    elif any(term in sample for term in ['ལྟ་བ', 'རང་བཞིན']):
                        new_notes = "- Type: Doctrinal exposition\n- Style: Philosophical analysis\n- Structure: Extended discussion"
                    else:
                        new_notes = "- Type: Doctrinal exposition\n- Style: Expository prose\n- Structure: Moderate exposition"
                
                # Determine final type label
                if actual_type == 'PROSE_TRANSITIONAL':
                    final_type = 'PROSE'
                else:
                    final_type = actual_type
                
                fixed_entries.append({
                    'start': start,
                    'end': end,
                    'type': final_type,
                    'notes': new_notes,
                    'changed': True
                })
            else:
                # Keep original VERSE but maybe improve notes
                fixed_entries.append({
                    'start': start,
                    'end': end,
                    'type': 'VERSE',
                    'notes': notes.strip(),
                    'changed': False
                })
        else:
            # Keep non-VERSE entries as-is
            fixed_entries.append({
                'start': start,
                'end': end,
                'type': seg_type,
                'notes': notes.strip(),
                'changed': False
            })
    
    # Write fixed content
    output_lines = []
    for entry in fixed_entries:
        output_lines.append(f"[{entry['start']:03d}-{entry['end']:03d}] [{entry['type']}]")
        output_lines.append(entry['notes'])
        output_lines.append('')
        output_lines.append('---')
        output_lines.append('')
    
    new_content = '\n'.join(output_lines)
    
    return new_content, changes_made


def main():
    base_dir = Path("/home/opencode/MDZOD/1")
    meter_dir = base_dir / "text" / "meter"
    tibetan_dir = base_dir / "text" / "tibetan"
    
    print("Fixing VERSE classifications...")
    print("="*60)
    
    total_changes = 0
    files_changed = []
    
    for meter_file in sorted(meter_dir.glob("*.txt")):
        new_content, changes = fix_meter_file(meter_file, tibetan_dir)
        
        if new_content is not None and changes > 0:
            # Write fixed content
            with open(meter_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            total_changes += changes
            files_changed.append((meter_file.name, changes))
            print(f"Fixed {meter_file.name}: {changes} reclassifications")
    
    print()
    print("="*60)
    print(f"Total: {total_changes} VERSE entries reclassified in {len(files_changed)} files")
    
    if files_changed:
        print("\nFiles modified:")
        for fname, count in files_changed[:10]:
            print(f"  {fname}: {count} changes")
        if len(files_changed) > 10:
            print(f"  ... and {len(files_changed) - 10} more files")


if __name__ == "__main__":
    main()
