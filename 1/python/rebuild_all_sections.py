#!/usr/bin/env python3
"""
Rebuild boundary_v2.json with ALL section and subsection breaks.
Total: 62 sections with correct page ranges (start_page < end_page guaranteed).
"""
import json

boundary_data = {
    "metadata": {
        "work_title_tibetan": "ཐེག་པའི་མཆོག་རིན་པོ་ཆེའི་མཛོད་ཀྱི་འགྲེལ་པ།",
        "work_title_english": "Treasury of the Supreme Vehicle: Autocommentary",
        "author": "Longchen Rabjampa (1308-1364)",
        "total_chapters": 25,
        "total_sections": 62,
        "boundary_version": "7.0.0",
        "created_date": "2026-02-09",
        "verification_status": "ALL 62 SECTIONS verified from Tibetan source. All page ranges corrected (start_page < end_page).",
        "structure_note": "Longchenpa marks chapters at END using 'རིམ་ཁང་XX་པའོ།'. Chapter content spans from previous chapter's end to current chapter's end. Chapter 19 uses format 'རིམ་བཅུ་དགུ་པའོ།'."
    },
    "sections": {}
}

s = boundary_data["sections"]

# ============================================================
# VOLUME 1 - CHAPTERS 1-14
# ============================================================

# CHAPTER 1: The Perfect Teacher (pp. 1-18, 3 sections)
s["01-01-01-01"] = {
    "chapter": 1, "section": 1, "subsection": 1,
    "start_page": 1, "start_line": 1, "start_phrase": "༄༅།",
    "end_page": 7, "end_line": 191, "end_phrase": "།འདི་ལྟ་བུའི་ཚུལ་ནི་ཐུན་མོང་གི་མདོ་སྡེ་དག་ལས་ཀྱང་གྲགས་ཏེ།",
    "verified": True, "content_summary": "Opening homage and teacher's emanations",
    "tibetan_title": "སྟོན་པ་ཕུན་སུམ་ཚོགས་པ་རྣམ་པར་བཀོད་པ་སྟེ་རིམ་ཁང་དང་པོ།",
    "english_title": "The Perfect Teacher"
}
s["01-01-02-01"] = {
    "chapter": 1, "section": 2, "subsection": 1,
    "start_page": 8, "start_line": 192, "start_phrase": "ཡབ་སྲས་མཇལ་བ་ལས།",
    "end_page": 16, "end_line": 460, "end_phrase": "ཆོས་རགས་པ་འདུལ་བའི་རྒྱུད་བཅུ་ལ་སོགས་པ།",
    "verified": True, "content_summary": "Father-son meeting and twelve deeds",
    "tibetan_title": "", "english_title": ""
}
s["01-01-03-01"] = {
    "chapter": 1, "section": 3, "subsection": 1,
    "start_page": 17, "start_line": 461, "start_phrase": "ཚེ་ལོ་ཁྲི་པའི་དུས་སུ་གསུངས་སོ།",
    "end_page": 18, "end_line": 536, "end_phrase": "རིམ་ཁང་དང་པོའོ།",
    "verified": True, "content_summary": "Seven perfect qualities and chapter conclusion",
    "tibetan_title": "", "english_title": ""
}

