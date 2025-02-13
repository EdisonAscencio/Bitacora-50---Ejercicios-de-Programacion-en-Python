'''
Ejercicio 19: Generador de contraseñas

Crea un programa que genere contraseñas aleatorias 
con una longitud especificada por el usuario.
'''

import random

# Definición de los caracteres que pueden formar parte de la contraseña
minusculas = 'abcdefghijklmnñopqrstuvwxyz'
mayusculas = minusculas.upper()
numeros = '0123456789'
simbolos = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

# Combinación de todos los caracteres posibles para la contraseña
base = minusculas + mayusculas + numeros + simbolos

# Solicitar al usuario la longitud deseada para la contraseña
longitud = int(input("Digite la longitud de la contraseña: "))

# Generar una muestra aleatoria de la longitud especificada
muestra = random.sample(base, longitud)

# Unir los caracteres aleatorios para formar la contraseña
password = "".join(muestra)

# Imprimir la contraseña generada aleatoriamente
print("La contraseña generada es:", password)

 
