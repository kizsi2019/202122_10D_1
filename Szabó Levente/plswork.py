class Negyzet:
    def __init__(self, hossz):
        self.hossz = hossz
    def terület(self):
        return self.hossz * self.hossz
    def kerület(self):
        return self.hossz * 4
    def info(self):
        print(f'A {self.hossz} négyzet területe {self.terület()}, kerülete {self.kerület()}')

hossz = []
while hossz != 0:
    hossz = int(input("Add meg a hosszát. "))
    terület = hossz * hossz
    kerület = hossz * 4
else:
    print("Nem")