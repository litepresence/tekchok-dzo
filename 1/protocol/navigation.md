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

| Layer | Min | Target | Max |
|-------|-----|--------|-----|
| Commentary | 0.6x | 0.8-1.5x | 2.0x |
| Scholar | 1.0x | 1.5-3.0x | 4.0x |
| Delusion | 0.7x | 1.0-2.0x | 3.0x |
| Epistemic | 0.3x | 0.5-1.0x | 1.5x |

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
  [ "$ratio" != "0" ] && [ $(echo "$ratio < 0.6" | bc) -eq 1 ] && echo "$s: $ratio"
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

**Version:** 9.0 (2026-02-15)  
**Last Updated:** Byte-ratio quality system (more accurate than line ratios)
