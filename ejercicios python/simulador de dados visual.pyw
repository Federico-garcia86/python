from ursina import *
import random
import time

# Función para generar el patrón de puntos de un dado
def crear_puntos(dado, numero):
    for punto in dado.puntos:
        punto.enabled = False  # Deshabilitar todos los puntos primero

    if numero == 1:
        dado.puntos[0].enabled = True
    elif numero == 2:
        dado.puntos[1].enabled = True
        dado.puntos[2].enabled = True
    elif numero == 3:
        dado.puntos[0].enabled = True
        dado.puntos[1].enabled = True
        dado.puntos[2].enabled = True
    elif numero == 4:
        dado.puntos[1].enabled = True
        dado.puntos[2].enabled = True
        dado.puntos[3].enabled = True
        dado.puntos[4].enabled = True
    elif numero == 5:
        dado.puntos[0].enabled = True
        dado.puntos[1].enabled = True
        dado.puntos[2].enabled = True
        dado.puntos[3].enabled = True
        dado.puntos[4].enabled = True
    elif numero == 6:
        dado.puntos[1].enabled = True
        dado.puntos[2].enabled = True
        dado.puntos[3].enabled = True
        dado.puntos[4].enabled = True
        dado.puntos[5].enabled = True
        dado.puntos[6].enabled = True

# Crear los dados y sus puntos
def crear_dado(posicion, color_dado):
    dado = Entity(model='cube', color=color_dado, position=posicion, scale=0.5)

    # Crear puntos en las caras del dado
    punto1 = Entity(parent=dado, model='sphere', color=color.black, scale=0.1, position=(0, 0, 0))
    punto2 = Entity(parent=dado, model='sphere', color=color.black, scale=0.1, position=(-0.15, 0.15, 0.5))
    punto3 = Entity(parent=dado, model='sphere', color=color.black, scale=0.1, position=(0.15, -0.15, 0.5))
    punto4 = Entity(parent=dado, model='sphere', color=color.black, scale=0.1, position=(-0.15, -0.15, -0.5))
    punto5 = Entity(parent=dado, model='sphere', color=color.black, scale=0.1, position=(0.15, 0.15, -0.5))
    punto6 = Entity(parent=dado, model='sphere', color=color.black, scale=0.1, position=(-0.15, 0.15, -0.5))
    punto7 = Entity(parent=dado, model='sphere', color=color.black, scale=0.1, position=(0.15, -0.15, -0.5))

    dado.puntos = [punto1, punto2, punto3, punto4, punto5, punto6, punto7]
    return dado

# Inicializar la aplicación Ursina
app = Ursina()

# Crear dos dados en la escena
dado1 = crear_dado(posicion=(-1, 0, 0), color_dado=color.red)
dado2 = crear_dado(posicion=(1, 0, 0), color_dado=color.blue)

# Animación de los dados
def lanzar_con_animacion(dado):
    for _ in range(20):  # Simular animación con varios cambios rápidos
        resultado = random.randint(1, 6)
        crear_puntos(dado, resultado)
        time.sleep(0.05)

# Actualizar animación con la barra espaciadora
def update():
    if held_keys['space']:
        lanzar_con_animacion(dado1)
        lanzar_con_animacion(dado2)

# Cámara inicial
camera.position = (0, 0, -5)
camera.rotation_x = 30

# Instrucciones en pantalla
Text(text="Presiona espacio para lanzar los dados", position=(0, 0.45), origin=(0, 0), scale=1.5)

app.run()

