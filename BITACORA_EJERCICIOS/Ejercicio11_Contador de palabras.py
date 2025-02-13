'''
Ejercicio 11: Contador de palabras

Crea un programa que cuente el número de palabras en 
una oración ingresada por el usuario.
'''

frase = input("Digite una frase: ")

contador_palabras = len(frase.split())

print(f'La frase "{frase}" tiene {contador_palabras} palabras')