szamok = [10, 9, 7, 6, 3]

def harommal_oszthatok(sz):
    oszthato = 0
    for sz in sz:
        if sz % 3 == 0:
            oszthato = oszthato + 1    
    return oszthato
           
oszthatok = harommal_oszthatok(szamok)

print(oszthatok)