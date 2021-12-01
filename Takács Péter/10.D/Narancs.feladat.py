from random import randint

szamlalo = 0
i = 0
while i < 20:
    ertek2 = randint(1,12)
    if ertek2 % 3 == 0:
        print(ertek2)
        szamlalo += 1
    i += 1
print("3-al oszthato szám ", szamlalo, " db volt.")