#!/usr/bin/env python3

"""
2409ec437d1f4b87e01ccd90d2ad7f25
python
lab5
v3
ussa19
2019-10-17 20:40:21
v4.0.0 (2019-03-05)

Generated 2019-10-17 22:40:21 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 5 - python
#
# "In these exercises we will take a look into lists."
#



# --------------------------------------------------------------------------
# Section 1. List basics
#
#
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Concatenate the two lists [Berenger, Sheen] and [butterfly, piano].
#
# Answer with your list.
#
# Write your code below and put the answer into the variable ANSWER.
#

list1 = ["Berenger", "Sheen"]
list2 = ["butterfly", "piano"]

list3 = list1 + list2



ANSWER = list3

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Use the list [Dafoe, Sheen, Berenger, Depp, Whitaker].
#
# Add the words 'hotdog' and 'pirate' as the second and third element.
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#

list4 = ["Dafoe", "Sheen", "Berenger", "Depp", "Whitaker"]
list4.insert(1, "hotdog")
list4.insert(2, "pirate")




ANSWER = list4

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Use the list [Dafoe, Sheen, Berenger, Depp, Whitaker].
#
# Replace the third word with: 'painting'.
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#

list5 = ["Dafoe", "Sheen", "Berenger", "Depp", "Whitaker"]

list5[2] = "painting"



ANSWER = list5

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Sort the list
#
# > [wasp, fly, butterfly, bumblebee, mosquito]
#
# in descending alphabetical order. Answer with the sorted list.
#
# Write your code below and put the answer into the variable ANSWER.
#

list6 = ["wasp", "fly", "butterfly", "bumblebee", "mosquito"]

list6.sort(reverse=True)




ANSWER = list6

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Use `remove()` to delete the word:
#
# > 'Whitaker'
#
# from the list:
#
# > [Dafoe, Sheen, Berenger, Depp, Whitaker]
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#

list7 = ["Dafoe", "Sheen", "Berenger", "Depp", "Whitaker"]

list7.remove("Whitaker")


ANSWER = list7

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Built-in list functions
#
# Some basic built-in functions.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Use a built-in function to sum all numbers in the list:
#
# > [98, 5, 12, 369, 1]
#
# Answer with the result as an integer.
#
# Write your code below and put the answer into the variable ANSWER.
#

list8 = [98, 5, 12, 369, 1]

list8_sum = sum(list8)




ANSWER = list8_sum

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Use built-in functions, such as `sum` and `len` to get the average value of
# the list:
#
# > [123, 4, 125, 69, 155]
#
# Answer with the result as a float with at most one decimal.
#
# Write your code below and put the answer into the variable ANSWER.
#

list9 = [123, 4, 125, 69, 155]
list9_count = len(list9)
list9_sum = sum(list9)

list9_av = list9_sum / list9_count



ANSWER = round(list9_av, 1)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# Use the built-in functions `split()` and `join()` to fix this string:
#
# > "The?wind?is?blowing"
#
# into a real sentence, (without '?').
#
# Answer with the fixed string.
#
# Write your code below and put the answer into the variable ANSWER.
#

fix_string = "The?wind?is?blowing"
items_as_list = fix_string.split("?")

fixed_string = " ".join(items_as_list)


ANSWER = fixed_string

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.4 (1 points)
#
# Use slice on the list
#
# > [reggae, rock, blues, jazz, opera]
#
# and replace the second and third element with
#
# > "book, candle"
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#

list10 = ["reggae", "rock", "blues", "jazz", "opera"]

list10[1:3] = ["book", "candle"]



ANSWER = list10

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.5 (1 points)
#
# Assign the list
#
# > [a, b, c, d, e]
#
# to a variable called 'list1'.
#
# Assign the list again, but to another variable called 'list2'.
#
# Answer with the result of 'list1 is list2'.
#
# Write your code below and put the answer into the variable ANSWER.
#

list1 = ["a", "b", "c", "d", "e"]
list2 = ["a", "b", "c", "d", "e"]



ANSWER = list1 is list2

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.6 (1 points)
#
# Use your lists from the last exercise. Assign 'list1' to another variable
# called 'list3' like this:
#
# > list3 = list1
#
# Answer with the result of 'list1 is list3'.
#
# Write your code below and put the answer into the variable ANSWER.
#

list3 = list1




ANSWER = list1 is list3

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.6", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.7 (1 points)
#
# Use your lists from the last exercise. Change the first element in 'list1'
# to
#
# > "z"
#
# Answer with 'list3'.
#
# Write your code below and put the answer into the variable ANSWER.
#

list1[0] = "z"





ANSWER = list3

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.7", ANSWER, False)

# --------------------------------------------------------------------------
# Section 3. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (3 points)
#
# Create a function that returns the list passed as argument sorted in
# numerical and ascending order. Also multiply all values with 10.
#
# Use the list:
#
# > [98, 5, 12, 369, 1]
#
# and the built-in method `sort()`.
#
# Answer with the sorted list.
#
# Write your code below and put the answer into the variable ANSWER.
#





ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (3 points)
#
# Create a function that takes the list:
#
# > [123, 4, 125, 69, 155]
#
# as argument.
#
# The function should multiply all even numbers by 2 and add 5 to all odd
# numbers.
#
# Answer with the modified list sorted in numerical order, descending.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, False)


dbwebb.exit_with_summary()
