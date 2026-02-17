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

**Primary Reference:** `/protocol/byte_ratios.md` — Single source of truth for all byte ratio targets

**Why Byte Ratios vs Line Ratios:**
1. Line counts vary with formatting (wrapping, paragraph breaks)
2. Byte counts reflect actual content density
3. Small files (<500 bytes) have extreme line-ratio distortions

**Key Principle:** Quality > Byte Ratios. Ratios are diagnostic guide rails, not quotas.

**Targets Vary by Tibetan Source Size:**
- Tiny (<200b): High ratios expected (2-15x)
- Small (200-2000b): Moderate ratios (0.5-6x)
- Medium (2000-10000b): Standard ratios (0.3-2.5x)
- Large (10000-50000b): Lower ratios (0.2-1.5x)
- Huge (>50000b): Minimal ratios (0.05-1.2x)

**See `/protocol/byte_ratios.md` for complete layer-specific targets.**

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
2. Check byte ratio targets in `/protocol/byte_ratios.md`
3. Generate content (quality over quantity)
4. Calculate actual byte ratio
5. Validate comprehensiveness (not just ratio)
6. Reference exemplars in `protocol/exemplars.md`

**Validation Command:**
```bash
cd text
tib=$(stat -c%s frozen/tibetan/01-01-02-01.txt)
comm=$(stat -c%s dynamic/commentary/01-01-02-01.txt)
echo "Byte ratio: $(echo "scale=2; $comm/$tib" | bc)x"
```

**Note:** Agents may update `/protocol/byte_ratios.md` if targets consistently produce false alarms.

---

**Version:** 3.1 (2026-02-16)
**Key Changes:**
- Byte-ratio-based quality system (more accurate than line ratios)
- Centralized targets in `/protocol/byte_ratios.md`
- Quality > Quantity philosophy throughout
