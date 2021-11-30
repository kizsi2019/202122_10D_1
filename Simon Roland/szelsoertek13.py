lista = []
lista2 = []
for i in range(10):
    szam = int(input('Adj meg egy szamot '))
    lista.append(szam)
for i in lista: 
    if i % 2 == 0:
        lista2.append(i)    
min = lista2[0]
max = lista2[0]
for i in lista2:
    if i < min:
        min = i 
    if i > max: 
        max = i 
print(lista)
print("Legkisebb: ", min )
print('Legnagyobb: ', max )
