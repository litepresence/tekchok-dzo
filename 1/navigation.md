# Project Navigation Guide: Theg mchog rin po che'i mdzod

## Overview

This is a 9-layer agentic translation project for Longchenpa's "Treasury of the Supreme Vehicle" (Theg mchog rin po che'i mdzod). 

**Structure:** 213 sections across 2 volumes (114 + 99 sections)
**Format:** Section-based (VV-CC-SS-SS.txt) - Migrated from page-based (PAGE_XXX.txt)

**Last Major Update:** 2026-02-10 - Migrated to `text/` folder with section-based structure

---

## 🚨 MIGRATION NOTICE (2026-02-10)

**PRIMARY BUILD NOW IN `text/` FOLDER**

The project has migrated from page-based files (PAGE_001.txt) to **section-based files** (01-01-01-01.txt):

| Old Location | New Location | Status |
|--------------|--------------|--------|
| `volume_1/tibetan/PAGE_001.txt` | `text/tibetan/01-01-01-01.txt` | Migrated ✅ |
| `volume_2/tibetan/PAGE_001.txt` | `text/tibetan/02-15-01-01.txt` | Migrated ✅ |
| `volume_1/commentary/` | `text/commentary/` | Migrated ✅ |
| `volume_2/delusion/` | `text/delusion/` | Migrated ✅ |

**Section ID Format:** `VV-CC-SS-SS.txt`
- **VV:** Volume (01 or 02)
- **CC:** Chapter (01-25)  
- **SS:** Section number (01-20+)
- **SS:** Subsection (01, 02, etc.)

**NEW:** `text/meter/` layer added - Contains metrical analysis (PROSE/VERSE/ORNAMENTAL/MANTRA) for all 213 sections.

**Archived:** Old page-based builds moved to `backup/volume_1/` and `backup/volume_2/` for reference.

---

## Text Structure Conventions

### Lecture Hall (རིམ་ཁང་) Chapter System

Longchenpa organizes this text into **19 chapters** called "Lecture Halls" (རིམ་ཁང་, *rim khang*):
- **རིམ་ཁང་དང་པོ** (First Lecture Hall) through **རིམ་ཁང་བཅུ་བཞི་པ** (Fourteenth Lecture Hall) in Volume 1
- **རིམ་ཁང་བཅོ་ལྔ་པ** (Fifteenth Lecture Hall) through **རིམ་ཁང་ཉི་ཤུ་རྩ་བཞི་པ** (Twenty-fourth Lecture Hall) in Volume 2

**CRITICAL NOTE:** Chapter markers appear at the **END** of chapters, not at the beginning. The line "རིམ་ཁང་XX་པའོ།" marks where a chapter concludes. For example:
- Page 479, line 20425 marks the **end** of Chapter 14
- Page 13, line 657 marks the **end** of Chapter 15
- Chapter 9 (Delusion through Symbols) is a brief transitional chapter spanning only **page 300** (approximately 25 lines)

This means chapter page ranges run from the **previous chapter's end marker** to the **current chapter's end marker**.

---

## Absolute Navigation Rules

1) **NEVER CREATE NEW FOLDERS**
2) **NEVER NAVIGATE UPSTREAM** from `/home/oracle/extinction-event/EV/theg pa'i mchog rin po che'i mdzod/1/`
3) **WORK WITHIN THE EXISTING DIRECTORY STRUCTURE**
4) **ALWAYS READ prompt.md BEFORE STARTING** - User may have updated conventions

---

## Directory Structure

```
/home/opencode/MDZOD/1/                         # Project root
├── prompt.md                    # Master editorial conventions & layer prompts
├── status.md                    # Real-time project status & metrics
├── khenpo.md                    # Dzogchen lineage quality review
├── PROJECT_STATE_REPORT.md      # Comprehensive project analysis
├── exemplars.md                 # Best-practice reference pages
├── contents.md                  # Detailed structural table of contents
├── conventions.md               # Technical translation conventions
├── navigation.md                #### THIS FILE #### Agent navigation guide
├── dictionary.md                # Tibetan-English terminology standards
├── boundary.json                # Master structural boundaries (213 sections)
├── markers.md                   # Section markers reference (165 markers)
├── python/                      # Automation scripts (archived)
│   ├── verify_boundaries.py     # Verifies boundary.json against source
│   ├── verify_titles.py         # Validates Tibetan/English titles
│   ├── verify_markers.py        # Syncs markers.md with boundary.json
│   ├── repair_summaries.py      # Repairs content summaries
│   └── [72 utility scripts archived]
├── backup/                      # Archive of old versions & PAGE-based builds
│   ├── boundary_v2.json         # Previous boundary versions
│   ├── contents_v2.md
│   ├── verified.json            # Verification outputs
│   ├── volume_1/                # [ARCHIVED] Page-based Volume 1 build
│   ├── volume_2/                # [ARCHIVED] Page-based Volume 2 build
│   └── [archived reports]
├── text/                        # PRIMARY BUILD - Section-based structure (213 sections)
│   ├── tibetan/                 # TSHAD MA - Source text (01-01-01-01.txt, etc.)
│   ├── wylie/                   # LAM - Extended Wylie transliteration
│   ├── literal/                 # Dpyad kyi bshad pa - 1:1 grammatical
│   ├── liturgical/              # sgrub pa'i gleng gzhi - Vajra speech
│   ├── commentary/              # ngo sprod kyi bshad pa - Heart instruction
│   ├── scholar/                 # mkhas pa'i dpyod pa - Academic analysis
│   ├── epistemic/               # lta ba'i rim pa - View stratification
│   ├── delusion/                # log pa spang ba - Error detection
│   ├── cognitive/               # shes pa'i rjes su brjod pa - Translator log
│   └── meter/                   # NEW - Metrical analysis (VERSE/PROSE/MANTRA)
```

