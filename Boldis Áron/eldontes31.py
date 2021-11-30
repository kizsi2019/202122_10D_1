import random
poziciok =["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
pozicio = random.choice(poziciok)

tipp =input("Adj meg egy pozíciót! ")
talalat = False
index = 0

while index <= 9 and not talalat:
    if pozicio == tipp:
        talalat = True
    else:
        tipp =input("Adj meg egy pozíciót! ")
    index = index +1
print ("A pozíció: ", pozicio)
if talalat:
    print("Talált")
    print("Ennyiből talaltad ki: ", index)
else:
    print("Nem talált")
    