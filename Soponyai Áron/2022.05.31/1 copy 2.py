szám1 = input("Adj meg egy számot")
szám2 = input("Adj meg még egy számot")
szám1j = len(szám1)
szám2j = len(szám2)

if szám1 > szám2:
    print(szám1, "a nagyobbik szám")
elif szám1j < szám2j:
    print(szám2, "a nagyobbik szám")
else:
    print("Egyenlő a két szám")