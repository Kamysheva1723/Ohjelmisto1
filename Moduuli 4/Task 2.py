"""
Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa
negatiivisen tuumamäärän.
Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm
"""
Pituus = float(input("Anna tuumamäärää: "))
while Pituus >= 0:
        print (f"{Pituus} tuumää yhtä suuri kuin {Pituus * 2.54:.2f} cm.")
        Pituus = float(input("Anna tuumamäärää: "))

print ("Annoit negatiivisen arvon. Ohjelman loppu.")