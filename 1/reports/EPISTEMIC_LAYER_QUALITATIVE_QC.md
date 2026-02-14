# EPISTEMIC LAYER QUALITATIVE QC REPORT

**Project:** MDZOD (Theg mchog rin po che'i mdzod)  
**Layer:** Epistemic (Layer 10 of 12)  
**Standard:** A++ Exemplar - Four Pillars Framework  
**Framework:** View Tags | Pedagogy Tags | Risk Flags | Classification Statements
**Date:** 2026-02-14

---

## A++ QUALITATIVE CRITERIA

A file achieves A++ status when it demonstrates:

### 1. Proper XML Tag Format (per prompt_epistemic.md)
- [ ] Uses `<view>` tags: `dzogchen-rigpa`, `dzogchen-sems`, `tantric-transformative`, `sutric-provisional`, `ordinary-cognition`, `non-assertive`
- [ ] Uses `<pedagogy>` tags: `declarative-finality`, `instructional-provisionality`, `polemical-distinction`, `upaya-statement`, `negational-clearing`
- [ ] Uses `<risk>` tags: `reification`, `nihilism`, `view-collapse`, `practice-misread-as-ontology`
- [ ] Contains `<classification>` section with epistemic framing (NOT content restatement)

### 2. Line Range Accuracy
- [ ] Line ranges [start-end] match Tibetan source
- [ ] No missing sections
- [ ] Sequential coverage

### 3. Epistemic Neutrality
- [ ] Classifies FROM WHERE statements are spoken, not what is true
- [ ] Prevents collapse of multiple epistemic registers
- [ ] No devotional language
- [ ] No practice advice
- [ ] No assertions of "ultimately true"

### 4. Cross-Layer Verification
- [ ] Read against Tibetan source
- [ ] Verified against liturgical layer for context
- [ ] Risk flags appropriately applied

---

## COMPLETION STATUS

### VOLUME 1 (Chapters 1-14, Sections 01-01-01-01 through 01-14-13-01)

| Chapter | Section | File | Lines | Status | Notes |
|---------|---------|------|-------|--------|-------|
| 01 | 01-01 | 01-01-01-01.txt | 1-175 | 🔄 IN REVIEW | Custom tags - needs reformat to Four Pillars |
| 01 | 01-02 | 01-01-02-01.txt | 175-577 | 🔄 IN REVIEW | Custom tags - needs reformat |
| 01 | 01-03 | 01-01-03-01.txt | 578-580 | 🔄 IN REVIEW | Short file |
| 02 | 02-01 | 01-02-01-01.txt | 635-840 | 🔄 IN REVIEW | Has [SŪTRIC PROVISIONAL VIEW] tags - needs standardization |

### VOLUME 2 (Chapters 15-25)

| Chapter | Section | File | Lines | Status | Notes |
|---------|---------|------|-------|--------|-------|
| TBD | TBD | TBD | TBD | ⏳ PENDING | Files to be reviewed |

---

## CRITICAL FORMAT ISSUES IDENTIFIED

### Issue 1: Non-Standard Tags
Current epistemic files use custom content tags:
- `<title-protocol>`, `<mandala-homage>`, `<gzhi-characterization>`
- `[SŪTRIC PROVISIONAL VIEW]`, `[TANTRIC TRANSFORMATIVE VIEW]`

**Required:** Convert to prompt-compliant format:
```xml
[1-4]
<view>dzogchen-rigpa</view>
<pedagogy>declarative-finality</pedagogy>
<risk>reification</risk>
<classification>
Statement of epistemic framing from where content is spoken
</classification>
```

### Issue 2: Content Restatement
Current files often restate passage content. Per prompt:
- **NO restating passage content**
- Only classify epistemic stance
- State FROM WHERE spoken, not WHAT is said

### Issue 3: Missing Risk Flags
Risk assessment should use proper `<risk>` tags, not prose "Risk:" mentions.

---

## STANDARD UPGRADE WORKFLOW

1. **Read Tibetan Source** - Verify content and line ranges
2. **Read Liturgical Layer** - Understand contextual meaning
3. **Analyze Current Epistemic** - Identify view registers present
4. **Reformat to Four Pillars**:
   - Convert custom tags to `<view>`, `<pedagogy>`, `<risk>`
   - Replace content summary with epistemic framing
   - Add proper line ranges
5. **Verify** - Ensure no content restatement, only stance classification
6. **Update QC Report** - Mark status and notes

---

## EXEMPLAR TARGET FORMAT (A++)

```xml
[1-4]
<view>dzogchen-rigpa</view>
<pedagogy>declarative-finality</pedagogy>
<risk>reification</risk>
<classification>
Title page establishing nges don (definitive meaning) framing. The protocol "theg mchog mdzod" 
situates text within Atiyoga as apex of nine vehicles—asserting direct recognition of awareness-nature 
over gradualist approaches. Spoken from recognition-register, not comparative evaluation.
</classification>

[5-15]
<view>dzogchen-rigpa</view>
<pedagogy>instructional-provisionality</pedagogy>
<risk>reification</risk>
<classification>
Homage structure encoding five perfections mapped onto three bodies framework. Fivefold prostration 
traces Samantabhadra → Five Families → Ocean Teacher → Five Vidyādharas → Three Worlds' Ornament. 
Pedagogical device for recognition-topology—each "level" simultaneous aspect of single recognition, 
not hierarchical lineage. Risk of temporalizing simultaneous aspects.
</classification>
```

---

## WORK LOG

| Date | Action | Files Processed | Status |
|------|--------|-----------------|--------|
| 2026-02-14 | Created QC Report, reviewed 01-01-01-01, 01-01-02-01, 01-04-01-01 | 3 | Assessment complete |

---

**Copyleft 2026:** Amid all this apparent happening, nothing has happened.
