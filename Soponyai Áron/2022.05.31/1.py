szám1 = input("Adj meg egy számot")
szám2 = input("Adj meg még egy számot")
szám1 = int(szám1)
szám2 = int(szám2)

if szám1 > szám2:
    print(szám1, "a nagyobbik szám")
elif szám1 < szám2:
    print(szám2, "a nagyobbik szám")
else:
    print("Egyenlő a két szám")