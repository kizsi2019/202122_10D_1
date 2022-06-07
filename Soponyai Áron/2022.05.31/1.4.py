indul = input('Hány órás visszaszámlálást tervezünk? ')
indul = int(indul)
marad = 0
for szám in range(indul, 0, -1):
    print('Visszaszámlálás:', szám)
    válasz = input('Fel kell függeszteni a visszaszámlálást (i/n)? ')
    if válasz == 'i':
        marad += 1
    print('A rakéta a visszaszámlálást követően ennyi órával indult:', indul + marad)