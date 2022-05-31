x = int(input("Hány óra van? "))
if x >= 8 and x < 16:
    print("A bolt még nyitva van. ")
    print('Ennyi órád van még odaérni: ', 16 - x)
else:
    print("A bolt zárva van. ")