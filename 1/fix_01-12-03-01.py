#!/usr/bin/env python3
"""Fix missing lines in 01-12-03-01.txt literal file"""

# Missing lines to insert after line 14861
missing_lines = [
    "[14862] /gis nas nam mkha'i dngas ma sems/",
    "[14863] /re zhig de nas 'gyur ba tsam/",
    "[14864] /khyab pa kun la khyab pa'o/",
    "[14865] /stong pa'i thig le brgyad yin te/",
    "[14866] /gnyis ni 'gyu ba'i thig le'o/",
    "[14867] /lhag ma stong 'gyur thig le'o/",
    "[14868] /'du ba'i rtsa ni bcu bzhi las/",
    "[14869] /bzhi ni bad kan sems kyi rtsa/",
    "[14870] /bzhi ni gti mug mkhris pa'i rtsa/",
]

filepath = "/home/opencode/MDZOD/1/text/frozen/literal/01-12-03-01.txt"

with open(filepath, 'r') as f:
    lines = f.readlines()

# Find where to insert (after line 14861)
insert_idx = None
for i, line in enumerate(lines):
    if line.startswith('[14861]'):
        insert_idx = i + 1
        break

if insert_idx:
    # Insert missing lines
    new_lines = lines[:insert_idx] + [l + '\n' for l in missing_lines] + lines[insert_idx:]
    
    with open(filepath, 'w') as f:
        f.writelines(new_lines)
    
    print(f"Inserted 9 missing lines after [14861]")
    print(f"Total lines now: {len(new_lines)}")
else:
    print("Could not find insertion point")
