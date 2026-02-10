#!/usr/bin/env python3
"""
Verify all sections have:
1. Tibetan titles (unicode only, not blank)
2. English titles (roman characters only, not blank)
3. No duplicate titles in consecutive sections
"""

import json
import re
from collections import defaultdict

def is_tibetan_only(text):
    """Check if text contains only Tibetan unicode characters and punctuation."""
    if not text or not text.strip():
        return False, "Empty"
    
    # Allow Tibetan unicode range, punctuation, spaces, and common Tibetan marks
    # Tibetan: 0F00-0FFF
    allowed_pattern = r'^[\u0F00-\u0FFF\s།༔༄༅༑༈་༌༎༏༐༒]+$'
    
    if re.match(allowed_pattern, text.strip()):
        return True, "Valid Tibetan"
    else:
        # Check what characters are causing issues
        non_tibetan = []
        for char in text:
            if not (re.match(r'[\u0F00-\u0FFF\s།༔༄༅༑༈་༌༎༏༐༒]', char) or char.isspace()):
                non_tibetan.append(char)
        return False, f"Contains non-Tibetan: {''.join(set(non_tibetan))[:20]}"

def is_roman_only(text):
    """Check if text contains only Roman/Latin characters and punctuation."""
    if not text or not text.strip():
        return False, "Empty"
    
    # Allow ASCII letters, numbers, spaces, common punctuation
    # Block Tibetan and other non-roman scripts
    allowed_pattern = r'^[\x00-\x7F\s\-–—\'"()\[\]{}:;,.!?/&]+$'
    
    if re.match(allowed_pattern, text.strip()):
        return True, "Valid Roman"
    else:
        # Check for non-roman characters
        non_roman = []
        for char in text:
            if ord(char) > 127:
                non_roman.append(char)
        return False, f"Contains non-Roman: {''.join(set(non_roman))[:20]}"

def find_consecutive_duplicates(sections_list):
    """Find sections with identical or very similar titles in a row."""
    duplicates = []
    
    for i in range(len(sections_list) - 1):
        curr_key, curr_section = sections_list[i]
        next_key, next_section = sections_list[i + 1]
        
        # Check English titles
        curr_en = curr_section.get('english_title', '').strip()
        next_en = next_section.get('english_title', '').strip()
        
        # Check Tibetan titles
        curr_tb = curr_section.get('tibetan_title', '').strip()
        next_tb = next_section.get('tibetan_title', '').strip()
        
        # Detect exact duplicates
        if curr_en and next_en and curr_en == next_en:
            duplicates.append({
                'type': 'Exact duplicate English',
                'sections': [curr_key, next_key],
                'title': curr_en
            })
        
        # Detect placeholder patterns (same base title with just ordinal markers)
        if curr_en and next_en:
            # Remove ordinal markers to check for base duplicates
            curr_base = re.sub(r'[-–]\s*(དང་པོ|གཉིས་པ|གསུམ་པ|བཞི་པ|ལྔ་པ)[ༀ-࿿\s]*$', '', curr_en).strip()
            next_base = re.sub(r'[-–]\s*(དང་པོ|གཉིས་པ|གསུམ་པ|བཞི་པ|ལྔ་པ)[ༀ-࿿\s]*$', '', next_en).strip()
            
            if curr_base == next_base and curr_base:
                duplicates.append({
                    'type': 'Similar base title',
                    'sections': [curr_key, next_key],
                    'title_curr': curr_en,
                    'title_next': next_en
                })
    
    return duplicates

