# Proof Editor Work Order
# 8-Opus Integration Plan
# Treasury of the Supreme Vehicle: Theg mchog rin po che'i mdzod

---

## EXECUTIVE SUMMARY

This document provides comprehensive instructions for proofing the complete 8-opus edition of Longchenpa's *Treasury of the Supreme Vehicle*. The edition is organized into 4 corpora serving distinct audiences, with each opus requiring specific proofing approaches.

**Total Scope:**
- 25 chapters, 213 sections
- 8 PDF volumes (opuses)
- 9 text layers across 4 corpora
- ~3,500 pages estimated

---

## CORPUS/OPUS ARCHITECTURE

### CORPUS 1: PRACTITIONER
**Audience:** Dharma practitioners, retreatants, general readers
**Purpose:** Direct transmission and heart-instruction

**Opus 1** (Chapters 1-14)
- Part I: Introductions + Liturgical text
- Part II: Commentary (Patrul Rinpoche voice)

**Opus 2** (Chapters 15-25)
- Part I: Introductions + Liturgical text
- Part II: Commentary (Patrul Rinpoche voice)

### CORPUS 2: SOURCE
**Audience:** Scholars, translators, Tibetan readers
**Purpose:** Source verification and grammatical analysis

**Opus 3** (Chapters 1-14)
- Tibetan / Wylie / Literal collated by line

**Opus 4** (Chapters 15-25)
- Tibetan / Wylie / Literal collated by line

### CORPUS 3: SCHOLAR
**Audience:** Academic scholars, advanced students
**Purpose:** Critical apparatus and hermeneutical analysis

**Opus 5** (Chapters 1-14)
- Scholar / Epistemic / Delusion interleaved by section

**Opus 6** (Chapters 15-25)
- Scholar / Epistemic / Delusion interleaved by section

### CORPUS 4: MIND
**Audience:** Translation scholars, process researchers
**Purpose:** Experimental documentation of translator cognition

**Opus 7** (Chapters 1-14)
- Cognitive layer (standalone)

**Opus 8** (Chapters 15-25)
- Cognitive layer (standalone)

---

## PROOFING WORKFLOW BY OPUS TYPE

### TYPE A: PRACTITIONER OPUS (1 & 2)

**Proofing Priority:** HIGHEST
**These volumes will be most widely read. Errors here affect transmission.**

**Proofing Sequence:**
1. **Introduction Layer**
   - Verify against chapter structure
   - Check cross-references to other chapters
   - Ensure accessibility without oversimplification
   - Confirm key terms match dictionary.md

2. **Liturgical Layer**
   - **CRITICAL:** Verify strict 1:1 line count with Tibetan
   - Check ||10|| markers every 10 lines
   - Verify <verse>, <prose>, <tantra>, <mantra>, <ornament> tags
   - Read aloud: does it chant? Does it breathe?
   - Capitalization audit against capitalize.md
   - Terminology consistency with dictionary.md
   - Metaphysical precision: no view distortion for elegance

3. **Commentary Layer**
   - Verify line range tags [start-end]
   - **CRITICAL:** Check for LLM-patterned speech:
     * No repetitive imperatives ("Listen!" "Look!")
     * No generic spiritual metaphors
     * Varying sentence length
     * Concrete nomadic/hermit metaphors present
   - Patrul voice consistency: earthy, direct, piercing
   - No scholarly hedging
   - Capitalization audit

**Format Verification:**
- Introduction appears before each chapter
- Liturgical marked with ||10|| line numbers
- Commentary clearly distinguished from liturgical
- Page breaks at logical points

---

### TYPE B: SOURCE OPUS (3 & 4)

**Proofing Priority:** HIGH
**Foundation for all other layers. Must be philologically exact.**

**Proofing Sequence:**
1. **Tibetan Layer**
   - Verify line numbers [1], [2], etc.
   - Check Unicode rendering
   - Confirm no transcription errors
   - Flag any characters that appear corrupted

2. **Wylie Layer**
   - Verify 1:1 correspondence with Tibetan
   - Check pyewts transliteration accuracy
   - Confirm forward slash delimiters /.../
   - Verify line numbers match Tibetan exactly

