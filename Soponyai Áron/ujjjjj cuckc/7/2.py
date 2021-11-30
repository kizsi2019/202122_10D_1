from typing import List, Literal


lista = []
for i in range(10):
    szam = int(input("adj meg eg számot"))
    lista.append(szam)
min = lista[0]
max = lista[0]


for i in lista:
    if i < min:
        min =i
    if i > max:
        max =i

print(lista)
print("legkissseb", min)
print("legnyagyobb", max)