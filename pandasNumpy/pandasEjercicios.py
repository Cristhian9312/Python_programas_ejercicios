import numpy as np
import pandas as pd

#---------- creacion de objetos series

s = pd.Series([2,4,6,8,10])#crea una lista como una tabla con su propio id
print(s)
altura = {
    'cristhian':178,
    'Santiago':175,
    'yeison':175
}
persona = {
    'Nombres':['cristhian','santiago','yeison'],
    'Apellidos': ['carrero','marino','gomez']
}
print(pd.Series(altura))# muestra el diccionario como una tabla 
print(pd.Series(altura,index=['cristhian','Santiago']))# solo me regresa lo que le pido 
print(pd.DataFrame(persona))# muestra una tabla pero por los valores de las listas iternas

a = pd.Series(30,['prueba1','prueba2','prueba3'])# le asigna el valor de 30 a los titulos asignados 
print(a)

b = pd.Series([2,1,4,5,7], index=["num1","num2","num3","num4","num5"])
print(b)
print(b["num3"])
print(b[4])
print(b*2)
temperaturas = [2.1,5.6,2.4,5.6,8.5,4.2]
c = pd.Series(temperaturas, name="temperaturas")
print(c)

# ---------------------------------------------------------
# --------------- DATA FRAME ------------------------------

persnas = {
    "peso": pd.Series([54,58,65,25,30],["santiago","cristhian","julian","juan","luis"]),
    "altura": pd.Series({"luis":165,"santiago":170,"cristhian":178,"julian":173,"juan":160}),
    "hijos": pd.Series([2,5],["pedro","luis"])
}

df = pd.DataFrame(persnas)
print(df) # muestra como tabla los datos ingresados en el diccionaro sin importar el orden ingresado, lo ordena 
df = pd.DataFrame(persnas, columns=["peso","altura"], index=["cristhian","santiago"])
print(df) # filtra como una consulta 