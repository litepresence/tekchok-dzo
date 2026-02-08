# Project Navigation Guide: Theg mchog rin po che'i mdzod

## Overview

This is a 6-layer agentic translation project for Longchenpa's "Treasury of the Supreme Vehicle" (Theg mchog rin po che'i mdzod). The project spans 894 pages across 2 volumes (479 + 415 pages).

## Directory Structure

```
/home/oracle/extinction-event/EV/theg pa'i mchog rin po che'i mdzod/1/
├── prompt.md                    # Master editorial conventions & layer prompts
├── status.md                    # Real-time project status & metrics
├── khenpo.md                    # Dzogchen lineage quality review
├── changelog.md                 # Revision history & milestones
├── exemplars.md                 # Best-practice reference pages
├── contents.md                  # Detailed structural table of contents
├── conventions.md               # Technical translation conventions
├── EPISTEMIC_COMPLETION_ROADMAP.md  # Advanced layer completion plan
├── python/                      # Automation scripts
│   ├── check_status.py
│   ├── complete_epistemic.py
│   ├── generate_all_liturgical.py
│   ├── transliterate_to_wylie.py
│   └── number_pages.py
├── backup/                      # Source text backups
└── volume_1/                    # Volume 1: 479 pages
│   ├── tibetan/                 # TSHAD MA - Source text (immutable)
│   │   └── PAGE [1-479].txt
│   ├── wylie/                   # LAM - Extended Wylie transliteration
│   │   └── PAGE [1-479].txt
│   ├── literal/                 # Dpyad kyi bshad pa - 1:1 grammatical
│   │   └── PAGE [1-479].txt
│   ├── liturgical/              # sgrub pa'i gleng gzhi - Vajra speech
│   │   └── PAGE [1-479].txt
│   ├── commentary/              # ngo sprod kyi bshad pa - Heart instruction
│   │   └── PAGE [1-479].txt
│   ├── scholar/                 # mkhas pa'i dpyod pa - Academic analysis
│   │   └── PAGE [1-479].txt     # (85 pages complete, 394 pending)
│   ├── epistemic/               # lta ba'i rim pa - View stratification
│   │   └── PAGE [1-479].txt
│   ├── delusion/                # log pa spang ba - Error detection
│   │   └── PAGE [1-479].txt     # (150 pages complete, 329 pending)
│   └── cognitive/               # shes pa'i rjes su brjod pa - Translator log
│       └── PAGE [1-479].txt
│
└── volume_2/                    # Volume 2: 415 pages
    ├── tibetan/                 # TSHAD MA - Source text
    │   └── PAGE [1-415].txt
    ├── wylie/                   # LAM - Transliteration
    │   └── PAGE [1-415].txt
    ├── literal/                 # 1:1 grammatical layer
    │   └── PAGE [1-415].txt
    ├── liturgical/              # Vajra speech layer
    │   └── PAGE [1-415].txt
    ├── commentary/              # Heart instruction layer
    │   └── PAGE [1-415].txt
    ├── scholar/                 # Academic analysis
    │   └── PAGE [1-415].txt
    ├── epistemic/               # View stratification
    │   └── PAGE [1-415].txt
    ├── delusion/                # Error detection
    │   └── PAGE [1-415].txt
    └── cognitive/               # Translator log
        └── PAGE [1-415].txt
```

## File Naming Convention

All page files follow: `PAGE [number].txt` with leading spaces for alignment.
- Example: `PAGE 1.txt`, `PAGE 10.txt`, `PAGE 100.txt`
- Pages are NOT zero-padded
- Files contain line numbers in brackets: `[1]`, `[100]`, etc.

## Nine-Layer Translation Architecture

### Foundation Layers (Immutable Sources)
| Layer | Tibetan | Purpose | Status |
|-------|---------|---------|--------|
| **1. TIBETAN** | *tshad ma* | Source of validity - BDRC "Best Quality" text | 100% Complete |
| **2. WYLIE** | *lam* | Extended Wylie transliteration bridge | 100% Complete |

