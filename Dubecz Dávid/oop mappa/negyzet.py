class Negyzet:
    def __init__(self, hossz=(0,0)):
        self.hossz = hossz

    def terulet(self):
        return self.hossz * self.hossz
        
    def kerulet(self):
        return self.hossz * 4
    
    def info(self):
        print(f'A negyzet {self.hossz} hosszusagu, terulete {self.terulet()} , kerulete {self.kerulet()} egyseg.')
    
negyzetek = []
hossz = int(input("adj meg egy oldalhosszat: "))
while hossz !=0:
    negyzet = Negyzet(hossz)
    negyzetek.append(negyzet)
    hossz = int(input("adj meg egy oldalhosszat: "))
for negyzet in negyzetek:
    print(negyzet.info())
        
        
