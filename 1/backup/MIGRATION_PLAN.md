# Content-Based Reorganization Plan
## Theg mchog rin po che'i mdzod - Migration from Page-Based to Section-Based

**Date:** 2026-02-08  
**Status:** Ready for Implementation  
**Principle:** Preserve original structure; create new organized view

---

## Overview

Migrate from page-based files (PAGE_001.txt) to content-based sections (section_A-i.txt) using boundary.json as the authoritative map.

**Original Structure (Preserved):**
- volume_1/ - 479 pages per layer, 9 layers (ARCHIVE)
- volume_2/ - 415 pages per layer, 9 layers (ARCHIVE)

**New Structure (Created):**
- partitioned_v1/ - 53 sections, 9 layers
- partitioned_v2/ - 34 sections, 9 layers

---

## Directory Structure

### New Layer-First Organization

```
partitioned_v1/
├── tibetan/
│   ├── chapter_01/
│   │   └── section_01.txt
│   ├── chapter_02/
│   │   ├── section_A.txt
│   │   ├── section_B.txt
│   │   └── ...
│   └── ...
├── wylie/
├── literal/
├── liturgical/
├── commentary/
├── scholar/
├── epistemic/
├── delusion/
└── cognitive/

partitioned_v2/
└── (same for chapters 14-19)
```

**Naming:**
- Chapters: chapter_XX (01-19)
- Sections: section_X.txt (01, A, A-i, B-ii, etc.)

---

## Migration Process

### Phase 1: Create Structure
Run: `./01_create_structure.sh`

### Phase 2: Extract Content  
Run: `./02_extract_content.py`

Uses boundary.json to extract lines from page files to section files.

### Phase 3: Verify
Run: `./03_verify_migration.py`

Checks line counts, boundary phrases, and completeness.

### Phase 4: Finalize
Original volume_*/ folders remain untouched.

---

## Success Criteria

- All 87 sections extracted
- All 9 layers present
- Line counts match
- Boundary phrases verified
- Original structure intact

---

## Scripts

See accompanying bash and Python scripts for automation.
