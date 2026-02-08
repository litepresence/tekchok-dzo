#!/usr/bin/env python3
"""
Generate scholar layer files for Volume 2, pages 251-300 of Theg mchog mdzod.
Uses Four Pillars: [STRUCTURE], [PHILOLOGY], [CONTEXT], [CONCEPT]
Third person analytical tone, no practice advice, no devotional language.
"""

import os
import re

BASE_DIR = "/home/oracle/extinction-event/EV/theg pa'i mchog rin po che'i mdzod/1"
VOLUME = "volume_2"
START_PAGE = 251
END_PAGE = 300

def read_page(page_num):
    """Read tibetan, wylie, and literal layers for a page."""
    page_str = f"PAGE {page_num}.txt"
    layers = {}
    
    for layer in ['tibetan', 'wylie', 'literal']:
        path = os.path.join(BASE_DIR, VOLUME, layer, page_str)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                layers[layer] = f.read()
        except FileNotFoundError:
            layers[layer] = ""
    
    return layers

def extract_line_range(content):
    """Extract line numbers from content."""
    lines = content.strip().split('\n')
    line_nums = []
    for line in lines:
        match = re.match(r'\[(\d+)\]', line)
        if match:
            line_nums.append(int(match.group(1)))
    
    if line_nums:
        return min(line_nums), max(line_nums)
    return None, None

def generate_scholar_page_251():
    """Generate scholar analysis for PAGE 251."""
    return """[10810-10824] [STRUCTURE] # Section: Signs of Nirvana Preceding
**Analysis:** This section concludes the enumeration of signs indicating approach to complete nirvana. The structure follows the standard fivefold analytical framework (ngo bo, nges tshig, dbye ba, mtshan nyid, 'bras bu) established earlier. The passage lists thirteen distinct signs of spiritual maturation before transitioning to the third major topic: bindu (thig le) familiarity signs.

[10810-10824] [CONCEPT] Preliminary Liberation Signs
**Analysis:** The enumerated signs include: (1) disinterest in human association, (2) sensation of flying in space, (3) joy at the thought of appearances ceasing, (4) non-attachment to body and life, (5) non-engagement with phenomena, (6) clarity without dullness, (7) natural spaciousness of awareness, (8) comfort in association, (9) inability of afflictions to arise, (10) non-grasping of arisen afflictions, (11) non-attachment to beautiful forms, (12) non-aversion to ugly forms, (13) absence of hunger/thirst perceptions through samadhi power, (14) discord with others' minds. These function as diagnostic indicators of progression toward yongs su mya ngan las 'da' ba (complete nirvana).

[10825] [STRUCTURE] # RIM_KHANG: Third Section - Bindu Familiarity Signs
**Analysis:** Major structural transition marked by "gsum pa" (third). The text moves from wind (rlung) and channel (rtsa) signs to bindu (thig le) analysis, maintaining the sequential progression through subtle body components.

[10826-10830] [STRUCTURE] Fivefold Analytical Framework
**Analysis:** Standard scholastic structure: (1) ngo bo (essence), (2) nges tshig (definition), (3) dbye ba (division), (4) mtshan nyid (characteristic), (5) 'bras bu (result). This framework derives from Indian pramana traditions adapted in Tibetan doxography.

[10831-10832] [PHILOLOGY] Bindu Essence Analysis
**Analysis:** "tha dad ma yin zhing gcig tu gnas pas zla dang bral ba" — The essence is defined through double negation: non-different (tha dad ma yin) yet not establishing oneness either (gcig tu gnas pas), resulting in freedom from both extremes (zla dang bral ba, literally "free from moons" or dualistic reference points).

[10834-10835] [PHILOLOGY] Etymology of Thig-le
**Analysis:** The term is analyzed as "thig mi 'gyur ba" (the undrawn/unwavering dot) plus "le gdal ba chen pos kun la khyab pa" (the great vastness that pervades all). This represents a Dzogchen-specific etymology distinct from tantric bindu concepts of essence-drops.

[10836-10839] [STRUCTURE] Threefold Bindu Division
**Analysis:** (1) lus gnas rtsa'i thig le (body-dwelling channel bindu), (2) rang bzhin lam gyi thig le (nature path bindu), (3) mthar phyin 'bras bu'i thig le (complete result bindu). This tripartite structure maps bindu across ground, path, and fruition.

[10840-10842] [CONCEPT] Conventional and Ultimate Bindus
**Analysis:** First level subdivides into: (a) kun rdzob rgyu'i thig le dkar dmar gnyis (two conventional causal bindus, white and red), and (b) don dam ye shes kyi thig le lnga (five ultimate wisdom bindus). This reflects the standard two-truth framework applied to subtle body anatomy.

[10843-10860] [CONTEXT] Thalgyur Citation on Wisdom Bindus
**Analysis:** Citation from Thalgyur (Thal 'gyur) tantra enumerates six wisdom bindus: (1) chos nyid thig le, (2) kun tu bzang po'i thig le, (3) dbyings thig le, (4) dbyings rnam dag thig le, (5) ye shes thig le, (6) ye shes chen po'i thig le. These correspond to progressively refined levels of realization.

[10844] [PHILOLOGY] Technical Term: Gzhi'i thig le bzang po
**Analysis:** "Ground bindu of excellence" refers to the non-moving (mi g.yo) presence within the general channels of the body, described as 'od kyi gong bur (a sphere/ball of light). The term "bzang po" (excellent/good) distinguishes this from lower bindu manifestations.

[10846-10849] [CONTEXT] Thalgyur Quotation on Body Locations
**Analysis:** Verse citation: "spyi dang tsit+ta rtsa yi nang / ma bcos dag pa'i chos nyid gnas" — identifies the crown (spyi) and heart (tsitta) channels as locations where unfabricated pure reality dwells. Tsitta (Skt. citta) represents the heart-center as mind-ground in subtle body physiology.
"""

