
class encriptador():
    def __init__(self, palabra):
        self.palabra = palabra
        self.lista=[]
    
    def encriptar(self):
        for letra in self.palabra:
            if letra == "a":
                self.lista.append("0")
            elif letra == "e":
                self.lista.append("1")
            elif letra == "i":
                self.lista.append("2")
            elif letra == "o":
                self.lista.append("3")
            elif letra == "u":
                self.lista.append("4")
            else:
                self.lista.append(letra)
        print(self.lista)

lol=encriptador("hola")
lol.encriptar()