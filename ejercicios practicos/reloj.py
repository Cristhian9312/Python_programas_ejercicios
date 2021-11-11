"""
ingresar un reloj que se le ingrese la hora, minutos y segundo
al finalizar entonces mostrar la hora con un segundo de mas 
"""

hora = int(input("ingrese las horas: "))
minutos = int(input("ingrese los minutos: "))
segundos = int(input("ingrese los segundos: "))

if segundos < 59:
    print(f"{hora}:{minutos}:{segundos + 1}")  
else:
    if minutos < 59:
        segundos = 0
        print(f"{hora}:{minutos + 1}:{segundos}0")
    else:
        if hora < 23:  
            minutos=0
            segundos=0
            print(f"{hora + 1}:{minutos}0:{segundos}0") 
        else:    
            hora = 0
            minutos=0
            segundos=0
            print(f"{hora}0:{minutos}0:{segundos}0")




