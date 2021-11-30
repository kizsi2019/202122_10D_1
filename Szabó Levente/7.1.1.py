import random
list = []
összeg = 0
for i in range(5):
    szám = random.randint(1, 10)
    list.append(szám)
    összeg = összeg + szám
print('A lista elemei: ', list)
print('Az összeg: ', összeg)