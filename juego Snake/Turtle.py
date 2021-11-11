import turtle
import time

screen = turtle.Screen()
screen.title('Esto es el titulo de la ventana')
screen.bgcolor('green')
screen.setup(width=1000, height=600)

t = turtle.Turtle()

t.goto(150,5)
t.goto(-100,-30)
t.speed(0)
t.goto(200,30)
t.shape("circle")
t.color("red")
t.penup()
t.write("Esto es un texto ", align="center", font=("Courier",24,"normal"))

t2 = turtle.Turtle()
t2.sety(t2.ycor()+100)
t.forward(20)

def move():
    t2.sety(t2.ycor()-20)

move()

screen.listen()
screen.onkeypress(move, "s")

while True:
    screen.update()
    time.sleep(0.1)

screen.mainloop()
turtle.mainloop()