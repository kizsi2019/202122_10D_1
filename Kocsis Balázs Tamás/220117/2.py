list = []

for i in range(3):
    szam = int(input("Adj meg egy számot! "))
    list.append(szam)

max = list[0]

for szam in list:
    if szam < max:
        max = szam
    
print(max)