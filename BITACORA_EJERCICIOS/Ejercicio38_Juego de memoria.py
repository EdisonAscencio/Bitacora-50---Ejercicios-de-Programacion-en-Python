'''
Ejercicio 38: Juego de memoria

Crea un juego de memoria en el que el programa muestra una 
secuencia de números y el usuario tiene que repetirla.
'''

import random # Importa el módulo random para generar números aleatorios.
import time # Importa el módulo time para manejar pausas temporales.
import os # Importa el módulo os para limpiar la pantalla según el sistema operativo.

def clear():
    """Limpia la pantalla."""
    os.system('cls')

print("JUEGO DE MEMORIA")
print("Memoriza la secuencia y repítela correctamente. ¡Buena suerte!")


lista_numeros = [] # Lista vacía que almacenará la secuencia de números.
Game = True

while Game:
    nuevo_numero = random.randint(1,9) # Generar un nuevo número aleatorio entre 1 y 9
    lista_numeros.append(nuevo_numero) # Agrega el número generado a la secuencia.

    print("La secuencia es:")
    for numero in lista_numeros: # Itera sobre cada número en la secuencia.
        print(numero, end=" ", flush=True)
        time.sleep(1) # Pausa de 1 segundo entre números para que el jugador pueda verlos.
    time.sleep(0.5) # Breve pausa antes de limpiar la pantalla.

    clear()

    respuesta_usuario = input("Repite la secuencia separando los números por un espacio: ")

    try:
        respuesta_lista = list(map(int, respuesta_usuario.split()))
        # La función `split()` separa la entrada en elementos usando los espacios como delimitadores.
        # `map(int, ...)` convierte cada elemento a entero, y `list(...)` crea una lista con esos valores.

        if respuesta_lista == lista_numeros:
            print("¡Correcto! Prepara la siguiente secuencia...")
            time.sleep(2)
            clear()
        else:
            # Si la respuesta es incorrecta, el juego termina.
            print("¡Incorrecto! La secuencia era:", lista_numeros)
            print(f"Sobreviviste a {len(lista_numeros) - 1} rondas.")  # Muestra cuántas rondas logró.
            Game = False  # Cambia el estado de la variable para salir del bucle.
    except ValueError:
        # Maneja errores en caso de que el usuario no ingrese números válidos.
        print("Entrada inválida. Asegúrate de ingresar números separados por espacios.")
        Game = False  # Termina el juego debido a un error de entrada.