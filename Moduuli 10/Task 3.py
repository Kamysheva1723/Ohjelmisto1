"""
Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys,
joka käskee kaikki hissit pohjakerrokseen. Jatka pääohjelmaa siten, että talossasi tulee palohälytys.
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

    def fire(self):
        for lift in self.lifts:
            lift.to_floor(lift.min_floor)
        return


#_____main____

building = building(-2,12,4)

print (building.take_lift(1,-3))  # too low
print (building.take_lift(2,5))  # ok
print (building.take_lift(3,14)) # too high
print (building.take_lift(4,10)) # ok
print (building.take_lift(3,-2))  # down

n=1

for lift in building.lifts:
    print(f"Elevator {n}. - {lift.current_floor}. krs.")
    n += 1

building.fire()
print("Fire...")

for lift in building.lifts:
    print(f"Elevator {n}. - {lift.current_floor}. krs.")
    n += 1