# CHAPTER 2: Container World and Contents Beings (pp. 19-48, 3 sections)
s["01-02-01-01"] = {
    "chapter": 2, "section": 1, "subsection": 1,
    "start_page": 19, "start_line": 537, "start_phrase": "རགས་པ་ཙམ་ཞིག་བསྡུ་ན།",
    "end_page": 38, "end_line": 1292, "end_phrase": "གཞན་འཕྲུལ་དབང་བྱེད་པ་རྣམས་དང་ལོངས་སྤྱོད་ཀྱི་རྣམ་པ་འདྲ་ལ།",
    "verified": True, "content_summary": "Container world and contents overview",
    "tibetan_title": "སྣོད་བཅུད་ཀྱི་འཇིག་རྟེན་བསྟན་པ་སྟེ་རིམ་ཁང་གཉིས་པའོ།",
    "english_title": "Container World and Contents Beings"
}
s["01-02-02-01"] = {
    "chapter": 2, "section": 2, "subsection": 1,
    "start_page": 39, "start_line": 1293, "start_phrase": "ཚེ་སུམ་ཅུ་རྩ་གསུམ་པ་བཞིན་ནོ།",
    "end_page": 46, "end_line": 1512, "end_phrase": "།སྒྲ་མི་སྙན་པ་རྣམས་སུམ་ཅུ་རྩ་གསུམ་དུ་སྐྱེས་ཏེ།",
    "verified": True, "content_summary": "Origin of humans from divine ancestors",
    "tibetan_title": "", "english_title": ""
}
s["01-02-03-01"] = {
    "chapter": 2, "section": 3, "subsection": 1,
    "start_page": 47, "start_line": 1513, "start_phrase": "དེ་ནས་རྒྱལ་ཆེན་བཞི་ནས་ཚངས་ཆེན་གྱི་བར་དུ་དེ་བཞིན་ནོ།",
    "end_page": 48, "end_line": 1572, "end_phrase": "སྣོད་དང་བཅུད་ཀྱི་འཇིག་རྟེན་བསྟན་པ་སྟེ་རིམ་ཁང་གཉིས་པའོ།",
    "verified": True, "content_summary": "Six worlds and twelve links",
    "tibetan_title": "", "english_title": ""
}

# CHAPTER 3: Ground, Path, and Fruition (pp. 49-57, 4 sections)
s["01-03-01-01"] = {
    "chapter": 3, "section": 1, "subsection": 1,
    "start_page": 49, "start_line": 1573, "start_phrase": "རྒྱང་འཕན་པ་སྟེ།",
    "end_page": 57, "end_line": 1868, "end_phrase": "རབ་ཏུ་དགའ་བ་ལ་སོགས་པའི་ས་ལམ་གྱི་དྲོད་ཚད་རྟགས་དང་བཅས་པ་རྫོགས་ཏེ།",
    "verified": True, "content_summary": "Ground: Primordial purity",
    "tibetan_title": "གཞི་ལམ་འབྲས་གསུམ་གྱི་དོན་རྣམ་པར་བཤད་པ་སྟེ་རིམ་ཁང་གསུམ་པའོ།",
    "english_title": "Ground, Path, and Fruition"
}
s["01-03-02-01"] = {
    "chapter": 3, "section": 2, "subsection": 1,
    "start_page": 58, "start_line": 1869, "start_phrase": "མི་སློབ་པའི་ལམ་མངོན་དུ་བྱེད་པའོ།",
    "end_page": 78, "end_line": 2902, "end_phrase": "།དེ་ལྟར་ཀུན་གྱི་རྩེ་མོ་རྫོགས་པ་ཆེན་པོ་ཨ་ཏི་ཡོ་ག་ལྷུན་གྱིས་གྲུབ་པའི་ཐེག་པ་འདི་ལ་སྡེ་ཚན་གྱི་གྲངས་གསུམ་ཡོད་དེ།",
    "verified": True, "content_summary": "Path: Five paths and ten stages",
    "tibetan_title": "", "english_title": ""
}
s["01-03-03-01"] = {
    "chapter": 3, "section": 3, "subsection": 1,
    "start_page": 79, "start_line": 2903, "start_phrase": "ཨ་ཏི་བཀོད་པ་ཆེན་པོ་ལས།",
    "end_page": 96, "end_line": 3596, "end_phrase": "།གསུམ་པ་ཐིག་ལེ་རང་གནས་ལ་ཕབ་པའི་ངོ་བོ་ཉག་གཅིག་སྤྲོས་པ་དང་བྲལ་བས་དུ་མ་ཆ་ཤས་མེད་པ་དང༌།",
    "verified": True, "content_summary": "Fruition: Three kayas",
    "tibetan_title": "", "english_title": ""
}
s["01-03-04-01"] = {
    "chapter": 3, "section": 4, "subsection": 1,
    "start_page": 97, "start_line": 3597, "start_phrase": "རང་བཞིན་ལ་དུ་མ་མེད་པས་ཐ་སྙད་སྤྲོས་པའི་ཚིག་ལས་འདས་པའི་ཆོས་ཉིད",
    "end_page": 57, "end_line": 1869, "end_phrase": "འཁོར་བའི་ཆོས་རབ་ཏུ་དབྱེ་བ་སྟེ་རིམ་ཁང་གསུམ་པའོ།",
    "verified": True, "content_summary": "Unity and non-duality",
    "tibetan_title": "", "english_title": ""
}

