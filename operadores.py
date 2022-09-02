class operadores():
    def __init__(self,operador1,operador2):
        self.operador1=operador1
        self.operador2=operador2
    
    def suma(self):
        print(self.operador1, "+", self.operador2 ,"= ", self.operador1+self.operador2)

    def producto(self):
        print(self.operador1, "x", self.operador2 ,"= ", self.operador1*self.operador2)

lol=operadores(5,6)
lol.suma()
lol.producto()