def generate_scholar_page_252():
    return """[10855-10860] [CONCEPT] Six Wisdom Bindus Detailed
**Analysis:** The six wisdom bindus are: (1) chos nyid kyi thig le (reality bindu) — unconditioned and all-pervading, (2) kun tu bzang po'i thig le — appearing without good/bad or size distinctions, (3) dbyings kyi thig le — clear without outer/inner division, (4) dbyings rnam dag thig le — arising without deviation or obscuration, (5) ye shes kyi thig le — primordially unmade, (6) ye shes chen po'i thig le — appearing directly unobscured by any affliction. These represent the bindu dimension of kayas.

[10861-10863] [CONCEPT] Result Bindu (mthar phyin 'bras bu'i thig le)
**Analysis:** The resultant bindu is characterized as dharmakaya bindu — single (nyag gcig), free from elaboration (spros bral), beyond identification (ngos gzung dang bral ba), primordially pure essence (ka dag gi ngo bo), appearing as variety from that state without any establishment cause (grub rgyu gang yang med pa).

[10864-10874] [STRUCTURE] Characteristics of Bindu
**Analysis:** Five characteristics enumerated: (1) free from various pains (sna tshogs zug rngu dang bral ba), (2) round/spherical without elaboration (zlum po spros pa med pa), (3) displaying awareness-appearance as great transparent wisdom (rig pa'i snang ba ston pas ye shes zang thal chen po), (4) five rims gathered as one (mu khyud lnga gcig tu bzlums pas sku'i gnas yin), (5) beyond identification due to emptiness not established as substance (stong nyid rdzas su ma grub pas ngo bo ngos gzung las 'das pa).

[10870-10874] [CONCEPT] Five Resultant Qualities
**Analysis:** From these characteristics arise: (1) virtue appearing directionless (yon tan phyogs med du shar), (2) characteristics stainless (mtshan nyid la dri ma med), (3) capacity appearing unceasing as various play (rtsal ma 'gags par snang bas rol pa sna tshogs su shar), (4) essence self-pure due to non-duality in characteristics (mtshan nyid la gnyis su med pas ngo bo rang dag), (5) nature self-liberated through directionless reasoning (gtan tshigs phyogs med du shar bas gnas lugs rang grol ba).

[10875-10899] [CONTEXT] Relic Citation on Bindu Signs
**Analysis:** Extended citation from Sku gdung 'bar ba (Blazing Relics) tantra describing external signs of bindu realization. The verses indicate: (1) bindu lamp of emptiness arising without effort, (2) all as self-experience signs, (3) cutting word elaborations, (4) mind not entering others' thoughts even for an instant, (5) impossibility of speech for others, (6) decision through single non-elaboration.

[10890-10896] [PHILOLOGY] Rtsad chod (Decisive Certainty)
**Analysis:** The term "rtsad chod" (decisive settling/cutting) appears in line 10891: "spros med nyag gcig des rtsad chod" — decisively settled through single non-elaboration. This technical term indicates irreversible realization rather than intellectual understanding.

[10897-10899] [CONTEXT] Dissolution Citation
**Analysis:** Final verse citation: "'byung ba rang dengs sa / 'gyur ba 'di la the tshom med" — elements self-dissolve, change without doubt. This indicates the automatic dissolution of elements when bindu realization is achieved.
"""

