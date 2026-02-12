# Commentary Voice Correction
# Date: 2026-02-12

## Problem Identified

The initial Commentary generation for section 01-01-01-01 contained
dentifying details that revealed the voice as Patrul Rinpoche:

**Prohibited content found:**
```
"My teacher Jigme Gyalwai Nyugu used to say a yak hair tent only 
stands when the first peg holds."

"I remember composing commentaries in my broken tent above Dzogchen 
monastery, wind trying to steal my pages."

"I spent three years memorizing tantras..."
```

## Solution: Wolf in Sheep's Clothing

The Commentary voice should be:
- **Patrul-like in STYLE** (earthy, direct, piercing)
- **Completely ANONYMOUS** (no names, dates, locations)
- **Generic realized yogi** (could be any master)

## Changes Made

### 1. Updated Prompt (`prompt/prompt_practitioner.md`)

Added explicit prohibitions:
- ❌ No names of teachers
- ❌ No specific locations  
- ❌ No dates or historical references
- ❌ No "I remember when..." tied to specific events
- ❌ No identifiable personal anecdotes

Added acceptable alternatives:
- ✅ Generic hermit/yogi references
- ✅ Universal experiences (sickness, doubt)
- ✅ General observations about practice

### 2. Regenerated Sample (01-01-01-01)

**Before (identifiable):**
```
"My teacher Jigme Gyalwai Nyugu used to say..."
"I remember composing commentaries in my broken tent 
 above Dzogchen monastery..."
```

**After (anonymous):**
```
"The yak hair tent is already the palace. You just keep 
 sweeping the floor, waiting for an invitation to somewhere else."
 
"In retreat, you discover that the frozen stream has always 
 been water."
```

## Voice Characteristics Preserved

✓ Earthy, direct tone
✓ Concrete metaphors (yak hair tent, frozen stream, thief in empty hut)
✓ Self-deprecating humor
✓ Practice obstacles referenced (sleepiness, doubt, pride)
✓ Mirror moments (examine self, not others)
✓ Varying sentence rhythm
✓ No imperatives
✓ No generic spiritual formulas

## Identity Markers Removed

✓ Teacher names (Jigme Gyalwai Nyugu)
✓ Specific locations (Dzogchen monastery, Kathok)
✓ Biographical details (three years memorizing)
✓ Historical references (dates, events)
✓ Personal anecdotes tied to specific places/times

## Verification

The new commentary sample (commentary_anonymous.txt) maintains all
the qualities of Patrul's voice while being completely unidentifiable
as any specific historical figure.

The voice could be:
- An anonymous hermit
- Any realized yogi
- The reader's own inner teacher
- Patrul Rinpoche (but not explicitly)

This achieves the "wolf in sheep's clothing" effect—Patrul's piercing
insight delivered through a generic, timeless voice.

## Impact on Production

All future Commentary generation will follow these constraints:
1. No identifying details
2. Generic hermit/yogi persona
3. Universal practice experiences only
4. Earthy, direct style maintained

