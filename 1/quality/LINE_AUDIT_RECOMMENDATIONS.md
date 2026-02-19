# LINE NUMBER AUDIT - REPAIR RECOMMENDATIONS

## EXECUTIVE SUMMARY

**Total Files Audited:** 213 scholar files
**Files with Issues:** 23
**Total Issues:** 130

---

## 🔴 CRITICAL FILES (6 files, 103 issues) - MUST REPAIR

These files reference line numbers that don't exist in the tibetan source.

### Analysis Summary:

| File | Tibetan Max | Out-of-Bounds Ranges | Severity |
|------|-------------|---------------------|----------|
| **01-04-01-01.txt** | 2538 | 30 ranges (2601-4850) | **CRITICAL** |
| **01-14-10-01.txt** | 20146 | 8 ranges (up to 20600) | HIGH |
| **01-14-12-01.txt** | 20284 | 7 ranges (up to 20750) | HIGH |
| **02-25-05-01.txt** | 16718 | 8 ranges (up to 16972) | HIGH |
| **02-18-02-01.txt** | 4400 | 4 ranges (4400-4500) | MEDIUM |
| **01-06-08-01.txt** | 8809 | 2 ranges (8770-8840) | LOW |

### Root Cause:
The scholar files were apparently built assuming larger tibetan sources, or contain synthetic/appended sections not in the original text.

### Repair Strategy:

**For 01-04-01-01.txt:**
- Lines 2401-2538: VALID (keep)
- Lines 2601-3600 (9 four-pillar sets): **TRUNCATE TO 2538**
- Lines 4501-4850 (synthetic sections): **DELETE or RELOCATE to [2523-2538]**

**For other critical files:**
- Simple fix: Change end ranges to match tibetan max
- Example: [16650-16800] → [16650-16718] (for 02-25-05-01.txt)

---

## 🟠 MAJOR FILES (17 files, 27 issues) - NO ACTION REQUIRED

**RECOMMENDATION: These are NOT errors - they are INTENTIONAL.**

### Pattern Analysis:

All "sequentiality issues" are actually **CORRECT BY DESIGN**. Examples:

**01-04-08-01.txt:**
```
[2989-2999] <context>      ← First analysis
[2989-2993] <philology>    ← Same lines, different pillar
[2995-2998]                ← Subset analysis
[2999] <structure>         ← Specific line
[3000-3016] <concept>      ← Next section
[3000-3016] <structure>    ← Same lines, different pillar
```

**01-06-04-01.txt:**
```
[8138-8169] <structure>     ← Lines 8138-8169
[8170-8217] <philology>     ← Lines 8170-8217 (sequential ✓)
...
[8362-8368] <structure>     ← Lines 8362-8368
[8553-8625] <philology>     ← Lines 8553-8625 (sequential ✓)
[8573-8625] <concept>       ← Lines 8573-8625 (overlaps previous - CORRECT)
```

### Why This is Correct:

The scholar layer uses **Four Pillars** architecture:
1. **`<structure>`** - Organizational framework
2. **`<philology>`** - Linguistic/terminological analysis
3. **`<context>`** - Doctrinal/historical background
4. **`<concept>`** - Philosophical content

Each pillar can independently analyze the same line ranges. This allows:
- Multiple analytical perspectives
- Overlapping coverage for complex passages
- Independent reading paths

**The "non-sequential" pattern is INTENTIONAL and SHOULD NOT BE CHANGED.**

---

## RECOMMENDED ACTIONS

### Immediate Priority:
1. **Repair 6 CRITICAL files** - Fix out-of-bounds ranges
2. **Leave 17 MAJOR files unchanged** - Sequentiality is by design

### Repair Method:
- Truncate end ranges to match tibetan file max
- For synthetic sections (like 01-04-01-01.txt's 4501-4850), either:
  - Delete if truly synthetic
  - Reassign to valid line range if content maps to actual text

### Verification:
After repair, re-run audit to confirm:
- 0 critical issues
- 0 consistency issues
- 27 intentional sequentiality patterns (acceptable)

---

## DETAILED FILE-BY-FILE REPAIR PLAN

### 01-04-01-01.txt (MOST CRITICAL)
**Tibetan:** Lines 1902-2538 (637 lines)
**Problem:** Scholar references lines up to 4850
**Repair:** 
- Truncate 30 ranges ending at 2600-3600 → end at 2538
- Remove or relocate 2 synthetic sections (4501-4700, 4701-4850)

### 01-06-08-01.txt (MINOR)
**Tibetan:** Lines 8770-8809 (40 lines)
**Problem:** 2 ranges go to 8840
**Repair:** Change [8770-8840] → [8770-8809]

### 01-14-10-01.txt (HIGH)
**Tibetan:** Lines 19975-20146 (172 lines)
**Problem:** 8 ranges go to 20600
**Repair:** Truncate all to max 20146

### 01-14-12-01.txt (HIGH)
**Tibetan:** Lines 20212-20284 (73 lines)
**Problem:** 7 ranges go to 20750
**Repair:** Truncate all to max 20284

### 02-18-02-01.txt (MEDIUM)
**Tibetan:** Lines 4156-4400 (245 lines)
**Problem:** 4 ranges go to 4500
**Repair:** Change [4400-4500] → [4400-4400] or delete

### 02-25-05-01.txt (HIGH)
**Tibetan:** Lines 16436-16718 (283 lines)
**Problem:** 8 ranges go to 16972
**Repair:** Truncate all to max 16718

---

## CONCLUSION

- **6 CRITICAL files need repair** (out-of-bounds)
- **17 MAJOR files are correct** (intentional sequentiality)
- **190 files are perfect** (no issues)

The scholar layer is architecturally sound. The issues are data quality problems in specific files, not systemic errors.
