import random
lista = []
szamlalo = 0
db=0
while szamlalo < 5:
    szam = random.randint(1,10)
    lista.append(szam)
    if szam % 2 == 0:
        db = db + 1
    szamlalo = szamlalo + 1
print("A práos számok száma:", db)
print("A lista elemei:", lista)
    