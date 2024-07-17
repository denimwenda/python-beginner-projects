# Store all the questions to asked, and returns the dictionary
def easy_question(num):
    easy_question_bank = {
        2: "COVID19 originated from which country?",
        3: "Which animal is known as the 'Ship of the Desert'?",
        4: "How many years are there in one Millenium?",
        8: "Who painted the monalisa?",
        9: "What is the largest country in world?",
        14: "What does the AC button on a calculator stand for?",
        15: "What is the largest building in the world?",
        16: "Which one of this is a fish: a whale, a shark or a dolphin?",
    }
    
    return easy_question_bank[num]

# Store all the hard questions to be asked, and returns the dictionary
def hard_question(num):
    hard_question_bank = {
        1: "What does ICAO stand for?",
        5: "Name the planet known as the Red Planet?",
        6: "Who is the founder of SpaceX?",
        7: "What is the capital of finland?",
        10: "How man valves does the heart have?",
        11: "What nut is in middle of a Ferrero Rocher?",
        12: "How many elements are there in the periodic table?",
        13: "how many bones does a shark have?",
    }
    
    return hard_question_bank[num]