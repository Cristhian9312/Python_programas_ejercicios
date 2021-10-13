from tkinter import *

window = Tk()

peso = StringVar()
altura = StringVar()
calculoimc = StringVar()

def send_data():
    peso_data=float(peso.get())
    altura_data=float(altura.get())
    calculo = peso_data/(altura_data*altura_data)

    if calculo < 18.5:
        calculoimc.set(f"su resultado fue {calculo} y estas delgado o bajo de peso")
        print(calculo)
    else:
        if calculo >= 18.5 and calculo <= 24.9:
            calculoimc.set(f"su resultado fue de {calculo} y en un peso optimo saludable")
            print(calculo)
        else:
            if calculo >= 25.0 and calculo <=29.9:
                calculoimc.set(f"su resultado fue de {calculo}, esto indica que estas en sobre peso")
                print(calculo)
            else:
                if calculo >= 30.0:
                    calculoimc.set(f"su resultado fue de {calculo}, indica que esta en obesidad")   
                    print(calculo)
 

window.title("Calculadora")#titulo de la ventana
window.geometry("500x400")#tamaño de la ventana
window.config(background = "#213141")
#window.resizable(False,False) # no permite cambiarle el tamaño a la ventan 
# aca se esta declarando el titulo y todas sus caracteristicas sin llamarlo
main_title = Label(text="Esta es una calculadora", font=("Cambria", 13), bg="#56CD63", fg=("white"), width="550", height="2" )
# se llama el title dentro del pack para que sea visible
main_title.pack() 
# aca se van a crear los label para peso y altura
username_label = Label(text="Peso", bg="#213141", fg=("white"))
username_label.place(x=22, y=70)
username_label = Label(text="Altura", bg="#213141", fg=("white"))
username_label.place(x=22, y=120)
# aca se crea el text field para peso y altura
campo_texto = Entry(textvariable=peso)
campo_texto.place(x=72, y=70)
campo_texto = Entry(textvariable=altura)
campo_texto.place(x=72, y=120)
# aca creo el boton para calcularel indice de masa corporal 
buttonCalculo = Button(borderwidth=15, text="calcular",command=send_data, width="13", height="1")
buttonCalculo.place(x=72, y=160)
#label para el resultado 
results_label = Label(text="Este sera el resultado", textvariable=calculoimc, bg="white", fg=("black"), width="63", height="10")
results_label.place(x=22, y=220)
window.mainloop()