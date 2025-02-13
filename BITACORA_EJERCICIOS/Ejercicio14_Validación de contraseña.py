'''
Ejercicio 14: Validación de contraseña

Desarrolla un programa que solicite al usuario ingresar una 
contraseña y valide si cumple con ciertos requisitos 
(longitud, presencia de números y letras).
'''

def validar_contraseña(contraseña):
    if len(contraseña) < 8:
        return False, "La contraseña debe tener al menos 8 caracteres, intente nuevamente."
    
    tiene_numero = any(i.isnumeric() for i in contraseña)
    tiene_letra = any(i.isalpha() for i in contraseña)
    
    if not tiene_numero or not tiene_letra:
        return False, "La contraseña debe contener tanto letras como numeros, intente nuevamente."
    
    return True, "¡La contraseña es valida!"

contraseña = input("Ingrese una contraseña: ")

es_valida, mensaje = validar_contraseña(contraseña)
print(mensaje)