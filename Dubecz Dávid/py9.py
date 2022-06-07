import random

def nevelo():
    magan = "aáeéiíoóöőuúüű"
    if szo[0].lower() in magan:
        return "az"
    else:
        return "a"

def jelzo():
    return random.choice(["piros", "nagy", "könnyed"])

print("Adj három főnevet!")
for sorszam in range(1, 4):
    fonev = input(str(sorszam) + ". főnév: ")
    print(nevelo(fonev).capitalize(), "", fonev, "", jelzo(), ".")