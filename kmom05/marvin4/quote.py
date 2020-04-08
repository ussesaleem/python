"""
The file contains the code for randomly picking quotes upon asking Marvin for citations.
"""
import random

filename = "quotes.txt"

def random_quote():
    """
    Picks a random quote from the textfile quotes.txt.
    """
    with open(filename) as filehandle:
        all_lines = filehandle.readlines()
        lines = len(all_lines)
        index = random.randint(0, lines - 1)
        line = "\n" + all_lines[index]
    print(line)
