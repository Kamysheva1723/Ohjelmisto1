"""
Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin parametrina saatu lista paitsi
että siitä on karsittu pois kaikki parittomat luvut.
Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja
tulostat sen jälkeen sekä alkuperäisen että karsitun listan.
"""
def del_odd(list):
    new_list = []
    for x in list:
        if x % 2 == 0:
            new_list.append(x)
    return new_list

list = [1,2,3,4,5,6,7,8,9,0, 17, 7654, 890,77]

print(f"Alkuperäinen lista {list}")
print(f"Uusi lista {del_odd(list)}")
