"""
Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita Kilpailu-luokka,
jolla on ominaisuuksina kilpailun nimi, pituus kilometreinä ja osallistuvien autojen lista.
Luokassa on alustaja, joka saa parametreinaan nimen, kilometrimäärän ja autolistan ja asettaa
ne ominaisuuksille arvoiksi. Luokassa on seuraavat metodit:

    tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein
    tehtävät toimenpiteet eli arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle
    kulje-metodia.

    tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.

    kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään
    kilpailun kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False.

Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli".
Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa
tehtävässä. Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa
tunti_kuluu-metodia, jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla,
onko kilpailu ohi. Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla
kymmenen tunnin välein sekä kertaalleen sen jälkeen, kun kilpailu on päättynyt.
"""

import random
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
                while self.current_speed > 0 and v !=0:
                    self.current_speed = self.current_speed - 1
                    v = v + 1

    def drive(self, time_h):
        self.dist = self.dist + self.current_speed * time_h

    pass

class kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot
        return

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.change_speed(random.randint(-10, 15))
            auto.drive(1)
        return

    def tulosta_tilanne(self):
        print(f"{self.nimi}   {self.pituus} km")
        print("{:<20} {:<15} {:<20} {:<8}".format('REKISTERINUMERO', 'HUIPPUNOPEUS', 'VIIMEINEN NOPEUS', 'MATKA'))
        for auto in self.autot:
            print("{:<20} {:<15} {:<20} {:<8}".format(auto.reg_number, auto.max_speed, auto.current_speed, auto.dist))
        return

    def kilpailu_ohi(self):
        finish = False
        for auto in self.autot:
             if auto.dist >= self.pituus:
                 finish = True
        return finish

    pass

#________________main____________

autot = []
for i in range(10):
    autot.append(auto("ABC-" + str(i+1), random.randint(100,200)))

for auto in autot:
    print(auto.reg_number, auto.max_speed)

kilpailu = kilpailu("Suuri romuralli", 8000, autot)

time = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    time += 1
    if time % 10 == 0:
        print(f"{time} tunnin kilpailun jälkeen...")
        kilpailu.tulosta_tilanne()

print(f"Kilpailu ohi.")
kilpailu.tulosta_tilanne()
