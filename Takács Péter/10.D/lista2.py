keresztnevek = []
nev = None
szamlalo = 1

while nev !='' and szamlalo < 4:
    nev = input('Adj meg egy keresztnevet! ')
    if nev !='':
        keresztnevek.append(nev)
    szamlalo = szamlalo + 1    
print(keresztnevek)