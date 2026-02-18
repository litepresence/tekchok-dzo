#!/usr/bin/env python3
"""
Rebuild all 5 commentary layers with correct paragraph grouping.
Layers: commentary, cognitive, delusion, epistemic, scholar
"""

import re
from pathlib import Path

BASE_DIR = Path("/home/opencode/MDZOD/1")
RESTORED_BASE = Path("/home/opencode/text/dynamic_restored")
LAYERS = ["commentary", "cognitive", "delusion", "epistemic", "scholar"]

def parse_restored_structure(filepath):
    """Parse restored file to get line ranges and their paragraph counts."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    structure = []
    current_range = None
    paragraphs_in_current = 0
    
    for line in lines:
        stripped = line.strip()
        match = re.match(r'^(\[\d+-?\d*\])', stripped)
        
        if match:
            if current_range:
                structure.append((current_range, paragraphs_in_current))
            current_range = match.group(1)
            paragraphs_in_current = 0
            text_after = stripped[len(match.group(1)):].strip()
            if text_after:
                paragraphs_in_current += 1
        elif stripped and current_range:
            paragraphs_in_current += 1
    
    if current_range:
        structure.append((current_range, paragraphs_in_current))
    
    return structure

def parse_current_paragraphs(filepath):
    """Extract all paragraphs from current dynamic file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    raw_paragraphs = content.split('\n\n')
    paragraphs = []
    
    for para in raw_paragraphs:
        para = para.strip()
        if para:
            para = ' '.join(para.split())
            paragraphs.append(para)
    
    return paragraphs

def calculate_new_grouping(original_groups, total_current):
    """Calculate new paragraph grouping proportionally."""
    total_original = sum(original_groups)
    
    if total_current == total_original:
        return original_groups
    
    if total_current < len(original_groups):
        return [1] * total_current + [0] * (len(original_groups) - total_current)
    
    new_groups = []
    for g in original_groups:
        prop = g / total_original if total_original > 0 else 1/len(original_groups)
        new_count = max(1, round(prop * total_current))
        new_groups.append(new_count)
    
    diff = sum(new_groups) - total_current
    if diff > 0:
        for i in range(len(new_groups)-1, -1, -1):
            if diff <= 0:
                break
            if new_groups[i] > 1:
                new_groups[i] -= 1
                diff -= 1
    elif diff < 0:
        for i in range(len(new_groups)):
            if diff >= 0:
                break
            new_groups[i] += 1
            diff += 1
    
    return new_groups

def rebuild_layer(layer_name):
    """Rebuild a single layer."""
    print(f"\n{'='*60}")
    print(f"PROCESSING: {layer_name.upper()}")
    print('='*60)
    
    restored_dir = RESTORED_BASE / layer_name
    current_dir = BASE_DIR / "text/dynamic" / layer_name
    output_dir = BASE_DIR / "text/final" / layer_name
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    if not restored_dir.exists():
        print(f"  ERROR: Restored directory not found: {restored_dir}")
        return 0, 0
    
    if not current_dir.exists():
        print(f"  ERROR: Current directory not found: {current_dir}")
        return 0, 0
    
    current_files = list(current_dir.glob("*.txt"))
    print(f"  Files to process: {len(current_files)}")
    
    processed = 0
    errors = []
    files_adjusted = 0
    
    for i, file_path in enumerate(sorted(current_files)):
        filename = file_path.name
        restored_path = restored_dir / filename
        output_path = output_dir / filename
        
        if not restored_path.exists():
            continue
        
        try:
            # Get structures
            structure = parse_restored_structure(restored_path)
            if not structure:
                continue
                
            line_ranges = [r for r, _ in structure]
            original_groups = [c for _, c in structure]
            
            current_paragraphs = parse_current_paragraphs(file_path)
            total_current = len(current_paragraphs)
            
            # Check if adjustment needed
            if sum(original_groups) != total_current:
                files_adjusted += 1
            
            # Calculate new grouping
            new_groups = calculate_new_grouping(original_groups, total_current)
            
            # Rebuild content
            output_lines = []
            para_idx = 0
            
            for j, line_range in enumerate(line_ranges):
                num_paras = new_groups[j] if j < len(new_groups) else 0
                if num_paras == 0:
                    continue
                
                output_lines.append(line_range)
                
                for _ in range(num_paras):
                    if para_idx < len(current_paragraphs):
                        output_lines.append(current_paragraphs[para_idx])
                        para_idx += 1
                
                output_lines.append('')
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(output_lines))
            
            processed += 1
            
            if (i + 1) % 50 == 0:
                print(f"    Processed {i + 1}/{len(current_files)}...")
                
        except Exception as e:
            errors.append(f"{filename}: {e}")
    
    print(f"  ✓ Complete: {processed} files processed")
    print(f"  Files with adjusted paragraph counts: {files_adjusted}")
    if errors:
        print(f"  Errors: {len(errors)}")
        for err in errors[:3]:
            print(f"    {err}")
    
    return processed, files_adjusted

def main():
    print("="*60)
    print("REBUILDING ALL 5 LAYERS")
    print("="*60)
    print()
    print("Source: Line numbers from commit 28ec555e")
    print("Content: Current text/dynamic/{layer}/")
    print("Output: text/final/{layer}/")
    print()
    
    total_files = 0
    total_adjusted = 0
    
    for layer in LAYERS:
        files, adjusted = rebuild_layer(layer)
        total_files += files
        total_adjusted += adjusted
    
    print("\n" + "="*60)
    print("FINAL SUMMARY")
    print("="*60)
    print(f"Total files processed: {total_files}")
    print(f"Total files with adjusted grouping: {total_adjusted}")
    print()
    print("✓ All 5 layers rebuilt with:")
    print("  - Line number ranges from commit 28ec555e")
    print("  - Paragraph grouping maintained proportionally")
    print("  - Content from current dynamic files")

if __name__ == "__main__":
    main()
