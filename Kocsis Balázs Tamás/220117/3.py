x = int(input("Add meg a dolgozatod pontszámát! "))

if x < 50:
    print("A dolgozatod 1-es lett! ")
elif 50 < x < 60:
    print("A dolgozatod 2-es lett! ")
elif 60 < x < 70:
    print("A dolgozatod 3-as lett! ")
elif 70 < x < 85:
    print("A dolgozatod 4-es lett! ")
else:
    print("A dolgozatod 5-ös lett! ")