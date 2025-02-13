import random
import time

# Diccionario de colores ANSI para resaltar letras
colors = {
    'green': '\033[92m',  # Letra en la posición correcta
    'yellow': '\033[93m',  # Letra en la palabra pero en posición incorrecta
    'red': '\033[91m',  # Letra incorrecta
    'ENDC': '\033[0m'  # Reset de color
}

def color_letra(letra, color):
    """Aplica un color a una letra según el resultado del intento."""
    return colors[color] + letra + colors["ENDC"]

def obtener_palabra():
    """Elige una palabra aleatoria de 6 letras para jugar."""
    lista_palabras = [
        "tierra", "clases", "madres", "grande", "nubes", "ratón",
        "floraz", "cantos", "juegos", "casero", "veloz", "bosque"
    ]
    return random.choice(lista_palabras).lower()

# Iniciar juego
print("BIENVENIDO AL JUEGO DE WORDLE")
time.sleep(1)

# Obtener una palabra aleatoria
palabra = obtener_palabra()
intentos_maximos = 6
longitud_palabra = len(palabra)

# Crear tablero con guiones bajos
board = [["_"] * longitud_palabra for _ in range(intentos_maximos)]

game_loop_counter = 0  # Contador de intentos
ganar = False  # Estado de victoria

while not ganar and game_loop_counter < intentos_maximos:
    # Solicitar palabra al usuario
    respuesta_palabra = input(f"Intento {game_loop_counter + 1}/{intentos_maximos}. Ingresa una palabra de {longitud_palabra} letras: ").lower()

    # Verificar que la palabra ingresada tenga la longitud correcta
    while len(respuesta_palabra) != longitud_palabra:
        print(f"La palabra debe tener exactamente {longitud_palabra} letras. Inténtalo de nuevo.")
        respuesta_palabra = input("Ingresa una palabra: ").lower()

    # Verificar si la palabra es correcta
    if respuesta_palabra == palabra:
        print("\n¡Felicidades! Adivinaste la palabra correctamente.")
        ganar = True
        board[game_loop_counter] = [color_letra(l, "green") for l in respuesta_palabra]  # Colorear en verde
    else:
        # Construir la pista de colores
        pista = []
        for j in range(longitud_palabra):
            if respuesta_palabra[j] == palabra[j]:
                pista.append(color_letra(respuesta_palabra[j], "green"))  # Letra correcta en posición correcta
            elif respuesta_palabra[j] in palabra:
                pista.append(color_letra(respuesta_palabra[j], "yellow"))  # Letra correcta en posición incorrecta
            else:
                pista.append(color_letra(respuesta_palabra[j], "red"))  # Letra incorrecta

        # Actualizar el tablero con la pista de colores
        board[game_loop_counter] = pista

    # Mostrar el tablero actualizado
    print("\nTablero actual:")
    for fila in board:
        print(" ".join(fila))

    # Incrementar el contador de intentos
    game_loop_counter += 1

# Mostrar mensaje final si el usuario no adivinó
if not ganar:
    print(f"\n¡Lo siento! La palabra correcta era '{palabra}'. ¡Sigue intentándolo!")
