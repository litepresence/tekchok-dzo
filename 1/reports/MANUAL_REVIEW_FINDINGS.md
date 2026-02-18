# MANUAL REVIEW FINDINGS - LINE NUMBER RESTORATION

## Date: 2026-02-18
## Reviewer: AI Assistant
## Scope: Cognitive and Epistemic Layers

---

## EXECUTIVE SUMMARY

**CRITICAL FINDING:** The automated restoration has significant issues. The dynamic/ versions have been substantially enhanced and expanded compared to frozen/ versions, making automated line number mapping unreliable.

**Impact:**
- **Cognitive:** 71% success rate (109 files with UNMAPPED blocks)
- **Epistemic:** 28% success rate (100% of files have UNMAPPED blocks)
- **Root Cause:** Content divergence between frozen/ and dynamic/ versions

---

## DETAILED FINDINGS

### 1. EPISTEMIC LAYER - CRITICAL ISSUES

**Sample File:** 01-01-01-01.txt

**Problem:** 
- Dynamic version has 30+ detailed classification blocks
- Frozen version has 22 blocks with different content structure
- Content is completely reorganized and expanded
- Automated mapper failed to match any blocks

**Frozen Version Structure:**
```
[1-4] - Title protocol (condensed)
[5-15] - Homage encoding (condensed)
[16-19] - Ground characterization (condensed)
[20-27] - Vehicle hierarchy (condensed)
...
[52-56] - Samantabhadra's emanations
```

**Dynamic Version Structure:**
```
[UNMAPPED] - Title protocol (expanded with view/pedagogy/risk tags)
[UNMAPPED] - Homage encoding (expanded)
[UNMAPPED] - Ground characterization (expanded)
[UNMAPPED] - Vehicle hierarchy (expanded)
...
[52-56] - Samantabhadra's emanations (only matching block)
[UNMAPPED] - Extended content not in frozen
```

**Issue:** The dynamic version uses XML-style tagging:
```xml
<view>atiyoga-recognition
<pedagogy>assertive-completion
<risk>substantialization
<classification> [detailed text]
```

While frozen version is more condensed without this structure.

**Verdict:** The epistemic layer content was completely rewritten between frozen and dynamic versions. Line numbers cannot be reliably mapped.

---

### 2. COGNITIVE LAYER - MODERATE ISSUES

**Sample File:** 02-22-01-01.txt (Bardo chapter)

**Problem:**
- Frozen version: ~20 concise blocks
- Dynamic version: 60+ expanded paragraphs
- Content in dynamic is 3x longer with extensive elaboration
- Only early blocks matched; later content is completely new

**Frozen Version (20 blocks):**
```
[10211-10230] - Bardo liberation signs introduction
[10231-10250] - Sign sequence citation
[10251-10270] - Physical marks detailed
...
[10471-10500] - Final recognition
```

**Dynamic Version (60+ paragraphs):**
```
[10211-10230] - Bardo liberation signs introduction (MATCHED)
[10231-10250] - Sign sequence citation (MATCHED)
...
[UNMAPPED] - Extended body marks coverage (NEW CONTENT)
[UNMAPPED] - Extended speech signs coverage (NEW CONTENT)
[UNMAPPED] - Extended mind signs coverage (NEW CONTENT)
[UNMAPPED] - Recognition mechanics (NEW CONTENT)
[UNMAPPED] - Certainty establishment (NEW CONTENT)
...
[UNMAPPED] - Comprehensive extended analysis (VERY LONG NEW CONTENT)
[UNMAPPED] - Final comprehensive summary (NEW CONTENT)
[UNMAPPED] - Ultimate definitive comprehensive coverage (NEW CONTENT)
```

**Issue:** Dynamic version has extensive "extended coverage" paragraphs not present in frozen. The content was expanded for completeness but line numbers were lost.

**Verdict:** Early blocks match, but later blocks (especially Ch 17-25) are significantly expanded and need manual line number assignment.

---

### 3. ROOT CAUSE ANALYSIS

**What Happened:**
1. Original content created in dynamic/ WITH line numbers
2. Content enhanced and expanded (more detail, better quality)
3. During "AI-tells" cleanup, line numbers were removed as "artifacts"
4. Frozen/ directory was a snapshot BEFORE the enhancements
5. Now we have:
   - Frozen/: Old content WITH line numbers
   - Dynamic/: New content WITHOUT line numbers

**Why Automated Mapping Failed:**
- Content is not just reorganized—it's completely rewritten
- New paragraphs added that don't exist in frozen
- Structure changed (epistemic especially)
- Simple text matching can't bridge the gap

---

## IMPACT ASSESSMENT

### Files by Category:

**Category A: Well-Mapped (Can Keep)**
- Cognitive: ~150 files with good mapping
- Epistemic: ~0 files (epistemic is mostly broken)

**Category B: Partially-Mapped (Needs Review)**
- Cognitive: ~63 files with some UNMAPPED blocks
- Epistemic: All 213 files

**Category C: Critical Sections (Must Fix)**
- All Volume 2 files (Ch 17-25) - safety-critical
- Chapter 19 (Trekcho), 22-23 (Bardo/Phowa)
- These have most expansion and need accurate line numbers

