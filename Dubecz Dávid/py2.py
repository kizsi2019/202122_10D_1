szo1 = str(input("Adj egy szot "))
szo2 = str(input("Adj egy masik szot "))
szohossz1 = len(szo1)
szohossz2 = len(szo2)

if szohossz1 > szohossz2:
    print("A hosszabb szo a", szo1)
else:
    print("A nagyobb szo a", szo2)