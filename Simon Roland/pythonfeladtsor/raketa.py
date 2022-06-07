start = int(input("Hány órás visszaszámlálást tervezünk?" )) 
felfüggesztések = 0

for szam in range(start,0, -1):
    print('Visszaszámlálás:', szam)
    válasz = input('Fel kell függeszteni a visszaszámlálást (i/n)? ')
    if válasz == 'i':
        felfüggesztések += 1
print('A rakéta a visszaszámlálást követően ennyi órával indult:', start + felfüggesztések)