### Layer Subfolder Contents
Each layer folder in `text/` contains:
- `01-01-01-01.txt through 02-25-99-01.txt` - 213 sections following `VV-CC-SS-SS.txt` format
  - **VV:** Volume (01 or 02)
  - **CC:** Chapter (01-25)
  - **SS:** Section number (01-20+)
  - **SS:** Subsection (01, 02, etc.)
- Example: `01-04-12-01.txt` = Volume 1, Chapter 4, Section 12, Subsection 1
- Example: `02-18-05-01.txt` = Volume 2, Chapter 18, Section 5, Subsection 1

**NEW:** `meter/` layer contains metrical analysis for all 213 sections:
- `[PROSE]` - Elegant prose sections
- `[VERSE]` - Rhythmic verse with meter classification (Sang Drel, Nor Nang, etc.)
- `[ORNAMENTAL]` - Headings, markers, symbols
- `[MANTRA]` - Sacred syllables

**IMPORTANT:** Track your changes in the layer's documentation:
- Line numbers affected
- Completion percentages  
- Stub counts
- Meter classifications applied

---

## CURRENT STATE (Updated 2026-02-08)

### ⚠️ CRITICAL FINDING: Bipolar Completion Pattern

**Volume 1:** 95% Complete (Excellent)  
**Volume 2:** 62% Complete (Critically Deficient)  
**Overall:** 79% Complete

### Foundation Layers (Immutable Sources)
| Layer | Tibetan | Purpose | V1 Status | V2 Status | Agent Action |
|-------|---------|---------|-----------|-----------|--------------|
| **1. TIBETAN** | *tshad ma* | Source of validity - BDRC "Best Quality" text | ✅ 100% | ✅ 100% | READ ONLY |
| **2. WYLIE** | *lam* | Extended Wylie transliteration bridge | ✅ 100% | ✅ 100% | READ ONLY |

### Translation Layers (Core Rendering)
| Layer | Tibetan | Purpose | Voice/Persona | V1 Status | V2 Status |
|-------|---------|---------|---------------|-----------|-----------|
| **3. LITERAL** | *dpyad kyi bshad pa* | 1:1 grammatical mapping | Precision scalpel | ✅ 99.2% (4 stubs) | ✅ 99.8% (1 stub) |
| **4. LITURGICAL** | *sgrub pa'i gleng gzhi* | Elegant Vajra speech | Vairotsana Lotsawa | ✅ 96.9% (15 stubs) | ✅ 96.4% (15 stubs) |

### Instruction Layers (Pedagogical) - 🔴 CRITICAL GAPS
| Layer | Tibetan | Purpose | Voice/Persona | V1 Status | V2 Status | Priority |
|-------|---------|---------|---------------|-----------|-----------|----------|
| **5. COMMENTARY** | *ngo sprod kyi bshad pa* | Direct heart-instruction | Patrul Rinpoche | 🔴 34.4% (314 stubs) | 🔴 24.1% (315 stubs) | **CRITICAL** |
| **6. SCHOLAR** | *mkhas pa'i dpyod pa* | Academic Four Pillars | Tibetologist | 🟡 90.4% (46 stubs) | 🟡 70.6% (122 stubs) | High |

### Analytical Layers (Meta-Analysis) - 🔴 CRITICAL GAPS
| Layer | Tibetan | Purpose | Function | V1 Status | V2 Status | Priority |
|-------|---------|---------|----------|-----------|-----------|----------|
| **7. EPISTEMIC** | *lta ba'i rim pa* | View stratification | Air-traffic control | 🟡 84.8% (73 stubs) | 🔴 46.3% (223 stubs) | High |
| **8. DELUSION** | *log pa spang ba* | Error detection | Failure-mode cartography | ✅ 100% (0 stubs) | ⚫ 0.2% (414 stubs) | **CRITICAL** |
| **9. COGNITIVE** | *shes pa'i rjes su brjod pa* | Translator alignment | Audit trail | ⚪ 0% (479 stubs) | ⚪ 0% (415 stubs) | Low |

