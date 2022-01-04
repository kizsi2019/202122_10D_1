def mezot():
  for sor in range(3):
    for oszlop in range (6):
      if sor == x and oszlop == y:
        print("X", end ="")

      else:
        print("O", end="")

    print()
x=int(input("Add meg az x kordinátát!"))
y=int(input("Add meg az y kordinátát!"))
mezot()