# codigo de front
from tkinter import *

window = Tk()

window.title('Calculadora')
window.geometry('500x500')
window.config(background = '#213141')
titulo = Label(Text='Mi primera calculadora', )

window.mainloop()

# El codigo funcional
acomulador = 0
numero1 = input('ingrese el primer numero: ')

while not numero1.isdigit():
    print('solo se admiten numeros enteros')
    numero1 = input('ingrese un numero entero: ')  
 
acomulador = float(numero1)    
        
flag = True 
while flag:
    accion = input('ingrese la operacion matematica o enter para el resultado ')
    if accion == '':
        flag = False
        print(acomulador)
        continue

    numero2 = input('ingrese el siguiente numero: ')

    while not numero2.isdigit() and not numero2 =='':
        print('solo se admiten numeros enteros')
        numero2 = input('ingrese un numero entero: ')  

    if accion == '/':          
        acomulador = acomulador / float(numero2)
    else:
        if accion == '*':
            acomulador = acomulador * float(numero2)
        else:
            if accion == '-':
                acomulador = acomulador - float(numero2)                
            else:
                if accion == '+':
                    acomulador = acomulador + float(numero2)
                else:
                    flag = False
                    print(acomulador)
