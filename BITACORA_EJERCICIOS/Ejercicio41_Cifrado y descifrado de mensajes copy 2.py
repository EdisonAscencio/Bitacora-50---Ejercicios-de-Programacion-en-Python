'''
Ejercicio 41: Cifrado y descifrado de mensajes

Implementa un programa que permita al usuario cifrar y descifrar 
mensajes utilizando algún algoritmo sencillo como el cifrado César.
'''

def cifrar_mensaje(mensaje, desplazamiento):
    mensaje_cifrado = ""
    for caracter in mensaje:
        if caracter.isalpha():  # Verificamos si es una letra
            if caracter.islower():  # Si es minúscula
                nueva_letra = chr((ord(caracter) - ord('a') + desplazamiento) % 26 + ord('a'))
            elif caracter.isupper():  # Si es mayúscula
                nueva_letra = chr((ord(caracter) - ord('A') + desplazamiento) % 26 + ord('A'))
            mensaje_cifrado += nueva_letra
        else:
            # Si no es una letra, no la modificamos
            mensaje_cifrado += caracter
    return mensaje_cifrado


def descifrar_mensaje(mensaje, desplazamiento):
    # Descifrar es lo mismo que cifrar pero con desplazamiento negativo
    return cifrar_mensaje(mensaje, -desplazamiento)

while True:
    print("\n--- Cifrado César ---")
    print("1. Cifrar mensaje")
    print("2. Descifrar mensaje")
    print("3. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        mensaje = input("Escribe el mensaje a cifrar: ")
        desplazamiento = int(input("Introduce el desplazamiento (número): "))
        cifrado = cifrar_mensaje(mensaje, desplazamiento)
        print(f"Mensaje cifrado: {cifrado}")

    elif opcion == "2":
        mensaje = input("Escribe el mensaje a descifrar: ")
        desplazamiento = int(input("Introduce el desplazamiento (número): "))
        descifrado = descifrar_mensaje(mensaje, desplazamiento)
        print(f"Mensaje descifrado: {descifrado}")

    elif opcion == "3":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")