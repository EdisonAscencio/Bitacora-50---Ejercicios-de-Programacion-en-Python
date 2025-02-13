'''
Ejercicio 26: Ordenamiento de lista (personalizado)

Modifica el programa de ordenamiento de lista para que el usuario 
pueda elegir el tipo de ordenamiento (ascendente o descendente).
'''

numeros_lista = input("Ingrese una lista de numeros separados por un espacio: ")

lista = [int(numero) for numero in numeros_lista.split()]

opcion = int(input('''
        TIPO DE ORDENAMIENTO 
      
      1. ASCENTENTE
      2. DESCENDENTE
      
      Seleccione una opción para organizar la: '''))

if opcion == 1:
    lista.sort()
    print("La lista de numeros ordenadas ascendentemente es:", lista)
elif opcion == 2:
    lista.sort(reverse=True)
    print("La lista de numeros ordenadas descendentemente es:", lista)
else:
    print("***** OPCIÓN INVÁLIDA, INTENTE NUEVAMENTE... *****")
    
    
