"""
Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
Kone arvuuttelee lukua pelaajalta siihen asti,
kunnes tämä arvaa oikein.
Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus,
Liian pieni arvaus tai Oikein.
Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.
"""

import random

Number = random.randint(1,10)
Arvo = Number + 1

while Arvo != Number:
    Arvo = int(input("Mikä numero tuli? "))
    if Arvo > Number:
        print ("Liian suuri arvaus.")
    elif Arvo < Number:
        print ("Liian pieni arvaus.")

print ("Oikein!")