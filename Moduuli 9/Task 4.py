"""
Nyt ohjelmoidaan autokilpailu.
Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä.
Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa.
Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
Tämä tehdään kutsumalla kiihdytä-metodia.
Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.
"""
import math
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
                while self.current_speed > 0 and v != 0:
                    self.current_speed = self.current_speed - 1
                    v = v + 1

    def drive(self, time_h):
        self.dist = self.dist + self.current_speed * time_h

    pass

#___________ correct numbers input____________
def input_speed():
    numbers = ["1","2","3","4","5","6","7","8","9","0"]
    while True:
        mistake = False
        v = input("Anna huippunopeuksen (100 km/h ... 200 km/h):")
        for symbol in v:
            if symbol not in numbers:
                mistake = True

        if not mistake:
            v = float(v)
            if v >= 100 and v <= 200:
                print("ok")
                return v
            else:
                print("Virheellinen syöte...")
        else:
            print("Virheellinen syöte...")



#_______________main___________________________

cars = []
for i in range(10):
    cars.append(auto("ABC-" + str(i+1), random.randint(100,200)))

for car in cars:
    print(car.reg_number, car.max_speed)

#___________kilpailu_____________

kilpailu = True
while kilpailu:
    for car in cars:
        car.change_speed(random.randint(-10,15))
        car.drive(1)
        if car.dist >= 10000:
            kilpailu = False


print ("{:<20} {:<15} {:<20} {:<8}".format('REKISTERINUMERO','HUIPPUNOPEUS','VIIMEINEN NOPEUS','MATKA'))
for car in cars:
   print ("{:<20} {:<15} {:<20} {:<8}".format(car.reg_number, car.max_speed, car.current_speed, car.dist))


