import allat

allatok = []
for _ in range(3):
    fajnév = input("Add meg egy állatfaj nevét!")
    tomeg = input("Hány kilogramm a tömege egy példánynak?")
    faj =  allat.faj(fajnév, tomeg)
    allatok.append(faj)

legnehezebb = faj[0]

for faj in allatok:
    print('A(z) ', faj.fajnév, ' tömege ', faj.tömeg, ' kg.', sep='')
    if faj.tömeg > legnehezebb_állat.tömeg:
        legnehezebb_állat = faj

f = open('legnehezebb.txt', 'w')
print('A(z)', legnehezebb_állat.fajnév, 'a legnehezebb.', file=f)
f.close()