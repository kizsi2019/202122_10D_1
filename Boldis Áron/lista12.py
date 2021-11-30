kersztnevek = []
nev = None
szamlalo = 1

while nev !='' and szamlalo < 4:
    nev = input("Adj meg egy keresztnevet:! ")
    szamlalo = szamlalo + 1
    if nev !="":
        kersztnevek.append(nev)
    
print(kersztnevek)