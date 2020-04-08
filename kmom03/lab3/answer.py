#!/usr/bin/env python3

"""
aa70365e78c55682e1cc08e0a571e2ec
python
lab3
v3
ussa19
2019-09-30 21:18:46
v4.0.0 (2019-03-05)

Generated 2019-09-30 23:18:46 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 3 - python
#
# In these exercises we will work with functions.
#



# --------------------------------------------------------------------------
# Section 1. Functions
#
#
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a function called `greeter` that returns `"Hi, the weather is nice
# today!"`.
#
# Answer with the return value from a call to the function.
#
# Write your code below and put the answer into the variable ANSWER.
#

def greeter():
    """
    Greets with a weather-check.
    """
    greeting = "Hi, the weather is nice today!"
    return greeting



ANSWER = greeter()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Assign the words: 'melon' and 'cabbage' to two different variables.
#
# Create a function and pass the two words as arguments to it. Your function
# should return them as a single word.
#
# Answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#

def single_word(variable_one, variable_two):
    """
    Puts together both words to one.
    """
    say = variable_one + variable_two
    return say



ANSWER = single_word("melon", "cabbage")

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Create a function called `funny_word` that takes one argument and prepends
# it to the string ' is a funny word'. **EXAMPLE:** If the argument is
# 'water', the function should return: `"water is a funny word"`.
#
# Use the argument 'sunshine' and answer with a call to the function.
#
# Write your code below and put the answer into the variable ANSWER.
#

def funny_word(word):
    """
    If you put in a word, it will always tell you it's a funny word.
    """
    reply = str(word) + " is a funny word"
    return reply




ANSWER = funny_word("sunshine")

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Create a function called `summation` that takes two arguments. The function
# should return the sum of the two arguments.
#
# Answer with the return value from a call to the function with the two
# arguments 15 and 51.
#
# Write your code below and put the answer into the variable ANSWER.
#

def summation(thefirst, thesecond):
    """
    The function that will help you sum up your values.
    """
    thesum = thefirst + thesecond
    return thesum




ANSWER = summation(15, 51)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Create a function called `multiplication` that takes two arguments. The
# function should return the product of the two arguments.
#
# Answer with the return value from a call to the function with the two
# arguments 15 and 51.
#
# Write your code below and put the answer into the variable ANSWER.
#

def multiplication(thethird, thefourth):
    """
    The function will present the product of any values that you insert.
    """
    thesumtwo = thethird * thefourth
    return thesumtwo




ANSWER = multiplication(15, 51)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (1 points)
#
# Create a function called `in_range` that takes one argument. The function
# should return `True` if the argument is higher than 50 and lower than 100.
# If the number is out of range, the function should return `False`. The
# return type should be boolean.
#
# Use the argument 79 and answer with a call to the function.
#
# Write your code below and put the answer into the variable ANSWER.
#

def in_range(testit):
    """
    The function will test if the value you insert is between 50 and 100.
    """
    test = testit > 50 and testit < 100
    return test




ANSWER = in_range(79)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.7 (1 points)
#
# Create a function called `multiplicator`. Inside the function create a loop
# that iterates from 5 to 20 (both included). For each number use the
# `multiplication` function from above to get the square of the current
# number. The function should return a comma-separated string of the squared
# numbers,  without an ending `,`.
#
# Answer with a call to the function `multiplicator`.
#
# Write your code below and put the answer into the variable ANSWER.
#



def multiplicator():
    """
    The function will add all the products in the range 5-20 into a string.
    """
    end = ""
    for i in range(5, 21):
        product = multiplication(i, i)
        end += str(product) + ","
    end = end[:-1]
    return end




ANSWER = multiplicator()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.7", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.8 (1 points)
#
# Create a function called `decider`. The function takes one argument. If the
# argument is a string return a call to `funny_word()`, if the argument is an
# integer return the square of the argument by using the `multiplication`
# function.
#
# Answer with a call to the function `decider` with the value `69` as
# argument.
#
# Write your code below and put the answer into the variable ANSWER.
#


def decider(word_or_number):
    """
    The function will test if the inserted value is a string or integer and give the output accordingly.
    """
    if isinstance(word_or_number, int):
        output = multiplication(word_or_number, word_or_number)
    else:
        output = funny_word(word_or_number)
    return output



ANSWER = decider(69)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.8", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.9 (1 points)
#
# Create a function called `double_decider`. The function takes two
# arguments. For each argument call the `decider` function. Concatenate the
# returned values in a string.
#
# Separate the two values by ' and the square is '.
#
# Answer with a call to the function `double_decider` with the values:
# blunderbuss and 68 as arguments.
#
# Write your code below and put the answer into the variable ANSWER.
#

def double_decider(one, two):
    """
    The function will test if the inserted value is a string or integer and give the output accordingly.
    """
    if isinstance(one, int):
        output_one = multiplication(one, one)
    else:
        output_one = funny_word(one)
    if isinstance(two, int):
        output_two = multiplication(two, two)
    else:
        output_two = funny_word(two)
    return str(output_one) + " and the square is " + str(output_two)




ANSWER = double_decider("blunderbuss", 68)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.9", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (3 points)
#
# Create a function that returns a binary string value of a given integer.
# Return only the binary number and not any identification that it is a
# binary number.
#
# Example: Calling the function with the number 3 should return `"11"`.
#
# Answer with a call to the function with the argument 79.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (3 points)
#
# Write a Python function that accepts a string and calculate the number of
# upper case letters and lower case letters. The function should return a
# string with the format "Lower case letters: #, upper case letters: #". Only
# count letters, you can ignore space and special characters.
#
# Answer with a call to the function with the argument: `"Pack my Box with
# five dozen LiQuor juGs."`.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)


dbwebb.exit_with_summary()
