# PROMPT: RAW LAYER
# Theg mchog rin po che'i mdzod

**Layer:** 1 of 12
**Type:** Archive/Source (Non-Generated)
**Status:** Immutable Archive

---

## PURPOSE

The Raw Layer contains the original BDRC (Buddhist Digital Resource Center) source files. This is the **immutable foundation** from which all processing begins.

---

## SOURCE FILES

Two raw files from BDRC:
1. **UT22920_005_0001_bo,sa,zh.txt** - Volume 1 (lines 1-20,425)
2. **UT22920_005_0002_bo,sa,zh.txt** - Volume 2 (lines 1-17,330)

### BDRC Metadata
- **BDRC Work ID:** bdr:MW22920_365376
- **Access Date:** February 1, 2026
- **URL:** https://library.bdrc.io/show/bdr:MW22920_365376
- **Quality:** "BEST QUALITY / KHENPO REVIEWED"
- **Format:** Unicode Tibetan text with BDRC metadata

---

## CONTENT ANALYSIS

**Volume 1:**
- Total characters: 717,939 Tibetan characters
- Content: Longchenpa's original text

**Volume 2:**
- Total characters: 634,678 Tibetan characters
- Note: 18,604 characters are appended commentary by Paltrul Rinpoche (lines 833-857)
- Clean Longchenpa text: 616,074 characters

**Combined:**
- Total Longchenpa text: 1,334,013 Tibetan characters

---

## PROCESSING NOTES

Raw files contain:
- Tibetan Unicode text in BDRC format
- Line numbers derived from space and non-breaking space (\u00A0) separation
- Pages derived from double line break (\n\n) separation
- BDRC metadata and headers preserved
- Volume 2 includes appended commentary by Paltrul Rinpoche (excluded from clean source)

---

## PROTOCOL

**NEVER MODIFY** the Raw layer. This is the original import archive.

Processing chain:
1. Raw (this layer) - Original import
2. Artifacts - OCR processing with PAGE markers
3. Tibetan - Clean source (production layer)

---

## LOCATION

`text/raw/UT22920_005_0001_bo,sa,zh.txt`
`text/raw/UT22920_005_0002_bo,sa,zh.txt`

---

**Status:** Archive complete
**Next:** Process to Artifacts layer
