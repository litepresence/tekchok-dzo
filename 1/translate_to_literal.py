import sys
import os
import re
from pathlib import Path
from ask_grok import create_context, ask_gpt


def main():
    input_dir = Path("numbered")
    output_dir = Path("translated")
    output_dir.mkdir(exist_ok=True)

    if not input_dir.exists():
        print("Error: 'numbered/' directory not found!")
        sys.exit(1)

    pattern = re.compile(r"^(\d+)_numbered\.md$")

    processed_count = 0

    driver = create_context()

    try:
        for file_path in input_dir.iterdir():
            if not file_path.is_file():
                continue

            filename = file_path.name
            match = pattern.match(filename)
            if not match:
                continue

            number = match.group(1)
            filename = f"{number}.md"
            if (output_dir/filename).is_file():
                continue

            print(f"Processing {filename} → {number}.txt")

            # Read input file
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()

            result = ask_gpt(driver, text)

            output_file = output_dir / f"{number}.md"
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(result)

            processed_count += 1

        print(f"\nDone! Processed {processed_count} files.")
        print(f"Labeled files saved in: {output_dir.resolve()}")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
