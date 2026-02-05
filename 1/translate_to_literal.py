#!/usr/bin/env python3
import sys
import re
from pathlib import Path
from ask_mistral import create_context, ask_gpt


def main():
    # Directories containing paired files
    tibetan_dir = Path("tibetan")
    wylie_dir = Path("wylie")

    # Prompt template file
    prompt_file = Path("prompt_literal.txt")

    # Output directory
    output_dir = Path("literal")
    output_dir.mkdir(exist_ok=True)

    # Validate inputs
    if not tibetan_dir.exists():
        print(f"Error: '{tibetan_dir}' directory not found!")
        sys.exit(1)
    if not wylie_dir.exists():
        print(f"Error: '{wylie_dir}' directory not found!")
        sys.exit(1)
    if not prompt_file.exists():
        print(f"Error: '{prompt_file}' not found!")
        sys.exit(1)

    # Read prompt template
    with open(prompt_file, "r", encoding="utf-8") as f:
        prompt_template = f.read()

    # Find all .txt files in tibetan directory
    tibetan_files = sorted(
        list(tibetan_dir.glob("*.txt"))#, key=lambda x: int(re.sub(r"[^0-9]", "", x))
    )

    if not tibetan_files:
        print(f"No .txt files found in '{tibetan_dir}'")
        sys.exit(1)

    processed_count = 0
    skipped_count = 0

    driver = create_context()

    try:
        for tibetan_path in tibetan_files:
            filename = tibetan_path.name
            wylie_path = wylie_dir / filename
            output_path = output_dir / filename

            # Check if wylie pair exists
            if not wylie_path.exists():
                print(f"Skipping {filename}: no matching wylie file")
                skipped_count += 1
                continue

            # Check if already processed
            if output_path.exists():
                print(f"Skipping {filename}: already translated")
                skipped_count += 1
                continue

            print(f"Processing {filename}...")

            # Read both files
            with open(tibetan_path, "r", encoding="utf-8") as f:
                tibetan_content = f.read()

            with open(wylie_path, "r", encoding="utf-8") as f:
                wylie_content = f.read()

            # Format prompt with tibetan and wylie content
            prompt = prompt_template.format(tibetan=tibetan_content, wylie=wylie_content)

            # Send to GPT/Mistral
            result = ask_gpt(driver, prompt)

            # Save result
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(result)

            processed_count += 1
            print(f"  Saved to {output_path}")

        print(f"Done! Processed {processed_count} files, skipped {skipped_count}.")
        print(f"Translated files saved in: {output_dir.resolve()}")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
