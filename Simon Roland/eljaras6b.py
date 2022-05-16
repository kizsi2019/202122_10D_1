def mezot_rajzol():
    for sor in range(3):
        for oszlop in range(6):
            if sor == xkord and oszlop == ykord:
                print('x ', end ='')
            else :
                print('O ', end ='')
        print()
xkord = int(input("add meg az x koordinátát got milf"))
ykord = int(input("add meg az y koordinátát got milf"))

mezot_rajzol()