3. **Literal Layer**
   - Verify 1:1 line count with Tibetan
   - Check hyphenation of compounds
   - Confirm particle translations (kyis, las, la)
   - Verify article omission (no "the" or "a" unless explicit)
   - Check bracket usage [ ] for ambiguities only
   - Confirm no interpretation, only grammar

**Collation Format:**
```
[1]
༄༅།
/theg pa'i mchog/
Supreme-Vehicle

[2]
...
```

**Verification:**
- Each Tibetan line has Wylie and Literal
- Blank line between line groups
- Consistent formatting throughout

---

### TYPE C: SCHOLAR OPUS (5 & 6)

**Proofing Priority:** MEDIUM-HIGH
**Academic credibility depends on precision.**

**Proofing Sequence:**
1. **Interleaving Verification**
   - Confirm sections appear in order: 01-01-01-01, 01-01-02-01, etc.
   - Verify all three layers present for each section
   - Check XML tag formatting: <structure>, <philology>, <context>, <concept>
   - Confirm kebab-case: <ontological-error>, <risk:reification>

2. **Scholar Layer**
   - Four Pillars coverage: structure, philology, context, concept
   - Third-person only (no "I")
   - No practice advice
   - Wylie terms in technical discussions
   - Markdown headers for structural divisions

3. **Epistemic Layer**
   - View tags: <ordinary-cognition>, <dzogchen-rigpa>, etc.
   - Pedagogy tags: <instructional-provisionality>, etc.
   - Risk flags: <risk:reification>, etc.
   - No restatement of content
   - No assertions of "ultimate truth"

4. **Delusion Layer**
   - Error type tags: <ontological-error>, <reification-error>
   - Format: **Misreading:**, **Why it arises:**, **Primary consequence:**
   - No stating of correct view
   - Cascade effects only when clear
   - Clinical, stark tone

**Section Format:**
```
=== SECTION 01-01-01-01 ===

[001-011] <structure>
<analysis>...</analysis>

[001-011] <epistemic>
<view>...</view>
<classification>...</classification>

[001-011] <delusion>
<ontological-error>
**Misreading:** ...
**Why it arises:** ...
```

**Cross-Reference Verification:**
- Line ranges match across all three layers
- Tags consistent (kebab-case)
- Section headers clearly demarcated

---

### TYPE D: MIND OPUS (7 & 8)

**Proofing Priority:** MEDIUM
**Experimental layer. Consistency matters more than perfection.**

**Proofing Sequence:**
1. **Tone Verification**
   - Calm, settled, non-didactic
   - No questions
   - No uncertainty language
   - Varying paragraph length
   - Internal self-talk quality

2. **Content Verification**
   - Line range tags [start-end]
   - Single paragraphs per range
   - No headings, bullets, or lists
   - Implicit coverage of structure, register, risk, preservation

3. **Preface Verification**
   - Reader advisory clear
   - Experimental nature explained
   - Distinction from other corpora stated

**Format:**
```
[24-27]
Scope declaration establishing this as rnam bshad...

[28-35]
Structural framing via three kāyas...
```

---

## CROSS-OPUS INTEGRITY

### Section Numbering System

All opuses use VV-CC-SS-SS format:
- VV: Volume (01 or 02)
- CC: Chapter (01-25)
- SS: Section (01-99)
- SS: Subsection (01-99)

**Example:** 01-07-05-01
- Volume 1
- Chapter 7
- Section 5
- Subsection 1

**Verification:**
- Same section number appears across all opuses
- Practitioner Opus 1/2: section in Commentary
- Source Opus 3/4: section in collation
- Scholar Opus 5/6: section in interleaving
- Mind Opus 7/8: section in cognitive

### Line Number Alignment

**Critical Check:** Line numbers must align across:
- Tibetan (source of truth)
- Wylie (transliteration)
- Literal (grammar)
- Liturgical (elegant English)

**Line 10 markers:** ||10|| appear only in Practitioner liturgical

### Terminology Consistency

All corpora must align with:
- **dictionary.md** - Tibetan-English standards
- **capitalize.md** - Capitalization rules

