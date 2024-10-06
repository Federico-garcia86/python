import pyautogui
import time
import subprocess
import math

# Abre Paint
subprocess.Popen('mspaint.exe')
time.sleep(2)  # Espera a que Paint abra

# Asegúrate de que Paint esté activo
pyautogui.click(x=100, y=100)  # Clic en la ventana de Paint para activarla
time.sleep(1)  # Espera un momento para asegurarse de que esté activa

# Mueve el mouse al botón de maximizar y hace clic
pyautogui.moveTo(x=1621, y=121)  # Ajusta estas coordenadas según la resolución de tu pantalla
pyautogui.click()  # Hace clic en el botón de maximizar
time.sleep(1)  # Espera un momento para asegurarse de que esté maximizado

# Asegúrate de que Paint esté activo
pyautogui.click(x=100, y=100)  # Clic en la ventana de Paint para activarla
time.sleep(1)  # Espera un momento para asegurarse de que esté activa

# Dibuja un rectángulo
pyautogui.moveTo(400, 400)  # Mueve a la posición inicial
pyautogui.mouseDown()  # Mantiene el botón del mouse presionado
pyautogui.moveTo(600, 600, duration=1)  # Dibuja un rectángulo a otra posición
pyautogui.mouseUp()  # Suelta el botón del mouse

print("Rectángulo dibujado en Paint.")
