szavak = ['alma', 'barack', 'Attila', 'kávé', 'szekrény', 'asztal']
lista = []
for szo in szavak:
    if szo[0] == 'A' or szo[0] == 'a':
        lista.append(szo)
print(' A feltételnek megfelelő szak: ' , lista)