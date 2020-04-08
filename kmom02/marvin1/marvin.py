#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""

marvin_image = r"""
             '   .
              '  /   .
              ' /  .- .
              .  .- .-
            ./    .--...
  .-------- 0    .--
 /                 .......
'                  ..
 '........            ----
          .          --..
           .   .---..   -
           .  '     -.
          /   '
         / ' ' '
        '  ' '  '
        '  '  ' '
        '  '  ' '
        '   ' ' '
        '   '  '
         -..'.----------.
            I   ----------
     /////////.
"""

"""
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""
while True:
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(marvin_image)
    print("Hi, I'm Marvin. I know it all. What can I do you for?")
    print("1) What is your name?")
    print("2) Convert Celsius to Fahrenheit.")
    print("3) Word-echoeing.")
    print("4) Sum of values.")
    print("5) Comparing values.")
    print("6) Increasing strings.")
    print("7) Isogram check.")
    print("q) Quit.")

    choice = input("--> ")

    if choice == "q":
        print("Bye, bye - and welcome back anytime!")
        break

    elif choice == "1":
        name = input("What is your name? ")
        print("\nMarvin says:")
        print("Hello %s - your awesomeness!" % name)
        print("\nWhat can I do you for?!")

# [°F] = [°C] * 9 / 5 + 32
    elif choice == "2":
        temperature = input("Please insert temperature in Celsius and let me do my magic: ")
        if temperature.isdigit:
            fahrenhet = int(temperature) * 9 / 5 + 32
        print("\nMarvin says:")
        print("According to my calculations, %s Celsius is" % temperature, fahrenhet, "in Fahrenheit.")
        print("\nWhat can I do you for?!")

    elif choice == "3":
        word = input("Insert a word: ")
        number = input("Insert a number: ")
        print("\nMarvin says:")
        print("%s " % word * int(number))
        print("\nWhat can I do you for?!")

    elif choice == "4":
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

    elif choice == "5":
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

    elif choice == "6":
        word = str(input("Enter a word: "))
        new_word = ""
        for letter, value in enumerate(word, 1):
            new_word += letter * value + "-"
        new_word = new_word[:-1]
        print("\nMarvin says:")
        print(new_word)
        print("\nWhat can I do you for?!")

    elif choice == "7":
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

    else:
        print("That is not a valid choice. You can only choose from the menu.")

    input("\nPress enter to continue...")
