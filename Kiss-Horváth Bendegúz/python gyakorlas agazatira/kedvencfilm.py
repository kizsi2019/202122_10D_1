def oraperc(hossz):
    ora = hossz // 60
    perc = hossz - ora * 60
    return str(ora) + "óra" + str(perc)+ "perc"
        




for _ in range(3):
    film_nev = input("Add meg egy film címét! ")
    hossz = int(input("Hány perces a film? "))
    print("A(z)", film_nev, "című film", oraperc(hossz), "hosszú")