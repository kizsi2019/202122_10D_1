import random
list =[]
összeg = 0
for i in range(5):
    szam = random.randint(1,10)
    list.append(szam)
    összeg = összeg + szam
print('A lista elemi: ', list)
print('Az összeg: ', összeg)