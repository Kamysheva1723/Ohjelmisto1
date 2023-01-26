"""
Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan
silmäluvun väliltä 1..6. Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.
"""

import random
def Noppa():
    return random.randint(1,6)

Count = 1

while Noppa() != 6:
    Count += 1

print(f"{Count}. heiton jälkeen saadun 6.")



