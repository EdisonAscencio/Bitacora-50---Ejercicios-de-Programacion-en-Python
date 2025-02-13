'''
Ejercicio 36: Ordenamiento de palabras por longitud

Modifica el programa de ordenamiento de lista para que ordene palabras
ingresadas por el usuario por longitud, de la más corta a la más larga.
'''

palabras_lista = input("Ingrese una lista de palabras separados por un espacio: ")

lista = [(palabra) for palabra in palabras_lista.split()]

lista_ordenada = sorted(lista, key=len)

print(f"La lista original es: {lista}")
print(f"La lista ordenada por longitud es: {lista_ordenada}")