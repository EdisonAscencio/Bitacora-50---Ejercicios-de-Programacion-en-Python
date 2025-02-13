'''
Ejercicio 7: Contador de vocales

Escribe un programa que cuente el número de vocales 
en una palabra ingresada por el usuario.
'''

def numero_vocales(palabra):
    vocales = 'aeiouAEIOU'
    return [i for i in palabra if i in vocales]

palabra = input('Ingresa una palabra: ')

print(f'El numero de vocales en la palabra {palabra} es {len(numero_vocales(palabra))}')
