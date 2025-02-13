'''
Ejercicio 42: Simulador de semáforo

Crea un programa que simule un semáforo. 
Cada color debe durar un tiempo configurable 
(por ejemplo, verde 5 segundos, amarillo 2 segundos, rojo 5 segundos).
'''

import time, os
from colorama import init, Fore, Style

init()

def clear():
    """Limpia la pantalla."""
    os.system('cls')

def mostrar_estado(color, tiempo):
    """Muestra el estado del semáforo con una cuenta regresiva."""
    clear()
    print(f"ESTADO DEL SEMÁFORO: {color}")
    print("El semáforo cambiará en:")
    for i in range(tiempo, 0, -1):  # Cuenta regresiva desde 'tiempo' hasta 1
        print(i, flush=True)
        time.sleep(1)

# Simulación continua del semáforo
try:
    while True:  # Bucle infinito hasta que el usuario lo detenga
        mostrar_estado(Fore.GREEN + "VERDE" + Style.RESET_ALL, 5)   # Verde dura 5 segundos
        mostrar_estado(Fore.YELLOW + "AMARILLO" + Style.RESET_ALL, 2)  # Amarillo dura 2 segundos
        mostrar_estado(Fore.RED + "ROJO" + Style.RESET_ALL, 5)   # Rojo dura 5 segundos
except KeyboardInterrupt:
    print("\nSimulación detenida por el usuario.")