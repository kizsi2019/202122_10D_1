import random
poziciok = ["A1","A2","A3","B1","B2","B3","C1","C2","C3"]
pozicio = random.choice(poziciok)
összestalalat = 0
tipp = input("Adj meg egy poziciót!")
talalat = False
while összestalalat <= 9 and not talalat:
    if pozicio == tipp:
        talalat = True
    else:
        tipp = input("Adj meg egy poziciót!")
    összestalalat = összestalalat + 1
print("A pozicio:", pozicio)
if talalat:
    print("Találat")
    print("Ennyiből találtad ki:", összestalalat)
else:
    print("Nem talált")
