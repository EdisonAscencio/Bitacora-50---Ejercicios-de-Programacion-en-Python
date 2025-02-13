'''
Ejercicio 16: Calculadora simple

Crea una calculadora que realice operaciones básicas 
(suma, resta, multiplicación, división) con dos números 
ingresados por el usuario.
'''

def calculadora(num1,num2):
    
    print("======================================================================================")
    print("Digite el numero de la operación que quiere realizar")
    seleccion = int(input("1. Suma, 2. Resta, 3. Multiplicación, 4. División, 5. Todas: "))
    
    suma = num1 + num2
    resta = num1 - num2
    multi = num1 * num2
    div = num1 / num2
    
    if seleccion == 1:
        print(f"El resultado de la suma del numero {num1} y {num2} es igual a {suma}")
    elif seleccion == 2:
        print(f"El resultado de la resta del numero {num1} y {num2} es igual a {resta}")
    elif seleccion == 3:
        print(f"El resultado de la multiplicación del numero {num1} y {num2} es igual a {multi}")
    elif seleccion == 4:
        print(f"El resultado de la división del numero {num1} y {num2} es igual a {div}")
    elif seleccion == 5:
        print("EL RESULTADO DE TODAS LAS OPERACIONES SON:")
        print(f"1. El resultado de la suma del numero {num1} y {num2} es igual a {suma}")
        print(f"2. El resultado de la resta del numero {num1} y {num2} es igual a {resta}")
        print(f"3. El resultado de la multiplicación del numero {num1} y {num2} es igual a {multi}")
        print(f"4. El resultado de la división del numero {num1} y {num2} es igual a {div}")
    else:
        print("***** DIGITE UNA OPCIÓN VALIDA *****")
        
        
num1 = int(input("Digite el numero 1: "))
num2 = int(input("Digite el numero 2: "))

calculadora_Operaciones = calculadora(num1,num2)
