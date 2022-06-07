jó = False

while not jó:
    név=input("Adja meg a felhasználónevét")
    jelszó=input("Adja meg a jelszavadat")
    if név == "bori99" and jelszó == "Szivecske<3":
        print("belépés engedélyezve")
        jó = True
    else:
        print("Belépés megtagadva")

