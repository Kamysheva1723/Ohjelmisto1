"""
Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina.
Polttomoottoriauton ominaisuutena on bensatankin koko litroina.
Kirjoita aliluokille alustajat.
Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden
ja akkukapasiteetin. Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi
sekä asettaa oman kapasiteettinsa. Kirjoita pääohjelma, jossa luot yhden sähköauton
(ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l).
Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan kolmen tunnin verran
ja tulosta autojen matkamittarilukemat.
"""
import random
class Auto:

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

class E_car(Auto):

    def __init__(self, reg_number, max_speed, battery):
        Auto.__init__(self,reg_number,max_speed)
        self.battery = battery

    pass


class F_car(Auto):

    def __init__(self, reg_number, max_speed, tank):
        Auto.__init__(self, reg_number, max_speed)
        self.tank = tank

    pass

#(ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l).

my_ecar = E_car("ABC-15", 180, 52.5)
my_fcar = F_car("ACD-123", 165, 32.3)

my_ecar.change_speed(65)
my_ecar.drive(3)
print(f"Sähköauto ajaa {my_ecar.dist} km.")

my_fcar.change_speed(101)
my_fcar.drive(3)
print(f"Polttomoottoriauto ajaa {my_fcar.dist} km.")