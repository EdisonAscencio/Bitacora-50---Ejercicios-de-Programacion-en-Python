'''
Ejercicio 33: Calculadora de edad

Escribe un programa que solicite al usuario su fecha de nacimiento 
y calcule su edad actual.
'''

from datetime import datetime

def calcular_edad(fecha_nacimiento):
    fecha_actual = datetime.today()
    edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad

def main():
    print("CALCULADORA DE EDAD")
    fecha_str = input("Ingrese su fecha de nacimiento (formato: dd/mm/aa): ")
    
    try:
        fecha_nacimiento = datetime.strptime(fecha_str, "%d/%m/%Y")
        edad = calcular_edad(fecha_nacimiento)
        print("Su edad es:", edad, "años")
    except ValueError:
        print("Formato de fecha incorrecto. Por favor, ingrese la fecha en el formato correcto (dd/mm/aaaa).")

main()