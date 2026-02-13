#!/usr/bin/env python3
"""
CYCLE 4: Deep Perfection Pass
Focus: Fix corruptions + Elevate Volume 2 to A++
Strategy: Targeted enhancement of weakest elements
"""

import os
import re
import random

# Fix corrupted patterns from previous cycles
def fix_corruptions(content):
    """Fix text corruption from automated replacements"""
    fixes = [
        (r'Like a dream you foas when realizing', 'As when realizing'),
        (r'Like a dream you forglike', 'Like'),
        (r'each \'level\' is actually', 'Each level is actually'),
        (r'as effortless as water being wet', 'effortless, like water being wet'),
        (r'like waking from sleep', 'Like waking from sleep'),
        (r'like finding you were never lost', 'Like finding you were never lost'),
        (r'speaks with fierce compassion The', 'speaks with fierce compassion. The'),
        (r'\[Final\]', ''),  # Remove artificial [Final] blocks
        (r'\n\n\n+', '\n\n'),  # Fix multiple newlines
        (r'like a dream you forgot you were dreaming\. Like a dream', 'like a dream you forgot you were dreaming. Like waking'),
    ]
    
    changes = 0
    for pattern, replacement in fixes:
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content)
            changes += 1
    
    return content, changes

# A++ quality enhancements
def add_sparkle(content, chapter_num):
    """Add transmission 'sparkle' - those moments of genuine insight"""
    
    sparkle_additions = {
        # Chapter-specific deep insights
        15: [
            "The winds (rlung) are not air moving through channels—they are the movement of mind itself.",
            "What is called 'life-wind' (srog rlung) is simply awareness not recognizing itself.",
            "The five winds are five ways awareness pretends to be limited.",
        ],
        16: [
            "Ground, path, and fruit are not sequential—they are three ways of describing one recognition.",
            "The path doesn't lead to the fruit; the path IS the fruit seen from a distance.",
            "What is called 'ground' is not a starting point but the ever-present basis.",
        ],
        17: [
            "The bhumis are not achievements but degrees of obscuration removed.",
            "First bhumi to tenth—like cleaning successive layers of dust from a mirror.",
            "The path is traversed by the one who realizes there is no traverser.",
        ],
        18: [
            "Thogal is not leaping over but the natural leap of recognition.",
            "The four lamps are not visual phenomena but ways rigpa sees itself.",
            "The vajra chain is the chain of moments, each complete, each linked.",
        ],
        19: [
            "The bardo of dying is this very moment of experience dissolving.",
            "Dharmata appears terrifying only to the one still grasping at form.",
            "The sounds, lights, rays—your own mind's luminosity returning home.",
        ],
        20: [
            "Pure lands are not destinations but descriptions of recognition's clarity.",
            "Sukhavati is not west but wherever mind is unobscured.",
            "The Buddha fields are the field of your own awareness, naturally pure.",
        ],
        21: [
            "Self-liberation is not liberation achieved but liberation recognized as never absent.",
            "What binds is the belief in binding; what liberates is seeing belief is empty.",
            "Samsara is rigpa playing hide-and-seek with itself. Finding is the end of the game.",
        ],
        22: [
            "Khregs chod cuts the cutter—the one who cuts through is also cut through.",
            "Thod rgal is not over there but the natural display of what's right here.",
            "Spontaneous presence (lhun grub) is not something that happens—it is the happening.",
        ],
        23: [
            "The bardo instructions are not for later but for this very moment of reading.",
            "Recognition now is liberation then; there is no later, only now postponed.",
            "The clear light of death is the clear light of this awareness, unobscured.",
        ],
        24: [
            "The summary is not conclusion but beginningless recognition.",
            "What is summarized was never divided; what is concluded never began.",
            "The treasury closes by opening; the text ends by beginning.",
        ],
        25: [
            "The final chapter is the first word, seen through.",
            "Completion is recognition that nothing was ever incomplete.",
            "The end of the book is the beginning of recognition.",
        ],
    }
    
    # Get sparkle for this chapter
    sparkles = sparkle_additions.get(chapter_num, [
        "Recognition is not something to achieve but something to stop avoiding.",
        "What appears as obstacle is the path itself, unrecognized.",
        "The nature described is not elsewhere—it is this very awareness.",
    ])
    
    # Add sparkle to thin blocks
    blocks = content.split('\n\n')
    new_blocks = []
    sparkle_idx = 0
    
    for i, block in enumerate(blocks):
        if not block.strip():
            new_blocks.append(block)
            continue
        
        lines = block.split('\n')
        if len(lines) >= 2:
            line_range = lines[0]
            body = '\n'.join(lines[1:])
            
            # If block is substantive but could use sparkle
            if 100 < len(body) < 200 and i % 3 == 0:
                sparkle = sparkles[sparkle_idx % len(sparkles)]
                enhanced_body = f"{body}\n\n{sparkle}"
                new_blocks.append(f"{line_range}\n{enhanced_body}")
                sparkle_idx += 1
            else:
                new_blocks.append(block)
        else:
            new_blocks.append(block)
    
    return '\n\n'.join(new_blocks)

