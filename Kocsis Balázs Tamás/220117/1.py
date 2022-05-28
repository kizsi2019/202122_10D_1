list = []

for i in range(3):
    szam = int(input("Adj meg egy számot! "))
    list.append(szam)

min = list[0]

for szam in list:
    if szam < min:
        min = szam
    
print(min)