szo1 = input('Adj meg egy szót! ')
szo1_hossza = len(szo1)
szo2 = input('Adj meg egy másik szót! ')
szo2_hossza = len(szo2)
if szo1_hossza > szo2_hossza:
    print('A hosszabb szó:', szo1)
elif szo2_hossza > szo1_hossza:
    print('A hosszabb szó:', szo2)
else:
    print('A két szó egyforma hosszú.')