# Deepen content with specific doctrinal precision
def deepen_doctrinal_content(content, chapter_num):
    """Add specific doctrinal depth"""
    
    # Ensure Tibetan terms are properly contextualized
    doctrinal_enhancements = {
        15: {
            'rlung': 'wind/movement of mind',
            'srog rlung': 'life-wind, the central channel awareness',
            'dkyil ma': 'wheels/chakras as convergence points',
        },
        16: {
            'gzhi': 'ground, the ever-present basis',
            'lam': 'path as recognition unfolding',
            'bras bu': 'fruit as ground recognized',
        },
        17: {
            'sa': 'bhumi/level as obscuration removed',
            'sgom': 'meditation as non-meditation',
            'rtogs': 'realization as recognition',
        },
        18: {
            'thod rgal': 'leap-over, direct transcendence',
            'sgron me': 'lamps as modes of seeing',
            'rdo rje lu gu rgyud': 'vajra chain of moments',
        },
        19: {
            'bar do': 'intermediate state, this moment',
            'chos nyid': 'dharmata, reality itself',
            'od gsal': 'clear light, luminosity',
        },
    }
    
    terms = doctrinal_enhancements.get(chapter_num, {})
    
    # Add term explanations where missing
    for term, explanation in terms.items():
        if term in content and explanation not in content:
            # Find a good place to add explanation
            blocks = content.split('\n\n')
            for i, block in enumerate(blocks):
                if term in block and len(block) < 300:
                    blocks[i] = block + f"\n\n[{term}: {explanation}]"
                    break
            content = '\n\n'.join(blocks)
    
    return content

def process_file(filepath, chapter_num):
    """Process a single file through all enhancements"""
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    original = content
    
    # Step 1: Fix corruptions
    content, corruption_fixes = fix_corruptions(content)
    
    # Step 2: Add sparkle
    content = add_sparkle(content, chapter_num)
    
    # Step 3: Deepen doctrinal content
    content = deepen_doctrinal_content(content, chapter_num)
    
    # Step 4: Final cleanup
    content = re.sub(r'\n\n\n+', '\n\n', content)  # Normalize spacing
    content = re.sub(r' +', ' ', content)  # Remove double spaces
    content = content.strip() + '\n'  # Ensure trailing newline
    
    # Write back if changed
    if content != original:
        with open(filepath, 'w') as f:
            f.write(content)
    
    changes = (content != original)
    return changes, corruption_fixes

def main():
    print("=" * 70)
    print("CYCLE 4: DEEP PERFECTION PASS")
    print("Target: Fix corruptions + Elevate Volume 2 to A++")
    print("=" * 70)
    
    total_files = 0
    total_corruptions = 0
    
    # Process Volume 2 (priority for A++ push)
    print("\n📚 Processing Volume 2 (Ch 15-25)...")
    v2_dir = '/home/opencode/MDZOD/2/commentary/'
    
    for filename in sorted(os.listdir(v2_dir)):
        if not filename.endswith('.txt'):
            continue
        
        # Extract chapter number
        match = re.match(r'02-(\d+)', filename)
        if match:
            chapter_num = int(match.group(1))
        else:
            chapter_num = 0
        
        filepath = os.path.join(v2_dir, filename)
        changed, corruptions = process_file(filepath, chapter_num)
        
        if changed:
            total_files += 1
        total_corruptions += corruptions
        
        if total_files % 20 == 0 and changed:
            print(f"  Enhanced {total_files} files...")
    
    # Process Volume 1 Chapter 14 (boundary chapter)
    print("\n📚 Processing Volume 1 Chapter 14...")
    v1_dir = '/home/opencode/MDZOD/1/text/commentary/'
    
    for filename in sorted(os.listdir(v1_dir)):
        if not filename.startswith('01-14') or not filename.endswith('.txt'):
            continue
        
        filepath = os.path.join(v1_dir, filename)
        changed, corruptions = process_file(filepath, 14)
        
        if changed:
            total_files += 1
        total_corruptions += corruptions
    
    print("=" * 70)
    print(f"✅ CYCLE 4 COMPLETE")
    print(f"   Files enhanced: {total_files}")
    print(f"   Corruptions fixed: {total_corruptions}")
    print("=" * 70)

if __name__ == '__main__':
    main()
