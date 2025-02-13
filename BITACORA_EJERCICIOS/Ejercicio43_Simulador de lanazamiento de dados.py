'''
Ejercicio 43: Simulador de lanzamiento de un dado

Crea un programa que simule el lanzamiento de un dado de seis caras. 
El usuario debe poder elegir cuántas veces quiere lanzar el dado, 
y el programa mostrará los resultados y la frecuencia de cada número.
'''

import random

print("SIMULADOR DE DADO")

resultados = []

numero_lanzamientos = int(input("Digite el número de lanzamientos del dado: "))

# Simulamos los lanzamientos del dado
for i in range(numero_lanzamientos):
    dado = random.randint(1, 6)  # Generamos un número aleatorio entre 1 y 6
    resultados.append(dado)  # Guardamos el resultado en la lista

# Función para calcular la frecuencia de cada número en la lista de resultados
def calcular_frecuencia(resultados):
    frecuencia = {}  # Diccionario para almacenar la frecuencia de cada número
    
    # Inicializamos el conteo en 0 para cada número del dado (1 al 6)
    for i in range(1, 7):
        frecuencia[i] = resultados.count(i)  # Contamos cuántas veces aparece 'i'
    
    return frecuencia

# Calculamos la frecuencia de cada número
frecuencia_resultados = calcular_frecuencia(resultados)

# Mostramos los resultados
print(f"\nEl resultado de los lanzamientos del dado fue: {resultados}")

# Mostramos la frecuencia de cada número
print(f"\nFrecuencia de cada lanzamiento (numero de lanzamientos {numero_lanzamientos}):")
for numero, cantidad in frecuencia_resultados.items():
    print(f"CARA {numero}: {cantidad} veces")
