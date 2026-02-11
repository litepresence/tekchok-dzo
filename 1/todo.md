# Translation Quality TODO List

**Document Type:** Quality Assurance Tracking  
**Last Updated:** 2026-02-11 (Audit completed)  
**Status:** Living document - update as sections are revised

**CRITICAL AUDIT FINDING:** Line count comparison with Tibetan sources reveals significant missing content. See "MISSING LINES AUDIT" section below.

**ACQUAINTANCE:** This document catalogs problematic sections across all translation layers that require revision to meet A++ Gold Standard. Use this to prioritize work and track progress.

---

## CHAPTER 1: The Perfect Teacher

### 01-01-03-01.txt - Telephonic Tibetan Throughout
**Priority:** HIGH  
**Lines:** 578-1060  
**Issues:**
- Tibetan word order preserved instead of natural English syntax
- Fragmentary sentence structures throughout
- Missing verbs and articles

**Example Problems:**
```
[578] First, the sequence of fields and container-contained is explained:
[579] Thus from bodhi in the self-nature of Vajradhara complete in qualities,
[580] Abiding as Saṃbhogakāya from Dharma-kāya,
[581] From the five-family kāya,
```

**Required Fixes:**
- [ ] Rewrite with natural English word order
- [ ] Add missing verbs ("Thus from bodhi..." → "Thus, from the bodhi...")
- [ ] Add articles ("five-family kāya" → "the five-family kāya")
- [ ] Complete fragmentary sentences

---

## CHAPTER 2: Container World and Contents

### 01-02-01-03.txt - Fragmentary Structure
**Priority:** CRITICAL  
**Lines:** 1-2 (entire file)  
**Issues:**
- Only 2 lines in entire file
- Incomplete thought
- Missing context

**Example Problems:**
```
[997] Second holding flower garland,
(End of file - total 2 lines)
```

**Required Fixes:**
- [ ] Expand to complete section (estimated 50-100 lines)
- [ ] Add proper context from Tibetan source
- [ ] Complete the thought with full sentences

---

### 01-02-01-04.txt - Fragmentary Structure
**Priority:** CRITICAL  
**Lines:** 1-1 (entire file)  
**Issues:**
- Only 1 line in entire file
- Clearly incomplete

**Required Fixes:**
- [ ] Expand to complete section
- [ ] Cross-reference with Tibetan source
- [ ] Add proper context

---

### 01-02-01-05.txt - Fragmentary & Garbled
**Priority:** CRITICAL  
**Lines:** 997-1060  
**Issues:**
- Abrupt transitions without context
- Missing subjects and verbs
- Garbled word order ("Measure making direction equal similar to four parks")
- Incomplete descriptions

**Example Problems:**
```
[1059] Measure making direction equal similar to four parks.
[1060] Tree at north-east called complete gather burst, root five leagues down reach,
[1061] Upward exceeding hundred, branches spread like umbrella, circumference fifty leagues curl,
```

**Required Fixes:**
- [ ] Rewrite with natural English syntax
- [ ] Add missing subjects ("Tree at north-east" → "The tree at the north-east")
- [ ] Add verbs ("called" → "is called")
- [ ] Fix word order to Subject-Verb-Object
- [ ] Complete fragmentary descriptions

---

### 01-02-02-01.txt - Convoluted Syntax
**Priority:** HIGH  
**Lines:** 1099-1200  
**Issues:**
- Extremely dense, convoluted sentences
- Tibetan word order preserved ("That time emanation vajra that mind extremely moved")
- Missing articles throughout
- Run-on sentences without proper punctuation

**Example Problems:**
```
[1102] That time emanation vajra that mind extremely moved,
[1103] From those realms' nature arisen realm that to,
[1104] Some drop-like surpassing cast,
[1105] Upper Sūraṅgama samādhi from lapsed,
```

**Required Fixes:**
- [ ] Rewrite with natural English word order
- [ ] Add articles throughout ("That time" → "At that time")
- [ ] Break run-on sentences into manageable units
- [ ] Add proper punctuation
- [ ] Ensure every sentence has clear subject and verb

---

## CHAPTER 4: Mistaken Tenets

### 01-04-14-01.txt - Blank Lines & Incomplete Sections
**Priority:** HIGH  
**Lines:** 3341-3720  
**Issues:**
- Multiple blank lines disrupting narrative flow (lines 3352-3353, 3383-3385, etc.)
- Fragmentary explanations
- Awkward constructions ("Thus: The great seal free from intellect...")
- Missing content between sections

**Example Problems:**
```
[3352] 
[3353] 
[3354] Wishing for self-liberated realization.
[3355] The clarification of the result is thus:
...
[3471] Thus: The great seal free from intellect, expanse and primordial wisdom, bliss-emptiness—the bodhicitta vehicle.
```

