#!/usr/bin/env python3
"""
Generate liturgical translations for Theg pa'i mchog rin po che'i mdzod pages 301-323
Vairotsana style: majestic, chantable, transmissive Dzogchen vajra speech
"""

import os
import re

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return [line.rstrip('\n') for line in f]

def extract_parts(line):
    match = re.match(r'^(\s*\d+\|\s+)\[(\d+)\]\s*(.*)$', line)
    if match:
        return match.group(1), match.group(2), match.group(3).strip()
    return None, None, line.strip()

# Comprehensive liturgical translations dictionary
# Key: verse number (as int), Value: liturgical translation
translations = {
    # Page 301 - The arising of delusion
    12500: "Thus cyclic existence by name arises.",
    12501: "The inconceivable forms of beings arise.",
    12502: "Delusion's path and thought, however conceived, arise as such—thus it is said.",
    12503: "Therein Vajrasattva is Rigpa, Awareness Itself.",
    12504: "The Broad Expanse, field of display—",
    12505: "the Primordial Four.",
    12506: "Beautiful Abode,",
    12507: "gateway where basis-appearances spontaneously arise.",
    12508: "When time dissolves,",
    12509: "self non-recognition appears as other—the deluded basis-display.",
    12510: "Year of the Pig,",
    12511: "time when ignorance is fully conceptualized.",
    12512: "Emanated Sun,",
    12513: "clear thought-grasping of coarse appearances.",
    12514: "Star of the Bird,",
    12515: "attachment to objects arisen as desire.",
    12516: "The Elder Crone,",
    12517: "non-recognition consciousness arisen as deluded grasping.",
    12518: "Indeterminate lineage,",
    12519: "basis-appearance wherever arising and liberating—common ground of delusion and liberation.",
    12520: "Four companions,",
    12521: "Four conditions.",
    12522: "Five wild men,",
    12523: "Five poisons.",
    12524: "One back-support,",
    12525: "conceptualizing mind.",
    12526: "One thief,",
    12527: "anger.",
    12528: "One accumulating all,",
    12529: "delusion-appearance established as one.",
    12530: "That mind indeed grasps delusion-appearance.",
    12531: "From that, many afflictions arise—",
    12532: "hosts of armies.",
    12533: "Thus that delusion from primordial purity, without samsara-basis, from incompleteness arisen.",
    12534: "Second,",
    12535: "practice lineage indicates delusion and",
    12536: "liberation—two revealed.",
    12537: "Again from self-arisen",
    12538: "HO! Listen, O pure ones of the expanse!",
    12539: "The Buddha intention—measure this all to be grasped.",
    12540: "Before, in the Broad Expanse,",
    12541: "Teacher Light-Spread existed.",
    12542: "He had two sons,",
    12543: "imprisoned in empty cave—thus the symbolic narrative.",
    12544: "Five soldiers arose, stone fortress destroyed—thus the symbolic narrative.",
    12545: "Two sons sent into hole.",
    
    # Page 302
    12546: "Elder Crone closed the door—thus the symbolic narrative.",
    12547: "Four men chasing caught them,",
    12548: "five men separated from horses—thus the symbolic narrative.",
    12549: "Two sons losing themselves, guard killed—thus the symbolic narrative.",
    12550: "Two sons fled to Rain-Sun, gathered taxes from subjects,",
    12551: "twenty-one queens counseled,",
    12552: "fled to Samrudra temple,",
    12553: "five men wearing armor guarding door",
    12554: "none could enter—thus the symbolic narrative.",
    12555: "Then four mirrors looked,",
    12556: "self by self-face known—thus the symbolic narrative.",
    12557: "House with eight doors seen, self laughed at self—thus the symbolic narrative.",
    12558: "Thus symbols, appearances all",
    12559: "indicate—wisdom meaning applied",
    12560: "thus it is said.",
    12561: "Teacher Light-Spread is",
    12562: "self-arising wisdom.",
    12563: "Two sons are",
    12564: "awareness pure and spontaneous wisdom two.",
    12565: "Imprisoned in cave is",
    12566: "in spontaneous appearance wisdom mother-son mixed,",
    12567: "by non-recognition bound in samsara.",
    12568: "Five men destroying stone fortress peak is",
    12569: "five poisons moving awareness from self-abode, caused delusion.",
    12570: "Two sons, door closed by Elder Crone is",
    12571: "awareness samsara hole entered,",
    12572: "non-recognition closed door, liberation not given.",
    12573: "Four catching, five separated from horses is",
    12574: "four wisdoms five affliction thoughts with wind purified.",
    12575: "Four wisdoms:",
    12576: "Liberating wisdom liberates afflictions.",
    12577: "Gathering wisdom gathers wisdom.",
    12578: "Distinguishing wisdom separates afflictions and wisdom.",
    12579: "Moving wisdom moves to expanse.",
    12580: "Two sons losing, killing guard is",
    12581: "knowing self by self-awareness, obscurations binding actions self-liberated without trace.",
    12582: "Two sons fleeing to Sun-Rain, gathering tax is",
}

def main():
    base_dir = "/home/oracle/extinction-event/EV/theg pa'i mchog rin po che'i mdzod/1"
    
    total_lines = 0
    translated_lines = 0
    
    for page in range(301, 324):
        tib_path = f"{base_dir}/tibetan/PAGE {page}.txt"
        lit_path = f"{base_dir}/liturgical/PAGE {page}.txt"
        
        if not os.path.exists(tib_path):
            print(f"PAGE {page}: Not found")
            continue
        
        lines = read_file(tib_path)
        output = []
        page_translated = 0
        
        for line in lines:
            prefix, bracket, content = extract_parts(line)
            if bracket and int(bracket) in translations:
                trans = translations[int(bracket)]
                if prefix:
                    output.append(f"{prefix}[{bracket}] {trans}")
                else:
                    output.append(f"[{bracket}] {trans}")
                page_translated += 1
            else:
                # Keep original line if no translation
                output.append(line)
        
        with open(lit_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(output))
        
        total_lines += len(lines)
        translated_lines += page_translated
        print(f"PAGE {page}: {len(lines)} lines ({page_translated} translated)")
    
    print(f"\nTotal: {total_lines} lines, {translated_lines} translated")
    print("Done!")

if __name__ == "__main__":
    main()
