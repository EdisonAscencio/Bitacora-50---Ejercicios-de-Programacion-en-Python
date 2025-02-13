'''
Ejercicio 3: Conversor de temperatura

Escribe un programa que convierta la temperatura de grados Celsius a Fahrenheit. 
El usuario debe ingresar la temperatura en Celsius.
'''

celsius = input('Digite la temperatura en grados Celsius: ')

conversion = (int(celsius)*(9/5))+32

print(f"La convesion de {celsius}°C a Fahrenheit es: {conversion}°F")