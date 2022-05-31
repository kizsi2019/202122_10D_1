class Állat:
    def __init__(self, név, tomeg):
        self.név = név
        self.tomeg = tomeg
        
Állatfajok = []

for _ in range(3):
    név = input('Add meg egy állatfaj nevét! ')
    tomeg = input('Hány kilogramm a tömege egy példánynak? ')
    állatfaj = Állat.állatfaj(név, tomeg )
    Állatfajok.append(állatfaj)
    
legnehezebb_állat = Állatfajok[0]

for állatfaj in Állatfajok:
    print('A(z) ', állatfaj.név, ' tömege ', állatfaj.tomeg, ' kg.', sep='')
    if állatfaj.tomeg > legnehezebb_állat.tomeg:
        legnehezebb_állat = állatfajcélfájl = open('legnehezebb.txt', 'w')
    print('A(z)', legnehezebb_állat.fajnév, 'a legnehezebb.', file=célfájl)

célfájl.close()