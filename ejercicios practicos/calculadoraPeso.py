peso = int(input('Ingrese su peso corporal: '))
altura = float(input('Ingrese su altura: '))

calculo = peso/(altura*altura)

if calculo < 18.5:
    print(f"su resultado fue {calculo} y estas delgado o bajo de peso")
else:
    if calculo >= 18.5 and calculo <= 24.9:
        print(f"su resultado fue de {calculo} y en un peso optimo saludable")
    else:
        if calculo >= 25.0 and calculo <=29.9:
            print(f"su resultado fue de {calculo}, esto indica que estas en sobre peso")
        else:
            if calculo >= 30.0:
                print(f"su resultado fue de {calculo}, indica que esta en obesidad")     