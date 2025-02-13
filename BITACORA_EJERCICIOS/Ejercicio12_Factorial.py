'''
Ejercicio 12: Factorial

Escribe un programa que calcule el factorial 
de un número ingresado por el usuario.
'''

numero = int(input("Digite el numero que quiere calcular su factorial: "))

factorial = 1

for i in range(1, numero + 1):
        factorial *= i
    
print(f"El numero factorial de {numero}! es: {factorial}")