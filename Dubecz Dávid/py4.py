szam1 = int(input("Hany masodperces a kiloves?"))
yn = str(input("Fel kell függeszteni a visszaszámlálást (i/n)?"))
switch = False

if yn == "n":
    print(szam1-1)
    switch == False
if switch == False:
    yn = str(input("Fel kell függeszteni a visszaszámlálást (i/n)?"))
    print(szam1-1)
elif yn == "i":
    print("Leallitva")