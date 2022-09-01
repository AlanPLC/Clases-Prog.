# TPN°1 : Modelar la clase Alfil y Caballo usando como
# clase padre pieza. No tener en cuenta el límite del 
# tablero para los movimientos.

class pieza():
    def __init__(self,color,posx,posy):
        self.color = color
        self.posx = posx
        self.posy = posy
        self.mov = False

    def posicion(self,orden):
        # print(orden,"(",self.posx,",",self.posy ,")")
        print(f"{orden} ({self.posx},{self.posy})")

class peon(pieza):
    def __init__(self,color,posx,posy):
        pieza.__init__(self,color,posx,posy)
        print("Se ha creado un peon ", color)

    def mover(self):
        self.posicion("Inicial")
        if self.mov == False:
            paso = 3
            while(int(paso)>2 or int(paso)<0):
                paso = int(input("Ingrese 1 o 2 \n"))
            self.posy = self.posy + paso
            self.mov = True
        else:
            self.posy = self.posy + 1
        self.posicion("Final")


class torre(pieza):
    def __init__(self,color,posx,posy):
        pieza.__init__(self,color,posx,posy)
        print("Se ha creado un torre ", color)

    def mover(self):
        self.posicion("Inicial")
        direccion = input("En que direccion se mueve x/y \n")
        casillas = 0
        casillas = int(input("Cantidad de casillas \n"))
        if(direccion == "x"):
            sentido = input("Sentido derecha/izquierda \n")
            if(sentido == "derecha"):
                self.posx = self.posx + casillas
            else:
                self.posx = self.posx - casillas
        else:
            sentido = input("Sentido arriba/abajo \n")
            if (sentido == "arriba"):
                self.posy = self.posy - casillas
            else:
                self.posy = self.posy + casillas
        self.posicion("Final")

class caballo(pieza):
    def __init__(self,color,posx,posy):
        pieza.__init__(self,color,posx,posy)
        print("Se ha creado un Caballo", color)
    
    def mover(self):
        self.posicion("Inicial")
        direccion = input("¿En qué dirección se mueve? (arriba/abajo/izquierda/derecha)\n")
        if(direccion=="arriba"):
            sentido=input("¿Con sentido hacia la derecha o izquierda?:\n")
            if (sentido=="derecha"):
                self.posy+=2
                self.posx+=1
            else:
                self.posy+=2
                self.posx-=1
        if(direccion=="abajo"):
            sentido=input("¿Con sentido hacia la derecha o izquierda?:\n")
            if (sentido=="derecha"):
                self.posy-=2
                self.posx+=1
            else:
                self.posy-=2
                self.posx-=1
        if(direccion=="derecha"):
            sentido=input("¿Con sentido hacia arriba o abajo?:\n")
            if(sentido=="arriba"):
                self.posx+=2
                self.posy+=1
            else:
                self.posx+=2
                self.posy-=1
        if(direccion=="izquierda"):
            sentido=input("¿Con sentido hacia arriba o abajo?:\n")
            if(sentido=="arriba"):
                self.posx-=2
                self.posy+=1
            else:
                self.posx-=2
                self.posy-=1
        self.posicion("Final")

class alfil(pieza):
    def __init__(self,color,posx,posy):
        pieza.__init__(self,color,posx,posy)
        print("Se ha creado un Alfil", color)

    def mover(self):
        self.posicion("Inicial")
        casillas=0
        casillas=int(input("Cantidad de casillas que va a mover:\n"))
        direccion=input("¿En qué dirección se va a mover? (arriba/abajo)\n")
        if(direccion=="arriba"):
            sentido=input("¿Con sentido hacia la derecha o izquierda?\n")
            if(sentido=="derecha"):
                self.posy+=casillas
                self.posx+=casillas
            else:
                self.posy+=casillas
                self.posx-=casillas
        else:
            sentido=input("¿Con sentido hacia la derecha o izquierda?\n")
            if(sentido=="derecha"):
                self.posy-=casillas
                self.posx+=casillas
            else:
                self.posy-=casillas
                self.posx-=casillas
        self.posicion("Final")
        
#peon1 = peon("negro",1,2)
#peon1.mover()
#peon1.mover()

#torre1 = torre("negro",1,1)
#torre1.mover()

#caballo1=caballo("negro",5,5)
#caballo1.mover()

#alfil1=alfil("negro",5,5)
#alfil1.mover()


    



