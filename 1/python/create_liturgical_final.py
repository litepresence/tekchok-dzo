#!/usr/bin/env python3
"""
Liturgical Translation Script - Final Vairotsana Style
Majestic, chantable, transmissive Dzogchen vajra speech
"""

import os
import re

def read_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.readlines()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return []

def parse_line(line):
    match = re.match(r'\[(\d+)\]\s*(.*)', line.strip())
    if match:
        return match.group(1), match.group(2)
    return None, line.strip()

def transform_final(literal, wylie, tibetan, line_num):
    """Final Vairotsana liturgical transformation."""
    lit = literal.strip()
    wyl = wylie.strip()
    tib = tibetan.strip()
    
    # Handle citations
    if 'CITATION' in lit or lit.startswith('###'):
        return lit
    
    # Check for verse
    is_verse = wyl.startswith('/') or lit.startswith('/')
    verse_marker = '/'
    if is_verse:
        lit = lit.lstrip('/').strip()
        wyl = wyl.lstrip('/').strip()
    
    # "Thus it is proclaimed"
    if 'zhes so' in wyl or lit.lower() in ['thus', 'thus is', 'thus is-said']:
        return f"{verse_marker}Thus it is proclaimed."
    
    # Build the text through progressive refinement
    text = lit
    
    # Step 1: Remove grammatical artifacts
    artifacts = ['by-means-of', 'by means of', 'possessed', 'possessing', 
                 'into', 'to', 'from', 'in', 'at', 'as', 'like', 'while']
    for art in artifacts:
        text = re.sub(r'\b' + art + r'\b', '', text, flags=re.IGNORECASE)
    
    # Step 2: Remove prepositional endings
    text = re.sub(r'\s+(and|or|but)\s*$', '', text, flags=re.IGNORECASE)
    
    # Step 3: Handle compound words
    text = text.replace('-', ' ')
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Step 4: Apply Dzogchen terminology
    # Wisdom types
    if 'ka dag' in wyl and 'ye shes' in wyl:
        text = re.sub(r'essence.*?wisdom', 'Wisdom of Primordial Purity', text, flags=re.IGNORECASE)
    if 'lhun grub' in wyl and 'ye shes' in wyl:
        text = re.sub(r'own nature.*?wisdom', 'Wisdom of Spontaneous Perfection', text, flags=re.IGNORECASE)
    if 'thugs rje' in wyl and 'kun khyab' in wyl:
        text = re.sub(r'mind compassion.*?wisdom', 'Wisdom of All-Pervading Compassion', text, flags=re.IGNORECASE)
    if 'chos dbyings' in wyl and 'ye shes' in wyl:
        text = re.sub(r'dharma.*?wisdom', 'Dharmadhatu Wisdom', text, flags=re.IGNORECASE)
    if 'me long' in wyl and 'ye shes' in wyl:
        text = re.sub(r'mirror.*?wisdom', 'Mirror-like Wisdom', text, flags=re.IGNORECASE)
    if 'mnyam nyid' in wyl and 'ye shes' in wyl:
        text = re.sub(r'equality.*?wisdom', 'Wisdom of Equality', text, flags=re.IGNORECASE)
    if 'sor rtog' in wyl and 'ye shes' in wyl:
        text = re.sub(r'discriminat.*?wisdom', 'Discriminating Wisdom', text, flags=re.IGNORECASE)
    if 'bya grub' in wyl and 'ye shes' in wyl:
        text = re.sub(r'action.*?wisdom', 'All-Accomplishing Wisdom', text, flags=re.IGNORECASE)
    
    # Key concepts
    text = re.sub(r'\bngo bo\b', 'Essence', text, flags=re.IGNORECASE)
    text = re.sub(r'\brang bzhin\b', 'Nature', text, flags=re.IGNORECASE)
    text = re.sub(r'\bthugs rje\b', 'Compassion', text, flags=re.IGNORECASE)
    text = re.sub(r'\brig pa\b', 'Awareness', text, flags=re.IGNORECASE)
    text = re.sub(r'\bchos nyid\b', 'Dharmata', text, flags=re.IGNORECASE)
    text = re.sub(r'\bgzhi\b', 'basis', text, flags=re.IGNORECASE)
    
    # Kayas
    text = re.sub(r'\bchos sku\b', 'Dharmakaya', text, flags=re.IGNORECASE)
    text = re.sub(r'\blongs sku\b', 'Sambhogakaya', text, flags=re.IGNORECASE)
    text = re.sub(r'\bsprul sku\b', 'Nirmanakaya', text, flags=re.IGNORECASE)
    text = re.sub(r'\bsku\b', 'Kaya', text, flags=re.IGNORECASE)
    
    # Five
    if 'rtsa ba lnga' in wyl or 'five' in lit.lower():
        text = re.sub(r'\bfive\b', 'five', text, flags=re.IGNORECASE)
    
    # Thirteen
    if 'sku bcu gsum' in wyl or 'thirteen' in lit.lower():
        text = re.sub(r'\bthirteen\b', 'Thirteen', text, flags=re.IGNORECASE)
    
    # Samsara/Nirvana
    text = re.sub(r'\bkhor.*?das\b', 'Samsara-Nirvana', text, flags=re.IGNORECASE)
    text = re.sub(r'\bsamsara.*?nirvana\b', 'Samsara-Nirvana', text, flags=re.IGNORECASE)
    text = re.sub(r'\bkhor ba\b', 'Samsara', text, flags=re.IGNORECASE)
    text = re.sub(r'\bmyang.*?das\b', 'Nirvana', text, flags=re.IGNORECASE)
    
    # Sacred terms capitalization
    sacred = ['wisdom', 'primordial', 'spontaneous', 'compassion', 'awareness',
              'emptiness', 'appearance', 'luminous', 'pure', 'perfect', 'complete',
              'buddha', 'dharmata', 'kaya', 'dharmakaya', 'sambhogakaya', 'nirvana',
              'samsara', 'vajra', 'mandala', 'bindu', 'light', 'clear', 'vidya']
    for term in sacred:
        text = re.sub(r'\b' + term + r'\b', term.title(), text, flags=re.IGNORECASE)
    
    # Clean up
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Capitalize first letter
    if text:
        text = text[0].upper() + text[1:]
    
    # Add verse marker
    if is_verse:
        text = verse_marker + text
    
    # Ensure punctuation
    if text and not text.endswith(('.', '!', '?', '*', '/')):
        text = text.rstrip('.') + '.'
    
    # Special cases
    if 'thal' in wyl.lower() and 'gyur' in wyl.lower():
        if 'from' in lit.lower():
            text = "From the Thalgyur."
    
    # Mu tig phreng ba
    if 'mu tig' in wyl.lower():
        text = "From the Mu Tig Phreng Ba."
    
    # Section markers
    if 'dang po' in wyl.lower():
        text = "First."
    if 'gnyis pa' in wyl.lower():
        text = "Second."
    if 'gsum pa' in wyl.lower():
        text = "Third."
    
    return text

