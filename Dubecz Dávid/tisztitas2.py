import string

def irasjel_eltavolitas(szoveg):
    irasjel_nelkuli = ""
    for karakter in szoveg:
        if karakter not in string.punctuation:
            irasjel_nelkuli += karakter
    return irasjel_nelkuli

print(irasjel_eltavolitas("Szia lajos!"))