szó = "almafa"
betű = int(input("Adj meg egy betűt"))
talalat = False
index = 0
while index < len(szó) and not talalat:
	if szó[index] == betű:
		talalat = True
	index = index + 1
print("A szó", szó)

if talalat:
	print("A kapott betű szerepel a szóban")
else:
	print("A kapott betű nem szerepel a szóban")
