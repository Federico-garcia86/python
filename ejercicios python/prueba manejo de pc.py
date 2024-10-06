import pyautogui
import time
import os
import psutil

# Función para verificar si Chrome está abierto
def is_chrome_open():
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == 'chrome.exe':
            return True
    return False

# Abrir Google Chrome (ajusta la ruta si es necesario)
os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")

# Esperar hasta que Chrome esté abierto
while not is_chrome_open():
    time.sleep(1)  # Espera un segundo antes de volver a verificar

# Esperar un poco más para asegurarnos que la ventana esté lista
time.sleep(30)

# Escribir la URL de chatgpt.com
pyautogui.write("www.youtube.com.ar", interval=0.5)

# Pulsar Enter para ir al sitio web
pyautogui.press("enter")
