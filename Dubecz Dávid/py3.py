szam1 = int(input("Adj egy orat "))

if szam1 > 8 and szam1 < 16:
    print("A bolt nyivta mar ennyi ideje:", szam1-8)
if szam1 < 8:
    print("A bolt nyivta lesz ennyi ora mulva:", 8-szam1)
if szam1 == 8:
    print("A bolt nyivta van, mert pont 8 ora van")
if szam1 > 16:
    print("A bolt zarva van", szam1-16, "oraja")