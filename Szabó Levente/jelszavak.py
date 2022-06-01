bejelntkezés = False
while not bejelntkezés:
    felhasználónév = input('Add meg a felhasználóneved! ')
    jelszó = input('Adja meg a jelszavad! ')
if felhasználónév == 'bori99' and jelszó == 'Szivecske<3':
    print('A belépés engedélyezve van.')
    bejelntkezés = True
else:
    print('A belépés megvan tagadva.')