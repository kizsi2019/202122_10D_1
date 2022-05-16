szó = "kutyafüle"
betű = int(input("Adj meg egy betűt"))
találat = False
index = 0 
while index < len(lista) and not talalat:
	      if szó[index] == 'piros':
		        talalat = True
	index = index + 1
print("A szó", szó)
    if talalat:
	print("A kapott betű szerepel a szóban")
else:
	 print("A kapott betű nem szerepel a szóban")
