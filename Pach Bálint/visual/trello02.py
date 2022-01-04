import random
szamok = []
szamok2 = []
for i in range(2):
    szam = int(input("Adj meg egy számot!"))
    szamok.append(szam)
for i in szamok:
    if i %2 == 0:
        szamok2.append(i)
min = szamok2[0]
max = szamok2[0]
for i in szamok2:
    if i < min:
        min = 1 
    if i > max:
        max = 1
print(szamok)
print("Legkisebb: ", min)
print("Legnagyobb: ", max)
