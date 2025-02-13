'''
Ejercicio 31: Juego de ahorcado

Crea el clásico juego de ahorcado, donde el usuario tiene que adivinar 
una palabra y cada letra incorrecta va dibujando partes de un ahorcado.
'''

import time, random

print(" JUEGO DEL AHORCADO ")

def seleccionar_palabras():
    palabras = ["python", "programacion", "computadora", "desarrollo", "inteligencia",
                "aplicacion", "tecnologia", "algoritmo", "ingenieria", "informatica",
                "programador", "herramienta", "aprendizaje", "proyecto", "aplicativo",
                "sistema", "analisis", "datos", "lenguaje", "estructura"]
    return random.choice(palabras)

def mostrar_tablero(palabra_secreta, letras_adivinadas):
    tablero = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero+=letra
        else:
            tablero+= "_"
    print(tablero)
    
def juego_ahorcado():
    palabra_secreta = seleccionar_palabras()
    letras_adivinadas = []
    intentos_restantes = 5
    
    while intentos_restantes > 0:
        mostrar_tablero(palabra_secreta, letras_adivinadas)
        letra = input("Digite una letra: ").lower()
        
        if letra in letras_adivinadas:
            print("Ya digitaste esta letra, intenta con otra...")
            continue
        
        if letra in palabra_secreta:
            letras_adivinadas.append(letra)
            if set(letras_adivinadas) == set(palabra_secreta):
                print(f"¡Felicidades! has acertado la palabra '{palabra_secreta}'. Ganaste...")
                break
        else:
            intentos_restantes-=1
            print(f"Letra incorrecta, te quedan {intentos_restantes} intentos...")
    if intentos_restantes == 0:
        print(f"Has perdido. la palabra era '{palabra_secreta}'...")
        
juego_ahorcado()
