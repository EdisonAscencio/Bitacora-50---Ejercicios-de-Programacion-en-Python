'''
Ejercicio 27: Calculadora de IMC

Escribe un programa que calcule el Índice de Masa Corporal (IMC) 
a partir del peso y la altura ingresados por el usuario.
'''

print(" CALCULADORA DE IMC (INDICE DE MASA CORPORAL) ")

altura = float(input("Digite su altua en metros: "))
peso = float(input("Digite su peso en kilogramos: "))

IMC = peso / altura**2


if IMC >= 1 and IMC < 18.5:
    print(f"Su indice de masa corportal es {round(IMC,2)} y esta bajo de peso.")
elif IMC >= 18.5 and IMC <= 24.9:
    print(f"Su indice de masa corportal es {round(IMC,2)} y esta en un peso saludable.")
elif IMC >= 25 and IMC <= 29.9:
    print(f"Su indice de masa corportal es {round(IMC,2)} y esta en sobrepeso.")
elif IMC >= 30:
    print(f"Su indice de masa corportal es {round(IMC,2)} y tiene obesidad.")
else:
    print(f"Su indice de masa corportal es {round(IMC,2)} es incorrecto, intente nuevamente...")