---

## REPAIR OPTIONS

### OPTION 1: Use Frozen/ Content (Conservative)
**Approach:** Replace dynamic/ content with frozen/ content

**Pros:**
- ✅ Perfect line numbers
- ✅ Consistent with Tibetan source
- ✅ Quick to implement

**Cons:**
- ❌ Loses all content enhancements
- ❌ Loses detailed analysis in epistemic layer
- ❌ Loses extended coverage in cognitive layer
- ❌ Lower quality content overall

**Recommended For:** Non-critical sections where content quality is less important than line number accuracy

---

### OPTION 2: Manual Line Number Assignment (Thorough)
**Approach:** Manually assign line numbers to dynamic/ content based on Tibetan source

**Pros:**
- ✅ Keeps all content enhancements
- ✅ Maintains high quality
- ✅ Line numbers will be accurate

**Cons:**
- ❌ Very time-consuming (639 files × ~10 blocks each = ~6,390 manual assignments)
- ❌ Requires reference to Tibetan source
- ❌ Risk of human error

**Recommended For:** Critical sections (Ch 17-25) where content quality is essential

---

### OPTION 3: Hybrid Approach (Balanced) **RECOMMENDED**
**Approach:** 
1. **For Chapters 1-14 (Volume 1):** Use frozen/ content (less critical)
2. **For Chapters 17-25 (Volume 2):** Manual line number assignment (safety-critical)
3. **For partially-mapped files:** Review case-by-case

**Pros:**
- ✅ Balances quality and accuracy
- ✅ Focuses effort on critical sections
- ✅ Maintains high quality where needed

**Cons:**
- ❌ Still requires significant manual work for Volume 2
- ❌ Less quality in Volume 1

**Implementation:**
1. Copy frozen/ to final/ for Ch 1-14
2. Manually restore line numbers for Ch 17-25
3. Review and fix any critical gaps

---

### OPTION 4: Proportional Assignment (Fast)
**Approach:** Assign line numbers proportionally based on Tibetan file size

**Method:**
1. Calculate total lines in Tibetan file
2. Divide by number of blocks in dynamic content
3. Assign proportional ranges

**Example:**
- Tibetan file: 1,000 lines
- Dynamic content: 10 blocks
- Each block gets ~100 lines: [1-100], [101-200], etc.

**Pros:**
- ✅ Very fast (fully automated)
- ✅ Roughly accurate
- ✅ No content loss

**Cons:**
- ❌ Not precise (line numbers approximate)
- ❌ May not align with actual content
- ❌ Unacceptable for scholarly accuracy

**Recommended For:** Draft/testing only, not production

---

## RECOMMENDATIONS

### Immediate Actions:

1. **REJECT current automated restoration for epistemic layer**
   - 28% success is unacceptable
   - All files need rework

2. **PARTIALLY ACCEPT cognitive layer restoration**
   - Keep well-mapped files (71%)
   - Flag files with >3 UNMAPPED blocks for manual review

3. **PRIORitize Volume 2 (Ch 17-25)**
   - These are safety-critical
   - Require accurate line numbers
   - Should use Option 2 (manual) or frozen/

### Suggested Workflow:

**Phase 1: Critical Sections (Ch 17-25)**
- Use frozen/ content OR manual line number assignment
- Priority: Delusion > Commentary > Scholar > Cognitive > Epistemic
- Focus on bardo (Ch 19, 22-23) and completion stage (Ch 18)

**Phase 2: Volume 1 (Ch 1-14)**
- Use frozen/ content for simplicity
- Or accept automated restoration with review
- Less critical for safety

**Phase 3: Quality Assurance**
- Spot-check 10% of files
- Verify line number alignment with Tibetan
- Check for missing content

---

## FILES REQUIRING IMMEDIATE ATTENTION

### Critical Files (Must Fix):
- All Ch 17-25 files in commentary, delusion, scholar layers
- Specifically: 02-17-*, 02-18-*, 02-19-*, 02-20-*, 02-22-*, 02-23-*

### High-Priority Files (Should Fix):
- Cognitive files with >10 UNMAPPED blocks
- Epistemic files (all 213 need rework)

### Medium-Priority Files (Can Review Later):
- Cognitive files with 1-5 UNMAPPED blocks
- Volume 1 files (Ch 1-14)

---

## ESTIMATED EFFORT

**Option 1 (Use Frozen):** 4-6 hours (copy files)
**Option 2 (Manual):** 40-60 hours (639 files × 5-10 min each)
**Option 3 (Hybrid):** 20-30 hours (manual for Ch 17-25, frozen for Ch 1-14)
**Option 4 (Proportional):** 1-2 hours (automated)

**Recommendation:** Option 3 (Hybrid) for best balance of quality and effort.

---

## NEXT STEPS

1. **Decision needed:** Which option to pursue?
2. **If Option 3:** 
   - Identify which Volume 2 files need manual work
   - Start with most critical (Ch 22-23 Bardo/Phowa)
3. **Verification:** Spot-check restored files
4. **Documentation:** Update status report

---

*Review completed. Awaiting decision on repair approach.*
