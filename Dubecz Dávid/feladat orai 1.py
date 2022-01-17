szam_lista = []

for i in range(3):
    szambekeres = int(input("Adj meg egy számot! "))
    szam_lista.append(szambekeres)

min = szam_lista[0]

for szam in szam_lista:
    if szam < min:
        min = szam

print("A legkisebb szám a három közül:", min)