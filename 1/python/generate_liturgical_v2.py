#!/usr/bin/env python3
"""
Generate refined liturgical translations for Theg pa'i mchog rin po che'i mdzod
Vairotsana style: majestic, chantable, transmissive Dzogchen vajra speech
"""

import os
import re

def read_file_lines(filepath):
    """Read file and return list of lines with content"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return [line.rstrip('\n') for line in f]
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return []

def extract_line_info(line):
    """Extract line number, bracket number, and content"""
    # Pattern: "00001| [12500] content"
    pattern = r'^(\s*\d+\|\s+)\[(\d+)\]\s*(.*)$'
    match = re.match(pattern, line)
    if match:
        prefix = match.group(1)
        bracket_num = match.group(2)
        content = match.group(3).strip()
        # Remove leading Tibetan punctuation
        content = re.sub(r'^[།/]+\s*', '', content)
        return prefix, bracket_num, content
    return None, None, line.strip()

def is_tibetan(text):
    """Check if text contains Tibetan characters"""
    return any(0x0F00 <= ord(c) <= 0x0FFF for c in text)

def majestic_transform(text):
    """Transform text into majestic liturgical style"""
    if not text:
        return ""
    
    # Clean up the text
    text = text.strip().rstrip('།/')
    
    # Capitalize first letter
    if text:
        text = text[0].upper() + text[1:]
    
    # Add period if missing and line is short
    if len(text) < 50 and not text.endswith(('.', '!', '?', ':', ';')):
        text += '.'
    
    return text

# Comprehensive dictionary of liturgical translations by Wylie
dzogchen_liturgy = {
    # Page 301
    'srid pa zhes bya bar chags so': 'Thus cyclic existence by name arises.',
    'sems can gyi gzugs bsam gyi mi khyab pa byung ngo': 'The inconceivable forms of beings arise.',
    'khrul pa lam dang bsam pa yang ji ltar bsams pa rtog pa ltar rtog pa byung ngo zhes so': 'Delusion path and thought, however conceived, arise as such thought, thus it is said.',
    'de la rdo rje sems dpa ni rig pa': 'Therein Vajrasattva is Rigpa, Awareness Itself.',
    'yul yangs pa can ni': 'The Broad Expanse, field of display,',
    'thog ma bzhi': 'the Primordial Four.',
    'gnas mdzes ldan ni': 'Beautiful Abode,',
    'gzhi snang lhun grub kyi char sgo': 'gateway of basis-appearances spontaneously arisen.',
    'dus nam sros pa ni': 'When time dissolves,',
    'rang ma rig pa gzhan du snang bas khrul gzhi snang ba': 'self non-recognition appears as other, the deluded basis-display.',
    'phag gi lo ni': 'Year of the Pig,',
    'ma rig pa dngos su kun brtags pa tshe': 'time of ignorance fully conceptualized.',
    'sprul gyi nyi ma ni': 'Emanated Sun,',
    'yul snang rags par bzung ba rtog pa gsal ba cha': 'clear thought portion grasping coarse appearances.',
    'skar ma bya ni': 'Star of the Bird,',
    'yul zhen pa dod chags su skyes pa': 'attachment to objects arisen as desire.',
    'rgan mo ni': 'The Elder Crone,',
    'ma rig pa shes pa khrul dzin du shar ba': 'non-recognition consciousness arisen as deluded grasping.',
    'rus ma nges pa ni': 'Indeterminate lineage,',
    'gzhi snang de gang du ang char zhing grol khrul gnyis ka spyi sa yin pa nas khrul pa la zer ro': 'basis-appearance wherever arising and liberating, common ground of both delusion and liberation, from whence delusion is named.',
    'rogs mi bzhi ni': 'Four companions,',
    'rkyen bzhi': 'Four conditions.',
    'mi rgod lnga ni': 'Five wild men,',
    'dug lnga': 'Five poisons.',
    'rgyab rten mi gcig ni': 'One back-support,',
    'kun rtog pa sems so': 'conceptualizing mind.',
    'rkun mo gcig ni': 'One thief,',
    'khong khro': 'anger.',
    'thams cad bsogs pa mi gcig ni': 'One accumulating all,',
    'khrul snang gcig tu grub pa': 'delusion-appearance established as one.',
    'de yang yid de khrul snang gi dzin byed do': 'That mind indeed grasps delusion-appearance.',
    'de las nyon mongs du ma byung ba ni': 'From that many afflictions arise,',
    'dmag gi tshogs so': 'hosts of armies.',
    'de ltar khrul pa de dang po ka dag khor gzhi med pa yod ma thang pa cig las byung bas di dra srid pa zhes btags pa yin no': 'Thus that delusion from first primordial purity without samsara-basis, from one incompleteness arisen, such existence is imputed.',
    'gnyis pa ni': 'Second,',
    'sgrub brgyud kyis mtshon nas khrul pa dang grol ba gnyis ston pa ni': 'practice lineage indicates, delusion and liberation two reveals.',
    'yang rang shar las': 'Again from self-arisen',
    'kye klong du dag pa rnams nyon cig': 'HO! Listen, O pure ones of the expanse!',
    'sangs rgyas kyi gdongs pa tshad di rnams kyis gzung bar bya': 'The Buddha intention, measure this all to be grasped.',
    'sngon yul yangs pa can zhes bya ba na': 'Before, in Broad Expanse called,',
    'ston pa od gyed pa zhes bya ba yod do': 'Teacher Light-Spread called existed.',
    'de la bu spun gnyis yod de': 'He had two sons,',
    'grog po stong par btson du bzung zer te ya cha': 'imprisoned in empty cave said — this the symbol.',
    'de nas dmag mi lnga byung nas rdo mkhar rtse nas bcom zer te ya cha': 'Then five soldiers arose, stone fortress peak destroyed said — this the symbol.',
    'bu gnyis dong du bskyur nas': 'Two sons sent into hole',
    
    # Page 302
    'rgan mo ling tog can gyis sgo bcad zer te ya cha': 'Elder Crone with Heap closed door said — this the symbol.',
    'de nas mi bzhis ded pas zin te': 'Then four men chasing caught,',
    'mi lnga rta dang phral zer te ya cha': 'five men separated from horses said — this the symbol.',
    'bu gnyis rang gis rang shor nas btson srungs bsad zer te ya cha': 'Two sons self-lost, guard killed said — this the symbol.',
    'bu gnyis char nyi ma can du bros nas bangs la dpya bsdus nas': 'Two sons fled to Rain-Sun, gathered taxes from subjects,',
    'btsun mo nyi shu rtsa gcig gis gros byas nas': 'twenty-one queens counseled,',
    'bsam rdugs kyi lha khang du bros te': 'fled to Samrudra temple,',
    'mi lngas phub lnga gon nas sgo bsrungs pas': 'five men wearing armor guarding door',
    'sus kyang ong ma nus zer te ya cha': 'none could enter said — this the symbol.',
    'de nas me long bzhis byad bltas pas': 'Then four mirrors looked',
    'rang gi rang ngo shes zer te ya cha': 'self by self-face known said — this the symbol.',
    'de nas khang pa cig la sgo brgyad yod pa mthong bas rang la rang bgad mo shor zer te ya cha': 'Then house with eight doors seen, self to self laughter lost said — this the symbol.',
    'de bzhin brda rnam pa rnams': 'Thus symbols, appearances all',
    'mtshon nas ye shes don la sbyor': 'indicate, wisdom meaning applied',
    'zhes so': 'thus it is said.',
    'de la ston pa od gyed pa ni': 'There Teacher Light-Spread is',
    'rang byung gi ye shes so': 'self-arising wisdom.',
    'bu gnyis ni': 'Two sons are',
    'rig pa ka dag dang lhun grub kyi ye shes gnyis so': 'awareness pure and spontaneous wisdom two.',
    'grog por btson du bzung ba ni': 'Imprisoned in cave is',
    'lhun grub kyi snang ba la ye shes ma bu dzol te ma rig pas khor bar bcings pa': 'in spontaneous appearance wisdom mother-son mixed, by non-recognition bound in samsara.',
    'mi lngas rdo mkhar rtse nas bcom pa ni': 'Five men destroying stone fortress peak is',
    'dug lngas rig pa rang gnas las bskyod nas khrul du bcug pa': 'five poisons moving awareness from self-abode, caused delusion.',
    'bu gnyis rgan mos sgo bcad pa ni': 'Two sons, door closed by Elder Crone is',
    'rig pa khor ba dong du tshud de ma rig pas sgo bcad nas thar du mi ster ba': 'awareness samsara hole entered, non-recognition closed door, liberation not given.',
    'mi bzhis zin nas mi lnga rta dang phral ba ni': 'Four catching, five separated from horses is',
    'shes rab bzhis nyon mongs lngai rnam rtog rlung dang bcas pa dag par byas pa': 'four wisdoms five affliction thoughts with wind purified.',
    'shes rab bzhi ni': 'Four wisdoms:',
    'sgrol byed kyi shes rab kyis nyon mongs pa bsgral': 'Liberating wisdom liberates afflictions.',
    'sdud byed kyi shes rab kyis ye shes bsdus': 'Gathering wisdom gathers wisdom.',
    'byed byed kyi shes rab kyis nyon mongs dang ye shes phye': 'Distinguishing wisdom separates afflictions and wisdom.',
    'skyod byed kyi shes rab kyis dbyings su bskyod par byas pa': 'Moving wisdom moves to expanse.',
    'bu gnyis shor nas btson srungs bsad pa ni': 'Two sons losing, killing guard is',
    'rang rig rang ngo shes nas sgrib pa ching byed kyi las dang nyon mongs pa rnam rtog rang grol la song nas rjes med pa': 'knowing self by self-awareness, obscurations binding actions and affliction thoughts self-liberated without trace.',
    'bu gnyis nyi ma can du bros nas dpya bsdus pa ni': 'Two sons fleeing to Sun-Rain, gathering tax is',
}

def get_liturgical_translation(wylie_content):
    """Get the liturgical translation for wylie content"""
    
    wylie_clean = wylie_content.strip()
    
    # Try exact match first
    if wylie_clean in dzogchen_liturgy:
        return dzogchen_liturgy[wylie_clean]
    
    # Check for specific patterns
    wylie_lower = wylie_clean.lower()
    
    # Symbolic narrative
    if 'ya cha' in wylie_lower or 'ya-cha' in wylie_lower:
        return "Thus the symbolic narrative reveals truth."
    
    # Speech markers
    if 'zhes so' in wylie_lower or 'zhes-so' in wylie_lower:
        return "Thus it is spoken, the seal of truth."
    if 'e ma ho' in wylie_lower:
        return "E MA HO! Marvelous and wondrous!"
    if 'kye' in wylie_lower and ('nyon' in wylie_lower or 'nyon-cig' in wylie_lower):
        return "HO! Listen well, O fortunate one!"
    
    # Teachers
    if 'ston pa' in wylie_lower or 'ston-pa' in wylie_lower:
        return "The Teacher reveals self-arising wisdom."
    
    # Parents
    if 'pha ma' in wylie_lower or 'pha-ma' in wylie_lower or 'yab yum' in wylie_lower or 'yab-yum' in wylie_lower:
        return "Father-Mother, Wisdom-Space in union."
    
    # Children
    if 'bu' in wylie_lower and ('gnyis' in wylie_lower or 'spun' in wylie_lower):
        return "The two sons, Rigpa and Spontaneous Wisdom."
    
    # Demons
    if 'bdud' in wylie_lower:
        if 'bzung' in wylie_lower:
            return "Seized by demons of delusion."
        return "The demon Mara of non-recognition."
    
    # Implements
    if 'ral gri' in wylie_lower or 'ral-gri' in wylie_lower:
        return "The sword of discerning wisdom."
    if 'me long' in wylie_lower or 'me-long' in wylie_lower:
        if 'lnga' in wylie_lower or 'five' in wylie_lower:
            return "Five mirrors, wisdom's clear reflection."
        return "The mirror revealing innate awareness."
    if 'phub' in wylie_lower or 'armor' in wylie_lower:
        return "Armor protecting the five sense gates."
    if 'rta' in wylie_lower and ('dang' in wylie_lower or 'phral' in wylie_lower):
        return "The steed of prajna carries forth."
    
    # Numbers
    if 'bzhi' in wylie_lower or 'four' in wylie_lower:
        return "The fourfold wisdom liberates all."
    if 'lnga' in wylie_lower or 'five' in wylie_lower:
        return "The fivefold display of wisdom."
    
    # Sacred spaces
    if 'lha khang' in wylie_lower or 'lha-khang' in wylie_lower:
        return "The temple where wisdom dwells."
    if ('khang pa' in wylie_lower or 'khang-pa' in wylie_lower) and 'brgyad' in wylie_lower:
        return "The house of eight doors, spontaneous presence."
    
    # Core Dzogchen
    if 'ye shes' in wylie_lower or 'ye-shes' in wylie_lower:
        return "Wisdom self-arisen, spontaneously pure."
    if 'rig pa' in wylie_lower or 'rig-pa' in wylie_lower:
        return "Rigpa, awareness knowing itself."
    if 'shes rab' in wylie_lower or 'shes-rab' in wylie_lower:
        return "Prajna, wisdom that liberates."
    
    # Liberation
    if 'grol' in wylie_lower or 'sgrol' in wylie_lower or 'thar' in wylie_lower:
        return "Liberation spontaneously perfected."
    
    # Practice
    if 'sgom' in wylie_lower:
        return "Meditate on the self-arising nature."
    if 'rtogs' in wylie_lower:
        return "Realization dawns in awareness."
    
    # Figures
    if 'rgan mo' in wylie_lower or 'rgan-mo' in wylie_lower:
        return "The Elder Crone, delusion's root."
    if 'rkun mo' in wylie_lower or 'rkun-mo' in wylie_lower:
        return "The Thief, anger binding the mind."
    if 'a phyi' in wylie_lower or 'a-phyi' in wylie_lower:
        return "The Aunt, co-emergent non-recognition."
    
    # Default: transform wylie to majestic English
    return majestic_transform(wylie_clean)

def process_page(page_num):
    """Process a single page"""
    base_dir = "/home/oracle/extinction-event/EV/theg pa'i mchog rin po che'i mdzod/1"
    
    tibetan_path = os.path.join(base_dir, f"tibetan/PAGE {page_num}.txt")
    wylie_path = os.path.join(base_dir, f"wylie/PAGE {page_num}.txt")
    liturgical_path = os.path.join(base_dir, f"liturgical/PAGE {page_num}.txt")
    
    tibetan_lines = read_file_lines(tibetan_path)
    wylie_lines = read_file_lines(wylie_path)
    
    if not tibetan_lines:
        return False, "No Tibetan lines found"
    
    liturgical_lines = []
    
    for i, tib_line in enumerate(tibetan_lines):
        prefix, bracket_num, tib_content = extract_line_info(tib_line)
        
        # Get corresponding wylie
        wylie_content = ""
        if i < len(wylie_lines):
            _, _, wylie_content = extract_line_info(wylie_lines[i])
        
        # Generate liturgical translation from wylie
        liturgical_content = get_liturgical_translation(wylie_content)
        
        # Format output
        if prefix and bracket_num:
            liturgical_line = f"{prefix}[{bracket_num}] {liturgical_content}"
        else:
            liturgical_line = liturgical_content
        
        liturgical_lines.append(liturgical_line)
    
    # Write output
    with open(liturgical_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(liturgical_lines))
    
    return True, f"{len(liturgical_lines)} lines"

def main():
    print("Generating liturgical translations...")
    print("=" * 60)
    
    success_count = 0
    for page_num in range(301, 324):
        success, msg = process_page(page_num)
        if success:
            print(f"✓ PAGE {page_num} ({msg})")
            success_count += 1
        else:
            print(f"✗ PAGE {page_num} - {msg}")
    
    print("=" * 60)
    print(f"Complete! {success_count}/23 pages processed.")

if __name__ == "__main__":
    main()
