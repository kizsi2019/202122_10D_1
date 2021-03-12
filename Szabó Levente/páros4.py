folytatja = True
while folytatja:
    szám = int(input("Kérek egy páros számot! "))
    if szám%2 == 0:
        folytatja = False
    if not szám%2 == 0:
        folytatja = True
        print("Ez a szám nem páros. ")
print("Ez a szám páros! ")