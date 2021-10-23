class Coche: # esta es la clase tipo coche
    
    def __init__(self, modelo, potencia, consumo): # el constructor y su inicializacion 
        self._modelo = modelo 
        self._potencia = potencia
        self._consumo = consumo
        self._km_actuales = 0 

    def espesificaciones(self):
        print(f"""
        El modelo es del auto es: {self._modelo} \n
        La potencia del auto es de: {self._potencia} \n
        El consumo del auto es de {self._consumo} litros * KM\n
        Kilometros actuales: {self._km_actuales}""") 
        
    @property
    def kilometros_property(self):
        return self._km_actuales

    @kilometros_property.setter
    def kilometros(self, kilometros):
        if kilometros > self._km_actuales:
            self._km_actuales = kilometros
        else:
            print("no se puede establecer un numero de kilometros menores a 0")
    
    def consumo_total(self):
        consumo = (self._km_actuales/100)*self._consumo
        print("El consumo total es de {} litros ".format(consumo))

renault = Coche("modelo 2020", 88, 7)
print("esto es...",renault.kilometros_property)
renault.kilometros=500
renault.espesificaciones()
renault.kilometros=200
renault.consumo_total()


 