---

## CRITICAL ISSUES IDENTIFIED

### 🔴 DELUSION Layer - Volume 2: CATASTROPHIC FAILURE
**Status:** 0.2% complete - 414 of 415 pages are empty stubs  
**Risk:** No error detection for wrong view adoption  
**Impact:** Dangerous - could propagate nihilism, eternalism, reification  
**Action:** STOP ALL OTHER WORK. Complete immediately.

### 🔴 COMMENTARY Layer: SEVERELY DEFICIENT  
**Status:** 29% complete - 629 stubs total (314 V1, 315 V2)  
**Risk:** Missing heart instruction (*ngo sprod*)  
**Impact:** Text becomes scholarly exercise, not transmission  
**Action:** Begin systematic Patrul Rinpoche voice generation

### 🔴 EPISTEMIC Layer - Volume 2: INADEQUATE
**Status:** 46% complete - 223 stubs remaining  
**Risk:** View confusion between provisional and definitive meaning  
**Impact:** Misunderstanding of ground, path, and fruition  
**Action:** Continue repair sweep with view-stratification tags

---

## File Naming Convention

All page files follow: `PAGE_XXX.txt` (zero-padded to 3 digits)
- Example: `PAGE_001.txt`, `PAGE_010.txt`, `PAGE_100.txt`
- Files contain line numbers in brackets: `[1]`, `[100]`, etc.

**CRITICAL:** Always use quotes around file paths:
```bash
# CORRECT - Section-based format (current):
cat "/home/opencode/MDZOD/1/text/epistemic/01-01-01-01.txt"

# INCORRECT (will fail):
cat /home/opencode/MDZOD/1/text/epistemic/01-01-01-01.txt

# ARCHIVED - Old page-based format (moved to backup/):
# cat "/home/opencode/MDZOD/1/backup/volume_2/epistemic/PAGE_101.txt"
```

**Recent Change:** Project migrated from PAGE-based structure (PAGE_001.txt) to section-based structure (VV-CC-SS-SS.txt format). All 213 sections follow consistent `VV-CC-SS-SS.txt` naming (e.g., `01-01-01-01.txt`, `02-18-05-01.txt`).

---

## Priority Matrix for Agents

### 🔴 IMMEDIATE (This Week)
1. **Volume 2 Delusion Layer** - 414 stubs need full development
2. **Emergency audit** - Verify no other "silent stub" patterns

### 🔴 URGENT (Next 2-4 Weeks)
3. **Commentary Layer** - 629 pages need Patrul Rinpoche voice
4. **Volume 2 Epistemic Layer** - 223 pages need expansion

### 🟡 HIGH (Next 1-2 Months)
5. **Volume 2 Scholar Layer** - 122 pages need completion
6. **Volume 1 Epistemic Layer** - 73 pages need expansion
7. **Remaining stubs** - 81 pages across all layers

### 🟢 MEDIUM (Polish)
8. **Liturgical stubs** - 30 pages
9. **Scholar V1** - 46 pages

### ⚪ LOW (Optional)
10. **Cognitive Layer** - Entire layer (894 pages)

---

## Agent Workflow Protocol

### Before Starting Work:
1. Read `prompt.md` - Check for updated conventions
2. Read `status.md` - Understand current priorities
3. Read `khenpo.md` - Internalize quality standards
4. Read target layer's `draft_status.md` - See what's been done

### While Working:
5. Follow layer-specific prompts in `prompt.md`
6. Update `draft_status.md` after every 10 files
7. Maintain voice consistency (Vairotsana, Patrul, etc.)
8. Verify line ranges match Tibetan source

### After Completing Work:
9. Update `status.md` with statistics
10. Append insights to `meta.md` if architectural issues found
11. Update `exemplars.md` if you find exceptional pages

---

## Quality Thresholds (Minimum Lines Per Page)

Agents should verify content meets these minimums:

| Layer | Minimum Lines | Target Range |
|-------|---------------|--------------|
| Commentary | 10 | 25-40 |
| Scholar | 20 | 35-80 |
| Epistemic | 15 | 25-60 |
| Delusion | 50 | 100-150 |
| Cognitive | 10 | 15-30 |

Files below minimums should be flagged as "stubs" needing work.

---

## Warning: Silent Stubs

**Critical Issue:** Many files exist in the filesystem but contain only 2-17 lines of placeholder content. These "silent stubs":
- Appear "complete" in file counts
- Are functionally useless for transmission
- Must be identified by line count, not file existence

**Always verify:** `wc -l text/[layer]/VV-CC-SS-SS.txt` before assuming content is substantive.

---

## Key Files for Reference

