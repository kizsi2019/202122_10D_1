szó1 = input("Adj meg egy szót. ")
szó2 = input("Adj meg egy másik szót. ")
if len(szó1) > len(szó2):
    print("Az első szó hosszabb.. ")
elif len(szó1) == len(szó2):
    print("A két szó egyenlő hosszú. ")
else:
    print("A második szó a hosszabb. ")