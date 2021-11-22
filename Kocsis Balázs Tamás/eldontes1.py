import random
list = []
talalat = False
szam2 = int(input('Adj meg egy számot 1 és 7 közt! '))
for i in range(5):
    szam = random.randint(1,7)
    list.append(szam)
print(list)
while index < len(list) and not talalat:
            if list[index] == szam2:
                talalat = True
            index = index + 1
if talalat:
    print('Szerepel a listában! ')
else:
    print('Nem szerepel a listában! ')