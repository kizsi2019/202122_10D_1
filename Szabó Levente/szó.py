szó = input("Adj meg egy szót! ")
szó1 = input("Adj meg egy másik szót! ")
if len(szó) > len(szó1):
    print ("Az első a nagyobb")
elif len(szó) == len(szó1):
    print("Két szó egyenlő hosszú! ")
else:
    print("Második hosszabb. ")