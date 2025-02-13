'''
Ejercicio 17: Suma de matrices

Desarrolla un programa que sume dos matrices de 
tamaño 3x3 ingresadas por el usuario.
'''

Matriz_A = [[1,2,3],
            [4,5,6],
            [7,8,9]]

Matriz_B = [[9,8,7],
            [6,5,4],
            [3,2,1]]

Matriz_C = []

for fila in range(len(Matriz_A)):
    nueva_fila = []
    for columna in range(len(Matriz_A[0])):
       nueva_fila.append(Matriz_A[fila][columna] + Matriz_B[fila][columna])
    Matriz_C.append(nueva_fila)
    
for fila in range(len(Matriz_A)):
    if fila != 1:
        print(f"{Matriz_A[fila]}   {Matriz_B[fila]}   {Matriz_C[fila]}")
    else:
        print(f"{Matriz_A[fila]} + {Matriz_B[fila]} = {Matriz_C[fila]}")