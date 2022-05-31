lista = []

szam1 = int(input("Adj meg egy számot! "))
lista.append(szam1)

szam2 = int(input("Adj meg egy másik számot! "))
lista.append(szam2)

for i in lista:
  if szam1 > szam2:
    print("A nagyobb szám: ", szam1)
  elif szam1 < szam2:
    print("A nagyobb szám: ", szam2)
  else:
    print("A két szám egyenlő")
