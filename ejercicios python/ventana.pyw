import tkinter as tk

# Función para cambiar los colores de las letras
def cambiar_colores():
    global colores_actuales
    # Rota la lista de colores hacia la izquierda
    colores_actuales = colores_actuales[1:] + [colores_actuales[0]]
    
    # Actualiza el color de cada letra
    for i, letra_id in enumerate(textos):
        canvas.itemconfig(letra_id, fill=colores_actuales[i % len(colores_actuales)])
    
    # Llama a la función nuevamente después de 500 ms (0.5 segundos)
    ventana.after(500, cambiar_colores)

ventana = tk.Tk()
ventana.title("Feliz cumpleaños")
ventana.geometry("400x300")

canvas = tk.Canvas(ventana, bg="lightblue")  # Creamos un Canvas
canvas.pack(fill=tk.BOTH, expand=True)  # Lo expandimos para llenar la ventana

texto = "Feliz cumpleaños"
colores_actuales = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]  # Lista de colores
textos = []  # Lista para almacenar las referencias de los textos en el canvas

x = 50  # Posición inicial en x
y = 150  # Posición en y

for i, letra in enumerate(texto):
    # Crear el texto y almacenar su referencia
    texto_id = canvas.create_text(x, y, text=letra, font=("Arial", 20), fill=colores_actuales[i % len(colores_actuales)])
    textos.append(texto_id)  # Agregar a la lista de textos
    x += 20  # Ajusta la posición x para la siguiente letra

# Llama a la función para cambiar colores al inicio
cambiar_colores()

ventana.mainloop()


