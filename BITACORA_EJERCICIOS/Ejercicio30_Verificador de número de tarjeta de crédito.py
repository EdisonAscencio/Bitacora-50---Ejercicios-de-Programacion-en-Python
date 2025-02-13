'''
Ejercicio 30: Verificador de número de tarjeta de crédito

Escribe un programa que valide si un número de tarjeta de crédito 
ingresado por el usuario es potencialmente válido utilizando 
el algoritmode Luhn.
'''

def validar_numero_tarjeta(numero):

    numero = numero.replace(" ", "")

    if not numero.isdigit():
        return False  # Si el número contiene caracteres que no son dígitos, retorna False

    suma = 0
    longitud = len(numero)
    parity = longitud % 2

    for i, d in enumerate(map(int, numero)):
        if i % 2 == parity:
            d *= 2
            if d > 9:
                d -= 9
        suma += d

    return suma % 10 == 0

def main():
    print("Verificador de Número de Tarjeta de Crédito")
    numero_tarjeta = input("Ingrese el número de tarjeta de crédito: ")

    if validar_numero_tarjeta(numero_tarjeta):
        print("El número de tarjeta de crédito es potencialmente válido según el algoritmo de Luhn.")
    else:
        print("El número de tarjeta de crédito no es válido según el algoritmo de Luhn.")


main()
