óra = input('Hány óra van most? ')
óra = int(óra)
if óra >= 8 and óra < 16:
    print('A bolt nyitva van.')
    zárásig = 16 - óra
    print('Ennyi órád van még odaérni:', zárásig)
else:
    print('A bolt zárva van.')