"""
Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C)
ja tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti.
Tehtävässä on käytettävä if/elif/else-toistorakennetta.

LUX on parvekkeellinen hytti yläkannella.
A on ikkunallinen hytti autokannen yläpuolella.
B on ikkunaton hytti autokannen yläpuolella.
C on ikkunaton hytti autokannen alapuolella.
Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa Virheellinen hyttiluokka.
"""
HyttiLuokka = input("Anna hyttiluokan: ")
if HyttiLuokka == "A":
    print ("A on ikkunallinen hytti autokannen yläpuolella.")
elif HyttiLuokka == "B":
    print ("B on ikkunaton hytti autokannen yläpuolella.")
elif HyttiLuokka == "C":
    print ("C on ikkunaton hytti autokannen alapuolella.")
elif HyttiLuokka == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
else:
    print("Virheellinen hyttiluokka")
