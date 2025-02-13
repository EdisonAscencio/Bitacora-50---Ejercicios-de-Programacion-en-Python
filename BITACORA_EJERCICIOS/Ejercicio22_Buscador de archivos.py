'''
Ejercicio 22: Buscador de archivos

Escribe un programa que busque archivos con una extensión 
específica en un directorio dado por el usuario.
'''

import os

def buscar_archivos(directorio, extension):
    """
    Función para buscar archivos con una extensión específica en un directorio dado.

    Args:
    - directorio (str): Ruta del directorio donde se realizará la búsqueda.
    - extension (str): Extensión de archivo que se está buscando.

    Returns:
    - archivos_encontrados (list): Lista de rutas completas de los archivos encontrados.
    """
    archivos_encontrados = []  # Lista para almacenar las rutas de los archivos encontrados

    # Recorrer el directorio y sus subdirectorios de manera recursiva
    for raiz, directorios, archivos in os.walk(directorio):
        for archivo in archivos:
            # Verificar si el archivo tiene la extensión buscada
            if archivo.endswith(extension):
                # Agregar la ruta completa del archivo a la lista de archivos encontrados
                archivos_encontrados.append(os.path.join(raiz, archivo))

    return archivos_encontrados


def main():
    """
    Función principal del programa.
    """
    print("Buscador de archivos por extensión")

    # Solicitar al usuario el directorio y la extensión de archivo a buscar
    directorio = input("Ingrese el directorio donde desea buscar archivos: ")
    extension = input("Ingrese la extensión de los archivos que está buscando (por ejemplo, '.txt', '.py'): ")

    # Validar si el directorio especificado existe
    if not os.path.isdir(directorio):
        print("El directorio especificado no existe.")
        return

    # Llamar a la función para buscar archivos en el directorio especificado
    archivos_encontrados = buscar_archivos(directorio, extension)

    # Mostrar los archivos encontrados
    if archivos_encontrados:
        print("Archivos encontrados:")
        for archivo in archivos_encontrados:
            print(archivo)
    else:
        print(f"No se encontraron archivos con la extensión '{extension}' en el directorio '{directorio}'.")

main()
