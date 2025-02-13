'''
Ejercicio 40: Generador de histograma

Desarrolla un programa que tome una lista de números 
y genere un histograma visual utilizando asteriscos.
'''

# Ejercicio 40: Generador de histograma

# Pedimos al usuario que ingrese una lista de números separados por comas
entrada = input("Introduce una lista de números separados por comas (por ejemplo, 3,5,2,7): ")

# Convertimos la entrada del usuario en una lista de números enteros
# Dividimos el string por las comas y convertimos cada parte en un entero
numeros = [int(num) for num in entrada.split(",")]

# Generamos el histograma
print("\nHistograma generado:")
for numero in numeros:  # Recorremos cada número en la lista
    print("*" * numero)  # Imprimimos un número de asteriscos igual al valor del número
