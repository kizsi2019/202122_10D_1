óra = int(input("Hány óra van? "))
if óra < 7:
    print("még zárva van. ")
elif óra > 16:
    print("már zárva van. ")
else:
    print("nyitva van. ")