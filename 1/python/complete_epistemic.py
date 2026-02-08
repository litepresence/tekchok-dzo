#!/usr/bin/env python3
"""
EPISTEMIC LAYER COMPLETION SCRIPT
Masterful Second Draft Generation for Theg mchog mdzod

This script provides a framework for systematically completing the epistemic layer
revision based on the gold-standard exemplars (Volume 1, Pages 1-20).

Usage:
    python complete_epistemic.py --volume 1 --start 21 --end 100
    python complete_epistemic.py --volume 2 --start 1 --end 100
"""

import argparse
import os
import sys
from pathlib import Path

# PROJECT CONFIGURATION
PROJECT_ROOT = Path(
    "/run/user/1000/gvfs/sftp:host=dad,user=oracle/home/oracle/extinction-event/EV/theg pa'i mchog rin po che'i mdzod/1"
)
VOLUME_SIZES = {1: 479, 2: 415}

# MASTERFUL EPISTEMIC STANDARDS
EPSTEMIC_TAGS = {
    "primary_views": [
        "[DZOGCHEN VIEW – RIGPA SIDE]",
        "[DZOGCHEN VIEW – SEMS SIDE]",
        "[TANTRIC TRANSFORMATIVE VIEW]",
        "[SŪTRIC PROVISIONAL VIEW]",
        "[ORDINARY COGNITION]",
        "[NON-ASSERTIVE VIEW]",
    ],
    "pedagogical": [
        "[DECLARATIVE FINALITY]",
        "[INSTRUCTIONAL PROVISIONALITY]",
        "[NEGATIONAL CLEARING]",
        "[POLEMICAL DISTINCTION]",
        "[UPĀYA STATEMENT]",
    ],
    "risk_flags": [
        "[RISK: VIEW COLLAPSE]",
        "[RISK: REIFICATION]",
        "[RISK: NIHILISM]",
        "[RISK: PRACTICE MISREAD AS ONTOLOGY]",
    ],
}

# KEY WYLIE TERMS FOR MASTERFUL ANALYSIS
ESSENTIAL_WYLIE_TERMS = [
    "rig pa",
    "sems",
    "chos sku",
    "longs sku",
    "sprul sku",
    "gzhi",
    "lam",
    "'bras bu",
    "ka dag",
    "lhun grub",
    "chos nyid",
    "rang snang",
    "ye shes",
    "sna tshogs",
    "nges don",
    "drang don",
    "dbyings",
    "klong",
    "sku gsum",
    "phun sum tshogs",
    "rtsal",
    "gdod nas",
]


def validate_epistemic_file(filepath):
    """
    Validate that an epistemic file meets masterful standards.

    Checks:
    - Has line range references [X-Y]
    - Uses standardized tags only
    - Contains Wylie terms in parentheses
    - Has analysis text (not just tags)
    - Proper formatting with angle brackets < >
    """
    issues = []

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        return [f"Cannot read file: {e}"]

    # Check for line range format
    if not any(
        line.strip().startswith("[") and "-" in line for line in content.split("\n")
    ):
        issues.append("Missing line range references [X-Y]")

    # Check for at least one primary view tag
    has_primary = any(tag in content for tag in EPSTEMIC_TAGS["primary_views"])
    if not has_primary:
        issues.append("Missing primary view tag")

    # Check for Wylie terms (asterisks indicate italicized Tibetan)
    if "*" not in content:
        issues.append("Missing Wylie terminology (should be *italicized*)")

    # Check for analysis content between angle brackets
    if "<" not in content or ">" not in content:
        issues.append("Missing analysis text in angle brackets < >")

    # Check analysis length (should be substantive)
    analysis_sections = content.split("<")
    for section in analysis_sections[1:]:  # Skip first split
        if ">" in section:
            analysis = section.split(">")[0]
            if len(analysis.strip()) < 50:
                issues.append(f"Analysis too brief ({len(analysis.strip())} chars)")
                break

    return issues


def get_completion_status():
    """Get current completion status of epistemic layer."""
    status = {}

    for vol in [1, 2]:
        epistemic_dir = PROJECT_ROOT / f"volume_{vol}" / "epistemic"
        if not epistemic_dir.exists():
            status[vol] = {"exists": 0, "total": VOLUME_SIZES[vol]}
            continue

        existing = len(list(epistemic_dir.glob("PAGE *.txt")))
        status[vol] = {
            "exists": existing,
            "total": VOLUME_SIZES[vol],
            "percentage": (existing / VOLUME_SIZES[vol]) * 100,
        }

    return status


