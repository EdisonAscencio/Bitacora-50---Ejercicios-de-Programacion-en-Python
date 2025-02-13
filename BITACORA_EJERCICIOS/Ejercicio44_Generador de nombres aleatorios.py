'''
Ejercicio 43: Generador de nombres aleatorios

Crea un programa que genere nombres aleatorios combinando 
listas de nombres y apellidos.
'''

import random

nombres = [
    "Carlos", "Ana", "Luis", "María", "José", "Elena", "Miguel", "Laura", 
    "Fernando", "Gabriela", "Diego", "Isabel", "Santiago", "Valeria", "Andrés", 
    "Sofía", "Ricardo", "Camila", "Alejandro", "Natalia"
]

apellidos = [
    "Gómez", "Fernández", "Martínez", "Rodríguez", "Pérez", "López", "García", 
    "Ramírez", "Torres", "Sánchez", "Díaz", "Mendoza", "Castro", "Ortega", 
    "Hernández", "Silva", "Rivas", "Acosta", "Morales", "Vargas"
]

numero_nombres = int(input("Digite el número de nombres generados: "))

# Simulamos los lanzamientos del dado
for i in range(numero_nombres):
    print(f"El nombre {i+1} generado es: {random.choice(nombres)} {random.choice(apellidos)}")
10