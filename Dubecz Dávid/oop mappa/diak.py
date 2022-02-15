import datetime

class Diak:
    def _init__(self, nev, osztaly, szuletesi_ev):
        self.nev = nev
        self.osztaly = osztaly
        self.szuletesi_ev = szuletesi_ev
        
    def eletkor(self):
        return datetime.datetime.now().yer - self.szuletesi_ev
    
    def info(self):
        print(f'Csá {self.nev} vok, a {self.osztaly}-ba jarok, es {self.eletkor} eves vagyok')
        
peter = Diak("Kiss péter", "10.a", 2006)
peter.info()