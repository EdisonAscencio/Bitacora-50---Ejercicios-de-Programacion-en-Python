'''
Ejercicio 25: Calculadora de Fibonacci

Mejora el programa de la secuencia de Fibonacci para que 
ahora sea una función que pueda generar los primeros n términos.
'''

a,b = 0,1

n = int(input("Ingrese el número de términos de la secuencia de Fibonacci que desea generar: "))

print("La lista de los primeros 10 números en la serie de fibonacci son: ")

for _ in range(n):  # Puedes usar _ como una convención cuando no usas la variable de bucle
    print(a, end=' ')
    a, b = b, a + b