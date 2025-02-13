'''
Ejercicio 49: To-Do List  

Desarrolla una lista de tareas pendientes donde  
el usuario pueda agregar, marcar como completadas  
y eliminar tareas de la lista.
'''

tareas = []

def agregar_tarea():
    tarea = input("Digite la tarea que va a ingresar: ")
    tareas.append({"descripcion": tarea, "completada": False})
    print(f"La tarea '{tarea}' fue agregada correctamente.")

def ver_tareas():
    if not tareas:
        print("Todavía no hay tareas en la lista.")
    else:
        print("\nLista de tareas:")
        for i, tarea in enumerate(tareas, 1):  # Empezamos desde 1 para que coincida con la vista del usuario
            estado = "✔" if tarea["completada"] else "✘"
            print(f"{i}. {estado} {tarea['descripcion']}")
        print("\n")

def eliminar_tarea():
    ver_tareas()
    if not tareas:
        return
    
    try:
        tarea_a_eliminar = int(input("Digite el número de la tarea a eliminar: "))
        if 1 <= tarea_a_eliminar <= len(tareas):
            tarea_eliminada = tareas.pop(tarea_a_eliminar - 1)  # Ajuste de índice
            print(f"La tarea '{tarea_eliminada['descripcion']}' ha sido eliminada.")
        else:
            print("Número de tarea inválido.")
    except ValueError:
        print("Entrada no válida, por favor ingrese un número.")

def marcar_completada():
    ver_tareas()
    if not tareas:
        return
    
    try:
        tarea_a_marcar = int(input("Digite el número de la tarea a marcar como completada: "))
        if 1 <= tarea_a_marcar <= len(tareas):
            tareas[tarea_a_marcar - 1]["completada"] = True
            print(f"La tarea '{tareas[tarea_a_marcar - 1]['descripcion']}' ha sido marcada como completada.")
        else:
            print("Número de tarea inválido.")
    except ValueError:
        print("Entrada no válida, por favor ingrese un número.")

if __name__ == "__main__":
    print("BIENVENIDO A TO-DO LIST")
    
    while True:
        print("\nSeleccione una opción:")
        print("1. Agregar una nueva tarea")
        print("2. Eliminar una tarea")
        print("3. Ver lista de tareas")
        print("4. Marcar tarea como completada")
        print("5. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            eliminar_tarea()
        elif opcion == "3":
            ver_tareas()
        elif opcion == "4":
            marcar_completada()
        elif opcion == "5":
            print("¡Gracias por usar TO-DO LIST! Hasta luego.")
            break
        else:
            print("Opción inválida, intente nuevamente.")