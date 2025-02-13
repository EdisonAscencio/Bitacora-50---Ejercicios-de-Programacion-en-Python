'''
Ejercicio 32: Calculadora de expresiones matemáticas

Desarrolla un programa que tome una expresión matemática 
ingresada por el usuario y calcule su resultado. 
Puedes utilizar la función eval() para evaluar la expresión.
'''

def calcular_expresion(expresion):
    try:
        resultado = eval(expresion)
        return resultado
    except Exception as e:
        print("Error al evaluar la expresión:", e)
        return None

def main():
    print("Calculadora de Expresiones Matemáticas")
    expresion = input("Ingrese la expresión matemática: ")
    resultado = calcular_expresion(expresion)
    
    if resultado is not None:
        print("El resultado de la expresión es:", resultado)
    
main()