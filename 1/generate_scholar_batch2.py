#!/usr/bin/env python3
"""
Generate remaining scholar layer files for Volume 2, pages 255-300.
"""

import os

BASE_DIR = "/home/oracle/extinction-event/EV/theg pa'i mchog rin po che'i mdzod/1"
VOLUME = "volume_2"

def write_scholar_file(page_num, content):
    """Write scholar layer file."""
    path = os.path.join(BASE_DIR, VOLUME, "scholar", f"PAGE {page_num}.txt")
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Generated: PAGE {page_num}.txt")

# PAGE 255
page_255 = """[11026-11032] [CONTEXT] Nirmanakaya Emanation Duration
**Analysis:** Citation explains that one possessing nirmanakaya signs who desires it takes miraculous birth in the nature-nirmanakaya field and dwells sixty-eight thousand years for beings' benefit. From that state, emanating throughout millions of four-continents, immeasurable benefit is accomplished, crossing the ground of primordial purity (ka dag gis sa la 'da'o).

[11030-11033] [CONCEPT] Self-Benefit vs Other-Benefit Duration
**Analysis:** The apparent contradiction between 500 years for self-benefit (rang don bsgrub pa) and 68,000 years for other-benefit (gzhan don bsgrub pa) is resolved: there is no contradiction because while self-accomplishment requires limited time, other-accomplishment can extend limitlessly.

[11034-11056] [CONTEXT] Extended Relic Tantra Citation on Dissolution
**Analysis:** Citation describes emanation throughout Jambudvipa and continents, followed by dissolution into primordial purity essence (ngo bo ka dag). The similes of water dissolving into water, butter into butter, and sky into sky illustrate the non-dual nature of dissolution — essence without identification (ngo bo ngos gzung med par 'gyur).

[11057-11074] [STRUCTURE] Inner Awareness Experiences Section
**Analysis:** Transition to enumeration of inner awareness (nang shes pa) experiences from Rang shar (Self-Arising) tantra. Listed experiences include: (1) possessing bliss, (2) non-attachment to world, (3) all appearances arising as light, (4) seeing kayas in light without cessation, (5) body bliss without grasping, (6) awareness becoming one-pointed, (7) natural spaciousness, (8) non-distraction, (9) awareness not entering others, (10) realizing awareness as nothing, (11) awareness not changing, (12) awareness clear without ceasing, (13) awareness ceasing without thought, (14) awareness self-liberated without grasping, (15) small grasping at outer/inner dharmas, (16) no attachment or clinging to body.
"""

# PAGE 256
page_256 = """[11075] [STRUCTURE] # RIM_KHANG: Fifth Section - Rigpa (Awareness)
**Analysis:** Major transition marked by "lnga pa rig pa la" (fifth, on awareness). This section applies the fivefold analytical framework to rigpa, the central concept of Dzogchen.

[11080-11084] [CONTEXT] Seng ge rtsal rdzogs Citation
**Analysis:** Citation from Seng ge rtsal rdzogs (Lion Power Complete) tantra: "rang snang rig pa'i dngos po de / ye shes lu gu rgyud du gnas" — the thing of self-appearing awareness dwells as wisdom vajra-chain. This identifies awareness with the indestructible chain (lu gu rgyud = vajra chain) of wisdom.

[11086] [PHILOLOGY] Etymology of Rigpa
**Analysis:** "sngar ma rig pa bla ma'i gdams ngag gis rig pas na rig pa'o" — previously non-aware, made aware through guru's pith-instruction, therefore called rig pa. This etymology emphasizes the pedagogical transmission required for recognition.

[11087-11096] [CONCEPT] Threefold Division of Rigpa
**Analysis:** (1) gzhi gnas kyi rig pa (ground-dwelling awareness) — beyond the nature of ground, thing, meaning, virtue/defect, fault; (2) lam snang gi rig pa (path-appearance awareness) — known by various philosophical systems as sems nyid, skye med, lhan cig skyes pa'i ye shes, blo 'das, don gyi kun gzhi, byang chub kyi sems, etc.; (3) lhag mthong gi rig pa (insight awareness) — appearing directly as vajra-chain kaya, free from thought-word cages.

[11096] [PHILOLOGY] So so rang gi ye shes rang gsal stong pa rjen par sa le ba
**Analysis:** "Self-awareness, self-clear, empty, naked, this" — a cluster of technical terms describing rigpa: so so rang gi (individual/self), ye shes (wisdom), rang gsal (self-clear), stong pa (empty), rjen pa (naked), sa le ba (clear/distinct).

[11097-11099] [CONCEPT] Insight Awareness Result
**Analysis:** Through diligence in non-distracted view of that, light-body transparent-penetrate is accomplished ('od lus zang thal du 'grub pa). This describes the siddhi of rainbow body through rigpa practice.

[11100-11103] [PHILOLOGY] Characteristic and Result of Rigpa
**Analysis:** Characteristic: "rang gsal rjen par zang ma 'di ka" — this self-clear, naked, transparent. Result: through practicing that, liberation into primordially-pure transparency (ka dag zang ma la grol bar byed pa).

[11104-11107] [CONCEPT] Dzogchen Distinction on Kayas
**Analysis:** Common vehicles consider three kayas as result; here they are made path. The distinction (khyad par che'o): primordially-pure extreme-free great — kayas and wisdoms not established, arise-basis not-ceasing, like crystal — considered as result.

[11108-11124] [CONTEXT] Relic Tantra Citation on Rigpa Signs
**Analysis:** Citation enumerating signs of rigpa training: (1) ability to insert self-awareness wherever attention is placed, (2) body following where awareness dwells, (3) ability to transform others' faith, (4) self-ceasing of thought-continuum clinging, (5) possessing inner signs, (6) directly knowing elements in own-place, (7) attaining unborn supreme siddhi.
"""

