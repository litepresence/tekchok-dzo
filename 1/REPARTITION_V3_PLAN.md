# Repartition v3 - Implementation Plan

## Tools Built

### 1. 02_extract_content_v3.py - FIXED EXTRACTION ENGINE
**Key Improvements:**
- **Boundary Overlap Fix**: Respects `end_line` even on pages before `end_page`
  - Fixes Ch 10 B→C overlap where section B extracted lines belonging to C
  - Checks if intermediate pages extend beyond `end_line` and stops accordingly

- **Liturgical Line Mapping (Option B)**: 
  - Dynamically maps liturgical lines to Tibetan line numbers during extraction
  - Reads corresponding Tibetan page to get proper line numbers
  - Assigns line numbers to liturgical lines that lack them in source
  - No modification to source files required

- **Range Format Handling**:
  - Parses `[start-end]` format for commentary layers
  - Uses LAST number in range for boundary calculations (per requirement)
  - Preserves range format in output: `[1-4] content` (no zero padding)
  - Handles scholar layer's `[001-004]` → normalizes to `[1-4]`

- **No Zero Padding on Line Numbers**:
  - Line numbers: `[1]`, `[4417]`, `[1-4]` (no padding)
  - FOLIO markers: `FOLIO_001`, `FOLIO_010` (3-digit padding preserved)

- **FOLIO Marker Placement**:
  - Tibetan layer only
  - `FOLIO_001` at Volume 1 start
  - Page transitions within multi-page sections get FOLIO markers
  - Blank lines above and below each FOLIO

### 2. 03_verify_migration_v3.py - COMPREHENSIVE VERIFICATION
**Validates:**
- All layers have proper content (not empty where they shouldn't be)
- Line number continuity (gaps and overlaps reported)
- Correct format for each layer type
- FOLIO markers only in Tibetan layer
- 3-digit padding on FOLIO markers
- No zero padding on line numbers

### 3. test_extraction_fixes.py - VALIDATION SUITE
**Tests:**
- Overlap fix (Ch 10 B should not include lines 19354-19356)
- Liturgical line number mapping
- Commentary range format preservation
- FOLIO marker format

## Issues Fixed from v2

| Issue | Root Cause | Fix |
|-------|-----------|-----|
| Boundary overlaps | Extracted past end_line on pages before end_page | Check all pages against end_line boundary |
| Liturgical gaps | ~100+ source files lacked line numbers | Map to Tibetan line numbers dynamically |
| Empty commentary files | Range format [1-4] not parsed | Parse ranges and use last number |
| Zero padding | Inconsistent formatting | Enforce no padding on lines, 3-digit on FOLIO |

## Pre-Flight Checklist

Before running full repartition:
- [ ] Clear old partitioned_v1/ and partitioned_v2/ directories
- [ ] Run directory creation: ./01_create_structure.sh
- [ ] Run extraction: ./02_extract_content_v3.py
- [ ] Run validation: ./test_extraction_fixes.py
- [ ] Run verification: ./03_verify_migration_v3.py
- [ ] Review gap/overlap reports
- [ ] Approve for final rebuild

## Expected Results

**File Sizes (approximate):**
- Tibetan: ~5,244 KB (larger due to FOLIO + preserved line numbers)
- Wylie: ~2,488 KB (with line numbers)
- Literal: ~2,476 KB (with line numbers)
- Liturgical: ~2,480 KB (with mapped line numbers)
- Commentary: ~4,800 KB (with ranges, minimal empty files)
- Other layers: Similar to commentary

**Continuity:**
- Tibetan/Wylie/Literal/Liturgical: 100% continuous
- Commentary layers: Range format, continuous where source exists

**Quality Metrics:**
- 0 boundary overlaps
- Minimal gaps (only where source data genuinely missing)
- All layers have substantial content
- Proper format compliance
