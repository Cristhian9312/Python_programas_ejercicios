from numpy.random.mtrand import randn, random
import pandas 
import sys
import numpy as np

d = {
    'Nombres':['cristhian','santiago','yeison'],
    'Apellidos': ['carrero','marino','gomez']
    }

df = pandas.DataFrame(d)
print(df)
#print(sys.path)

a = np.zeros((2,4))# crea una lista con listas dentro
print(a)
print(a.shape)# regresa la cantidad de sublistas que tiene y los elementos por ellas
print(a.ndim)# regresa la cantidad de sublistas
print(a.size)# regresa el tamaño total de elementos que tiene a lista principal
b = np.ones((2,4,5))# regresa un array de 3 y iniciados con 1s
print(b)
c = np.full((4,4,4),9)# regresa la cantidad de arrays tridimencional y con el numero o lo que se quiera llenar
print(c)
d = np.linspace(0,6,10)
print(d)
e = np.random.rand(2,1,5)
print(e)
"""
import matplotlib.pyplot as plt
#%matplotlib.inline

f = np.random.randn(100000000)
plt.hist(c, bins=200)
print(plt.show())
"""
lista = np.array([[5,4,7,8,6],[4,2,5,8,5]])
print(lista[0][1])
print(lista[1, :])# muestra todos los elementos de la primera lista interna
print(lista[0:2,2])#accedeal 3er elemeto de las primeras filas 
array1 = np.arange(25)# me crea 24 valores dentro del array
print(array1)
#print(array1.shape(7,4))#cambiar las dimensiones del array 

array2 = np.arange(24,49)
print(array2)
print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)
array4 = np.arange(5,)
array5 = np.array([3])
print(array4)
print(array5)
print(array4+array5)
print(array4-array5)
print(array4*array5)
print(array4/array5)

array6 = [[1,2,3],[4,5,6]] #np.full((2,3),np.arange(3,))
print(array6)
array7 = [7,8,9] #np.arange(2)
print(array7)
print(array6+array7)

print(array2.mean())# regresa la media de todo el array 
print(array2.sum())#me da la suma de todo el arra 
print(dir(array2))# muestra todas las opciones que se pueden hacer con arrays

#---------------- funciones universales 

print(np.square(array2))# me regresa los cuadrados de todos los elementos de un array
print(np.sqrt(array2))#funcion raiz cuadrada
print(np.exp(array2))#exponencial
print(np.log(array2))#logaritmos 