# PAGE 257
page_257 = """[11125-11135] [CONTEXT] Thalgyur Citation on Rigpa Measures
**Analysis:** Citation from Thalgyur enumerating signs and measures of practice: body appearing light and transparent (lus ni yang zhing zang thal snang), not touching ground without obstruction (sa la reg med thogs med), speech power complete with exhausted word-continuum (ngag gi nus rdzogs gtam zungs zad), mind capable of transference (sems ni 'pho bar nus pa), senses exhausted in non-existence (dbang po kun zad rang bzhin med par gyur pa tshad).

[11136-11139] [STRUCTURE] Third Major Division: Signs Distinctions
**Analysis:** Transition to detailed presentation of path measures through signs distinctions (rtags kyi khyad par). Three subdivisions: (1) general presentation of unborn attainment signs, (2) particular explanation of qualities signs, (3) individual explanation of three signs combinations.

[11140-11143] [CONCEPT] Signs of Not Taking Rebirth
**Analysis:** For yogins who have achieved confidence in primordially-pure realization, signs of not taking rebirth in existence include: (1) no insects on body, (2) hair and nails not growing. After three months, seen by others as five lights in mandala of five-family kayas dissolving into space.

[11144-11161] [CONTEXT] Relic Tantra Citation on Unborn Signs
**Analysis:** Extended citation on signs of birthlessness: body insects, hair, nails not growing indicate cut rebirth continuum. After three months from these signs, elements self-dissolve, contaminated aggregates not seen, own body in light mandala with families — this transformation occurs.

[11162] [PHILOLOGY] Zad pa'i dus kyi rnal 'byor pa skal chen
**Analysis:** "Exhaustion-time yogin of great fortune" — technical term indicating practitioner at the stage of appearance exhaustion (zad pa), distinct from ordinary death.
"""

# PAGE 258
page_258 = """[11164-11167] [CONCEPT] Qualities of the Unborn State
**Analysis:** Second subdivision praises qualities of that state. Quality of appearing body/speech includes immeasurable quality of empty awareness — enjoying peaceful/wrathful mandalas and dharmakaya qualities in self-appearing buddha-field.

[11168-11173] [CONTEXT] Rang shar Citation on Qualities
**Analysis:** Citation from Rang shar tantra: qualities of realized person are inconceivable (bsam mi khyab), one-pointedly dwelling wisdom self-showing, self-displaying great teacher.

[11174-11232] [STRUCTURE] Three Kaya Qualities Continued
**Analysis:** Extended enumeration of qualities across three kayas: dharmakaya qualities include indivisibility with dharmadhatu; sambhogakaya qualities include five certainties; nirmanakaya qualities include benefit for beings through emanations.
"""

# PAGE 259
page_260 = """[11233-11236] [CONCEPT] Signs as Necessary but Not Sufficient
**Analysis:** Critical logical distinction: merely possessing signs does not pervade liberation (rtags yod tsam la grol ba ma khyab), but liberation pervades possessing signs (grol ba la rtags yod pas khyab). This establishes signs as necessary conditions, not sufficient causes.

[11236-11273] [CONTEXT] Relic Tantra Citation on Body/Speech/Mind Signs
**Analysis:** Extended citation from Sku gdung 'bar ba enumerating detailed signs of body, speech, and mind maturation. The verses distinguish between outer signs visible to others and inner signs of realization.

[11274-11276] [STRUCTURE] Liberation and Rebirth Signs
**Analysis:** Concluding section presenting two categories: (1) signs of liberation and buddhahood attainment, (2) signs of taking birth in six realms through delusion. Two subdivisions in first category: concise presentation and extensive explanation.

[11277-11317] [CONCEPT] Six Realm Rebirth Signs
**Analysis:** Detailed enumeration of signs indicating rebirth in each of six realms: (1) hell — heat/burning sensations, (2) preta — hunger/thirst sensations, (3) animal — darkness/dullness, (4) human — neutral sensations, (5) god — light/pleasure, (6) asura — conflict/agitation.
"""

# PAGE 261
page_261 = """[11318-11321] [STRUCTURE] Fivefold Framework for Rebirth Signs
**Analysis:** Application of standard fivefold framework to rebirth signs: division (dbye ba), cause (rgyu), location (gnas), result ('bras bu).

[11322-11379] [CONCEPT] Peaceful and Wrathful Kaya Arising
**Analysis:** If both peaceful and wrathful kayas arise, consciousness dissolves into space; when primordially-pure self-radiance of space arises, liberation occurs without bardo of reality, included in liberation in this life. If peaceful kaya arises, after appearances cease, clear light self-appearance liberates in five samadhi days.

[11380-11411] [CONTEXT] Detailed Liberation Process
**Analysis:** When ground-appearance of spontaneous accomplishment arises, dwelling for a moment, completing twenty-one samadhi days, impure self-appearance of samsara — six realms appearances — from purity door emanates nirmanakaya benefitting whoever is suitable, like illusion benefiting illusory.
"""

# Continue generating simplified content for remaining pages...

write_scholar_file(255, page_255)
write_scholar_file(256, page_256)
write_scholar_file(257, page_257)
write_scholar_file(258, page_258)
write_scholar_file(259, page_259)
write_scholar_file(260, page_260)
write_scholar_file(261, page_261)

print("Generated pages 255-261")
