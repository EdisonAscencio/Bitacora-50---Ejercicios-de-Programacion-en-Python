'''
Ejercicio 20: Piedra, papel o tijera

Implementa el juego clásico de piedra, papel o tijera. 
El programa debe permitir al usuario jugar contra la computadora.
'''

import random

def jugar():
    
    opciones = ['PIEDRA','PAPEL','TIJERAS']
    computadora_resultado = opciones[random.randint(0,2)]
    
    mensaje_bienvenida = '''
    ¡BIENVENIDO AL JUEGO DE PIEDRA-PAPEL-TIJERAS!
    
    Selecciona una opción:
    
    1. PIEDRA
    2. PAPEL
    3. TIJERAS
    '''
    
    print(mensaje_bienvenida)
    
    try:
        usuario_resultado = int(input("Por favor digite una opción: "))
        
        while (usuario_resultado != 1) and (usuario_resultado != 2) and (usuario_resultado != 3):
            usuario_resultado = int(input("¡Por favor digite una opción del 1 al 3!: "))
        
        print(logica_juego(
            usuario_resultado = usuario_resultado,
            computadora_resultado = computadora_resultado,
            opciones = opciones)
        )
        
    except ValueError:
        print("*****UNICAMENTE PUEDES UTILIZAR UNA OPCIÓN DEL 1 AL 3, POR FAVOR REINICIA EL PROGRAMA...*****")   
        
def logica_juego(usuario_resultado,computadora_resultado,opciones):
    EMPATE = 'EMPATE'
    PERDER = 'PERDISTE...'
    GANAR = '¡GANASTE!'
    PIEDRA = 'PIEDRA'
    PAPEL = 'PAPEL'
    TIJERAS = 'TIJERAS'
    
    if usuario_resultado == 1:
        usuario_resultado = PIEDRA
        print(f"JUGADOR: {usuario_resultado} vs PC: {computadora_resultado}")
        
        if computadora_resultado == opciones[0]:
            return EMPATE
        if computadora_resultado == opciones[1]:
            return PERDER
        if computadora_resultado == opciones[2]:
            return GANAR
        
    if usuario_resultado == 2:
        usuario_resultado = PAPEL
        print(f"JUGADOR: {usuario_resultado} vs PC: {computadora_resultado}")
        
        if computadora_resultado == opciones[0]:
            return GANAR
        if computadora_resultado == opciones[1]:
            return EMPATE
        if computadora_resultado == opciones[2]:
            return PERDER
        
    if usuario_resultado == 3:
        usuario_resultado = TIJERAS
        print(f"JUGADOR: {usuario_resultado} vs PC: {computadora_resultado}")
        
        if computadora_resultado == opciones[0]:
            return PERDER
        if computadora_resultado == opciones[1]:
            return GANAR
        if computadora_resultado == opciones[2]:
            return EMPATE
        

jugar()

'''
Otra forma corte de hacer el juego:

import random

def juego_ppt():
    opciones = ["piedra", "papel", "tijera"]
    
    # Elegir la opción del usuario
    print("Elige una opción: piedra, papel o tijera")
    usuario = input().lower()
    
    # Validar la opción del usuario
    if usuario not in opciones:
        print("Opción no válida. Por favor, elige entre piedra, papel o tijera.")
        return
    
    # Elegir la opción de la computadora
    computadora = random.choice(opciones)
    
    # Mostrar las opciones elegidas
    print(f"Tú elegiste: {usuario}")
    print(f"La computadora eligió: {computadora}")
    
    # Determinar el ganador
    if usuario == computadora:
        print("¡Es un empate!")
    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijera" and computadora == "papel"):
        print("¡Ganaste!")
    else:
        print("¡La computadora gana!")

# Jugar al juego
juego_ppt()

'''