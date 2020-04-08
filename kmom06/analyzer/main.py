#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This file contains the commando-loop which will use the codes from the files menu.py and analyzer.py.
"""

import menu
import analyzer

while True:
    try:
        choice = input("--> ")
    except EOFError as e:
        print(end="")

    if choice == "q":
        print("Goodbye!")
        break

    elif choice == "menu":
        menu.menu()

    elif choice == "lines":
        analyzer.lines()
        print("Number of lines: " + str(analyzer.lines()))

    elif choice == "words":
        analyzer.words()
        print("Number of words: " + str(analyzer.words()))

    elif choice == "letters":
        analyzer.letters()
        print("Number of letters: " + str(analyzer.letters()))

    elif choice == "word_frequency":
        analyzer.word_frequency()
        print(analyzer.word_frequency())

    elif choice == "letter_frequency":
        analyzer.letter_frequency()
        print(analyzer.letter_frequency())

    elif choice == "all":
        analyzer.all_functions()
        print(analyzer.all_functions())

    elif choice == "change":
        analyzer.change()

    else:
        print("That is not a valid choice. Please typ 'menu' to see the menu options.")
