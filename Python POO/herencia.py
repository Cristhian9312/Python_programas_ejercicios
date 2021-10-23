import types


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

class Bateria: # Clase que espesifica una bateria para un carro

    def __init__(self, capacidad, tipo_pila, num_pilas, peso):# constructor donde inicializo las variables
        self._capacidad = capacidad
        self._tipo_pila = tipo_pila
        self._num_pilas = num_pilas
        self._peso = peso    

    def espesificaciones_bateria(self):
        print(f"Capacidad: {self._capacidad} KWH\n",
        f"Tipo de pilas: {self._tipo_pila}\n",
        f"Numero de pilas: {self._num_pilas}\n",
        f"Peso: {self._peso}")

class Coche_electrico(Coche): # esta heredando metodos y atributos de la clase coche
    
    def __init__(self, modelo, potencia, consumo, bateria):#inicializa los atributos de la clase padre
        super().__init__(modelo, potencia, consumo)
        self._combustible = "KWH/100km"
        self._bateria = bateria

    def detalles_bateria(self):
        self._bateria.espesificaciones_bateria()
    
    def consumo_total(self):
        consumo = (self._km_actuales/100)*self.consumo
        print("El consumo total es de {} KWH ".format(consumo))
 

"""
tesla = Coche_electrico("modelo tesla 3", 300, 15, 50)
tesla.espesificaciones()
tesla.detalles_bateria()
tesla.consumo_total()
tesla.kilometros = 100
tesla.consumo_total()
"""

bateria_tesla_modelo = Bateria(80, 2170, 203_541,480)
tesla = Coche_electrico("tesla modelos S",450,20,bateria_tesla_modelo)
#bateria_tesla_modelo.espesificaciones()
tesla.detalles_bateria() 