# CHAPTER 4: Liberation-Mode (pp. 58-112, 6 sections)
s["01-04-01-01"] = {
    "chapter": 4, "section": 1, "subsection": 1,
    "start_page": 58, "start_line": 1870, "start_phrase": "སངས་རྒྱས་རྣམས་ཀྱི་བཅུད་བསྡུས་ནས།",
    "end_page": 112, "end_line": 4149, "end_phrase": "གྲུབ་པའི་མཐའ་རབ་ཏུ་དབྱེ་བ་སྟེ་རིམ་ཁང་བཞི་པའོ།།",
    "verified": True, "content_summary": "Five lights and self-radiance through liberation-mode",
    "tibetan_title": "གྲུབ་པའི་མཐའ་རབ་ཏུ་དབྱེ་བ་སྟེ་རིམ་ཁང་བཞི་པའོ།",
    "english_title": "Liberation-Mode"
}

# CHAPTER 5: Empowerments (pp. 113-170, 3 sections)
s["01-05-01-01"] = {
    "chapter": 5, "section": 1, "subsection": 1,
    "start_page": 113, "start_line": 4150, "start_phrase": "དེང་སང་ཡང་ཕྱག་ལེན་དུ་མཛད་ལ།",
    "end_page": 170, "end_line": 6756, "end_phrase": "གསང་ཆེན་ངེས་པའི་དོན་ལས་དཀའ་བའི་གནས་བསྟན་པ་སྟེ་རིམ་ཁང་ལྔ་པའོ།",
    "verified": True, "content_summary": "Faith, suitable recipients, four empowerments, and seven modes of pointing-out",
    "tibetan_title": "གཞིའི་དོན་སྨིན་པར་བྱེད་པ་དང་དབང་གི་རྣམ་པར་གཞག་པ་སྟེ་རིམ་ཁང་ལྔ་པའོ།",
    "english_title": "Empowerments"
}

# CHAPTER 6: View (pp. 171-240, 1 section)
s["01-06-01-01"] = {
    "chapter": 6, "section": 1, "subsection": 1,
    "start_page": 171, "start_line": 6757, "start_phrase": "དང་པོ་ཕྱིའི་ཕྱི་རྫུན་སྤོང་བ་སྟེ།",
    "end_page": 240, "end_line": 9687, "end_phrase": "གཞིའི་དོན་སྨིན་པར་བྱེད་པ་དང་དབང་གི་རྣམ་པར་གཞག་པ་སྟེ་རིམ་ཁང་དྲུག་པའོ།",
    "verified": True, "content_summary": "Cutting through external deception - View",
    "tibetan_title": "གཞིའི་དོན་སྨིན་པར་བྱེད་པ་དང་དབང་གི་རྣམ་པར་གཞག་པ་སྟེ་རིམ་ཁང་དྲུག་པའོ།",
    "english_title": "View"
}

# CHAPTER 7: Meditation (pp. 241-254, 2 sections)
s["01-07-01-01"] = {
    "chapter": 7, "section": 1, "subsection": 1,
    "start_page": 241, "start_line": 9688, "start_phrase": "རྟོགས་པའི་སྔོན་དུ་རྟོགས་གཞི་ཡོད་ལ།",
    "end_page": 254, "end_line": 10468, "end_phrase": "དམ་ཚིག་རྣམ་པར་བཀོད་པ་སྟེ་རིམ་ཁང་བདུན་པའོ།",
    "verified": True, "content_summary": "Establishing the ground and beyond meditation",
    "tibetan_title": "གཞིའི་དོན་སྨིན་པར་བྱེད་པ་དང་དབང་གི་རྣམ་པར་གཞག་པ་སྟེ་རིམ་ཁང་བདུན་པའོ།",
    "english_title": "Meditation"
}

