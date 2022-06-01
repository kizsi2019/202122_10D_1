def sikeres(pontok):
    if pontok >= 48:
        return True
    else:
        return False
név = None
név = input("Add meg a nevet! ")
if név:
    pontok = int(input("Add meg a pontszámot! "))
    if sikeres(pontok):
        print(név, "vizsgája sikeres lett.")
    else:
        print(név, "vizsga sikertelen lett.")
