import tkinter as tk
import requests

class Conversor:
    def __init__(self, tasas):
        self.tasas = tasas

    def convertir(self, cantidad, moneda_origen, moneda_destino): 
        return (cantidad / self.tasas[moneda_origen]) * self.tasas[moneda_destino]

def obtener_tasas():
    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    data = response.json()
    return data['rates']

def convertir():
    cantidad = float(cantidad_input.get())
    moneda_origen = moneda_origen_var.get()
    moneda_destino = moneda_destino_var.get()
    tasas = obtener_tasas()
    conversor = Conversor(tasas)
    resultado = conversor.convertir(cantidad, moneda_origen, moneda_destino)
    resultado_label.config(text=f"{cantidad} {moneda_origen} son {resultado} {moneda_destino}")

# Crear la ventana principal
root = tk.Tk()
root.title("Conversor de monedas")

# Crear los widgets
cantidad_label = tk.Label(root, text="Valor a cambiar:")
cantidad_input = tk.Entry(root)
moneda_origen_var = tk.StringVar()
moneda_origen_label = tk.Label(root, text="Moneda origen:")
moneda_origen_option = tk.OptionMenu(root, moneda_origen_var, "USD", "GBP", "PEN", "BRL", "COP")
moneda_destino_var = tk.StringVar()
moneda_destino_label = tk.Label(root, text="Moneda destino:")
moneda_destino_option = tk.OptionMenu(root, moneda_destino_var, "USD", "GBP", "PEN", "BRL", "COP")
convertir_button = tk.Button(root, text="Convertir", command=convertir)
resultado_label = tk.Label(root, text="")

# Colocar los widgets en la ventana
cantidad_label.grid(row=0, column=0)
cantidad_input.grid(row=0, column=1)
moneda_origen_label.grid(row=1, column=0)
moneda_origen_option.grid(row=1, column=1)
moneda_destino_label.grid(row=2, column=0)
moneda_destino_option.grid(row=2, column=1)
convertir_button.grid(row=3, column=1)
resultado_label.grid(row=4, column=0, columnspan=2)

# Iniciar el bucle de eventos
root.mainloop()
