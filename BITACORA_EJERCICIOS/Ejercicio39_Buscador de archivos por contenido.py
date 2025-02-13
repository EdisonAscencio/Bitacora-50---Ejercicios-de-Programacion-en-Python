'''
Ejercicio 39: Buscador de archivos por contenido

Modifica el programa de buscador de archivos para que 
ahora pueda buscar archivos que contengan una cierta cadena de texto.
'''

import os

def buscar_archivos_por_contenido(directorio, cadena):
    """
    Busca archivos dentro de un directorio que contengan una cadena específica.

    :param directorio: Ruta del directorio donde buscar.
    :param cadena: Cadena de texto a buscar en los archivos.
    """
    # Recorremos el directorio y todos sus subdirectorios
    for root, dirs, files in os.walk(directorio):
        # Iteramos sobre cada archivo en el directorio actual
        for file in files:
            ruta_completa = os.path.join(root, file)  # Construimos la ruta completa del archivo
            try:
                # Abrimos el archivo en modo lectura
                with open(ruta_completa, "r", encoding="utf-8", errors="ignore") as f:
                    contenido = f.read()  # Leemos todo el contenido del archivo
                    if cadena in contenido:  # Verificamos si la cadena está en el contenido
                        print(f"Cadena encontrada en: {ruta_completa}")
            except (UnicodeDecodeError, FileNotFoundError, OSError):
                # Ignoramos archivos que no se puedan leer (binarios o problemas de permisos)
                print(f"No se pudo leer el archivo: {ruta_completa}")

# Entrada del usuario
print("BUSCADOR DE ARCHIVOS POR CONTENIDO")
cadena_a_buscar = input("Introduce la cadena de texto a buscar: ")
directorio_base = input("Introduce la ruta del directorio donde buscar: ")

# Verificamos que el directorio exista
if not os.path.isdir(directorio_base):
    print("El directorio no existe. Por favor, verifica la ruta.")
else:
    # Llamamos a la función para buscar archivos
    buscar_archivos_por_contenido(directorio_base, cadena_a_buscar)
