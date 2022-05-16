import random 
poziciók =['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
pozíció = random.choice(poziciok)
# print(pozíciók)
tipp = input("Adj meg egy pozíciót! ")
találat = False
index = 0
while index <= 9 and not találat:
    if pozíció == tipp:
        találat = True
    else: 
     tipp = input("Adj meg egy pozíciót")
index = index + 1
if találat:
    print("Talált! ")
else:
    print("Nem talált! ")

     