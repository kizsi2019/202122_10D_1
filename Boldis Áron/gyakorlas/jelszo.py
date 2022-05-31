
jelszo = "Szivecske<3"
felhaszn = "bori99"

loop = False

while loop == False:
    in1 = input("Add meg a felhasználóneved: ")
    in2 = input("Add meg a jelszavad: ")
    
    if in1 == felhaszn and in2 == jelszo:
        loop = True
    else:
        print("Belépés megtagadva")

print("Belepes engedélyezve")