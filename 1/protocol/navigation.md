# NAVIGATION: Theg mchog rin po che'i mdzod

**Project:** 12-layer Dzogchen translation (213 sections, 2 volumes)  
**Format:** `text/` folder - Section-based (VV-CC-SS-SS.txt)  

---

## Directory Structure

```
text/
├── frozen/              # Immutable (READ ONLY)
│   ├── tibetan/        # Source: 213 files
│   ├── wylie/          # Transliteration: 213 files
│   ├── literal/        # 1:1 mapping: 213 files
│   ├── liturgical/     # Vajra speech: 213 files
│   ├── epistemic/      # View stratification: 213 files
│   └── cognitive/      # Translator log: 213 files
├── dynamic/            # Mutable (WORK HERE)
│   ├── commentary/    # Heart instruction: 213 files
│   ├── scholar/       # Four Pillars: 213 files
│   ├── delusion/      # Error detection: 213 files
│   ├── collated/      # Combined frozen layers: 213 files
│   ├── meter/         # PROSE/VERSE/ORNAMENTAL: 213 files
│   └── assessment/    # Quality metadata: 8 files
├── root/               # Source materials (READ ONLY)
│   ├── artifacts/     # Reference materials
│   └── raw/          # Original source files
└── preface/            # Front matter
```

**Section ID:** `VV-CC-SS-SS` (Volume-Chapter-Section-Subsection)
- `01-01-01-01` = Vol1, Ch1, Sec1, Subsec1
- `02-18-05-01` = Vol2, Ch18, Sec5, Subsec1

---

## Quality Ratios (MANDATORY - BYTE-BASED)

**Measure:** Dynamic layer bytes ÷ Tibetan source bytes

**Why Bytes, Not Lines:**
- Line counts vary with formatting
- Bytes reflect actual content density
- Small files have extreme line-ratio distortions

### SCHOLAR LAYER BYTE RATIO TARGETS

**Critical for preventing fluff and ensuring complete coverage:**

**Based on analysis of 213 sections:**
- 162 complex sections (2000+ bytes): Currently averaging 1.01x - **NEED EXPANSION**
- 31 standard sections (200-2000 bytes): Currently averaging 7.57x - **NEED TRIMMING**
- 20 tiny fragments (<200 bytes): Currently averaging 31.88x - **MASSIVE OVER-ANALYSIS**

| Content Type | Hard Min | Optimal Range | Hard Max | Current Avg | Action |
|--------------|----------|---------------|----------|-------------|--------|
| **Tiny Fragments** (<200 bytes) | 0.5x | 1.0-2.0x | 3.0x | 31.88x | **TRIM** - Brief annotation only |
| **Standard** (200-2000 bytes) | 1.0x | 1.5-3.0x | 4.0x | 7.57x | **TRIM** - Four Pillars coverage |
| **Complex** (2000+ bytes) | 1.5x | 2.0-4.0x | 5.0x | 1.01x | **EXPAND** - Comprehensive analysis |

**Content-Specific Guidance:**

**Trim These (Currently Over-Analyzed):**
- Single-verse structural markers (Tibetan <200 bytes)
- List item annotations ("First:", "Second:")
- Brief transitional phrases
- Section headers without doctrinal content
- Current ratios 10-60x = excessive

**Expand These (Currently Under-Analyzed):**
- Chapter 4: Philosophical doxography (Sāṃkhya, Lokāyata, etc.)
- Chapter 8: Ground/basis analysis with objections/responses
- Chapters 11-14: Detailed tantric physiology (channels, winds, bindus)
- Chapters 18-23: Thögal, bardo, phowa instructions
- Extended tantra citations requiring unpacking
- Current ratios <1.0x on material >5000 bytes = incomplete

**Anti-Fluff Safeguards:**
- **>5.0x on complex material = FLUFF ALERT** - Review for padding
- **>10.0x on any material = MAJOR FLUFF** - Significant trimming required
- **<1.0x on material >2000 bytes = INCOMPLETE** - Missing doctrinal content
- **<0.5x = STRUCTURAL FAILURE** - Needs complete rewrite
- Every paragraph must serve a pillar (Structure/Philology/Context/Concept)

**Qualitative Standards (Beyond Byte Ratios):**

**A++ Quality Markers:**
- ✅ Comprehensive Four Pillars coverage appropriate to content
- ✅ Every technical term in Wylie with semantic explanation
- ✅ No generic filler ("this is important in Buddhism")
- ✅ Line ranges accurately mapped to Tibetan
- ✅ Third-person scholarly voice throughout
- ✅ No devotional language or practice instructions
- ✅ Citations identified and contextualized
- ✅ Doxographical distinctions (Nyingma vs Sarma) clarified