def generate_scholar_page_253():
    return """[10900] [STRUCTURE] # RIM_KHANG: Fourth Section - Kaya (sku)
**Analysis:** Major transition to fourth topic: the three kayas. Marked by "bzhi pa sku la" (fourth, on kayas). Maintains the fivefold analytical framework established in previous sections.

[10906] [PHILOLOGY] Kaya Essence Definition
**Analysis:** "rtag par gnas pa'i rang bzhin mya ngan las 'das pa'i chos rnams kyi rten du gnas pa'o" — essence defined as the support for all nirvana dharmas, possessing the nature of permanent abiding. The term "rtag par gnas pa" (permanent abiding) requires careful analysis: in Dzogchen, this indicates unconditioned stability (gnas lugs) rather than eternalist permanence.

[10908] [PHILOLOGY] Etymology: Dri med zang thal rang rdzogs chen po
**Analysis:** Definition as "stainless transparent-penetrate self-complete great" — dri med (stainless) negates afflictive obscurations, zang thal (transparent-penetrate) indicates unimpeded manifestation, rang rdzogs (self-complete) indicates spontaneous perfection without effort, chen po (great) indicates universality.

[10910-10912] [STRUCTURE] Three Kaya Division
**Analysis:** Standard triad: chos sku (dharmakaya), longs sku (sambhogakaya), sprul sku (nirmanakaya). This division appears across all Mahayana schools but receives distinct interpretation in Dzogchen.

[10913-10918] [CONTEXT] Dzogchen Distinction: Path Appearance vs. Result
**Analysis:** Critical doxographical distinction: common vehicles consider three kayas as fruition ('bras bur 'dod), while Great Perfection considers them as path appearances (lam gyi snang bar 'dod). This reflects the Dzogchen emphasis on recognition during the path of what is ultimately the case.

[10915-10918] [CONCEPT] Dharmakaya as Self-Appearance
**Analysis:** Chos sku rang snang yin — dharmakaya is one's own appearance. The reasoning: as long as dharmas exist, mind exists, therefore it is path; as long as kayas exist, body exists, therefore it is path appearance. Not ultimate (mthar thug ma yin). This subordinates kayas to the path process rather than treating them as ontological endpoints.

[10919-10921] [CONCEPT] Exhaustion Appearance
**Analysis:** "dngos gzhi tshad phebs rdzogs nas / zad pa'i snang ba ste / ka dag la thim du nye ba" — when the main practice reaches complete measure, exhaustion appearance (zad pa'i snang ba) approaches dissolution into primordial purity. This technical term indicates the stage where phenomena no longer appear as solid/obstructing.

[10922-10924] [CONCEPT] Sambhogakaya and Nirmanakaya as Path Appearance
**Analysis:** These kayas are also path appearances because while various appearing dharmas exist in stages, they are not the final extreme of markless equality (mtha' bral ris med mnyam pa'i mthar thug ma yin).

[10925-10928] [CONCEPT] Spontaneously Accomplished Appearance
**Analysis:** At the time of measure-reach, from spontaneously accomplished appearance arise kayas, fields (zhing), and teachers. This indicates the natural unfolding of display (rol pa) without fabrication.

[10930] [PHILOLOGY] Lam snang 'od gsal stong pa'i rang bzhin
**Analysis:** Path appearance characterized as clear-light empty nature. 'Od gsal (clear light) indicates luminous clarity, stong pa (empty) indicates lack of inherent existence, rang bzhin (nature) indicates this is not an attribute but the fundamental character.

[10931-10933] [CONCEPT] Result as Secret Jewel Interior
**Analysis:** Result described as ka dag rin po che gsang ba'i sbubs (primordially-pure jewel secret interior) where movement produces only the arising-basis of inner-clear three kayas. This spatial metaphor (sbubs = inside) suggests kayas are always present but obscured.

[10934-11025] [CONTEXT] Extended Relic Tantra Citation
**Analysis:** Lengthy citation from Sku gdung 'bar ba enumerating signs of three kaya familiarity: dharmakaya signs include body invisible to others while yogin plays freely; sambhogakaya signs include playing in five kayas and five wisdoms; nirmanakaya signs include speaking untaught dharma and displaying miraculous powers. The verses employ distinct dzogchen technical terminology.
"""

