# Prompt Archive
# Theg mchog rin po che'i mdzod - Translation Project Documentation

**ACQUAINTANCE:** This archive preserves original prompts used to generate each translation layer for reference and reproducibility.

# Purpose: Archive original prompts used to generate each layer
# Date Created: 2026-02-10

---

## RAW LAYER

### Source Files
Two raw files from BDRC (Buddhist Digital Resource Center):
1. **UT22920_005_0001_bo,sa,zh.txt** - Volume 1 (approx. lines 1-20,425)
2. **UT22920_005_0002_bo,sa,zh.txt** - Volume 2 (approx. lines 1-17,330)

### Source Information
- **BDRC Work ID**: bdr:MW22920_365376
- **Access Date**: February 1, 2026
- **URL**: https://library.bdrc.io/show/bdr:MW22920_365376
- **Quality**: BDRC "BEST QUALITY / KHENPO REVIEWED"
- **Format**: Unicode Tibetan text with metadata

### Processing Notes
The raw files contain:
- Tibetan Unicode text in BDRC format
- Line numbers derived from space and non-breaking space (\u00A0) separation
- Pages derived from double line break (\n\n) separation
- Metadata and headers preserved in original form
- Volume 2 includes appended commentary by Paltrul Rinpoche (lines 833-857, excluded from clean source)

