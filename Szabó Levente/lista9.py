import random
szamlista = []

for i in range(10):
    szam = random.randint(1,40)
    if szam % 3 == 0:
        szamlista.append(szam)
print(szamlista)
print('A lista', len(szamlista), 'elemből áll')
