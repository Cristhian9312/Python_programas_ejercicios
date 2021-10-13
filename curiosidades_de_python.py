#palabra = input("ingrese algo: ")
# una variable puede guardar un if 
"""
print(palabra)
print("hola mundo")
"""

# pytho deja hacer un if dentro de un mensaje de texto 
"""
print("vamos a ", "piscina" if palabra == "sol" else "el cine")
"""
"""tablero = [[1,2],[2,2]]

def mostrar_tablero(tablero):

    for i in tablero:
        print(i, end=" ")

print(mostrar_tablero(tablero))"""

def crear_tablero(filas, columnas):
    tablero = [None]*filas
    for f in range(filas):
        tablero[f] = ['.']*columnas
    return tablero 

tablero = crear_tablero(7,7) 
print(len(tablero))

def mostrar_tablero(tablero):
    for num in range(len(tablero)):
        print(num, end="  ")
    for fila in tablero:
        print("")
        for casilla in fila:
            print(casilla,end="  ")
    
mostrar_tablero(tablero)