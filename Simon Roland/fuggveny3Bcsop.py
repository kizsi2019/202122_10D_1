lista = [4, 9, 12, 32, 90]

def harommal_oszthatok(lista):
  darab = 0
  for i in lista:
    if i % 3 == 0:
      darab = darab + 1
  
  return darab

print("Hárommal osztható számok:", harommal_oszthatok(lista))