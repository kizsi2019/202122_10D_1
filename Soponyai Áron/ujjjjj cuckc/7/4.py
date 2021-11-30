lista = []
for i in range(3):
    szo = input("Adj meg egy szabat!")
    lista.append(szo)
print(lista)
min = lista[0]
max = lista[0]
for i in lista:
    if len(lista[i]) < min:
        min = lista[i]
    if len(lista[i]) < min:
        max = lista[i]
print("Legrövidebb" ,min)
print("leghosszabb" ,max)
