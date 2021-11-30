import random
from typing import List 

lista =[]
szamlalo = 0
darab=0
while szamlalo<5:
    szam=random.randint(1,10)
    list.append(szam)
    if szam % 2 == 0:
    szamlalo =szamlalo + 1
        darab=darab+1
print('A páros számok száma: ',darab)
print('A lista elemei', list)
