"""
Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden.
Ohjelma tulostaa suorakulmion piirin ja pinta-alan.
Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.
"""

A = float(input("Anna suorakulmion kanaan (m): "))
B = float(input("Anna suorakulmion korkeuden (m): "))

RectangleSquare = A*B
RectanglePerimetr = 2*(A+B)

print(f"Sen pinta-ala on {RectangleSquare:0.2f} neliömetriä ja sen piiri on {RectanglePerimetr:0.2f} metriä. ")