**Spot check:** rig pa, ka dag, lhun grub should be consistent

---

## QUALITY STANDARDS

### Tier 1: Critical (Must Fix)
- Line count mismatches
- Missing sections
- Corrupted Tibetan Unicode
- Doctrinal errors in Liturgical/Commentary
- Incorrect view classification in Epistemic

### Tier 2: High (Should Fix)
- Capitalization inconsistencies
- Formatting errors (XML tags, markdown)
- Line range mismatches
- Terminology inconsistencies
- Tone violations (Patrul voice, Scholar objectivity)

### Tier 3: Medium (Fix if Time)
- Spacing inconsistencies
- Punctuation variations
- Minor formatting irregularities
- Paragraph length variations (Cognitive)

### Tier 4: Low (Optional)
- Stylistic preferences
- Alternative phrasings
- Layout optimizations

---

## PROOFING PHASES

### Phase 1: Pre-Proof (Automated)
- Line count verification
- Format validation (XML, markdown)
- Section completeness check
- Automated capitalization audit

### Phase 2: Content Proof (Human)
- Practitioner Opus 1/2: Full read-through
- Source Opus 3/4: Spot-check collation
- Scholar Opus 5/6: Tag verification
- Mind Opus 7/8: Tone consistency

### Phase 3: Integration Proof
- Cross-opus section alignment
- Terminology consistency
- Line number verification
- Cross-reference checking

### Phase 4: Final Polish
- Table of contents generation
- Page break optimization
- PDF compilation test
- Final read-through

---

## DELIVERABLES

**For Each Opus:**
1. PDF proof (print-ready)
2. Change log (all corrections)
3. Query list (questions for editor)
4. Sign-off sheet (proof editor certification)

**Final Deliverables:**
- 8 PDF opuses
- Master change log
- Final query resolutions
- Production-ready files

---

## TOOLS AND REFERENCES

**Required References:**
- `dictionary.md` - Terminology standards
- `capitalize.md` - Capitalization rules
- `hyphenation.md` - Compound word standards
- Exposition files for layer conventions

**Verification Commands:**
```bash
# Line count check
wc -l tibetan/01-01-01-01.txt liturgical/01-01-01-01.txt

# Section completeness
ls text/commentary/ | wc -l  # Should be 213

# Format validation
grep -n "<[^>]*>" scholar/01-01-01-01.txt
```

---

## TIMELINE

**Estimated Schedule:**
- Opus 1 (Practitioner Vol 1): 2 weeks
- Opus 2 (Practitioner Vol 2): 2 weeks
- Opus 3 (Source Vol 1): 1 week
- Opus 4 (Source Vol 2): 1 week
- Opus 5 (Scholar Vol 1): 2 weeks
- Opus 6 (Scholar Vol 2): 2 weeks
- Opus 7 (Mind Vol 1): 1 week
- Opus 8 (Mind Vol 2): 1 week
- Integration proofing: 2 weeks

**Total: 14 weeks (3.5 months)**

---

## CONTACT AND ESCALATION

**Questions about:**
- Tibetan source: Reference Tibetan Layer (absolute truth)
- Translation choices: Consult dictionary.md
- Voice/style: Reference prompt documents
- Doctrinal concerns: Escalate to litepresence

**Change Requests:**
- Tier 1-2: Fix immediately, log in change log
- Tier 3-4: Batch for review

---

## SIGN-OFF

**Proof Editor Certification:**

I certify that I have proofed the assigned opuses according to the standards in this work order:

- [ ] Opus 1 (Practitioner Vol 1)
- [ ] Opus 2 (Practitioner Vol 2)
- [ ] Opus 3 (Source Vol 1)
- [ ] Opus 4 (Source Vol 2)
- [ ] Opus 5 (Scholar Vol 1)
- [ ] Opus 6 (Scholar Vol 2)
- [ ] Opus 7 (Mind Vol 1)
- [ ] Opus 8 (Mind Vol 2)

**Proof Editor:** _________________ **Date:** _________________

**Final Approval:** litepresence **Date:** _________________

