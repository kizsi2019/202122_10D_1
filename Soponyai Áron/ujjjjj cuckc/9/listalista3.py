xy = int(input("adj meg kordinátát"))
elem = "o"
sor = [elem, elem, elem]
tarolo = [sor,sor,sor]
def rajzolas():
    for sor in tarolo:

        for elem in sor:
            print(elem, end="")
        print()
rajzolas()
