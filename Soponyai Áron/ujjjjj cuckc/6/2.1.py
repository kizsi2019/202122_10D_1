szavak = ["alma","barack", "Atilla", "kávé","szekrény", "asztal"]
lista = []
for szó in szavak:
    if szó[0] == "a" or szó[0] == "A":
        lista.append(szó)
print("A feltételnek megfelelő szavak", lista)