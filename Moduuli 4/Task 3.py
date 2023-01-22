"""
Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.
"""
Input = input("Anna lukusi: ")

if Input != "":
    Min = float(Input)
    Max = float(Input)

while Input != "":
    Input = input("Anna lukusi: ")
    if Input != "":
       if  Max < float (Input):
           Max = float (Input)
       elif Min > float (Input):
           Min = float (Input)

print(f"Syötetyistä numeroista surin oli numero {Max:.2f} ja pienin numero {Min:.2f}.")