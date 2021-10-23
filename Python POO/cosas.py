def crear_tablero(filas, columnas):
    tablero = [None]*filas
    for f in range(filas):
        tablero[f] = ['.']*columnas
    return tablero  

def mostrar_tablero(tablero):
    for num in range(len(tablero[0])):
        print(num, end="  ") 
    for fila in tablero:
        print("")
        for casilla in fila:
            print(casilla, end="  ")


tablero = crear_tablero(6,7) 
mostrar_tablero(tablero)