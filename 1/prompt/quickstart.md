## Quick Start for New Agents

**ACQUAINTANCE:** This document provides orientation and getting-started instructions for new agents joining the translation project.

Hello, I'm litepresence. I'm an emergent systems engineer, cryptographer, translator, and dzogchen practitioner.

You are a general AI agent tasked with revising Longchenpa's *theg pa'i mchog rin po che'i mdzod*.

---

**PRIMARY BUILD IN `text/` FOLDER**

The project uses **section-based** files (01-01-01-01.txt):

**Section ID Format:** `VV-CC-SS-SS.txt`
- **VV:** Volume (01 or 02)
- **CC:** Chapter (01-25)
- **SS:** Section number (01-20+)
- **SS:** Subsection (01, 02, etc.)

**Example:**
- `text/tibetan/01-01-01-01.txt` = Volume 1, Chapter 1, Section 1, Subsection 1


# 1: If you encounter issues with your shell tools, visit navigation.md and/or update navigation.md and meta.md with suggestions
# 2: Stay on task and complete the following steps: 

---

## ⚠️ MANDATORY READING PROTOCOL ⚠️

**CRITICAL:** This section contains non-negotiable requirements. Failure to follow these protocols will result in corrupted output and wasted work.

### 1. READ !!!!

**YOU MUST:**
- Read the **ENTIRE** file, not just the first few lines
- If the file is large, read it in portions using `cat file | head -100`, then `cat file | tail -100`, etc. until you've seen every line
- Return to these files periodically (every 10-15 pages you edit) as I may update them with new instructions

**NEVER:**
- Assume you know the content from a quick scan
- Read only the first section and skip the rest
- Rely on summaries or previous readings without refreshing



## BYTE RATIO ANALYSIS WORKFLOW (MANDATORY)

**Primary Reference:** `/protocol/byte_ratios.md` — Single source of truth for all byte ratio targets

**Core Principle:** Qualitative depth over quantitative targets. Use byte ratios to identify potential gaps, not as rigid requirements.

### Quick Reference

| Layer | Primary Reference | Key Point |
|-------|------------------|-----------|
| **Commentary** | `/protocol/byte_ratios.md` | 0.4-2.0x (size-dependent) |
| **Scholar** | `/protocol/byte_ratios.md` | 0.5-10.0x (size-dependent) |
| **Delusion** | `/protocol/byte_ratios.md` | 0.2-15.0x (size-dependent) |
| **Epistemic** | `/protocol/byte_ratios.md` | 0.05-10.0x (naturally lower) |
| **Cognitive** | `/protocol/byte_ratios.md` | 0.2-1.0x (concise recognition) |

**Frozen/Root/Preface Layers:** No byte targets (immutable or non-textual)

### Quality Philosophy

✅ **Quality is King** - Excellent content outside ratio ranges beats mediocre content that hits targets  
✅ **Diagnostic Tool** - Ratios catch potential gaps, not mandate volume  
✅ **Agent Updatable** - If targets consistently produce false alarms, update `/protocol/byte_ratios.md`  
✅ **Size Matters** - Targets vary dramatically by Tibetan source size (tiny <200b vs huge >50000b)

### Calculation Method

```bash
cd /home/opencode/MDZOD/1/text
section="01-01-01-01"
tib=$(stat -c%s frozen/tibetan/${section}.txt)
layer=$(stat -c%s dynamic/commentary/${section}.txt)  # Replace with your layer
ratio=$(echo "scale=2; $layer/$tib" | bc)
echo "Byte ratio: ${ratio}x"
```

**See `/protocol/byte_ratios.md` for complete targets, tiers, and quality guidelines.**

---

**DELUSION LAYER QUALITY CHECKLIST (More Important Than Byte Ratio):**

✅ **Comprehensive Coverage** - All significant misinterpretations identified  
✅ **Deep Analysis** - Multi-layer "Why it arises" (cognitive, cultural, historical)  
✅ **Consequence Mapping** - Primary, secondary, long-term, and social effects  
✅ **Cascade Effects** - Clear error propagation chains  
✅ **Cross-Layer Awareness** - Related errors noted  
✅ **Safety Flags** - Critical errors marked explicitly  

**Never add content solely to hit a ratio. Stop when errors are comprehensively mapped.**

---

**EPISTEMIC LAYER QUALITY CHECKLIST (More Important Than Byte Ratio):**

✅ **Comprehensive Coverage** - Every major doctrinal point from Tibetan source classified  
✅ **Specific Terminology** - Technical terms (ka-dag, lhun-grub, kun gzhi, chos sku, rig pa) explicitly named  
✅ **Zero Generic Content** - No template phrases ("This passage presents...", "sophisticated hermeneutical strategy...")  
✅ **View Precision** - Specific view-register (dzogchen-rigpa, tantric-transformative, sutric-provisional)  
✅ **Citation Integration** - Root text citations identified with functional context  
✅ **Risk Contextualization** - Specific doctrinal tension points flagged (not generic "reification")
- **Complex sections** (500+ bytes): 0.8-1.2x, detailed view stratification

