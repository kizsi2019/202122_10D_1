import random
list = []
összeg = 0
for i in range(5):
    szam = random.randint(1,10)
    list.append(szam)
    összeg = összeg + 1
print('A lista elemei: ', list)
print('Az összegük: ', összeg)