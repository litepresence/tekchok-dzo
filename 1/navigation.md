# Project Navigation Guide: Theg mchog rin po che'i mdzod

## Overview

This is a 6-layer agentic translation project for Longchenpa's "Treasury of the Supreme Vehicle" (Theg mchog rin po che'i mdzod). The project spans 894 pages across 2 volumes (479 + 415 pages).

## Directory Structure

```
/home/oracle/extinction-event/EV/theg pa'i mchog rin po che'i mdzod/1/
├── prompt.md              # Editorial conventions (READ THIS FIRST)
├── status.md              # Current project status
├── khenpo.md              # Critical review from Dzogchen perspective
├── changelog.md           # Revision history
├── exemplars.md           # Best pages by layer
├── contents.md            # Detailed table of contents
├── volume_1/              # Volume 1: 479 pages
│   ├── tibetan/           # Source text (TSHAD MA - immutable)
│   ├── wylie/             # Structural reference (LAM)
│   ├── literal/           # Draft layer 1 (precision grammatical)
│   ├── liturgical/        # Draft layer 2 (Vairotsana voice)
│   ├── commentary/        # Draft layer 3 (Patrul Rinpoche)
│   └── scholar/           # Draft layer 4 (academic analysis)
└── volume_2/              # Volume 2: 415 pages
    ├── tibetan/
    ├── wylie/
    ├── literal/
    ├── liturgical/
    ├── commentary/
    └── scholar/
```

## File Naming Convention

All page files follow: `PAGE [number].txt` with leading spaces for alignment.
- Example: `PAGE 1.txt`, `PAGE 10.txt`, `PAGE 100.txt`
- Pages are NOT zero-padded
- Files contain line numbers in brackets: `[1]`, `[100]`, etc.

## Layer Hierarchy (Order of Precedence)

1. **TIBETAN** (`tibetan/`) - Absolute truth, never modify
2. **WYLIE** (`wylie/`) - Structural reference, 99% accurate
3. **LITERAL** (`literal/`) - 1:1 mechanical translation
4. **LITURGICAL** (`literal/`) - Elegant Vajra speech
5. **COMMENTARY** (`commentary/`) - Patrul Rinpoche persona
6. **SCHOLAR** (`scholar/`) - Academic Four Pillars analysis

---
## CURRENT STATE SNAPSHOT

- Volume 1 (479 pages): subfolders tibetan, wylie, literal, liturgical, commentary, scholar, cognitive, delusion, epistemic
- Volume 2 (415 pages): subfolders tibetan, wylie, literal, liturgical, commentary, scholar, cognitive, delusion, epistemic
- Wylie contamination detected in Literal layer:
  - Volume 1: 7 pages affected (PAGE 3.txt; PAGES 95-100.txt)
  - Volume 2: 15+ pages affected (final section 350-415; specific pages listed in audit)
- Progress by layer (Volumes 1-2):
- Volume 1: Literal (contaminated); Liturgical ~30% revised; Commentary complete; Scholar complete; Epistemic partial (3%); others not started
- Volume 2: Literal contaminated; Liturgical first draft; Commentary partial; Scholar complete; Epistemic partial (4%); others not started
- Next steps: remediation of Wylie-contaminated literal files, completion of Volume 2 commentary, and expansion of Epistemic/Delusion/Cognitive layers

## Essential Shell Scripts

### 1. Count Files in Each Layer

```bash
#!/bin/bash
# count_layers.sh - Shows completion status of all layers

echo "=== FILE COUNT BY LAYER ==="
for vol in volume_1 volume_2; do
    echo -e "\n--- $vol ---"
    for layer in tibetan wylie literal liturgical commentary scholar; do
        path="/home/oracle/extinction-event/EV/theg pa'i mchog rin po che'i mdzod/1/$vol/$layer"
        if [ -d "$path" ]; then
            count=$(ls -1 "$path"/*.txt 2>/dev/null | wc -l)
            echo "$layer: $count files"
        else
            echo "$layer: directory not found"
        fi
    done
done
```

