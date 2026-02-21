#!/usr/bin/env python3
"""
Liturgical Meter Transformation Script
Transforms liturgical layer for breath, meter, and resonance
"""

import os
import re
import sys
import shutil
from pathlib import Path

BASE_DIR = "/home/opencode/MDZOD/1/text/frozen"
LITURGICAL_DIR = os.path.join(BASE_DIR, "liturgical")
TIBETAN_DIR = os.path.join(BASE_DIR, "tibetan")
BACKUP_DIR = os.path.join(BASE_DIR, "liturgical_backup")

def count_words_in_line(line):
    """Count words in a line (excluding tags and line numbers)"""
    # Remove line number and tags
    cleaned = re.sub(r'^\[\d+\]\s*<[^>]+>\s*', '', line)
    # Remove verse markers
    cleaned = re.sub(r'\|\|\s*\d+\s*\|\|', '', cleaned)
    # Count words
    return len(cleaned.split())

def is_long_line(line, threshold=15):
    """Check if line is too long for comfortable breath"""
    return count_words_in_line(line) > threshold

def transform_verse_line(line):
    """Transform verse line for better meter (8-12 words target)"""
    # This is a placeholder - actual transformation requires
    # understanding Tibetan meaning and careful rephrasing
    word_count = count_words_in_line(line)
    if word_count <= 12:
        return line  # Already good length
    # Lines >12 words need careful editing
    # For now, just flag them
    return line

def transform_prose_line(line):
    """Transform prose line for better breath (max 15 words)"""
    word_count = count_words_in_line(line)
    if word_count <= 15:
        return line  # Already good
    # Lines >15 words should be simplified
    # Remove unnecessary words while preserving meaning
    return line

def process_file(filename):
    """Process a single liturgical file"""
    filepath = os.path.join(LITURGICAL_DIR, filename)
    tibetan_path = os.path.join(TIBETAN_DIR, filename)
    
    if not os.path.exists(filepath):
        print(f"File not found: {filename}")
        return False
    
    if not os.path.exists(tibetan_path):
        print(f"Tibetan source not found: {filename}")
        return False
    
    # Read files
    with open(filepath, 'r', encoding='utf-8') as f:
        liturgical_lines = f.readlines()
    
    with open(tibetan_path, 'r', encoding='utf-8') as f:
        tibetan_lines = f.readlines()
    
    # Check line count
    if len(liturgical_lines) != len(tibetan_lines):
        print(f"LINE COUNT MISMATCH: {filename}")
        print(f"  Liturgical: {len(liturgical_lines)}")
        print(f"  Tibetan: {len(tibetan_lines)}")
        return False
    
    # Analyze content
    verse_lines = 0
    prose_lines = 0
    tantra_lines = 0
    long_lines = 0
    
    for line in liturgical_lines:
        if '<verse>' in line:
            verse_lines += 1
            if is_long_line(line, 12):
                long_lines += 1
        elif '<prose>' in line:
            prose_lines += 1
            if is_long_line(line, 15):
                long_lines += 1
        elif '<tantra>' in line:
            tantra_lines += 1
    
    stats = {
        'filename': filename,
        'total_lines': len(liturgical_lines),
        'verse_lines': verse_lines,
        'prose_lines': prose_lines,
        'tantra_lines': tantra_lines,
        'long_lines': long_lines
    }
    
    return stats

def main():
    """Main processing function"""
    print("="*70)
    print("LITURGICAL METER TRANSFORMATION")
    print("="*70)
    print()
    
    # Get all liturgical files
    files = sorted([f for f in os.listdir(LITURGICAL_DIR) if f.endswith('.txt')])
    
    print(f"Total files to analyze: {len(files)}")
    print()
    
    # Analyze all files
    all_stats = []
    files_with_issues = []
    
    for i, filename in enumerate(files, 1):
        stats = process_file(filename)
        if stats:
            all_stats.append(stats)
            if stats['long_lines'] > 0:
                files_with_issues.append(stats)
        
        if i % 50 == 0:
            print(f"Analyzed {i}/{len(files)} files...")
    
    print()
    print("="*70)
    print("ANALYSIS COMPLETE")
    print("="*70)
    print()
    
    # Summary statistics
    total_verse = sum(s['verse_lines'] for s in all_stats)
    total_prose = sum(s['prose_lines'] for s in all_stats)
    total_tantra = sum(s['tantra_lines'] for s in all_stats)
    total_long = sum(s['long_lines'] for s in all_stats)
    
    print(f"Total Lines: {sum(s['total_lines'] for s in all_stats):,}")
    print(f"Verse Lines: {total_verse:,}")
    print(f"Prose Lines: {total_prose:,}")
    print(f"Tantra Lines: {total_tantra:,}")
    print(f"Long Lines (>threshold): {total_long:,}")
    print()
    
    # Files needing work
    files_with_issues.sort(key=lambda x: x['long_lines'], reverse=True)
    
    print(f"Files with Long Lines: {len(files_with_issues)}")
    print()
    print("Top 20 files needing attention:")
    for i, stats in enumerate(files_with_issues[:20], 1):
        print(f"{i}. {stats['filename']}: {stats['long_lines']} long lines")
    
    return files_with_issues

if __name__ == "__main__":
    files_with_issues = main()
    
    # Write report
    report_path = "/home/opencode/MDZOD/1/LITURGICAL_ANALYSIS_REPORT.txt"
    with open(report_path, 'w') as f:
        f.write("LITURGICAL LAYER ANALYSIS REPORT\n")
        f.write("="*70 + "\n\n")
        f.write(f"Files needing transformation: {len(files_with_issues)}\n\n")
        for stats in files_with_issues:
            f.write(f"{stats['filename']}: {stats['long_lines']} long lines\n")
    
    print(f"\nReport written to: {report_path}")