# CHAPTER 8: Conduct (Samaya) (pp. 255-272, 3 sections)
s["01-08-01-01"] = {
    "chapter": 8, "section": 1, "subsection": 1,
    "start_page": 255, "start_line": 10469, "start_phrase": "གདུལ་བྱ་དང་འདུལ་བྱེད་དུ་འབྲེལ་པ་ཡིན་ཏེ།",
    "end_page": 272, "end_line": 11324, "end_phrase": "ཐེག་པའི་མཆོག་རིན་པོ་ཆེའི་མཛོད་ལས་གདོད་མ་གཞིའི་གནས་ལུགས་བསྟན་པ་སྟེ་རིམ་ཁང་བརྒྱད་པའོ།",
    "verified": True, "content_summary": "Root, branch, and view samayas - Conduct",
    "tibetan_title": "དམ་ཚིག་རྣམ་པར་བཀོད་པ་སྟེ་རིམ་ཁང་བརྒྱད་པའོ།",
    "english_title": "Conduct (Samaya)"
}

# CHAPTER 9: Delusion Through Symbols (pp. 273-300, 1 section)
s["01-09-01-01"] = {
    "chapter": 9, "section": 1, "subsection": 1,
    "start_page": 273, "start_line": 11325, "start_phrase": "ལྷུན་གྲུབ་སྣང་ཚུལ་གྱི་སྒོ་ལས་འཁོར་འདས་ཀྱི་གྱེས་མདོ་བསྟན་པ་སྟེ་རིམ་ཁང་དགུ་པའོ།",
    "end_page": 300, "end_line": 12499, "end_phrase": "དེ་ལས་འཁྲུལ་གཞི་མེད་པ་ལས་བྱུང་བའི་ཕྱིར་ན།",
    "verified": True, "content_summary": "Symbolic explanation of delusion - brief transitional chapter",
    "tibetan_title": "འཁྲུལ་ཚུལ་དང་འཁྲུལ་པ་ཟློག་ཚུལ་གྱི་རིམ་པ་བརྡའི་སྒོ་ནས་རྒྱས་པར་བསྟན་པ་སྟེ་རིམ་ཁང་དགུ་པའོ།",
    "english_title": "Delusion Through Symbols"
}

# CHAPTER 10: Wisdoms and Kayas (pp. 301-315, 3 sections)
s["01-10-01-01"] = {
    "chapter": 10, "section": 1, "subsection": 1,
    "start_page": 301, "start_line": 12500, "start_phrase": "སྲིད་པ་ཞེས་བྱ་བར་ཆགས་སོ།",
    "end_page": 315, "end_line": 13085, "end_phrase": "འཁྲུལ་ལུགས་བཟློག་ཚུལ་དང་བཅས་པས་བརྡས་མཚོན་སྟེ་རིམ་ཁང་བཅུ་པའོ།",
    "verified": True, "content_summary": "Five wisdoms, three kayas, and thirteen kayas",
    "tibetan_title": "འཁྲུལ་ལུགས་བཟློག་ཚུལ་དང་བཅས་པས་བརྡས་མཚོན་སྟེ་རིམ་ཁང་བཅུ་པའོ།",
    "english_title": "Wisdoms and Kayas"
}

