"""
Kirjoita ohjelma, joka kysyy kolme kokonaislukua.
Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.
"""
x = int(input("Anna ensimainen kokonaisluku: "))
y = int(input("Anna toinen kokonaisluku: "))
z = int(input("Anna kolmas kokonaisluku: "))

print(f"Näiden lukujen summa on yhtä suuri kuin {x+y+z}, "
      f"niiden tulo on yhtä suuri kuin {x*y*z} "
      f"ja niiden keskiarvo on yhtä suuri kuin {((x+y+z)/3):.2f}.")