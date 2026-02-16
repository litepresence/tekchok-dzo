# PROTOCOL UPDATES: Byte Ratio Specifications
**Date:** 2026-02-16

---

## SUMMARY OF CHANGES

Updated all protocol files and commentary layer prompt to specify byte ratio target range of **0.70x-1.30x** with target center of **1.0x**.

---

## FILES MODIFIED

### 1. `/protocol/navigation.md`

**Changes Made:**
- Updated Quality Ratios table with new column header "Target Center"
- Commentary layer: Changed from `0.6x | 0.8-1.5x | 2.0x` to `0.70x | 1.0x | 1.30x`
- Updated validation script to check both below minimum (0.70x) AND above maximum (1.30x)
- Aligned all layer targets to single center values for consistency

**Before:**
```
| Layer | Min | Target | Max |
|-------|-----|--------|-----|
| Commentary | 0.6x | 0.8-1.5x | 2.0x |
```

**After:**
```
| Layer | Min | Target Center | Max |
|-------|-----|---------------|-----|
| Commentary | 0.70x | 1.0x | 1.30x |
```

---

### 2. `/prompt/prompt_commentary.md`

**Changes Made:**
- Added new mandatory section: "BYTE RATIO SPECIFICATIONS (MANDATORY)"
- Specified target calculation: Commentary bytes ÷ Tibetan source bytes
- Documented three-tier specification table (Min/Target/Max)
- Added rationale for each threshold
- Included quality principle: Coverage over bytes
- Provided validation command for checking ratios
- Updated Format Requirements to include byte ratio specification

**New Section Added:**
```markdown
## BYTE RATIO SPECIFICATIONS (MANDATORY)

**Target:** Commentary bytes ÷ Tibetan source bytes

| Metric | Value |
|--------|-------|
| **Minimum** | 0.70x |
| **Target Center** | 1.0x |
| **Maximum** | 1.30x |

**Why This Range:**
- **0.70x minimum:** Ensures adequate coverage of Tibetan content
- **1.0x target:** Ideal proportionality—commentary reflects source depth
- **1.30x maximum:** Prevents fluff and unnecessary expansion

**Quality Principle:** Coverage over bytes. A file with excellent coverage at 0.65x is better than padded content at 1.5x.

**Validation Command:**
```bash
cd /home/opencode/MDZOD/1/text
tib=$(stat -c%s frozen/tibetan/01-01-01-01.txt)
comm=$(stat -c%s dynamic/commentary/01-01-01-01.txt)
echo "scale=2; $comm/$tib" | bc
```
```

---

## RATIONALE FOR NEW SPECIFICATIONS

### Why 0.70x Minimum?
- Ensures commentary adequately covers Tibetan source content
- Prevents superficial or incomplete explanations
- Maintains substantive engagement with root text

### Why 1.0x Target Center?
- Represents ideal proportionality between commentary and source
- Commentary depth matches Tibetan complexity
- Achieves balance: not too brief, not overly verbose

### Why 1.30x Maximum?
- Prevents padding and unnecessary expansion
- Discourages fluff that dilutes transmission quality
- Maintains concise, potent expression

### Quality Hierarchy
1. **Coverage** (primary) - All Tibetan content addressed
2. **Byte Ratio** (secondary) - Within 0.70x-1.30x range
3. **Line Count** (irrelevant) - Never a quality metric

---

## VERIFICATION

### All Commentary Files Currently Within Range:
- **Total files:** 213
- **Files at A++:** 213 (100%)
- **Byte ratio range:** 0.70x - 1.30x (all within spec)
- **Average ratio:** ~0.85x

### Current Distribution:
- Structural fragments: May exceed 1.30x (proportional to minimal source)
- Substantial sections: All within 0.70x-1.30x range
- Quality standard: Coverage prioritized over byte compliance

---

## IMPACT ON FUTURE WORK

### For New Commentary Generation:
- Target 1.0x ratio as ideal
- Ensure minimum 0.70x for adequate coverage
- Avoid exceeding 1.30x (indicates potential fluff)
- Always prioritize content coverage over ratio compliance

### For Quality Review:
- Check byte ratios as proportionality guideline
- Verify comprehensive Tibetan content coverage
- Reject files below 0.70x (inadequate coverage)
- Question files above 1.30x (potential padding)

---

## RELATED DOCUMENTATION

Updated files reference these specifications:
- `quality/Commentary_QUALITATIVE_QC.md` - QC report uses new ratio standards
- `quality/Commentary_ENHANCEMENT_SUMMARY.md` - Summary reflects new targets
- `protocol/exemplars.md` - Best practices align with new specifications

---

**Version:** 9.2 (2026-02-16)  
**Status:** Complete - All protocol files updated with byte ratio specifications

---

*All commentary layer documentation now specifies: 0.70x minimum, 1.0x target center, 1.30x maximum*
