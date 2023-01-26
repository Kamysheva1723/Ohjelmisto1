"""
Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina
ja palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma, joka kysyy gallonamäärän
käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen.
Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
Yksi gallona on 3,785 litraa.
"""
def gal_litr(gal_number):
    return gal_number * 3.785

gal_number = float(input("Anna gallonmäärä: "))

while gal_number >= 0:
    print(f"{gal_number} gallonna on {gal_litr(gal_number)} litraa.")
    gal_number = float(input("Anna gallonmäärä: "))