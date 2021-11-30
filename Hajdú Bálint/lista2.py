

list2=[]
list=[]
min = [0]
max=[0]
for i in range(10):
  szam = int(input('adj meg egy számot!'))
  list.append(szam)
min=list[0]
max=[0]
for i in list:
  szam=int(input('adjmeg egy számot!'))
min=list[0]
max=list[0]
for i in list:
  if i < min:
    min=i
  if i>max:
    max=1


print('legnagyobb',max)
print('legkissebb',min)
print('list')
