"""
Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille
argumentiksi reverse=True.
"""
Values = []
IndexMax = 0

UserValue = input("Anna luku: ")

while UserValue != "":
      Values.append(float(UserValue))
      UserValue = input("Anna luku: ")
      IndexMax += 1

Values.sort(reverse=True)

for i in range(0,min(IndexMax,5)):
    print(Values[i])

print("The end.")



