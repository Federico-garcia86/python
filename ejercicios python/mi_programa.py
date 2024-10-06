import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ventana de ejemplo")  # Título de la ventana
ventana.geometry("400x300")  # Dimensiones de la ventana (ancho x alto)

# Etiqueta dentro de la ventana
etiqueta = tk.Label(ventana, text="¡Hola desde Tkinter!", font=("Arial", 16))
etiqueta.pack(pady=20)

# Botón dentro de la ventana
def accion_boton():
    print("El botón fue presionado")

boton = tk.Button(ventana, text="Presioname", command=accion_boton)
boton.pack(pady=10)

# Iniciar el bucle de la ventana
ventana.mainloop()