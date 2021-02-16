szam = True
while szam: 
    valasz = int(input("Adjon meg egy páros számot! "))
    if valasz%2 == 0:
        szam = False
print("Ez egy páros szám, program vége! ")