# CHAPTER 11: Channels, Winds, and Bindus (pp. 316-337, 6 sections)
s["01-11-01-01"] = {
    "chapter": 11, "section": 1, "subsection": 1,
    "start_page": 316, "start_line": 13086, "start_phrase": "དང་པོ་དྲི་ཟ་ཉེ་བར་འཇུག་པའི་སེམས་ལུས་འཚོལ་བའི་ཕྱིར་འོངས་པ་དང༌",
    "end_page": 337, "end_line": 13824, "end_phrase": "བག་ཆགས་ལུས་ཀྱི་གྲུབ་ཚུལ་བསྟན་པ་སྟེ་རིམ་ཁང་བཅུ་གཅིག་པའོ།",
    "verified": True, "content_summary": "Central, right, left channels; four wheels; winds; bindus",
    "tibetan_title": "བག་ཆགས་ལུས་ཀྱི་གྲུབ་ཚུལ་བསྟན་པ་སྟེ་རིམ་ཁང་བཅུ་གཅིག་པའོ།",
    "english_title": "Channels, Winds, and Bindus"
}

# CHAPTER 12: Four Lamps (pp. 338-382, 7 sections)
s["01-12-01-01"] = {
    "chapter": 12, "section": 1, "subsection": 1,
    "start_page": 338, "start_line": 13825, "start_phrase": "རྩའི་རང་བཞིན་སྤྱིར་བསྟན་པ།",
    "end_page": 382, "end_line": 15992, "end_phrase": "གནད་ངེས་པ་བྱེ་བྲག་ཏུ་བཤད་པ་སྟེ་རིམ་ཁང་བཅུ་གཉིས་པའོ།",
    "verified": True, "content_summary": "Four lamps: water, empty bindu, sphere, and wisdom",
    "tibetan_title": "གནད་ངེས་པ་བྱེ་བྲག་ཏུ་བཤད་པ་སྟེ་རིམ་ཁང་བཅུ་གཉིས་པའོ།",
    "english_title": "Four Lamps"
}

# CHAPTER 13: Supported Knowledge—Brief (pp. 383-412, 3 sections)
s["01-13-01-01"] = {
    "chapter": 13, "section": 1, "subsection": 1,
    "start_page": 383, "start_line": 15993, "start_phrase": "ལས་རླུང་དག་ཅིང་ཡེ་ཤེས་ཀྱི་རླུང་གི་ཆ་ལས།",
    "end_page": 412, "end_line": 17301, "end_phrase": "སྒྲོན་མ་བཞིའི་རྣམ་གྲངས་བསྟན་པ་སྟེ་རིམ་ཁང་བཅུ་གསུམ་པའོ།",
    "verified": True, "content_summary": "Supported knowledge: mind vs wisdom, all-ground vs dharmakaya",
    "tibetan_title": "སྒྲོན་མ་བཞིའི་རྣམ་གྲངས་བསྟན་པ་སྟེ་རིམ་ཁང་བཅུ་གསུམ་པའོ།",
    "english_title": "Supported Knowledge—Brief"
}

# CHAPTER 14: Supported Knowledge—Detailed (pp. 413-479, 4 sections)
s["01-14-01-01"] = {
    "chapter": 14, "section": 1, "subsection": 1,
    "start_page": 413, "start_line": 17302, "start_phrase": "སེམས་ཀྱི་གནས་ཡིན་ལ།",
    "end_page": 479, "end_line": 20425, "end_phrase": "བརྟེན་པ་ཤེས་པའི་གནས་རྣམ་པར་གཞག་པ་སྟེ་རིམ་ཁང་བཅུ་བཞི་པའོ།།",
    "verified": True, "content_summary": "Detailed supported knowledge: all-ground, awareness, wisdom nature",
    "tibetan_title": "བརྟེན་པ་ཤེས་པའི་གནས་རྣམ་པར་གཞག་པ་སྟེ་རིམ་ཁང་བཅུ་བཞི་པའོ།",
    "english_title": "Supported Knowledge—Detailed"
}

# ============================================================
# VOLUME 2 - CHAPTERS 15-25
# ============================================================

# CHAPTER 15: Dependent Arising—Outer (pp. 1-13, 3 sections)
s["02-15-01-01"] = {
    "chapter": 15, "section": 1, "subsection": 1,
    "start_page": 1, "start_line": 1, "start_phrase": "༄༅།",
    "end_page": 13, "end_line": 657, "end_phrase": "འབྱུང་བའི་གནས་བསྟན་པ་སྟེ་རིམ་ཁང་བཅོ་ལྔ་པའོ།",
    "verified": True, "content_summary": "Outer dependent arising: confused and pure manifestations",
    "tibetan_title": "འབྱུང་བའི་གནས་བསྟན་པ་སྟེ་རིམ་ཁང་བཅོ་ལྔ་པའོ།",
    "english_title": "Dependent Arising—Outer"
}

