# PROMPT LAYER OVERVIEW
# Theg mchog rin po che'i mdzod - Treasury of the Supreme Vehicle

**Date:** 2026-02-13
**Purpose:** Master index of all 12 translation/generation layers

---

## THE 12 LAYERS

### SOURCE/ARCHIVE LAYERS (Non-Generated)

**1. RAW** `prompt_raw.md`
- **Purpose:** BDRC source documentation
- **Content:** Original BDRC download files, metadata, verification
- **Status:** Archive - Never modify
- **Location:** `text/raw/`

**2. ARTIFACTS** `prompt_artifacts.md`
- **Purpose:** Processing layer documentation
- **Content:** OCR output with PAGE markers, processing notes
- **Status:** Archive - Reference only
- **Location:** `text/artifacts/`

---

### FOUNDATION LAYERS (Immutable)

**3. TIBETAN** `prompt_tibetan.md`
- **Purpose:** Tshad ma (Source of Validity)
- **Content:** Clean Unicode Tibetan, absolute truth for project
- **Status:** Immutable - Never modify
- **Location:** `text/tibetan/`
- **Key Constraint:** Final arbiter of all disputes

**4. WYLIE** `prompt_wylie.md`
- **Purpose:** Lam (Bridge between script and translation)
- **Content:** Extended Wylie transliteration via pyewts
- **Status:** Immutable - Structural reference only
- **Location:** `text/wylie/`
- **Key Constraint:** 99% accurate mechanical transliteration

---

### GENERATED TRANSLATION LAYERS (LLM)

**5. LITERAL** `prompt_literal.md`
- **Purpose:** Dpyad kyi bshad pa (Analytical Translation)
- **Content:** Grammatical scaffold - Tibetan syntax in English
- **Status:** Frozen - FINALIZED 2026-02-10
- **Location:** `text/literal/`
- **Key Constraint:** Zero semantic interpretation, exact word order

**6. LITURGICAL** `prompt_liturgical.md`
- **Purpose:** Sgrub pa'i gleng gzhi (Basis for Practice)
- **Content:** Elegant prose/verse for ritual recitation
- **Status:** Active - Iterative refinement
- **Location:** `text/frozen/liturgical/`
- **Key Constraint:** Balance metaphysical precision with vibratory effect

---

### GENERATED COMMENTARY LAYERS (LLM)

**7. INTRODUCTION** `prompt_introduction.md`
- **Purpose:** Chapter overview and contextual framing
- **Content:** Accessible prose bridging technical and experiential
- **Status:** Active
- **Location:** `text/introduction/`
- **Key Constraint:** Benefit both scholars and practitioners

**8. COMMENTARY** `prompt_commentary.md`
- **Purpose:** Man ngag (Pith Instructions) - unlocking terma
- **Content:** Multi-voice heart instructions FROM realization
- **Status:** Active - Recently polished for "pointing"
- **Location:** `text/commentary/`
- **Key Constraint:** FROM not ABOUT; shake complacency; plain speech

**9. SCHOLAR** `prompt_scholar.md`
- **Purpose:** Academic technical analysis
- **Content:** Breakdown of all technical aspects
- **Status:** Active
- **Location:** `text/scholar/`
- **Key Constraint:** Epistemic precision for academic readers

**10. EPISTEMIC** `prompt_epistemic.md`
- **Purpose:** Technical right view
- **Content:** Correct philosophical positions
- **Status:** Active
- **Location:** `text/epistemic/`
- **Key Constraint:** Rigorous logical analysis

**11. DELUSION** `prompt_delusion.md`
- **Purpose:** Technical wrong view
- **Content:** Incorrect positions to avoid
- **Status:** Active
- **Location:** `text/delusion/`
- **Key Constraint:** Show what obscures recognition

**12. COGNITIVE** `prompt_cognitive.md`
- **Purpose:** Real-time understanding demonstration
- **Content:** Shows recognition in preparation for translation
- **Status:** Active
- **Location:** `text/cognitive/`
- **Key Constraint:** Demonstrate understanding process

---

## PROCESSING LAYERS

**METER** `prompt_meter.md`
- **Purpose:** Metrical classification for liturgical generation
- **Content:** PROSE/VERSE/ORNAMENTAL/MANTRA classification
- **Status:** Processing layer
- **Location:** `text/meter/`
- **Key Constraint:** Strict 1:1 line correspondence with Tibetan

---

## LAYER RELATIONSHIPS

```
RAW → ARTIFACTS → TIBETAN → WYLIE
                                    ↓
LITERAL (grammatical) → LITURGICAL (transmission)
                                    ↓
                    COMMENTARY (pointing/unlocking)
                                    ↓
    SCHOLAR / EPISTEMIC / DELUSION / COGNITIVE (analysis)
                                    ↓
                        INTRODUCTION (bridge to reader)
```

**Transmission Flow:**
- **Literal:** Makes you think in nondual terms (grammar)
- **Liturgical:** Induces transmission (vibration)
- **Commentary:** Demonstrates real-time understanding (pointing)
- **Cognitive:** Shows recognition process

---

## CRITICAL PRINCIPLES

### For All Generated Layers:
1. **Reference Standards:** dictionary.md, capitalize.md, exemplars.md
2. **Source Priority:** Tibetan > Wylie > Literal > Higher Layers
3. **Never Modify Immutable:** Tibetan, Wylie, Literal (frozen)
4. **Verify Against Source:** All interpretive layers must bow to Tibetan

### Commentary Layer Specific:
- **FROM not ABOUT:** Speak from realization, not about it
- **POINTING:** Unlock terma code, don't explain it academically
- **Conversational:** Spoken tone without operatic vibratory effect
- **Shake Complacency:** Plain speech that prevents confusion
- **Transmission-Serving:** Support liturgical induction, not replace it

---

## REFERENCE DOCUMENTS

All agents must consult:
- **dictionary.md** - Terminology standards
- **capitalize.md** - Capitalization rules (STRICT)
- **exemplars.md** - Best-practice examples
- **navigation.md** - Project structure
- **conventions.md** - Methodology
- **status.md** - Current completion state

---

## PROMPT ARCHITECTURE

**Single Layer Per File:**
- Each `.md` file contains ONE layer's complete prompt
- No mixing of multiple layers in one file
- Clear boundaries between layer functions

**Backup Location:**
- Old consolidated files: `/prompt/backup/`
- prompt_design.md (contained Raw, Artifacts, Meter)
- prompt_practitioner.md (contained Introduction, Liturgical, Commentary)
- prompt.md (master document, now split)
- prompt_archive.md (archive notes, now incorporated)

---

**Copyleft 2026:** Amid all this apparent happening, nothing has happened.
