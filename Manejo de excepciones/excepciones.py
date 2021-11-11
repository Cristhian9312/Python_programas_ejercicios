
from typing import Type


try:
    print(var)
except NameError:
    var = 'hola mundo'

print(var)
#************************************************************************
print('antes del try .... \n')
try:
    print('codigo antes de la excepcion')
    10+'3'
    print('codigo de la excepcion') # lo que se coloca despues del error que rompe el codigo, no se ejecutan por que salta al excep
except TypeError:
    print('no se puede sumar un string con un numero \n')

print('despues del except ..')

#************************************************************************

try:
    10+'3'
except:
    print(' No se pueden sumar numeros con letras, sin espesificar el excep este me lo captura')

#************************************************************************

print('multiples clausulas EXCEPT')

try:
    print(variable)
except NameError:
    print('gestionando excepcion NameError')
except TypeError:
    print('gestionando Excepcion TypeError')
except ZeroDivisionError:
    print('no se puede dividir un numero entre cero 0')

#************************************************************************
# tambien se puede capturar el error en una variable y usarla para mostrar mas informacion

try:
    print(variable)
except NameError as error: 
    print('objeto de tipo', type(error))
    print('la excepcion consiste en: ' , error )

#************************************************************************
# excepciones personalizadas 

#colores_permitidos = ('azul', 'rojo', 'amarillo')
#color = 'cafe'

#if color not in colores_permitidos:
#    raise Exception(f'El color {color} no se encuentra en la lista permitida ')

#************************************************************************

pasword = input('introduce una contraseña de mas de 8 digitos: ')

assert len(pasword) > 8, 'La contraseña es menor a 8 digitos'

#************************************************************************

try:
    print(variable2)
except NameError:
    print('variable2 no estaba definida, se define con cadena "hola mundo"')
    variable2= 'hola mundo'
else: 
    print(' variable2 ya estaba definida con el valor:', variable2)

#************************************************************************

try:
    print(variable3)
except NameError:
    print('variable3 no estaba definida, se define con cadena "hola mundo"')
    variable3 = 'hola mundo'
else: 
    print(' variable2 ya estaba definida con el valor:', variable3)
finally:
    del variable3