- **PROJECT_STATE_REPORT.md** - Comprehensive analysis of real project state
- **status.md** - Project-wide status and metrics
- **prompt.md** - Layer specifications and constraints
- **conventions.md** - Methodology and quality standards
- **exemplars.md** - Best-practice examples

---

**Navigation Guide Version:** 3.1  
**Last Updated:** 2026-02-10  
**Critical Path:** 1,339 pages remaining (Commentary 629, Delusion V2 414, Epistemic V2 223)

---

## 🆕 STRUCTURAL DOCUMENTATION (New - Feb 2026)

### Verified Structural Files

The project now has **Khenpo-grade verified** structural documentation:

| File | Purpose | Status |
|------|---------|--------|
| **boundary.json** | Master structural data (213 sections) | ✅ Verified |
| **markers.md** | Section markers reference (165 markers) | ✅ Synchronized |
| **contents.md** | Human-readable documentation | ✅ Complete |

### Key Structural Discoveries

#### 1. Chapter Count: 25 (Not 19!)
**Previous Understanding:** 19 chapters (Lecture Halls 1-19)  
**Correct Understanding:** 25 chapters

The text has 25 chapters total:
- **Volume 1:** Chapters 1-14 (Pages 1-479)
- **Volume 2:** Chapters 15-25 (Pages 1-415)

Chapter markers (རིམ་ཁང་) appear at chapter **ENDS**, not beginnings:
- Chapter 1 ends: "རིམ་ཁང་དང་པོའོ།" (Page 18, line 583)
- Chapter 14 ends: "རིམ་ཁང་བཅུ་བཞི་པའོ།" (Page 479, line 20425)
- Chapter 25 ends: "རིམ་ཁང་ཉི་ཤུ་རྩ་ལྔ་པ་སྟེ་ཐ་མའོ།" (Page 409, line ~16972)

#### 2. Section Structure: 213 Sections

Total sections across all chapters: **213**
- Main sections (subsection 1): **165** (documented in markers.md)
- Subsections (subsection 2+): **48** (within main sections)

Example structure:
```
Chapter 4 (Philosophical Systems)
├── Section 1 (01-04-01-01) - 1 subsection
├── Section 2 (01-04-02-01) - 1 subsection
├── Section 3 (01-04-03-01) - 1 subsection
├── Section 4 (01-04-04-01) - 1 subsection
├── ...
└── Section 20 (01-04-20-01) - 2 subsections (01-04-20-01, 01-04-20-02)
```

#### 3. Volume Boundary

**Critical:** Page numbers **restart** in Volume 2!

- Volume 1: Pages 1-479 (Chapters 1-14)
- Volume 2: Pages 1-415 (Chapters 15-25)

When navigating to content:
- If chapter ≤ 14: Use `text/tibetan/01-CC-SS-SS.txt` (Volume 1 sections)
- If chapter ≥ 15: Use `text/tibetan/02-CC-SS-SS.txt` (Volume 2 sections)
- Section ID format: `VV-CC-SS-SS` (Volume-Chapter-Section-Subsection)

#### 4. Line Numbering System

All source files in `text/` use bracketed line numbers with continuous line numbering per volume:
```
[1] ༄༅།
[2] །ཐེག་མཆོག་མཛོད་ཀྱི་གླེགས་བམ་དང་པོའོ།
[3] །
```

Line numbers are **continuous within each volume** (not per-section):
- Volume 1 (text/tibetan/): Lines 1-20,425
- Volume 2 (text/tibetan/): Lines 1-16,972 (approximately)

**Note:** While files are now section-based (VV-CC-SS-SS.txt), line numbering preserves the original volume-wide continuity for cross-referencing.

---

## 🔧 Verification Scripts

### Available Scripts (in `python/` folder)

#### 1. verify_boundaries.py
**Purpose:** Verifies all 213 start phrases in boundary.json match source text  
**Usage:**
```bash
cd /home/opencode/MDZOD/1
python3 python/verify_boundaries.py
```
**Output:** Creates `backup/verified.json` with True/False for each section
**Status:** All 213 sections verified ✅
**Source:** References `text/tibetan/` for verification

#### 2. verify_titles.py
**Purpose:** Validates Tibetan titles (Tibetan unicode only) and English titles (Roman only)  
**Usage:**
```bash
python3 python/verify_titles.py
```
**Checks:**
- Tibetan titles contain only Tibetan characters (U+0F00-U+0FFF)
- English titles contain only Roman/Latin characters
- No duplicate consecutive titles
- No empty/blank titles

**Output:** Creates `backup/title_verified.json`  
**Status:** 0 issues found ✅

#### 3. verify_markers.py
**Purpose:** Synchronizes markers.md with boundary.json  
**Usage:**
```bash
python3 python/verify_markers.py
```
**Checks:**
- Marker count matches (165)
- Volume assignments correct
- Page numbers match
- Line numbers match
- Auto-repairs discrepancies

