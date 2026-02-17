# Byte Ratio Guidelines
## Theg mchog rin po che'i mdzod Translation Project

**Date:** 2026-02-16
**Purpose:** Centralized byte ratio targets for all translation layers

---

## Philosophy

**Quality is King. Bytes are Guide Rails.**

Byte ratios exist to catch potential problems—sections that might be undersized or oversized. They are NOT quotas. If a section is qualitatively excellent but outside the ratio range, the quality wins. If ratios are consistently triggering false alarms, agents should update these guidelines.

**Never sacrifice quality to hit a byte target.**

---

## Calculation Method

### Single Section
```bash
cd /home/opencode/MDZOD/1/text
section="01-01-01-01"  # Replace with your section

# Get Tibetan source size
tib=$(stat -c%s frozen/tibetan/${section}.txt)

# Get your layer size (replace 'commentary' with your layer)
layer=$(stat -c%s dynamic/commentary/${section}.txt)

# Calculate ratio
ratio=$(echo "scale=2; $layer/$tib" | bc)
echo "Byte ratio: ${ratio}x"
```

### Batch Analysis
```bash
cd /home/opencode/MDZOD/1/text

# Find all sections below minimum threshold for your layer
for f in frozen/tibetan/*.txt; do
  section=$(basename $f .txt)
  tib=$(stat -c%s "$f")
  
  # Adjust path for your layer
  layer_file="dynamic/commentary/${section}.txt"
  
  if [ -f "$layer_file" ]; then
    layer=$(stat -c%s "$layer_file")
    ratio=$(echo "scale=2; $layer/$tib" | bc)
    
    # Check against your layer's minimum (0.7 for commentary)
    if [ $(echo "$ratio < 0.7" | bc) -eq 1 ]; then
      echo "$section: ${ratio}x (below target)"
    fi
  fi
done | sort -t: -k2 -n | head -20
```

---

## Tibetan Size Categories

| Category | Size Range | Characteristics |
|----------|-----------|-----------------|
| **Tiny** | <200 bytes | Structural fragments, headers, list markers |
| **Small** | 200-2,000 bytes | Brief sections, single concepts |
| **Medium** | 2,000-10,000 bytes | Standard doctrinal sections |
| **Large** | 10,000-50,000 bytes | Major chapters, philosophical analysis |
| **Huge** | >50,000 bytes | Encyclopedic sections, advanced practices |

---

## Layer-Specific Targets

### COMMENTARY (Heart Instruction)
**Purpose:** Man ngag—living transmission from realized masters

| Category | Target Range | Notes |
|----------|--------------|-------|
| Tiny (<200b) | 0.8-2.0x | High ratios acceptable—tiny sources need substantial commentary |
| Small (200-2000b) | 0.8-1.5x | Standard heart instruction depth |
| Medium (2000-10000b) | 0.7-1.2x | Full voice rotation, doctrinal engagement |
| Large (10000-50000b) | 0.5-1.0x | Comprehensive coverage expected |
| Huge (>50000b) | 0.4-0.8x | May trend lower due to source size |

**Quality Indicators:**
- Minimum 6 distinct voices per file
- Specific line ranges [start-end] for every block
- No voice attribution (anonymous speaking)
- Fresh metaphors, no repetition within 5 sections

---

### SCHOLAR (Academic Analysis)
**Purpose:** Four Pillars structural analysis

| Category | Target Range | Notes |
|----------|--------------|-------|
| Tiny (<200b) | 2.0-10.0x | High ratios expected—minimal sources need context |
| Small (200-2000b) | 2.0-6.0x | Standard doctrinal unpacking |
| Medium (2000-10000b) | 1.0-2.5x | Full Four Pillars coverage |
| Large (10000-50000b) | 0.6-1.5x | Deep philological analysis |
| Huge (>50000b) | 0.5-1.2x | Comprehensive citations and context |

**Quality Indicators:**
- Four Pillars: <structure>, <philology>, <context>, <concept>
- Wylie terminology with semantic explanations
- Third person only ("Longchenpa presents...")
- No devotional language

---

### DELUSION (Error Cartography)
**Purpose:** Mapping failure modes and misinterpretations

| Category | Target Range | Notes |
|----------|--------------|-------|
| Tiny (<200b) | 2.0-15.0x | Contextual error mapping for minimal content |
| Small (200-2000b) | 1.0-3.0x | Standard error taxonomy |
| Medium (2000-10000b) | 0.4-1.5x | Comprehensive cascade chains |
| Large (10000-50000b) | 0.2-1.0x | Exhaustive error coverage |
| Huge (>50000b) | 0.2-0.8x | Critical: advanced practice material needs minimum 0.3x |

