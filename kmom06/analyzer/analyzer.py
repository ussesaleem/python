#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This file contains the functions for textanalysis used in this exercise.
"""

FILENAME = "phil.txt"

def lines():
    """
    This function will count the lines in the chosen text file, excluding blank lines.
    """
    num_lines = 0
    with open(FILENAME, "r") as f:
        for line in f:
            if line.strip():
                num_lines += 1
    return num_lines

def words():
    """
    This function will count words in the chosen text file.
    """
    word_count = 0
    with open(FILENAME, "r") as f:
        for line in f:
            word_count += len(line.split())
    return word_count

def letters():
    """
    This function will count letters in the chosen text file.
    """
    with open(FILENAME, "r") as f:
        total_letters = 0
        for char in f.read().replace(" ", ""):
            if char not in " -.,?!\n":
                total_letters += 1
    return total_letters

def word_frequency():
    """
    This function will show the 7 most used words in the chosen text file.
    """
    with open(FILENAME) as f:
        words_list = f.read().split()
        words_count = {}
        for word in words_list:
            word = word.lower().replace(",", "").replace(".", "").replace("!", "").replace("?", "")
            if word not in words_count:
                words_count[word] = 1
            else:
                words_count[word] += 1
        freq_dict = {}
        for word in words_count:
            number = words_count[word]
            if number in freq_dict:
                freq_dict[number].append(word)
            else:
                freq_dict[number] = []
                freq_dict[number].append(word)
        sorted_d = sorted(freq_dict, reverse=True)
        all_the_words_sorted = []
        for number in sorted_d:
            temp_list = freq_dict[number]
            for i in temp_list:
                all_the_words_sorted.append(i)
        top_seven = all_the_words_sorted[:7]
        total_words = len(words_list)
        final = ""
        for word in top_seven:
            percentage = round(words_count[word] / total_words * 100, 1)
            final += "   " + word + ": " + str(words_count[word]) + " | " + str(percentage) + "%\n"
        return final

def letter_frequency():
    """
    This function will show the 7 most used letters in the chosen text file.
    """
    with open(FILENAME) as f:
        letter = {}
        total_letters = 0
        for char in f.read():
            char = char.lower()
            if char not in " -.,?!\n":
                total_letters += 1
                if char not in letter:
                    letter[char] = 1
                else:
                    letter[char] += 1
        freq_dict = {}
        for char in letter:
            number = letter[char]
            if number in freq_dict:
                freq_dict[number].append(char)
            else:
                freq_dict[number] = []
                freq_dict[number].append(char)
        sorted_d = sorted(freq_dict, reverse=True)
        all_the_letters_sorted = []
        for number in sorted_d:
            temp_list = freq_dict[number]
            for i in temp_list:
                all_the_letters_sorted.append(i)
        top_seven = all_the_letters_sorted[:7]
        final = ""
        for char in top_seven:
            percentage = round(letter[char] / total_letters * 100, 1)
            final += "   " + char + ": " + str(letter[char]) + " | " + str(percentage) + "%\n"
        return final

def all_functions():
    """
    This function will run all the analysis functions on the chosen text file.
    """
    return "lines: " + str(lines()) + "\n" \
    + "words: " + str(words()) + "\n" \
    + "letters: " + str(letters()) + "\n" + "\n" \
    + "word_frequency:\n" + str(word_frequency()) + "\n" + "\n" \
    + "letter_frequency:\n" + str(letter_frequency())

def change():
    """
    This function will change which file to analyze.
    """
    global FILENAME
    FILENAME = input("Enter filename: ")
    return
