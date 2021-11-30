import random

list =[]
szamlalo = 0
darab = 0
while szamlalo<=5:
    szam= random.randint(1,10)
    list.append(szam)
    if szam % 2 == 0:
        darab = darab + 1
print(" A számok száma: ", darab)
print("A lista elemei: ", list)