**Required Fixes:**
- [ ] Fill blank lines with proper content from Tibetan
- [ ] Rewrite awkward constructions with flowing prose
- [ ] Add transitions between sections
- [ ] Ensure consistent XML tagging
- [ ] Complete fragmentary explanations

---

### 01-04-16-01.txt - Repetition & Fragmentation
**Priority:** MEDIUM  
**Lines:** 3693-3720  
**Issues:**
- Repetition of content from earlier files (01-04-14-01.txt)
- Telephonic style ("Second mind's aspect exist speaking mind's category.")
- Blank lines disrupting flow

**Example Problems:**
```
[3631] Second mind's aspect exist speaking mind's category.
[3632] That also essence appearance-direction is.
```

**Required Fixes:**
- [ ] Consolidate with 01-04-14-01.txt or differentiate content
- [ ] Add verbs ("exist" → "is explained")
- [ ] Add articles throughout
- [ ] Remove or fill blank lines

---

## CHAPTER 8: Seven Views on the Basis

### 01-08-04-01.txt - Extreme Fragmentation
**Priority:** CRITICAL  
**Lines:** 10722-10728  
**Issues:**
- Only 7 lines in entire file
- Incomplete thought at line 10723: "First, if one asserts like this:"
- Missing all subsequent content

**Example Problems:**
```
[10722] Fourth: the view that holds changeability as the basis.
[10723] First, if one asserts like this:
(End of file - total 7 lines)
```

**Required Fixes:**
- [ ] Expand to complete section (estimated 100+ lines)
- [ ] Cross-reference with Tibetan source (01-08-04-01.txt in text/tibetan/)
- [ ] Add complete exposition of changeability view
- [ ] Ensure continuity with surrounding sections (01-08-03-01.txt and 01-08-05-01.txt)

---

### 01-08-08-01.txt - Incomplete Fragment
**Priority:** CRITICAL  
**Lines:** 11334-11339  
**Issues:**
- Only 6 lines in entire file
- "First." as a complete entry (line 11335)
- Clearly incomplete - should contain view #7 discussion

**Example Problems:**
```
[11334] Seventh: the view that holds multiplicity as the basis.
[11335] First.
(End of file - total 6 lines)
```

**Required Fixes:**
- [ ] Expand to complete section (estimated 100+ lines)
- [ ] Cross-reference with Tibetan source
- [ ] Add complete exposition of multiplicity view
- [ ] Parallel structure with other seven views sections

---

## COMMON ISSUES ACROSS MULTIPLE FILES

### Issue: Missing Articles
**Severity:** MEDIUM  
**Files Affected:** 01-01-03-01.txt, 01-02-02-01.txt, 01-04-16-01.txt
**Pattern:** "From five-family kāya" → "From the five-family kāya"
**Fix:** Systematic article addition pass

### Issue: Telephonic Tibetan Word Order
**Severity:** HIGH  
**Files Affected:** 01-01-03-01.txt, 01-02-01-05.txt, 01-02-02-01.txt
**Pattern:** "Measure making direction equal" → "Making the measure equal in direction"
**Fix:** Complete rewrite with natural English syntax

### Issue: Fragmentary Files (under 10 lines)
**Severity:** CRITICAL  
**Files Affected:** 
- 01-02-01-03.txt (2 lines)
- 01-02-01-04.txt (1 line)
- 01-08-04-01.txt (7 lines)
- 01-08-08-01.txt (6 lines)
**Fix:** Cross-reference with Tibetan sources and expand

### Issue: Blank Lines Disrupting Flow
**Severity:** MEDIUM  
**Files Affected:** 01-04-14-01.txt, 01-04-16-01.txt
**Fix:** Fill with content or remove if structural

### Issue: Inconsistent XML Tagging
**Severity:** MEDIUM  
**Files Affected:** Multiple
**Pattern:** Some lists use `<list>`, some don't
**Fix:** Standardize tagging across all files

---

## MISSING LINES AUDIT (2026-02-11)

**CRITICAL FINDING:** Line count comparison between Tibetan sources and liturgical translations reveals significant missing content across multiple chapters.

### **CHAPTER 1: Missing 59 Lines**
**Tibetan:** 706 lines | **Liturgical:** 647 lines | **Missing:** 59 lines
- 01-01-01-01.txt: Tibetan 194, Liturgical 178 (-16 lines)
- 01-01-02-01.txt: Tibetan 451, Liturgical 413 (-38 lines)
- 01-01-03-01.txt: Tibetan 61, Liturgical 56 (-5 lines)

