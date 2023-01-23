"""
Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
Käytä for-toistorakennetta.
"""

import random

Count = int (input("Kuinka monta noppaa heitämme?"))
Sum = 0

for i in range (0, Count):
    Sum += random.randint(1,6)

print (f"{Sum}")
