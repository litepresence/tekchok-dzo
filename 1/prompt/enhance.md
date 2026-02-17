You have been assigned to update the "cognitive" `<LAYER>` files. 

We are translating one of Longchenpa's Treasuries and approaching final draft stage. Your job is to ENHANCE existing files to A++ exemplar quality.

**Core Enhancement Principles**

A) If content is verbose or full of fluff, condense to its most meaningful essence.  
B) If the Tibetan source is not fully covered, incorporate the most important missing content.  
C) If phrasing can better serve the reader's understanding, reword for clarity and utility.  
D) If content already meets A++ standards, proceed without modification—do not force unnecessary changes.

**Mandatory Requirements**

- Follow the prompt protocol for your assigned `<LAYER>` EXACTLY.  
- Maintain exemplar quality standards throughout all work.

---

**Workflow Protocol**

1. **Scope**  
   - 213 sections exist across all layers. Process one section at a time.  
   - Before beginning, familiarize yourself with the project:  
     - `/home/opencode/MDZOD/1/protocol/navigation.md` (folder/file structure)  
     - `/home/opencode/MDZOD/1/contents/contents.md` (table of contents)  
   - **Important**: The navigation document may be outdated regarding frozen/dynamic file states. Always verify actual file locations in the filesystem.

2. **File Format**  
   - Naming convention: `volume-chapter-section-subsection.txt`  
     Example: `01-01-01-01.txt` = Volume 1, Chapter 1, Section 1, Subsection 1  
   - Chapter 15 begins Volume 2.

3. **Prompt Framework**  
   - Consult structure and language guidance specific to your assigned layer:  
     - `/home/opencode/MDZOD/1/prompt/prompt_<LAYER>.md` 
   - If you have been assigned the commentary layer, pay close attention to all directives as it is complex.  

4. **Review Existing Files**  
   Open files from:  
   - `/home/opencode/MDZOD/1/text/dynamic/<LAYER>`  

   Create a create a comprehensive task list / TODO checklist in your working notes:

   ```
   Review and enhance Volume 1 Chapter 1 (3 sections)
   Review and enhance Volume 1 Chapter 2 (7 sections)
   Review and enhance Volume 1 Chapter 3 (3 sections)
   Review and enhance Volume 1 Chapter 4 (20 sections)
   Review and enhance Volume 1 Chapter 5 (10 sections)
   Review and enhance Volume 1 Chapter 6 (20 sections)
   Review and enhance Volume 1 Chapter 7 (5 sections)
   Review and enhance Volume 1 Chapter 8 (9 sections)
   Review and enhance Volume 1 Chapter 9 (2 sections)
   Review and enhance Volume 1 Chapter 10 (1 section)
   Review and enhance Volume 1 Chapter 11 (2 sections)
   Review and enhance Volume 1 Chapter 12 (8 sections)
   Review and enhance Volume 1 Chapter 13 (6 sections)
   Review and enhance Volume 1 Chapter 14 (17 sections)
   Review and enhance Volume 2 Chapter 15 (3 sections)
   Review and enhance Volume 2 Chapter 16 (5 sections)
   Review and enhance Volume 2 Chapter 17 (15 sections)
   Review and enhance Volume 2 Chapter 18 (25 sections)
   Review and enhance Volume 2 Chapter 19 (2 sections)
   Review and enhance Volume 2 Chapter 20 (9 sections)
   Review and enhance Volume 2 Chapter 21 (2 sections)
   Review and enhance Volume 2 Chapter 22 (10 sections)
   Review and enhance Volume 2 Chapter 23 (20 sections)
   Review and enhance Volume 2 Chapter 24 (1 section)
   Review and enhance Volume 2 Chapter 25 (8 sections)
   ```

5. **Source Verification**  
   Examine current content against root sources:  
   - `/home/opencode/MDZOD/1/text/frozen/tibetan/`  
   - `/home/opencode/MDZOD/1/text/dynamic/liturgical/`  

   **CRITICAL**: Always verify line counts before editing to prevent data loss from partial overwrites.

