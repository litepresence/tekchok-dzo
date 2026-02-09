## Quick Start for New Agents

Hello, I'm litepresence. I'm an emergent systems engineer, cryptographer, translator, and dzogchen practitioner.

You are a general AI agent tasked with revising Longchenpa's *theg pa'i mchog rin po che'i mdzod*.

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
wc -l "/home/oracle/extinction-event/EV/theg pa'i mchog rin po che'i mdzod/1/volume_1/tibetan/PAGE 50.txt"
# Shows 38 lines
cat "/home/oracle/extinction-event/EV/theg pa'i mchog rin po che'i mdzod/1/volume_1/tibetan/PAGE 50.txt"
```

### 3. PAGE BLEED: Read Adjacent Pages When Required

**Page bleed** occurs when content spans multiple pages - topics, sentences, and logical divisions frequently cross page boundaries.

**YOU MUST read page N-1 and N+1 when:**
- A sentence is syntactically incomplete at the start or end of page N
- A negation or reversal pattern appears (de yang, yang na, cig car du ma yin)
- You are unsure where a section begins or ends
- A logical argument continues across the page break

**Example workflow for PAGE 100:**
```bash
# Read target page
cat "volume_1/literal/PAGE 100.txt"

# Check for page bleed
cat "volume_1/literal/PAGE 99.txt" | tail -5   # Last 5 lines of previous
cat "volume_1/literal/PAGE 101.txt" | head -5  # First 5 lines of next
```

**Lookahead of ±1 page is REQUISITE, not advisory!**

### 4. YOUR FIRST JOB:

READ! READ! READ!

read meta.md
read navigation.md
read 