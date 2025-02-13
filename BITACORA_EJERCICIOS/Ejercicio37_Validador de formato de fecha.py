'''
Ejercicio 37: Validador de formato de fecha

Escribe un programa que valide si una fecha ingresada por el usuario 
sigue un formato específico (por ejemplo, "dd/mm/aaaa").
'''
 
import re
import calendar

fecha = input("Introduce una fecha en formato dd/mm/aaaa: ")
patron = r"^\d{2}/\d{2}/\d{4}$"

# Validar el formato de la fecha
if not re.match(patron, fecha):
    print("Formato inválido. Debes usar el formato dd/mm/aaaa.")
else:
    # Dividir la fecha en día, mes y año
    dia, mes, año = map(int, fecha.split('/'))
    
    # Validar mes y día
    if mes < 1 or mes > 12:
        print("Mes inválido.")
    elif dia < 1 or dia > calendar.monthrange(año, mes)[1]:
        print("Día inválido.")
    elif año < 1900 or año > 2025:
        print("Año inválido.")
    else:
        print("Fecha válida.")

