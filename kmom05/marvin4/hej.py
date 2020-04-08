"""
The file contains the code for randomly picking hej upon saying hi to Marvin.
"""
import random

hej = ["Hej själv!",
       "Trevligt att du bryr dig om mig.",
       "Tjena!",
       "Det var länge sedan någon var trevlig mot mig.",
       "Hej!",
       "Halloj, det ser ut att bli mulet idag.",
       "Tjo!"]

greeting = ["Ja, vad kan jag göra för Dig?",
            "Låt mig hjälpa dig med dina strävanden.",
            "Ursäkta, vad önskas?",
            "Kan jag stå till din tjänst?",
            "Jag kan svara på alla dina frågor.",
            "Ge me hög-fem!",
            "Jag svarar endast inför Usama, det är min enda Master Chief.",
            "Oh, ursäkta, jag slumrade visst till."]

def random_hej():
    """
    Picks a random hej from the list hej.
    """
    lines = len(hej)
    index = random.randint(0, lines - 1)
    line = "\n" + hej[index]
    greet_lines = len(greeting)
    greet_index = random.randint(0, greet_lines - 1)
    greet = greeting[greet_index]
    print(line + " " + greet)
