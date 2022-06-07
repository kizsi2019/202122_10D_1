def siker(pont):
    if pont >= 48:
        return True
    else:
        return False

name = None
while name != "":
    name = str(input("Add megj meg nevet! "))
    if name:
        pont = int(input("Add meg a pontjait! "))
    
        if siker(pont):
            print(name, "vizsgája sikeres.")
        else:
            print(name, "vizsgája sikertelen.")