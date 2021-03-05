olytatja = True
while folytatja:
    szam = int(input("Adj meg egy páros számot!"))
    if szam%2 == 0:
        folytatja = False
    if not szam%2 == 0:
        folytatja = True
        print("Ez nem páros szám! Adj meg egy új számot")
print("Szép!")