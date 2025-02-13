'''
Ejercicio 9: Palíndromo

Dado un string, determina si es un palíndromo 
(se lee igual de izquierda a derecha que de derecha a izquierda).
'''

def es_palindromo(palabra):
    palabra = palabra.lower().replace(' ','')
    palabra = palabra.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
    
    return palabra == palabra[::-1]

palabra = input('Ingrese una palabra: ')

if es_palindromo(palabra):
    print(f'La palabra "{palabra}" es un palíndromo.')
else:
    print(f'La palabra "{palabra}" no es un palíndromo.')