### Translation Layers (Core Rendering)
| Layer | Tibetan | Purpose | Voice/Persona | Status |
|-------|---------|---------|---------------|--------|
| **3. LITERAL** | *dpyad kyi bshad pa* | 1:1 grammatical mapping | Precision scalpel | 95.5% clean |
| **4. LITURGICAL** | *sgrub pa'i gleng gzhi* | Elegant Vajra speech | Vairotsana Lotsawa | Draft 2 ~30% |

### Instruction Layers (Pedagogical)
| Layer | Tibetan | Purpose | Voice/Persona | Status |
|-------|---------|---------|---------------|--------|
| **5. COMMENTARY** | *ngo sprod kyi bshad pa* | Direct heart-instruction | Patrul Rinpoche | 100% ✓ OUTSTANDING |
| **6. SCHOLAR** | *mkhas pa'i dpyod pa* | Academic Four Pillars | Tibetologist | V1: 18%, V2: 100% |

### Analytical Layers (Meta-Analysis)
| Layer | Tibetan | Purpose | Function | Status |
|-------|---------|---------|----------|--------|
| **7. EPISTEMIC** | *lta ba'i rim pa* | View stratification | Air-traffic control for views | 100% Complete |
| **8. DELUSION** | *log pa spang ba* | Error detection | Failure-mode cartography | V1: 31%, V2: 100% |
| **9. COGNITIVE** | *shes pa'i rjes su brjod pa* | Translator alignment log | Audit trail | 100% Complete |

### Layer Hierarchy (Order of Authority)
```
TIBETAN (tshad ma) ──► WYLIE (lam) ──► LITERAL (dpyad kyi bshad pa)
                                              │
                                              ▼
LITURGICAL (sgrub pa'i gleng gzhi) ◄──────────┘
       │
       ├──► COMMENTARY (ngo sprod kyi bshad pa) [Patrul]
       │
       ├──► SCHOLAR (mkhas pa'i dpyod pa) [Tibetologist]
       │
       └──► Meta-Analysis Layers:
            ├── EPISTEMIC (view stratification)
            ├── DELUSION (error detection)
            └── COGNITIVE (translator log)
```

### Critical Conventions
- **NEVER modify Tibetan layer** - It is *tshad ma* (absolute truth)
- **NEVER modify Wylie layer** - Reference-only structural guide
- **LITERAL layer:** No articles, 1:1 word order, particle precision
- **LITURGICAL layer:** *rig pa* = "awareness" ONLY, never sacrifice precision for elegance
- **All downstream layers:** Validate against Tibetan source, not upstream translations

---

## Layer Content Format

### Foundation Layers
**TIBETAN:** Unicode Tibetan text, one page per file
```
[1] ཐེག་མཆོག་མཛོད་ཀྱི་རྒྱབ་ཡིག
[2] ཀུན་ཏུ་བཟང་པོ་ལ་ཕྱག་འཚལ་ལོ།
```

**WYLIE:** Extended Wylie transliteration
```
[1] theg mchog mdzod kyi rgyab yig
[2] kun tu bzang po la phyag 'tshal lo
```

### Translation Layers
**LITERAL:** Strict 1:1 mechanical mapping
```
[45] awareness nature from clear-light vajra heart essence teaching */
[46] thus-come all-of mind-of secret unsurpassable complete/
```
*Constraints: No articles, preserve word order, hyphenate compounds*

**LITURGICAL:** Elegant prose and rhythmic verse
```
[45] The teaching of the clear-light vajra heart essence reveals the nature of awareness.
[46] The secret of all Thus-Come Ones, unsurpassable and complete,
```
*Constraints: Metaphysical precision, majestic resonance, no rhyme*

### Instruction Layers
**COMMENTARY:** Patrul Rinpoche heart-instruction
```
[1-4] Look here, you who seek liberation! Longchenpa begins not with doctrine but with homage...
```
*Constraints: Direct "you" address, tangible metaphors, piercing insight*