6. **Exemplar Benchmarking**  
   - Compare all work against best examples in:  
     - `/home/opencode/MDZOD/1/protocol/exemplars.md`  
   - If you discover content surpassing existing exemplars, update the "best of the best" section accordingly.

7. **Quality Assessment**  
   Evaluate each file against A++ standards focusing on:  
   - Literary quality and linguistic elegance  
   - Conceptual coherence  
   - Translation accuracy relative to Tibetan sources  
   - Depth of contextual understanding  
   - Usefulness to the end reader. 

   Provide HONEST Assessment!  Don't sugar coat the remaining work.

   **Important**: Assess every section individually. Do not assume chapter-wide consistency—quality varies within chapters.

8. **File Enhancement**  
   For files below A++ standard, enhance by:  
   - Clarifying ambiguous or obscure concepts  
   - Incorporating contextual depth from Tibetan and liturgical sources  
   - Adhering strictly to layer-specific prompt standards  
   - Producing content worthy of exemplar status

9. **Quality Control Reporting**  
   - **Delete** any existing QC report:  
     - `/home/opencode/MDZOD/1/quality/<LAYER>_QUALITATIVE_QC.md`  
   - Create fresh reports using `quality/Template.md`  and your layer name eg. `<LAYER>_QUALITATIVE_QC.md`  
   - Document every reviewed file with completion status:

   ```
   ## COMPLETION STATUS

   | Volume | Chapter | File | Status | Assessed | Notes |
   |--------|---------|------|--------|----------|-------|
   | 01 | 01 | 01-01-01-01.txt | ✅ A++ COMPLETE | 2026-02-16 | Exemplar quality. No enhancement required. |
   ```

   Every QC Report MUST INCLUDE:

    "⚠️ WEAKEST 10 FILES: [list]"
    "🔴 MOST CRITICAL GAPS: [list]"
    "💡 SUGGESTED IMPROVEMENTS: [minimum 5]"


10. **Iteration**  
    Process all 213 sections systematically until every file meets A++ standards. Maintain quality integrity throughout—do not cut corners.

11. **Time Constraints**  
    Do not concern yourself with time limitations. The system operates on high-power infrastructure enabling rapid processing without quality compromise. Focus solely on producing exemplary work.

12. **Final Reporting**  
    Complete a FULL QUALITATIVE_QC.md report upon finishing all sections. Focus on qualitative assessment—do not substitute statistical analysis for substantive evaluation.

13. **Exemplar Updates**  
    After completing all enhancements, review `exemplars.md` and update the "best of the best" section if your work has produced content exceeding current benchmarks.

14. **Byte Ratios (CRITICAL - Reference `/protocol/byte_ratios.md`)**
    - **ALWAYS** consult `/protocol/byte_ratios.md` before starting work
    - Byte ratios are diagnostic guide rails, NOT quotas or targets
    - **Quality is King:** If content is excellent but outside ratio range, quality wins
    - Calculate ratios using the standard method in byte_ratios.md
    - **Agents may update targets:** If you find ranges consistently produce false alarms (flagging good content as too high/low), update `/protocol/byte_ratios.md` comprehensively
    - When updating, also update any prompts in `/prompt/` that reference your layer
    - Never sacrifice quality to hit a byte target
    - Use ratios to catch potential gaps, not to mandate content volume  

---

**Critical Reminders**

- Never overwrite files without verifying complete content via line count comparison.  
- Review all sections individually; quality varies within chapters.  
- The navigation documentation may not reflect current frozen/dynamic file states—verify actual filesystem structure.  
- Focus on qualitative excellence, not quantitative metrics.

**Final Note**

- Many of the files may already be high quality.   
- Your primary job is to find those that are weak and improve them.  
- Work on the weakest files first!