def generate_scholar_page_254():
    return """[10968-10978] [CONTEXT] Relic Tantra Citation: Miraculous Powers
**Analysis:** Citation continues from Sku gdung 'bar ba describing siddhis resulting from kaya practice: flying in sky, penetrating mountains, entering earth, not drowning in water. Line 10976 marks the critical transition point: "dbyings rig gdeng du ma tshud na" (if expanse-awareness is not entered as confidence) — indicating these powers alone do not constitute realization.

[10977-10981] [CONCEPT] Element Dissolution at Death
**Analysis:** If confidence is not achieved, elements self-dissolve ('byung ba nyid ni rang dengs su) and at death, transferring to the bardo of reality (chos nyid kyi bar do), liberation occurs in five instants (skad cig lnga la grol bar 'gyur). This describes the "automatic liberation" characteristic of Dzogchen at death.

[10982-11025] [CONTEXT] Extended Verses on Nirmanakaya Signs
**Analysis:** Comprehensive enumeration of signs indicating nirmanakaya familiarity: (1) previously heard dharma meanings arising instantly in continuum, (2) spontaneously speaking unheard dharmas, (3) clear recitation of other tantras, (4) answering questions according to beings' dispositions, (5) lion-like speech, (6) enhanced physical powers, (7) reversal of aging, (8) rejuvenation, (9) arising of unprecedented compassion, (10) ability to give body/limbs, (11) touching nirmanakaya.

[10990-10991] [PHILOLOGY] Cig car du 'char ba
**Analysis:** "Simultaneously arising" — a key Dzogchen technical term distinguishing instantaneous recognition from gradual cultivation. The dharma meanings arise not sequentially but all-at-once (cig car).

[11003] [PHILOLOGY] Smra ba'i seng ge
**Analysis:** "Speech lion" (smra ba'i seng ge) — epithet indicating fearlessness and power in teaching. Derives from standard Mahayana epithets for the Buddha's speech.

[11014-11016] [CONCEPT] Arising of Spontaneous Compassion
**Analysis:** "sngon na med pa'i snying rje yang / 'di la gting nas skye ba dang / de rjes sems can don la 'jug" — unprecedented compassion arising from depth, followed by engaging in beings' benefit. This indicates compassion not as cultivated quality but as spontaneous expression of realization.

[11020-11023] [CONCEPT] Bodily Self-Sacrifice
**Analysis:** Ability to give body and limbs (lus dang yan lag gtong bar nus) and even to guru — represents the complete transcendence of self-grasping that characterizes advanced realization in Mahayana and Vajrayana frameworks.
"""

def write_scholar_file(page_num, content):
    """Write scholar layer file."""
    path = os.path.join(BASE_DIR, VOLUME, "scholar", f"PAGE {page_num}.txt")
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Generated: PAGE {page_num}.txt")

def main():
    # Generate pages 251-253 immediately as exemplars
    write_scholar_file(251, generate_scholar_page_251())
    write_scholar_file(252, generate_scholar_page_252())
    write_scholar_file(253, generate_scholar_page_253())
    write_scholar_file(254, generate_scholar_page_254())
    
    print("Generated exemplar pages 251-254")
    print("Remaining pages 255-300 to be generated...")

if __name__ == "__main__":
    main()
