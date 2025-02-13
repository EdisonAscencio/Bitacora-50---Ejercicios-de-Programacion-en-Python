'''
Ejercicio 45: Ruleta de casino  

Crea un programa que simule una ruleta de casino.  
Debe permitir al usuario apostar por números, colores o secciones,  
girar la ruleta y mostrar el resultado de la apuesta.
'''

import random

print("BIENVENIDO AL JUEGO DE LA RULETA")

# Definir colores antes de la función
color_rojo = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}
color_negro = {2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35}

def determinar_color(numero):
    if numero in color_rojo:
        return 'rojo'
    elif numero in color_negro:
        return 'negro'
    else:
        return 'verde'

Game = True

try:
    while Game:
        try:
            tipo_apuesta = int(input(
            '''
            ¿Qué tipo de apuesta quiere realizar?:

                1. Números individuales (0 - 36)
                2. Colores (rojo o negro)
                3. Secciones (pares, impares, docenas)
                4. Salir del programa
            
            Digite el número de la opción: '''))

            numero_ruleta = random.randint(0, 36)

            if tipo_apuesta == 1:
                numeros = list(map(int, input("Introduce los números separados por comas: ").split(",")))

                if numero_ruleta in numeros:
                    print(f"¡Ganaste! El número es {numero_ruleta} {determinar_color(numero_ruleta)}")
                else:
                    print(f"¡Perdiste! El número es {numero_ruleta} {determinar_color(numero_ruleta)}")

            elif tipo_apuesta == 2:
                respuesta_color = int(input("Apuesta por color: (1) Rojo, (2) Negro: "))

                if (respuesta_color == 1 and numero_ruleta in color_rojo) or (respuesta_color == 2 and numero_ruleta in color_negro):
                    print(f"¡Ganaste! El número es {numero_ruleta} {determinar_color(numero_ruleta)}")
                else:
                    print(f"¡Perdiste! El número es {numero_ruleta} {determinar_color(numero_ruleta)}")

            elif tipo_apuesta == 3:
                respuesta_secciones = int(input("Secciones: (1) Pares, (2) Impares, (3) Docenas: "))

                if (respuesta_secciones == 1 and numero_ruleta % 2 == 0) or (respuesta_secciones == 2 and numero_ruleta % 2 == 1):
                    print(f"¡Ganaste! El número es {numero_ruleta} {determinar_color(numero_ruleta)}")
                elif respuesta_secciones == 3:
                    docenas = {1: range(1, 13), 2: range(13, 25), 3: range(25, 37)}
                    respuesta_docenas = int(input("Elige una docena (1: 1-12, 2: 13-24, 3: 25-36): "))
                    
                    if respuesta_docenas in docenas and numero_ruleta in docenas[respuesta_docenas]:
                        print(f"¡Ganaste! El número es {numero_ruleta} {determinar_color(numero_ruleta)}")
                    else:
                        print(f"¡Perdiste! El número es {numero_ruleta} {determinar_color(numero_ruleta)}")

            elif tipo_apuesta == 4:
                Game = False
                print("\nJuego terminado. ¡Gracias por jugar!")

            else:
                print("Opción inválida, intente nuevamente...")

        except ValueError:
            print("Entrada inválida. Por favor ingrese un número válido.")

except KeyboardInterrupt:
    print("\nJuego terminado. ¡Gracias por jugar!")
