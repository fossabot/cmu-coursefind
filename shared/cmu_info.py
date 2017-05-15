﻿# @file cmu_info.py
# @brief Stores information about CMU.
# @author Justin Chu (justinchuby@cmu.edu)


ONETWELVE = ["I love 112 !",
             "Carpe Diem !",
             "Hot Diggity",
             "\"THINK rather than kicking the code a little bit and somehow let it pass test cases.\"",
             "\"Onward !\"",
             "\"Live purposefully.\""]

CMU_BUILDINGS = {
    "baker": "BH",
    "cyert": "CYH",
    "doherty": "DH",
    "stadium": "GES",
    "gates": "GHC",
    "weigand": "GYM",
    "gymnasium": "GYM",
    "gym": "GYM",
    "hamburg": "HBH",
    "hamerschlag": "HH",
    "hunt": "HL",
    "library": "HL",
    "tepper": "POS",
    "posner": "POS",
    "gsia": "IA",
    "mellon": "MI",
    "newell": "NSH",
    "simon": "NSH",
    "purnell": "PCA",
    "porter": "PH",
    "roberts": "REH",
    "scaife": "SH",
    "warner": "WH",
    "wean": "WEH"
}

CMU_BUILDINGS_ABBR = {'bh', 'cfa', 'cic', 'cyh', 'dh', 'eds', 'ges',
    'ghc', 'gym', 'hbh', 'hh', 'hl', 'ia', 'ini', 'mi', 'mm', 'nsh',
    'pca', 'pos', 'ph', 'ptc', 'reh', 'scr', 'sei', 'sh', 'uc', 'wh', 'weh'}

DAYS_STRING = { "mon": 1,
                "tue": 2,
                "wed": 3,
                "thu": 4,
                "fri": 5,
                "sat": 6,
                "sun": 0,
                "monday": 1,
                "tuesday": 2,
                "wednesday": 3,
                "thursday": 4,
                "friday": 5,
                "saturday": 6,
                "sunday": 0}

CMU_BUILDINGS_FROM_ABBR = {
    "BH": "Baker Hall" ,
    "CYH": "Cyert Hall" ,
    "DH": "Doherty Hall" ,
    "EDS": "Elliot Dunlap Smith Hall",
    "GES": "Gesling Stadium",
    "GHC": "Gates and Hillman Centers" ,
    # "GYM": "Weigand Gymnasium",
    "HBH": "Hamburg Hall" ,
    "HH": "Hamerschlag Hall" ,
    "HL": "Hunt Library" ,
    "POS": "Posner Hall" ,
    "IA": "GSIA (Tepper School of Business)" ,
    "MI": "Mellon Institute" ,
    "NSH": "Newell-Simon Hall" ,
    "PCA": "Purnell Center for the Arts" ,
    "PH": "Porter Hall" ,
    "REH": "Roberts Engineering Hall" ,
    "SH": "Scaife Hall" ,
    "WH": "Warner Hall" ,
    "WEH": "Wean Hall" ,
    "SCR": "300 South Craig Street",
    "SEI": "Software Engineering Institute",
    "PTC": "Pittsburgh Technology Center - 2nd Avenue",
    "INI": "4616 Henry Street",
    "MM": "Margaret Morrison Carnegie Hall",
    "CIC": "Collaborative Innovation Center",
    "CFA": "College of Fine Arts"
}

CMU_NUMBER_DEPARTMENTS = {
    "48": "Architecture",
    "60": "Art",
    "52": "BXA Intercollege Degree Programs",
    "83": "Biological Sciences",
    "42": "Biomedical Engineering",
    "70": "Business Administration",
    "62": "CFA Interdisciplinary",
    "39": "CIT Interdisciplinary",
    "99": "Carnegie Mellon University-Wide Studies",
    "64": "Center for the Arts in Society",
    "86": "Center for the Neural Basis of Cognition",
    "06": "Chemical Engineering",
    "09": "Chemistry",
    "12": "Civil & Environmental Engineering",
    "02": "Computational Biology",
    "15": "Computer Science",
    "62": "Computer Science and Arts",
    "93": "Creative Enterprise:Sch of Pub Pol & Mgt",
    "51": "Design",
    "67": "Dietrich College Information Systems",
    "66": "Dietrich College Interdisciplinary",
    "54": "Drama",
    "73": "Economics",
    "18": "Electrical & Computer Engineering",
    "20": "Electronic Commerce",
    "19": "Engineering & Public Policy",
    "76": "English",
    "53": "Entertainment Technology Pittsburgh",
    "65": "General Dietrich College",
    "94": "Heinz College Wide Courses",
    "79": "History",
    "05": "Human-Computer Interaction",
    "62": "Humanities and Arts",
    "04": "Information & Communication Technology",
    "14": "Information Networking Institute",
    "95": "Information Systems:Sch of IS & Mgt",
    "84": "Institute for Politics and Strategy",
    "08": "Institute for Software Research",
    "49": "Integrated Innovation Institute",
    "11": "Language Technologies Institute",
    "38": "MCS Interdisciplinary",
    "10": "Machine Learning",
    "27": "Materials Science & Engineering",
    "21": "Mathematical Sciences",
    "24": "Mechanical Engineering",
    "92": "Medical Management:Sch of Pub Pol & Mgt",
    "82": "Modern Languages",
    "57": "Music",
    "32": "Naval Science - ROTC",
    "80": "Philosophy",
    "69": "Physical Education",
    "33": "Physics",
    "85": "Psychology",
    "91": "Public Management:Sch of Pub Pol & Mgt",
    "90": "Public Policy & Mgt: Sch of Pub Pol & Mgt",
    "16": "Robotics",
    "62": "Science and Arts",
    "88": "Social & Decision Sciences",
    "17": "Software Engineering",
    "36": "Statistics",
    "98": "StuCo (Student Led Courses)",
    "45": "Tepper School of Business",
    "03": " Biological Sciences"
}