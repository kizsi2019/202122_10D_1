start = int(input('Hány órás visszaszámlálást tervezünk? '))
felfüggesztések = 0

for num in range(start, 0, -1):
    print('Visszaszámlálás:', num)
    felfugg = input('Fel kell függeszteni a visszaszámlálást (i/n)? ')
    if felfugg == 'i':
        felfüggesztések += 1
print('A rakéta a visszaszámlálást követően ennyi órával indult:', start + felfüggesztések)