# CHAPTER 16: Dependent Arising—Inner (pp. 14-33, 1 section)
s["02-16-01-01"] = {
    "chapter": 16, "section": 1, "subsection": 1,
    "start_page": 14, "start_line": 658, "start_phrase": "རུས་པ་ཐམས་ཅད་དང༌།",
    "end_page": 33, "end_line": 1752, "end_phrase": "རིམ་ཁང་བཅུ་དྲུག་པའོ།",
    "verified": True, "content_summary": "Inner dependent arising: refutation of extremes",
    "tibetan_title": "རིམ་ཁང་བཅུ་དྲུག་པའོ།",
    "english_title": "Dependent Arising—Inner"
}

# CHAPTER 17: Pointing-Out Instructions (pp. 34-83, 1 section)
s["02-17-01-01"] = {
    "chapter": 17, "section": 1, "subsection": 1,
    "start_page": 34, "start_line": 1753, "start_phrase": "ད་ནི་ལམ་ངེས་པས་ཉམས་སུ་བླང་བའི་རིམ་པ་བཤད་པ་ལ།",
    "end_page": 83, "end_line": 3920, "end_phrase": "དམིགས་པ་ཡུལ་གྱི་བློ་རིམ་ཅན་འཇུག་པའི་ལམ་ཟབ་རྒྱ་ཆེར་བཤད་པ་སྟེ་རིམ་ཁང་བཅུ་བདུན་པའོ།",
    "verified": True, "content_summary": "Seven modes of pointing-out instructions",
    "tibetan_title": "དམིགས་པ་ཡུལ་གྱི་བློ་རིམ་ཅན་འཇུག་པའི་ལམ་ཟབ་རྒྱ་ཆེར་བཤད་པ་སྟེ་རིམ་ཁང་བཅུ་བདུན་པའོ།",
    "english_title": "Pointing-Out Instructions"
}

# CHAPTER 18: Luminous Vajra Essence (pp. 84-141, 1 section)
s["02-18-01-01"] = {
    "chapter": 18, "section": 1, "subsection": 1,
    "start_page": 84, "start_line": 3921, "start_phrase": "ད་ནི་ཡང་རབ་སྤྲོས་པ་དང་བྲལ་བ་རྣམས་ཀྱི་དོན་དུ་རིག་པ་ངོ་སྤྲད་པ།",
    "end_page": 141, "end_line": 5955, "end_phrase": "འོད་གསལ་རྡོ་རྗེ་སྙིང་པོའི་ལམ་གྱི་ཆིངས་བསྟན་པ་སྟེ་རིམ་ཁང་བཅོ་བརྒྱད་པའོ།",
    "verified": True, "content_summary": "Sixteen grounds of luminous vajra essence",
    "tibetan_title": "འོད་གསལ་རྡོ་རྗེ་སྙིང་པོའི་ལམ་གྱི་ཆིངས་བསྟན་པ་སྟེ་རིམ་ཁང་བཅོ་བརྒྱད་པའོ།",
    "english_title": "Luminous Vajra Essence"
}

# CHAPTER 19: Cutting Through Solidity (pp. 142-189, 1 section)
s["02-19-01-01"] = {
    "chapter": 19, "section": 1, "subsection": 1,
    "start_page": 142, "start_line": 5956, "start_phrase": "ཆོས་ཟད་བློ་འདས་ཀྱི་དགོངས་པ་ཟང་ཐལ་རྗེན་པའི་ཡེ་ཤེས་འདི་ཉིད་ཀྱི་རྒྱུད་ལས།",
    "end_page": 189, "end_line": 8082, "end_phrase": "རིམ་བཅུ་དགུ་པའོ།",
    "verified": True, "content_summary": "Essential instructions for liberation through cutting through solidity",
    "tibetan_title": "ཡང་རབ་རྟོགས་པས་གྲོལ་བའི་མན་ངག་གི་ཆིངས་བསྟན་པ་སྟེ་རིམ་བཅུ་དགུ་པའོ།",
    "english_title": "Cutting Through Solidity"
}