**Quality Indicators:**
- Every doctrinal point has error mapping
- Distinct errors remain separate (not merged)
- Cascade effects show propagation chains
- Clinical tone, no stating correct view

**Critical Alert:** Sections <0.3x on material >5000 bytes need immediate review

---

### EPISTEMIC (View Stratification)
**Purpose:** Classifying FROM WHERE statements are spoken

| Category | Target Range | Notes |
|----------|--------------|-------|
| Tiny (<200b) | 1.0-10.0x | Minimal classification still needs context |
| Small (200-2000b) | 0.5-2.0x | Standard view marking |
| Medium (2000-10000b) | 0.2-1.0x | Precise view-register identification |
| Large (10000-50000b) | 0.1-0.5x | Concise classification format |
| Huge (>50000b) | 0.05-0.3x | Highly technical, minimal by design |

**Quality Indicators:**
- XML tags: <view>, <pedagogy>, <risk>
- View registers precise (dzogchen-rigpa, tantric-transformative, sutric-provisional)
- Risk flags specific and contextualized
- No content restatement—classification only

**Note:** Epistemic ratios are naturally lower than other layers due to concise format

---

### COGNITIVE (Translator's Log)
**Purpose:** Internal alignment—recognition before articulation

| Category | Target Range | Notes |
|----------|--------------|-------|
| Tiny (<200b) | 0.4-1.0x | Quiet recognition of minimal content |
| Small (200-2000b) | 0.4-0.7x | Standard translator's notes |
| Medium (2000-10000b) | 0.3-0.6x | Structural and view register notes |
| Large (10000-50000b) | 0.25-0.5x | Preservation requirements documentation |
| Huge (>50000b) | 0.2-0.4x | Pre-rendering recognition log |

**Quality Indicators:**
- Line ranges: [start-end]
- Quiet, non-didactic tone (calm, settled)
- No questions, no uncertainty language
- Covers: Structure, View Register, Translation Risks, Preservation Requirements

---

## Layers WITHOUT Byte Targets

These layers either are complete (frozen) or have different quality metrics:

| Layer | Location | Status |
|-------|----------|--------|
| **Tibetan** | `frozen/tibetan/` | Source of truth—immutable |
| **Wylie** | `frozen/wylie/` | Mechanical transliteration |
| **Literal** | `frozen/literal/` | 1:1 grammatical mapping—complete |
| **Liturgical** | `dynamic/liturgical/` | Quality measured by voice/precision, not bytes |
| **Meter** | `dynamic/meter/` | Classification layer—size-independent |
| **Root** | `root/` | Source material |
| **Preface** | `preface/` | Editorial material |

---

## Diagnostic Alerts

### Red Flags (Check Immediately)
- Any layer: <0.1x on material >10,000 bytes
- Delusion: <0.3x on advanced Dzogchen (Trekcho/Thogal/Bardo/Phowa)
- Commentary: <0.5x on standard sections (missing voices)

### Yellow Flags (Verify Qualitatively)
- Ratio outside target range but content appears comprehensive
- Sudden ratio jumps between adjacent sections
- Tiny files with extremely high ratios (>50x)

### When to Update These Guidelines

If you consistently find:
- **Quality content falling outside ranges** → Expand acceptable ranges
- **Fluffy content hitting targets** → Tighten ranges or improve quality criteria
- **Certain content types behaving differently** → Add new categories

**Process:** Update this file, then update all prompts that reference it.

---

## Quick Reference Card

| Layer | Tiny | Small | Medium | Large | Huge |
|-------|------|-------|--------|-------|------|
| **Commentary** | 0.8-2.0x | 0.8-1.5x | 0.7-1.2x | 0.5-1.0x | 0.4-0.8x |
| **Scholar** | 2.0-10.0x | 2.0-6.0x | 1.0-2.5x | 0.6-1.5x | 0.5-1.2x |
| **Delusion** | 2.0-15.0x | 1.0-3.0x | 0.4-1.5x | 0.2-1.0x | 0.2-0.8x |
| **Epistemic** | 1.0-10.0x | 0.5-2.0x | 0.2-1.0x | 0.1-0.5x | 0.05-0.3x |
| **Cognitive** | 0.4-1.0x | 0.4-0.7x | 0.3-0.6x | 0.25-0.5x | 0.2-0.4x |

---

**Version:** 1.0 (2026-02-16)  
**Principle:** Quality over quantity. Bytes serve insight, not the reverse.
