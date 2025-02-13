'''
Ejercicio 21: Contador de días entre fechas

Desarrolla un programa que tome dos fechas ingresadas por el usuario 
y calcule la cantidad de días que hay entre ellas.
'''

from datetime import date

print("========== CALCULADORA ENTRE FECHAS==========")

dia1 = int(input("Digite el dia de la fecha #1: "))
mes1 = int(input("Digite el mes del la fecha #1: "))
año1 = int(input("Digite el año de la fecha #1: "))

fecha_hoy = date(año1,mes1,dia1)

dia2 = int(input("Digite el dia de la fecha #2: "))
mes2 = int(input("Digite el mes del la fecha #2: "))
año2 = int(input("Digite el año de la fecha #2: "))

otra_fecha = date(año2,mes2,dia2)

diferencia = otra_fecha - fecha_hoy

print(f"La difencia de la fecha {fecha_hoy} y la fecha {otra_fecha} es de {diferencia.days} dias")