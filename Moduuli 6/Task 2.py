"""
Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan
nopan maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.
"""
import random

def Noppa(Tahko_määrä):
    return random.randint(1,Tahko_määrä)

Tahko_määrä = int(input("Anna nopan tahkojen lukumäärä: "))

Count = 1

while Noppa(Tahko_määrä) != Tahko_määrä:
    Count += 1

print(f"{Count}. heiton jälkeen saadun {Tahko_määrä}.")