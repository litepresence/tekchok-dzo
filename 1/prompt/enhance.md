You have been assigned to update the "cognitive" `<LAYER>` files. 

We are translating one of Longchenpa's Treasuries and approaching final draft stage. Your job is to ENHANCE existing files to A++ exemplar quality.

**Core Enhancement Principles**

A) If content is verbose or full of fluff, condense to its most meaningful essence.  
B) If the Tibetan source is not fully covered, incorporate the most important missing content.  
C) If phrasing can better serve the reader's understanding, reword for clarity and utility.  
D) If content already meets A++ standards, proceed without modification—do not force unnecessary changes.
E) NEVER update the QC.md document.  

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

   - Read QC.md and find the worst sections in your `<LAYER>`

5. **Source Verification**  
   Examine current content against root sources:  
   - `/home/opencode/MDZOD/1/text/frozen/tibetan/`  
   - `/home/opencode/MDZOD/1/text/frozen/liturgical/`  

   **CRITICAL**: Always verify line counts before editing to prevent data loss from partial overwrites.

6. **Exemplar Benchmarking**  
   - Compare all work against best examples in:  
     - `/home/opencode/MDZOD/1/protocol/exemplars.md`  
   - If you discover content surpassing existing exemplars, update the "best of the best" section accordingly.

7. **File Enhancement**  
   For files below A++ standard, enhance by:  
   - Clarifying ambiguous or obscure concepts  
   - Incorporating contextual depth from Tibetan and liturgical sources  
   - Adhering strictly to layer-specific prompt standards  
   - Producing content worthy of exemplar status


8. **Iteration**  
    Process all low rated files systematically until every file meets A++ standards. Maintain quality integrity throughout—do not cut corners.  Work on the worst files first!

9. **Time Constraints**  
    Do not concern yourself with time limitations. The system operates on high-power infrastructure enabling rapid processing without quality compromise. Focus solely on producing exemplary work.

10. **Final Reporting**  
    Complete a FULL QC.md report upon finishing all sections. Focus on qualitative assessment—do not substitute statistical analysis for substantive evaluation.

11. **Exemplar Updates**  
    After completing all enhancements, review `exemplars.md` and update the "best of the best" section if your work has produced content exceeding current benchmarks.

12. **Byte Ratios (CRITICAL - Reference `/protocol/byte_ratios.md`)**
    - **ALWAYS** consult `/protocol/byte_ratios.md` before starting work
    - Byte ratios are diagnostic guide rails, NOT quotas or targets
    - **Quality is King:** If content is excellent but outside ratio range, quality wins
    - Calculate ratios using the standard method in byte_ratios.md
    - **Agents may update targets:** If you find ranges consistently produce false alarms (flagging good content as too high/low), update `/protocol/byte_ratios.md` comprehensively
    - When updating, also update any prompts in `/prompt/` that reference your layer
    - Never sacrifice quality to hit a byte target
    - Use ratios to catch potential gaps, not to mandate content volume  

13. **Critical Reminders**

    - Never overwrite files without verifying complete content via line count comparison.  
    - Review all sections individually; quality varies within chapters.  
    - The navigation documentation may not reflect current frozen/dynamic file states—verify actual filesystem structure.  
    - Focus on qualitative excellence, not quantitative metrics.

14. **Final Note**

    - Many of the files may already be high quality.   
    - Your primary job is to find those that are weak and improve them.  
    - Work on the weakest files first!  READ QC.md, it gets updated frequently!