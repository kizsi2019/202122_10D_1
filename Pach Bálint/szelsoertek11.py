lista = []
for i in range(10):
    szam = int(input("Adj meg egy számot!"))
    lista.append(szam)
min = lista[0]
max = lista[0]
for i in lista:
    if i < min:
        min = 1
    if i > max:
        max = 1
print(lista)
print ("Legkisebb: ", min)
print ("Legnagyobb: ", max)