**Red Flags (Regardless of Byte Ratio):**
- 🔴 Repetitive explanations restating the same point
- 🔴 Generic background not specific to the text
- 🔴 Missing analysis for significant Tibetan passages
- 🔴 Inaccurate line ranges
- 🔴 Devotional voice ("we should meditate on this")
- 🔴 No philological analysis of key terms

**Balancing Act:**
- **Tiny content** (1 line): 5-10 lines of analysis maximum
- **Standard content** (50-100 lines): Comprehensive Four Pillars
- **Complex content** (100+ lines): Encyclopedic depth with all pillars

**Validation Commands:**

```bash
# Check single section
cd /home/opencode/MDZOD/1/text
section="01-01-01-01"
tib=$(stat -c%s frozen/tibetan/${section}.txt)
sch=$(stat -c%s dynamic/scholar/${section}.txt)
ratio=$(echo "scale=2; $sch/$tib" | bc)
echo "Scholar ratio: ${ratio}x (target: 1.5-3.0x)"

# Find sections needing expansion (large material <1.5x)
cd /home/opencode/MDZOD/1/text
for f in frozen/tibetan/*.txt; do
  section=$(basename $f .txt)
  tib=$(stat -c%s "$f")
  # Focus on substantial sections (>2000 bytes)
  [ "$tib" -lt 2000 ] && continue
  sch=$(stat -c%s dynamic/scholar/${section}.txt 2>/dev/null || echo 0)
  [ "$sch" != "0" ] && ratio=$(echo "scale=2; $sch/$tib" | bc) && 
    [ $(echo "$ratio < 1.5" | bc) -eq 1 ] && 
    echo "$section: Tibetan=${tib} Ratio=${ratio}x (NEEDS EXPANSION)"
done | sort -t= -k3 -n | head -20

# Find sections needing trimming (tiny material >10x)
cd /home/opencode/MDZOD/1/text
for f in frozen/tibetan/*.txt; do
  section=$(basename $f .txt)
  tib=$(stat -c%s "$f")
  [ "$tib" -gt 200 ] && continue  # Only tiny files
  sch=$(stat -c%s dynamic/scholar/${section}.txt 2>/dev/null || echo 0)
  [ "$sch" != "0" ] && ratio=$(echo "scale=2; $sch/$tib" | bc) && 
    [ $(echo "$ratio > 10" | bc) -eq 1 ] && 
    echo "$section: Tibetan=${tib} Ratio=${ratio}x (NEEDS TRIMMING)"
done | sort -t= -k3 -n | tail -20
```

### COMMENTARY LAYER TARGETS

**Critical for ensuring coverage without fluff:**

| Content Type | Hard Min | Typical Range | Soft Max | Diagnostic Review | Notes |
|--------------|----------|---------------|----------|-------------------|-------|
| **Standard Sections** (1000-5000b) | 0.70x | 0.80-1.20x | 1.50x | >2.50x | Most commentary files |
| **Dense Technical** (philosophy/tantra) | 0.70x | 1.00-1.50x | 1.50x | >2.50x | Samaya, thogal, madhyamaka |
| **Structural Fragments** (<500b) | 0.50x | 1.0-30.0x+ | N/A | >50.0x | Markers, lists, headers |
| **Complex Sections** (>5000b) | 0.60x | 0.80-1.20x | 1.50x | >2.00x | Extended teachings |

**Quality Priority:** Comprehensive coverage > byte ratio. A file at 0.65x with excellent content coverage is better than 1.5x with fluff.

**Current Status (213 files):**
- Average ratio: 1.201x
- Within typical range: 192 files (90.1%)
- Below minimum: 0 files
- Above diagnostic review: 0 files
- Qualitative assessment: A++ across all files

### ALL LAYER TARGETS (Reference)

| Layer | Typical Range | Diagnostic Alert | Diagnostic Review | Focus |
|-------|---------------|------------------|-------------------|-------|
| **Commentary** | **0.80-1.50x** | **<0.70x** | **>2.50x** | **Heart instruction** |
| **Scholar** | **1.5-3.0x** | **<1.00x** | **>5.00x** | **Four Pillars depth** |
| **Delusion** | **0.8-1.5x** | **<0.50x** | **>2.50x** | **Error coverage quality** |
| **Epistemic** | **0.5-1.0x** | **<0.40x** | **>1.50x** | **View precision** |
| Cognitive | 0.3-0.8x | <0.20x | >1.00x | Translator notes |

**Note:** Ratios are diagnostic tools, not targets. Prioritize qualitative criteria over byte counts.

### EPISTEMIC LAYER QUALITY CRITERIA (A++ Standard)

