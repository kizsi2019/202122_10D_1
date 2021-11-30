import random
list =[]
talalat = False
szam2 =int(input("Adjmeg egy számot kérlek 1 és 7 között"))
for i in range(5):
    szam = random.randint(1,7)
    list.append(szam)
print(list)
 while index < len(list) and not talalat:
     if list[index] == szam2: 
        talalat = True 
    index =index + 1
    
    if talalat:
        print('szerepel a listában a szám')
        else:
            print('nem szerepel a listában')
    