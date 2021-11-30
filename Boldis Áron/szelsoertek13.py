szamok = []
szamok2 = []

for i in range(5):
    szam = input("Adj meg egy számot! ")
    szamok.append(szam)

for i in szamok:
    if i % 2 == 0:
        szamok2.append(i)

min = szamok[0]
max = szamok[0]
for i in szamok2:
    if  i < min:
        min = i
    if i > max:
        max = i

print("Legkisebb: ", min)
print("Legnagyobb:", max)