### 2. Find Missing Pages

```bash
#!/bin/bash
# find_gaps.sh - Identifies missing pages in a layer

VOLUME="volume_2"
LAYER="liturgical"
BASE_DIR="/home/oracle/extinction-event/EV/theg pa'i mchog rin po che'i mdzod/1"
TARGET_DIR="$BASE_DIR/$VOLUME/$LAYER"
SOURCE_DIR="$BASE_DIR/$VOLUME/tibetan"

echo "=== FINDING MISSING PAGES IN $VOLUME/$LAYER ==="
echo "Comparing against source (tibetan layer)..."

for source_file in "$SOURCE_DIR"/PAGE*.txt; do
    filename=$(basename "$source_file")
    target_file="$TARGET_DIR/$filename"
    
    if [ ! -f "$target_file" ]; then
        echo "MISSING: $filename"
    fi
done
```

### 3. Check Line Number Continuity

```bash
#!/bin/bash
# check_continuity.sh - Verifies line numbers flow between pages

VOLUME="volume_2"
LAYER="liturgical"
BASE_DIR="/home/oracle/extinction-event/EV/theg pa'i mchog rin po che'i mdzod/1"
DIR="$BASE_DIR/$VOLUME/$LAYER"

echo "=== CHECKING LINE CONTINUITY ==="
cd "$DIR" || exit 1

prev_last_line=0

for page in $(ls -v PAGE*.txt); do
    # Get first line number of current page
    first_line=$(head -1 "$page" | grep -oP '^\[\K\d+' | head -1)
    
    # Get last line number of current page
    last_line=$(tail -1 "$page" | grep -oP '^\[\K\d+' | head -1)
    
    if [ $prev_last_line -ne 0 ]; then
        expected=$((prev_last_line + 1))
        if [ "$first_line" -ne "$expected" ]; then
            echo "GAP: $page starts at [$first_line], expected [$expected]"
        fi
    fi
    
    prev_last_line=$last_line
done
```

### 4. Batch Page Processing

```bash
#!/bin/bash
# process_batch.sh - Template for processing a range of pages

START_PAGE=26
END_PAGE=50
VOLUME="volume_2"
LAYER="liturgical"
BASE_DIR="/home/oracle/extinction-event/EV/theg pa'i mchog rin po che'i mdzod/1"

echo "=== PROCESSING PAGES $START_PAGE-$END_PAGE ==="

for ((i=START_PAGE; i<=END_PAGE; i++)); do
    PAGE_FILE="PAGE $i.txt"
    TIBETAN_FILE="$BASE_DIR/$VOLUME/tibetan/$PAGE_FILE"
    WYLIE_FILE="$BASE_DIR/$VOLUME/wylie/$PAGE_FILE"
    TARGET_FILE="$BASE_DIR/$VOLUME/$LAYER/$PAGE_FILE"
    
    if [ -f "$TIBETAN_FILE" ] && [ -f "$WYLIE_FILE" ]; then
        echo "Processing: $PAGE_FILE"
        # Add your processing logic here
        # Example: Check if target exists, read sources, generate output
    else
        echo "SKIP: $PAGE_FILE (source not found)"
    fi
done
```

### 5. Quick Page Stats

```bash
#!/bin/bash
# page_stats.sh - Shows statistics for a specific page

PAGE="PAGE 26.txt"
VOLUME="volume_2"
BASE_DIR="/home/oracle/extinction-event/EV/theg pa'i mchog rin po che'i mdzod/1"

echo "=== STATS FOR $PAGE ==="

for layer in tibetan wylie literal liturgical; do
    FILE="$BASE_DIR/$VOLUME/$layer/$PAGE"
    if [ -f "$FILE" ]; then
        lines=$(wc -l < "$FILE")
        first_line=$(head -1 "$FILE" | grep -oP '^\[\K\d+' | head -1)
        last_line=$(tail -1 "$FILE" | grep -oP '^\[\K\d+' | head -1)
        echo "$layer: $lines lines, lines [$first_line-$last_line]"
    else
        echo "$layer: NOT FOUND"
    fi
done
```

