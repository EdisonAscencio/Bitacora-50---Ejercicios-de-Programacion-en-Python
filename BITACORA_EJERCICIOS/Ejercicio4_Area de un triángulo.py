'''
Ejercicio 4: Área de un triángulo

Dado un triángulo con base y altura,
escribe un programa que calcule y muestre su área.
'''

base = input('Digite la base del triangulo: ')
altura = input('Digite la altura del triangulo: ')

area = (int(base)*int(altura))/2

print(f'El triangulo con base {base} m y altura {altura} m tiene una area de {area} m²')