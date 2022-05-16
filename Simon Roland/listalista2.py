elem = 'O '
sor = [elem,elem,elem]
tarolo = [sor, sor, sor]
print (tarolo)
def rajzolas(): 
    for sor in tarolo: 
        for elem in sor: 
            print(elem, end='')
        print()
rajzolas() 