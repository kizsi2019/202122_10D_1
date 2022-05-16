szam = int(input('Adj meg egy számot -5 és 5 között! '))
összeg = 0
lista = []
while -5 >= szam <= 5:
    összeg = összeg + szam
    list.append(szam)
    szam = int(input("Adj meg egy számot -5 és 5 között! "))
print(lista)
print("Összeg: ", összeg)

