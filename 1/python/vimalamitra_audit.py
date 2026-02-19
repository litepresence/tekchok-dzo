#!/usr/bin/env python3
"""
Vimalamitra Comprehensive Text Audit
Audits all 213 sections across Tibetan/Wylie/Literal/Liturgical layers
"""

import os
import re
import glob
from pathlib import Path

BASE_DIR = "/home/opencode/MDZOD/1/text/frozen"
LAYERS = ["tibetan", "wylie", "literal", "liturgical"]

def get_line_count(filepath):
    """Count lines in file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return len(f.readlines())
    except Exception as e:
        return -1

def check_line_numbers(filepath):
    """Verify line numbers are sequential"""
    issues = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            expected = 1
            for i, line in enumerate(lines, 1):
                match = re.match(r'^\[(\d+)\]', line)
                if match:
                    actual = int(match.group(1))
                    if actual != expected:
                        issues.append(f"Line {i}: expected [{expected}], found [{actual}]")
                    expected = actual + 1
    except Exception as e:
        issues.append(f"Error reading file: {e}")
    return issues

def check_liturgical_tags(filepath):
    """Check liturgical layer has proper XML tags"""
    issues = []
    valid_tags = ['<verse>', '<prose>', '<tantra>', '<mantra>', '<ornament>', '<list>', '<break>']
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for i, line in enumerate(lines, 1):
                if line.strip() and not line.startswith('[1]'):
                    # Check for tags after line number
                    has_tag = any(tag in line for tag in valid_tags)
                    if not has_tag and not line.strip().endswith('>'):
                        # Skip lines that are just numbers or ornaments
                        content = re.sub(r'^\[\d+\]\s*', '', line).strip()
                        if content and not content.startswith('<') and not content.startswith('༄'):
                            issues.append(f"Line {i}: Missing XML tag")
    except Exception as e:
        issues.append(f"Error: {e}")
    return issues

def audit_section(filename):
    """Audit a single section across all layers"""
    results = {
        'filename': filename,
        'line_counts': {},
        'issues': []
    }
    
    # Check line counts
    counts = []
    for layer in LAYERS:
        filepath = os.path.join(BASE_DIR, layer, filename)
        count = get_line_count(filepath)
        results['line_counts'][layer] = count
        counts.append(count)
    
    # Check if all counts match
    if len(set(counts)) != 1:
        results['issues'].append(f"LINE COUNT MISMATCH: {results['line_counts']}")
    
    # Check line numbering in each layer
    for layer in LAYERS:
        filepath = os.path.join(BASE_DIR, layer, filename)
        numbering_issues = check_line_numbers(filepath)
        if numbering_issues:
            results['issues'].extend([f"{layer}: {issue}" for issue in numbering_issues[:5]])
    
    # Check liturgical tags
    liturgical_path = os.path.join(BASE_DIR, "liturgical", filename)
    if os.path.exists(liturgical_path):
        tag_issues = check_liturgical_tags(liturgical_path)
        if tag_issues:
            results['issues'].extend([f"liturgical: {issue}" for issue in tag_issues[:5]])
    
    return results

def main():
    """Main audit function"""
    print("=" * 80)
    print("VIMALAMITRA COMPREHENSIVE TEXT AUDIT")
    print("Theg mchog rin po che'i mdzod - Treasury of the Supreme Vehicle")
    print("=" * 80)
    print()
    
    # Get all files from tibetan layer (source of truth)
    tibetan_dir = os.path.join(BASE_DIR, "tibetan")
    files = sorted(glob.glob(os.path.join(tibetan_dir, "*.txt")))
    
    total_files = len(files)
    print(f"Total sections to audit: {total_files}")
    print()
    
    # Track statistics
    perfect_files = 0
    files_with_issues = 0
    total_issues = 0
    
    # Process each file
    for i, filepath in enumerate(files, 1):
        filename = os.path.basename(filepath)
        results = audit_section(filename)
        
        if results['issues']:
            files_with_issues += 1
            total_issues += len(results['issues'])
            print(f"[{i}/{total_files}] {filename}")
            for issue in results['issues']:
                print(f"  ⚠️  {issue}")
            print()
        else:
            perfect_files += 1
            if i % 50 == 0:
                print(f"[{i}/{total_files}] {filename} ✓")
    
    # Summary
    print()
    print("=" * 80)
    print("AUDIT SUMMARY")
    print("=" * 80)
    print(f"Total sections audited: {total_files}")
    print(f"Perfect sections: {perfect_files}")
    print(f"Sections with issues: {files_with_issues}")
    print(f"Total issues found: {total_issues}")
    print()
    
    if files_with_issues == 0:
        print("✅ ALL SECTIONS PASS - Line counts match, numbering is sequential")
    else:
        print(f"⚠️  {files_with_issues} sections require attention")
    
    return files_with_issues

if __name__ == "__main__":
    exit_code = main()
    exit(exit_code)
