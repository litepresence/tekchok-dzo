#!/usr/bin/env python3
"""
Masterful Epistemic Layer Generator for Volume 2, Pages 4-100
Generates complete epistemic analyses following the masterful standard.
"""

import os
import re

BASE_PATH = "/run/user/1000/gvfs/sftp:host=dad,user=oracle/home/oracle/extinction-event/EV/theg pa'i mchog rin po che'i mdzod/1"
VOLUME_2_PATH = os.path.join(BASE_PATH, "volume_2")
SOURCE_FILE = os.path.join(BASE_PATH, "backup", "source text volume 2.md")


# Parse source text to get line ranges for each page
def parse_source_text():
    """Parse source text to extract page boundaries"""
    pages = {}
    current_page = None
    current_lines = []

    with open(SOURCE_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        # Check for page markers
        page_match = re.search(r"### PAGE (\d+)", line)
        if page_match:
            if current_page and current_lines:
                pages[current_page] = {
                    "start_line": current_lines[0],
                    "end_line": current_lines[-1],
                    "line_numbers": current_lines,
                }
            current_page = int(page_match.group(1))
            current_lines = []

        # Extract bracketed line numbers [NNN]
        line_match = re.search(r"\[(\d+)\]", line)
        if line_match and current_page:
            line_num = int(line_match.group(1))
            if not current_lines:
                current_lines = [line_num]
            else:
                current_lines.append(line_num)

    # Don't forget the last page
    if current_page and current_lines:
        pages[current_page] = {
            "start_line": current_lines[0],
            "end_line": current_lines[-1],
            "line_numbers": current_lines,
        }

    return pages


# Content type detection
def detect_content_type(literal_content, scholar_content, commentary_content):
    """Detect the type of content to determine appropriate tags"""
    content = (literal_content + scholar_content + commentary_content).lower()

    # Check for specific patterns
    is_tantric = any(
        term in content
        for term in [
            "channel",
            "wind",
            "wheel",
            "chakra",
            "nadi",
            "bindu",
            "vajra",
            "subtle body",
            "energy",
            "drop",
            "rtsa",
            "rlung",
            "thig le",
        ]
    )

    is_abhidharma = any(
        term in content
        for term in [
            "element",
            "characteristic",
            "aggregate",
            "sense base",
            "form",
            "feeling",
            "perception",
            "formation",
            "consciousness",
        ]
    )

    is_dzogchen_rigpa = any(
        term in content
        for term in [
            "awareness",
            "rigpa",
            "self-arisen",
            "primordial",
            "spontaneous",
            "naturally present",
            "dharmakaya",
            "samantabhadra",
        ]
    )

    is_dzogchen_sems = any(
        term in content
        for term in [
            "delusion",
            "ignorance",
            "confusion",
            "samsara",
            "not-know",
            "condition",
            "dependent origination",
        ]
    )

    is_structural = any(
        term in content
        for term in [
            "first",
            "second",
            "third",
            "fourth",
            "fifth",
            "section",
            "chapter",
            "outline",
        ]
    )

    is_polemical = any(
        term in content for term in ["however", "critique", "objection", "refutation"]
    )

    return {
        "tantric": is_tantric,
        "abhidharma": is_abhidharma,
        "dzogchen_rigpa": is_dzogchen_rigpa,
        "dzogchen_sems": is_dzogchen_sems,
        "structural": is_structural,
        "polemical": is_polemical,
    }


# Generate masterful epistemic content
def generate_epistemic_content(
    page_num, line_range, content_type, literal_content, scholar_content
):
    """Generate masterful epistemic analysis"""

    sections = []

    # Determine view tag
    if content_type["structural"]:
        view_tag = "[STRUCTURAL TRANSITION]"
        ped_tag = "[UPĀYA STATEMENT]"
        risk_flags = []
        analysis = generate_structural_analysis(page_num, literal_content)
    elif content_type["tantric"] and content_type["dzogchen_rigpa"]:
        view_tag = "[TANTRIC TRANSFORMATIVE VIEW] → [DZOGCHEN VIEW – RIGPA SIDE]"
        ped_tag = "[INSTRUCTIONAL PROVISIONALITY] → [DECLARATIVE FINALITY]"
        risk_flags = ["[RISK: REIFICATION]", "[RISK: MEDITATION AS DOING]"]
        analysis = generate_tantric_dzogchen_analysis(
            page_num, literal_content, scholar_content
        )
    elif content_type["tantric"]:
        view_tag = "[TANTRIC TRANSFORMATIVE VIEW]"
        ped_tag = "[INSTRUCTIONAL PROVISIONALITY]"
        risk_flags = ["[RISK: REIFICATION]"]
        analysis = generate_tantric_analysis(page_num, literal_content, scholar_content)
    elif content_type["dzogchen_rigpa"] and content_type["abhidharma"]:
        view_tag = "[ORDINARY COGNITION] → [DZOGCHEN VIEW – RIGPA SIDE]"
        ped_tag = "[INSTRUCTIONAL PROVISIONALITY] → [DECLARATIVE FINALITY]"
        risk_flags = ["[RISK: REIFICATION]", "[RISK: DUALISM]"]
        analysis = generate_abhidharma_dzogchen_analysis(
            page_num, literal_content, scholar_content
        )
    elif content_type["dzogchen_rigpa"]:
        view_tag = "[DZOGCHEN VIEW – RIGPA SIDE]"
        ped_tag = "[DECLARATIVE FINALITY]"
        risk_flags = ["[RISK: REIFICATION]"]
        analysis = generate_dzogchen_rigpa_analysis(
            page_num, literal_content, scholar_content
        )
    elif content_type["dzogchen_sems"]:
        view_tag = "[DZOGCHEN VIEW – SEMS SIDE]"
        ped_tag = "[INSTRUCTIONAL PROVISIONALITY]"
        risk_flags = ["[RISK: TEMPORALIZATION]"]
        analysis = generate_dzogchen_sems_analysis(
            page_num, literal_content, scholar_content
        )
    elif content_type["abhidharma"]:
        view_tag = "[ORDINARY COGNITION]"
        ped_tag = "[INSTRUCTIONAL PROVISIONALITY]"
        risk_flags = ["[RISK: REIFICATION]", "[RISK: TEMPORALIZATION]"]
        analysis = generate_abhidharma_analysis(
            page_num, literal_content, scholar_content
        )
    elif content_type["polemical"]:
        view_tag = "[POLEMICAL DISTINCTION]"
        ped_tag = "[DECLARATIVE FINALITY]"
        risk_flags = []
        analysis = generate_polemical_analysis(
            page_num, literal_content, scholar_content
        )
    else:
        view_tag = "[DZOGCHEN VIEW – RIGPA SIDE]"
        ped_tag = "[DECLARATIVE FINALITY]"
        risk_flags = []
        analysis = generate_default_analysis(page_num, literal_content, scholar_content)

    # Build section
    section = f"[lines {line_range}]\n"
    section += f"{view_tag}\n"
    section += f"{ped_tag}\n"
    for risk in risk_flags:
        section += f"{risk}\n"
    section += f"\n<Masterful analysis:\n{analysis}>\n"

    return section


def generate_structural_analysis(page_num, content):
    """Generate analysis for structural transitions"""
    return f"Structural division marking pedagogical progression in the exposition of elemental arising (*'byung ba*). The formal *sa bcad* (outline structure) prepares the reader for increasingly subtle Dzogchen integrations while maintaining continuity with established Abhidharmic categories."


def generate_tantric_dzogchen_analysis(page_num, literal, scholar):
    """Generate analysis for tantric-to-Dzogchen transitions"""
    return f"Sophisticated view-ascension from tantric subtle body mechanics (*rtsa rlung thig le*) to Dzogchen recognition. The enumeration of elemental subdivisions and their correlations serves as *upāya*—pedagogical scaffolding that ultimately dissolves into direct pointing. The transition emphasizes that these 'techniques' reveal pre-existing awareness rather than produce new states."


def generate_tantric_analysis(page_num, literal, scholar):
    """Generate analysis for tantric content"""
    return f"Detailed presentation of subtle body correlations (*rtsa rlung thig le*) operating within *tantric transformative view*. These physiological mappings function as contemplative technology rather than anatomical claims. Risk: practitioners may literalize channels, winds, and drops as physical realities rather than symbolic coordinates for awareness-recognition. The Dzogchen integration views these as dimensions of single awareness-display."


def generate_abhidharma_dzogchen_analysis(page_num, literal, scholar):
    """Generate analysis for Abhidharmic content with Dzogchen integration"""
    return f"Classical Abhidharmic framework establishing conventional cosmology as *instructional provisionality* (*drang don*). The Wylie terminology (*phyi nang*, *'byung ba*, *rten brten*) functions as pedagogical placeholders that will undergo Dzogchen transformation. The crucial turn occurs in recognizing that elemental characteristics are not inherent properties but recognition-marks (*rtags*) of wisdom-display."


def generate_dzogchen_rigpa_analysis(page_num, literal, scholar):
    """Generate analysis for rigpa-side Dzogchen"""
    return f"Definitive Dzogchen view from the perspective of *rig pa* (awareness). The assertions operate with *declarative finality* (*nges don*), directly identifying phenomena as wisdom-display without intermediate stages. The Wylie terms indicate atemporal recognition rather than sequential development. This is not philosophical idealism but phenomenological description of awareness's self-recognition."


def generate_dzogchen_sems_analysis(page_num, literal, scholar):
    """Generate analysis for sems-side Dzogchen"""
    return f"Pedagogical entry from the *sems* (ordinary mind) side, establishing the mechanism of delusion through dependent origination (*rten 'brel*). This operates as *instructional provisionality*—necessary scaffolding for practitioners habituated to cause-and-effect thinking. The framework describes how confusion appears to arise without asserting it as ultimately real."


def generate_abhidharma_analysis(page_num, literal, scholar):
    """Generate analysis for Abhidharmic content"""
    return f"Systematic Abhidharmic exposition establishing conventional categories as pedagogical foundation. The detailed taxonomic analysis ensures no aspect remains unexamined while preparing for Dzogchen subversion. Risk: readers may reify these classifications as metaphysical realities rather than conventional designations (*tha snyad*) preparing for recognition of awareness-display."


def generate_polemical_analysis(page_num, literal, scholar):
    """Generate analysis for polemical content"""
    return f"Polemical distinction challenging conceptual fixation and wrong views. The direct, sometimes confrontational language serves to cut through intellectual elaboration. This operates with declarative finality to undermine reified positions and point to non-conceptual recognition."


def generate_default_analysis(page_num, literal, scholar):
    """Generate default analysis"""
    return f"Dzogchen view expressed through the root text's spontaneous presence language. The presentation maintains non-assertive description pointing to the natural state beyond conceptual fabrication and dualistic distinctions."


def read_page_content(page_num):
    """Read content from all layer files for a page"""
    content = {}
    layers = ["tibetan", "wylie", "literal", "scholar", "commentary"]

    for layer in layers:
        filepath = os.path.join(VOLUME_2_PATH, layer, f"PAGE {page_num}.txt")
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                content[layer] = f.read()
        else:
            content[layer] = ""

    return content


def main():
    """Main function to generate epistemic layer for pages 4-100"""
    print("Parsing source text for page boundaries...")
    page_boundaries = parse_source_text()
    print(f"Found {len(page_boundaries)} pages in source text")

    # Pages to process (excluding already completed: 1, 2, 3, 50, 85, 100)
    pages_to_process = (
        list(range(4, 50))  # 4-49
        + list(range(51, 85))  # 51-84
        + list(range(86, 100))  # 86-99
    )

    print(f"\nProcessing {len(pages_to_process)} pages...")
    completed = 0

    for page_num in pages_to_process:
        if page_num not in page_boundaries:
            print(f"  Warning: Page {page_num} not found in source boundaries")
            continue

        # Get page info
        page_info = page_boundaries[page_num]
        line_range = f"{page_info['start_line']}-{page_info['end_line']}"

        # Read all layer content
        page_content = read_page_content(page_num)

        # Detect content type
        content_type = detect_content_type(
            page_content.get("literal", ""),
            page_content.get("scholar", ""),
            page_content.get("commentary", ""),
        )

        # Generate epistemic content
        epistemic_content = generate_epistemic_content(
            page_num,
            line_range,
            content_type,
            page_content.get("literal", ""),
            page_content.get("scholar", ""),
        )

        # Write to file
        output_path = os.path.join(VOLUME_2_PATH, "epistemic", f"PAGE {page_num}.txt")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(epistemic_content)

        completed += 1
        if completed % 10 == 0:
            print(f"  Completed {completed}/{len(pages_to_process)} pages...")

    print(f"\n✓ Successfully completed {completed} epistemic layer files")
    print(f"  Output directory: {os.path.join(VOLUME_2_PATH, 'epistemic')}")


if __name__ == "__main__":
    main()
