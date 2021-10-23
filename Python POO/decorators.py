# los decoradores son funciones extras a otras funciones
def funcion_original():#primera funcion a decorar
    print("hola mundo")

def mi_decorator(func):# decorador donde entra por parametro la primera funcion
    def wrapper():
        print("ejecucion antes de llamar a funcion_original")
        func()#aca pide que ejecute lo que entra por parametro en la linea 5
        print("ejecucion despues de llamar a la funcion")
    return wrapper 

mi_funcion_modificada = mi_decorator(funcion_original)# creo para poderle asignar el funcionamiento
mi_funcion_modificada() #la llamo como funcion 

#-----------------otro metodo----------------
print("-----------------otro metodo----------------")
def mi_decorator2(func):
    def wrapper():
        print("ejecucion antes de llamar a funcion_original")
        func()
        print("ejecucion despues de llamar a la funcion")
    return wrapper 

@mi_decorator2 # esto permite ejecutarla o que se comporte con lo del decorador y tiene que ir antes de la funcion
def funcion_original2():
    print("hola mundo")

funcion_original2()