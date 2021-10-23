class Coche: # esta es la clase tipo coche
    
    def __init__(self, modelo, potencia, consumo): # el constructor y su inicializacion 
        self.modelo = modelo 
        self.potencia = potencia
        self.consumo = consumo
        self._km_actuales = 0
        self._combustible = "1/100 km" 

    def espesificaciones(self):
        print("Modelo", self.modelo,
        "\nPotencia: {} cv".format(self.potencia),
        "\nConsumo: {} {}".format(self.consumo, self._combustible),
        "\nKilometros actuales: ",self._km_actuales) 
        
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


class Coche_electrico(Coche): # esta heredando metodos y atributos de la clase coche
    
    def __init__(self, modelo, potencia, consumo,capacidad_bateria):#inicializa los atributos de la clase padre
        super().__init__(modelo, potencia, consumo)
        self._combustible = "KWH/100km"
        self._capacidad_bateria = capacidad_bateria 

    def detalles_bateria(self):
        print("El tamaño de la bateria es : {} KWH" .format(self._capacidad_bateria))

tesla = Coche_electrico("modelo tesla 3", 300, 15, 50)
tesla.espesificaciones()
tesla.detalles_bateria()


 