**SCHOLAR:** Four Pillars academic analysis
```
[45-47] [STRUCTURE] New rim khanga: The Presentation of the Ground (gzhi)
[45-47] [PHILOLOGY] Analysis of *kun gzhi* vs *rig pa*...
```
*Constraints: [STRUCTURE], [PHILOLOGY], [CONTEXT], [CONCEPT] tags, third person*

### Analytical Layers
**EPISTEMIC:** View classification
```
[87-92]
[DZOGCHEN VIEW - SEMS SIDE]
[INSTRUCTIONAL PROVISIONALITY]
<Rationale for classification>
```

**DELUSION:** Error mapping
```
[214-218]
[ONTOLOGICAL ERROR] [REIFICATION ERROR]
MISREADING: <The ground is a truly existing substrate>
WHY IT ARISES: <Western ontological frameworks>
```

**COGNITIVE:** Translator recognition log
```
[line range]
RECOGNITION: <What is happening in the text>
VIEW REGISTER: <Sutric provisional / Dzogchen rigpa-side>
TRANSLATION NOTES: <Specific cautions>
```

---

## CURRENT STATE SNAPSHOT

### VOLUME 1 (479 pages)
| Layer | Files | Status | Notes |
|-------|-------|--------|-------|
| tibetan | 479 | COMPLETE | TSHAD MA - Source text immutable |
| wylie | 479 | COMPLETE | LAM - 99% accurate transliteration |
| literal | 479 | CONTAMINATED | Wylie contamination: ~20+ pages (1, 94, 144-145, 303-350s, 402, 412, 414) |
| liturgical | 479 | DRAFT 2 | ~30% revised (Pages 1-25, 72-110, 151-192) |
| commentary | 479 | COMPLETE | OUTSTANDING - Patrul Rinpoche voice exemplary |
| scholar | 85 | PARTIAL | ~18% complete - needs completion |
| epistemic | 479 | COMPLETE | All pages generated |
| delusion | 150 | PARTIAL | ~31% complete |
| cognitive | 479 | COMPLETE | All pages generated |

### VOLUME 2 (415 pages)
| Layer | Files | Status | Notes |
|-------|-------|--------|-------|
| tibetan | 415 | COMPLETE | TSHAD MA - Source text immutable |
| wylie | 415 | COMPLETE | LAM - 99% accurate transliteration |
| literal | 415 | CONTAMINATED | Wylie contamination: ~20+ pages (14-30s, 314-317) |
| liturgical | 415 | DRAFT 1 | Complete first draft, needs Draft 2 revision |
| commentary | 415 | COMPLETE | OUTSTANDING - Consistent Patrul Rinpoche voice |
| scholar | 415 | COMPLETE | All pages generated with Four Pillars analysis |
| epistemic | 415 | COMPLETE | All pages generated |
| delusion | 415 | COMPLETE | All pages generated |
| cognitive | 415 | COMPLETE | All pages generated |

### CRITICAL FINDINGS
- **Wylie Contamination:** 40+ pages across both volumes contain Wylie text instead of English
  - Volume 1: PAGE 1, 94, 144-145, 303-350s range, 402, 412, 414
  - Volume 2: PAGE 14-30 range, 314-317 range
- **Volume 1 Scholar Gap:** Only 85/479 pages (18%) - significant completion needed
- **Volume 1 Delusion Gap:** Only 150/479 pages (31%) - needs completion

### NEXT PRIORITIES
1. **CRITICAL:** Remediate Wylie-contaminated literal files (40+ pages)
2. **HIGH:** Complete Volume 1 Scholar layer (394 remaining pages)
3. **HIGH:** Complete Volume 1 Delusion layer (329 remaining pages)
4. **MEDIUM:** Continue Volume 2 Liturgical Draft 2 revisions
5. **LOW:** Final polish pass on all layers

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
