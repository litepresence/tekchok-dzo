#!/usr/bin/env python3
"""
Liturgical Translation Script - Vairotsana Style
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

def create_liturgical_translation(tibetan_lines, wylie_lines, literal_lines):
    """
    Create liturgical translation following Vairotsana style.
    Majestic, chantable, transmissive Dzogchen vajra speech.
    """
    liturgical_lines = []
    
    for i, (tib_line, wyl_line, lit_line) in enumerate(zip(tibetan_lines, wylie_lines, literal_lines)):
        line_num, tib_content = parse_line(tib_line)
        _, wyl_content = parse_line(wyl_line)
        _, lit_content = parse_line(lit_line)
        
        if not line_num:
            liturgical_lines.append(tib_line)
            continue
        
        # Transform literal to liturgical style
        liturgical = transform_to_liturgical(lit_content, wyl_content, tib_content)
        
        liturgical_lines.append(f"[{line_num}] {liturgical}\n")
    
    return liturgical_lines

def transform_to_liturgical(literal, wylie, tibetan):
    """
    Transform literal translation to Vairotsana liturgical style.
    """
    # Dictionary of common Dzogchen terms with liturgical equivalents
    term_transforms = {
        # Wisdom terms
        'exalted-wisdom': 'Wisdom',
        'primordial-wisdom': 'Primordial Wisdom',
        'wisdom': 'Wisdom',
        'ye shes': 'Wisdom',
        'mkhyen pa': 'Omniscience',
        'rig pa': 'Awareness',
        
        # Nature terms
        'ka-dag': 'primordially pure',
        'lhun grub': 'spontaneously perfected',
        'chos nyid': 'Dharmata',
        'rang bzhin': 'innate nature',
        'ngo bo': 'essence',
        
        # Body/Kaya terms
        'sku': 'kaya',
        'body': 'kaya',
        'chos sku': 'Dharmakaya',
        'longs sku': 'Sambhogakaya',
        'sprul sku': 'Nirmanakaya',
        
        # Compassion terms
        'thugs rje': 'Compassion',
        'mind-compassion': 'Compassion',
        'compassion': 'Compassion',
        
        # Reality terms
        'stong pa': 'emptiness',
        'empty': 'empty',
        'snang ba': 'appearance',
        'appearance': 'appearance',
        'snang stong': 'appearance-emptiness',
        
        # Purity terms
        'dag pa': 'pure',
        'pure': 'pure',
        'ma dag': 'impure',
        'impure': 'impure',
        
        # Self terms
        'rang': 'self-',
        'bdag': 'self',
        'self-': 'self-',
        'self': 'self',
        
        # Non-existence terms
        'med pa': 'non-existent',
        'non-existence': 'non-existent',
        'non-existent': 'non-existent',
        'yod med': 'existent and non-existent',
        
        # Perception terms
        'mthong': 'seeing',
        'see': 'seeing',
        'rtogs': 'realization',
        'realize': 'realization',
        'shes': 'knowing',
        'know': 'knowing',
        
        # Spontaneous terms
        'lhun gyis grub': 'spontaneously accomplished',
        'spontaneously': 'spontaneously',
        
        # Complete/Perfect terms
        'rdzogs': 'perfect',
        'complete': 'perfect',
        'perfect': 'perfect',
        'rdzogs pa': 'perfection',
        
        # Buddha/Sentient being terms
        'sangs rgyas': 'Buddha',
        'buddha': 'Buddha',
        'sems can': 'sentient being',
        'sentient-being': 'sentient being',
        
        # Samsara/Nirvana terms
        'khor ba': 'samsara',
        'samsara': 'samsara',
        'myang das': 'nirvana',
        'nirvana': 'nirvana',
        'khor das': 'samsara and nirvana',
        
        # Root terms
        'rtsa ba': 'root',
        'root': 'root',
        'rtsa': 'root',
        
        # Characteristic terms
        'mtshan nyid': 'characteristic',
        'characteristic': 'characteristic',
        'mtshan ma': 'characteristic mark',
        
        # Five wisdoms
        'chos dbyings ye shes': 'Dharmadhatu Wisdom',
        'me long ye shes': 'Mirror-like Wisdom',
        'mnyam nyid ye shes': 'Wisdom of Equality',
        'sor rtog ye shes': 'Discriminating Wisdom',
        'bya grub ye shes': 'All-Accomplishing Wisdom',
        
        # Thalgyur quotes
        'thal gyur': 'Thalgyur',
        'zhes so': 'Thus it is said.',
        'thus': 'Thus',
        'thus is': 'Thus it is.',
        'thus is-said': 'Thus it is said.',
        
        # Various
        'dang': 'and',
        'la': 'in',
        'kyi': 'of',
        'gi': 'by',
        'ste': 'is',
        'ni': 'is',
        'las': 'from',
        'kyang': 'also',
        'yang': 'also',
        'de': 'that',
        'di': 'this',
        'lta': 'like',
        'bu': 'like',
        'ltar': 'as',
        'zhin': 'while',
    }
    
    # Start with literal translation
    text = literal.lower()
    
    # Remove common literal artifacts
    text = re.sub(r'-by-means-of\b', '', text)
    text = re.sub(r'-to\b', '', text)
    text = re.sub(r'-from\b', '', text)
    text = re.sub(r'-in\b', '', text)
    text = re.sub(r'-and\b', '', text)
    text = re.sub(r'-of\b', '', text)
    text = re.sub(r'-by\b', '', text)
    text = re.sub(r'-as\b', '', text)
    text = re.sub(r'-while\b', '', text)
    text = re.sub(r'-into\b', '', text)
    text = re.sub(r'-like\b', '', text)
    text = re.sub(r'-possessed\b', '', text)
    text = re.sub(r'-possessing\b', '', text)
    
    # Clean up hyphens and extra spaces
    text = re.sub(r'-+', '-', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    
    # Apply poetic/liturgical transformations
    # Replace mundane words with majestic equivalents
    poetic_replacements = {
        r'\bis\b': 'is',
        r'\bare\b': 'are',
        r'\bnon-exist\b': 'non-existent',
        r'\bexist\b': 'existent',
        r'\bclear\b': 'luminous',
        r'\bmanifest\b': 'display',
        r'\bappear\b': 'appear',
        r'\babide\b': 'abide',
        r'\bdo\b': 'act',
        r'\bmake\b': 'render',
        r'\bcalled\b': 'known as',
        r'\bsaid\b': 'proclaimed',
        r'\bexplain\b': 'expound',
        r'\belaborate\b': 'extensive',
        r'\bregard\b': 'view',
        r'\bfirst\b': 'primordial',
        r'\bsecond\b': 'second',
        r'\bthree\b': 'three',
        r'\bfour\b': 'four',
        r'\bfive\b': 'five',
        r'\bgreat\b': 'Great',
        r'\bvast\b': 'Vast',
        r'\bexpansive\b': 'Expansive',
    }
    
    for pattern, replacement in poetic_replacements.items():
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    
    # Capitalize important Dzogchen terms
    dzogchen_terms = [
        'primordial', 'wisdom', 'dharmata', 'awareness', 'compassion',
        'kaya', 'dharmakaya', 'sambhogakaya', 'nirmanakaya', 'buddha',
        'samsara', 'nirvana', 'emptiness', 'appearance', 'luminous',
        'spontaneous', 'perfection', 'pure', 'dharma', 'vidya',
        'rigpa', 'kadag', 'lhundrub', 'thugje', 'dzogchen',
    ]
    
    for term in dzogchen_terms:
        text = re.sub(r'\b' + term + r'\b', term.capitalize(), text, flags=re.IGNORECASE)
    
    # Clean up remaining hyphens (word separators in literal translation)
    text = text.replace('-', ' ')
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    
    # Capitalize first letter
    if text:
        text = text[0].upper() + text[1:]
    
    # Add appropriate punctuation for liturgical flow
    if text and not text.endswith(('.', '!', '?', '*/', '/')):
        # Check if it's a verse line (from Thalgyur)
        if text.startswith('/') or wylie.startswith('/'):
            text = text.rstrip('.') + '.'
        else:
            text = text.rstrip('.') + '.'
    
    # Handle verse markers
    if text.startswith('*/'):
        text = text.replace('*/', '').strip()
        text = '*/' + text
    if text.startswith('/'):
        text = text.lstrip('/').strip()
        text = '/' + text
    
    # Handle special Dzogchen citations
    if 'thalgyur' in text.lower():
        text = re.sub(r'thalgyur', 'Thalgyur', text, flags=re.IGNORECASE)
    
    # Final cleanup
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    
    # Ensure proper capitalization after verse markers
    if text.startswith('/'):
        text = '/' + text[1:].strip().capitalize()
    
    return text

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
    liturgical_lines = create_liturgical_translation(tibetan_lines, wylie_lines, literal_lines)
    
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
