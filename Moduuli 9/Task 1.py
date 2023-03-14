"""
Kirjoita Auto-luokka, jonka ominaisuuksina ovat
rekisteritunnus,
huippunopeus,
tämänhetkinen nopeus ja
kuljettu matka.
Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi ensin mainittua parametreina
saatuihin arvoihin. Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi.
Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h).
Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.
"""
class auto:

    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.dist = 0
    pass

my_auto = auto ("ABC-123", 142)
print(f"Luodun auton ominaisuudet:")
print(f"rekisteritunnus - {my_auto.reg_number},")
print(f"huippunopeus - {my_auto.max_speed} km/h,")
print(f"tämänhetkinen nopeus - {my_auto.current_speed} km/h,")
print(f"kuljettu matka - {my_auto.dist} km.")