**NEVER add content to meet ratio. Stop when all doctrinal points are specifically classified.**

---

### STEP 1: PRIMARY ANALYSIS - Calculate Byte Ratios

```bash
cd /home/opencode/MDZOD/1/text

# Calculate byte ratio for any section/layer
section="01-01-02-01"
layer="commentary"

tib=$(stat -c%s frozen/tibetan/${section}.txt)
layer_bytes=$(stat -c%s dynamic/${layer}/${section}.txt)
ratio=$(echo "scale=2; $layer_bytes/$tib" | bc)

echo "Section: $section"
echo "Layer: $layer"
echo "Tibetan: $tib bytes"
echo "Layer: $layer_bytes bytes"
echo "Byte Ratio: ${ratio}x"
```

---

### STEP 2: SECONDARY ANALYSIS - Find Worst Deviations

**Purpose:** Identify the sections most out of range to prioritize work

```bash
cd /home/opencode/MDZOD/1/text

# Find worst Commentary deviations (below minimum 0.7x)
echo "=== COMMENTARY - WORST DEVIATIONS (below 0.7x) ==="
for f in frozen/tibetan/*.txt; do
  section=$(basename $f .txt)
  tib=$(stat -c%s "$f")
  comm=$(stat -c%s dynamic/commentary/${section}.txt 2>/dev/null || echo 0)
  [ "$comm" != "0" ] && ratio=$(echo "scale=2; $comm/$tib" | bc) && 
    [ $(echo "$ratio < 0.7" | bc) -eq 1 ] && 
    deviation=$(echo "scale=2; 0.7 - $ratio" | bc) &&
    echo "$section: $ratio (deviation: -${deviation})"
done | sort -t: -k3 -n | head -10

# Find worst Scholar deviations
echo ""
echo "=== SCHOLAR - WORST DEVIATIONS (below 1.0x) ==="
for f in frozen/tibetan/*.txt; do
  section=$(basename $f .txt)
  tib=$(stat -c%s "$f")
  sch=$(stat -c%s dynamic/scholar/${section}.txt 2>/dev/null || echo 0)
  [ "$sch" != "0" ] && ratio=$(echo "scale=2; $sch/$tib" | bc) && 
    [ $(echo "$ratio < 1.0" | bc) -eq 1 ] && 
    deviation=$(echo "scale=2; 1.0 - $ratio" | bc) &&
    echo "$section: $ratio (deviation: -${deviation})"
done | sort -t: -k3 -n | head -10

# Find worst Delusion deviations
echo ""
echo "=== DELUSION - WORST DEVIATIONS (below 0.7x) ==="
for f in frozen/tibetan/*.txt; do
  section=$(basename $f .txt)
  tib=$(stat -c%s "$f")
  del=$(stat -c%s dynamic/delusion/${section}.txt 2>/dev/null || echo 0)
  [ "$del" != "0" ] && ratio=$(echo "scale=2; $del/$tib" | bc) && 
    [ $(echo "$ratio < 0.7" | bc) -eq 1 ] && 
    deviation=$(echo "scale=2; 0.7 - $ratio" | bc) &&
    echo "$section: $ratio (deviation: -${deviation})"
done | sort -t: -k3 -n | head -10

# Find worst Epistemic deviations
echo ""
echo "=== EPISTEMIC - WORST DEVIATIONS (below 0.4x) ==="
for f in frozen/tibetan/*.txt; do
  section=$(basename $f .txt)
  tib=$(stat -c%s "$f")
  epi=$(stat -c%s dynamic/epistemic/${section}.txt 2>/dev/null || echo 0)
  [ "$epi" != "0" ] && ratio=$(echo "scale=2; $epi/$tib" | bc) && 
    [ $(echo "$ratio < 0.4" | bc) -eq 1 ] && 
    deviation=$(echo "scale=2; 0.4 - $ratio" | bc) &&
    echo "$section: $ratio (deviation: -${deviation})"
done | sort -t: -k3 -n | head -10
```

---

### STEP 3: SYSTEMATIC REPAIR WORKFLOW

**For each hotspot identified in secondary analysis:**

#### 3a. Find Hot Spot
```bash
# Example: Most urgent Commentary issue is 01-06-02-01
section="01-06-02-01"
layer="commentary"

# Check current ratio
tib=$(stat -c%s frozen/tibetan/${section}.txt)
current=$(stat -c%s dynamic/${layer}/${section}.txt)
ratio=$(echo "scale=2; $current/$tib" | bc)
echo "Current: ${ratio}x (need 0.7-1.5x, target ~1.0x)"
```

#### 3b. View Prompt and Exemplars
```bash
# Read the layer prompt for guidance
read prompt/prompt_${layer}.md

# The commentary prompt is particularly tricky! PAY ATTENTION!

# Read exemplars for this layer
read protocol/exemplars.md
# Look for sections with good ratios in the target range
```