### **CHAPTER 2: Missing 121 Lines**
**Tibetan:** 1067 lines | **Liturgical:** 946 lines | **Missing:** 121 lines
- 01-02-01-01.txt: Tibetan 281, Liturgical 257 (-24 lines)
- 01-02-01-02.txt: Tibetan 113, Liturgical 105 (-8 lines)
- 01-02-01-05.txt: Tibetan 493, Liturgical 424 (-69 lines)
- 01-02-02-01.txt: Tibetan 43, Liturgical 39 (-4 lines)
- 01-02-02-02.txt: Tibetan 135, Liturgical 119 (-16 lines)

### **CHAPTER 3: Missing 36 Lines**
**Tibetan:** 356 lines | **Liturgical:** 320 lines | **Missing:** 36 lines
- 01-03-01-01.txt: Tibetan 97, Liturgical 89 (-8 lines)
- 01-03-02-01.txt: Tibetan 69, Liturgical 61 (-8 lines)
- 01-03-03-01.txt: Tibetan 190, Liturgical 170 (-20 lines)

### **CHAPTER 4: Status OK (Liturgical has 18 extra lines)**
**Tibetan:** 2490 lines | **Liturgical:** 2508 lines | **Note:** Extra lines may be duplicates or formatting

### **CHAPTER 5: Missing 72 Lines**
**Tibetan:** 2861 lines | **Liturgical:** 2789 lines (excluding temp file) | **Missing:** 72 lines
- 01-05-01-01.txt: Tibetan 119, Liturgical 117 (-2 lines)
- 01-05-02-01.txt: Tibetan 392, Liturgical 375 (-17 lines)
- 01-05-03-01.txt: Tibetan 229, Liturgical 218 (-11 lines)
- 01-05-04-01.txt: Tibetan 1708, Liturgical 1674 (-34 lines)
- 01-05-04-06.txt: Tibetan 363, Liturgical 356 (-7 lines)
- 01-05-05-01.txt: Tibetan 46, Liturgical 45 (-1 line)

### **CHAPTER 8: Status OK (4 extra lines)**
**Tibetan:** 935 lines | **Liturgical:** 939 lines | **Status:** Close enough

### **CHAPTER 9: CRITICAL - Missing 859 Lines**
**Tibetan:** 1277 lines | **Liturgical:** 418 lines | **Missing:** 859 lines (67% missing!)
- 01-09-01-01.txt: **Tibetan 1251, Liturgical 392** (-859 lines)
- 01-09-02-01.txt: Tibetan 26, Liturgical 26 (match)

**URGENT:** Chapter 9 section 1 is severely incomplete. Only 31% translated!

### **CHAPTER 10: Has 124 Extra Lines**
**Tibetan:** 664 lines | **Liturgical:** 788 lines | **Note:** Extra lines may be duplicates

### **CHAPTER 11: Missing 28 Lines**
**Tibetan:** 815 lines | **Liturgical:** 787 lines | **Missing:** 28 lines
- 01-11-01-01.txt: Tibetan 372, Liturgical 358 (-14 lines)
- 01-11-02-01.txt: Tibetan 443, Liturgical 429 (-14 lines)

### **CHAPTER 12: CRITICAL - Missing 1,011 Lines**
**Tibetan:** 2374 lines | **Liturgical:** 1363 lines | **Missing:** 1011 lines (43% missing!)
- 01-12-01-01.txt: Tibetan 765, Liturgical 559 (-206 lines)
- 01-12-02-01.txt: Tibetan 303, Liturgical 210 (-93 lines)
- 01-12-03-01.txt: Tibetan 237, Liturgical 118 (-119 lines)
- 01-12-04-01.txt: Tibetan 399, Liturgical 170 (-229 lines)
- 01-12-05-01.txt: Tibetan 234, Liturgical 122 (-112 lines)
- 01-12-05-02.txt: Tibetan 156, Liturgical 56 (-100 lines)
- 01-12-07-01.txt: Tibetan 271, Liturgical 116 (-155 lines)

**URGENT:** Chapter 12 is severely incomplete. Nearly half the content missing!

### **CHAPTER 13: Missing 432 Lines**
**Tibetan:** 1456 lines | **Liturgical:** 1024 lines | **Missing:** 432 lines
- 01-13-01-01.txt: Tibetan 281, Liturgical 280 (-1 line)
- 01-13-02-01.txt: Tibetan 225, Liturgical 225 (match)
- 01-13-03-01.txt: Tibetan 310, Liturgical 308 (-2 lines)
- 01-13-04-01.txt: Tibetan 105, Liturgical 103 (-2 lines)
- 01-13-05-01.txt: **Tibetan 222, Liturgical 49** (-173 lines)
- 01-13-06-01.txt: **Tibetan 313, Liturgical 59** (-254 lines)

**URGENT:** Sections 5 and 6 severely incomplete!

