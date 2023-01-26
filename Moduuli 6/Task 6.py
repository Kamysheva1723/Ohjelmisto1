"""
Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä
sekä pizzan hinnan euroina. Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa,
kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.
"""
import math

def hinta_per_neliö(diametr,price):
    return price / (math.pi * ((diametr/2.0) ** 2) * (10 ** (-4)))

price1 = float(input("Anna ensimisen pizzan hinta: "))
diametr1 = float(input("Anna ensimaisen pizzan halkaisija: "))

price2 = float(input("Anna toisen pizzan hinta: "))
diametr2 = float(input("Anna toisen pizzan halkaisija: "))

if hinta_per_neliö(diametr1,price1) > hinta_per_neliö(diametr2,price2):
    print (f"Toinen pizza on halvempi, sen yksikköhinta on {hinta_per_neliö(diametr2,price2):.2f}")

elif hinta_per_neliö(diametr1,price1) < hinta_per_neliö(diametr2,price2):
    print(f"Ensimäinen pizza on halvempi, sen yksikköhinta on {hinta_per_neliö(diametr1, price1):.2f}")

else:
    print(f"Näillä pizzoilla on sama neliöhinta, ja se on {hinta_per_neliö(diametr2, price2):.2f}")
