"""
Du har säkert suttit på ett flygplan och sett på skärmen hur högt planet flyger,
vilken hastighet det har, temperaturen utanför och hur långt det är till destinationen
och vad klockan är för tillfället.

Det är siffror som omväxlande visas i meter, km/h och Celsius och sedan växlar det
till feet, mph och Farenheit.

Du skall nu göra ett program som ber användaren mata in följande värden:
- Höjd över havet (meter)
- Hastighet (km/h)
- Temperatur utanför flygplanet (Celsius)

Sedan skall programmet skriva ut motsvarande värden enligt:
- Höjd över havet (feet)
- Hastighet (mph)
- Temperatur utanför flygplanet (Farenheit)

1 meter är 3.28084 feet.
1 kilometer är 0.62137 miles.

För att konvertera från Celcius till Farenheit används följande formel:
[°F] = [°C] * 9 / 5 + 32
"""


height_m = input("Insert height over sea (meter): ")
speed_kmh = input("Insert the speed (km/h): ")
temp_c = input("Insert temperature (Celsius): ")


feets = 3.28084
mphs = 0.62137

height_f = int(height_m) * feets
speed_mph = int(speed_kmh) * mphs
temp_f = int(temp_c) * 9 / 5 + 32


print("Height over sea: " + " " + str(height_f) + " " + "feet")
print("Speed: " + " " + str(speed_mph) + " " + "mph")
print("Temperature: " + " " + str(temp_f) + " " + "Fahrenheit")
