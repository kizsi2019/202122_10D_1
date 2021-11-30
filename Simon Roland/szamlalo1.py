import random     

list = []
darab = 0 
szamlalo = 0 
while szamlalo <= 5:
    szam = random.randint(1,10)
    list.append(szam)
for szam in lista:
    if szam % 2 == 0:
        darab = darab +1 
print('A listában ennyi páros szám van: ', darab)
print (list)