def generate_revision_prompt(volume, start_page, end_page):
    """Generate a task prompt for revising a batch of pages."""
    prompt = f"""Revise epistemic layer for Volume {volume}, pages {start_page}-{end_page} to masterful second draft standard.

## EXISTING FILES
These pages already have first-draft epistemic files that need revision.

## MASTERFUL STANDARD (Based on Exemplars Pages 1-20)

Each entry must include:

1. **Precise Line Ranges** - Match actual Tibetan structure
2. **Layered View Tags** - Primary, secondary (if shifting), pedagogical
3. **Wylie Terminology** - Key terms in italics: (*rig pa*, *sems*, *gzhi*, etc.)
4. **Sophisticated Analysis** - 2-4 sentences minimum
5. **Doxographical Precision** - Clear Nyingma positioning
6. **Risk Assessment** - Specific misinterpretation dangers

## OUTPUT FORMAT
```
[lines X-Y]
[PRIMARY VIEW TAG]
[SECONDARY VIEW TAG] (if applicable)
[PEDAGOGICAL TAG]
[RISK FLAG] (when relevant)

<Masterful analysis with Wylie terms (*rig pa*, *chos nyid*, etc.), hermeneutical 
function, pedagogical purpose, and specific risk explanation. 2-4 sentences.>
```

## STANDARDIZED TAGS

**Primary Views:**
- [DZOGCHEN VIEW – RIGPA SIDE] - Definitive awareness view
- [DZOGCHEN VIEW – SEMS SIDE] - Mind-based pedagogical entry  
- [TANTRIC TRANSFORMATIVE VIEW] - Result tantra methods
- [SŪTRIC PROVISIONAL VIEW] - Causal vehicle reasoning
- [ORDINARY COGNITION] - Conventional empirical
- [NON-ASSERTIVE VIEW] - No position asserted

**Pedagogical Functions:**
- [DECLARATIVE FINALITY] - Definitive assertion
- [INSTRUCTIONAL PROVISIONALITY] - Guiding only, not ontology
- [NEGATIONAL CLEARING] - Removing wrong views
- [POLEMICAL DISTINCTION] - Excluding other positions
- [UPĀYA STATEMENT] - Expedient means framing

**Risk Flags:**
- [RISK: VIEW COLLAPSE] - Sutric/Dzogchen confusion
- [RISK: REIFICATION] - Symbol as ontology
- [RISK: NIHILISM] - Negation as denial
- [RISK: PRACTICE MISREAD AS ONTOLOGY]

## WORKFLOW FOR EACH PAGE
1. Read volume_{volume}/tibetan/PAGE N.txt
2. Read volume_{volume}/literal/PAGE N.txt for structure
3. Read volume_{volume}/scholar/PAGE N.txt for technical context
4. Read existing volume_{volume}/epistemic/PAGE N.txt
5. Craft masterful revision with Wylie precision
6. Overwrite with second draft

## EXAMPLE QUALITY
See volume_1/epistemic/PAGE 1.txt or PAGE 10.txt for masterful exemplars.

BEGIN with page {start_page} and continue through {end_page}.
Report progress every 10 pages.
"""
    return prompt


def main():
    parser = argparse.ArgumentParser(
        description="Complete epistemic layer revision for Theg mchog mdzod"
    )
    parser.add_argument(
        "--status", action="store_true", help="Show current completion status"
    )
    parser.add_argument(
        "--validate",
        action="store_true",
        help="Validate existing epistemic files for quality",
    )
    parser.add_argument(
        "--volume", type=int, choices=[1, 2], help="Volume number (1 or 2)"
    )
    parser.add_argument("--start", type=int, help="Starting page number")
    parser.add_argument("--end", type=int, help="Ending page number")
    parser.add_argument(
        "--generate-prompt",
        action="store_true",
        help="Generate task prompt for specified range",
    )

    args = parser.parse_args()

    if args.status:
        print("=== EPISTEMIC LAYER COMPLETION STATUS ===\n")
        status = get_completion_status()

        total_existing = 0
        total_pages = 0

        for vol in [1, 2]:
            s = status[vol]
            total_existing += s["exists"]
            total_pages += s["total"]
            print(
                f"Volume {vol}: {s['exists']}/{s['total']} pages ({s['percentage']:.1f}%)"
            )

        print(
            f"\nTotal: {total_existing}/{total_pages} pages ({(total_existing / total_pages) * 100:.1f}%)"
        )
        print(f"Remaining: {total_pages - total_existing} pages")

        # Check exemplars
        exemplar_path = PROJECT_ROOT / "volume_1" / "epistemic" / "PAGE 1.txt"
        if exemplar_path.exists():
            issues = validate_epistemic_file(exemplar_path)
            if not issues:
                print("\n✓ Exemplar quality (PAGE 1.txt): MASTERFUL")
            else:
                print(f"\n⚠ Exemplar issues: {issues}")

        return

    if args.validate and args.volume:
        print(f"Validating Volume {args.volume} epistemic files...")
        epistemic_dir = PROJECT_ROOT / f"volume_{args.volume}" / "epistemic"

        if not epistemic_dir.exists():
            print(f"Directory not found: {epistemic_dir}")
            return

        files = sorted(epistemic_dir.glob("PAGE *.txt"))
        issues_found = 0

        for filepath in files[:20]:  # Check first 20 as sample
            issues = validate_epistemic_file(filepath)
            if issues:
                print(f"\n{filepath.name}:")
                for issue in issues:
                    print(f"  - {issue}")
                issues_found += 1

        print(f"\nChecked 20 files, {issues_found} with issues")
        return

    if args.generate_prompt and args.volume and args.start and args.end:
        prompt = generate_revision_prompt(args.volume, args.start, args.end)
        print(prompt)
        return

    if args.volume and args.start and args.end:
        print(f"\nTo revise Volume {args.volume}, pages {args.start}-{args.end}:")
        print("\n1. Use this task prompt with the agent system:")
        print("\n" + "=" * 60)
        prompt = generate_revision_prompt(args.volume, args.start, args.end)
        print(prompt)
        print("=" * 60)
        return

    parser.print_help()


if __name__ == "__main__":
    main()
