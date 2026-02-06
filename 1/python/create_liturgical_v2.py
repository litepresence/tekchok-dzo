#!/usr/bin/env python3
"""
Liturgical Translation Script - Enhanced Vairotsana Style
Generates majestic, chantable Dzogchen vajra speech translations
"""

import os
import re

def read_file(filepath):
    """Read a file and return lines."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.readlines()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return []

def parse_line(line):
    """Parse a line to extract line number and content."""
    match = re.match(r'\[(\d+)\]\s*(.*)', line.strip())
    if match:
        return match.group(1), match.group(2)
    return None, line.strip()

def is_verse_line(literal, wylie):
    """Check if this is a verse line (typically starts with / in Tibetan/Wylie)."""
    return wylie.strip().startswith('/') or literal.strip().startswith('/')

def transform_to_liturgical_v2(literal, wylie, tibetan, line_num):
    """
    Transform literal translation to elevated Vairotsana liturgical style.
    Majestic, chantable, transmissive Dzogchen vajra speech.
    """
    lit = literal.strip()
    wyl = wylie.strip()
    tib = tibetan.strip()
    
    # Handle citations and headers
    if 'CITATION' in lit or lit.startswith('###'):
        return lit
    
    # Check if it's a verse line from scripture
    is_verse = is_verse_line(literal, wylie)
    verse_marker = ''
    if is_verse:
        verse_marker = '/'
        lit = lit.lstrip('/').strip()
        wyl = wyl.lstrip('/').strip()
    
    # Handle "zhes so" / "thus is said"
    if 'zhes so' in wyl.lower() or lit.lower() in ['thus', 'thus is', 'thus is-said']:
        return f"{verse_marker}Thus it is proclaimed."
    
    # Handle section headers
    if 'dang po' in wyl and any(x in lit.lower() for x in ['first', 'primordial']):
        if 'la gsum' in wyl or 'three' in lit.lower():
            return f"{verse_marker}Primordial—divided into three aspects of Wisdom abiding in the basis."
        return f"{verse_marker}Primordial."
    
    if 'gnyis pa' in wyl and any(x in lit.lower() for x in ['second', 'two']):
        return f"{verse_marker}Second."
    
    # Major conceptual transformations for majestic speech
    majestic_transforms = {
        # Wisdom categories
        r'\bcharacteristic-hold.*?wisdom\b': 'Wisdom that holds characteristics',
        r'\bobject-pervad.*?wisdom\b': 'Wisdom pervading all objects',
        r'\basis-abid.*?wisdom\b': 'Wisdom abiding in the basis',
        r'\bka-dag.*?wisdom\b': 'Wisdom primordially pure',
        r'\bspontaneous.*?wisdom\b': 'Wisdom spontaneously perfected',
        r'\ball-pervad.*?wisdom\b': 'All-pervading Wisdom of Compassion',
        r'\bmirror.*?wisdom\b': 'Mirror-like Wisdom',
        r'\bequality.*?wisdom\b': 'Wisdom of Equality',
        r'\bdiscriminat.*?wisdom\b': 'Discriminating Wisdom',
        r'\bdharmadhatu.*?wisdom\b': 'Dharmadhatu Wisdom',
        r'\ball-accomplish.*?wisdom\b': 'All-Accomplishing Wisdom',
        
        # Key Dzogchen terms
        r'\bngo bo ka dag\b': 'Essence primordially pure',
        r'\brang bzhin lhun grub\b': 'Nature spontaneously perfected',
        r'\bthugs rje kun khyab\b': 'Compassion all-pervading',
        r'\bchos nyid\b': 'Dharmata',
        r'\brig pa\b': 'Awareness',
        r'\bsku\b': 'Kaya',
        
        # Body/Kaya descriptions
        r'\bvast dharmata.*?body\b': 'Vast Kaya of Dharmata',
        r'\bexpansive space.*?body\b': 'Expansive Kaya of Space',
        r'\broot awareness.*?body\b': 'Root Kaya of Awareness',
        r'\bnon-chang.*?vajra.*?body\b': 'Vajra Kaya of Changelessness',
        r'\bbody thirteen\b': 'Thirteen Kayas',
        
        # Pure/impure distinctions
        r'\bpure non-existence\b': 'Pure through primordial non-existence',
        r'\bnon-awareness non-existent\b': 'Non-awareness is non-existent',
        r'\bmind non-existent\b': 'Mind is non-existent',
        r'\bintellect non-existent\b': 'Intellect is non-existent',
        r'\bgrasping non-existent\b': 'Grasping is non-existent',
        
        # Appearances and emptiness
        r'\bappearance-empty\b': 'Appearance-emptiness',
        r'\bempty appearance\b': 'Empty appearance',
        r'\bclear and empty\b': 'Luminous and empty',
        
        # Buddha/samsara
        r'\bbuddha non-existent\b': 'Buddha is non-existent',
        r'\bsentient-being non-existent\b': 'Sentient beings are non-existent',
        r'\bsamsara non-existent\b': 'Samsara is non-existent',
        
        # Actions
        r'\bself-liberated\b': 'Self-liberated',
        r'\bspontaneously accomplished\b': 'Spontaneously accomplished',
        r'\bself-exhausted\b': 'Self-exhausted',
        r'\bnon-ceased\b': 'Non-ceasing',
        
        # Quotations
        r'\bthal.*?gyur\b': 'From the Thalgyur',
        r'\bmu tig phreng ba\b': 'From the Mu Tig Phreng Ba',
    }
    
    # Apply major transformations
    text_lower = lit.lower()
    result = lit
    
    for pattern, replacement in majestic_transforms.items():
        result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)
    
    # Clean up grammatical artifacts
    cleanup_patterns = [
        (r'\bby-means-of\b', ''),
        (r'\bto\b', ''),
        (r'\bfrom\b', ''),
        (r'\binto\b', ''),
        (r'\bpossessed\b', ''),
        (r'\bpossessing\b', ''),
        (r'\band\s+(?=[a-z]+\s+are\b)', ''),  # Remove redundant 'and' before 'are'
        (r'\s+', ' '),  # Normalize spaces
    ]
    
    for pattern, replacement in cleanup_patterns:
        result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)
    
    # Handle compound words
    result = result.replace('-', ' ')
    result = re.sub(r'\s+', ' ', result).strip()
    
    # Capitalize Dzogchen terms
    sacred_terms = [
        'wisdom', 'dharmata', 'awareness', 'compassion', 'kaya', 'dharmakaya',
        'sambhogakaya', 'nirmanakaya', 'buddha', 'samsara', 'nirvana', 'emptiness',
        'appearance', 'luminous', 'spontaneous', 'perfection', 'pure', 'primordial',
        'vajra', 'vidya', 'kadag', 'lhundrub', 'thugje', 'dzogchen', 'bindu',
        'mandala', 'deity', 'dharma', 'sangha', 'sentient being'
    ]
    
    for term in sacred_terms:
        result = re.sub(r'\b' + term + r'\b', term.title(), result, flags=re.IGNORECASE)
    
    # Final poetic touches
    # Remove trailing prepositions
    result = re.sub(r'\s+(in|at|to|from|by|with|and)$', '', result, flags=re.IGNORECASE)
    
    # Capitalize first letter
    if result:
        result = result[0].upper() + result[1:]
    
    # Add verse marker back if it was a verse
    if is_verse:
        result = verse_marker + result
    
    # Ensure proper punctuation
    if result and not result.endswith(('.', '!', '?', '/', '*')):
        result = result.rstrip('.') + '.'
    
    # Special handling for specific phrases
    if 'three are' in result.lower():
        result = result.replace('three are', 'are three')
    
    # Handle "is said" type endings
    if result.lower().endswith('is said'):
        result = result.replace('is said', 'is proclaimed')
    
    if result.lower().endswith('is called'):
        result = result.replace('is called', 'is known as')
    
    # Final cleanup
    result = re.sub(r'\s+', ' ', result).strip()
    
    return result

def create_liturgical_translation_v2(tibetan_lines, wylie_lines, literal_lines):
    """
    Create liturgical translation with enhanced Vairotsana style.
    """
    liturgical_lines = []
    
    for i, (tib_line, wyl_line, lit_line) in enumerate(zip(tibetan_lines, wylie_lines, literal_lines)):
        line_num, tib_content = parse_line(tib_line)
        _, wyl_content = parse_line(wyl_line)
        _, lit_content = parse_line(lit_line)
        
        if not line_num:
            liturgical_lines.append(tib_line)
            continue
        
        # Transform to liturgical
        liturgical = transform_to_liturgical_v2(lit_content, wyl_content, tib_content, line_num)
        
        liturgical_lines.append(f"[{line_num}] {liturgical}\n")
    
    return liturgical_lines

def process_page(page_num):
    """Process a single page."""
    tibetan_path = f"./tibetan/PAGE {page_num}.txt"
    wylie_path = f"./wylie/PAGE {page_num}.txt"
    literal_path = f"./literal/PAGE {page_num}.txt"
    output_path = f"./liturgical/PAGE {page_num}.txt"
    
    # Read source files
    tibetan_lines = read_file(tibetan_path)
    wylie_lines = read_file(wylie_path)
    literal_lines = read_file(literal_path)
    
    if not all([tibetan_lines, wylie_lines, literal_lines]):
        print(f"Skipping page {page_num} - missing source files")
        return False
    
    # Create liturgical translation
    liturgical_lines = create_liturgical_translation_v2(tibetan_lines, wylie_lines, literal_lines)
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Write output
    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(liturgical_lines)
    
    return True

def main():
    """Process all pages from 434 to 479."""
    success_count = 0
    failed_pages = []
    
    for page_num in range(434, 480):
        if process_page(page_num):
            success_count += 1
            print(f"✓ Page {page_num}")
        else:
            failed_pages.append(page_num)
            print(f"✗ Page {page_num}")
    
    print(f"\n{'='*50}")
    print(f"Completed: {success_count}/46 pages")
    if failed_pages:
        print(f"Failed: {failed_pages}")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()
