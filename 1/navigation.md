# Project Navigation Guide: Theg mchog rin po che'i mdzod

## Overview

This is a 9-layer agentic translation project for Longchenpa's "Treasury of the Supreme Vehicle" (Theg mchog rin po che'i mdzod). The project spans 894 pages across 2 volumes (479 + 415 pages).

**Last Major Update:** 2026-02-08 - Volume 2 Subsequent LLM Drafts Sweep Complete (25 pages remediated)

---

## Absolute Navigation Rules

1) **NEVER CREATE NEW FOLDERS**
2) **NEVER NAVIGATE UPSTREAM** from `/home/oracle/extinction-event/EV/theg pa'i mchog rin po che'i mdzod/1/`
3) **WORK WITHIN THE EXISTING DIRECTORY STRUCTURE**
4) **ALWAYS READ prompt.md BEFORE STARTING** - User may have updated conventions

---

## Directory Structure

```
/home/oracle/extinction-event/EV/theg pa'i mchog rin po che'i mdzod/1/
├── prompt.md                    # Master editorial conventions & layer prompts
├── status.md                    # Real-time project status & metrics
├── khenpo.md                    # Dzogchen lineage quality review
├── exemplars.md                 # Best-practice reference pages
├── contents.md                  # Detailed structural table of contents
├── conventions.md               # Technical translation conventions
├── navigation.md                #### THIS FILE #### Agent navigation guide
├── python/                      # Automation script backups
│   ├── check_status.py
│   ├── complete_epistemic.py
│   ├── generate_all_liturgical.py
│   ├── transliterate_to_wylie.py
│   └── number_pages.py
├── backup/                      # Source text backups
├── volume_1/                    # Volume 1: 479 pages
│   ├── tibetan/                 # TSHAD MA - Source text (immutable)
│   ├── wylie/                   # LAM - Extended Wylie transliteration
│   ├── literal/                 # Dpyad kyi bshad pa - 1:1 grammatical
│   ├── liturgical/              # sgrub pa'i gleng gzhi - Vajra speech
│   ├── commentary/              # ngo sprod kyi bshad pa - Heart instruction
│   ├── scholar/                 # mkhas pa'i dpyod pa - Academic analysis
│   ├── epistemic/               # lta ba'i rim pa - View stratification
│   ├── delusion/                # log pa spang ba - Error detection
│   └── cognitive/               # shes pa'i rjes su brjod pa - Translator log
│
└── volume_2/                    # Volume 2: 415 pages
    ├── tibetan/                 # TSHAD MA - Source text (immutable)
    ├── wylie/                   # LAM - Extended Wylie transliteration
    ├── literal/                 # 1:1 grammatical layer
    ├── liturgical/              # Vajra speech layer
    ├── commentary/              # Heart instruction layer
    ├── scholar/                 # Academic analysis
    ├── epistemic/               # View stratification
    ├── delusion/                # Error detection
    └── cognitive/               # Translator log
```

### Layer Subfolder Contents
Each layer folder contains:
- `PAGE [1-415].txt` or `PAGE [1-479].txt` - Individual page files
- `draft_status.md` - **CRITICAL: Track your changes here**

**IMPORTANT:** Each layer's `draft_status.md` tracks:
- Pages you've revised
- What issues you found
- What corrections you made
- Line numbers affected

---

## Nine-Layer Translation Architecture

### Foundation Layers (Immutable Sources)
| Layer | Tibetan | Purpose | Status | Agent Action |
|-------|---------|---------|--------|--------------|
| **1. TIBETAN** | *tshad ma* | Source of validity - BDRC "Best Quality" text | ✅ 100% Complete | READ ONLY - Never modify |
| **2. WYLIE** | *lam* | Extended Wylie transliteration bridge | ✅ 100% Complete | READ ONLY - Reference only |

### Translation Layers (Core Rendering)
| Layer | Tibetan | Purpose | Voice/Persona | Status |
|-------|---------|---------|---------------|--------|
| **3. LITERAL** | *dpyad kyi bshad pa* | 1:1 grammatical mapping | Precision scalpel | ✅ 100% clean (major remediation complete) |
| **4. LITURGICAL** | *sgrub pa'i gleng gzhi* | Elegant Vajra speech | Vairotsana Lotsawa | ✅ Draft 1 complete |

### Instruction Layers (Pedagogical)
| Layer | Tibetan | Purpose | Voice/Persona | Status |
|-------|---------|---------|---------------|--------|
| **5. COMMENTARY** | *ngo sprod kyi bshad pa* | Direct heart-instruction | Patrul Rinpoche | ✅ OUTSTANDING |
| **6. SCHOLAR** | *mkhas pa'i dpyod pa* | Academic Four Pillars | Tibetologist | V1: 18%, V2: ✅ 100% |

