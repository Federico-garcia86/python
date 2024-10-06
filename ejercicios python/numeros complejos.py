import numpy as np
import matplotlib.pyplot as plt

# Función que verifica si un punto en el plano complejo pertenece al conjunto de Mandelbrot
def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

# Parámetros del gráfico
ancho, alto = 800, 800
xmin, xmax = -2.5, 1.5
ymin, ymax = -2.0, 2.0
max_iter = 100

# Crear la cuadrícula de números complejos
real = np.linspace(xmin, xmax, ancho)
imag = np.linspace(ymin, ymax, alto)
mandelbrot_set = np.zeros((alto, ancho))

# Iterar sobre cada punto en el plano complejo
for i in range(ancho):
    for j in range(alto):
        c = complex(real[i], imag[j])
        mandelbrot_set[j, i] = mandelbrot(c, max_iter)

# Mostrar el fractal de Mandelbrot
plt.imshow(mandelbrot_set.T, extent=[xmin, xmax, ymin, ymax], cmap='hot')
plt.colorbar()
plt.title("Conjunto de Mandelbrot")
plt.show()
