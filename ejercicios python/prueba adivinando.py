import random
import time
numero = random.randint(1, 100)
print("Adivina el número que tengo, es entre 1 y 100")
mi_numero = 0
count = 0
total = 0
inicio=time.time()
while mi_numero != numero and total<=30:
    mi_numero = int(input("Ingresar un número: "))
    count += 1  # Aquí está la corrección
    fin=time.time()
    total=fin-inicio
    if mi_numero < numero:
        print(f"El número es mayor a {mi_numero}")
    elif mi_numero > numero:
        print(f"El número es menor a {mi_numero}")
    print(f"tiempo restante {int(total)}")
if mi_numero==numero: 
    print(f"¡Correcto! El número es {mi_numero}. Intentos: {count}")
    print("muy bien hecho")
else:
    print(f"fin del juego, el numero era {numero}")
input("Presiona Enter para salir...")