#### 3c. Read Existing Layer
```bash
# Read what currently exists
read dynamic/${layer}/${section}.txt
```

#### 3d. Read Tibetan and Liturgical Source
```bash
# Read Tibetan source (immutable truth)
read text/frozen/tibetan/${section}.txt

# Read liturgical for context
read text/dynamic/liturgical/${section}.txt
```

#### 3e. Update Layer to Target Range
```bash
# Calculate target bytes for 1.0x ratio (center of range)
tib=$(stat -c%s frozen/tibetan/${section}.txt)
target=$(echo "scale=0; $tib * 1.0 / 1" | bc)
echo "Target: ~$target bytes (for 1.0x ratio)"

# Edit the file to expand/contract to target range
# Use 0.7x minimum, 1.5x maximum as boundaries
```

#### 3f. Verify Fix
```bash
# Confirm ratio is now in range
tib=$(stat -c%s frozen/tibetan/${section}.txt)
new_bytes=$(stat -c%s dynamic/${layer}/${section}.txt)
new_ratio=$(echo "scale=2; $new_bytes/$tib" | bc)
echo "NEW: ${new_ratio}x"

# Should show: in range 0.7-1.5x for Commentary
```

---

### STEP 4: ITERATE - Next Hot Spot

**⚠️ CRITICAL: Run fresh analysis each time!**
Before each iteration, ALWAYS run a fresh comprehensive byte ratio analysis to identify the CURRENT worst deviations. The situation changes after each fix. Do not assume the previous worst deviations are still the worst.

```bash
# Run fresh comprehensive analysis to find CURRENT worst deviations
cd /home/opencode/MDZOD/1 && python3 << 'EOF'
import os
from pathlib import Path

targets = {
    'wylie': (0.43, 0.45),
    'literal': (0.38, 0.42),
    'liturgical': (0.45, 0.60),
    'cognitive': (0.30, 0.70),
    'commentary': (0.70, 2.00),
    'delusion': (0.70, 2.50),  # Optimal: 1.0-1.8x, Center: 1.4x
    'epistemic': (0.40, 1.50),  # Min 0.4x, Optimal 0.6-1.0x
    'scholar': (1.00, 4.00),
}

tibetan_dir = Path('text/frozen/tibetan')
layers = ['wylie', 'literal', 'liturgical', 'cognitive', 'commentary', 'delusion', 'epistemic', 'scholar']

results = []
for layer in layers:
    layer_dir = Path(f'text/dynamic/{layer}')
    if not layer_dir.exists():
        continue
    target_min, target_max = targets[layer]
    target_center = (target_min + target_max) / 2
    
    for tib_file in sorted(tibetan_dir.glob('*.txt')):
        section_id = tib_file.stem
        layer_file = layer_dir / f'{section_id}.txt'
        if not layer_file.exists():
            continue
        tib_size = tib_file.stat().st_size
        layer_size = layer_file.stat().st_size
        if tib_size == 0:
            continue
        ratio = layer_size / tib_size
        deviation = abs(ratio - target_center)
        results.append({'section': section_id, 'layer': layer, 'ratio': ratio, 'target': f'{target_min}-{target_max}', 'deviation': deviation})

results.sort(key=lambda x: x['deviation'], reverse=True)
print("TOP 20 WORST DEVIATIONS:")
for i, r in enumerate(results[:20], 1):
    print(f"{i}. {r['section']} {r['layer']}: {r['ratio']:.2f}x (target: {r['target']})")
EOF
```

Then pick one of the top 20 worst deviations and continue the repair.

**Priority Order:**
1. Commentary < 0.7x (most critical - heart instruction)
2. Scholar < 1.0x (academic context)
3. Delusion < 0.7x (safety layer)
4. Epistemic < 0.4x (view stratification - indicates missing view distinctions)

---

### QUICK REFERENCE: Common Commands

```bash
# Check single section ratio
cd /home/opencode/MDZOD/1/text
section="01-01-02-01"
for layer in commentary scholar delusion epistemic; do
  tib=$(stat -c%s frozen/tibetan/${section}.txt)
  bytes=$(stat -c%s dynamic/${layer}/${section}.txt 2>/dev/null || echo 0)
  ratio=$(echo "scale=2; $bytes/$tib" | bc)
  echo "$layer: ${ratio}x"
done

# Find all sections below minimum for a layer
cd /home/opencode/MDZOD/1/text
min=0.7
layer=commentary
for f in frozen/tibetan/*.txt; do
  section=$(basename $f .txt)
  tib=$(stat -c%s "$f")
  bytes=$(stat -c%s dynamic/${layer}/${section}.txt 2>/dev/null || echo 0)
  [ "$bytes" != "0" ] && ratio=$(echo "scale=2; $bytes/$tib" | bc) && 
    [ $(echo "$ratio < $min" | bc) -eq 1 ] && echo "$section: ${ratio}x"
done
```

---

**Version:** 2.0 (2026-02-15)  
**Key Change:** Byte-ratio-based analysis workflow with secondary deviation detection