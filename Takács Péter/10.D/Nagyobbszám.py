lista = []

szam1 = int(input("Adj egy számot! "))
lista.append(szam1)

szam2 = int(input("Adj egy számot! "))
lista.append(szam2)

for i in lista:
    if szam2 < szam1:
        print("Ez a szám nagyobb!", szam1)
    elif szam2 > szam1:
        print("Ez a szám nagyobb!", szam2)
    else:
        print("A két szám egyenlő!")