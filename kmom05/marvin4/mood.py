"""
The file contains the code for randomly picking quotes upon asking Marvin for citations.
"""
import random
import datetime

def the_mood():
    """
    Prints a string with randomised insertions.
    """
    filename = open("mood.txt")
    line = filename.readline()

    moods = ["happy", "sad", "depressed", "angry", "annoyed", "bored", "confused", "excited", "lonely"]
    mood = random.choice(moods)

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    number = random.choice(numbers)

    float_numbers = [1.924, 2.887, 3.564, 4.237, 5.476, 6.187, 7.934, 8.782, 9.123, 10.680]
    float_number = random.choice(float_numbers)

    date_and_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("\n" + line.format(date_and_time=date_and_time, mood=mood, number=number, float_number=float_number))
