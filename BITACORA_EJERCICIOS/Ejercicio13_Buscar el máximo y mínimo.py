'''
Ejercicio 13: Buscar el máximo y mínimo

Crea un programa que encuentre el valor máximo 
y mínimo en una lista de números ingresada por el usuario.
'''

numeros_lista = input("Ingrese una lista de numeros separados por un espacio: ")

lista = [int(numero) for numero in numeros_lista.split()]

print("La lista de numeros es:", lista)
print(f"El numero menor es: {min(lista)}")
print(f"El numero mayor es: {max(lista)}")