"""
The file contains the code for randomly picking a lunch restaurant upon mentioning lunch to Marvin.
"""
import random

lunchplaces = ["thairestaurangen vid korsningen",
               "det är lite mysigt i fiket jämte demolabbet",
               "Indiska",
               "Pappa curry",
               "boden uppe på parkeringen",
               "Bergåsa kebab",
               "Pasterian",
               "Villa Oscar",
               "Eat here",
               "Bistro J"]

def lunch_places():
    """
    Picks a random lunch restaurant from the list lunchplaces.
    """
    lines = len(lunchplaces)
    index = random.randint(0, lines - 1)
    line = lunchplaces[index]
    return line

lunch = ["Ska vi ta " + lunch_places() + "?",
         "Ska vi dra ned till " + lunch_places() + "?",
         "Jag tänkte käka på " + lunch_places() + ", ska du med?",
         "På " + lunch_places() + " är det mysigt, ska vi ta där?"]

def random_lunch():
    """
    Picks a random lunch restaurant from the list lunch.
    """
    lines = len(lunch)
    index = random.randint(0, lines - 1)
    line = "\n" + lunch[index]
    print(line)
