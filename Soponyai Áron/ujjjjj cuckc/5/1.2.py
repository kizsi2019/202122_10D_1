import random
összeg = 0
list = []
for i in range(5):
    szam = random.randint(1,10)
    list.append(szam)
    összeg=összeg+szam
print( "A list elemei", list)
print("Az összeg:", összeg)