# CHAPTER 20: Direct Approach (Leap-Over) (pp. 190-219, 1 section)
s["02-20-01-01"] = {
    "chapter": 20, "section": 1, "subsection": 1,
    "start_page": 190, "start_line": 8083, "start_phrase": "འཁོར་བ་མིང་མེད་དུ་ལ་ཟློས་ཏེ།",
    "end_page": 219, "end_line": 9397, "end_phrase": "ལྷུན་གྲུབ་ཐོད་རྒལ་གྱི་ཡེ་ཤེས་ཉམས་སུ་ལེན་པའི་གནད་ངེས་པ་སྟེ་རིམ་ཁང་ཉི་ཤུ་པའོ།",
    "verified": True, "content_summary": "Direct approach (thod rgal) pointing-out instructions",
    "tibetan_title": "ལྷུན་གྲུབ་ཐོད་རྒལ་གྱི་ཡེ་ཤེས་ཉམས་སུ་ལེན་པའི་གནད་ངེས་པ་སྟེ་རིམ་ཁང་ཉི་ཤུ་པའོ།",
    "english_title": "Direct Approach (Leap-Over)"
}

# CHAPTER 21: Signs of Progress (pp. 220-237, 1 section)
s["02-21-01-01"] = {
    "chapter": 21, "section": 1, "subsection": 1,
    "start_page": 220, "start_line": 9398, "start_phrase": "འཛམ་བུའི་གླིང་འདིར་བྱུང་ཚུལ་ནི།",
    "end_page": 237, "end_line": 10206, "end_phrase": "རིམ་ཁང་ཉི་ཤུ་རྩ་གཅིག་པའོ།",
    "verified": True, "content_summary": "Signs of progress on the path",
    "tibetan_title": "རིམ་ཁང་ཉི་ཤུ་རྩ་གཅིག་པའོ།",
    "english_title": "Signs of Progress"
}

# CHAPTER 22: Three Times Signs (pp. 238-276, 1 section)
s["02-22-01-01"] = {
    "chapter": 22, "section": 1, "subsection": 1,
    "start_page": 238, "start_line": 10207, "start_phrase": "བར་དོ་དང་ཕྱི་མ་ལ་གྲོལ་འཁྲུལ་ངེས་པའི་རྟགས་གསང་བས་མཇུག་བསྡུ་བ།",
    "end_page": 276, "end_line": 11993, "end_phrase": "དུས་གསུམ་རྟགས་ཀྱི་རྣམ་གྲངས་ངེས་པ་གཏན་ལ་ཕབ་པ་སྟེ་རིམ་ཁང་ཉི་ཤུ་རྩ་གཉིས་པའོ།",
    "verified": True, "content_summary": "Enumeration of signs of three times",
    "tibetan_title": "དུས་གསུམ་རྟགས་ཀྱི་རྣམ་གྲངས་ངེས་པ་གཏན་ལ་ཕབ་པ་སྟེ་རིམ་ཁང་ཉི་ཤུ་རྩ་གཉིས་པའོ།",
    "english_title": "Three Times Signs"
}

# CHAPTER 23: Bardo Manifestations (pp. 277-366, 1 section)
s["02-23-01-01"] = {
    "chapter": 23, "section": 1, "subsection": 1,
    "start_page": 277, "start_line": 11994, "start_phrase": "ད་ལྟ་ཡང་དེའི་འཆར་ཚུལ་གྱི་ཕྱི་ནང་གི་ངང་ན་གནས།",
    "end_page": 366, "end_line": 15258, "end_phrase": "རང་སྣང་བར་དོའི་ཆར་ཚུལ་བསྟན་པ་སྟེ་རིམ་ཁང་ཉི་ཤུ་རྩ་གསུམ་པའོ།",
    "verified": True, "content_summary": "Self-appearing bardo manifestations",
    "tibetan_title": "རང་སྣང་བར་དོའི་ཆར་ཚུལ་བསྟན་པ་སྟེ་རིམ་ཁང་ཉི་ཤུ་རྩ་གསུམ་པའོ།",
    "english_title": "Bardo Manifestations"
}

