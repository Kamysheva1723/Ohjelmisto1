"""
Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
Ohjelma palauttaa listassa olevien lukujen summan.
Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat
sen palauttaman summan.
"""
def list_sum(list):
    sum = 0
    for n in list:
        sum += n
    return sum

numbers = [1,2,3,4,50,7,8]

print (f"Summa on {list_sum(numbers)}")