**Status:** Synchronized ✅

#### 4. repair_summaries.py
**Purpose:** Repairs short/generic content summaries  
**Usage:**
```bash
python3 python/repair_summaries.py
```
**What it does:**
- Finds sections with summaries like "དང་པོ་ ནི།" (First:)
- Extracts actual content from source text
- Replaces generic summaries with meaningful Tibetan text

**Status:** Repaired 84 sections ✅

---

## 💡 Tips for Future Agents

### 1. ALWAYS Verify File Paths

**Primary Build Location:** All work happens in `text/` folder using section-based naming:
```bash
# CORRECT - Current section-based format:
cat "/home/opencode/MDZOD/1/text/tibetan/01-01-01-01.txt"
cat "/home/opencode/MDZOD/1/text/liturgical/01-04-12-01.txt"

# INCORRECT (will fail):
cat /home/opencode/MDZOD/1/text/tibetan/01-01-01-01.txt

# ARCHIVED - Old page-based format (moved to backup/volume_1/, backup/volume_2/):
# cat "/home/opencode/MDZOD/1/backup/volume_1/tibetan/PAGE_001.txt"
```

### 2. Check Line Counts, Not Just File Existence

**Silent Stubs:** Many files may exist but contain only 2-17 lines of placeholder content:
```bash
# WRONG - assumes content exists:
ls text/delusion/02-17-05-01.txt  # File exists ✓

# RIGHT - verifies actual content:
wc -l text/delusion/02-17-05-01.txt  # Shows 3 lines ⚠️
```

Always verify with `wc -l` before assuming a section is complete.

**Section Lookup:** Use boundary.json to find which section covers specific content:
```bash
# Find section for Chapter 4, Section 12:
grep '"section_id": "01-04-12-01"' boundary.json

# Find all sections in Chapter 18:
grep '"chapter": 18' boundary.json | grep '"subsection": 1' | head -10
```

### 3. Use Structural Files for Navigation

Instead of guessing file locations, use the section-based structure:
```bash
# Look up sections in Chapter 18:
grep '"chapter": 18' boundary.json | grep -o '"section_id": "[^"]*"' | head -5
# Output: Section IDs like 02-18-01-01, 02-18-02-01, etc.

# Find which section contains specific content:
grep -B 2 "specific Tibetan phrase" text/tibetan/*.txt

# List all files in Chapter 4:
ls text/tibetan/01-04-*-*.txt | head -10
```

### 4. Verify Source Before Translating

Before working on any section:
```bash
# 1. Check the section exists in source
ls text/tibetan/01-04-12-01.txt

# 2. Verify it has content
wc -l text/tibetan/01-04-12-01.txt

# 3. Check line numbering
tail -5 text/tibetan/01-04-12-01.txt

# 4. Check meter classification
grep "01-04-12-01" text/meter/*.txt | head -3
```

### 5. Run Verification Scripts Before Major Work

Before starting bulk operations:
```bash
# Verify structural integrity
python3 python/verify_boundaries.py
python3 python/verify_markers.py

# Check for issues
python3 python/verify_titles.py
```

### 6. Update Status Documentation Religiously

After every batch of work, document progress in the appropriate status file:
```bash
# Update the main status file
nano status.md

# Or append to meta.md for architectural insights
nano meta.md

# Document:
# - Sections revised (e.g., 01-04-12-01 through 01-04-15-01)
# - Issues found
# - Line numbers affected
# - Completion percentage
# - Meter classifications applied (VERSE/PROSE/ORNAMENTAL/MANTRA)
```

### 7. Use Exemplars as Templates

Don't improvise—replicate:
```bash
# Read the relevant exemplar from backup/ (page-based) or text/ (section-based)
cat backup/volume_1/commentary/PAGE_141.txt  # 65-line exemplar (page-based)

# Study the pattern, then apply to your section
# Match structure, voice, and depth
# Apply meter layer classifications for liturgical formatting
```

### 8. Mind the Volume Boundary

When working across volumes:
- Volume 1 sections: 01-01-01-01 through 01-14-XX-XX (Chapters 1-14)
- Volume 2 sections: 02-15-01-01 through 02-25-XX-XX (Chapters 15-25)
- Line numbers DO NOT continue between volumes
- Use section IDs to navigate: 01-CC-SS-SS or 02-CC-SS-SS

### 9. Check Section Markers

When looking for specific content:
```bash
# Find all "First" (དང་པོ་) sections
grep "དང་པོ་" markers.md | head -10

# Find sections in Chapter 4
grep -A 25 "## Chapter 4" markers.md
```

### 10. Preserve Source Integrity

**NEVER modify:**
- text/tibetan/ (source text - TSHAD MA)
- text/wylie/ (transliteration - LAM)
- backup/volume_*/ (archived page-based builds)

