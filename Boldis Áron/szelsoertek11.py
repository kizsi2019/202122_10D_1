szamok = []

for i in range(10):
    szam = input("Adj meg egy számot! ")
    szamok.append(szam)
min = szamok[0]
max = szamok[0]
for i in szamok:
    if  i < min:
        min = i
    if i > max:
        max = i

print("Legkisebb: ", min)
print("Legnagyobb:", max)

