lista = []

for i in range(3):
    bekeres = int(input("Adj meg egy egész számot: "))
    lista.append(bekeres)

if (lista[0] + lista[1]) == lista[2]:
    print("Az első két szám összege egyenlő a harmadik számmal.")
else:
    print("Az első két szám összege nem egyenlő a harmadik számmal.")