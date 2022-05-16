lista = []
szam = int(input("Adj meg egy számot! "))
while szam >= 0:
  lista.append(szam)
  szam = int(input("Adj meg egy számot! "))

def harommal_oszthatok(lista):
  darab = 0
  for i in lista:
    if i % 3 == 0:
      darab = darab + 1
  
  return darab

print("Hárommal osztható számok:", harommal_oszthatok(lista))