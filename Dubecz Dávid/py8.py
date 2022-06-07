def hourmins(mins):
    hour = mins // 60
    mins = mins - hour * 60
    return str(hour) + " óra " + str(mins) + " perc"

for _ in range(3):
    cim = str(input("Add meg a film! "))
    hossz = int(input("Hány perces a film? "))
    print("A", cim, "film", hourmins(hossz), "hosszú.")