#!/usr/bin/env python3
"""
Generate epistemic layer files for Theg mchog mdzod project
Uses pattern recognition to classify epistemic stance from commentary content
"""

import os
import re
import glob


def get_line_range(commentary_file):
    """Extract line numbers from commentary file"""
    with open(commentary_file, "r") as f:
        content = f.read()

    # Find all [number-number] patterns
    matches = re.findall(r"\[(\d+)-(\d+)\]", content)
    if matches:
        first_start = min(int(m[0]) for m in matches)
        last_end = max(int(m[1]) for m in matches)
        return f"[{first_start}-{last_end}]"
    return ""


def classify_epistemic(commentary_file):
    """Classify epistemic stance based on commentary content"""
    with open(commentary_file, "r") as f:
        content = f.read().lower()

    # Initialize classifications
    view_tags = []
    pedagogical_tags = []
    risk_flags = []
    description = ""

    # Check for Patrul Rinpoche voice (Dzogchen pointing)
    is_patul = "patrul rinpoche" in content or "fireside" in content

    # Check for negational patterns
    has_negation = any(
        phrase in content
        for phrase in [
            "has no",
            "no letter",
            "no form",
            "no name",
            "no number",
            "empty",
            "names for",
            "labels for",
            "do not seek",
            "do not count",
            "find that",
            "who",
            "where is",
            "the one who",
        ]
    )

    # Check for tantric technical content
    has_tantra = any(
        term in content
        for term in [
            "channel",
            "wheel",
            "chakra",
            "nadi",
            "bindu",
            "wind",
            "drop",
            "letter",
            "syllable",
            "vajra",
            "chakra",
            "petal",
            "essence",
        ]
    )

    # Check for sems-side content (delusion mechanism)
    has_sems = any(
        term in content
        for term in [
            "delusion",
            "ignorance",
            "condition",
            "samsara",
            "twelve links",
            "dependent origination",
            "not-know",
            "face not-know",
        ]
    )

    # Check for rigpa-side content (spontaneous presence)
    has_rigpa = any(
        term in content
        for term in [
            "spontaneous",
            "naturally present",
            "self-arisen",
            "primordial",
            "dharmakaya",
            "samantabhadra",
            "crystal light",
            "youth vase",
        ]
    )

    # Check for polemical content
    has_polemical = any(
        phrase in content
        for phrase in [
            "fool",
            "you think",
            "you read this",
            "technical terms for children",
            "beautiful descriptions of empty",
        ]
    )

    # Determine view tags
    if is_patul and has_negation:
        view_tags.append("[DZOGCHEN VIEW – RIGPA SIDE]")
    elif has_rigpa and not has_sems:
        view_tags.append("[DZOGCHEN VIEW – RIGPA SIDE]")
    elif has_sems and not has_rigpa:
        view_tags.append("[DZOGCHEN VIEW – SEMS SIDE]")
    elif has_tantra and not is_patul:
        view_tags.append("[TANTRIC TRANSFORMATIVE VIEW]")
    else:
        view_tags.append("[DZOGCHEN VIEW – RIGPA SIDE]")  # default for Patrul

    # Determine pedagogical tags
    if has_negation and is_patul:
        pedagogical_tags.append("[NEGATIONAL CLEARING]")
    elif has_polemical:
        pedagogical_tags.append("[POLEMICAL DISTINCTION]")
    elif "listen" in content or "look" in content:
        pedagogical_tags.append("[DECLARATIVE FINALITY]")
    elif has_tantra and not is_patul:
        pedagogical_tags.append("[INSTRUCTIONAL PROVISIONALITY]")

    # Determine risk flags
    if has_tantra and not has_negation:
        risk_flags.append("[RISK: REIFICATION]")
    if "nothing" in content or "empty" in content:
        risk_flags.append("[RISK: NIHILISM]")

    # Generate description based on content patterns
    if is_patul:
        if has_negation:
            description = "<Patrul Rinpoche's fireside voice employs negational clearing, using technical description as the basis for direct pointing to non-dual awareness. The commentary consistently undermines its own content to reveal the empty nature of all designation.>"
        elif has_polemical:
            description = "<Polemical Dzogchen instruction challenging conceptual fixation. The Patrul voice rejects sophistication in favor of immediate recognition, cutting through technical elaboration with direct pointing.>"
        else:
            description = "<Direct Dzogchen pointing instruction from the rigpa-side perspective. The fireside voice guides recognition of spontaneous presence beyond all conceptual fabrication.>"
    elif has_sems:
        description = "<Sems-side exposition of delusion's mechanism through twelve links and symbolic narrative. Instructional provisionality marks this as pedagogical framework for understanding samsaric emergence, not ontological assertion.>"
    elif has_tantra:
        description = "<Tantric transformative view describing subtle body mechanics as upāya. Channel, wind, and drop terminology serves contemplative technology rather than anatomical claim.>"
    else:
        description = "<Dzogchen view expressed through the root text's spontaneous presence language. Non-assertive description pointing to the natural state beyond elaboration.>"

    return view_tags, pedagogical_tags, risk_flags, description


def generate_epistemic_file(volume, page_num):
    """Generate epistemic file for a given page"""
    commentary_path = f"volume_{volume}/commentary/PAGE {page_num}.txt"
    epistemic_path = f"volume_{volume}/epistemic/PAGE {page_num}.txt"

    if not os.path.exists(commentary_path):
        return False

    # Skip if already exists
    if os.path.exists(epistemic_path):
        return True

    # Get classifications
    line_range = get_line_range(commentary_path)
    view_tags, pedagogical_tags, risk_flags, description = classify_epistemic(
        commentary_path
    )

    # Generate content
    content = f"{line_range}\n"
    for tag in view_tags:
        content += f"{tag}\n"
    for tag in pedagogical_tags:
        content += f"{tag}\n"
    for flag in risk_flags:
        content += f"{flag}\n"
    content += f"\n{description}\n"

    # Write file
    with open(epistemic_path, "w") as f:
        f.write(content)

    return True


# Generate for Volume 1 pages 366-400
print("Generating Volume 1 pages 366-400...")
for page in range(366, 401):
    if generate_epistemic_file(1, page):
        print(f"  PAGE {page}", end="\r")

print("\nGenerating Volume 1 pages 401-479...")
for page in range(401, 480):
    if generate_epistemic_file(1, page):
        print(f"  PAGE {page}", end="\r")

print("\nGenerating Volume 2 pages 301-350...")
for page in range(301, 351):
    if generate_epistemic_file(2, page):
        print(f"  PAGE {page}", end="\r")

print("\nGenerating Volume 2 pages 351-400...")
for page in range(351, 401):
    if generate_epistemic_file(2, page):
        print(f"  PAGE {page}", end="\r")

print("\nGenerating Volume 2 pages 401-415...")
for page in range(401, 416):
    if generate_epistemic_file(2, page):
        print(f"  PAGE {page}", end="\r")

print("\n\nDone!")
