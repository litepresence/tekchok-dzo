# NAVIGATION: Theg mchog rin po che'i mdzod

**Project:** 12-layer Dzogchen translation (213 sections, 2 volumes)  
**Format:** `text/` folder - Section-based (VV-CC-SS-SS.txt)  

---

## Directory Structure

```
text/
├── frozen/              # Immutable (READ ONLY)
│   ├── tibetan/        # Source: 213 files
│   ├── wylie/          # Transliteration: 213 files
│   ├── literal/        # 1:1 mapping: 213 files
│   ├── liturgical/     # Vajra speech: 213 files
│   ├── meter/         # PROSE/VERSE/ORNAMENTAL
│   └── conventions/   # Editorial
├── dynamic/            # Mutable (WORK HERE)
│   ├── commentary/    # Heart instruction: 213 files
│   ├── scholar/       # Four Pillars: 213 files
│   ├── epistemic/     # View stratification: 213 files
│   ├── delusion/      # Error detection: 213 files
│   └── cognitive/     # Translator log: 213 files
```

**Section ID:** `VV-CC-SS-SS` (Volume-Chapter-Section-Subsection)
- `01-01-01-01` = Vol1, Ch1, Sec1, Subsec1
- `02-18-05-01` = Vol2, Ch18, Sec5, Subsec1

---

## Quality Ratios (MANDATORY - BYTE-BASED)

**Measure:** Dynamic layer bytes ÷ Tibetan source bytes

Reference: `quality/byte_ratio_table.md` (all 213 sections)

| Layer | Min | Target Center | Max |
|-------|-----|---------------|-----|
| Commentary | 0.70x | 1.0x | 1.30x |
| Scholar | 1.0x | 2.0x | 4.0x |
| Delusion | 0.7x | 1.5x | 3.0x |
| Epistemic | 0.3x | 0.75x | 1.5x |

**Why Bytes, Not Lines:**
- Line counts vary with formatting
- Bytes reflect actual content density
- Small files have extreme line-ratio distortions

**Validation (byte-based):**
```bash
cd /home/opencode/MDZOD/1/text
for f in frozen/tibetan/*.txt; do
  s=$(basename $f .txt)
  tib=$(stat -c%s $f)
  comm=$(stat -c%s dynamic/commentary/$s.txt 2>/dev/null || echo 0)
  ratio=$(echo "scale=2; $comm/$tib" | bc 2>/dev/null || echo 0)
  [ "$ratio" != "0" ] && [ $(echo "$ratio < 0.70" | bc) -eq 1 ] && echo "$s: $ratio (BELOW MIN)"
  [ "$ratio" != "0" ] && [ $(echo "$ratio > 1.30" | bc) -eq 1 ] && echo "$s: $ratio (ABOVE MAX)"
done
```

---

## Key Files

| File | Purpose |
|------|---------|
| `protocol/khenpo.md` | Quality review standards |
| `protocol/status.md` | Current metrics, priorities |
| `protocol/exemplars.md` | Best-practice examples |
| `prompt/prompt_*.md` | Layer-specific guidance |
| `contents/boundary.json` | Section boundaries |

---

## Workflow

1. **Read** `protocol/status.md` for current priorities
2. **Read** `prompt/prompt_[layer].md` for guidance
3. **Read** Tibetan source: `text/frozen/tibetan/VV-CC-SS-SS.txt`
4. **Check** ratios after editing
5. **Reference** exemplars in `protocol/exemplars.md`

---

## 1:1 Line Mapping (LITURGICAL)

**NEVER add/remove lines** - breaks Tibetan alignment.

**Fix breathless lines with punctuation:**
```
❌ WRONG:
[46] <prose> Part one,
[47] <prose> Part two...

✅ CORRECT:
[46] <prose> Part one; part two...
```

---

## Current Priority

**First 4 Sections Status (Byte Ratios):**

| Section | Tib Bytes | Commentary | Byte Ratio | Action |
|---------|-----------|------------|------------|--------|
| 01-01-01-01 | 26,532 | 5,784 | 0.22x | 🔴 EXPAND |
| 01-01-02-01 | 54,442 | 41,694 | 0.77x | ✅ DONE |
| 01-01-03-01 | 5,811 | 5,828 | 1.00x | ✅ DONE |
| 01-02-01-01 | 31,199 | 26,657 | 0.85x | ✅ DONE |

---

**CRITICAL QUALITY PRINCIPLES:**

1. **Full Coverage of Root Material** - Every significant concept, term, and doctrinal point in the Tibetan source must be addressed in the dynamic layer
2. **Zero Fluff** - No padding, repetition, or generic filler content 
3. **Byte Ratios as Guidelines** - The byte ratio targets are standards to check proportionality, NOT quotas to fill
4. **Line Counts Are Irrelevant** - Tibetan sources vary from 1 line to 1000+ lines; line count is never a valid quality metric

**Quality Hierarchy:**
- ✅ A++: Comprehensive coverage, precise terminology, no fluff, appropriate byte ratio
- ✅ A+: Minor gaps but solid coverage, good terminology
- ⚠️  B: Inadequate coverage or excessive fluff despite "good" byte ratio
- 🔴 C: Missing major content or filled with repetitive/generic text

**Version:** 9.1 (2026-02-16)  
**Last Updated:** Quality-first standards (coverage > bytes > lines)
