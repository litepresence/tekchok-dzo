#!/usr/bin/env python3
"""
CYCLE 1: Template Fatigue Repair
Replaces 2,591 repetitive phrases with 100+ variations
Target: Volume 2 Chapters 15-25
Goal: Elevate from C+ to A material
"""

import os
import random
import re

# 100+ VARIATION PATTERNS (replacing "natural, unforced, complete as it is...")
VARIATIONS = [
    # Recognition-focused (25 variations)
    "What the text describes is not elsewhere—it is the nature of this very moment.",
    "The teaching points to what is already present, not what must be attained.",
    "Recognition dawns when seeking ceases, not through further effort.",
    "The nature described here is not distant—it is the essence of experience itself.",
    "What Longchenpa reveals is the ground of all appearance, always available.",
    "The treasury opens when the seeker rests as the sought.",
    "This passage describes your own nature, though words can only gesture toward it.",
    "The meaning unfolds in recognition, not in accumulation of understanding.",
    "What is taught here is not new knowledge but ancient recognition.",
    "The text invites seeing what has always been the case.",
    "Dzogchen points to the nature of mind, which requires no modification.",
    "The wisdom described is not acquired but acknowledged.",
    "This teaching reveals what was never hidden, only overlooked.",
    "The path spoken of is the recognition that there is no path.",
    "What appears in these lines is the self-liberated nature of all phenomena.",
    "The treasury holds what you already possess but do not recognize.",
    "Longchenpa's words point beyond themselves to direct experience.",
    "The meaning here is found in the space between the words.",
    "This verse describes the nature that cannot be described.",
    "The teaching offers recognition, not information.",
    "What is spoken is the unspeakable nature of awareness.",
    "The text is a finger pointing—look not at the finger.",
    "The treasury contains what has always been your own.",
    "This passage invites the recognition of primordial completeness.",
    "The Dzogchen view is not a view to adopt but the nature to recognize.",
    
    # Nature/Metaphor-focused (25 variations)
    "Like {metaphor}, it requires no effort to be what it is.",
    "The nature described here is as effortless as {metaphor}.",
    "Just as {metaphor} needs no instruction to arise, this nature is self-existing.",
    "The teaching reveals what is as natural as {metaphor}.",
    "What is pointed to here is as spontaneous as {metaphor}.",
    "Like {metaphor}, awareness requires no support to exist.",
    "The nature Longchenpa describes arises as naturally as {metaphor}.",
    "This verse speaks of what is as uncaused as {metaphor}.",
    "The treasury reveals what is as self-existing as {metaphor}.",
    "What is taught here is as unconstructed as {metaphor}.",
    "Like {metaphor}, the nature of mind needs no permission to be.",
    "The meaning here is as ungraspable yet present as {metaphor}.",
    "This passage describes what is as undefiled as {metaphor}.",
    "The Dzogchen view is as unmanufactured as {metaphor}.",
    "What appears in these words is as primordial as {metaphor}.",
    "The teaching points to what is as timeless as {metaphor}.",
    "Like {metaphor}, recognition cannot be forced, only allowed.",
    "The nature described is as unchanging as {metaphor} yet ever-fresh.",
    "This verse reveals what is as vast as {metaphor}.",
    "The treasury holds what is as intimate as {metaphor}.",
    "What Longchenpa transmits is as immediate as {metaphor}.",
    "The meaning here is as luminous as {metaphor}.",
    "This passage speaks of what is as empty yet apparent as {metaphor}.",
    "The teaching describes what is as free as {metaphor}.",
    "Dzogchen recognition is as natural as {metaphor}—always happening.",
    "What is pointed to is as ordinary yet extraordinary as {metaphor}.",
    
    # Direct/Experiential (25 variations)
    "Look at your own mind right now—this is what is meant.",
    "The experience of reading these words is itself the teaching.",
    "What knows these concepts is what the concepts describe.",
    "The awareness that understands is the awareness to be recognized.",
    "This moment of perception is the Dzogchen view manifesting.",
    "The mind that questions is the mind that answers.",
    "What seeks recognition is already recognized in the seeking.",
    "The present experience cannot be separated from primordial wisdom.",
    "Your immediate awareness is the treasury Longchenpa reveals.",
    "The space in which these words arise is the nature described.",
    "What hears or reads this is what is being pointed to.",
    "The knowing quality of this instant is Dharmakaya itself.",
    "This very thought about the teaching is the teaching itself.",
    "The confusion about the meaning is itself luminous clarity.",
    "What appears to not understand is the understanding appearing.",
    "The struggle to grasp this is spontaneous self-liberation.",
    "Your ordinary mind right now is Buddha-mind.",
    "The awareness that feels confused has never been confused.",
    "What searches for recognition is already it.",
    "This instant of experience is the only scripture needed.",
    "The perceiver and perceived are both the treasury's display.",
    "What you are now is what all verses describe.",
    "The nature of this moment is the nature of all moments.",
    "Your present wakefulness is Samantabhadra's enlightenment.",
    "The texture of experience now is the Dzogchen view.",
    
    # Profound/Philosophical (25 variations)
    "Samsara and nirvana are not different in this nature.",
    "The distinction between deluded and liberated mind dissolves here.",
    "What appears as confusion is the play of primordial wisdom.",
    "The aggregates that bind are the display that liberates.",
    "There is no meditation to do, only recognition to allow.",
    "The path is traversed by realizing there is no path.",
    "Effort to achieve what is already present creates the obstacle.",
    "The seeker and sought are one in the treasury's view.",
    "Grasping at liberation is the final bondage to release.",
    "The concepts about emptiness are emptiness itself.",
    "Trying to understand prevents the understanding that is always present.",
    "The teaching undermines the one who would practice it.",
    "What is sought has never been apart from the seeker.",
    "The Dzogchen view dissolves the one who views it.",
    "Recognition happens when the recognizer is recognized as empty.",
    "The practice is the recognition that practice is unnecessary.",
    "What is called confusion is wisdom not recognizing itself.",
    "The treasury reveals that there is nothing to reveal.",
    "Liberation is liberation from the idea of liberation.",
    "The nature described cannot be contaminated or purified.",
    "What is taught is the unteachable nature of awareness.",
    "The text dissolves the one who would understand it.",
    "Dzogchen is the end of all paths, including the path to Dzogchen.",
    "The view is viewed by the view itself, leaving no viewer.",
    "What is spoken here unspeaks the one who speaks.",
]

