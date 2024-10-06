from ursina import Ursina, Entity, color

app = Ursina()

# Crear un cubo en 3D
cubo = Entity(model='cube', scale=(1, 1, 1), position=(0, 0, 0))

# Crear caras individuales con colores
def crear_cara(pos, color):
    return Entity(model='quad', color=color, scale=(1, 1), position=pos)

# Colores para cada cara (definiendo un color púrpura con opacidad)
colores = [
    color.red,      # Rojo
    color.green,    # Verde
    color.blue,     # Azul
    color.yellow,   # Amarillo
    color.orange,   # Naranja
    (0.5, 0, 0.5, 1)  # Púrpura definido como un color RGBA (con opacidad completa)
]
caras = [
    (0, 0, 0.5),  # Frontal
    (0, 0, -0.5), # Trasero
    (0, 0.5, 0),  # Arriba
    (0, -0.5, 0), # Abajo
    (-0.5, 0, 0), # Izquierda
    (0.5, 0, 0)   # Derecha
]

# Crear cada cara y almacenarlas en una lista
entidades = []
for pos, col in zip(caras, colores):
    entidad = crear_cara(pos, col)
    entidades.append(entidad)

def update():
    for cara in entidades:
        cara.rotation_y += 1  # Rotar cada cara

app.run()
