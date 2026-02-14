import json

# Comprehensive section data based on Tibetan text analysis
sections_data = {
    # VOLUME 1 - CHAPTER 1: The Perfect Teacher (Pages 1-26)
    "01-01-01-01": {
        "chapter": 1, "section": 1, "subsection": 1,
        "pages": "1-7", "lines": "1-191",
        "start": {"page": 1, "line": 1, "phrase": "༄༅།"},
        "end": {"page": 7, "line": 191, "phrase": "།འདི་ལྟ་བུའི་ཚུལ་ནི་ཐུན་མོང་གི་མདོ་སྡེ་དག་ལས་ཀྱང་གྲགས་ཏེ།"},
        "verified": True,
        "title_en": "Opening Homage and Teacher's Emanations",
        "title_tb": "སྟོན་པ་ཕུན་སུམ་ཚོགས་པ་རྣམ་པར་བཀོད་པ།",
        "summary": "Opening homage to Samantabhadra. Explanation of how the teacher's emanations appear to sentient beings across three times."
    },
    "01-01-02-01": {
        "chapter": 1, "section": 2, "subsection": 1,
        "pages": "7-16", "lines": "192-460",
        "start": {"page": 7, "line": 192, "phrase": "ཡབ་སྲས་མཇལ་བ་ལས།"},
        "end": {"page": 16, "line": 460, "phrase": "ཆོས་རགས་པ་འདུལ་བའི་རྒྱུད་བཅུ་ལ་སོགས་པ།"},
        "verified": True,
        "title_en": "Father-Son Meeting and Twelve Deeds",
        "title_tb": "ཡབ་སྲས་མཇལ་བ།",
        "summary": "Meeting between father and son. Detailed explanation of the Buddha's twelve deeds and emanation displays for disciples."
    },
    "01-01-03-01": {
        "chapter": 1, "section": 3, "subsection": 1,
        "pages": "16-26", "lines": "461-915",
        "start": {"page": 16, "line": 461, "phrase": "ཚེ་ལོ་ཁྲི་པའི་དུས་སུ་གསུངས་སོ།"},
        "end": {"page": 26, "line": 915, "phrase": "[CHAPTER_1_END]"},
        "verified": False,
        "title_en": "Seven Perfect Qualities",
        "title_tb": "ཕུན་སུམ་ཚོགས་པ་བདུན།",
        "summary": "The seven qualities of perfection - place, teacher, retinue, time, teaching, and intention."
    },
    
    # VOLUME 1 - CHAPTER 2: Container and Contents (Pages 26-58)
    "01-02-01-01": {
        "chapter": 2, "section": 1, "subsection": 1,
        "pages": "26-38", "lines": "916-1292",
        "start": {"page": 26, "line": 916, "phrase": "རགས་པ་ཙམ་ཞིག་བསྡུ་ན།"},
        "end": {"page": 38, "line": 1292, "phrase": "[SECTION_END_TBD]"},
        "verified": False,
        "title_en": "Container World and Contents Beings",
        "title_tb": "སྣོད་བཅུད་ཀྱི་འཇིག་རྟེན་བསྟན་པ་སྟེ་རིམ་ཁང་གཉིས་པའོ།",
        "summary": "Explanation of the world as container (snod) and beings as contents (bcud). Enumeration of realms from hells to heavens."
    },
    "01-02-02-01": {
        "chapter": 2, "section": 2, "subsection": 1,
        "pages": "39-46", "lines": "1293-1512",
        "start": {"page": 39, "line": 1293, "phrase": "ཚེ་སུམ་ཅུ་རྩ་གསུམ་པ་བཞིན་ནོ།"},
        "end": {"page": 46, "line": 1512, "phrase": "[SECTION_END_TBD]"},
        "verified": False,
        "title_en": "Origin of Humans from Divine Ancestors",
        "title_tb": "",
        "summary": "How the first humans descended from divine light beings. The devolution from light to solid form."
    },
    "01-02-03-01": {
        "chapter": 2, "section": 3, "subsection": 1,
        "pages": "47-52", "lines": "1513-1703",
        "start": {"page": 47, "line": 1513, "phrase": "དེ་ནས་རྒྱལ་ཆེན་བཞི་ནས་ཚངས་ཆེན་གྱི་བར་དུ་དེ་བཞིན་ནོ།"},
        "end": {"page": 52, "line": 1703, "phrase": "[SECTION_END_TBD]"},
        "verified": False,
        "title_en": "The Six Worlds and Their Characteristics",
        "title_tb": "",
        "summary": "Detailed explanation of the six realms - hell, preta, animal, human, asura, and deva realms."
    },
    "01-02-04-01": {
        "chapter": 2, "section": 4, "subsection": 1,
        "pages": "53-58", "lines": "1704-1943",
        "start": {"page": 53, "line": 1704, "phrase": "དྲི་མ་རྣམས་མངོན་དུ་དག་པའི་ཕྱིར་ཚུལ་ཁྲིམས་ཀྱི་ཕུང་པོ་དང༌།"},
        "end": {"page": 58, "line": 1943, "phrase": "[CHAPTER_2_END]"},
        "verified": False,
        "title_en": "Twelve Links of Dependent Origination",
        "title_tb": "",
        "summary": "The twelve links explained through container-contents relationship. Formation, abiding, and destruction of worlds."
    }
}

# Load existing file
with open('/home/opencode/MDZOD/1/boundary_v2.json', 'r', encoding='utf-8') as f:
    boundary_data = json.load(f)

# Add all sections
for section_id, data in sections_data.items():
    boundary_data["sections"][section_id] = {
        "chapter": data["chapter"],
        "section": data["section"],
        "subsection": data["subsection"],
        "start_page": data["start"]["page"],
        "start_line": data["start"]["line"],
        "start_phrase": data["start"]["phrase"],
        "end_page": data["end"]["page"],
        "end_line": data["end"]["line"],
        "end_phrase": data["end"]["phrase"],
        "verified": data["verified"],
        "content_summary": data["summary"],
        "tibetan_title": data["title_tb"],
        "english_title": data["title_en"]
    }

# Save updated file
with open('/home/opencode/MDZOD/1/boundary_v2.json', 'w', encoding='utf-8') as f:
    json.dump(boundary_data, f, indent=2, ensure_ascii=False)

print(f"✓ Updated boundary_v2.json")
print(f"✓ Total sections: {len(boundary_data['sections'])}")
print(f"✓ Chapters covered: 1-2")
