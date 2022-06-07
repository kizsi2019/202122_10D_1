class lady:
    def __init__(self, nev, munka, nemzetiseg):
        self.nev = nev
        self.munka = munka
        self.nemzetiseg = nemzetiseg
        
    def elotag(self):
        if self.nemzetiseg == "a":
            return "Ms."
        else:
            return "Frau"

hires_nok = []
for _ in range(3):
    nev = input("Add meg a popular lady nevét! ")
    munka = input("Add meg a munkáját! ")
    nemzetiseg = input("Add meg a nemzetiségét! ")
    hires_lady = lady(nev, munka, nemzetiseg)
    hires_ladyk.append(hires_lady)

for hires_no in hires_nok:
    print(lady.elotag(), hires_lady.nev, "egy popular", hires_lady.munka)