## Critical Workflow Steps

### Before Starting Work:

1. **ALWAYS read prompt.md first** - This contains the editorial conventions
2. **Check status.md** - See what's been done and what's priority
3. **Review khenpo.md** - Understand quality issues to avoid
4. **Read exemplars.md** - See best practices for each layer

### When Revising a Page:

1. Read the TIBETAN source (absolute truth)
2. Read the WYLIE reference (structural guide)
3. Read the existing target layer file
4. Apply the layer-specific constraints from prompt.md
5. Write the revision maintaining 1:1 line mapping

### Layer-Specific Constraints:

**LITERAL Layer:**
- NO articles ("the", "a", "an") unless Tibetan uses de/di
- 1:1 word order preservation
- Particle ambiguity: use slashes ("to/in", "from/out-of")
- Compounds hyphenated: "self-appearance", "five-arising"

**LITURGICAL Layer:**
- Vairotsana persona: majestic, transmissive
- Elegant prose for commentary, rhythmic verse for citations
- Metaphysical precision over flowery language
- Terminology: *rig pa* = "awareness" ONLY

**COMMENTARY Layer:**
- Patrul Rinpoche voice: earthy, direct, "you" address
- Tangible metaphors (sky, mountain, fire)
- No scholarly hedging ("this could mean...")
- End with Emaho wonder exclamation

**SCHOLAR Layer:**
- Use [STRUCTURE], [PHILOLOGY], [CONTEXT], [CONCEPT] tags
- Third-person objective (no "I", "you")
- No practice instructions
- Wylie terms with explanations

## Common Pitfalls to Avoid

1. **Page Bleed Errors** - Topics often span pages. Don't reset context at page breaks.
2. **Article Creep** - Literal layer must have ZERO articles unless explicitly in Tibetan.
3. **Terminology Drift** - *rig pa* is ALWAYS "awareness", never "consciousness" or "knowing".
4. **Sentence Length** - Liturgical layer: keep sentences under 40 words when possible.
5. **File Misplacement** - Check you're writing to the correct layer folder.

## Useful One-Liners

```bash
# Count files quickly
ls "/home/oracle/extinction-event/EV/theg pa'i mchog rin po che'i mdzod/1/volume_2/liturgical"/*.txt | wc -l

# Find pages with specific content
grep -l "rig pa" "/home/oracle/extinction-event/EV/theg pa'i mchog rin po che'i mdzod/1/volume_2/tibetan"/*.txt

# Check first few lines of a page
head -5 "/home/oracle/extinction-event/EV/theg pa'i mchog rin po che'i mdzod/1/volume_2/liturgical/PAGE 26.txt"

# Compare line counts between layers
for layer in tibetan wylie liturgical; do echo -n "$layer: "; wc -l < "/home/oracle/extinction-event/EV/theg pa'i mchog rin po che'i mdzod/1/volume_2/$layer/PAGE 26.txt"; done

# List pages in order (handles numeric sorting correctly)
ls -1v "/home/oracle/extinction-event/EV/theg pa'i mchog rin po che'i mdzod/1/volume_2/liturgical"/PAGE*.txt | head -20
```

## Mission Statement Protocol

Per prompt.md line 57: When you begin, and every 10 files edited:
1. Re-read prompt.md (user may have updated it)
2. Re-read status.md
3. Re-read khenpo.md
4. Update status.md with current progress

## Key Contacts/Issues

- Report issues: https://github.com/anomalyco/opencode/issues
- Translator: litepresence
- Project: The Seven Treasuries (mdzod bdun) - 5th Treasury

## Remember

- **Tibetan is TSHAD MA** - Absolute truth, never alter
- **Maintain continuity** across page breaks
- **Quality over speed** - This text carries blessing
- **When in doubt, read prompt.md**

---

*Last Updated: 2026-02-07*
*Navigation Guide for Agentic Translation Project*