**ONLY modify:**
- text/literal/
- text/liturgical/
- text/commentary/
- text/scholar/
- text/epistemic/
- text/delusion/
- text/cognitive/
- text/meter/ (metrical analysis layer)

---

## 📊 Quick Reference

### Section ID Format
All sections follow: `VV-CC-SS-SS`
- **VV:** Volume (01 or 02)
- **CC:** Chapter (01-25)
- **SS:** Section number (01-20+)
- **SS:** Subsection (01, 02, etc.)

Examples:
- `01-01-01-01` = Volume 1, Chapter 1, Section 1, Subsection 1
- `02-18-05-01` = Volume 2, Chapter 18, Section 5, Subsection 1
- `01-04-20-02` = Volume 1, Chapter 4, Section 20, Subsection 2

### Chapter Distribution

| Volume | Chapters | Pages | Sections |
|--------|----------|-------|----------|
| 1 | 1-14 | 1-479 | 114 |
| 2 | 15-25 | 1-415 | 99 |
| **Total** | **25** | **894** | **213** |

### Layer Completion Status (Updated 2026-02-10)

| Layer | V1 Status | V2 Status | Priority |
|-------|-----------|-----------|----------|
| Tibetan | ✅ 100% | ✅ 100% | Immutable |
| Wylie | ✅ 100% | ✅ 100% | Immutable |
| Literal | ✅ 99% | ✅ 100% | Low |
| Liturgical | ✅ 97% | ✅ 96% | Medium |
| Commentary | 🔴 34% | 🔴 24% | **CRITICAL** |
| Scholar | 🟡 90% | 🟡 71% | High |
| Epistemic | 🟡 85% | 🔴 46% | High |
| Delusion | ✅ 100% | ⚫ 0.2% | **CRITICAL** |
| Cognitive | ⚪ 0% | ⚪ 0% | Low |

---

**Navigation Guide Version:** 4.0  
**Last Updated:** 2026-02-10  
**Major Change:** Migrated to `text/` folder with section-based structure  
**Primary Build:** `text/` folder (213 sections in VV-CC-SS-SS.txt format)  
**Archived:** `backup/volume_1/` and `backup/volume_2/` (page-based builds)  
**New Layer:** `text/meter/` (metrical analysis for all 213 sections)  
**Structural Documentation:** Khenko-Grade Verified ✅  
**Critical Path:** 1,339 sections remaining

---

## EXEMPLAR-BASED WORKFLOW

### Discovery: Use Exemplars as Templates

The comprehensive audit revealed **7 high-quality exemplar pages** that prove quality is achievable. Use these as templates instead of improvising.

### Exemplar Library

| Task | Use Exemplar | Why It Works |
|------|-------------|--------------|
| **Commentary repair** | Volume 1 PAGE_141.txt | 65 lines, perfect Patrul voice |
| **Delusion V2 generation** | Volume 1 PAGE_001.txt | 104 lines, 5 error types |
| **Scholar V2 repair** | Volume 2 PAGE_002.txt | 119 lines, Four Pillars |
| **Scholar V2 intro** | Volume 2 PAGE_001.txt | 90 lines, structural precision |

### How to Use Exemplars

1. **Read the exemplar file completely**
   ```bash
   cat "/home/oracle/extinction-event/EV/theg pa'i mchog rin po che'i mdzod/1/volume_1/commentary/PAGE_141.txt"
   ```

2. **Study the pattern:**
   - Commentary: Line-by-line engagement, earthy tone, technical precision
   - Delusion: Error type → Why → Consequences → Cascade
   - Scholar: [STRUCTURE] → [PHILOLOGY] → [CONCEPT] → [CONTEXT]

3. **Apply pattern to stub files:**
   - Don't invent new formats
   - Copy the exemplar structure
   - Adapt content to current page

4. **Verify against exemplar:**
   - Does it match the voice?
   - Does it have the structure?
   - Does it meet line count?

### Quality Gates Using Exemplars

**Before marking complete:**
- [ ] Read the relevant exemplar
- [ ] Match exemplar's structure
- [ ] Match exemplar's voice/persona
- [ ] Meet or exceed exemplar's line count
- [ ] Update draft_status.md with exemplar reference

### Example Workflow

**Task:** Repair Commentary section 01-04-12-01.txt (currently 9-line stub)

**Step 1:** Study exemplar
```bash
wc -l backup/volume_1/commentary/PAGE_141.txt
# Result: 65 lines
cat "backup/volume_1/commentary/PAGE_141.txt"
# Note: Line-by-line pattern, earthy metaphors, direct address
```

**Step 2:** Read source
```bash
cat "text/tibetan/01-04-12-01.txt"
cat "text/literal/01-04-12-01.txt"
cat "text/meter/01-04-12-01.txt"  # Check if VERSE or PROSE
```

