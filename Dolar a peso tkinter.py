import tkinter as tk

class Conversor:
    def __init__(self, tasa_dolar):
        self.tasa_dolar = tasa_dolar

    def pasar_a_pesos(self, cantidad): 
        return cantidad * self.tasa_dolar

    def pasar_a_dolar(self, cantidad): 
        return cantidad / self.tasa_dolar

conversor = Conversor(3900)

def convertir():
    cantidad = float(cantidad_input.get())
    operacion = operacion_var.get()

    if operacion == 1:
        resultado = conversor.pasar_a_pesos(cantidad)
        resultado_label.config(text=f"{cantidad} dólares son {resultado} pesos")
    elif operacion == 2:
        resultado = conversor.pasar_a_dolar(cantidad)
        resultado_label.config(text=f"{cantidad} pesos son {resultado} dólares")
    else:
        resultado_label.config(text="Opción incorrecta")

# Crear la ventana principal
root = tk.Tk()
root.title("Conversor de monedas")

# Crear los widgets
cantidad_label = tk.Label(root, text="A cuanto está el dolar:")
cantidad_input = tk.Entry(root)
operacion_var = tk.IntVar()
operacion_label = tk.Label(root, text="Operación:")
dolares_a_pesos_radio = tk.Radiobutton(root, text="Dólares a pesos", variable=operacion_var, value=1)
pesos_a_dolares_radio = tk.Radiobutton(root, text="Pesos a dólares", variable=operacion_var, value=2)
convertir_button = tk.Button(root, text="Convertir", command=convertir)
resultado_label = tk.Label(root, text="")

# Colocar los widgets en la ventana
cantidad_label.grid(row=0, column=0)
cantidad_input.grid(row=0, column=1)
operacion_label.grid(row=1, column=0)
dolares_a_pesos_radio.grid(row=1, column=1)
pesos_a_dolares_radio.grid(row=1, column=2)
convertir_button.grid(row=2, column=1)
resultado_label.grid(row=3, column=0, columnspan=2)

# Iniciar el bucle de eventos
root.mainloop()
