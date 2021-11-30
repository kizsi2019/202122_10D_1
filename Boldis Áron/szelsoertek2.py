lista = []
for i in range(3):
    szo = input("Adj meg egy szót! ")
    lista.append(szo)
print(lista)

for i in lista:
    min = len(lista[0])
    max = len(lista[0])
for i in lista:
    if len(lista[i]) < min:
        min = len(lista[i])
    if len(lista[i]) > max:
        max = len(lista[i])

print("A legrövidebb szó hossza: ", min)
print("A leghoszabb szó hossza: ",  max)