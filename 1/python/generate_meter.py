#!/usr/bin/env python3
"""
Generate meter analysis layer for all Tibetan sections.
Analyzes text to classify as PROSE, VERSE, ORNAMENTAL, or MANTRA.
Provides traditional Tibetan metrical analysis for verse sections.
"""

import re
from pathlib import Path


def count_syllables(tibetan_line):
    """Count Tibetan syllables in a line.
    Syllables are separated by ་ or །
    """
    # Remove line number prefix
    content = re.sub(r'^\[\d+\]\s*', '', tibetan_line)
    
    # Count syllable markers
    syllables = content.replace('།', '་').split('་')
    # Filter out empty strings
    syllables = [s.strip() for s in syllables if s.strip()]
    return len(syllables)


def analyze_section(section_file):
    """Analyze a Tibetan section and return meter classification."""
    with open(section_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    
    # Extract content lines (with line numbers)
    content_lines = []
    for line in lines:
        match = re.match(r'^(\[(\d+)\])\s*(.*)', line)
        if match:
            line_num = int(match.group(2))
            text = match.group(3)
            content_lines.append((line_num, text))
    
    if not content_lines:
        return []
    
    # Analyze line by line
    segments = []
    current_segment = {
        'type': None,
        'start': content_lines[0][0],
        'end': content_lines[0][0],
        'lines': []
    }
    
    for i, (line_num, text) in enumerate(content_lines):
        # Determine type
        line_type = classify_line(text, line_num)
        
        # If type changes or we're at ornamental, start new segment
        if line_type != current_segment['type'] or line_type == 'ORNAMENTAL':
            if current_segment['lines']:
                segments.append(current_segment)
            current_segment = {
                'type': line_type,
                'start': line_num,
                'end': line_num,
                'lines': [(line_num, text)]
            }
        else:
            current_segment['end'] = line_num
            current_segment['lines'].append((line_num, text))
    
    if current_segment['lines']:
        segments.append(current_segment)
    
    # Analyze each segment
    results = []
    for segment in segments:
        analysis = analyze_segment(segment)
        results.append(analysis)
    
    return results


def classify_line(text, line_num):
    """Classify a single line."""
    stripped = text.strip()
    
    # Check for ornamental markers
    if '༄༅།' in stripped or stripped == '།' or stripped == '།།' or stripped == '།།།':
        return 'ORNAMENTAL'
    
    # Check for mantras (Sanskrit-derived)
    mantra_markers = ['ཨོཾ', 'ཧཱུྃ', 'སྭཱཧཱ', 'ཕཊ']
    for marker in mantra_markers:
        if marker in stripped:
            return 'MANTRA'
    
    # Check for verse markers (ends with shad)
    if stripped.endswith('།'):
        # Could be verse or prose - need syllable analysis
        return 'POTENTIAL_VERSE'
    
    return 'PROSE'


def analyze_segment(segment):
    """Analyze a segment and return detailed classification."""
    seg_type = segment['type']
    start = segment['start']
    end = segment['end']
    lines = segment['lines']
    
    if seg_type == 'ORNAMENTAL':
        return {
            'range': (start, end),
            'type': 'ORNAMENTAL',
            'notes': analyze_ornamental(lines)
        }
    
    elif seg_type == 'MANTRA':
        return {
            'range': (start, end),
            'type': 'MANTRA',
            'notes': analyze_mantra(lines)
        }
    
    elif seg_type == 'POTENTIAL_VERSE':
        # Check if it's actually verse based on syllable patterns
        syllable_counts = []
        for _, text in lines:
            count = count_syllables(f'[{start}] {text}')
            syllable_counts.append(count)
        
        # If syllable counts are consistent, it's verse
        if len(set(syllable_counts)) <= 2 and len(syllable_counts) >= 2:
            return {
                'range': (start, end),
                'type': 'VERSE',
                'notes': analyze_verse(lines, syllable_counts)
            }
        else:
            return {
                'range': (start, end),
                'type': 'PROSE',
                'notes': analyze_prose(lines)
            }
    
    else:  # PROSE
        return {
            'range': (start, end),
            'type': 'PROSE',
            'notes': analyze_prose(lines)
        }


def analyze_ornamental(lines):
    """Analyze ornamental lines."""
    elements = []
    for _, text in lines:
        if '༄༅།' in text:
            elements.append('Triple ornamental shad (༄༅།)')
        elif text.strip() == '།':
            elements.append('Single shad')
        elif text.strip() == '།།':
            elements.append('Double shad')
        elif text.strip() == '།།།':
            elements.append('Triple shad')
    
    unique_elements = list(set(elements))
    
    notes = []
    notes.append(f"- Type: {'Title marker' if '༄༅།' in str(lines) else 'Structural marker'}")
    notes.append(f"- Elements: {', '.join(unique_elements[:3])}")
    
    return '\n'.join(notes)


def analyze_mantra(lines):
    """Analyze mantra lines."""
    mantras_found = []
    for _, text in lines:
        if 'ཨོཾ' in text:
            mantras_found.append('oṃ')
        if 'ཧཱུྃ' in text:
            mantras_found.append('hūṃ')
        if 'སྭཱཧཱ' in text:
            mantras_found.append('svāhā')
        if 'ཕཊ' in text:
            mantras_found.append('phat')
    
    notes = []
    notes.append(f"- Type: {'Seed syllables' if len(mantras_found) <= 2 else 'Dharani'}")
    if mantras_found:
        notes.append(f"- Elements: {', '.join(set(mantras_found))}")
    
    return '\n'.join(notes)


def analyze_verse(lines, syllable_counts):
    """Analyze verse lines for meter."""
    # Determine primary meter type
    avg_syllables = sum(syllable_counts) / len(syllable_counts)
    
    if 8 <= avg_syllables <= 10:
        meter_name = 'Nor Nang (9-syllable)'
        pattern = '9'
    elif 6 <= avg_syllables <= 8:
        meter_name = 'Sang Drel (7-syllable)'
        pattern = '7'
    elif 10 <= avg_syllables <= 12:
        meter_name = 'Chudral (11-syllable)'
        pattern = '11'
    else:
        meter_name = 'Mixed/Unclassified'
        pattern = str(int(avg_syllables))
    
    # Count stanzas (assuming 4-line stanzas)
    num_lines = len(lines)
    stanzas = num_lines // 4
    if num_lines % 4 != 0:
        stanzas += 1
    
    # Determine syllable pattern
    unique_counts = list(set(syllable_counts))
    if len(unique_counts) == 1:
        syllable_pattern = f"{pattern}-{pattern}-{pattern}-{pattern} quatrains"
    else:
        counts_str = '-'.join([str(c) for c in syllable_counts[:4]])
        syllable_pattern = f"{counts_str} (irregular)"
    
    notes = []
    notes.append(f"- Primary meter: {meter_name}")
    notes.append(f"- Syllable pattern: {syllable_pattern}")
    notes.append(f"- Stanzas: {stanzas}")
    notes.append(f"- Rhyme: End-line assonance")
    
    return '\n'.join(notes)


def analyze_prose(lines):
    """Analyze prose lines for type and style."""
    # Sample first few lines to determine type
    sample_text = ' '.join([text for _, text in lines[:5]])
    
    # Determine prose type
    if any(term in sample_text for term in ['ལྟ་བ', 'གྲུབ་མཐའ', 'རང་བཞིན']):
        prose_type = 'Doctrinal exposition'
        style = 'Philosophical argumentation'
    elif any(term in sample_text for term in ['བསྒོམ', 'སྒྲུབ', 'ཉམས']):
        prose_type = 'Instructional/methodological'
        style = 'Practice guidance'
    elif any(term in sample_text for term in ['ལོ་རྒྱུས', 'སྐྱེས་རབས']):
        prose_type = 'Narrative/historical'
        style = 'Biographical account'
    elif re.search(r'\d+\.', sample_text) or 'དང་པོ' in sample_text or 'གཉིས་པ' in sample_text:
        prose_type = 'Definitional/enumerative'
        style = 'Systematic enumeration'
    elif 'དེ་ནས' in sample_text or 'ད་ནི' in sample_text:
        prose_type = 'Transitional/structural'
        style = 'Section transition'
    else:
        prose_type = 'Doctrinal exposition'
        style = 'Expository prose'
    
    # Determine structure
    if len(lines) > 20:
        structure = 'Extended analysis with multiple points'
    elif len(lines) > 10:
        structure = 'Moderate exposition'
    else:
        structure = 'Brief passage'
    
    notes = []
    notes.append(f"- Type: {prose_type}")
    notes.append(f"- Style: {style}")
    notes.append(f"- Structure: {structure}")
    
    return '\n'.join(notes)


def write_meter_file(section_id, analyses, output_dir):
    """Write meter analysis to file."""
    output_path = output_dir / f"{section_id}.txt"
    
    lines = []
    for analysis in analyses:
        start, end = analysis['range']
        seg_type = analysis['type']
        notes = analysis['notes']
        
        lines.append(f"[{start:03d}-{end:03d}] [{seg_type}]")
        lines.append(notes)
        lines.append('')
        lines.append('---')
        lines.append('')
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))


def main():
    base_dir = Path("/home/opencode/MDZOD/1")
    tibetan_dir = base_dir / "text" / "tibetan"
    output_dir = base_dir / "text" / "meter"
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Process all sections
    section_files = sorted(tibetan_dir.glob("*.txt"))
    
    print(f"Processing {len(section_files)} sections...")
    
    for i, section_file in enumerate(section_files):
        section_id = section_file.stem
        
        analyses = analyze_section(section_file)
        
        if analyses:
            write_meter_file(section_id, analyses, output_dir)
        
        if (i + 1) % 50 == 0:
            print(f"Processed {i + 1}/{len(section_files)} sections...")
    
    print(f"\nMeter analysis complete!")
    print(f"Generated {len(section_files)} files in text/meter/")


if __name__ == "__main__":
    main()
