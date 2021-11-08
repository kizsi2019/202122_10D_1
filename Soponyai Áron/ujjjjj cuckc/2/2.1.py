szavak = []
szó = None

while szó !='':
    szó = input("Adj meg kis a betüs szavakat!")
    if szó !='' and szó[0] == "a":
        szavak.append(szó)
print(szavak)