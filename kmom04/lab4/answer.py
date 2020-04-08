#!/usr/bin/env python3

"""
773b4ec3e9056a6b5f94342e59daee85
python
lab4
v3
ussa19
2019-10-07 20:25:47
v4.0.0 (2019-03-05)

Generated 2019-10-07 22:25:47 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""
import physics
from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 4 - python
#
# In this lab we take another look at functions and we use modules to
# structure our code.
#



# --------------------------------------------------------------------------
# Section 1. Functions
#
#
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a function `valid_password` that takes one string argument. Check
# whether the argument is a valid password according to the following rules:
#
# * 8 characters or longer
# * Contains upper and lowercase letters
# * Contains a number
#
# The function should return True or False depending on whether the password
# is valid.
#
# Answer with the return value of the function when called with the string
# 'mYsecretpassword'.
#
# Tip: Use built-in character functions `isupper()`, `islower()`,
# `isdigit()`.
#
# Write your code below and put the answer into the variable ANSWER.
#

def valid_password(password):
    """
    This functions test the password according to criterias.
    """
    val = True

    if len(password) < 8:
        val = False
        return val

    if not any(char.isdigit() for char in password):
        val = False
        return val

    if not any(char.isupper() for char in password):
        val = False
        return val

    if not any(char.islower() for char in password):
        val = False
        return val

    if val:
        return val


ANSWER = valid_password("mYsecretpassword")

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Using the function `valid_password` answer with the return value of the
# function when called with the string 'mYsecretPASSW0rd'.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER = valid_password("mYsecretPASSW0rd")

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Create a function `number_of_vowels` that takes one argument. The function
# returns the number of vowels (vokaler) in the given argument. The following
# letters is used as vowels in this exercise: aeiouy
#
# Answer with the number of vowels in the following text:
#
# 'Stoicism has just a few central teachings. It sets out to remind us of how
# unpredictable the world can be.'
#
# Write your code below and put the answer into the variable ANSWER.
#

def number_of_vowels(find_vowels):
    """
    The function calculates how many vowels there are in the inserted string.
    """
    v = ["a", "e", "i", "o", "u", "y"]
    new_vowels = find_vowels.lower()
    vowels = ""
    for x in new_vowels:
        if x in v:
            vowels += x
    return len(vowels)

test = "Stoicism has just a few central teachings. It sets out to remind us of how unpredictable the world can be."


ANSWER = number_of_vowels(test)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Create a function `analyze_password` that uses `valid_password` and
# `number_of_vowels`. The function should return whether or not a password is
# valid and how many vowels the given password contains concatenated to a
# string.
#
# Example: With the input value Se3ret the function should return the
# following string: 'Se3ret is not a valid password and contains 2 vowels.'.
#
# With the input value mYsecretPASSW0rd the function should return the
# following string: 'mYsecretPASSW0rd is a valid password and contains 4
# vowels.'.
#
# Answer with the return value of the function `analyze_password` called with
# the following argument: Se3ret.
#
# Write your code below and put the answer into the variable ANSWER.
#

def analyze_password(password):
    """
    Testing the inserted password according to the rules in valid_password.
    """
    vowels = number_of_vowels(password)
    if valid_password(password) is True:
        result = password + " is a valid password and contains " + str(vowels) + " vowels."
    else:
        result = password + " is not a valid password and contains " + str(vowels) + " vowels."
    return result



ANSWER = analyze_password("Se3ret")

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Modules
#
# In this section we will look into modules and how we can structure our
# code.
#
# Tip: For all exercises if you are asked to round the result do it outside
# the functions.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Create a new Python file called `physics.py`. Import your new file/module
# in `answer.py` using the import statement: `import physics`
#
# In your physics module create a function `free_fall` that calculates the
# speed after a free fall without air resistance. The function takes two
# arguments time and initial speed. The inital speed argument should have a
# default value of 0 and it should be possible to call the function only with
# a time argument.
#
# Tip: the formula for calculating the speed of a free fall without air
# resistance is:
#
#     speed = initial speed + g * time, where g = 9.82
#
# Answer with a call to the function with time = 7. Round your answer to two
# decimals outside your function.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER = round(physics.free_fall(7), 2)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Modify your defined function `free_fall` to take another argument `gravity`
# with a default value of 9.82.
#
# Answer with a call to the function with time = 5, an initial speed of 4 and
# a gravity value of 1.62 (gravity on the moon). Round your answer to two
# decimals.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER = round(physics.free_fall(5, 4, 1.62), 2)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (2 points)
#
# Kinetic energy describes the energy of an object with a certain mass (m)
# and velocity (v).
#
# Create a function `kinetic_energy` that calculates the amount of kinetic
# energy of an object.
#
# The formula for calculating kinetic energy is:
#
#     energy = 0.5 * m * v².
#
# Use your defined function `free_fall` in combination with `kinetic_energy`
# to calculate the kinetic energy of an object with m = 10 after a free fall
# of time = 8 with the default gravity of earth (9.82).
#
# Round the answer to one decimal outside of the functions.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER = round(physics.kinetic_energy(10, 8), 1)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.4 (2 points)
#
# Potential energy is the energy stored in an object by virtue of the objects
# position in a gravitational field. The higher an object is lifted the
# greater the potential energy.
#
# The formula for calculating the potential energy is:
#
#     energy = m * g * h
#
# with m being the mass of the object, g the gravity and h the height of the
# object.
#
# When an object falls, all of the potential energy is converted into kinetic
# energy. So it is possible to calculate the height of the fall based on the
# amount of kinetic energy an object has at the end of the fall using the
# following formula:
#
#     height = kinetic_energy / (m * g)
#
# Create a function `height` that calculates the height of a free fall of
# time = 8 for an object with m = 10 and g = 9.82. Use your already defined
# functions `free_fall` to calculate the velocity and `kinetic_energy` the
# kinetic energy.
#
# Round the answer to one decimal outside the functions.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER = round(physics.height(10, 8), 1)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.4", ANSWER, True)

# --------------------------------------------------------------------------
# Section 3. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (3 points)
#
# Whether a certain year is a leap year depends on a few different rules.
# There is a leap year every year whose number is perfectly divisible by four
# - except for years which are both divisible by 100 and not divisible by
# 400. The second part of the rule effects century years. For example; the
# century years 1600 and 2000 are leap years, but the century years 1700,
# 1800, and 1900 are not.
#
# Create a function `leap_year` that checks whether a certain year is a leap
# year. The function should take one argument.
#
# Then create another function `leap_decider` that takes two arguments:
# `start_year` and `end_year`. The return value from the function should be a
# string containing the years and whether the years are leap years.
#
# Example: With the arguments `start_year`: 1999 and `end_year`: 2005, the
# string would be:
#
# 1999 is not a leap year, 2000 is a leap year, 2001 is not a leap year, 2002
# is not a leap year, 2003 is not a leap year, 2004 is a leap year, 2005 is
# not a leap year
#
# Answer with a call to `leap_decider` with the following arguments 1998 and
# 2004.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (3 points)
#
# Create a function `multiplication_table` that returns a multiplication
# table from 1 up to the argument given. As 4 * 3 = 3 * 4 you only need to
# return half of the multiplication table.
#
# Example: With the argument being 3 the returned multiplication table should
# be:
#
# 1
#
# 2 4
#
# 3 6 9
#
# Which is equal to the string '1\n2 4\n3 6 9\n'
#
#
# Answer with a call to the function with the argument 10.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, False)


dbwebb.exit_with_summary()