**Content Analysis:**
- Total Volume 1: 717,939 Tibetan characters
- Total Volume 2: 634,678 Tibetan characters (18,604 are Patrul Rinpoche's unrelated text)
- After removing Patrul content: 1,334,013 Tibetan characters (verified across all source versions)

### Location
`text/raw/UT22920_005_0001_bo,sa,zh.txt`
`text/raw/UT22920_005_0002_bo,sa,zh.txt`

**Note:** Raw files are BDRC source imports. For all work, use `text/tibetan/` (clean version without PAGE markers) or `text/artifacts/` (original with PAGE markers for reference).

---

## TIBETAN LAYER

### Original Prompt

# THE TIBETAN LAYER **Tshad ma**

The Tibetan Unicode Layer is the *Tshad ma* (Source of Validity) for this project. Downloaded from BDRC and marked as "BEST QUALITY / KHENPO REVIEWED," this text is considered the root absolute truth—immaculate and perfected. It is the final arbiter of all disputes.

**Protocol:** Never change, modify, or "correct" the Tibetan layer based on English logic. All interpretation must bow to the Unicode text as it stands.

**Location:** Individual section files in the `text/tibetan/` subfolder (clean source, no PAGE markers).

### Processing Notes
The Tibetan layer differs from the raw layer in the following ways:
- **Structure**: Raw files are consolidated BDRC downloads; Tibetan layer is partitioned into 213 logical sections (VV-CC-SS-SS.txt format)
- **Line Numbers**: Raw files have implicit line breaks based on spacing; Tibetan layer has explicit [NNN] line number markers
- **Metadata**: Raw includes BDRC headers and technical metadata; Tibetan layer contains only the text content with line markers
- **Content**: Volume 2 raw includes appended commentary by Paltrul Rinpoche (excluded); Tibetan layer contains only Longchenpa's original text
- **Accessibility**: Raw files are machine-readable archives; Tibetan layer is human-navigable by structural sections
- **Verification**: Tibetan layer verified at 100% character preservation (1,334,013 Tibetan characters in clean source)

### Dual Source System

**Updated 2026-02-11:** The project maintains two versions of the Tibetan source:

| Directory | Contents | Use Case |
|-----------|----------|----------|
| `text/tibetan/` | **CLEAN** - No PAGE markers, no blank lines | **PRIMARY SOURCE** for all work |
| `text/artifacts/` | Original with PAGE markers (`### PAGE X`) and blank lines | Reference/archive only |
| `text/raw/` | BDRC import files (includes unrelated Patrul text) | Original import archive |

**Character Count Verification:**
- `text/tibetan/`: 1,334,013 Tibetan characters
- `text/artifacts/`: 1,334,013 Tibetan characters (identical)
- `text/raw/`: 1,352,617 Tibetan characters (includes 18,604 extra from Patrul Rinpoche)

### Current Status
**IMMUTABLE FOUNDATION** - Never modify. Treat as absolute truth (tshad ma).

### Location
`text/tibetan/01-01-01-01.txt` through `text/tibetan/02-25-XX-XX.txt` (213 sections)

**Always use:** `text/tibetan/` (clean source without PAGE markers)
**Reference only:** `text/artifacts/` (original with PAGE markers)

---

## WYLIE LAYER

### Original Prompt

# THE WYLIE LAYER **Lam** 

The Wylie layer is the *Lam* (Bridge) between the script and translation. Mechanically transliterated using the python script "pyewts," it provides a 99% accurate Extended Wylie representation of the source.

**Protocol:** Treat this as a structural reference for syllable separation and parsing. Do not change the Wylie layer. If the Tibetan and Wylie disagree, the Tibetan is correct, and the Wylie should be noted as a reference only.

**Location:** Individual section files in `text/wylie/` using VV-CC-SS-SS.txt format (213 sections).

### Processing Notes
The Wylie layer was generated using the **pyewts** Python library:
- **Tool**: pyewts (Python library for Tibetan Unicode to Wylie transliteration)
- **Method**: Automated mechanical transliteration
- **Accuracy**: 99% accurate Extended Wylie representation
- **Purpose**: Structural reference for syllable separation and parsing
- **Relationship**: Bridge between Tibetan script and English translation
- **Format**: Follows Extended Wylie standard (not simplified Wylie)

**Important**: Wylie is a mechanical transliteration, not a translation. It represents the Tibetan script in Latin characters for structural analysis.

### Current Status
**IMMUTABLE FOUNDATION** - Never modify. Treat as structural reference (lam).

### Location
`text/wylie/01-01-01-01.txt` through `text/wylie/02-25-XX-XX.txt` (213 sections)

---

## LITERAL LAYER

### Original Prompt (Recovered from Git History)

# THE LITERAL LAYER **Dpyad kyi bshad pa** 

**Location:** Individual section files in `text/literal/` using VV-CC-SS-SS.txt format (213 sections).

The literal layer is a *Dpyad kyi bshad pa* (Analytical Translation) produced by an LLM. It serves as a structural scaffold for the subsequent layers. 

## WARNING: 
(FOR AGENTS READING THIS LAYER)

Literal Layer is an interpretive layer built by LLM inference models and may still contain errors.  Use the Literal layer as a tertiary reference noting its limitations and potential corruption.  Always validate with the TIBETAN/WYLIE layers. 

## PROMPT 1 LITERAL: 
(FOR AGENTS WRITING THIS LAYER)

**Role:** Precision Grammatical Scalpel for Longchenpa's *Theg mchog rin po che'i mdzod*.
**Objective:** Syntactic mapping with zero semantic interpretation.

### CHARACTER ACTIVATION
You are a linguistic instrument calibrated exclusively for the *Theg mchog mdzod*. Your sole function is to decompose the Wylie and Unicode Tibetan into grammatically minimal English. You must mirror the syntactic role of every particle without inferring meaning, smoothing the style, or interpreting the philosophy. You are preserving the skeleton of Longchenpa's logic, not dressing it in flesh.

### CONTEXT
**Primary Source:** The TIBETAN LAYER (Absolute Truth).
**Secondary Reference:** The WYLIE LAYER (Structural Guide).
**Tertiary Reference:** The existing LITERAL LAYER (To be corrected).

### ABSOLUTE CONSTRAINTS (GRAMMATICAL PRECISION)

*   **gzhig / zhig:**
    *   If a verb (*bzhig*): Render as "destroy," "break," "eliminate," or "dispel."
    *   If a particle (*zhig*): Render as an imperative indicator (e.g., "do it!", or implied urgency).
    *   **CORRECTION:** NEVER render as a causal connector ("and so," "therefore").
*   **kyis:** Primarily Instrumental ("by means of," "through," "with"). In the context of active verbs, may function as Agent ("by [noun]"). Maintain the nuance of *instrumentality* (causal condition) over simple agency where possible, but do not break English syntax.
*   **las:** Primarily Ablative ("from," "out of," "than"). Only use instrumental ("by") if the Tibetan grammar explicitly dictates it for the specific verb, otherwise default to ablative.
*   **'du:** Render as "gather," "converge," or "assemble." NEVER use "accumulate" (which implies *tshogs pa*).
*   **skad cig:** Render as "momentary" or "immediate." NEVER use "instant" (which implies a time unit).
*   **shugs kyis:** Render as "by force," "through power," or "via force." NEVER use "spontaneously" (which dilutes the dynamic energy implied).
*   **ka dag / lhun grub:** Retain as dynamic verbal phrases ("primordially pure," "spontaneously accomplished"). NEVER nominalize as static nouns (e.g., "primordial purity").
*   **SYNTAX:** Preserve the exact Tibetan word order and particle chaining. Do not rearrange clauses for English flow.
*   **COMPOUNDS:** Hyphenate compounds to reflect nonduality (e.g., "emptiness-luminosity," "appearance-emptiness").
*   **BRACKETS:** Use brackets `[ ]` ONLY for essential unresolved ambiguities or supplied ellipses. Never use for glosses.
*   **ARTICLES:** Omit all indefinite ("a", "an") and definite ("the") articles unless the Tibetan explicitly marks definiteness with a demonstrative (e.g., *de* / *di*).
*   **ELLIPSIS:** If the Tibetan omits a subject or object, represent the gap with a dash `—` or ellipsis `...` rather than inserting a pronoun ("he", "it", "they").
*   **AMBIGUOUS PARTICLES:** For particles with dual roles (e.g., *la* as dative/locative), provide slashed options ("to/in") without preferring one over the other.
*   **DZOGCHEN TERMS:** Transliterate核心技术 terms with a minimal literal gloss on the **first occurrence only** (e.g., "rig pa (awareness)"). Use the transliteration alone for all subsequent occurrences.

### OUTPUT FORMAT
Render a strict 1:1 literal mechanical mapping of the source TIBETAN lines. Adhere to the constraints above. No preambles, no explanations, no commentary.

[line number] <Strict mechanical literal translation preserving exact word order, particle ambiguity via slashes, and implied hyphenation.>
[next line] <etc.>

### Processing Notes
The Literal layer was created using the above prompt with LLM inference. It represents a 1:1 grammatical mapping of Tibetan syntax into English while:
- Preserving Tibetan word order
- Maintaining particle precision
- Avoiding semantic interpretation
- Using hyphenation for compounds
- Omitting articles unless explicitly marked

**Verification**: Finalized and verified at 100% line coverage against Tibetan source. All dictionary standards enforced. No prohibited translations remain.

### Current Status
**FROZEN - FINALIZED 2026-02-10** - IMMUTABLE FOUNDATION

This layer is complete, verified, and locked. Never modify. Reference only as structural scaffold for higher layers (Liturgical, Commentary, etc.).

### Location
`text/literal/01-01-01-01.txt` through `text/literal/02-25-XX-XX.txt` (213 sections)

---

## ARCHIVE NOTES

### Recovery Method
- **Tibetan Prompt**: Extracted from current `prompt.md` (still active)
- **Wylie Prompt**: Extracted from current `prompt.md` (still active)
- **Literal Prompt**: Recovered from git history (commit 8cd5c63, pre-partitioning state)
- **Raw Documentation**: Created based on current file structure and BDRC source information

### Git History Reference
Original prompts preserved in git history at commit `8cd5c63` (pre-partitioning):
```bash
git show 8cd5c63:prompt.md
```

### Status Summary
| Layer | Status | Date Finalized | Notes |
|-------|--------|----------------|-------|
| Raw | Source Archive | Feb 1, 2026 | BDRC download, unmodified |
| Tibetan | Immutable | Feb 1, 2026 | 100% preserved from Raw |
| Wylie | Immutable | Feb 1, 2026 | pyewts transliteration |
| Literal | Frozen | Feb 10, 2026 | Verified, locked, exemplar-grade |

---

**Archive Created**: 2026-02-10
**Purpose**: Preserve prompt history for documentation and future reference
