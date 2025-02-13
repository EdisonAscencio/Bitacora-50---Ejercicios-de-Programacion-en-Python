'''
Ejercicio 28: Juego de palabras ocultas

Crea un juego en el que la computadora elige una palabra y 
el usuario tiene que adivinarla, mostrando las letras a medida 
que son adivinadas.
'''

import random

def seleccionar_palabras():
    palabras = ["python", "programacion", "computadora", "desarrollo", "inteligencia",
                "aplicacion", "tecnologia", "algoritmo", "ingenieria", "informatica",
                "programador", "herramienta", "aprendizaje", "proyecto", "aplicativo",
                "sistema", "analisis", "datos", "lenguaje", "estructura"]
    return random.choice(palabras)

def mostrar_palabra_oculta(palabra,letras_adivinadas):
    palabra_mostrada = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            palabra_mostrada += letra + " "
        else:
            palabra_mostrada += "  "
    print(palabra_mostrada)
  
def jugar():
    
    print("¡Bienvenido al Juego de Palabras Ocultas!")
    
    palabra = seleccionar_palabras()
    letras_adivinadas = []
    intentos_maximos = 7
    
    print("La palabra tiene", len(palabra),"letras.")
    mostrar_palabra_oculta(palabra,letras_adivinadas)
    
    while intentos_maximos > 0:
        letras_usuario = input("Ingrese una letra: ").lower()
        
        if letras_usuario in letras_adivinadas:
            print("¡Ya has intentado esa letra! Inténtalo de nuevo.")
            continue
        
        letras_adivinadas.append(letras_usuario)
        
        if letras_usuario not in palabra:
            intentos_maximos -= 1
            print("¡Letra incorrecta! Te quedan", intentos_maximos, "intentos.")
        else:
            print("¡Letra correcta!")
            
        mostrar_palabra_oculta(palabra, letras_adivinadas)
        
        if all(letra in letras_adivinadas for letra in palabra):
            print("¡Felicidades! Has adivinado la palabra:", palabra)
            break
        
    if intentos_maximos == 0:
        print("¡Lo siento! Te has quedado sin intentos. La palabra era:", palabra)

jugar()