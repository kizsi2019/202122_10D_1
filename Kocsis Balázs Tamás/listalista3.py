elem = 'O '
sor = [elem, elem, elem]
tarolo = [sor, sor, sor]

def rajzolas():
    xkord = int(input("Add meg az x koordinátát! "))
    ykord = int(input("Add meg az y koordinátát! "))
    for sor in range(3):
        for oszlop in range(3):
            if sor == xkord and oszlop == ykord:
                print('+ ', end='')
            else:
                print(elem, end='')
        print()

rajzolas() 