import math
import json
from parse_roman import parse_roman  # assuming this is your roman numeral → int function
import os
from pathlib import Path
import re
import itertools

# Load the boundary index
with open("boundary.json", "r", encoding="utf-8") as f:
    data = json.load(f)

volume = 1

# Folders containing the page-by-page text files
folders = [
    "tibetan",
    "wylie",
    "literal",
    "liturgical",
    # #
    # "cognitive",
    # "commentary",
    # "delusion",
    # "epistemic",
    # "scholar",
]


def get_page_file_path(folder: str, page: int) -> Path:
    # Adjust pattern if your naming is different (e.g. PAGE_001.txt vs page001.txt)
    return Path(folder) / f"PAGE_{page:03d}.txt"  # or f"PAGE_{page}.txt"


# de-layer the boundary data - take 3d and make 1d with 3d indices
sections = []
volume_data = data["volumes"][volume - 1]
vol_num = volume_data.get("volume_number", "?")
for chapter in volume_data["chapters"]:
    chap_num = chapter.get("chapter_number", "?")
    for section in chapter["sections"]:
        section_id = section["section_id"]
        section_num = parse_roman(section_id)

        start_page = section["boundary_start"]["page"]
        start_line = section["boundary_start"]["line"]
        split_phrase = section["boundary_start"]["phrase_tibetan"]

        sections.append(
            dict(
                zip(
                    [
                        "vol_num",
                        "chap_num",
                        "section_num",
                        "start_page",
                        "start_line",
                        "split_phrase",
                    ],
                    [vol_num, chap_num, section_num, start_page, start_line, split_phrase],
                )
            )
        )

# find start and end points for every section
pairs = list(itertools.pairwise(sections))
# the end section just needs to absorb the rest of the data
pairs.append(
    (
        pairs[-1][-1],
        {
            "vol_num": math.inf,
            "chap_num": math.inf,
            "section_num": math.inf,
            "start_page": math.inf,
            "start_line": math.inf,
            "split_phrase": "",
        },
    )
)

# add all file contents into a 2d list, one dimension is the folder, the other is the data

path = f"volume_{volume}/{{folder}}"

files = [
    (int(re.match(r"PAGE_(\d+)\.txt", i).groups()[0]), i)
    for i in os.listdir(path.format(folder="tibetan"))
    if re.match(r"PAGE_\d+\.txt", i)
]

files.sort()

start_page = min([i[0] for i in files])
end_page = max([i[0] for i in files])

page_data = [[], [], [], []]
for page in range(start_page, end_page + 1):
    for idx, folder in enumerate(folders):
        with open(path.format(folder=folder) + f"/PAGE_{page:03d}.txt", "r") as handle:
            page_data[idx].extend(handle.read().split("\n"))


# iterate through all lines
# have a pair in mind
# when you find that pair
# then start a new section and use the next pair to keep track of

# REF: pair format is [vol_num, chap_num, section_num, start_page, start_line, split_phrase]

buf = []

for type_idx, kind in enumerate(page_data):
    pdx = 0
    buf.append([[]])
    for line in kind:
        if not line.strip() or any(
            line.startswith(i) for i in ["### CITATION", "[### CITATION", "(End"]
        ):
            continue
        line_num = int(re.match(r"^\[(\d+)\]", line)[1])

        line = re.sub(r"^(?:\s*\[(\d+)\]\s*)+", "", line)
        # print(line)
        line = line.strip()

        if pdx >= len(pairs) or pairs[pdx][0]["start_line"] == line_num:
            # if we haven't started a new section yet, do so
            buf[-1].append([])

            after = line
            if not type_idx:
                if pairs[pdx][0]["split_phrase"] not in line:
                    raise

                before, after = line.split(pairs[pdx][0]["split_phrase"])
                if before:
                    buf[-1][-2].append((line_num, before))
                after = pairs[pdx][0]["split_phrase"] + after

            buf[-1][-1].append((line_num, after))
            pdx += 1
        else:
            buf[-1][-1].append((line_num, line))


for name, section in zip(folders, buf):
    for data, text in zip(pairs, section):
        filename = f"volume_{volume}_processed/{name}/{data[0]['chap_num']:02d}_{data[0]['section_num']}.txt"
        raw = "\n".join(f"[{i}] {j}" for i, j in text)
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as handle:
            handle.write(raw)

exit()
