"""
Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan.
Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä.
Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä.
Hissien lista tallennetaan talon ominaisuutena.
Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen.
Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.
"""

class lift:
    def __init__(self, min_floor, max_floor):
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.current_floor = min_floor
        return

    def floor_up(self):
        if self.current_floor < self.max_floor:
            self.current_floor += 1
        return self.current_floor

    def floor_down(self):
        if self.current_floor > self.min_floor:
            self.current_floor -= 1
        return self.current_floor

    # it returns False if not succes.
    def to_floor(self, floor):
        if floor >= self.min_floor and floor <= self.max_floor:
            while self.current_floor != floor:
                if floor > self.current_floor:
                    self.floor_up()
                else:
                    self.floor_down()
            return True
        else:
            return False

    pass

class building:
    lifts = []
    def __init__(self, min_floor, max_floor, lifts_number):
        self.lifts_numbers = lifts_number
        for i in range(lifts_number):
            self.lifts.append(lift(min_floor, max_floor))
        return

    pass

    def take_lift(self, lift_number, to_floor):
        return self.lifts[lift_number-1].to_floor(to_floor)


#_____main____

building = building(2,12,4)

print (building.take_lift(1,1))  # too low
print (building.take_lift(2,5))  # ok
print (building.take_lift(3,14)) # too high
print (building.take_lift(4,10)) # ok
print (building.take_lift(3,7))  # down

n=1

for lift in building.lifts:
    print(f"Elevator {n}. - {lift.current_floor}. krs.")
    n += 1




