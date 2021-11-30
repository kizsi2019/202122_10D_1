lista = []
for i in range(10):
    szó = input('Adj egy szót. ')
    lista.append(szó)
print(lista)
min = len(lista[0])
max = len(lista[0])
for i in lista:
    if len(lista[0]) < len(min):
        min = len(lista[0])
    if len(lista[0]) > max:
        max = len(lista[0])
print('A legrövidebb szó', min)
print('A leghoszabb szó', max)