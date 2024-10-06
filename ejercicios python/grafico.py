from ursina import Ursina, Entity, color

# Crear la aplicación Ursina
app = Ursina()

# Crear un cubo rojo en 3D
cubo = Entity(model='cube', color=color.red, scale=(1, 1, 1), position=(0, 0, 0))

# Función para actualizar el cubo (animación)
def update():
    cubo.rotation_y += 1  # Hacer rotar el cubo en el eje Y

# Ejecutar la aplicación
app.run()

