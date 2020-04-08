#!/usr/bin/env python3

"""
a95b45ebd9ab9ffd1ec2ed1b2d660571
python
lab1
v3
ussa19
2019-09-07 17:04:53
v4.0.0 (2019-03-05)

Generated 2019-09-07 19:50:42 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 1 - python
#
# If you need to peek at examples or just want to know more, take a look at
# the [Python manual](https://docs.python.org/3/library/index.html).
#
# There you will find everything this lab will go through and much more.
#



# --------------------------------------------------------------------------
# Section 1. Integers, floats and basic arithmetics
#
# The foundation of numbers and basic arithmetic.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a variable called `num_one` and give it the value 62.
#
# Answer with the value of `num_one`.
#
# Write your code below and put the answer into the variable ANSWER.
#
num_one = 62





ANSWER = num_one

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Create another variable called `num_two` and give it the value 54. Create a
# third variable called `result` and assign to it the sum of the first two
# variables.
#
# Answer with the `result` variable.
#
# Write your code below and put the answer into the variable ANSWER.
#

num_two = 54

result_one = num_one + num_two


ANSWER = result_one

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Create a variable called `num_three` and give it the value 90.
#
# Create another variable called `num_four` and give it the value 24.
#
# Subtract `num_three` from `num_four` and add the `result` variable from
# above to result of the subtraction. Answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#

num_three = 90

num_four = 24

result_two = num_four - num_three + result_one



ANSWER = result_two

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Answer with the result of a multiplication of `num_one` and `num_three`.
#
# Write your code below and put the answer into the variable ANSWER.
#

result_three = num_one * num_three




ANSWER = result_three

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Create a variable called `float_one` and give it the value 91.22.
#
# Create another variable called `float_two` and give it the value 29.18.
#
# Sum the two values and answer with the result, rounded to two decimals. Use
# the function `round()` to round the number to two decimals.
#
# Write your code below and put the answer into the variable ANSWER.
#

float_one = 91.22

float_two = 29.18

result_four = float_one + float_two


ANSWER = round(result_four, 2)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (1 points)
#
# All variables used in the exercise below are defined above.
#
# Sum `num_three` with `num_one` and subtract `num_four`. Multiply the result
# by `num_two`, add `float_two` and subtract `float_one`. Use the function
# `round()` to round the number to two decimals.
#
# Answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#

result_five = num_three + num_one - num_four

result_six = result_five * num_two + float_two - float_one



ANSWER = round(result_six, 2)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Strings and concatenation
#
#
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Concatenate (svenska: konkatenera) the two words 'screen' and 'water' and
# answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#

word_one = "screen"

word_two = "water"


concated_result_one = word_one + word_two



ANSWER = concated_result_one

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Concatenate the word 'water' with the integer 62, with a space between the
# two values.
# Answer with the new string.
#
# Write your code below and put the answer into the variable ANSWER.
#

word_two = "water"

value_one = 62


concated_result_two = word_two + " " + str(value_one)


ANSWER = concated_result_two

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# Concatenate the integer 62 with the word 'screen' with a space between. To
# the resulting string concatenate the string ' and '. To this string
# concatenate integer 54 and the word 'water' with a space between between
# the two variables.
#
# Write your code below and put the answer into the variable ANSWER.
#

value_one = 62

word_three = "screen"

concated_result_three = str(value_one) + " " + word_three

concated_result_four = concated_result_three + " and "

value_two = 54

word_two = "water"

concated_result_five = str(value_two) + " " + word_two

concated_result_six = concated_result_four + concated_result_five


ANSWER = concated_result_six

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.4 (1 points)
#
# Assign the string value '30' to a variable called `string_number` and
# assign the integer value 5 to a variable called `actual_number`.
#
# Use `int()` to change the type of `string_number` to an integer and divide
# the integer value with `actual_number`. Answer with an integer by using the
# function `round()`.
#
# Write your code below and put the answer into the variable ANSWER.
#

string_number = str(30)

actual_number = 5

result = int(string_number)/actual_number



ANSWER = round(result)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.4", ANSWER, False)

# --------------------------------------------------------------------------
# Section 3. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (3 points)
#
# BTH is using a wind-turbine and solar panels to harvest energy from the
# wind and sun. On a windy and sunny day in September the sun shines for 10
# hours with an average output effect of the solar panels of 9345 W. The wind
# turbine has an average output effect of 314 W per hour for all 24 hours of
# the day.
#
# Calculate the total output energy i kWh from the wind turbine and the solar
# panels for the entire day.
#
# Energy i kWh is calculated as `energy = effect * hours / 1000`.
#
# Write your code below and put the answer into the variable ANSWER.
#

hours_solar = 10

effect_solar = 9345

energy_solar = effect_solar * hours_solar / 1000

hours_wind = 24

effect_wind = 314

energy_wind = effect_wind * hours_wind / 1000

energy_total = energy_solar + energy_wind




ANSWER = energy_total

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (3 points)
#
# Peter has the phonenumber '0731415926' and Anna has the phonenumber
# '0727182818'. They call each other every sunday afternoon for 9 minutes.
#
# Calculate the number of hours that they talk with each other pr year
# (assume 52 sundays pr year). Use that number in a string concatenation with
# the following format:
#
# 'Peter calls from [#Peter's phonenumber] to Anna on [#Anna's phonenumber]
# for [#hours] hours every year.'
#
# Replace the content inside [#] with the corresponding values.
#
# Answer with the concatenated string.
#
# Write your code below and put the answer into the variable ANSWER.
#

name_one = "Peter"

name_two = "Anna"

p_number = str("0731415926")

a_number = str("0727182818")

call_length = 9

number_calls = 52

total_length = call_length * number_calls

hours = total_length / 60


ANSWER = "Peter calls from " + p_number + " to Anna on " + a_number + " for " + str(hours) + " hours every year."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, False)


dbwebb.exit_with_summary()