def create_translation(tibetan_lines, wylie_lines, literal_lines):
    liturgical_lines = []
    
    for i, (tib_line, wyl_line, lit_line) in enumerate(zip(tibetan_lines, wylie_lines, literal_lines)):
        line_num, tib_content = parse_line(tib_line)
        _, wyl_content = parse_line(wyl_line)
        _, lit_content = parse_line(lit_line)
        
        if not line_num:
            liturgical_lines.append(tib_line)
            continue
        
        liturgical = transform_final(lit_content, wyl_content, tib_content, line_num)
        liturgical_lines.append(f"[{line_num}] {liturgical}\n")
    
    return liturgical_lines

def process_page(page_num):
    tibetan_path = f"./tibetan/PAGE {page_num}.txt"
    wylie_path = f"./wylie/PAGE {page_num}.txt"
    literal_path = f"./literal/PAGE {page_num}.txt"
    output_path = f"./liturgical/PAGE {page_num}.txt"
    
    tibetan_lines = read_file(tibetan_path)
    wylie_lines = read_file(wylie_path)
    literal_lines = read_file(literal_path)
    
    if not all([tibetan_lines, wylie_lines, literal_lines]):
        return False
    
    liturgical_lines = create_translation(tibetan_lines, wylie_lines, literal_lines)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(liturgical_lines)
    
    return True

def main():
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
