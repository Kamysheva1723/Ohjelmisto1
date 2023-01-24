"""
Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
(käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä
kuin ne syötettiin. käytä for-toistorakennetta nimien kysymiseen
ja for/in toistorakennetta niiden läpikäymiseen.
"""
Kaupungit = []

for i in range (0,5):
    Kaupungit.append (input (f"Anna {i+1}. kaupungin nimi: "))


for k in Kaupungit:
    print (f"{Kaupungit.index(k)+1}. kaupunki oli {k}.")


