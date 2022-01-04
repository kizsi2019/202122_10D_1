list = []

for i in range(3):
    szo = input("Adj meg egy szót! ")
    list.append(szo)

min = list[0]

for i in list:
    if i < min:
        min = i

print("Legrövidebb", min)