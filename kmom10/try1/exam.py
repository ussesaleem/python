#!/usr/bin/env python3
"""
Write your code in this file. Fill out the defined functions with your solutions.
You are free to write additional functions and modules as you see fit.
"""

def find_replace():
    """
    Assignment 1
    """
    find = input("Enter word to find: ")
    change = input("Enter word to replace with: ")

    find_space = " " + find + " "
    change_space = " " + change + " "
    find_period = " " + find + "."
    change_period = " " + change + "."
    find_comma = " " + find + ","
    change_comma = " " + change + ","
    find_excla = " " + find + "!"
    change_excla = " " + change + "!"
    find_quest = " " + find + "?"
    change_quest = " " + change + "?"
    find_dash = " " + find + "-"
    change_dash = " " + change + "-"
    find_enter = " " + find + "\n"
    change_enter = " " + change + "\n"
    find_space_alt = "\n" + find + " "
    change_space_alt = "\n" + change + " "
    find_period_alt = "\n" + find + "."
    change_period_alt = "\n" + change + "."
    find_comma_alt = "\n" + find + ","
    change_comma_alt = "\n" + change + ","
    find_excla_alt = "\n" + find + "!"
    change_excla_alt = "\n" + change + "!"
    find_quest_alt = "\n" + find + "?"
    change_quest_alt = "\n" + change + "?"
    find_dash_alt = "\n" + find + "-"
    change_dash_alt = "\n" + change + "-"
    find_enter_alt = "\n" + find + "\n"
    change_enter_alt = "\n" + change + "\n"

    with open("manifesto.txt", "r") as f:
        open_output = open("output.txt", "w")
        text = f.read()
        text = text.replace(find_space, change_space)
        text = text.replace(find_period, change_period)
        text = text.replace(find_comma, change_comma)
        text = text.replace(find_excla, change_excla)
        text = text.replace(find_quest, change_quest)
        text = text.replace(find_dash, change_dash)
        text = text.replace(find_enter, change_enter)
        text = text.replace(find_space_alt, change_space_alt)
        text = text.replace(find_period_alt, change_period_alt)
        text = text.replace(find_comma_alt, change_comma_alt)
        text = text.replace(find_excla_alt, change_excla_alt)
        text = text.replace(find_quest_alt, change_quest_alt)
        text = text.replace(find_dash_alt, change_dash_alt)
        text = text.replace(find_enter_alt, change_enter_alt)
        open_output.write(text)
        open_output.close()


def count_animals(animals):
    """
    Assignment 2
    """
    for animal in animals:
        if type(animals[animal]) is not list:
            animals = list(animals[animal])

    for name in animals:
        animals[name] = sorted(animals[name])

    numbers_list = []
    sort_by_number = {}
    for animal in animals:
        quant = len(animals[animal])
        if quant not in sort_by_number:
            sort_by_number[quant] = []
            numbers_list.append(quant)
        names = str(animals[animal]).replace("[", "").replace("]", "").replace("\'", "")
        result = animal + ": " + names
        sort_by_number[quant].append(result)
    numbers_list = sorted(numbers_list)

    for number in sort_by_number:
        sort_by_number[number] = sorted(sort_by_number[number])

    end_result = ""
    for numbers in numbers_list:
        for animal in sort_by_number[numbers]:
            end_result += str(numbers) + " " + str(animal) + "\n"

    return end_result.strip("\n")


def validate_isbn(numbers):
    """
    Assignment 3
    """

    return numbers

def decide_winners(matches):
    """
    Assignment 4
    """
    return matches

def validate_bookings(bookings):
    """
    Assignment 5
    """
    return bookings

if __name__ == '__main__':
    find_replace()
    count_animals({})
    validate_isbn("")
    decide_winners([])
    validate_bookings([])
