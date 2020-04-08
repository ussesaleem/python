"""
This document contains the code for all the functions in Marvin.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import mood

def menu():
    """
    Prints menu
    """
    print("1) What is your name?")
    print("2) Convert Celsius to Fahrenheit.")
    print("3) Word-echoeing.")
    print("4) Sum of values.")
    print("5) Comparing values.")
    print("6) Increasing strings.")
    print("7) Isogram check.")
    print("8) Toss the letters.")
    print("9) Anagram check.")
    print("10) Creating an acronym.")
    print("11) Masking a string.")
    print("12) What's Marvin's mood?")
    print("You can also choose to type the commands: 'inv', 'citat', 'hej' or 'lunch'.")
    print("q) Quit.")

def greeter():
    """
    Print greeting.
    """
    name = input("What is your name? ")
    print("\nMarvin says:")
    print("Hello %s - your awesomeness!" % name)
    print("\nWhat can I do you for?!")

def celsius_converter():
    """
    Converts celsius into Fahrenheit.
    """
    temperature = input("Please insert temperature in Celsius and let me do my magic: ")
    if temperature.isdigit:
        fahrenhet = int(temperature) * 9 / 5 + 32
    else:
        print("Sorry, seems like you got some letters into your input. Kindly try again and only insert numbers.")
    print("\nMarvin says:")
    print("According to my calculations, %s Celsius is" % temperature, fahrenhet, "in Fahrenheit.")
    print("\nWhat can I do you for?!")

def word_echo():
    """
    Echoes a word that's inserted.
    """
    word = input("Insert a word: ")
    number = input("Insert a number: ")
    print("\nMarvin says:")
    print("%s " % word * int(number))
    print("\nWhat can I do you for?!")

def sum_of_values():
    """
    Sums up all the inserted values.
    """
    count = 0
    total = 0
    number = 0
    while number != "Done":
        number = input("Enter a number, type Done to quit: ")
        if number != "Done":
            total += int(number)
            count += 1
    if count:
        mean = total / count
    print("\nMarvin says:")
    print("The sum of your entered numbers is %s" % total, "with the mean value of", mean, ".")
    print("\nWhat can I do you for?!")

def comparing_values():
    """
    Compares the last inserted and the previous value.
    """
    previous = input("Insert a number: ")
    current = input("Insert another number: ")
    while current != "Done":
        if int(current) > int(previous):
            print("The last inserted value, %s, is larger than the previous number." % current)
        elif int(current) < int(previous):
            print("The last inserted value, %s, is smaller than the previous number." % current)
        else:
            print("The last inserted value and the previous value are the same.")
        previous = current
        current = input("Insert another number, type Done to quit: ")
    print("\nMarvin says:")
    print("\nWhat can I do you for?!")

def increasing_strings():
    """
    Increases the letter by index number of letter of the inserted word.
    """
    word = str(input("Enter a word: "))
    new_word = ""
    for letter, value in enumerate(word, 1):
        new_word += letter * value + "-"
    new_word = new_word[:-1]
    print("\nMarvin says:")
    print(new_word)
    print("\nWhat can I do you for?!")

def isogram_check():
    """
    Checks if the inserted word is an isogram or not.
    """
    word = input("Enter a word for isogram check: ")
    isogram = "True"
    for letter in word:
        count = word.count(letter)
        if count > 1:
            isogram = False
    print("\nMarvin says:")
    if isogram == "True":
        print("Match")
    else:
        print("No Match")
    print("\nWhat can I do you for?!")

def toss_the_letters():
    """
    Tosses around the letters of the inserted word randomly.
    """
    word = input("Enter a word: ")
    shuffle_word = ""
    length = len(word) - 1
    while length >= 0:
        index = random.randint(0, int(length))
        shuffle_word += word[index]
        word = word[:index] + word[index + 1:]
        length = len(word) - 1
    print(shuffle_word)
    print("\nWhat can I do you for?!")

def anagram_check():
    """
    Comparing two inserted strings to check if they are anagrams.
    """
    string_one = input("Insert first string: ")
    string_two = input("Insert second string: ")
    string_one = string_one.lower()
    string_two = string_two.lower()
    new_string_one = sorted(string_one)
    new_string_two = sorted(string_two)

    if new_string_one == new_string_two:
        answer = "Match"
    else:
        answer = "No Match"
    print(answer)
    print("\nWhat can I do you for?!")

def create_acronym():
    """
    Creating acronyms of inserted string.
    """
    the_string = input("Insert a string: ")
    new_string = ""
    for letter in the_string:
        if letter.isupper():
            new_string += letter
        else:
            continue
    print(new_string)
    print("\nWhat can I do you for?!")

def string_masking():
    """
    Masking the string except for the last 4 letters.
    """
    a_string = input("Input a string: ")
    front_string = ""
    length = len(a_string) - 4
    for _ in range(0, length):
        front_string += "#"
    end_string = a_string[-4:]
    answer = str(front_string) + end_string
    print(answer)
    print("\nWhat can I do you for?!")

def marvin_mood():
    """
    Prints a string of text with combined values.
    """
    mood.the_mood()
