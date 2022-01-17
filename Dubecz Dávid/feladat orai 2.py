szam_lista = []

for i in range(3):
    szambekeres = int(input("Adj meg egy számot! "))
    szam_lista.append(szambekeres)

max = szam_lista[0]

for szam in szam_lista:
    if szam > max:
        max = szam

print("A legnagyobb szám:", max)