### **CHAPTER 14: Status OK**
**Tibetan:** 3330 lines | **Liturgical:** 3330 lines | **Status:** Perfect match

### **CHAPTERS 15-17: Missing 57 Lines**
**Tibetan:** 4253 lines | **Liturgical:** 4196 lines | **Missing:** 57 lines
- Various sections need verification

---

## AUDIT SUMMARY

| Chapter | Tibetan | Liturgical | Missing | Status |
|---------|---------|------------|---------|--------|
| 1 | 706 | 647 | 59 lines | ⚠️ Needs work |
| 2 | 1067 | 946 | 121 lines | ⚠️ Needs work |
| 3 | 356 | 320 | 36 lines | ⚠️ Needs work |
| 4 | 2490 | 2508 | -18 lines | ✅ OK (duplicates?) |
| 5 | 2861 | 2789 | 72 lines | ⚠️ Needs work |
| 8 | 935 | 939 | -4 lines | ✅ OK |
| 9 | 1277 | 418 | 859 lines | 🔴 CRITICAL |
| 10 | 664 | 788 | -124 lines | ✅ Check duplicates |
| 11 | 815 | 787 | 28 lines | ⚠️ Needs work |
| 12 | 2374 | 1363 | 1011 lines | 🔴 CRITICAL |
| 13 | 1456 | 1024 | 432 lines | 🔴 CRITICAL |
| 14 | 3330 | 3330 | 0 lines | ✅ Perfect |
| 15-17 | 4253 | 4196 | 57 lines | ⚠️ Verify |
| **TOTAL** | **25,844** | **23,585** | **2,259 lines** | **9% missing** |

**CRITICAL FILES REQUIRING IMMEDIATE ATTENTION:**
1. **01-09-01-01.txt** - Missing 859 lines (67% incomplete)
2. **01-12-04-01.txt** - Missing 229 lines
3. **01-12-01-01.txt** - Missing 206 lines
4. **01-12-05-02.txt** - Missing 100 lines
5. **01-13-06-01.txt** - Missing 254 lines
6. **01-13-05-01.txt** - Missing 173 lines

**TOTAL MISSING:** 2,259 lines across all chapters (approximately 9% of total content)

---

## PRIORITY SUMMARY

### Priority 1 (Critical - Complete First)
1. 01-02-01-03.txt (2 lines) - Expand to full section
2. 01-02-01-04.txt (1 line) - Expand to full section
3. 01-08-04-01.txt (7 lines) - Expand to full section
4. 01-08-08-01.txt (6 lines) - Expand to full section

### Priority 2 (High - Complete Second)
1. 01-01-03-01.txt - Rewrite telephonic Tibetan
2. 01-02-02-01.txt - Fix convoluted syntax
3. 01-04-14-01.txt - Fill blanks, fix fragments
4. 01-02-01-05.txt - Rewrite garbled sections

### Priority 3 (Medium - Complete Third)
1. 01-04-16-01.txt - Consolidate and polish
2. Systematic article addition across all files
3. Standardize XML tagging
4. Remove or fill blank lines

---

## QUALITY CHECKLIST FOR REVISIONS

Before marking any section complete, verify:
- [ ] Every sentence has subject + verb
- [ ] Articles (the, a, an) used properly throughout
- [ ] Natural English word order (not Tibetan)
- [ ] Proper XML tags: `<tantra>`, `<list>`, `<ornament>`
- [ ] No fragmentary lines under 5 words
- [ ] No blank lines unless structural (<ornament>)
- [ ] Technical terms consistent with dictionary.md
- [ ] Vajra Speech cadence maintained
- [ ] 1:1 line mapping preserved
- [ ] Tibetan source verified for accuracy

---

## PROGRESS TRACKING

**Last Updated:** 2026-02-11

| File | Priority | Status | Assigned | Date Complete |
|------|----------|--------|----------|---------------|
| 01-02-01-03.txt | Critical | Not Started | - | - |
| 01-02-01-04.txt | Critical | Not Started | - | - |
| 01-08-04-01.txt | Critical | Not Started | - | - |
| 01-08-08-01.txt | Critical | Not Started | - | - |
| 01-01-03-01.txt | High | Not Started | - | - |
| 01-02-02-01.txt | High | Not Started | - | - |
| 01-04-14-01.txt | High | Partial | - | - |
| 01-02-01-05.txt | High | Not Started | - | - |
| 01-04-16-01.txt | Medium | Not Started | - | - |

---

## NOTES

- All files referenced are in `/home/opencode/MDZOD/1/text/liturgical/`
- Corresponding Tibetan sources are in `/home/opencode/MDZOD/1/text/tibetan/`
- Reference exemplars.md for A++ Gold Standard examples
- Reference dictionary.md for terminology standards

---

*This document is maintained by the translation team. Update as work progresses.*
