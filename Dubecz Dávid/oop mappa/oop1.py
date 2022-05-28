kor_01 = {
    "kozeppont" : (2, 5),
    "sugar" : 10
}

def terulet (kor):
    return kor["sugar"] * pow(3.14, 2)

def kerulet(kor):
    return kor["sugar"] * 2 * 3.14

print(f"A kör kerülete: {kerulet(kor_01)} egyseg")
print(f"A kör területe: {terulet(kor_01)} egyseg")