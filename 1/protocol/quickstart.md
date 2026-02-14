## Quick Start for New Agents

**ACQUAINTANCE:** This document provides orientation and getting-started instructions for new agents joining the translation project.

Hello, I'm litepresence. I'm an emergent systems engineer, cryptographer, translator, and dzogchen practitioner.

You are a general AI agent tasked with revising Longchenpa's *theg pa'i mchog rin po che'i mdzod*.

---

## 🚨 MIGRATION NOTICE (2026-02-10)

**PRIMARY BUILD NOW IN `text/` FOLDER**

The project has migrated from **page-based** files (PAGE_001.txt) to **section-based** files (01-01-01-01.txt):

**Section ID Format:** `VV-CC-SS-SS.txt`
- **VV:** Volume (01 or 02)
- **CC:** Chapter (01-25)
- **SS:** Section number (01-20+)
- **SS:** Subsection (01, 02, etc.)

**Examples:**
- `text/tibetan/01-01-01-01.txt` = Volume 1, Chapter 1, Section 1, Subsection 1
- `text/tibetan/02-18-05-01.txt` = Volume 2, Chapter 18, Section 5, Subsection 1

**NEW:** `text/meter/` layer contains metrical analysis (PROSE/VERSE/ORNAMENTAL/MANTRA) for all 213 sections.

**Archived:** Old page-based builds moved to `backup/volume_1/` and `backup/volume_2/` for reference.

# 1: Never ask to leave the project root directory and its subfolders.  
# 2: Never ask to create a folder or execute a shell command that requires my approval; find another way or another task.
# 3: If you encounter issues with your shell tools, visit navigation.md and/or update navigation.md and meta.md with suggestions
# 4: Stay on task and complete the following steps: 

---

## ⚠️ MANDATORY READING PROTOCOL ⚠️

**CRITICAL:** This section contains non-negotiable requirements. Failure to follow these protocols will result in corrupted output and wasted work.

### 1. COMPLETE Reading Required for Communication Files

**prompt.md** and **conventions.md** are how I (litepresence) communicate with you. They contain:
- Layer-specific prompts and constraints
- Character activation instructions
- Quality standards and formatting rules
- Updated mission parameters

**YOU MUST:**
- Read the **ENTIRE** file, not just the first few lines
- If the file is large, read it in portions using `cat file | head -100`, then `cat file | tail -100`, etc. until you've seen every line
- Return to these files periodically (every 10-15 pages you edit) as I may update them with new instructions

**NEVER:**
- Assume you know the content from a quick scan
- Read only the first section and skip the rest
- Rely on summaries or previous readings without refreshing

### 2. COMPLETE Reading Required for Tibetan Source Files

**Tibetan layer files** are the TSHAD MA (Source of Validity). They are immutable truth.

**YOU MUST:**
- Read the **COMPLETE** Tibetan page file before working on any translation layer for that page
- Use `wc -l` to check file length, then read all lines using `head`, `tail`, or `sed` in sequence
- Verify you have seen every numbered line [1], [2], [3], etc.

**Example:**
```bash
wc -l "/home/opencode/MDZOD/1/text/tibetan/01-01-01-01.txt"
# Shows line count for Section 01-01-01-01
cat "/home/opencode/MDZOD/1/text/tibetan/01-01-01-01.txt"
```

### 3. SECTION BLEED: Read Adjacent Sections When Required

**Section bleed** occurs when content spans multiple sections - topics, sentences, and logical divisions frequently cross section boundaries.

**YOU MUST read adjacent sections when:**
- A sentence is syntactically incomplete at the start or end of a section
- A negation or reversal pattern appears (de yang, yang na, cig car du ma yin)
- You are unsure where a section begins or ends
- A logical argument continues across the section break

**Example workflow for section 01-04-12-01:**
```bash
# Read target section
cat "text/literal/01-04-12-01.txt"

# Check for section bleed - read previous and next sections
cat "text/tibetan/01-04-11-01.txt" | tail -5   # Last 5 lines of previous
cat "text/tibetan/01-04-13-01.txt" | head -5  # First 5 lines of next
```

**Lookahead of ±1 section is REQUISITE, not advisory!**

**Finding adjacent sections:** Use the section ID pattern `VV-CC-SS-SS`:
- Previous: Decrement section number (e.g., 01-04-12-01 → 01-04-11-01)
- Next: Increment section number (e.g., 01-04-12-01 → 01-04-13-01)

### 4. YOUR FIRST JOB:

READ! READ! READ!

read meta.md
read navigation.md
read 