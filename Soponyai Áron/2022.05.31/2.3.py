import random
from time import altzone

def nevelo():
    magan = "aáeéoóöüőúűuií"
    if szó[0].lower() in magan:
        return "az"
    else:
        return "a"
    
def jelzo():
    return random.choice(["piros", "nagy", "könnyed"])


print('Adj meg három főnevet!')
for szám in range(1,4):
    főnév = input(str(szám) + '. főnév: ')
    print(nevelo(főnév).capitalize(), ' ', főnév, ' ', jelzo(), '.', sep='')
    