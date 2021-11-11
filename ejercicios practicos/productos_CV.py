print("PROGRAMA DE PRODUCTOS")
entrada = True
producto_1 = 3
producto_2 = 2
producto_3 = 1
variable = 0
producto_seleccionado = 0
while entrada == True:
    
    def pregunta():        
        global a_que_producto, cantidad      
        condicion = True    
        while condicion:
            a_que_producto = input("||||| ingrese uno de los tres productos existentes |||||")
            cantidad = input("||||| ingrese una CANTIDAD aceptable |||||")
            if cantidad.isnumeric() and  a_que_producto.isnumeric():
                cantidad=int(cantidad)
                a_que_producto=int(a_que_producto)
                if cantidad < 0 or a_que_producto < 0 or a_que_producto > 4:   
                    print("CANTIDADES O PRODUCTOS ERRADOS")
                else:
                    condicion=False        
    print("\n1. Comprar producto \n2. Vender producto \n3. Ver productos \n4. Salir ")
    opcion = input("\nIngresa una opcion: ")
    
    if opcion.isnumeric():
        opcion = int(opcion)  
        if opcion > 4:
            print("\n||||| Ingrese una opcion valida |||||")        
    else:
        print("\n||||| Ingrese una opcion valida |||||")     
    
    while opcion ==1 or opcion ==2 or opcion ==3 or opcion ==4:             
        if opcion == 1:
            pregunta()
            if cantidad > 0:
                if a_que_producto == 1:                    
                    producto_1 += cantidad 
                elif a_que_producto == 2:
                    producto_2 += cantidad
                elif a_que_producto == 3:
                    producto_3 += cantidad
            print("\n|||||||||| compra exitosa ||||||||||")
            break
        elif opcion == 2:
            pregunta()
            if (cantidad <= producto_1 and cantidad >=0) or (cantidad <= producto_2 and cantidad >=0) or (cantidad <= producto_3 and cantidad >=0):
                if a_que_producto ==1:
                    producto_1 -= cantidad
                elif a_que_producto == 2:
                    producto_2 -= cantidad
                elif a_que_producto ==3:
                    producto_3-= cantidad
                print("Venta exitosa")
            else:
                print("esa cantidad no es aceptable")
            break                       
        elif opcion == 3:
            print(f"\nla cantidad de unidades existentes para producto 1 es: {producto_1} \nla cantidad de unidades existentes para producto 2 es: {producto_2} \nla cantidad de unidades existentes para producto 3 es: {producto_3} \n")
            break
        elif opcion == 4:
            entrada = False    
            break 