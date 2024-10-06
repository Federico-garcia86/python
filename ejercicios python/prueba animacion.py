from ursina import *
import random

app = Ursina()

# Cargar texturas para los dados (asegúrate de tener estas imágenes en la carpeta correcta)
texturas_dados = [
    load_texture('cara1.png'),  # Asegúrate de tener estas imágenes
    load_texture('cara2.png'),
    load_texture('cara3.png'),
    load_texture('cara4.png'),
    load_texture('cara5.png'),
    load_texture('cara6.png')
]

def lanzar_dado():
    return random.randint(0, 5)  # Devuelve un índice de 0 a 5

def crear_dado(position=(0, 0, 0), cara=0):
    return Entity(model='cube', texture=texturas_dados[cara], position=position)

# Crear los dados
dado1 = crear_dado(position=(-1, 0, 0), cara=lanzar_dado())
dado2 = crear_dado(position=(1, 0, 0), cara=lanzar_dado())

def lanzar():
    global dado1, dado2
    dado1.cara = lanzar_dado()  # Cambia la cara del dado 1
    dado2.cara = lanzar_dado()  # Cambia la cara del dado 2
    dado1.texture = texturas_dados[dado1.cara]  # Actualiza la textura del dado 1
    dado2.texture = texturas_dados[dado2.cara]  # Actualiza la textura del dado 2
    print(f"Has lanzado: {dado1.cara + 1} y {dado2.cara + 1}!")

# Añadir un botón para lanzar los dados
boton_lanzar = Button(text='Lanzar Dados', scale=(0.1, 0.1), position=(-0.5, -0.5), color=color.azure)

def actualizar():
    if boton_lanzar.hovered and held_keys['left mouse']:
        lanzar()

app.run()