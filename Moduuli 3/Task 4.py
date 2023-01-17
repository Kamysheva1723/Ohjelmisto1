"""
Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.
Vuosi on karkausvuosi, jos se on jaollinen neljällä.
Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.
"""

Vuosi = int(input("Anna vuosi: "))

if Vuosi % 100 == 0:
    if Vuosi % 400 == 0:
        print(f"{Vuosi} on karkausvuosi.")
    else:
        print(f"{Vuosi} ei ole karkavuosi.")
elif Vuosi % 4 == 0:
    print(f"{Vuosi} on karkausvuosi.")
else:
    print(f"{Vuosi} ei ole karkavuosi.")

