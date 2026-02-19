# FULL SURGICAL REMEDIATION PLAN
## Option A: Complete AI;DR and Line Range Repair

**Scope:** All 1,465 text files across all layers
**Duration:** 4-6 hours
**Goal:** 0 AI-tells, 100% valid line ranges, 0 empty sections

---

## PHASE 1: CRITICAL AI-TELL REMOVAL (90 min)

### 1.1 "Hide-and-Seek" Formula Excision
**Target:** 106 files with exact phrase:
> "What is called delusion here is wisdom's play of hide-and-seek, spontaneously self-liberating."

**Action:** Complete removal - this adds no doctrinal value
**Verification:** grep -r "hide-and-seek" must return 0 results

### 1.2 Hallucinated Attribution Removal
**Target:** 36 files
- "A practitioner" → Remove
- "An old vagabond" → Remove  
- "Hence. The structure." → Remove
- "Voice [0-9]+ proclaims" → Already removed, verify gone

### 1.3 Spiritual Cliché Cleanup
**Target:** 102 files
- "never absent" → Remove when used as cliché
- "never left" → Remove when used as cliché
- "space between thoughts" → Remove
- "already complete" → Remove when used as cliché

**Preservation:** Keep if part of valid technical analysis

---

## PHASE 2: LINE RANGE REPAIR (90 min)

### 2.1 Duplicate Range Consolidation
**Target:** 10,246 duplicate ranges
**Action:** 
- Keep first occurrence
- Remove subsequent duplicates
- Merge content if different

**Priority:** frozen/epistemic/ line 7 duplicates first

### 2.2 Non-Sequential Range Reordering
**Target:** 1,140 non-sequential ranges
**Action:**
- Sort ranges by start line
- Commentary may intentionally overlap - flag for review
- Verify no content loss during reorder

### 2.3 Invalid Boundary Repair
**Target:** 64 ranges with end < start
**Action:**
- Check for typos (swapped digits)
- Verify against liturgical source
- Correct or remove invalid ranges

---

## PHASE 3: EMPTY SECTION POPULATION (60 min)

### 3.1 Critical Empty Sections
**Target:** 57 empty/short sections
**Priority files:**
- commentary/01-05-04-01.txt (32 sections)
- commentary/01-14-05-01.txt (10 sections)
- commentary/01-02-01-05.txt (5 sections)

### 3.2 Population Method
For each empty [start-end]:
1. Extract corresponding lines from liturgical layer
2. Generate concise cognitive note (20-100 words)
3. Include: structural function, view register, key Tibetan terms
4. Maintain metaphysical precision

### 3.3 Placeholder Removal
**Target:** 79 files with "Structural function: Textual exposition..."
**Action:** Either populate with liturgical content or remove section

---

## PHASE 4: BYTE-LEVEL VERIFICATION (30 min)

### 4.1 Pre-Repair Snapshots
Before any changes:
- Record total bytes per file
- Create git commit point
- Document current state

### 4.2 Per-File Accountability
For each file modified:
- Record bytes before
- Record bytes after
- Verify: Content removed = AI artifacts only
- Verify: No doctrinal content lost

### 4.3 Aggregate Verification
- Total bytes before remediation
- Total bytes after remediation
- Expected: -50KB to -100KB (AI slop removal)
- Unacceptable: >200KB loss (doctrinal content lost)

---

## PHASE 5: FINAL VALIDATION (30 min)

### 5.1 Zero AI-Tell Verification
```bash
grep -r "hide-and-seek" /home/opencode/MDZOD/1/text/ | wc -l  # Must be 0
grep -r "Hence\. The structure" /home/opencode/MDZOD/1/text/ | wc -l  # Must be 0
grep -r "space between thoughts" /home/opencode/MDZOD/1/text/ | wc -l  # Must be 0
```

### 5.2 Line Range Validation
```bash
# Run line range validator
python3 /tmp/validate_all_ranges.py
# Expected: 0 errors
```

### 5.3 Content Quality Sampling
- Random sample 50 files
- Verify no empty sections
- Verify Tibetan terms preserved
- Verify metaphysical precision

---

## CHECKPOINTS & SAFETY

### Checkpoint 1: Post AI-Tell Removal
- Verify 280+ files cleaned
- Byte delta check
- Spot check 10 files

### Checkpoint 2: Post Line Range Repair
- Verify sequential ranges
- No duplicate markers
- Content integrity check

### Checkpoint 3: Post Empty Section Population
- All sections have content
- Liturgical alignment verified
- Byte count reasonable

### Checkpoint 4: Final Verification
- All grep scans return 0
- All line ranges valid
- Sample files A++ quality

---

## DELEGATION STRATEGY

### Agent 1: AI-Tell Hunter
**Scope:** commentary/, delusion/, scholar/
**Task:** Remove all identified AI-tell patterns
**Verification:** Must achieve 0 hits on all patterns

### Agent 2: Line Range Surgeon
**Scope:** All layers
**Task:** Fix 10,246 duplicates, 1,140 non-sequential, 64 invalid
**Verification:** 100% valid ranges

### Agent 3: Empty Section Populator
**Scope:** 57 empty sections
**Task:** Populate from liturgical or remove
**Verification:** 0 empty sections remaining

### Agent 4: Byte Auditor
**Scope:** All files
**Task:** Track bytes before/after, verify no data loss
**Verification:** Aggregate report showing healthy compression

---

## SUCCESS CRITERIA

✅ **AI-Tells:** 0 remaining across all 1,465 files
✅ **Line Ranges:** 100% valid (sequential, unique, proper boundaries)
✅ **Empty Sections:** 0 remaining
✅ **Bytes:** -50KB to -100KB (AI slop removed, content preserved)
✅ **Tibetan Terms:** 100% preserved (rang bzhin, ye shes, rig pa, etc.)
✅ **Metaphysical Precision:** All doctrinal analysis intact

---

## RISK MITIGATION

### Risk: Accidental Content Removal
**Mitigation:** 
- Only remove exact match phrases
- Never remove Tibetan technical terms
- Review all removals >100 bytes

### Risk: Line Range Corruption
**Mitigation:**
- Validate after every 50 files
- Automated boundary checking
- Rollback capability via git

### Risk: Timeout/Interruption
**Mitigation:**
- Phase-based checkpoints
- Can resume from any checkpoint
- Progress saved to reports/

---

## ESTIMATED TIMELINE

- Phase 1 (AI-Tells): 90 min
- Phase 2 (Line Ranges): 90 min  
- Phase 3 (Empty Sections): 60 min
- Phase 4 (Byte Verification): 30 min
- Phase 5 (Final Validation): 30 min
- **Total: 5 hours**

---

## APPROVAL REQUIRED

This plan will modify:
- ~400 files for AI-tell removal
- ~684 files for line range repair
- ~57 sections for population

**Total impact: ~1,141 files modified**

Ready to execute upon your approval.
