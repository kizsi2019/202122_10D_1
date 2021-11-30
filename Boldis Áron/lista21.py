szavak = []
szo = None


while szo !='':
    szo = input("Adj meg szavakat: ")
    if szo !="" and szo[0] == "a":
        szavak.append(szo)
    
print(szavak)