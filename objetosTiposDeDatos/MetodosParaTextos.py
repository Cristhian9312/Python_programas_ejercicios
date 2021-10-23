texto = ("hola mundo")
print(dir(texto))

# metodos que tienen los objetos de tipo texto
texto2 = "HoLa MuNdO"
print(texto.capitalize())
texto2.lower()
texto2.upper()
texto2.title()
texto2.swapcase()

#----- Buscar y reemplazar
texto3 = "aoo boo coo doo"
texto3.count("oo")#muestra la cantidad de veces que se repite
texto3.find("boo")#busca en la cadena de texto y regresa la posicion donde encontro la coincidencia
texto3[4:4 + len('boo')]
texto3.rfind("boo")# busca en la cadena de texto de antras hacia adelante

#----- Clasificacion de caracteres 
texto4 = "123abc"
texto5 = "123$!$bc"
texto4.isalnum()#veriifica si los caracteres son alfanumericos y regresa true o false
texto5.isdigit()#verifica si lo que hay son solo numeros

#----- String format
texto6 = "Hola mundo"
texto6.center(20)# centra el texto segun la cantidad de caracteres que se quiera a los lados
texto6.ljust(30)#crea una cadena de 30 caracteres y lo identa a la isquierda dejando ese campo al lado 
texto7 = "             espacios       en         el          texto                "
texto7.rstrip()#quita los espacios en la parte izquierda
texto7.lstrip()#quita los espacios en la parte derecha
texto7.strip()#quita todos los espacios que existen en la cadena
texto7.replace(" ","")#busca lo que se le dio primero y lo remplaza por lo 2do
texto7.zfill(30)#si la cadena de texto no cumple la cantidad de caracteres, remplaza los faltantes por 0
",".join(["Azul","Rojo","Amarillo"])#concatena el string inicial con cada elemento de la lista
"{}-{}-{}".format(3,"hola",[2,3])#ingresa cada elemento en orden dentro de los corchetes
