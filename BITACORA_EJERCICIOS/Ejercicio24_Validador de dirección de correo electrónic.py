'''
Ejercicio 24: Validador de dirección de correo electrónico

Desarrolla un programa que valide si una dirección de correo 
electrónico ingresada por el usuario es válida según ciertos criterios 
(presencia de "@" y "." al menos).
'''

import re

email = input("Digita tu email: ")

patron = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

resultado = re.match(patron,email)

if resultado:
    print("Dirección de correo válido")
else:
    print("Dirección de correo inválida, vuelva a intentarlo...")