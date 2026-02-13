# PROMPT: ARTIFACTS LAYER
# Theg mchog rin po che'i mdzod

**Layer:** 2 of 12
**Type:** Processing Layer (Non-Generated)
**Status:** Archive - Reference Only

---

## PURPOSE

The Artifacts Layer represents the OCR (Optical Character Recognition) output with PAGE markers preserved. This is an **intermediate processing stage** between Raw and clean Tibetan.

---

## PROCESSING

### From Raw to Artifacts:
1. Convert double line breaks (\n\n) → PAGE markers (`### PAGE X`)
2. Convert spaces → numbered lines
3. Preserve all OCR artifacts and formatting
4. Break into section files per contents.md

### Structure
- **PAGE Numbering:** Physical page markers from OCR scanning
  - Note: Page numbering restarts at Volume 2 boundary
- **Line Numbering:** Implicit via spacing
- **Format:** Original with all markers preserved

---

## CONTENT

**Total:** 1,334,013 Tibetan characters (identical to Tibetan layer)

**Format includes:**
- `### PAGE X` markers
- Blank lines preserved
- Original OCR structure
- Section breaks per contents.md

---

## DUAL SOURCE SYSTEM

| Directory | Contents | Use Case |
|-----------|----------|----------|
| `text/tibetan/` | **CLEAN** - No PAGE markers, no blank lines | **PRIMARY SOURCE** |
| `text/artifacts/` | Original with PAGE markers | Reference/archive only |
| `text/raw/` | BDRC import (includes unrelated Patrul text) | Original import archive |

**Always use:** `text/tibetan/` for all translation work
**Reference only:** `text/artifacts/` for understanding original OCR structure

---

## PROTOCOL

**Do not modify.** This is a processing archive.

**Chain:**
- Raw → Artifacts (this layer) → Tibetan (clean)

---

## LOCATION

`text/artifacts/01-01-01-01.txt` through `text/artifacts/02-25-XX-XX.txt`

---

**Status:** Processing complete
**Next:** Use Tibetan layer (clean source) for all work
