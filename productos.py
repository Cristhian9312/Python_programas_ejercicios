producto1 = int(input("Costo primer producto: "))
producto2 = int(input("Costo segundo producto: "))
producto3 = int(input("Costo tercer producto: "))
suma = producto1+producto2+producto3

if producto3 >= 15000:
    producto3 = producto3 - (producto3 * 0.15)
    print(f"Menos el 15% al producto 3: {producto3}")

if producto2 >= 10000:
    producto2 = producto2 - (producto2 * 0.1)
    print(f"Menos el 10% al producto 2: {producto2}")  
   
if producto1 >= 2000:
    producto1 = producto1 - (producto1 * 0.05)
    print(f"Menos el 5% al producto 1: {producto1}")

suma = producto1+producto2+producto3

if suma >= 30000:
    suma = suma - ( suma * 0.3)
    print(f"la compra total con descuento es de: {suma}")
else:
    if suma >=15000:
        suma = suma - ( suma * 0.2)
        print(f"la compra total con descuento es de: {suma}")
    else:
        if suma >= 5000:
            suma = suma - ( suma * 0.1)
            print(f"la compra total con descuento es de: {suma}")
        else:
            print(suma)


# 100 1000 2250 = 3350   8750