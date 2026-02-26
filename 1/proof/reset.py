#!/usr/bin/env python3
"""
Reset script - regenerates all HTML files from source data.
Run from the proof directory: python3 reset.py
"""

import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent

def run_script(script_name):
    """Run a Python script and return success status."""
    print(f"\n{'='*60}")
    print(f"Running: {script_name}")
    print('='*60)
    result = subprocess.run([sys.executable, script_name], cwd=SCRIPT_DIR)
    return result.returncode == 0

def main():
    scripts = [
        "process_literal.py",
        "process_tibetan.py", 
        "process_wylie.py",
        "process_liturgical.py",
        "process_commentary.py",
        "process_scholar.py",
        "process_epistemic.py",
        "process_delusion.py",
        "process_cognitive.py",
        "process_contents.py",
        "process_introduction.py",
        "process_glossary.py",
        "process_conventions.py",
    ]
    
    print("Starting HTML regeneration...")
    print("="*60)
    
    failed = []
    for script in scripts:
        if not run_script(script):
            failed.append(script)
            print(f"ERROR: {script} failed!")
    
    print("\n" + "="*60)
    if failed:
        print(f"FAILED: {len(failed)} script(s) failed: {failed}")
        return 1
    else:
        print("SUCCESS: All HTML files regenerated!")
        print("="*60)
        return 0

if __name__ == "__main__":
    sys.exit(main())