def main():
    print("=" * 80)
    print("TITLE VERIFICATION SCRIPT")
    print("=" * 80)
    
    # Load boundary file
    with open('/home/opencode/MDZOD/1/boundary_v3.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    issues = {
        'missing_tibetan': [],
        'missing_english': [],
        'invalid_tibetan': [],
        'invalid_english': [],
        'blank_tibetan': [],
        'blank_english': []
    }
    
    # Check each section
    sections_list = sorted(data['sections'].items())
    
    print("\nChecking titles...")
    
    for key, section in sections_list:
        tibetan = section.get('tibetan_title', '')
        english = section.get('english_title', '')
        
        # Check Tibetan
        if not tibetan:
            issues['missing_tibetan'].append(key)
        elif not tibetan.strip():
            issues['blank_tibetan'].append(key)
        else:
            valid, msg = is_tibetan_only(tibetan)
            if not valid:
                issues['invalid_tibetan'].append({
                    'key': key,
                    'title': tibetan[:50],
                    'reason': msg
                })
        
        # Check English
        if not english:
            issues['missing_english'].append(key)
        elif not english.strip():
            issues['blank_english'].append(key)
        else:
            valid, msg = is_roman_only(english)
            if not valid:
                issues['invalid_english'].append({
                    'key': key,
                    'title': english[:50],
                    'reason': msg
                })
    
    # Find duplicates
    duplicates = find_consecutive_duplicates(sections_list)
    
    # Report results
    print("\n" + "=" * 80)
    print("VERIFICATION RESULTS")
    print("=" * 80)
    
    total_issues = sum(len(v) for v in issues.values()) + len(duplicates)
    
    print(f"\nTotal sections: {len(sections_list)}")
    print(f"Total issues: {total_issues}")
    
    if issues['missing_tibetan']:
        print(f"\n❌ Missing Tibetan titles: {len(issues['missing_tibetan'])}")
        for key in issues['missing_tibetan'][:5]:
            print(f"   - {key}")
        if len(issues['missing_tibetan']) > 5:
            print(f"   ... and {len(issues['missing_tibetan']) - 5} more")
    
    if issues['blank_tibetan']:
        print(f"\n❌ Blank Tibetan titles: {len(issues['blank_tibetan'])}")
        for key in issues['blank_tibetan'][:5]:
            print(f"   - {key}")
    
    if issues['invalid_tibetan']:
        print(f"\n❌ Invalid Tibetan titles (non-Tibetan chars): {len(issues['invalid_tibetan'])}")
        for item in issues['invalid_tibetan'][:5]:
            print(f"   - {item['key']}: {item['reason']}")
            print(f"     Title: {item['title']}")
        if len(issues['invalid_tibetan']) > 5:
            print(f"   ... and {len(issues['invalid_tibetan']) - 5} more")
    
    if issues['missing_english']:
        print(f"\n❌ Missing English titles: {len(issues['missing_english'])}")
        for key in issues['missing_english'][:5]:
            print(f"   - {key}")
        if len(issues['missing_english']) > 5:
            print(f"   ... and {len(issues['missing_english']) - 5} more")
    
    if issues['blank_english']:
        print(f"\n❌ Blank English titles: {len(issues['blank_english'])}")
        for key in issues['blank_english'][:5]:
            print(f"   - {key}")
    
    if issues['invalid_english']:
        print(f"\n❌ Invalid English titles (non-Roman chars): {len(issues['invalid_english'])}")
        for item in issues['invalid_english'][:5]:
            print(f"   - {item['key']}: {item['reason']}")
            print(f"     Title: {item['title']}")
        if len(issues['invalid_english']) > 5:
            print(f"   ... and {len(issues['invalid_english']) - 5} more")
    
    if duplicates:
        print(f"\n⚠️  Consecutive duplicate/similar titles: {len(duplicates)}")
        for dup in duplicates[:5]:
            print(f"   - {dup['type']}: {dup['sections']}")
            if 'title' in dup:
                print(f"     Title: {dup['title']}")
            else:
                print(f"     {dup['title_curr']} | {dup['title_next']}")
        if len(duplicates) > 5:
            print(f"   ... and {len(duplicates) - 5} more")
    
    if total_issues == 0:
        print("\n✅ All sections have valid Tibetan and English titles!")
        print("✅ No consecutive duplicates detected!")
    
    # Save results
    results = {
        'total_sections': len(sections_list),
        'total_issues': total_issues,
        'issues': issues,
        'duplicates': duplicates,
        'passed': total_issues == 0
    }
    
    with open('/home/opencode/MDZOD/1/title_verified.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"\nDetailed results saved to title_verified.json")
    
    return total_issues == 0

if __name__ == '__main__':
    success = main()
    exit(0 if success else 1)
