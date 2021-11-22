keresztnevek = []
nev = None
szamlalo = 1

while nev !='' and szamlalo < 4:
    nev = input("adj meg egy nevet!")
    szamlalo = szamlalo + 1 
    if nev !='':
        keresztnevek.append(nev)
        
print(keresztnevek)