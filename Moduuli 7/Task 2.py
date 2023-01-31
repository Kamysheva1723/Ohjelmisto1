"""
Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää
tyhjän merkkijonon. Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin
Uusi nimi tai Aiemmin syötetty nimi sen mukaan, syötettiinkö nimi ensimmäistä kertaa.
Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä.
Käytä joukkotietorakennetta nimien tallentamiseen.
"""
names = set()
name = input ("Anna nimi (Enter lopetaa): ")

while name != "":
    if name in names:
        print ("Aiemmin syötetty nimi.")
    else:
        print ("Uusi nimi.")
        names.add(name)
    name = input ("Anna nimi (Enter lopetaa): ")

for n in names:
    print (n)

