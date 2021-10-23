#Modificar una lista
lista = ["azul","verde","rojo"]
lista.append('amarillo')#Añade cosas a la lista
lista = ["azul","verde","rojo"]
lista.extend(["morado","amarillo","rosado"])#Ingresa una lista y la concatena a la primera
lista.remove("azul")#busca de izquierda a derecha y elimina lo que encuentre
lista.reverse()#le da la vuelta a la lista
lista.pop()#elimina o corta el ultimo elemento de la lista
lista[0]="otra cosa" #remplaza lo que se iguala en la lista en esa posicion
lista2 = lista.copy() #realiza una copia y la deja en la nueva variable 
lista.clear()#limpia la lista y la deja vacia 
lista2.index("verde")# regresa el indice que tiene 
lista2.count("verde")#cuenta la cantidad de verde que encuetra en la lista