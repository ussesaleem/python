"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""
import marvin
import inventory

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

    marvin.menu()

    choice = input("--> ")

    if choice == "q":
        print("Bye, bye - and welcome back anytime!")
        break

    elif choice == "1":
        marvin.greeter()

# [°F] = [°C] * 9 / 5 + 32
    elif choice == "2":
        marvin.celsius_converter()

    elif choice == "3":
        marvin.word_echo()

    elif choice == "4":
        marvin.sum_of_values()

    elif choice == "5":
        marvin.comparing_values()

    elif choice == "6":
        marvin.increasing_strings()

    elif choice == "7":
        marvin.isogram_check()

    elif choice == "8":
        marvin.toss_the_letters()

    elif choice == "9":
        marvin.anagram_check()

    elif choice == "10":
        marvin.create_acronym()

    elif choice == "11":
        marvin.string_masking()

    elif "inv" in choice:
        print("Inventory:\n" + inventory.readfile() + "\n")
        if choice == "inv":
            inventory.readfile()
        elif "inv pick " in choice:
            if choice.index("inv pick ") == 0:
                inventory.add(choice[9:])
                print("Item added to the inventory: " + choice[9:] + "\n")
                print("The inventory contains the following items:\n" + inventory.readfile())
            else:
                print("Not a valid inventory command!")
        elif "inv drop " in choice:
            if choice.index("inv drop ") == 0:
                inventory.remove_item(choice[9:])
                print("Item removed from the inventory: " + choice[9:] + "\n")
                print("The inventory contains the following items:\n" + inventory.readfile())
            else:
                print("Not a valid inventory command!")
        elif choice == "inv drop":
            inventory.remove_content()
            print("The inventory is now empty.")
        else:
            print("Not a valid inventory command!")

    else:
        print("That is not a valid choice. You can only choose from the menu.")

    input("\nPress enter to continue...")
