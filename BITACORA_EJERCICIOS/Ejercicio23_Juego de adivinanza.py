'''
Ejercicio 23: Juego de adivinanza

Crea un juego en el que la computadora elige un número aleatorio 
y el usuario tiene que adivinarlo. Proporciona pistas como 
"demasiado alto" o "demasiado bajo".
'''

import random

def juego_adivinanza():
    print("========== JUEGO DE ADIVINANZAS ==========")
    print("(RECUERDA QUE ENTRE MÁS GRANDE EL NÚMERO, ES MÁS DIFÍCIL EL JUEGO)")

    # Solicitar al usuario el número máximo para el juego
    numero_maximo = int(input("Selecciona el número máximo para el juego: "))

    # Generar un número aleatorio entre 0 y el número máximo seleccionado
    numero_aleatorio = random.randint(0, numero_maximo)
    intentos = 0

    while True:
        try:
            # Pedir al usuario que adivine el número
            usuario_resultado = int(input("Por favor, digita un número: "))
            intentos += 1

            # Comparar la suposición del usuario con el número aleatorio
            if usuario_resultado == numero_aleatorio:
                print(f"¡FELICIDADES, GANASTE! El número era {numero_aleatorio}.")
                break
            elif usuario_resultado > numero_aleatorio:
                print("Demasiado alto...")
            elif usuario_resultado < numero_aleatorio:
                print("Demasiado bajo...")

        except ValueError:
            print("¡Solo puedes utilizar opciones numéricas!")

    print(f"Número de intentos: {intentos}")

# Llamar a la función para comenzar el juego
juego_adivinanza()