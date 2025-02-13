'''
Ejercicio 18: Contador de palabras repetidas

Escribe un programa que tome una oración y cuente cuántas 
veces aparece cada palabra en ella.
'''

def palabra_repetidas(frase):
    
    frase = frase.lower() # Convertimos toda la frase a minusculas 
    
    # Definimos los signos de puntuación que queremos eliminar
    signos_puntuacion = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    # Eliminamos los signos de puntuación de la frase
    for caracter in frase:
        if caracter in signos_puntuacion:
            frase = frase.replace(caracter, " ")
    
    contador = {} # Diccionario para almacenar las palabras
    
    palabras = frase.split() # Separa cada palabra por espacio y lo vuelve lista

    for palabra in palabras:
        if palabra in contador: # Si la palabra ya está en el diccionario, incrementamos su frecuencia
            contador[palabra] += 1
        else:
            contador[palabra] = 1 # Si la palabra no está en el diccionario, la agregamos con frecuencia 1
        
    return contador

frase = input("Ingrese una oración: ")

frecuencias = palabra_repetidas(frase)

# Mostramos el resultado
print("Frecuencia de palabras:")
for palabra, frecuencia in frecuencias.items():
    print(f"La palabra '{palabra}' aparece {frecuencia} veces.")