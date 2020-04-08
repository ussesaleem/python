"""
Programmet skriver ut en hälsning till Jack Black
"""

year = 2019

name = input("Skriv ett namn, klicka sedan enter: ") # Ber användaren mata in sitt namn
age = input("Skriv en ålder, klicka sedan enter: ") # Ber användaren mata in sin ålder

year_born = str(year - int(age))

greeting = "Hej " + name + ", du är " + age + " år gammal och föddes år " + year_born + " . " # Sätter ihop alla delar
print(greeting) # Skriver ut ett sträng värde
