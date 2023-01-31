"""
Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman,
hakea jo syötetyn lentoaseman tiedot vai lopettaa.
Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman
ICAO-koodin ja nimen. Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin
ja tulostaa sitä vastaavan lentoaseman nimen. Jos käyttäjä haluaa lopettaa,
ohjelman suoritus päättyy. Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa
aina siihen asti, kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste.
Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)
"""
def add():
    code = input ("Anna ICAO-koodi: ")
    name = input ("Anna lentoaseman nimi: ")
    Lentoasemat[code] = name
    return
def find():
    code = input("Anna ICAO-koodi löytääksesi lentokentä:")
    if code in Lentoasemat:
        print(f"ICAO-koodi on {code}, Lentoasmen nimi on {Lentoasemat[code]}")
    else:
        print("Lentoasema ei löydy.")
    return

Lentoasemat = dict()

desicion = int(input ("1 - syöttää uuden lentoaseman, "
                  "2 - hakea jo syötetyn lentoaseman tiedot,"
                  "3 - lopettaa."))

while desicion != 3:
    if desicion == 1:
        add()
    elif desicion == 2:
        find()
    desicion = int (input("1 - syöttää uuden lentoaseman, "
                     "2 - hakea jo syötetyn lentoaseman tiedot, "
                     "3 - lopettaa."))

print("The end.")