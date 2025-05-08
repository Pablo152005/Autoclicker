import pyautogui
import time

# Esperar 5 segundos antes de iniciar el autoclicker
time.sleep(5)

# Realizar 10 clics en la ubicación (100, 200) con un intervalo de 0.1 segundos entre clics
for i in range(10):
    pyautogui.click(x=100, y=200)
    time.sleep(0.1)
