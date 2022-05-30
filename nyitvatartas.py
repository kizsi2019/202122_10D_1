time = int(input("Hány óra van most? "))

close = 16
open = 8

if time >= open and time < close:
    print("A bolt nyitva van")
    print("Ennyi órád van még odaérni: ",close - time)
else:
    print("A bolt zárva van.")