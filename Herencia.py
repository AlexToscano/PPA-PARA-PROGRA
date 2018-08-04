class vehiculo :
    def __init__(self,velmaxima,capacidad,color,aceleracion):
        self.velmaxima=velmaxima
        self.capacidad=capacidad
        self.color=color
        self.velActual=0
        self.enMovimiento=False
        self.aceleracion=aceleracion

    def Acelerar(self):
        if(self.velActual <= self.velmaxima):
            self.velActual += self.aceleracion
        self.enMovimiento=True
  
    def frenar(self):
        if(not(self.velActual>0)):
            self.enMovimiento=False
        self.velActual -= self.aceleracion

class coche(vehiculo):
    def __init__(self,velmaxima,capacidad,color,aceleracion,numllan):
        super().__init__(velmaxima,capacidad,color,aceleracion)
        self.numllantas=numllan

scooter = vehiculo(8,1,"Azul",1)
mustang = coche(340,5,"Rojo",5,4)
print(mustang.velActual)
mustang.Acelerar()
print(mustang.velActual)