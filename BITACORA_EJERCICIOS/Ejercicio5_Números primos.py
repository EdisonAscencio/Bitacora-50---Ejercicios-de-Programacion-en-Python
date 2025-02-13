'''
Ejercicio 5: Números primos

Crea un programa que solicite al usuario un número 
y determine si es primo o no.
'''

numero = int(input("Digite un numero para determinar si es primo o no: "))

def es_primo(numero):
    """
    Verifica si un número es primo.
    """
    if numero < 2:
        return False # Los numeros menores a 2 no son primos
    for i in range(2, numero): 
        # Verificamos que el número ingresado no pueda dividirse por ningún número entre 2 y ese mismo número -1
        if numero % i == 0: 
            # Si es divisible por algún número, retornamos False y termina el bucle
            return False
    # Si termina el bucle y no fue divisible, entonces es primo
    return True

if es_primo(numero):
    print(f'El numero {numero} es primo')
else:
    print(f'El numero {numero} no es primo')
    
 