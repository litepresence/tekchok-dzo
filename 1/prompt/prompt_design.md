# PROMPT: DESIGN LAYERS
# Machine-Consumption Focused Generation Prompts
# For: Raw, Artifacts, Meter

===

## RAW LAYER GENERATION PROMPT

**LAYER:** Raw OCR/Text extraction
**OUTPUT:** /text/raw/VV-CC-SS-SS.txt
**FORMAT:** Plain text, page-by-page extraction

### TASK
Extract raw text from source documents maintaining:
- Original line breaks
- Tibetan Unicode characters
- Page markers [PAGE: N]
- Section boundaries

### CONSTRAINTS
- Do not interpret or correct
- Preserve all characters exactly as scanned
- Flag unclear/illegible sections with [UNCLEAR]
- Maintain original pagination

### OUTPUT FORMAT
```
[PAGE: 1]
༄༅།
ཐེག་པའི་མཆོག་རིན་པོ་ཆེའི་མཛོད།
...

[PAGE: 2]
...
```

===

## ARTIFACTS LAYER GENERATION PROMPT

**LAYER:** Processing artifacts and metadata
**OUTPUT:** /text/artifacts/VV-CC-SS-SS.txt
**FORMAT:** XML-structured metadata

### TASK
Document processing pipeline artifacts:
- OCR confidence scores
- Character recognition alternatives
- Formatting anomalies
- Editorial decisions

### XML SCHEMA
```xml
<artifact section="VV-CC-SS-SS">
  <source page="N" confidence="0.95"/>
  <alternatives>
    <char position="X" candidates="A,B,C"/>
  </alternatives>
  <anomalies>
    <item line="N" type="illegible_char" confidence="low"/>
  </anomalies>
  <editorial>
    <decision line="N" action="preserved_original" reason="context"/>
  </editorial>
</artifact>
```

===

## METER LAYER GENERATION PROMPT

**LAYER:** Metrical classification
**OUTPUT:** /text/meter/VV-CC-SS-SS.txt
**FORMAT:** Line-by-line classification

### CLASSIFICATION CODES
- **[PROSE]** - Prose exposition (82.6% of text)
- **[VERSE]** - Rhythmic verse, chantable (9.1%)
- **[ORNAMENTAL]** - Headings, markers, symbols (5.6%)
- **[MANTRA]** - Sacred syllables, no translation (1.8%)

### VERSE SUB-CLASSIFICATION
- **SANG_DREL** - 7-syllable meter
- **NOR_NANG** - 9-syllable meter  
- **CHUDRAL** - 6-syllable meter
- **MIXED** - Irregular patterns

### OUTPUT FORMAT
```
[1] <ornament>
[2] <ornament>
[3] [VERSE: SANG_DREL] 7 syllables
[4] [VERSE: SANG_DREL] 7 syllables
[5] [PROSE]
...
```

### TASK
For each line in Tibetan source:
1. Count syllables (Tibetan characters between shad markers)
2. Identify meter pattern
3. Classify into PROSE/VERSE/ORNAMENTAL/MANTRA
4. Output classification with line number

### CONSTRAINTS
- Strict 1:1 line correspondence with Tibetan
- No interpretation, only classification
- Preserve line numbering exactly

