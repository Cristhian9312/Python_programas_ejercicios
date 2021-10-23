diccionario1 = {'amarillo','azul','rojo'}
diccionario2 = {'uno','dos','tres'}
diccionario1.intersection(diccionario2)# regresa lo que se repeite en ambos
list(diccionario1.union(diccionario2))# une y convierte los dos diccionarios en una lista    
diccionario1.symmetric_difference(diccionario2)#regresa lo que no se repite en ambos diccionarios 

mio = {
    'key1':1,
    'key2':2
}

mio.update({'key1':10})#agrega y edita lo que tenga el diccionario y agrega el nuevo elemento
mio.pop("key1")#Extrae y elimina del diccionario el valor de esa posicion
diccionario3 = mio.copy()#hace una copia del diccionario 
mio.clear()#elimina lo que tenga el diccionario

#----- acceso a los elementos del diccionario 
mio2 = {
    'key1':1,
    'key2':2,
    'key3':3,
    'key4':4
}

mio2.values()#regresa todos los valores de las claves sin ver la clave
mio2.keys()#regresa el nombre de las claves sin los valores
mio2.items()#regresa como lista los elementos del diccionario para poderlo meter dentro de un for 
for key,value in mio2.items():
    print("{} -> {}".format(key,value))