# Additional fresh metaphors
FRESH_METAPHORS = [
    "mountain shadows shifting with the sun",
    "echo returning to the cliff face",
    "fog lifting from valley floor",
    "seed sprouting without instruction",
    "river cutting canyon over eons",
    "starlight traveling years to reach the eye",
    "ice cracking on frozen lake",
    "heat rising from sun-warmed stone",
    "bird migrating without map",
    "moon pulling tides without effort",
    "fire consuming fuel without choice",
    "clouds forming and dissolving",
    "sound fading into silence",
    "perfume rising from unseen flowers",
    "breath moving without command",
    "heart beating without decision",
    "honey forming in dark hive",
    "pearl growing in hidden oyster",
    "crystal forming in silent cave",
    "aurora dancing without dancer",
    "sand dune shaped by nameless wind",
    "ancient tree growing in cliff face",
    "spring water bubbling from earth",
    "comet streaking through void",
    "mushroom emerging overnight",
]

def replace_templates_in_file(filepath):
    """Replace all template patterns in a single file"""
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    original_content = content
    replacements_made = 0
    
    # Pattern 1: "—natural, unforced, complete as it is. This is the nature of what the text points to. Recognition, not achievement."
    pattern1 = r'—natural, unforced, complete as it is\. This is the nature of what the text points to\. Recognition, not achievement\.'
    matches = re.findall(pattern1, content)
    for match in matches:
        replacement = random.choice(VARIATIONS)
        # If replacement contains {metaphor}, fill it in
        if '{metaphor}' in replacement:
            metaphor = random.choice(FRESH_METAPHORS)
            replacement = replacement.format(metaphor=metaphor)
        content = content.replace(match, replacement, 1)
        replacements_made += 1
    
    # Pattern 2: Same without em-dash
    pattern2 = r'natural, unforced, complete as it is\. This is the nature of what the text points to\. Recognition, not achievement\.'
    matches = re.findall(pattern2, content)
    for match in matches:
        replacement = random.choice(VARIATIONS)
        if '{metaphor}' in replacement:
            metaphor = random.choice(FRESH_METAPHORS)
            replacement = replacement.format(metaphor=metaphor)
        content = content.replace(match, replacement, 1)
        replacements_made += 1
    
    # Pattern 3: "natural, unforced, complete as it is." (standalone)
    pattern3 = r'natural, unforced, complete as it is\.'
    matches = re.findall(pattern3, content)
    for match in matches:
        # Choose a shorter variation
        short_variations = [
            "self-existing and unconstructed.",
            "already complete.",
            "spontaneously perfect.",
            "requiring no modification.",
            "primordially pure.",
            "effortlessly present.",
            "unborn and unceasing.",
            "naturally luminous.",
            "uncaused and unconditioned.",
            "inseparable from awareness.",
        ]
        replacement = random.choice(short_variations)
        content = content.replace(match, replacement, 1)
        replacements_made += 1
    
    # Write back if changes made
    if replacements_made > 0:
        with open(filepath, 'w') as f:
            f.write(content)
    
    return replacements_made

def main():
    commentary_dir = '/home/opencode/MDZOD/2/commentary/'
    
    print("=" * 60)
    print("CYCLE 1: TEMPLATE FATIGUE REPAIR")
    print("Target: 2,591 repetitive phrases")
    print("=" * 60)
    
    files = sorted([f for f in os.listdir(commentary_dir) if f.endswith('.txt')])
    total_replacements = 0
    
    for i, filename in enumerate(files):
        filepath = os.path.join(commentary_dir, filename)
        count = replace_templates_in_file(filepath)
        total_replacements += count
        
        if count > 0 and i % 10 == 0:
            print(f"Processed {i+1}/{len(files)} files... ({total_replacements} replacements so far)")
    
    print("=" * 60)
    print(f"✅ COMPLETE: {total_replacements} template replacements made")
    print(f"✅ Files processed: {len(files)}")
    print("=" * 60)

if __name__ == '__main__':
    main()
