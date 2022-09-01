import random

class dado():
    def __init__(self,caras):
        self.caras=caras

    def tirar(self):
        print("Salió ",random.randint(1,self.caras))
        cara = random.randint(1,self.caras)
        return cara
        
dado1=dado(6)
dado1.tirar()
