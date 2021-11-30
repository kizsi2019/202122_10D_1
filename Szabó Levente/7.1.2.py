szám = int(input("Adj meg egy számot -5 és 5 között! "))
összeg = 0
lista = []
while -5 <= szám <= 5:
    összeg = összeg + szám
    lista.append(szám)
    szám = int(input("Adj meg egy számot -5 és 5 között! "))
print(lista)
print("Összeg: ", összeg)