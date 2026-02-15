# META: Project Architecture & Insights

**Purpose:** Meta-level communication for project management

---

## Architecture: 12-Layer Translation

| Layer | Type | Purpose |
|-------|------|---------|
| Tibetan | Frozen | Source (BDRC) |
| Wylie | Frozen | Transliteration |
| Literal | Frozen | 1:1 mapping |
| Liturgical | Frozen | Vajra speech |
| Commentary | Dynamic | Heart instruction |
| Scholar | Dynamic | Four Pillars |
| Epistemic | Dynamic | View stratification |
| Delusion | Dynamic | Error detection |
| Cognitive | Dynamic | Translator log |

---

## Current Discovery: BYTE-RATIO-Based Quality

**THE METRIC:** Content ÷ Tibetan source bytes

Reference: `quality/byte_ratio_table.md` (213 sections × 9 layers)

| Byte Ratio Tier | Sections | % |
|-----------------|----------|---|
| Disaster | <0.3x | 45 (21%) |
| Critical | 0.3-0.5x | 38 (18%) |
| Low | 0.5-0.7x | 35 (16%) |
| Good | 0.7-1.2x | 42 (20%) |
| Excellent | >1.2x | 53 (25%) |

**Why Byte Ratios vs Line Ratios:**
1. Line counts vary with formatting (wrapping, paragraph breaks)
2. Byte counts reflect actual content density
3. Small files (<500 bytes) have extreme line-ratio distortions

**Target Byte Ratios for A++ Quality:**
- Commentary: 0.8-1.5x
- Scholar: 1.5-3.0x
- Delusion: 1.0-2.0x
- Epistemic: 0.5-1.0x

**First 4 Sections Priority (Byte Ratios):**

| Section | Tib Bytes | Commentary | Byte Ratio | Action |
|---------|-----------|------------|------------|--------|
| 01-01-01-01 | 26,532 | 5,784 | 0.22x | 🔴 EXPAND |
| 01-01-02-01 | 54,442 | 41,694 | 0.77x | ✅ GOOD |
| 01-01-03-01 | 5,811 | 5,828 | 1.00x | ✅ EXCELLENT |
| 01-02-01-01 | 31,199 | 26,657 | 0.85x | ✅ GOOD |

---

## Key Insight

**Larger sections were under-generated** - generation truncated at ~100 lines regardless of source length. The fix is proportional expansion based on bytes, not lines.

---

## Workflow

1. Read Tibetan source
2. Write to target byte ratio (see quality/byte_ratio_table.md)
3. Validate with byte-ratio script
4. Reference exemplars in `protocol/exemplars.md`

**Validation Command:**
```bash
cd text
tib=$(stat -c%s frozen/tibetan/01-01-02-01.txt)
comm=$(stat -c%s dynamic/commentary/01-01-02-01.txt)
echo "Byte ratio: $(echo "scale=2; $comm/$tib" | bc)x"
```

---

**Version:** 3.0 (2026-02-15)  
**Key Change:** Byte-ratio-based quality system (more accurate than line ratios)
