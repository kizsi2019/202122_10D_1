import random
helyek = ['a1', 'a2', 'a2', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
hely = random.choice(helyek)
#print(helyek)
tipp = input("Adj meg egy poziciót! ")
találat = False
index = 0
while index <= 9 and not találat:
    if hely == tipp:
        találat = True
    else:
        ripp = input(" Adj meg egy pozíciót")
    index = index + 1
    if találat:
        print("Talált! ")
    else:
        print("Nem talált! ")