### Analytical Layers (Meta-Analysis)
| Layer | Tibetan | Purpose | Function | Status |
|-------|---------|---------|----------|--------|
| **7. EPISTEMIC** | *lta ba'i rim pa* | View stratification | Air-traffic control for views | ✅ Major remediation complete (25 pages) |
| **8. DELUSION** | *log pa spang ba* | Error detection | Failure-mode cartography | V1: 31%, V2: ✅ 100% |
| **9. COGNITIVE** | *shes pa'i rjes su brjod pa* | Translator alignment log | Audit trail | ✅ 100% |

---

## CURRENT STATE (Updated 2026-02-08)

### Major Remediation Completed

**Volume 2 Subsequent LLM Drafts Sweep:**
- ✅ **18 EPISTEMIC pages** rewritten: 5-7 lines → Comprehensive masterful analysis
- ✅ **6 COMMENTARY pages** rewritten: Garbled text → Proper Patrul voice
- ✅ **1 LITURGICAL page** rewritten: Garbled → Vairotsana rhythmic verse
- ✅ **~600 copula violations** removed from LITERAL layer
- ✅ **8 pages** with severe prose contamination rewritten

**Pages Remediated:**
- **Epistemic:** 16, 101, 102, 103, 105, 152, 200, 223, 250, 253, 266, 273, 285, 300, 322, 350, 400
- **Commentary:** 31, 54, 58, 72, 118, 196
- **Liturgical:** 192

### Critical Issues Resolved
- ✅ Wylie contamination: All 894 literal pages verified clean
- ✅ Copula violations: "is/are" removed where Tibetan doesn't use yin/te
- ✅ Verse markers: "/" and "*/" standardized
- ✅ Prose contamination: Pages 4, 15-20, 203 fully rewritten

---

## File Naming Convention

All page files follow: `PAGE [number].txt` with leading spaces for alignment.
- Example: `PAGE 1.txt`, `PAGE 10.txt`, `PAGE 100.txt`
- Pages are NOT zero-padded
- Files contain line numbers in brackets: `[1]`, `[100]`, etc.

**CRITICAL:** Always use quotes around file paths:
```bash
# CORRECT:
cat "/home/oracle/extinction-event/EV/theg pa'i mchog rin po che'i mdzod/1/volume_2/epistemic/PAGE 101.txt"

# INCORRECT (will fail):
cat /home/oracle/extinction-event/EV/theg pa'i mchog rin po che'i mdzod/1/volume_2/epistemic/PAGE 101.txt
```

---

## Layer Content Format & Constraints

### TIBETAN Layer (TSHAD MA)
```
[1] ཐེག་མཆོག་མཛོད་ཀྱི་རྒྱབ་ཡིག
[2] ཀུན་ཏུ་བཟང་པོ་ལ་ཕྱག་འཚལ་ལོ།
```
**Status:** Immutable. Never modify.

### WYLIE layer (LAM)
```
[1] theg mchog mdzod kyi rgyab yig
[2] kun tu bzang po la phyag 'tshal lo
```
**Status:** Reference only. 99% accurate.

### LITERAL Layer (Dpyad kyi bshad pa)
```
[45] awareness nature from clear-light vajra heart essence teaching */
[46] thus-come all-of mind-of secret unsurpassable complete/
```
**CRITICAL CONSTRAINTS:**
- ❌ NO articles ("the", "a", "an") unless Tibetan uses *de/di*
- ✅ 1:1 word order preservation
- ✅ Particle precision: *las* = "from", *kyis* = "by-means-of"
- ✅ Hyphenate compounds: "self-appearance", "five-arising"
- ✅ Use "/" and "*/" for verse markers
- ✅ Slashed particles: "to/in", "from/out-of"

### LITURGICAL Layer (sgrub pa'i gleng gzhi)
```
[45] The teaching of the clear-light vajra heart essence reveals the nature of awareness.
[46] The secret of all Thus-Come Ones, unsurpassable and complete,
```
**VOICE:** Vairotsana - Majestic, transmissive, Vajra speech
- Metaphysical precision over flowery language
- Elegant prose for commentary, rhythmic verse for root verses
- NO rhyme (creates conceptual closure)
- *rig pa* = "awareness" ONLY

### COMMENTARY Layer (ngo sprod kyi bshad pa)
```
[1-4] Look here, you who seek liberation! Longchenpa begins not with doctrine but with homage...
```
**VOICE:** Patrul Rinpoche - Earthy, direct, heart-instruction
- Direct "you" address throughout
- Tangible metaphors (sky, mountain, fire, ocean)
- Piercing instructions without hedging
- Emaho exclamations at page endings
- NO repetitive formulas (e.g., "empty yet luminous")