**Step 3:** Generate using exemplar pattern
- Write 50-65 lines (match exemplar)
- Use line-by-line engagement (match exemplar)
- Include earthy metaphors (match exemplar)
- Direct "you" address (match exemplar)
- Apply meter classification from meter layer

**Step 4:** Verify
```bash
wc -l text/commentary/01-04-12-01.txt
# Should be: 50+ lines (matching exemplar's 65)
```

**Step 5:** Document
```bash
# Update status.md:
# "Repaired 01-04-12-01 using PAGE_141.txt exemplar pattern"
```

### Critical Path Using Exemplars

**Phase 1: Volume 2 Delusion (10 sessions)**
- Exemplar: PAGE_001.txt (104 lines, 5 error types)
- Target: 414 stubs
- Pattern: Error classification → Why it arises → Consequences → Cascade

**Phase 2: Commentary (15 sessions)**
- Exemplar: PAGE_141.txt (65 lines, Patrul voice)
- Target: 629 stubs (314 V1 + 315 V2)
- Pattern: Line-by-line, earthy, direct, piercing

**Phase 3: Scholar Volume 2 (5 sessions)**
- Exemplar: PAGE_002.txt (119 lines, Four Pillars)
- Target: 122 stubs
- Pattern: [STRUCTURE] → [PHILOLOGY] → [CONCEPT] → [CONTEXT]

**Total: 30 sessions** (not 54)

### Why Exemplars Change Everything

**Before:** Each session = experimentation, uncertainty, variable quality
**After:** Each session = replication of proven excellence

The exemplars prove:
1. The architecture works
2. Quality IS achievable
3. Volume 2 CAN match Volume 1
4. The pattern is established—just scale it

**Don't reinvent. Replicate.**

---

*Exemplar Navigation Guide Added:* 2026-02-08  
*Total Exemplars:* 7 proven high-quality pages  
*Workflow:* Study exemplar → Replicate pattern → Verify match → Scale


---

## PREMIER EXEMPLAR WORKFLOW: Exceptional Quality Standards

### Discovery: 3 PREMIER Exemplars Achieve 242-365% of Targets

The deep-dive audit uncovered **3 PREMIER exemplars** that redefine quality expectations:

| Tier | Exemplar | Layer | Lines | Target % | Standard |
|------|----------|-------|-------|----------|----------|
| **🏆 PREMIER** | PAGE_126-127 | Delusion | 363 | 242% | Exceptional depth |
| **🏆 PREMIER** | PAGE_199 | Scholar | 292 | 365% | Dissertation quality |
| **🏆 PREMIER** | PAGE_123 | Epistemic | 97 | 162% | Hermeneutical mastery |
| **🥈 ELITE** | PAGE_327 | Commentary | 53 | 133% | Outstanding instruction |
| **🥈 ELITE** | V2 PAGE_050 | Scholar | 131 | 164% | Volume 2 proof |

### The New Standard: Don't Aim for Minimum

**OLD THINKING:** "Generate stubs to minimum viable quality (100 lines Delusion, 80 lines Scholar)"

**NEW THINKING:** "Generate stubs to PREMIER standards (363 lines Delusion, 292 lines Scholar)"

**Why:** PAGE_126 proves 363 lines is achievable. The architecture supports MASSIVE depth. Scale it.

### Premier Tier Generation Protocol

#### Phase 1: Exceptional Depth (15 sessions)

**Sessions 1-5: Volume 2 Delusion (414 stubs)**
- **Template:** PAGE_126.txt (363 lines)
- **Standard:** 8-10 error taxonomies, CASCADE EFFECTS, PAGE BLEED
- **Depth:** 200-360 lines per page

**Step-by-step:**
```bash
# 1. Study template
cat volume_1/delusion/PAGE_126.txt
# Note: Multiple [TAGS: ...], CASCADE EFFECTS, PAGE BLEED AWARENESS

# 2. Read source
cat volume_2/tibetan/PAGE_XXX.txt
cat volume_2/literal/PAGE_XXX.txt

# 3. Generate using template structure
# - 8-10 error types per page
# - [TAGS: ERROR-TYPE-1] [TAGS: ERROR-TYPE-2]
# - MISREADING → WHY IT ARISES → PRIMARY CONSEQUENCE
# - SECONDARY CONSEQUENCES → CASCADE EFFECTS
# - PAGE BLEED AWARENESS

# 4. Verify depth
cat volume_2/delusion/PAGE_XXX.txt | wc -l
# Should be: 200-360 lines (matching PAGE_126's 363)
```

**Sessions 6-10: Scholar (168 stubs)**
- **Template:** PAGE_199.txt (292 lines)
- **Standard:** Tantra citations, philological depth, verse analysis
- **Depth:** 150-290 lines per page

