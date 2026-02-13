# PROMPT: METER LAYER
# Theg mchog rin po che'i mdzod

**Layer:** Processing Layer (LLM Generated)
**Purpose:** Metrical classification of Tibetan text
**Output:** `/text/meter/VV-CC-SS-SS.txt`
**Format:** Line-by-line classification

---

## PURPOSE

The Meter Layer classifies each line of Tibetan text by its metrical pattern. This classification guides the Liturgical Layer in determining whether to render as prose, verse, ornamental markers, or mantra.

---

## CLASSIFICATION CODES

### Primary Types

**[PROSE]** - Prose exposition
- 82.6% of text
- Flowing, non-metrical exposition
- Render as elegant prose in liturgical layer

**[VERSE]** - Rhythmic verse, chantable
- 9.1% of text
- Strict syllabic meter
- Render as chantable verse in liturgical layer

**[ORNAMENTAL]** - Headings, markers, symbols
- 5.6% of text
- Visual/textual ornaments
- Preserve with minimal translation

**[MANTRA]** - Sacred syllables
- 1.8% of text
- No semantic translation
- Transliterate only

### Verse Sub-Classification

When classifying as [VERSE], specify meter type:

- **SANG_DREL** - 7-syllable meter
- **NOR_NANG** - 9-syllable meter  
- **CHUDRAL** - 6-syllable meter
- **MIXED** - Irregular patterns

---

## OUTPUT FORMAT

```
[1] <ornament>
[2] <ornament>
[3] [VERSE: SANG_DREL] 7 syllables
[4] [VERSE: SANG_DREL] 7 syllables
[5] [PROSE]
[6] [PROSE]
[7] <mantra>
...
```

---

## TASK

For each line in Tibetan source:
1. Count syllables (Tibetan characters between shad markers །)
2. Identify meter pattern
3. Classify into PROSE/VERSE/ORNAMENTAL/MANTRA
4. Output classification with line number

---

## CONSTRAINTS

- **Strict 1:1 line correspondence** with Tibetan
- **No interpretation**, only classification
- **Preserve line numbering exactly**
- Tibetan line 1 = Meter line 1

---

## SYLLABLE COUNTING

**Method:**
- Count Tibetan characters between shad (།) punctuation
- Each character = one syllable
- Ignore spaces
- Example: "ཐེག་པ་ཆེན་པོ།" = 4 syllables (ཐེག་ པ་ ཆེན་ པོ)

**Meter Patterns:**
- **6 syllables** = CHUDRAL meter
- **7 syllables** = SANG_DREL meter
- **9 syllables** = NOR_NANG meter
- **Irregular** = MIXED meter

---

## EXAMPLES

### Ornamental
```
[1] <ornament> ༄༅།
[2] <ornament> །ཐེག་པའི་མཆོག་རིན་པོ་ཆེའི་མཛོད།
```

### Verse
```
[10] [VERSE: SANG_DREL] 7 syllables
[11] [VERSE: SANG_DREL] 7 syllables
[12] [VERSE: SANG_DREL] 7 syllables
```

### Prose
```
[20] [PROSE]
[21] [PROSE]
[22] [PROSE]
```

### Mantra
```
[50] <mantra> oṃ maṇi padme hūṃ
```

---

## USAGE

**Liturgical Layer reads this file FIRST** before generating content.

Based on meter classification:
- **[PROSE]** → Generate elegant flowing prose
- **[VERSE]** → Generate chantable rhythmic verse
- **[ORNAMENTAL]** → Preserve symbols, minimal translation
- **[MANTRA]** → Transliterate only

---

## LOCATION

`text/meter/01-01-01-01.txt` through `text/meter/02-25-XX-XX.txt` (213 sections)

---

**Copyleft 2026:** Amid all this apparent happening, nothing has happened.
