"""
Kirjoita while-toistorakennetta käyttävä ohjelma, joka tulostaa kolmella jaolliset luvut väliltä 1..1000.
"""
import random

number = 1
while number <= 3:
    Variable = random.randint(1,1000)
    if Variable % 3 == 0:
        print (f"Variable_{number} is {Variable:3d}.")
        number += 1

print ("The end.")