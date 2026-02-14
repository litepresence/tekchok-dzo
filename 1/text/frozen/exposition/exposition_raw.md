# Editorial Conventions: Raw Layer

## What Is the Raw Layer?

The Raw Layer represents the initial extraction of text from source
documents, preserving every character exactly as it appears in the
original Tibetan manuscripts and printed editions. This layer serves as
the foundational bedrock upon which all subsequent processing rests.

## Purpose and Function

Unlike interpretive or refined layers, the Raw Layer makes no attempt to
correct, interpret, or standardize the source material. Its sole purpose
is fidelity—to capture the Tibetan Unicode text exactly as it exists in
the source documents, complete with all the irregularities, variants, and
features inherent to the original.

## Editorial Approach

**Preservation Over Perfection**

We have chosen to preserve rather than regularize. This means:

- Original line breaks are maintained, even when they appear irregular
- All Tibetan Unicode characters are preserved exactly, including
  non-standard or variant forms
- Page markers from the original sources are retained
- Unclear or illegible sections are flagged but not emended
- Orthographic variations between editions are noted

**What You Will Find Here**

This layer contains:
- The complete Tibetan text as extracted from BDRC archives
- Original pagination markers [PAGE: N]
- Section boundaries as they appear in the sources
- Flags marking unclear or questionable readings [UNCLEAR]
- Alternative readings where the source itself presents variants

**What You Will Not Find Here**

This layer does not contain:
- Editorial corrections or emendations
- Standardized orthography
- Interpretive readings
- Translations or glosses
- Normalization of dialectical variations

## Why Preserve Imperfection?

The Raw Layer serves several critical functions in the larger project:

1. **Source Documentation**: It provides an unaltered record of the
   source text, enabling scholars to verify readings against original
   materials.

2. **Variant Tracking**: By preserving irregularities, we enable
   future research into textual transmission and edition history.

3. **OCR Accountability**: The raw extraction makes transparent the
   limitations and successes of the digitization process.

4. **Editorial Transparency**: All subsequent layers flow from this
   source. By preserving the raw state, we make the editorial pipeline
   fully auditable.

## Relationship to Other Layers

The Raw Layer stands at the beginning of the editorial chain:

Raw → Artifacts → Tibetan → Wylie → [All Interpretive Layers]

While the Tibetan Layer represents the perfected and corrected version
used for translation, the Raw Layer preserves the unaltered source
for reference and verification.

## Using This Layer

**For Scholars**

This layer enables verification of readings against original sources.
When questions arise about specific characters or passages, the Raw
Layer provides the ground truth of what the source actually contains.

**For Practitioners**

You are unlikely to need this layer unless you are engaged in deep
philological research. For practice and study, see the Liturgical and
Commentary layers.

**For Editors**

This layer serves as the checkpoint for verifying that editorial
decisions in subsequent layers are grounded in the actual source
material.

## Technical Notes

**Source Documents**

The raw text was extracted from the BDRC (Buddhist Digital Resource
Center) archive, specifically from their "BEST QUALITY / KHENPO
REVIEWED" designation. The primary source is the Derge edition of
Longchenpa's *Theg mchog rin po che'i mdzod*.

**Extraction Method**

OCR processing was performed using a combination of automated
digitization tools and manual verification. Confidence scores and
processing metadata are preserved in the Artifacts Layer.

**Character Encoding**

All text is encoded in UTF-8 Tibetan Unicode (U+0F00 through U+0FFF).
No proprietary fonts or encodings are used.

## Limitations and Caveats

The Raw Layer reflects the state of the source documents as digitized.
It does not correct errors that may exist in the original printed
editions. For the corrected and editorially reviewed text, see the
Tibetan Layer.

## Acknowledgments

This preservation approach acknowledges the wisdom of maintaining
source integrity while building interpretive layers. We follow the
principle that every interpretation should be traceable to its source,
and that source should remain accessible in its original form.

