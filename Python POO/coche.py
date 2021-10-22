class Coche:
    
    def __init__(self, modelo, potencia, consumo):
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

    def actualizar_kilometros(self, kilometros):
        if kilometros > self._km_actuales:
            self._km_actuales = kilometros
        else:
            print("no se puede establecer un numero de kilometros menores a 0")
    
    def consumo_total(self):
        consumo = (self._km_actuales/100)*self._consumo
        print("El consumo total es de {} litros ".format(consumo))

renault = Coche("modelo 2015", 80, 2)
renault.espesificaciones() 
renault.actualizar_kilometros(1000)
renault.espesificaciones()
renault.consumo_total()
 