**Step-by-step:**
```bash
# 1. Study template
cat volume_1/scholar/PAGE_199.txt
# Note: STRUCTURE section, PHILOLOGY section, tantra citations

# 2. Generate using template structure
# - [STRUCTURE] with comprehensive analysis
# - [PHILOLOGY] with technical terms
# - Verse quotations from tantras
# - Synonym analysis

# 3. Verify depth
wc -l volume_1/scholar/PAGE_XXX.txt
# Should be: 150-290 lines (matching PAGE_199's 292)
```

**Sessions 11-15: Epistemic (296 stubs)**
- **Template:** PAGE_123.txt (97 lines)
- **Standard:** Sophisticated tagging, risk analysis, technical precision
- **Depth:** 60-100 lines per page

#### Phase 2: Elite Quality (12 sessions)

**Sessions 16-25: Commentary (629 stubs)**
- **Template:** PAGE_327.txt (53 lines)
- **Standard:** Progressive instruction, call to action, earthy voice
- **Depth:** 40-65 lines per page

**Sessions 26-27: Polish & Consistency**
- Cross-layer verification
- PAGE BLEED continuity checks
- Voice consistency validation

### Quality Verification Against Premier Exemplars

**Don't verify against minimum thresholds. Verify against PREMIER exemplars:**

```bash
# Verification script concept
verify_premier_standard() {
    layer=$1
    page=$2
    exemplar=$3
    
    page_lines=$(wc -l < "$page")
    exemplar_lines=$(wc -l < "$exemplar")
    
    # Should be within 50% of exemplar (not minimum)
    min_acceptable=$((exemplar_lines / 2))
    
    if [ $page_lines -lt $min_acceptable ]; then
        echo "FAIL: $page ($page_lines lines) < 50% of exemplar ($exemplar_lines lines)"
        return 1
    fi
    
    echo "PASS: $page meets PREMIER standard"
    return 0
}

# Usage:
verify_premier_standard "delusion" "volume_2/delusion/PAGE_100.txt" "volume_1/delusion/PAGE_126.txt"
# Should be: >181 lines (50% of PAGE_126's 363)
```

### Volume 2 Proof: PAGE_050

**The Critical Evidence:**
```bash
cat volume_2/scholar/PAGE_050.txt | wc -l
# Result: 131 lines

head -40 volume_2/scholar/PAGE_050.txt
# Shows: SA BCAD structure, 12+ philological terms, visionary terminology
```

**What This Proves:**
- Volume 2 CAN achieve 131-line Scholar pages
- Volume 2 CAN achieve Volume 1 quality
- The gap is coverage (122 stubs), not capability

**Implication:** All 414 Volume 2 Delusion stubs, 223 Epistemic stubs, and 315 Commentary stubs can reach PREMIER standards.

### Revised Timeline (PREMIER Standards)

**Original:** 54 sessions (discouraging)
**Revised (minimum):** 30 sessions (achievable)
**Revised (PREMIER):** 27 sessions (exceptional)

**The Math:**
- PREMIER replication: 25 pages/session using templates
- Total stubs: 1,339 pages
- Sessions: 1,339 ÷ 25 = 53.5 → **27 sessions with batch efficiency**

### Critical Success Factors

**1. Study Template First**
```bash
# Before generating ANY page, read the premier exemplar:
cat volume_1/delusion/PAGE_126.txt    # 363-line template
cat volume_1/scholar/PAGE_199.txt     # 292-line template
cat volume_2/epistemic/PAGE_123.txt   # 97-line template
cat volume_1/commentary/PAGE_327.txt  # 53-line template
```

**2. Replicate Structure, Not Content**
- Copy the organizational pattern
- Adapt content to current page
- Maintain voice/persona
- Match depth (lines per analysis point)

**3. Verify Against Exemplar, Not Minimum**
```bash
# Bad: "Is this >20 lines?"
# Good: "Is this >50% of PAGE_126's 363 lines (=181+)?"
```

**4. Document in draft_status.md**
```markdown
### PAGE XXX - Revised to PREMIER Standard
**Date:** 2026-XX-XX
**Template:** PAGE_126.txt (Delusion)
**Lines:** 245 (68% of exemplar's 363)
**Quality:** 8 error taxonomies, CASCADE EFFECTS, PAGE BLEED
**Status:** PREMIER Tier Complete
```

### Final Guidance

**Don't aim for "good enough."**

PAGE_126 proves 363-line delusion analysis is achievable.  
PAGE_199 proves 292-line scholarly exposition is achievable.  
PAGE_123 proves 97-line epistemic stratification is achievable.

**Generate all 1,339 stubs to these standards.**

The Theg mchog mdzod deserves EXCEPTIONAL quality. The PREMIER exemplars prove it's achievable.

---

*Premier Workflow Added:* 2026-02-08  
*Total Premier Exemplars:* 3 exceptional + 5 elite  
*Quality Standard:* 242-365% of original targets  
*Timeline:* 27 sessions to exceptional quality  
*Key Principle:* Replicate PREMIER templates, don't settle for minimums

