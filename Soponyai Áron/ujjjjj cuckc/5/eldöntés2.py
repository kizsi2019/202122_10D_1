szó = "kutyafüle"
betu = input("Adj meg egy betűt")
talalat = False
index = 0
while index < len(szó) and not talalat:
    if szó[index] == betu:
        talalat = True
    index = index + 1
    
if talalat:
    print('Van olyn betu.')
else:
    print('Nincs olyan betu.')