### SCHOLAR Layer (mkhas pa'i dpyod pa)
```
[45-47] [STRUCTURE] New rim khanga: The Presentation of the Ground (gzhi)
[45-47] [PHILOLOGY] Analysis of *kun gzhi* vs *rig pa*...
```
**PERSONA:** Eminent Tibetologist-Philologist
- Use [STRUCTURE], [PHILOLOGY], [CONTEXT], [CONCEPT] tags
- Third-person objective (no "I", "you")
- No practice instructions
- Wylie terms with explanations

### EPISTEMIC Layer (lta ba'i rim pa)
```
[87-92]
[DZOGCHEN VIEW - RIGPA SIDE]
[DECLARATIVE FINALITY]
[RISK: REIFICATION]

<Masterful analysis:
Detailed stratification of viewpoint, authority, and pedagogical intent...>
```
**TAGGING SYSTEM:**
- **[DZOGCHEN VIEW – RIGPA SIDE]** - Definitive, atemporal recognition
- **[DZOGCHEN VIEW – SEMS SIDE]** - Entry-level, mind-based
- **[TANTRIC TRANSFORMATIVE VIEW]** - Upaya, subtle body practices
- **[ORDINARY COGNITION]** - Conventional Abhidharmic presentation
- **[DECLARATIVE FINALITY]** - *nges don*, ultimate truth
- **[INSTRUCTIONAL PROVISIONALITY]** - *drang don*, skillful means
- **[UPĀYA STATEMENT]** - Methodological bridge
- **[RISK: ...]** - Error warnings (REIFICATION, NIHILISM, DETERMINISM, etc.)

### DELUSION Layer (log pa spang ba)
```
[214-218]
[ONTOLOGICAL ERROR] [REIFICATION ERROR]

MISREADING: <The ground is a truly existing substrate>
WHY IT ARISES: <Western ontological frameworks>
PRIMARY CONSEQUENCE: <...>
SECONDARY CONSEQUENCES: <...>
CASCADE EFFECTS: <...>
```

### COGNITIVE Layer (shes pa'i rjes su brjod pa)
```
[line range]

RECOGNITION: <What is happening in the text>
VIEW REGISTER: <Sutric provisional / Dzogchen rigpa-side>
TRANSLATION NOTES: <Specific cautions>
PRESERVATION FLAGS: <Technical precision required>
```

---

## Essential Shell Scripts

### 1. Check Status Across All Layers
```bash
#!/bin/bash
echo "=== VOLUME 2 FILE COUNTS ==="
for layer in tibetan wylie literal liturgical commentary scholar epistemic delusion cognitive; do
    count=$(ls -1 "/home/oracle/extinction-event/EV/theg pa'i mchog rin po che'i mdzod/1/volume_2/$layer"/*.txt 2>/dev/null | wc -l)
    echo "$layer: $count files"
done
```

### 2. Find Short/Deficient Files
```bash
#!/bin/bash
# Find epistemic pages with < 15 lines (likely deficient)
echo "=== SHORT EPISTEMIC FILES ==="
find "/home/oracle/extinction-event/EV/theg pa'i mchog rin po che'i mdzod/1/volume_2/epistemic" -name "PAGE *.txt" -exec sh -c '
    lines=$(wc -l < "$1")
    if [ "$lines" -lt 15 ] && [ "$lines" -gt 1 ]; then
        echo "$lines lines: $(basename "$1")"
    fi
' _ {} \; | sort -n
```

### 3. Check Specific Page Across All Layers
```bash
#!/bin/bash
PAGE="PAGE 101.txt"
VOLUME="volume_2"
BASE="/home/oracle/extinction-event/EV/theg pa'i mchog rin po che'i mdzod/1"

echo "=== STATS FOR $PAGE ==="
for layer in tibetan wylie literal liturgical commentary scholar epistemic; do
    FILE="$BASE/$VOLUME/$layer/$PAGE"
    if [ -f "$FILE" ]; then
        lines=$(wc -l < "$FILE")
        echo "$layer: $lines lines"
    else
        echo "$layer: NOT FOUND"
    fi
done
```

### 4. Sample Pages for Quality Check
```bash
#!/bin/bash
# Check first 5 lines of pages 100-105
cd "/home/oracle/extinction-event/EV/theg pa'i mchog rin po che'i mdzod/1/volume_2/epistemic"
for page in {100..105}; do
    echo "=== PAGE $page ==="
    head -5 "PAGE $page.txt"
    echo ""
done
```

