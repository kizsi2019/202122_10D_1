ora = int(input("Hány óra van most?" ))
if ora < 16 and ora >= 8:
    print("A bolt nyitva van.")
    print("Ennyi órád van még odaérni:", 16 - ora )
else:
    print("A bolt zárva van.")