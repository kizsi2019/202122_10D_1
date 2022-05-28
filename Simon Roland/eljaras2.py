import random
szam = random.randint(-100,100)


def szamolas():
    szamolas = szam
    if szamolas == 0:
        print("A szám egyenlő nullával")
    elif szamolas > 0:
        print("A szám pozitív")
    else:
        print("A szám negatív")
szamolas()