### 5. Find Pages Missing Content
```bash
#!/bin/bash
# Find commentary pages that might need work
cd "/home/oracle/extinction-event/EV/theg pa'i mchog rin po che'i mdzod/1/volume_2/commentary"
for f in PAGE*.txt; do
    lines=$(wc -l < "$f")
    if [ $lines -lt 10 ]; then
        echo "$f: $lines lines (possibly deficient)"
    fi
done
```

---

## Quality Control Checklist

### Before Editing Any File:
- [ ] Read `prompt.md` for current conventions
- [ ] Read `status.md` for priority tasks
- [ ] Check the layer's `draft_status.md` for previous work
- [ ] Read TIBETAN source (absolute truth)
- [ ] Read WYLIE reference (structural guide)

### While Editing:
- [ ] Maintain 1:1 line mapping with TIBETAN
- [ ] Follow layer-specific constraints (see above)
- [ ] Use proper tagging for EPISTEMIC/SCHOLAR/DELUSION
- [ ] Maintain voice consistency (Patrul/Vairotsana/Tibetologist)
- [ ] Check for "page bleed" (topics spanning multiple pages)

### After Editing:
- [ ] Verify line count is reasonable (>10 lines for most layers)
- [ ] Update the layer's `draft_status.md` with your changes
- [ ] Run any available validation scripts
- [ ] Check next page for continuity

---

## Common Issues & How to Identify Them

### 1. **Severely Deficient Epistemic Pages**
**Symptom:** Only 5-7 lines with generic text like:
- "The framework presents..."
- "Establishes non-increase as..."
- "Passage operates at the level of..."

**Fix:** Complete rewrite with:
- 2-5 comprehensive sections
- Proper tagging: [DZOGCHEN VIEW - ...], [DECLARATIVE FINALITY], [RISK: ...]
- Masterful analysis with Wylie terms
- Line range coverage

### 2. **Garbled Commentary Pages**
**Symptom:** Text reads like literal translation with no voice:
- "Second particular explain in four from..."
- "Thus, summarizing meaning of gods' and humans'..."
- Awkward syntax, no direct address

**Fix:** Rewrite in Patrul voice:
- "Look here, friend!"
- "Listen!"
- "Do you see?"
- Tangible metaphors
- Emaho endings

### 3. **Prose Contamination in LITERAL**
**Symptom:** Flowing English sentences with articles:
- "The wisdom of awareness is joined with..."
- "Having established the distinction..."
- Complete sentences with "the", "a", "an"

**Fix:** Complete rewrite following literal constraints (no articles, 1:1 word order)

### 4. **Missing Verse Markers**
**Symptom:** Verse sections without "/" at start or "*/" at end

**Fix:** Add proper markers:
```
[265] /project wind move portion/
[266] /awakening self-awareness bliss great/
[267] /five-arise cause-from seed/
[268] /thus*/
```

### 5. **Copula Violations**
**Symptom:** "is", "are" at end of lines in verses (Tibetan doesn't use yin/te)

**Fix:** Remove copula:
- "life wind self essence is/" → "life wind self essence/"
- "that abide palace is/" → "that abide palace/"

---

## Workflow for Subsequent LLM Drafts

### Sequential Sweep Process:

1. **Identify Worst Layer per Page:**
   - Read all 9 layers for the page
   - Compare against TIBETAN source
   - Select the single most deficient layer

2. **Evaluate Against Constraints:**
   - Check for constraint violations (articles, word order, voice)
   - Check for generic/placeholder content
   - Check for proper formatting

3. **Rewrite the Single Worst Layer:**
   - Follow layer-specific prompt constraints
   - Maintain 1:1 line mapping
   - Write comprehensive content

4. **Log Changes:**
   - Update `draft_status.md` in that layer's folder
   - Note: page number, issues found, fixes made

5. **Advance to Next Page:**
   - Check for page bleed (lookahead ±1 page)
   - Continue sequential sweep

---

## Key Reminders

- **Tibetan is TSHAD MA** - Absolute truth, never alter
- **Check draft_status.md** - Other agents may have worked on the same layer
- **Page Bleed is Real** - Topics span pages; maintain continuity
- **Quality Over Speed** - This text carries blessing (jinlab)
- **When in Doubt** - Re-read prompt.md

---

## Contact & Issues

- Report tool issues: https://github.com/anomalyco/opencode/issues
- Translator: litepresence
- Project: The Seven Treasuries (mdzod bdun) - 5th Treasury

---

*Last Updated: 2026-02-08*  
*Navigation Guide for Agentic Translation Project*  
*Volume 2 Remediation Sweep Complete - 25 Pages*
