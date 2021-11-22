szam = int(input('Adj meg egy számot -5 és 5 közt! '))
összeg = 0
list = []
while -5 <= szam <= 5:
    list.append(szam)
    összeg = összeg + 1
szam = int(input('Add meg a következő számot -5 és 5 közt! '))
print(list)
print(összeg)