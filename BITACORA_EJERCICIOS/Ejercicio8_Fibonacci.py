'''
Ejercicio 8: Fibonacci

Crea un programa que genere los primeros 10 
términos de la secuencia de Fibonacci.
'''

a,b = 0,1

print("La lista de los primeros 10 números en la serie de fibonacci son: ")

for _ in range(10):  # Puedes usar _ como una convención cuando no usas la variable de bucle
    print(a, end=' ')
    a, b = b, a + b
    


