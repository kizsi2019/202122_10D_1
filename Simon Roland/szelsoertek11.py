lista = []
for i in range(10):
    szam = int(input('Adj meg egy szamot'))
    lista.append(szam)
min = lista[0]
max = lista[0]
for i in lista:
    if i < min:
        min = i 
    if i > max:
        max = i 
print(lista)
print("Legkisebb: ", min)
print('Legnagyobb: ', max )

