"""
Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron.
Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas.
Uusi hissi on aina alimmassa kerroksessa.
Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5),
metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa,
että hissi päätyy viidenteen kerrokseen. Viimeksi mainitut metodit ajavat hissiä
yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on.
Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen
ja sen jälkeen takaisin alimpaan kerrokseen.
"""
class Lift:
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

my_lift = Lift(2,18)
print (my_lift.current_floor)

my_lift.to_floor(7)
print (my_lift.current_floor)

my_lift.to_floor(9)
print (my_lift.current_floor)

my_lift.to_floor(20)
print (my_lift.current_floor)

my_lift.to_floor(15)
print (my_lift.current_floor)

my_lift.to_floor(0)
print (my_lift.current_floor)

my_lift.to_floor(2)
print (my_lift.current_floor)

