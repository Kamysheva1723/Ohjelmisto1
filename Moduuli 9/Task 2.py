"""
Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi,
joka saa parametrinaan nopeuden muutoksen (km/h).
Jos nopeuden muutos on negatiivinen, auto hidastaa.
Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h
ja lopuksi +50 km/h. Tulosta tämän jälkeen auton nopeus.
Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus.
Kuljettua matkaa ei tarvitse vielä päivittää.
"""

import math

class auto:

    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.dist = 0

    def change_speed (self, v):
    # v/abs(v) määrittää onko v positiivisen (sitten se on 1) tai negativiisen (sitten se on -1)
        if v != 0:
             if v / abs(v) == 1: # jos nopeus kasvaa
                while self.current_speed < self.max_speed and v != 0:
                     self.current_speed = self.current_speed + 1
                     v = v - 1
             else:  # jos nopeus vähenee
                   while self.current_speed > 0 and v != 0:
                        self.current_speed = self.current_speed - 1
                        v = v + 1
    pass

my_auto = auto ("ABC-123", 142)
print(f"Luodun auton ominaisuudet:")
print(f"rekisteritunnus - {my_auto.reg_number},")
print(f"huippunopeus - {my_auto.max_speed} km/h,")
print(f"tämänhetkinen nopeus - {my_auto.current_speed} km/h,")
print(f"kuljettu matka - {my_auto.dist} km.")

my_auto.change_speed(30)
print(f"tämänhetkinen nopeus - {my_auto.current_speed} km/h,")
my_auto.change_speed(70)
print(f"tämänhetkinen nopeus - {my_auto.current_speed} km/h,")
my_auto.change_speed(50)
print(f"tämänhetkinen nopeus - {my_auto.current_speed} km/h,")

print(f"Luodun auton ominaisuudet muutoksen (+30, +70, +50) jälkeen:")
print(f"rekisteritunnus - {my_auto.reg_number},")
print(f"huippunopeus - {my_auto.max_speed} km/h,")
print(f"tämänhetkinen nopeus - {my_auto.current_speed} km/h,")
print(f"kuljettu matka - {my_auto.dist} km.")

my_auto.change_speed(-200)

print(f"Luodun auton ominaisuudet muutoksen (-200) jälkeen:")
print(f"rekisteritunnus - {my_auto.reg_number},")
print(f"huippunopeus - {my_auto.max_speed} km/h,")
print(f"tämänhetkinen nopeus - {my_auto.current_speed} km/h,")
print(f"kuljettu matka - {my_auto.dist} km.")