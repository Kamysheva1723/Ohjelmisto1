"""
Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan
leivisköinä, nauloina ja luoteina.
Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi
sekä ilmoittaa tuloksen käyttäjälle.

Yksi leiviskä on 20 naulaa.
Yksi naula on 32 luotia.
Yksi luoti on 13,3 grammaa.
"""

LeiviskäNumber = float(input("Anna leiviskät: "))
NaulaNumber = float(input("Anna naulat: "))
LuotiNumber = float(input("Anna luodit: "))

Massa = LuotiNumber*13.3 + NaulaNumber*32*13.3 + LeiviskäNumber*20*32*13.3

print(f"Massa nykymittojen mukaan: {int(Massa/1000.0)} kilogramma "
      f"ja {(Massa-int(Massa/1000.0)*1000.0):.2f} gramma.")