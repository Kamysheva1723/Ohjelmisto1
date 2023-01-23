"""
Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.

Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten,
että jako menee tasan. Toisaalta esimerkiksi luku 21 ei ole alkuluku,
koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.
"""

N = int(input("Anna kokonaisluku: "))

if N % 2 != 0:
    Step = 2
    d = 3
else:
    Step = 1
    d = 2

while d * d <= N and N % d != 0:
    d += Step

# print (f"N = {N}, d = {d}, Step = {Step}, Counter = {Counter}")


if  N == 1:
    print("1 ei ole alkuluku.")
elif d * d > N:
    print(f"Sinun luku {N} on alkuluku.")
else:
    print(f"Sinun luku {N} ei ole alkuluku. Luku {d} on sen jakaja.")
