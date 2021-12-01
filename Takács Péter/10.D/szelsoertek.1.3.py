lista = []
lista2 =[]
for i in range(4):
  szam = input("Adj meg egy számot! ")
  
  lista.append(szam)

for i in lista:
  if i % 2 == 0:
    lista2.append(i)
    

min = lista2[0]
max = lista2[0]
for i in lista2:
   
  if i <min and i % 2 == 0: 
    min= i
  if i >max and i % 2 == 0:
    max = i

print(lista2)
print("Legkisebb: ", min)
print("Legnagyobb: ", max)
