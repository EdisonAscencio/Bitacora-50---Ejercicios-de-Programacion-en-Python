'''
Ejercicio 35: Calculadora de interés compuesto

Desarrolla un programa que calcule el monto final después de ciertos años,
dado un capital inicial, una tasa de interés y 
un número de períodos de tiempo.
'''

print("CALCULADORA DE INTERES COMPUESTO")

inversion_inicial = float(input("Monto de dinero que tiene disponible para inivertir inicialmente: "))
Contribucion_mensual = float(input("Monto que tiene previsto agregar cada mes: "))
Tiempo = int(input("Candidad de tiempo, en años, que tiene previsto ahorrar: "))
tasa_interes = float(input("Su tasa de interés anual estimada (en %): "))

tasa_interes_mensual = tasa_interes / 100 / 12

monto_final = inversion_inicial * (1 + tasa_interes_mensual)**(Tiempo * 12) + Contribucion_mensual * (((1 + tasa_interes_mensual)**(Tiempo * 12) - 1) / tasa_interes_mensual)

print(f"El resultado de interes compuesto que en {Tiempo} años, tendrá {monto_final:.2f} $")
