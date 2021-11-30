import random

num1 = random.randint(1,20)
print(num1)
num2 = int(input("Adj megy egy számot 1-20ig: "))

while num1 != num2:
    num2 = int(input("Adj megy egy számot 1-20ig: "))
if num1 == num2:
    print("A két szám egyenlö")

