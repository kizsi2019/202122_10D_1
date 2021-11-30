lista = []
lista2 = []
for i in range(4):
    szam = int(input("adj meg eg számot"))
    lista.append(szam)
for i in lista:
    if i % 2 == 0:
        lista2.append(i)
min = lista[0]
max = lista[0]
for i in lista2:
    if i < min:
        min =i
    if i > max:
        max =i
print(lista2)
print("legkissseb", min)
print("legnyagyobb", max)