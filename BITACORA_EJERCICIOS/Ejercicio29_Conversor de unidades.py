'''
Ejercicio 29: Conversor de unidades

Desarrolla un programa que convierta entre diferentes unidades de medida
(por ejemplo, de kilómetros a millas o de gramos a libras).
'''

def convertir_longitud():
    print("\n1. Centímetro a Metro")
    print("2. Metro a Kilómetro")
    print("3. Metro a Pulgada")
    print("4. Pulgada a Pie")
    print("5. Kilómetro a Milla")

    opcion = int(input("Seleccione la conversión que desea realizar: "))

    if opcion == 1:
        cm = float(input("Ingrese la longitud en centímetros: "))
        print(f"{cm} centímetros son {cm / 100} metros.")
    elif opcion == 2:
        m = float(input("Ingrese la longitud en metros: "))
        print(f"{m} metros son {m / 1000} kilómetros.")
    elif opcion == 3:
        metro = float(input("Ingrese la longitud en metros: "))
        print(f"{metro} metros son {metro * 39.37} pulgadas.")
    elif opcion == 4:
        pulgadas = float(input("Ingrese la longitud en pulgadas: "))
        print(f"{pulgadas} pulgadas son {pulgadas / 12} pies.")
    elif opcion == 5:
        km = float(input("Ingrese la longitud en kilómetros: "))
        print(f"{km} kilómetros son {km * 0.621371} millas.")
    else:
        print("Opción no válida.")
    
def convertir_masa():
    print("\n1. Gramo a Kilogramo")
    print("2. Gramo a Libra")
    print("3. Kilogramo a Libra")
    print("4. Libra a Onzas")

    opcion = int(input("Seleccione la conversión que desea realizar: "))

    if opcion == 1:
        gramos = float(input("Ingrese la masa en gramos: "))
        print(f"{gramos} gramos son {gramos / 1000} kilogramos.")
    elif opcion == 2:
        gramos = float(input("Ingrese la masa en gramos: "))
        print(f"{gramos} gramos son {gramos * 0.00220462} libras.")
    elif opcion == 3:
        kilogramos = float(input("Ingrese la masa en kilogramos: "))
        print(f"{kilogramos} kilogramos son {kilogramos * 2.20462} libras.")
    elif opcion == 4:
        libras = float(input("Ingrese la masa en libras: "))
        print(f"{libras} libras son {libras * 16} onzas.")
    else:
        print("Opción no válida.")

def convertir_tiempo():
    print("\n1. Segundo a Minuto")
    print("2. Minuto a Hora")
    print("3. Hora a Días")
    print("4. Días a Meses")
    print("5. Meses a Año")

    opcion = int(input("Seleccione la conversión que desea realizar: "))

    if opcion == 1:
        segundos = float(input("Ingrese la cantidad de segundos: "))
        print(f"{segundos} segundos son {segundos / 60} minutos.")
    elif opcion == 2:
        minutos = float(input("Ingrese la cantidad de minutos: "))
        print(f"{minutos} minutos son {minutos / 60} horas.")
    elif opcion == 3:
        horas = float(input("Ingrese la cantidad de horas: "))
        print(f"{horas} horas son {horas / 24} días.")
    elif opcion == 4:
        dias = float(input("Ingrese la cantidad de días: "))
        print(f"{dias} días son {dias / 30} meses.")
    elif opcion == 5:
        meses = float(input("Ingrese la cantidad de meses: "))
        print(f"{meses} meses son {meses / 12} año(s).")
    else:
        print("Opción no válida.")
        
def main():
    print("========== CONVERSOR DE UNIDADES ==========")

    while True:
        print("\n1. Longitud")
        print("2. Masa")
        print("3. Tiempo")
        print("4. Salir")

        opcion_unidades = int(input("Seleccione la unidad para la conversión: "))

        if opcion_unidades == 1:
            convertir_longitud()
        elif opcion_unidades == 2:
            convertir_masa()
        elif opcion_unidades == 3:
            convertir_tiempo()
        elif opcion_unidades == 4:
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            
main()