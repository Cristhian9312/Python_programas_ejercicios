#from IPython.display import clear_output
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

def introducir_ficha(tablero, columna, color):
    
    if columna >= len(tablero[0]) or columna < 0:
        print("ERROR: Numero de columna fuera del rango.")
        return
    elif tablero[0][columna] != '.':
        print("ERROR: La columna esta llena de fichas")
        return
    else:
        for fila in range(len(tablero)-1, -1, -1):
            if tablero[fila][columna] == '.':
                tablero[fila][columna] = color
                return tablero

def revisar_filas(tablero, color):
    numero_filas = len(tablero)
    numero_columnas = len(tablero[0])

    for fila in range(numero_filas):
        for columna in range(numero_columnas - 3):
            if tablero[fila][columna] == color and tablero[fila][columna+1] == color and tablero[fila][columna+2] == color and tablero[fila][columna+3] == color:
                return True

def revisar_columnas(tablero, color):
    numero_filas = len(tablero)
    numero_columnas = len(tablero[0])

    for columna in range(numero_columnas):
        for fila in range(numero_filas - 3):
            if tablero[fila][columna] == color and tablero[fila+1][columna] == color and tablero[fila+1][columna] == color and tablero[fila+1][columna] == color:
                return True

def revisar_diagonal_derecha(tablero, color):
    numero_filas = len(tablero)
    numero_columnas = len(tablero[0])

    for columna in range(numero_columnas - 3):
        for fila in range(numero_filas -1, 2, -3):
            if tablero[fila][columna] == color and tablero[fila-1][columna+1] == color and tablero[fila-2][columna+2] == color and tablero[fila-3][columna+3] == color:
                return True

def revisar_diagonal_izquierda(tablero, color):
    numero_filas = len(tablero)
    numero_columnas = len(tablero[0])

    for columna in range(numero_columnas -1, -2, -1):
        for fila in range(numero_filas -1, 2, -3):
            if tablero[fila][columna] == color and tablero[fila-1][columna-1] == color and tablero[fila-2][columna-2] == color and tablero[fila-3][columna-3] == color:
                return True
 
def comprobar_ganador(tablero, color):
    return revisar_filas(tablero, color) or revisar_columnas(tablero, color) or revisar_diagonal_derecha(tablero, color) or revisar_diagonal_izquierda(tablero,color) 
        
tablero = crear_tablero(6,7) 
turno ="R"
sig_turno = "A"
while True:
    columna=0
    turno=sig_turno
    mostrar_tablero(tablero)
    if turno == "R":
        columna = int(input("\n\nturno del Rojo: "))
        sig_turno = "A"
    elif turno == "A":
        columna = int(input("\n\nturno dl amarillo: "))
        sig_turno = "R"
    introducir_ficha(tablero, columna, turno)
    if comprobar_ganador(tablero, turno):
        print(f"\n*** el ganador es el jugador {turno} ***\n")
        #clear_output(wait=False)
        mostrar_tablero(tablero)
        break
        





