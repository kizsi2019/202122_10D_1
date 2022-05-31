def sikeres(pontszam):
    if pontszam >= 48:
        return True
    else:
        return False
vizsgazo = None


while vizsgazo != "":
    vizsgazo = input("Add meg a vizsgázó nevét! ")
    if vizsgazo:
        pont = int(input("Add meg a pontszámát! "))
        if sikeres(pont):
            print(vizsgazo, "vizsgája sikeres")
        else:
            print(vizsgazo, "vizsgája sikertelen.")

