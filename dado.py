import random

class dado():
    def __init__(self,caras):
        self.caras=caras

    def tirar(self):
        cara1 = random.randint(1,self.caras)
        print(f"\nSalió {cara1}")
    
    def varios_dados(self,cantidad_dados):
        total=0
        for i in range (0,cantidad_dados):
            cara = random.randint(1,self.caras)
            total += cara
            print ("Salió ", cara)
        print ("\nEl total es: ",total)
        return total

dado1=dado(6)
dado1.varios_dados(9)
dado1.tirar()
