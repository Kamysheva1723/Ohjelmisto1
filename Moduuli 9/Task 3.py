"""
Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa
tuntimäärässä edennyt. Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km.
Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.
"""

class auto:

    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.dist = 0

    def change_speed (self, v):
    # v/abs(v) määrittää onko v positiivisen (sitten se on 1) tai negativiisen (sitten se on -1)
        if v!=0:
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

my_auto = auto ("ABC-123", 142)
print(f"Luodun auton ominaisuudet:")
print(f"rekisteritunnus - {my_auto.reg_number},")
print(f"huippunopeus - {my_auto.max_speed} km/h,")
print(f"tämänhetkinen nopeus - {my_auto.current_speed} km/h,")
print(f"kuljettu matka - {my_auto.dist} km.")

my_auto.change_speed(100)
my_auto.drive(20)
print(f"kuljettu matka - {my_auto.dist} km.")

my_auto.change_speed(-40)
my_auto.drive(1.5)
print(f"kuljettu matka - {my_auto.dist} km.")