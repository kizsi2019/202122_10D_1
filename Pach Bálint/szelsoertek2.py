lista = []
for i in range(10):
    szo = input('Adj meg egy szót!')
    lista.append(szo)
print(lista)
min = lista[0]
max = lista[0]
for i in lista:
    if len(lista[i]) < min:
        min = len 