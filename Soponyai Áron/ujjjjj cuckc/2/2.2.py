szavak = []
szó = None

while szó !='':
    szó = input("Adj meg kis a betüs szavakat!")
    if szó !='' and (szó[0] == "a" or szó[0] == "A"):
        szavak.append(szó)
print(szavak)