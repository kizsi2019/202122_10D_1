pontszambekeres = int(input("Adja meg a dolgozat pontszámot: "))

if pontszambekeres < 50:
    print("Az érdemjegy: 1")
elif pontszambekeres >= 50 and pontszambekeres < 60:
    print("Az érdemjegy: 2")
elif pontszambekeres >= 60 and pontszambekeres < 70:
    print("Az érdemjegy: 3")
elif pontszambekeres >= 70 and pontszambekeres < 85:
    print("Az érdemjegy: 4")
elif pontszambekeres >= 85:
    print("Az érdemjegy: 5")