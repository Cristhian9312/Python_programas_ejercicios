from operator import le
import time
import turtle
import random

class SnakeGame:
    def __init__(self, color = "green", width = 600, height = 600):
        """Inicializa los componentes del juego"""
        self._ancho = width
        self._alto = height
        self.screen = turtle.Screen() #aca ya sale el lienzo
        self.screen.title("juego Snake")
        self.screen.bgcolor(color)#se le da el color al lienzo
        self.screen.setup(width=width, height=height)# se le da el tamaño al lienzo
        self.screen.tracer(0)
        """Inicializa la serpiente"""
        self.snake = turtle.Turtle()# aca se crea la cabeza de la Snake
        self.snake.speed(0)
        self.snake.shape("square")
        self.snake.color("black")
        self.snake.penup()
        self.snake.goto(0,0)
        """Inicializar el texto que se muestra en la pantalla"""
        self.texto = turtle.Turtle()# se inicia el texto de la pantalla
        self.texto.speed(0)
        self.texto.shape("square")
        self.texto.color("white")
        self.texto.penup()
        self.texto.hideturtle()
        self.texto.goto(0, (height/2)-40)
        #inicializar la comida de la snake
        self.comida = turtle.Turtle()
        self.comida.speed(0)   
        self.comida.shape("circle")
        self.comida.color("red")
        self.comida.penup()
        self.comida.goto(0,100)
        # atributos de la clase
        self._direccion = None
        self._delay = 0.1
        self._score = 0
        self._high_score = 0
        self.snake_cuerpo = []
        # Asociacion de los movimientos y las teclas 
        self.screen.listen() 
        self.screen.onkeypress(self.arriba,"w")
        self.screen.onkeypress(self.abajo,"s")
        self.screen.onkeypress(self.isquierda,"a")
        self.screen.onkeypress(self.derecha,"d")
        #sacamos el texto por pantalla
        self._print_score()

    def arriba(self):
        """este metodo hace el movimiento para arriba"""
        if self._direccion != "abajo":
            self._direccion= "arriba"
    
    def abajo(self):
        """este metodo hace el movimiento para abajo"""
        if self._direccion != "arriba":
            self._direccion= "abajo"
    
    def isquierda(self):
        """este metodo hace el movimiento para isquierda"""
        if self._direccion != "derecha":
            self._direccion= "isquierda"

    def derecha(self):
        """este metodo hace el movimiento para derecha"""
        if self._direccion != "isquierda":
            self._direccion= "derecha"

    def muve(self):
        #obtener las coordenadas de la cabeza de la snake
        hx, hy = self.snake.xcor(), self.snake.ycor()

        #mover el cuerpo de la snake
        for i in range(len(self.snake_cuerpo)-1,0,-1):
            x = self.snake_cuerpo[i-1].xcor()
            y = self.snake_cuerpo[i-1].ycor()
            self.snake_cuerpo[i].goto(x,y)

        #mover el segmento mas cercano a la cabeza
        if len(self.snake_cuerpo)>0:
            self.snake_cuerpo[0].goto(hx, hy)

        """Se mueve la snake hacia todos los lados sumando 20 puntos"""
        if self._direccion == "arriba":
            self.snake.sety(hy+20)
        elif self._direccion == "abajo":
            self.snake.sety(hy-20)
        elif self._direccion == "isquierda":
            self.snake.setx(hx-20)
        elif self._direccion == "derecha":
            self.snake.setx(hx+20)
    
    def jugar(self):
        while True:
            self.screen.update()
            self.colision_borde()
            self.colision_comida()
            self.colision_cuerpo()
            time.sleep(self._delay)
            self.muve()
        self.screen.mainloop()

    def colision_borde(self):
        bxcor = (self._ancho // 2) - 10
        bycor = (self._alto // 2) -10
        
        if self.snake.xcor() > bxcor or self.snake.xcor() < -bxcor or  self.snake.ycor() > bycor or self.snake.ycor() < -bycor:
            self._reset()

    def colision_cuerpo(self):
        for s in self.snake_cuerpo:
            if s.distance(self.snake) < 20:
                self._reset()
        
    def colision_comida(self):
        if self.snake.distance(self.comida) < 20:
            #mover la comida a un lugar aleatorio
            bxcor = (self._ancho // 2) - 10
            bycor = (self._alto // 2) -10
            x = random.randint(-bxcor, bxcor)
            y = random.randint(-bycor, bycor)
            self.comida.goto(x,y)
            #incrementar el cuerpo de la snake
            self.incrementar_cuerpo()     
            #reducir el dalay
            self._delay -= 0.001 
            # Aumentar el score
            self._score += 10 
            self.texto.write
            self._print_score()

    def incrementar_cuerpo(self):
        segmento = turtle.Turtle()
        segmento.speed(0)
        segmento.shape('square')
        segmento.color('grey')
        segmento.penup()
        self.snake_cuerpo.append(segmento)

    def _print_score(self):
        self.texto.clear()
        self.texto.write(f"puntos: {self._score} Record: {self._high_score}", align="center", font=("currier",24,"normal")) 
    
    def _reset(self):
        time.sleep(1)
        self.snake.goto(0,0)
        self._direccion=None
        #reinicio del cuerpo de la snake
        for s in self.snake_cuerpo:
            s.ht()
        # limpiar la lista de segmentos
        self.snake_cuerpo.clear()
        # reiniciar el delay
        self._delay = 0.1
        #reiniciar el score
        if self._score > self._high_score:
            self._high_score = self._score
        self._score = 0
        self._print_score() 
    
juego_snake = SnakeGame()
juego_snake.jugar()

"""esto mueve la snake son las teclas"""

"""juego_snake.arriba() 
juego_snake.muve()
juego_snake.isquierda()
juego_snake.muve()
juego_snake.derecha()
juego_snake.muve()
juego_snake.abajo()
juego_snake.muve()"""


