szamok = []

szam  = None
while szam != "":
    szam = int(input("Adj meg számokat: "))
    if szam < 0:
        szamok.append(szam)

    
def harommal_oszthatok(sz):
    oszthato = 0
    for sz in sz:
        if sz % 3 == 0:
            oszthato = oszthato + 1    
    return oszthato
           
oszthatok = harommal_oszthatok(szamok)

print(oszthatok)