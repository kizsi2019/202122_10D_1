lista =[]
for i in range(2):
  szo = input('Asj meg egy szót! ')
  lista.append(szo)
print(lista)
min = lista[0]
max = lista[0]
for i in lista:
  if len(lista[i])< min:
    min = len(lista[i])
  if len(lista[i]) > max:
    max = len(lista[i])
print('A legrövidebb szó: ', min)
print('A leghosszabb szó: ', max)   