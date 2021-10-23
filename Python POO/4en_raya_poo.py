#from IPython.display import clear_output

from IPython.display import clear_output

class cuatroEnRaya:
    def __init__(Self, filas, columnas):
        Self._filas = filas
        Self._columnas = columnas
        Self._tablero = Self._crear_tablero()
        Self._turno=None
    
    def _crear_tablero(Self):
        tablero = [None]*Self._filas
        for f in range(Self._filas):
            tablero[f] = ['.']*Self._columnas
        return tablero  
    
    def _mostrar_tablero(Self):
        for num in range(Self._columnas):
            print(num, end="  ") 
        for fila in Self._tablero:
            print("")
            for casilla in fila:
                print(casilla, end="  ")
        return ""
    
    def _introducir_ficha(self, columna, color):     
        if columna >= self._columnas or columna < 0:
            print("ERROR: Numero de columna fuera del rango.")
            return
        elif self._tablero[0][columna] != '.':
            print("ERROR: La columna esta llena de fichas")
            return
        else:
            for fila in range(self._filas-1, -1, -1):
                if self._tablero[fila][columna] == '.':
                    self._tablero[fila][columna] = color  
                    return 

    def _revisar_filas(Self, color):
        for fila in range(Self._filas):
            for columna in range(Self._columnas - 3):
                if Self._tablero[fila][columna] == color and Self._tablero[fila][columna+1] == color and Self._tablero[fila][columna+2] == color and Self._tablero[fila][columna+3] == color:
                    return True
    
    def _revisar_columnas(Self, color):
        for columna in range(Self._columnas):
            for fila in range(Self._filas - 3):
                if Self._tablero[fila][columna] == color and Self._tablero[fila+1][columna] == color and Self._tablero[fila+1][columna] == color and Self._tablero[fila+1][columna] == color:
                    return True
    
    def _revisar_diagonal_derecha(Self, color):
        for columna in range(Self._columnas - 3):
            for fila in range(Self._filas -1, 2, -3):
                if Self._tablero[fila][columna] == color and Self._tablero[fila-1][columna+1] == color and Self._tablero[fila-2][columna+2] == color and Self._tablero[fila-3][columna+3] == color:
                    return True

    def _revisar_diagonal_izquierda(Self, color):
        for columna in range(Self._columnas -1, -2, -1):
            for fila in range(Self._filas -1, 2, -3):
                if Self._tablero[fila][columna] == color and Self._tablero[fila-1][columna-1] == color and Self._tablero[fila-2][columna-2] == color and Self._tablero[fila-3][columna-3] == color:
                    return True    
    
    def comprobar_ganador(Self, color):
        return Self._revisar_filas(color) or Self._revisar_columnas(color) or Self._revisar_diagonal_derecha(color) or Self._revisar_diagonal_izquierda(color) 

    def jugar(Self, player1 = 'X', player2 = 'O'):
        Self._turno = player2
        while True:
            Self._turno = player1 if Self._turno == player2 else player2
            Self._mostrar_tablero()
            columna = int(input(f"\n\nTurno del jugador {Self._turno}"))
            Self._introducir_ficha(columna, Self._turno)
            clear_output(wait=False)
            if Self.comprobar_ganador(Self._turno):
                print(f"\n Ganador el jugador {Self._turno}")
                Self._mostrar_tablero()
                break

juego = cuatroEnRaya(4,7)
juego.jugar()
