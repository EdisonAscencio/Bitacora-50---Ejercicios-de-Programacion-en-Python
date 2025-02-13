def morse_codigo(texto):
    codigo = {
        'A': '• ⎯', 'B': '⎯ • • •', 'C': '⎯ • ⎯ •', 'D': '⎯ • •', 'E': '•',
        'F': '• • ⎯ •', 'G': '⎯ ⎯ •', 'H': '• • • •', 'I': '• •', 'J': '• ⎯ ⎯ ⎯',
        'K': '⎯ • ⎯', 'L': '• ⎯ • •', 'M': '⎯ ⎯', 'N': '⎯ •', 'O': '⎯ ⎯ ⎯',
        'P': '• ⎯ ⎯ •', 'Q': '⎯ ⎯ • ⎯', 'R': '• ⎯ •', 'S': '• • •', 'T': '⎯',
        'U': '• • ⎯', 'V': '• • • ⎯', 'W': '• ⎯ ⎯', 'X': '⎯ • • ⎯', 'Y': '⎯ • ⎯ ⎯',
        'Z': '⎯ ⎯ • •', '1': '• ⎯ ⎯ ⎯ ⎯', '2': '• • ⎯ ⎯ ⎯', '3': '• • • ⎯ ⎯',
        '4': '• • • • ⎯', '5': '• • • • •', '6': '⎯ • • • •', '7': '⎯ ⎯ • • •',
        '8': '⎯ ⎯ ⎯ • •', '9': '⎯ ⎯ ⎯ ⎯ •', '0': '⎯ ⎯ ⎯ ⎯ ⎯',
        ' ': '/'  # Separador de palabras
    }

    morse_traducido = [] 
    caracteres_invalidos = []

    for letra in texto.upper(): # Recorremos cada letra del texto y el texto lo pasamos a mayuscula
        if letra in codigo: # Si la letra esta en el diccionario
            morse_traducido.append(codigo[letra]) # Guardamos su equivalente
        else:
            caracteres_invalidos.append(letra) # Sino agregamos los caracteres invalidos

    resultado = " ".join(morse_traducido)  # Espacio entre letras y '/' para palabras

    print(f"\nLa palabra fue: {texto}")
    print(f"La traducción de '{texto}' a código Morse es:\n{resultado}")

    if caracteres_invalidos:
        print(f"\nAdvertencia: Los siguientes caracteres no fueron traducidos: {', '.join(caracteres_invalidos)}")

print("\n🔵 TRADUCTOR TEXTO A CÓDIGO MORSE 🔵")
morse_codigo(input("\nDigite la palabra que quiere traducir en código Morse: "))