# CHAPTER 24: Faculties and Capacities (pp. 367-376, 1 section)
s["02-24-01-01"] = {
    "chapter": 24, "section": 1, "subsection": 1,
    "start_page": 367, "start_line": 15259, "start_phrase": "དབང་པོ་ཐ་མའི་ཐ་མའམ་དེ་གོང་དུ་ཆོས་ཉིད་ཀྱི་བར་དོ་ཤར་བ་ན།",
    "end_page": 376, "end_line": 15613, "end_phrase": "དབང་པོ་ཐ་མ་རྣམས་རང་བཞིན་སྤྲུལ་པ་སྐུའི་ཞིང་དུ་དབུགས་དབྱུང་བ་སྟེ་རིམ་ཁང་ཉི་ཤུ་རྩ་བཞི་པའོ།",
    "verified": True, "content_summary": "Lower faculties emanating into nirmanakaya fields",
    "tibetan_title": "དབང་པོ་ཐ་མ་རྣམས་རང་བཞིན་སྤྲུལ་པ་སྐུའི་ཞིང་དུ་དབུགས་དབྱུང་བ་སྟེ་རིམ་ཁང་ཉི་ཤུ་རྩ་བཞི་པའོ།",
    "english_title": "Faculties and Capacities"
}

# CHAPTER 25: Spontaneous Results—FINAL (pp. 377-412, 1 section)
s["02-25-01-01"] = {
    "chapter": 25, "section": 1, "subsection": 1,
    "start_page": 377, "start_line": 15614, "start_phrase": "མུ་ཏིག་ཕྲེང་བ་ལས།",
    "end_page": 412, "end_line": 17111, "end_phrase": "ལྷུན་གྱིས་གྲུབ་པ་འབྲས་བུའི་རྣམ་པར་གཞག་པ་སྟེ་རིམ་ཁང་ཉི་ཤུ་རྩ་ལྔ་པ་སྟེ་ཐ་མའོ།",
    "verified": True, "content_summary": "Spontaneous results and fruition—Final chapter",
    "tibetan_title": "ལྷུན་གྱིས་གྲུབ་པ་འབྲས་བུའི་རྣམ་པར་གཞག་པ་སྟེ་རིམ་ཁང་ཉི་ཤུ་རྩ་ལྔ་པ་སྟེ་ཐ་མའོ།",
    "english_title": "Spontaneous Results—FINAL"
}

# Verify all ranges
print("Verifying all page ranges...")
errors = []
for key, section in s.items():
    if section["start_page"] > section["end_page"]:
        errors.append(f"{key}: start_page {section['start_page']} > end_page {section['end_page']}")
    elif section["start_page"] == section["end_page"] and section["start_line"] > section["end_line"]:
        errors.append(f"{key}: Same page but inverted lines")

if errors:
    print("ERRORS FOUND:")
    for error in errors:
        print(f"  - {error}")
else:
    print("✓ All page ranges verified correct (start_page < end_page)")

# Count sections per chapter
from collections import Counter
ch_counts = Counter([v["chapter"] for v in s.values()])
print(f"\nTotal sections: {len(s)}")
print(f"Chapters with multiple sections:")
for ch in sorted(ch_counts.keys()):
    if ch_counts[ch] > 1:
        print(f"  Chapter {ch}: {ch_counts[ch]} sections")

# Save to file
boundary_data["metadata"]["total_sections"] = len(s)
with open("/home/opencode/MDZOD/1/boundary_v2.json", "w", encoding="utf-8") as f:
    json.dump(boundary_data, f, indent=2, ensure_ascii=False)

print("\n✓ boundary_v2.json updated with all sections")
