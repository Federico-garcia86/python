import tkinter as tk

class Blob:
    def __init__(self, width, height, color='black', emphasis=None, highlight=0):
        self.width = width
        self.height = height
        self.color = color
        self.emphasis = emphasis
        self.highlight = highlight

class Rectangle(Blob):
    def __init__(self, width, height, color='black', emphasis=None, highlight=0):
        # Validaciones para condiciones específicas
        if (width == 0 and height == 0 and color == 'red' and emphasis == 'strong') or highlight > 100:
            raise ValueError("sorry, you lose")
        if width == 0 and height == 0 and (color == 'red' or emphasis is None):
            raise ValueError("I don't think so -- values are %s, %s" % (width, height))

        # Inicializa la clase base Blob
        super().__init__(width, height, color, emphasis, highlight)

    def area(self):
        """Calcula el área del rectángulo."""
        return self.width * self.height

    def draw(self, canvas, x, y):
        """Dibuja el rectángulo en un canvas."""
        canvas.create_rectangle(x, y, x + self.width, y + self.height, fill=self.color)

# Función para crear y dibujar un rectángulo
def create_rectangle():
    try:
        rect = Rectangle(200, 200, color='black')  # Crea un rectángulo válido
        rect.draw(canvas, 100, 50)  # Dibuja el rectángulo en el canvas
        print(f"Rectángulo creado: {rect.width}x{rect.height}, color: {rect.color}")
        print(f"Área del rectángulo: {rect.area()}")  # Imprime el área
    except ValueError as e:
        print(e)  # En caso de error, imprime el mensaje

# Crear la ventana principal
root = tk.Tk()
root.title("Dibujo de Rectángulo")

# Crear un canvas donde se dibujará el rectángulo
canvas = tk.Canvas(root, width=400, height=300, bg='blue')
canvas.pack()

# Botón para crear y dibujar el rectángulo
button = tk.Button(root, text="Crear Rectángulo", command=create_rectangle)
button.pack()

# Ejecutar el bucle principal de la aplicación
root.mainloop()
