lista = []

for i in range(3):
    bekeres = int(input("Adj meg egy egész számot: "))
    lista.append(bekeres)

if lista[0] % 2 == 0 and lista[1] % 2 == 0 and lista[2] % 2 == 0:
    print("Mind a három szám páros.")
else:
    print("Mind a három szám nem páros.")