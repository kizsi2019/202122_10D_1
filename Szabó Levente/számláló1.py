import random
lista = []
számláló = 0
darab = 0
while számláló <= 5:
    szám = random.randint(1,10)
    list.append(szám)
    if szám % 2 == 0:
        darab = darab + 1
        számláló = számláló + 1
print('A páros számok száma:', darab)
print('A lista elemei:', lista)