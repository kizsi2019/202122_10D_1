import random
list =[]
talalat = False 
szam2 = int(input("Adj meg egy számot 1 és 7 között! "))
for i in range(5):
    szam = random.randint(1,7)
    list.append(szam)
print(list)

index = 0
while index < len(lista) and not talalat:
	if lista[index] == 'piros':
		talalat = True
	    index = index + 1

if talalat:
	 print('Van a listában piros szín, az indexe: ', index-1)
else:
    print('Nincs a listában piros szín.')