'''
Ejercicio 15: Buscar elementos comunes

Escribe un programa que encuentre los elementos comunes 
entre dos listas ingresadas por el usuario.
'''

elementos_lista1 = input("Ingrese una lista 1 de elementos separados por un espacio: ")

lista = [int(elementos) for elementos in elementos_lista1.split()]

elementos_lista2 = input("Ingrese una lista 2 de elementos separados por un espacio: ")

lista2 = [int(elementos) for elementos in elementos_lista2.split()]

print("La lista 1 de elementos es: ", lista)
print("La lista 2 de elementos es: ", lista2)

# Encuentra los elementos comunes utilizando conjuntos
conjunto1 = set(lista)
conjunto2 = set(lista2)
elementos_comunes = conjunto1.intersection(conjunto2)

print(f"Los elementos comunes entre las listas son: {list(elementos_comunes)}")