**⚠️ QUALITATIVE ASSESSMENT IS PRIMARY**

**A++ Requirements:**
1. **Comprehensive Coverage** - Every major doctrinal point classified
2. **Specific Terminology** - Technical terms (ka-dag, lhun-grub, kun gzhi, chos sku) explicitly named
3. **Zero Generic Content** - No template phrases ("This passage presents...")
4. **View Precision** - Specific view-register (dzogchen-rigpa, tantric-transformative, sutric-provisional)
5. **Citation Integration** - Root text citations identified with functional context
6. **Risk Contextualization** - Specific doctrinal tension points flagged

**Diagnostic Indicators (Epistemic Layer - Minimal but Specific):**

| Warning | Ratio | Meaning | Action |
|---------|-------|---------|--------|
| INCOMPLETE | <0.05x on doctrinal material (>5000 bytes) | Major doctrinal points unclassified | Check: Are all key view distinctions identified? |
| FLUFF | >0.8x | May contain generic padding | Check: Is every classification passage-specific? |
| HEALTHY | 0.05-0.4x | Proportionate for view classification | Verify 6 qualitative criteria above |

**⚠️ CRITICAL:** Epistemic layer is VIEW CLASSIFICATION, not commentary. Ratios will naturally be lower than commentary/scholar layers. A file at 0.1x with comprehensive view coverage is A++; a file at 0.6x with generic content is C.

**Epistemic Layer Ratio Guidance:**
- **Complex doctrinal sections (50KB+ Tibetan):** 0.05-0.2x is healthy (concise classification)
- **Standard sections (10-50KB):** 0.1-0.4x is healthy
- **Brief sections (<10KB):** 0.2-0.8x is healthy
- **Critical threshold:** <0.03x on major doctrinal material suggests insufficient coverage

**ALWAYS prioritize qualitative assessment:**
- ✅ Are all major doctrinal points classified?
- ✅ Are view registers precisely identified?
- ✅ Are risk flags specific and contextualized?
- ✅ Is Tibetan terminology used appropriately?
- ✅ Zero generic template content?

Files can have LOW ratios but be HIGH QUALITY (minimal but specific).

---

## Key Files

| File | Purpose |
|------|---------|
| `protocol/khenpo.md` | Quality review standards |
| `protocol/status.md` | Current metrics, priorities |
| `protocol/exemplars.md` | Best-practice examples |
| `prompt/prompt_*.md` | Layer-specific guidance |
| `contents/boundary.json` | Section boundaries |

---

## Workflow

1. **Read** `protocol/status.md` for current priorities
2. **Read** `prompt/prompt_[layer].md` for guidance
3. **Read** Tibetan source: `text/frozen/tibetan/VV-CC-SS-SS.txt`
4. **Check** ratios after editing
5. **Reference** exemplars in `protocol/exemplars.md`

---

## 1:1 Line Mapping (LITURGICAL)

**NEVER add/remove lines** - breaks Tibetan alignment.

**Fix breathless lines with punctuation:**
```
❌ WRONG:
[46] <prose> Part one,
[47] <prose> Part two...

✅ CORRECT:
[46] <prose> Part one; part two...
```

---

## Current Priority

**First 4 Sections Status (Byte Ratios):**

| Section | Tib Bytes | Commentary | Byte Ratio | Action |
|---------|-----------|------------|------------|--------|
| 01-01-01-01 | 26,532 | 5,784 | 0.22x | 🔴 EXPAND |
| 01-01-02-01 | 54,442 | 41,694 | 0.77x | ✅ DONE |
| 01-01-03-01 | 5,811 | 5,828 | 1.00x | ✅ DONE |
| 01-02-01-01 | 31,199 | 26,657 | 0.85x | ✅ DONE |

---

**CRITICAL QUALITY PRINCIPLES:**

1. **Full Coverage of Root Material** - Every significant concept, term, and doctrinal point in the Tibetan source must be addressed in the dynamic layer
2. **Zero Fluff** - No padding, repetition, or generic filler content 
3. **Byte Ratios as Guidelines** - The byte ratio targets are standards to check proportionality, NOT quotas to fill
4. **Line Counts Are Irrelevant** - Tibetan sources vary from 1 line to 1000+ lines; line count is never a valid quality metric

**Quality Hierarchy:**
- ✅ A++: Comprehensive coverage, precise terminology, no fluff, appropriate byte ratio
- ✅ A+: Minor gaps but solid coverage, good terminology
- ⚠️  B: Inadequate coverage or excessive fluff despite "good" byte ratio
- 🔴 C: Missing major content or filled with repetitive/generic text

**Version:** 9.2 (2026-02-16)  
**Last Updated:** Data-driven byte ratio targets (coverage > bytes > lines)

